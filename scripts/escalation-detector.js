/**
 * escalation-detector.js
 * Detecta escalação: completada (100%) → fixup automático → decisão humana
 */

import Logger from './logger.js';

const logger = new Logger('escalation-detector');

/**
 * Verifica se todos gaps são reparáveis (fixable=true, severity≠critical)
 */
function canAutoFixGaps(gaps) {
  if (!Array.isArray(gaps) || gaps.length === 0) return false;
  return gaps.every((g) => g && g.fixable === true && g.severity !== 'critical');
}

/**
 * Normaliza score 0-100
 */
function normalizeScore(score) {
  let n = parseFloat(score);
  return isNaN(n) ? 0 : Math.max(0, Math.min(100, n));
}

/**
 * Valida entrada
 */
function validateInput(phase, score, gaps) {
  const errors = [];
  if (!phase || typeof phase !== 'string') errors.push('phase inválido');
  if (score === null || score === undefined) errors.push('score inválido');
  if (!Array.isArray(gaps)) errors.push('gaps deve ser array');
  return { valid: errors.length === 0, errors };
}

/**
 * Avalia completude de fase e retorna status de escalação
 *
 * @param {string} phase - Nome da fase
 * @param {number} score - Score 0-100
 * @param {Array<Object>} gaps - Array de { type, severity, fixable }
 *
 * @returns {Object}
 *   - score=100% → { status: 'completed', nextPhase: true }
 *   - canFixup=true → { status: 'attempting-fixup', willRetry: true }
 *   - else → { status: 'escalated', requiresHumanDecision: true }
 *   + phase, score, gaps, timestamp
 */
export function evaluatePhaseCompletion(phase, score, gaps = []) {
  const validation = validateInput(phase, score, gaps);
  if (!validation.valid) {
    logger.error('Validação falhou', { errors: validation.errors });
    throw new Error(validation.errors.join('; '));
  }

  const normalizedScore = normalizeScore(score);
  const canFixup = canAutoFixGaps(gaps);
  const isCompleted = normalizedScore === 100;

  // Branch 1: Score 100% → completed
  if (isCompleted) {
    const result = {
      status: 'completed',
      nextPhase: true,
      willRetry: false,
      requiresHumanDecision: false,
      phase,
      score: normalizedScore,
      gaps,
      timestamp: new Date().toISOString(),
    };
    logger.debug(`Fase ${phase} completada`, { score: normalizedScore });
    return result;
  }

  // Branch 2: Gaps fixáveis → attempting-fixup
  if (canFixup) {
    const result = {
      status: 'attempting-fixup',
      nextPhase: false,
      willRetry: true,
      requiresHumanDecision: false,
      phase,
      score: normalizedScore,
      gaps,
      timestamp: new Date().toISOString(),
    };
    logger.debug(`Fase ${phase} em fixup automático`, {
      score: normalizedScore,
      fixableGaps: gaps.length,
    });
    return result;
  }

  // Branch 3: Escalação necessária
  const result = {
    status: 'escalated',
    nextPhase: false,
    willRetry: false,
    requiresHumanDecision: true,
    phase,
    score: normalizedScore,
    gaps,
    timestamp: new Date().toISOString(),
  };
  logger.warn(`Fase ${phase} escalada para análise humana`, {
    score: normalizedScore,
    criticalGaps: gaps.filter((g) => g.severity === 'critical').length,
  });
  return result;
}

export default { evaluatePhaseCompletion };
