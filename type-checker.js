const { execSync } = require('child_process');
const path = require('path');

/**
 * Type-checker: Executa tsc --noEmit e retorna diagnósticos em JSON
 * @returns {{ errors: number, warnings: number, errorList: Array<{file, line, column, message, type}> }}
 */
function typeCheck() {
  let output = '';

  try {
    output = execSync('tsc --noEmit 2>&1', {
      encoding: 'utf-8',
      stdio: ['pipe', 'pipe', 'pipe'],
      maxBuffer: 10 * 1024 * 1024
    });
  } catch (error) {
    output = error.stdout || error.stderr || '';
  }

  const lines = output.split('\n').filter(l => l.trim());
  const errorList = [];
  let errorCount = 0;
  let warningCount = 0;

  // Regex: arquivo(linha,coluna): severity TSnnnn: mensagem
  const diagRegex = /^(.+?)\((\d+),(\d+)\):\s+(error|warning)\s+TS(\d+):\s+(.+)$/;

  for (const line of lines) {
    const match = line.match(diagRegex);

    if (match) {
      const [, file, lineNum, col, severity, tsCode, message] = match;
      const type = severity === 'error' ? 'error' : 'warning';

      if (type === 'error') {
        errorCount++;
      } else {
        warningCount++;
      }

      errorList.push({
        file: path.resolve(file),
        line: parseInt(lineNum, 10),
        column: parseInt(col, 10),
        code: `TS${tsCode}`,
        message: message.trim(),
        type
      });
    }
  }

  return {
    errors: errorCount,
    warnings: warningCount,
    errorList
  };
}

/**
 * CLI: Executa type-check e exibe JSON + exit code
 */
function main() {
  const result = typeCheck();
  console.log(JSON.stringify(result, null, 2));

  // Exit 1 se houver erros, 0 caso contrário
  if (result.errors > 0) {
    process.exit(1);
  }
  process.exit(0);
}

if (require.main === module) {
  main();
}

module.exports = { typeCheck };
