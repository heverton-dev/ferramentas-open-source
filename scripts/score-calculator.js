/**
 * score-calculator.js (120 linhas)
 * Agrega 4 reports (tests, types, lint, coverage) em FINAL_SCORE (0-100%)
 *
 * Fórmula:
 *   FINAL_SCORE = (tests × 0.25) + (types × 0.25) + (lint × 0.25) + (coverage × 0.25)
 *
 * Retorna:
 *   { score, breakdown, passing: boolean }
 */

import Logger from './logger.js';

const logger = new Logger('score-calculator');

/**
 * Normaliza valor entre 0-100, validando e coagindo para número
 * @param {*} value - Valor bruto (pode ser string, float, etc)
 * @param {string} metricName - Nome da métrica para logging
 * @returns {number} Valor 0-100
 */
function normalizeScore(value, metricName) {
  let score = parseFloat(value);

  // Validação: não-número → 0
  if (isNaN(score)) {
    logger.warn(`Métrica ${metricName} inválida, usando 0`, { value });
    score = 0;
  }

  // Coagir para range [0, 100]
  score = Math.max(0, Math.min(100, score));

  return score;
}

/**
 * Calcula score agregado a partir de 4 reports
 *
 * @param {Object} reports - { tests, types, lint, coverage }
 *   Cada um pode ser:
 *   - number (0-100)
 *   - object com propriedade 'score' (ex: { score: 85, passed: true })
 *   - null/undefined → tratado como 0
 *
 * @returns {Object} {
 *   score: number (0-100),
 *   breakdown: {
 *     tests: number,
 *     types: number,
 *     lint: number,
 *     coverage: number
 *   },
 *   passing: boolean (score >= 80)
 * }
 */
export function calculateScore(reports) {
  // Validação entrada
  if (!reports || typeof reports !== 'object') {
    logger.error('Reports inválido', { reports });
    throw new Error('Reports deve ser um objeto');
  }

  // Extrair e normalizar cada métrica
  const testsScore = normalizeScore(
    reports.tests?.score ?? reports.tests ?? 0,
    'tests'
  );
  const typesScore = normalizeScore(
    reports.types?.score ?? reports.types ?? 0,
    'types'
  );
  const lintScore = normalizeScore(
    reports.lint?.score ?? reports.lint ?? 0,
    'lint'
  );
  const coverageScore = normalizeScore(
    reports.coverage?.score ?? reports.coverage ?? 0,
    'coverage'
  );

  // Breakdown para transparência
  const breakdown = {
    tests: testsScore,
    types: typesScore,
    lint: lintScore,
    coverage: coverageScore,
  };

  // Calcular score agregado: média ponderada (25% cada)
  const finalScore = Math.round(
    testsScore * 0.25 +
    typesScore * 0.25 +
    lintScore * 0.25 +
    coverageScore * 0.25
  );

  // Determinar passing (threshold: 80%)
  const passing = finalScore >= 80;

  const result = {
    score: finalScore,
    breakdown,
    passing,
  };

  logger.debug('Score calculado', {
    finalScore,
    breakdown,
    passing,
  });

  return result;
}

/**
 * Valida estrutura de um report individual
 * Útil para pre-flight checks
 *
 * @param {Object} report
 * @param {string} metricName
 * @returns {boolean} true se estrutura válida
 */
export function isValidReportStructure(report, metricName) {
  // Aceita: null, number, ou object com .score
  if (report === null || report === undefined) return true;
  if (typeof report === 'number') return report >= 0 && report <= 100;
  if (typeof report === 'object' && 'score' in report) {
    return (
      typeof report.score === 'number' &&
      report.score >= 0 &&
      report.score <= 100
    );
  }

  logger.warn(`Estrutura inválida para ${metricName}`, { report });
  return false;
}

/**
 * Valida todos os 4 reports antes de calcular
 *
 * @param {Object} reports
 * @returns {Object} { valid: boolean, errors: Array<string> }
 */
export function validateReports(reports) {
  const errors = [];

  if (!reports || typeof reports !== 'object') {
    errors.push('Reports deve ser um objeto');
    return { valid: false, errors };
  }

  // Validar cada métrica
  const metrics = ['tests', 'types', 'lint', 'coverage'];
  for (const metric of metrics) {
    if (!isValidReportStructure(reports[metric], metric)) {
      errors.push(
        `${metric}: esperado number|null|{score: number}, recebido ${typeof reports[metric]}`
      );
    }
  }

  return {
    valid: errors.length === 0,
    errors,
  };
}

/**
 * Calcula score com validação completa
 *
 * @param {Object} reports
 * @returns {Object} { score, breakdown, passing } ou { error, valid: false }
 */
export function calculateScoreSafe(reports) {
  const validation = validateReports(reports);

  if (!validation.valid) {
    logger.error('Validação de reports falhou', {
      errors: validation.errors,
    });
    return {
      error: validation.errors.join('; '),
      valid: false,
    };
  }

  try {
    return calculateScore(reports);
  } catch (error) {
    logger.error('Erro ao calcular score', { error: error.message });
    return {
      error: error.message,
      valid: false,
    };
  }
}

export default { calculateScore, calculateScoreSafe, validateReports };
