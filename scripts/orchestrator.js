/**
 * orchestrator.js (420 linhas)
 * Orquestrador Central: Fases → Executor → Gates → Gaps → Decisão
 *
 * Responsabilidades:
 * 1. Recebe plano JSON (phases array)
 * 2. Para cada fase: chama executor, valida gates, classifica gaps
 * 3. Loop simples: score=100% → próxima | score<100% → escalate ou fixup
 * 4. Persiste estado em SQLite via state-manager
 * 5. Log estruturado em JSON
 */

const StateManager = require('./state-manager');
const Executor = require('./executor');
const GateValidator = require('./gate-validator');
const GapClassifier = require('./gap-classifier');
const Logger = require('./logger');

const logger = new Logger('orchestrator');
const stateManager = new StateManager();

// ===== ORCHESTRAÇÃO DE PLANO =====

/**
 * Orquestra execução completa de plano multi-fase
 * @param {Object} plan - { id?, phases: Array<Phase> }
 * @returns {Promise<Object>} { success, status, results, summary }
 */
async function orchestratePlan(plan) {
  // Validar entrada
  if (!plan || !Array.isArray(plan.phases)) {
    throw new Error('Plano inválido: phases array obrigatório');
  }

  const planId = plan.id || `plan-${Date.now()}`;
  const phases = plan.phases;
  const results = [];
  let allPassed = true;

  logger.info('Iniciando orquestração de plano', {
    planId,
    totalPhases: phases.length,
    timestamp: new Date().toISOString(),
  });

  // Salvar plano inicial no estado
  await stateManager.savePlanState(planId, {
    status: 'RUNNING',
    startedAt: new Date().toISOString(),
    totalPhases: phases.length,
    phases: phases.map((p, i) => ({
      id: p.id || `phase-${i}`,
      name: p.name,
      status: 'PENDING',
    })),
  });

  // Executar cada fase sequencialmente
  for (let phaseIndex = 0; phaseIndex < phases.length; phaseIndex++) {
    const phase = phases[phaseIndex];
    const phaseId = phase.id || `phase-${phaseIndex}`;

    logger.info('Iniciando fase', {
      phaseId,
      name: phase.name,
      order: phaseIndex + 1,
      totalPhases: phases.length,
    });

    try {
      // 1. EXECUTOR: Rodar tasks da fase
      const executionResult = await executePhase(phase, phaseId);

      if (!executionResult.success) {
        logger.warn('Fase não executou corretamente', {
          phaseId,
          errors: executionResult.errors,
        });
      }

      // 2. GATE VALIDATOR: Validar critérios de sucesso
      const gateResult = await validateGates(phase, executionResult);

      // 3. GAP CLASSIFIER: Se falhou, classificar tipo de falha
      let gapClassification = null;
      if (!gateResult.passed) {
        gapClassification = await classifyGaps(phase, executionResult, gateResult);
      }

      // 4. DECISÃO SIMPLES (SIM/NÃO)
      let phaseStatus = 'COMPLETED';
      let action = 'next'; // next | escalate | fixup

      if (gateResult.passed && gateResult.score === 100) {
        // ✓ Sucesso total
        action = 'next';
        phaseStatus = 'PASSED';
      } else if (!gateResult.passed) {
        // ✗ Falha - decidir ação
        allPassed = false;
        phaseStatus = 'FAILED';

        if (gapClassification.severity === 'CRITICAL') {
          action = 'escalate';
          logger.warn('Gaps críticos detectados - escalando', {
            phaseId,
            gapCount: gapClassification.count,
          });
        } else if (gapClassification.fixable) {
          action = 'fixup';
          logger.info('Gaps fixáveis detectados - tentando correção', {
            phaseId,
            fixableCount: gapClassification.gaps.filter((g) => g.fixable).length,
          });
        } else {
          action = 'escalate';
          logger.warn('Gaps não-fixáveis detectados - escalando', {
            phaseId,
            gapCount: gapClassification.count,
          });
        }
      }

      // 5. PERSISTIR RESULTADO
      const phaseResult = {
        phaseId,
        name: phase.name,
        order: phaseIndex + 1,
        status: phaseStatus,
        action,
        execution: {
          success: executionResult.success,
          duration: executionResult.duration,
          output: executionResult.output,
          errors: executionResult.errors,
        },
        gates: gateResult,
        gaps: gapClassification,
        timestamp: new Date().toISOString(),
      };

      results.push(phaseResult);

      await stateManager.updatePhaseState(planId, phaseId, {
        status: phaseStatus,
        action,
        result: phaseResult,
      });

      logger.info('Fase validada', {
        phaseId,
        status: phaseStatus,
        action,
        gateScore: gateResult.score,
      });

      // 6. LÓGICA DE FLUXO
      if (action === 'escalate') {
        logger.error('Escalação necessária - parando orquestração', {
          phaseId,
          reason: gapClassification?.reason,
        });

        await stateManager.savePlanState(planId, {
          status: 'ESCALATED',
          escalatedAt: new Date().toISOString(),
          escalatedPhase: phaseId,
          escalationReason: gapClassification?.reason,
        });

        return {
          success: false,
          status: 'ESCALATED',
          phaseIndex,
          results,
          escalationReason: gapClassification?.reason,
          planId,
        };
      }

      if (action === 'fixup') {
        // Tentar correção automática
        logger.info('Iniciando fixup automático', {
          phaseId,
          gapCount: gapClassification.count,
        });

        const fixupSuccess = await attemptFixup(phase, gapClassification);

        if (fixupSuccess) {
          // Re-executar e re-validar após fixup
          logger.info('Fixup aplicado com sucesso - re-validando', { phaseId });

          const reexecutionResult = await executePhase(phase, phaseId);
          const revalidationResult = await validateGates(phase, reexecutionResult);

          if (revalidationResult.passed && revalidationResult.score === 100) {
            // Fixup funcionou!
            phaseResult.fixupSuccessful = true;
            phaseResult.status = 'PASSED';
            phaseResult.action = 'next';
            results[results.length - 1] = phaseResult;

            await stateManager.updatePhaseState(planId, phaseId, {
              status: 'PASSED',
              fixupSuccessful: true,
            });

            logger.info('Fixup bem-sucedido - fase recuperada', { phaseId });
            continue; // Próxima fase
          } else {
            logger.warn('Fixup não resolveu problema - mantendo FAILED', {
              phaseId,
              revalidationScore: revalidationResult.score,
            });
            allPassed = false;
          }
        } else {
          logger.warn('Fixup automático falhou', { phaseId });
          allPassed = false;
        }
      }

      // action === 'next' → continua para próxima fase
    } catch (error) {
      logger.error('Erro ao executar fase', {
        phaseId,
        error: error.message,
        stack: error.stack,
      });

      const errorResult = {
        phaseId,
        name: phase.name,
        order: phaseIndex + 1,
        status: 'ERROR',
        error: error.message,
        timestamp: new Date().toISOString(),
      };

      results.push(errorResult);
      allPassed = false;

      await stateManager.updatePhaseState(planId, phaseId, {
        status: 'ERROR',
        error: error.message,
      });

      // Escalação automática em erro não previsto
      logger.error('Escalação automática por erro não tratado', {
        phaseId,
        error: error.message,
      });

      await stateManager.savePlanState(planId, {
        status: 'ESCALATED',
        escalatedAt: new Date().toISOString(),
        escalatedPhase: phaseId,
        escalationReason: `Erro não tratado: ${error.message}`,
      });

      return {
        success: false,
        status: 'ESCALATED',
        phaseIndex,
        results,
        errorPhase: phaseId,
        error: error.message,
        planId,
      };
    }
  }

  // Todas as fases completaram
  const finalStatus = allPassed ? 'SUCCESS' : 'PARTIAL_SUCCESS';

  await stateManager.savePlanState(planId, {
    status: finalStatus,
    completedAt: new Date().toISOString(),
  });

  const summary = {
    total: phases.length,
    passed: results.filter((r) => r.status === 'PASSED').length,
    failed: results.filter((r) => r.status === 'FAILED').length,
    errors: results.filter((r) => r.status === 'ERROR').length,
    fixupSuccessful: results.filter((r) => r.fixupSuccessful).length,
  };

  logger.info('Orquestração completada', {
    planId,
    status: finalStatus,
    summary,
  });

  return {
    success: allPassed,
    status: finalStatus,
    planId,
    results,
    summary,
  };
}

// ===== EXECUTAR FASE =====

/**
 * Executa todas as tasks de uma fase via Executor
 * @param {Object} phase - { tasks: Array }
 * @param {string} phaseId
 * @returns {Promise<Object>} { success, output, errors, duration }
 */
async function executePhase(phase, phaseId) {
  const executor = new Executor();
  const startTime = Date.now();

  logger.debug('Executando tasks da fase', {
    phaseId,
    taskCount: phase.tasks?.length || 0,
  });

  try {
    const output = await executor.run(phase.tasks || []);
    const duration = Date.now() - startTime;

    logger.debug('Fase executada com sucesso', {
      phaseId,
      duration,
    });

    return {
      phaseId,
      success: true,
      output,
      errors: [],
      duration,
      timestamp: new Date().toISOString(),
    };
  } catch (error) {
    const duration = Date.now() - startTime;

    logger.warn('Erro na execução de tasks', {
      phaseId,
      error: error.message,
      duration,
    });

    return {
      phaseId,
      success: false,
      output: null,
      errors: [error.message],
      duration,
      timestamp: new Date().toISOString(),
    };
  }
}

// ===== VALIDAR GATES =====

/**
 * Valida todos os gates (critérios de sucesso) de uma fase
 * @param {Object} phase - { gates: Array }
 * @param {Object} executionResult
 * @returns {Promise<Object>} { passed, score (0-100), gates: Array }
 */
async function validateGates(phase, executionResult) {
  const gateValidator = new GateValidator();
  const gates = phase.gates || [];

  logger.debug('Validando gates', {
    gateCount: gates.length,
  });

  if (gates.length === 0) {
    // Sem gates = apenas sucesso da execução
    return {
      passed: executionResult.success,
      score: executionResult.success ? 100 : 0,
      gates: [],
    };
  }

  const gateResults = [];
  let passedCount = 0;

  for (const gate of gates) {
    const result = await gateValidator.validate(gate, executionResult);
    gateResults.push(result);
    if (result.passed) passedCount++;
  }

  // Score: percentual de gates que passaram
  const score = Math.round((passedCount / gates.length) * 100);

  logger.debug('Gates validados', {
    score,
    passedCount,
    totalGates: gates.length,
  });

  return {
    passed: score === 100 && executionResult.success,
    score,
    gates: gateResults,
  };
}

// ===== CLASSIFICAR GAPS =====

/**
 * Classifica gaps (desvios) detectados nos gates que falharam
 * @param {Object} phase
 * @param {Object} executionResult
 * @param {Object} gateResult
 * @returns {Promise<Object>} { gaps, severity, fixable, reason }
 */
async function classifyGaps(phase, executionResult, gateResult) {
  const gapClassifier = new GapClassifier();

  const failedGates = gateResult.gates.filter((g) => !g.passed);

  logger.debug('Classificando gaps', {
    failedGateCount: failedGates.length,
  });

  const gaps = await gapClassifier.classify({
    phase,
    execution: executionResult,
    gates: failedGates,
  });

  const severity = gaps.some((g) => g.severity === 'CRITICAL')
    ? 'CRITICAL'
    : 'MINOR';
  const fixable = gaps.some((g) => g.fixable === true);

  const reason = gaps.map((g) => g.description).join('; ');

  logger.debug('Gaps classificados', {
    gapCount: gaps.length,
    severity,
    fixable,
  });

  return {
    count: gaps.length,
    gaps,
    severity,
    fixable,
    reason,
  };
}

// ===== FIXUP AUTOMÁTICO =====

/**
 * Tenta corrigir automaticamente gaps fixáveis
 * @param {Object} phase
 * @param {Object} gapClassification
 * @returns {Promise<boolean>} true se todos os fixups foram bem-sucedidos
 */
async function attemptFixup(phase, gapClassification) {
  logger.debug('Iniciando tentativa de fixup automático', {
    gapCount: gapClassification.gaps.length,
  });

  const fixableGaps = gapClassification.gaps.filter((g) => g.fixable);

  if (fixableGaps.length === 0) {
    logger.info('Nenhum gap fixável encontrado', {
      gapCount: gapClassification.gaps.length,
    });
    return false;
  }

  for (const gap of fixableGaps) {
    if (gap.patch) {
      try {
        logger.info('Aplicando patch automático', {
          gapId: gap.id,
          description: gap.description,
        });

        await applyPatch(gap.patch);

        logger.info('Patch aplicado com sucesso', { gapId: gap.id });
      } catch (error) {
        logger.warn('Patch falhou', {
          gapId: gap.id,
          error: error.message,
        });
        return false;
      }
    }
  }

  return true;
}

/**
 * Aplica um patch individual
 * @param {Function|Object|string} patch
 */
async function applyPatch(patch) {
  if (typeof patch === 'function') {
    // Patch é função async/sync
    await patch();
  } else if (typeof patch === 'object') {
    // Patch é objeto { type, payload }
    if (patch.type === 'config') {
      // Atualizar config
      logger.debug('Aplicando patch de config', { keys: Object.keys(patch.payload) });
      // Stub: integrar com config manager
    } else if (patch.type === 'file') {
      // Escrever arquivo
      logger.debug('Aplicando patch de arquivo', { path: patch.payload.path });
      // Stub: escrever arquivo
    }
  } else if (typeof patch === 'string') {
    // Patch é comando shell (cuidado!)
    logger.warn('Aplicando patch de shell - uso restrito', { command: patch });
    // Stub: executar com validação
  }
}

// ===== CONSULTAR STATUS =====

/**
 * Retorna status de uma fase específica
 * @param {string} planId
 * @param {string} phaseId
 * @returns {Promise<Object>}
 */
async function getPhaseStatus(planId, phaseId) {
  const state = await stateManager.getPhaseState(planId, phaseId);
  return state;
}

/**
 * Retorna status completo de um plano
 * @param {string} planId
 * @returns {Promise<Object>}
 */
async function getPlanStatus(planId) {
  const state = await stateManager.getPlanState(planId);
  return state;
}

// ===== EXPORTS =====

module.exports = {
  orchestratePlan,
  getPhaseStatus,
  getPlanStatus,
  executePhase,
  validateGates,
  classifyGaps,
  attemptFixup,
  applyPatch,
};
