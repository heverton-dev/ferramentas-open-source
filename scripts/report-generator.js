/**
 * report-generator.js (120 linhas)
 * Gera escalation report JSON estruturado com fase, score, gaps e próximos passos
 *
 * Exports: generateEscalationReport(phase, score, gaps)
 * Retorna: { phase, score, status, reason, gaps[], nextSteps[], previousAttempts, maxReached }
 */

import Logger from './logger.js';

const logger = new Logger('report-generator');

// Mapeamento de fases válidas
const VALID_PHASES = ['planning', 'implementation', 'testing', 'deployment', 'monitoring'];

// Thresholds de score por fase
const PHASE_THRESHOLDS = {
  planning: 70,        // Mínimo 70% para avançar
  implementation: 75,  // Mínimo 75% para implementação
  testing: 80,         // Mínimo 80% para testes
  deployment: 85,      // Mínimo 85% para deploy
  monitoring: 90,      // Mínimo 90% para monitoramento
};

// Razões de escalação por faixa de score
const ESCALATION_REASONS = {
  critical: 'Pontuação crítica: requer escalação imediata',
  low: 'Pontuação baixa: necessário revisão antes de prosseguir',
  moderate: 'Pontuação moderada: identificados alguns gaps, recomenda-se correção',
  acceptable: 'Pontuação aceitável: pode prosseguir com monitoramento',
  excellent: 'Pontuação excelente: pronto para próxima fase',
};

// Sugestões de próximos passos por fase
const NEXT_STEPS_BY_PHASE = {
  planning: [
    'Revisar requisitos com stakeholders',
    'Validar escopo e cronograma',
    'Documentar critérios de sucesso',
  ],
  implementation: [
    'Executar code review detalhado',
    'Aplicar correções identificadas',
    'Executar testes unitários localmente',
  ],
  testing: [
    'Executar suite de testes completa',
    'Validar cobertura mínima (80%)',
    'Documentar casos de teste falhando',
  ],
  deployment: [
    'Preparar plano de rollback',
    'Validar ambiente de produção',
    'Comunicar timeline de deploy',
  ],
  monitoring: [
    'Configurar alertas e métricas',
    'Preparar runbook de incidents',
    'Validar logs e observabilidade',
  ],
};

/**
 * Determina status baseado em score
 * @param {number} score - 0-100
 * @returns {string} Status (critical, low, moderate, acceptable, excellent)
 */
function determineStatus(score) {
  if (score < 40) return 'critical';
  if (score < 60) return 'low';
  if (score < 75) return 'moderate';
  if (score < 90) return 'acceptable';
  return 'excellent';
}

/**
 * Valida e normaliza phase
 * @param {string} phase
 * @returns {string} Phase válida ou 'planning' (padrão)
 */
function normalizePhase(phase) {
  if (!phase || !VALID_PHASES.includes(phase)) {
    logger.warn(`Phase inválida: ${phase}, usando padrão 'planning'`);
    return 'planning';
  }
  return phase;
}

/**
 * Calcula número de tentativas baseado em histórico
 * (simula histórico: cada chamada incrementa)
 * @returns {number} Número de tentativas
 */
function calculatePreviousAttempts() {
  // Em cenário real, consultaria banco de dados
  // Aqui retorna baseado em env var para teste
  const env = parseInt(process.env.ESCALATION_ATTEMPTS || '0', 10);
  return Math.max(0, env);
}

/**
 * Determina se máximo de escalações foi atingido (threshold: 3)
 * @param {number} attempts
 * @returns {boolean}
 */
function hasReachedMax(attempts) {
  const MAX_ATTEMPTS = 3;
  return attempts >= MAX_ATTEMPTS;
}

/**
 * Gera lista de próximos passos
 * @param {string} phase
 * @param {string} status
 * @param {Array} gaps
 * @returns {Array<string>}
 */
function generateNextSteps(phase, status, gaps) {
  const baseSteps = NEXT_STEPS_BY_PHASE[phase] || [];

  // Se status crítico, adicionar escalação
  if (status === 'critical') {
    return [
      'Escalar para líder técnico imediatamente',
      'Convocar reunião de triage',
      ...baseSteps,
    ];
  }

  // Se há gaps, adicionar resolução específica
  if (gaps && gaps.length > 0) {
    return [
      `Resolver ${gaps.length} gap(s) identificado(s)`,
      ...baseSteps.slice(0, 2),
    ];
  }

  return baseSteps;
}

/**
 * Gera report estruturado de escalação
 *
 * @param {string} phase - planning|implementation|testing|deployment|monitoring
 * @param {number} score - 0-100
 * @param {Array<string>} gaps - Lista de gaps identificados
 *
 * @returns {Object} {
 *   phase: string,
 *   score: number,
 *   status: string,
 *   reason: string,
 *   gaps: Array,
 *   nextSteps: Array,
 *   previousAttempts: number,
 *   maxReached: boolean
 * }
 */
export function generateEscalationReport(phase, score, gaps = []) {
  // Validações
  const normalizedPhase = normalizePhase(phase);
  const normalizedScore = Math.max(0, Math.min(100, parseInt(score, 10) || 0));
  const normalizedGaps = Array.isArray(gaps) ? gaps : [];

  // Determinar status e razão
  const status = determineStatus(normalizedScore);
  const reason = ESCALATION_REASONS[status] || ESCALATION_REASONS.moderate;

  // Calcular tentativas prévias e verificar limite
  const previousAttempts = calculatePreviousAttempts();
  const maxReached = hasReachedMax(previousAttempts);

  // Gerar próximos passos
  const nextSteps = generateNextSteps(normalizedPhase, status, normalizedGaps);

  // Montar report
  const report = {
    phase: normalizedPhase,
    score: normalizedScore,
    status,
    reason,
    gaps: normalizedGaps,
    nextSteps,
    previousAttempts,
    maxReached,
  };

  logger.info('Escalation report gerado', {
    phase: normalizedPhase,
    score: normalizedScore,
    status,
    gapCount: normalizedGaps.length,
    maxReached,
  });

  return report;
}

/**
 * Valida estrutura do report gerado
 * @param {Object} report
 * @returns {boolean}
 */
export function isValidEscalationReport(report) {
  if (!report || typeof report !== 'object') return false;

  const required = ['phase', 'score', 'status', 'reason', 'gaps', 'nextSteps', 'previousAttempts', 'maxReached'];
  return required.every((key) => key in report);
}

export default { generateEscalationReport, isValidEscalationReport };
