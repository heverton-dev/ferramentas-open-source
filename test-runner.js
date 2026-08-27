#!/usr/bin/env node

const { execSync, spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

/**
 * test-runner.js: Executa suite de testes (npm test ou pytest) e retorna JSON estruturado.
 * Retorna: { passed, failed, duration, failures[] }
 */

function detectTestRunner() {
  const cwd = process.cwd();

  // Verifica npm/Jest
  if (fs.existsSync(path.join(cwd, 'package.json'))) {
    const pkg = JSON.parse(fs.readFileSync(path.join(cwd, 'package.json'), 'utf8'));
    if (pkg.devDependencies?.jest || pkg.scripts?.test) {
      return 'npm';
    }
  }

  // Verifica pytest
  if (fs.existsSync(path.join(cwd, 'pytest.ini')) ||
      fs.existsSync(path.join(cwd, 'setup.py')) ||
      fs.existsSync(path.join(cwd, 'pyproject.toml'))) {
    return 'pytest';
  }

  return 'npm'; // padrão
}

function runNpmTest() {
  const startTime = Date.now();
  let passed = 0, failed = 0, failures = [];

  try {
    const output = execSync('npm test -- --json 2>&1', {
      encoding: 'utf8',
      stdio: ['pipe', 'pipe', 'pipe'],
      cwd: process.cwd()
    });

    // Tenta fazer parse do JSON da saída do Jest
    const jsonMatch = output.match(/\{[\s\S]*"numPassedTests"/);
    if (jsonMatch) {
      const testResult = JSON.parse(jsonMatch[0]);
      passed = testResult.numPassedTests || 0;
      failed = testResult.numFailedTests || 0;

      // Extrai detalhes das falhas
      if (testResult.testResults) {
        testResult.testResults.forEach(file => {
          if (file.assertionResults) {
            file.assertionResults.forEach(test => {
              if (test.status === 'failed') {
                failures.push({
                  test: test.fullName || test.title,
                  error: test.failureMessages?.[0] || 'Unknown error',
                  file: file.name
                });
              }
            });
          }
        });
      }
    } else {
      // Fallback: parse simples da saída
      const passedMatch = output.match(/(\d+)\s+passed/);
      const failedMatch = output.match(/(\d+)\s+failed/);
      passed = passedMatch ? parseInt(passedMatch[1]) : 0;
      failed = failedMatch ? parseInt(failedMatch[1]) : 0;
    }
  } catch (error) {
    // Tenta extrair info do stderr
    const errorStr = error.stderr?.toString() || error.message;
    const passedMatch = errorStr.match(/(\d+)\s+passed/);
    const failedMatch = errorStr.match(/(\d+)\s+failed/);

    passed = passedMatch ? parseInt(passedMatch[1]) : 0;
    failed = failedMatch ? parseInt(failedMatch[1]) : 0;

    if (failed > 0) {
      failures.push({
        test: 'General Test Failure',
        error: errorStr.split('\n').slice(0, 3).join('\n'),
        file: 'unknown'
      });
    }
  }

  const duration = Date.now() - startTime;
  return { passed, failed, duration, failures };
}

function runPytest() {
  const startTime = Date.now();
  let passed = 0, failed = 0, failures = [];

  try {
    const result = spawnSync('pytest', ['--json-report', '--json-report-file=/tmp/pytest-report.json', '-v'], {
      encoding: 'utf8',
      cwd: process.cwd(),
      stdio: ['pipe', 'pipe', 'pipe']
    });

    // Tenta ler relatório JSON do pytest
    const reportPath = '/tmp/pytest-report.json';
    if (fs.existsSync(reportPath)) {
      const report = JSON.parse(fs.readFileSync(reportPath, 'utf8'));
      passed = report.summary?.passed || 0;
      failed = report.summary?.failed || 0;

      if (report.tests) {
        report.tests.forEach(test => {
          if (test.outcome === 'failed') {
            failures.push({
              test: test.nodeid,
              error: test.call?.longrepr || 'Unknown failure',
              file: test.nodeid.split('::')[0]
            });
          }
        });
      }
    } else {
      // Fallback: parse simples da saída
      const output = result.stdout || result.stderr || '';
      const passedMatch = output.match(/(\d+)\s+passed/);
      const failedMatch = output.match(/(\d+)\s+failed/);
      passed = passedMatch ? parseInt(passedMatch[1]) : 0;
      failed = failedMatch ? parseInt(failedMatch[1]) : 0;
    }
  } catch (error) {
    const output = error.stdout?.toString() || error.stderr?.toString() || error.message;
    const passedMatch = output.match(/(\d+)\s+passed/);
    const failedMatch = output.match(/(\d+)\s+failed/);

    passed = passedMatch ? parseInt(passedMatch[1]) : 0;
    failed = failedMatch ? parseInt(failedMatch[1]) : 0;
  }

  const duration = Date.now() - startTime;
  return { passed, failed, duration, failures };
}

function main() {
  const runner = detectTestRunner();
  let result;

  if (runner === 'npm') {
    result = runNpmTest();
  } else {
    result = runPytest();
  }

  // Retorna JSON estruturado
  console.log(JSON.stringify(result, null, 2));

  // Exit code baseado em falhas
  process.exit(result.failed > 0 ? 1 : 0);
}

main();
