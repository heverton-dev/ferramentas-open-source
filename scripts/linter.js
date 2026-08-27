#!/usr/bin/env node
/**
 * linter.js: Executa eslint, parseia resultado, retorna JSON estruturado.
 *
 * Entrada:  globs (array de padrões) ou stdin (newline-separated)
 * Saida:    {violations: N, rules: [{rule, count}], errorLines: [N, ...]}
 *
 * Uso:
 *   node scripts/linter.js src/**/*.js
 *   echo "src/index.js" | node scripts/linter.js
 *   node scripts/linter.js --fix src/**/*.js
 *
 * Garantias: determinisma (R8), idempotente (R10), exit 0 = ok.
 */

import { execSync } from "child_process";
import * as fs from "fs";

/**
 * Executa eslint com formato JSON.
 * Retorna array de resultados (objects com messages, filePath, etc).
 */
function runEslint(globs, fix = false) {
  const args = [
    "eslint",
    "--format=json",
    fix ? "--fix" : "",
    ...globs,
  ].filter(Boolean);

  try {
    const output = execSync(args.join(" "), {
      encoding: "utf-8",
      stdio: ["pipe", "pipe", "pipe"],
    });
    return JSON.parse(output || "[]");
  } catch (e) {
    // eslint retorna exit 1 se houver violacoes, nao e erro
    try {
      return JSON.parse(e.stdout || "[]");
    } catch (_) {
      throw new Error(`Falha ao parsear eslint: ${e.message}`);
    }
  }
}

/**
 * Extrai metricas dos resultados eslint.
 * Retorna: {violations: N, rules: [...], errorLines: [...]}
 */
function aggregateResults(eslintResults) {
  const ruleMap = new Map();
  const errorLines = new Set();
  let violations = 0;

  for (const file of eslintResults) {
    for (const msg of file.messages || []) {
      violations++;
      const rule = msg.ruleId || "unknown";
      ruleMap.set(rule, (ruleMap.get(rule) || 0) + 1);
      if (msg.line) errorLines.add(msg.line);
    }
  }

  return {
    violations,
    rules: Array.from(ruleMap.entries())
      .map(([rule, count]) => ({ rule, count }))
      .sort((a, b) => b.count - a.count),
    errorLines: Array.from(errorLines).sort((a, b) => a - b),
  };
}

/**
 * Valida argumentos e retorna globs.
 */
function parseArgs() {
  const args = process.argv.slice(2);
  const fix = args.includes("--fix");
  const globs = args.filter((a) => !a.startsWith("--"));
  return { globs, fix };
}

/**
 * Main: CLI + stdin, retorna JSON.
 */
async function main() {
  let globs = [];
  const { globs: cliGlobs, fix } = parseArgs();

  if (cliGlobs.length > 0) {
    globs = cliGlobs;
  } else if (!process.stdin.isTTY) {
    // Le stdin (newline-separated)
    globs = await new Promise((resolve) => {
      let data = "";
      process.stdin.setEncoding("utf-8");
      process.stdin.on("data", (chunk) => {
        data += chunk;
      });
      process.stdin.on("end", () => {
        resolve(data.trim().split("\n").filter(Boolean));
      });
    });
  }

  if (globs.length === 0) {
    console.error("Erro: forneça globs ou envie via stdin");
    process.exit(1);
  }

  try {
    const results = runEslint(globs, fix);
    const metrics = aggregateResults(results);

    console.log(JSON.stringify(metrics, null, 2));
    process.exit(metrics.violations > 0 ? 1 : 0);
  } catch (e) {
    console.error(
      JSON.stringify({
        error: e.message,
        violations: 0,
        rules: [],
        errorLines: [],
      })
    );
    process.exit(1);
  }
}

// Export para uso como modulo
export { runEslint, aggregateResults };

// CLI: invocado como script
const isMainModule =
  import.meta.url === `file://${process.argv[1]}` ||
  (process.argv[1] && process.argv[1].endsWith("linter.js"));

if (isMainModule) {
  main().catch((e) => {
    console.error(
      JSON.stringify({
        error: e.message,
        violations: 0,
        rules: [],
        errorLines: [],
      })
    );
    process.exit(1);
  });
}
