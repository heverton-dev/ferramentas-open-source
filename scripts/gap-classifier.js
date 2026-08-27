#!/usr/bin/env node
/**
 * gap-classifier.js: Classifica falhas de test, type, lint, coverage.
 *
 * Recebe 4 reports estruturados e retorna gaps[] com metadata + canAttemptFixup.
 *
 * Entrada:
 *   - testReport: { passed, failed, duration, failures: [{test, error, file}] }
 *   - typeReport: { errors, warnings, errorList: [{file, line, column, code, message}] }
 *   - lintReport: { violations, rules: [{rule, count}], errorLines: [] }
 *   - coverageReport: { actual, target, gap, status, branches: [...] }
 *
 * Saída:
 *   {
 *     gaps: [{ category, severity, count, fixable, examples }],
 *     canAttemptFixup: boolean
 *   }
 */

/**
 * Classifica falhas de teste.
 */
function classifyTestFailures(testReport) {
  if (!testReport || testReport.failed === 0) {
    return null;
  }

  const failures = testReport.failures || [];
  const examples = failures.slice(0, 3).map(f => ({
    test: f.test,
    file: f.file,
    snippet: (f.error || '').split('\n')[0].substring(0, 60)
  }));

  return {
    category: 'test-failure',
    severity: testReport.failed > 10 ? 'high' : testReport.failed > 5 ? 'medium' : 'low',
    count: testReport.failed,
    fixable: true, // testes falhando são geralmente fixáveis
    examples
  };
}

/**
 * Classifica erros de tipo TypeScript.
 */
function classifyTypeErrors(typeReport) {
  if (!typeReport || typeReport.errors === 0) {
    return null;
  }

  const errorList = typeReport.errorList || [];
  const examples = errorList.slice(0, 3).map(e => ({
    file: e.file,
    line: e.line,
    code: e.code,
    snippet: e.message.substring(0, 60)
  }));

  // Type errors: generally fixable (add type annotations, fix signatures)
  const fixable = errorList.every(e =>
    !e.code || !e.code.match(/TS(20\d\d|24\d\d)/) // excluir tipos impossíveis
  );

  return {
    category: 'type-error',
    severity: typeReport.errors > 20 ? 'high' : typeReport.errors > 5 ? 'medium' : 'low',
    count: typeReport.errors,
    fixable,
    examples
  };
}

/**
 * Classifica violações de linting.
 */
function classifyLintViolations(lintReport) {
  if (!lintReport || lintReport.violations === 0) {
    return null;
  }

  const rules = lintReport.rules || [];
  const examples = rules.slice(0, 3).map(r => ({
    rule: r.rule || 'unknown',
    count: r.count
  }));

  // Linting: geralmente fixable com --fix
  return {
    category: 'linting',
    severity: lintReport.violations > 100 ? 'high' : lintReport.violations > 20 ? 'medium' : 'low',
    count: lintReport.violations,
    fixable: true,
    examples
  };
}

/**
 * Classifica gaps de cobertura.
 */
function classifyCoverageGap(coverageReport) {
  if (!coverageReport || coverageReport.gap <= 0) {
    return null;
  }

  const branches = (coverageReport.branches || [])
    .filter(b => b.status !== 'ok')
    .slice(0, 3)
    .map(b => ({
      file: b.name,
      current: b.coverage,
      gap: coverageReport.target - b.coverage
    }));

  return {
    category: 'coverage',
    severity: coverageReport.gap > 30 ? 'high' : coverageReport.gap > 10 ? 'medium' : 'low',
    count: coverageReport.gap, // gap percentual
    fixable: branches.length > 0, // fixable se há branches específicas a cobrir
    examples: branches
  };
}

/**
 * Classifica todos os gaps a partir dos 4 reports.
 *
 * @param {object} testReport - saida de test-runner.js
 * @param {object} typeReport - saida de type-checker.js
 * @param {object} lintReport - saida de linter.js
 * @param {object} coverageReport - saida de coverage-meter.js
 *
 * @returns {object} { gaps: [...], canAttemptFixup: boolean }
 */
function classifyGaps(testReport, typeReport, lintReport, coverageReport) {
  const gaps = [];

  // Classifica cada categoria
  const testGap = classifyTestFailures(testReport);
  if (testGap) gaps.push(testGap);

  const typeGap = classifyTypeErrors(typeReport);
  if (typeGap) gaps.push(typeGap);

  const lintGap = classifyLintViolations(lintReport);
  if (lintGap) gaps.push(lintGap);

  const coverageGap = classifyCoverageGap(coverageReport);
  if (coverageGap) gaps.push(coverageGap);

  // Ordena por severity (high > medium > low)
  const severityOrder = { high: 0, medium: 1, low: 2 };
  gaps.sort((a, b) => severityOrder[a.severity] - severityOrder[b.severity]);

  const canAttemptFixup = shouldAttemptFixup(gaps);

  return {
    gaps,
    canAttemptFixup
  };
}

/**
 * Determina se vale a pena tentar corrigir automaticamente.
 *
 * Condição: TODOS os gaps devem ser:
 *   - Severity: low
 *   - Fixable: true
 *   - Linting violations: < 5 (nem contar com linting pesado)
 *
 * @param {array} gaps - array de gaps classificados
 * @returns {boolean} true se vale tentar fixup automático
 */
function shouldAttemptFixup(gaps) {
  if (gaps.length === 0) return false;

  // Verifica se todos são low severity e fixable
  const allLowAndFixable = gaps.every(g =>
    g.severity === 'low' && g.fixable
  );

  if (!allLowAndFixable) return false;

  // Verifica se linting é < 5 violations (se houver linting)
  const lintGap = gaps.find(g => g.category === 'linting');
  if (lintGap && lintGap.count >= 5) {
    return false;
  }

  return true;
}

/**
 * CLI: lê os 4 reports de stdin/arquivo e exibe resultado JSON.
 */
async function main() {
  // Simples: args = caminhos para os 4 reports
  const args = process.argv.slice(2);
  if (args.length < 4) {
    console.error('Uso: gap-classifier.js <test.json> <type.json> <lint.json> <coverage.json>');
    process.exit(1);
  }

  try {
    const fs = require('fs');
    const testReport = JSON.parse(fs.readFileSync(args[0], 'utf-8'));
    const typeReport = JSON.parse(fs.readFileSync(args[1], 'utf-8'));
    const lintReport = JSON.parse(fs.readFileSync(args[2], 'utf-8'));
    const coverageReport = JSON.parse(fs.readFileSync(args[3], 'utf-8'));

    const result = classifyGaps(testReport, typeReport, lintReport, coverageReport);
    console.log(JSON.stringify(result, null, 2));

    process.exit(result.canAttemptFixup ? 0 : 1);
  } catch (error) {
    console.error(JSON.stringify({
      error: error.message,
      gaps: [],
      canAttemptFixup: false
    }));
    process.exit(1);
  }
}

// Exports para uso como módulo
module.exports = {
  classifyGaps,
  shouldAttemptFixup
};

// CLI
if (require.main === module) {
  main();
}
