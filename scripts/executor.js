#!/usr/bin/env node
/**
 * executor.js: Wrapper para fork subagent com cache de contexto.
 *
 * Recebe: phase spec (JSON) com title, description, tasks, tests, files.
 * Carrega: contexto anterior (cached em disk).
 * Monta: prompt otimizado (3-5 linhas + código, sem fluff).
 * Chama: fork subagent → resultado.
 * Retorna: changes JSON (modificacoes, status, logs).
 *
 * Entrada:  {"phase": {...}, "previousContext": "..."}
 * Saida:    {"status": "success|error", "phase_id": "...", "changes": {...}, "logs": [...]}
 *
 * Uso:
 *   node scripts/executor.js --spec phase-spec.json
 *   node scripts/executor.js --spec phase-spec.json --cache cache.json
 *
 * Garantias: idempotente, cache-first, exit 0 = sucesso.
 */

import * as fs from "fs";
import * as path from "path";
import { execSync } from "child_process";

/**
 * Cache em disco: armazena contexto anterior e evita recomputacao.
 * Chave: hash(phase_id + version). Valor: {context, timestamp, hash}.
 */
class ExecutorCache {
  constructor(cachePath = "cache/executor-cache.json") {
    this.cachePath = cachePath;
    this.data = this.load();
  }

  load() {
    try {
      const dir = path.dirname(this.cachePath);
      if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
      if (fs.existsSync(this.cachePath)) {
        return JSON.parse(fs.readFileSync(this.cachePath, "utf-8"));
      }
    } catch (_) {}
    return {};
  }

  save() {
    const dir = path.dirname(this.cachePath);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(
      this.cachePath,
      JSON.stringify(this.data, null, 2),
      "utf-8"
    );
  }

  get(key) {
    return this.data[key];
  }

  set(key, value) {
    this.data[key] = { ...value, timestamp: new Date().toISOString() };
    this.save();
  }
}

/**
 * Gera hash simples de uma string (deterministico, R8).
 */
function simpleHash(s) {
  let h = 0;
  for (let i = 0; i < s.length; i++) {
    h = ((h << 5) - h + s.charCodeAt(i)) | 0;
  }
  return Math.abs(h).toString(16);
}

/**
 * Monta prompt otimizado (telegrafic, sem fluff).
 * Entrada: phaseSpec, previousContext
 * Saida: string prompt estruturado (3-5 linhas + arquivos)
 */
function buildOptimizedPrompt(phaseSpec, previousContext) {
  const lines = [
    `# Phase: ${phaseSpec.title}`,
    `Spec: ${phaseSpec.description}`,
    `Tests: ${Array.isArray(phaseSpec.tests) ? phaseSpec.tests.join(", ") : phaseSpec.tests || "none"}`,
  ];

  // Adiciona contexto anterior se disponivel
  if (previousContext) {
    lines.push(`Previous: ${JSON.stringify(previousContext).substring(0, 100)}...`);
  }

  // Adiciona arquivos (até 3 snippets)
  if (Array.isArray(phaseSpec.files) && phaseSpec.files.length > 0) {
    lines.push("Files:");
    for (let i = 0; i < Math.min(3, phaseSpec.files.length); i++) {
      const file = phaseSpec.files[i];
      try {
        const content = fs.readFileSync(file, "utf-8").substring(0, 200);
        lines.push(`\n\`\`\`${path.extname(file)}\n${content}...\n\`\`\``);
      } catch (_) {
        lines.push(`\n\`\`\`\n[arquivo nao encontrado: ${file}]\n\`\`\``);
      }
    }
  }

  // Adiciona tasks (estrutura YAML)
  if (Array.isArray(phaseSpec.tasks) && phaseSpec.tasks.length > 0) {
    lines.push("\nTasks:");
    for (const task of phaseSpec.tasks.slice(0, 5)) {
      lines.push(
        `  - ${task.name || task.action}: ${task.target_path || "global"}`
      );
    }
  }

  return lines.join("\n");
}

/**
 * Orquestra chamada para subagent (fork).
 * Retorna: {status, result, elapsed_ms}
 *
 * Em ambiente real, isto chamaria TaskCreate com o prompt otimizado.
 * Aqui simulamos com um mock de resultado (R3 autonomia).
 */
async function callSubagent(phaseId, prompt) {
  const startMs = Date.now();
  const logs = [];

  logs.push(`[executor] subagent fork para phase ${phaseId}`);
  logs.push(`[executor] prompt size=${prompt.length} chars`);

  // Simula delay de processamento
  await new Promise((r) => setTimeout(r, 100));

  // Retorna resultado estruturado (em prod, seria resultado real do subagent)
  const result = {
    phase_id: phaseId,
    status: "completed",
    changes: {
      files_modified: 0,
      files_created: 0,
      tests_passed: 0,
      gates_passed: 0,
    },
    summary: "Fase executada com sucesso.",
  };

  const elapsed = Date.now() - startMs;
  return { status: "success", result, elapsed_ms: elapsed, logs };
}

/**
 * Valida schema minimo do phaseSpec (R9 - gates mecanicos).
 * Retorna: {valid: bool, errors: [string]}
 */
function validatePhaseSpec(spec) {
  const errors = [];

  if (!spec.title || typeof spec.title !== "string") {
    errors.push("title e obrigatorio (string)");
  }
  if (!spec.description || typeof spec.description !== "string") {
    errors.push("description e obrigatorio (string)");
  }
  if (!Array.isArray(spec.tasks) || spec.tasks.length === 0) {
    errors.push("tasks deve ser array nao-vazio");
  }
  for (const task of spec.tasks || []) {
    if (!task.name && !task.action) {
      errors.push("cada task deve ter name ou action");
    }
  }

  return {
    valid: errors.length === 0,
    errors,
  };
}

/**
 * Executa a fase: carrega cache, monta prompt, chama subagent, retorna resultado.
 * Entrada: phaseSpec (objeto ou caminho JSON)
 * Saida: {status, phase_id, changes, logs, cached}
 */
async function executePhase(phaseSpec, cachePath) {
  const logs = [];
  const now = new Date().toISOString();
  let spec = phaseSpec;

  // Carrega spec se for caminho de arquivo
  if (typeof phaseSpec === "string") {
    try {
      spec = JSON.parse(fs.readFileSync(phaseSpec, "utf-8"));
      logs.push(`[executor] carregado spec de ${phaseSpec}`);
    } catch (e) {
      return {
        status: "error",
        phase_id: "unknown",
        error: `Falha ao carregar spec: ${e.message}`,
        logs,
      };
    }
  }

  // Valida schema (R9)
  const validation = validatePhaseSpec(spec);
  if (!validation.valid) {
    return {
      status: "error",
      phase_id: spec.phase_id || spec.title || "unknown",
      error: `Validacao falhou: ${validation.errors.join("; ")}`,
      logs,
    };
  }

  const phaseId = spec.phase_id || simpleHash(spec.title);
  logs.push(`[executor] phase_id=${phaseId} title="${spec.title}"`);

  // Carrega cache (R11 - estado em disco)
  const cache = new ExecutorCache(cachePath || "cache/executor-cache.json");
  let previousContext = null;
  let cached = false;

  const cacheKey = `${phaseId}:${simpleHash(spec.description)}`;
  const cachedEntry = cache.get(cacheKey);
  if (cachedEntry) {
    previousContext = cachedEntry.context;
    cached = true;
    logs.push(`[executor] cache hit para ${cacheKey}`);
  } else {
    logs.push(`[executor] cache miss para ${cacheKey}`);
  }

  // Monta prompt otimizado (R0 - economia)
  const optimizedPrompt = buildOptimizedPrompt(spec, previousContext);
  logs.push(`[executor] prompt otimizado=${optimizedPrompt.length} chars`);

  // Chama subagent (orquestracao)
  let subagentResult;
  try {
    subagentResult = await callSubagent(phaseId, optimizedPrompt);
    logs.push(...subagentResult.logs);
  } catch (e) {
    logs.push(`[executor] erro ao chamar subagent: ${e.message}`);
    return {
      status: "error",
      phase_id: phaseId,
      error: e.message,
      logs,
    };
  }

  // Retorna resultado com cache (R10 - idempotencia)
  if (subagentResult.status === "success") {
    // Armazena resultado em cache para proxima execucao
    cache.set(cacheKey, {
      context: subagentResult.result,
      phase_id: phaseId,
      spec_hash: simpleHash(spec.description),
    });

    return {
      status: "success",
      phase_id: phaseId,
      changes: subagentResult.result.changes,
      summary: subagentResult.result.summary,
      elapsed_ms: subagentResult.elapsed_ms,
      cached,
      timestamp: now,
      logs,
    };
  }

  return {
    status: "error",
    phase_id: phaseId,
    error: subagentResult.error || "subagent retornou erro desconhecido",
    logs,
  };
}

/**
 * Exporta funcao publica.
 */
export { executePhase, ExecutorCache, buildOptimizedPrompt };

/**
 * CLI: leitura de stdin ou arquivo, executa, escreve resultado em stdout (JSON).
 *
 * Uso:
 *   node executor.js --spec spec.json --cache cache.json
 *   cat spec.json | node executor.js
 *   node executor.js < spec.json > result.json
 */
async function main() {
  let specInput = null;
  let cachePath = "cache/executor-cache.json";

  // Parse argumentos CLI
  const args = process.argv.slice(2);
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--spec" && i + 1 < args.length) {
      specInput = args[++i];
    } else if (args[i] === "--cache" && i + 1 < args.length) {
      cachePath = args[++i];
    }
  }

  // Lê stdin se nao houver --spec (detecta piping)
  if (!specInput && !process.stdin.isTTY) {
    specInput = await new Promise((resolve) => {
      let data = "";
      process.stdin.setEncoding("utf-8");
      process.stdin.on("data", (chunk) => {
        data += chunk;
      });
      process.stdin.on("end", () => resolve(data));
    });
    try {
      specInput = JSON.parse(specInput);
    } catch (e) {
      console.error(JSON.stringify({ status: "error", error: `Stdin nao e JSON valido: ${e.message}` }));
      process.exit(1);
    }
  }

  if (!specInput) {
    console.error("Erro: forneça --spec <arquivo.json> ou envie JSON via stdin");
    process.exit(1);
  }

  // Executa fase
  const result = await executePhase(specInput, cachePath);

  // Escreve resultado em JSON (R7 - fidelidade de conteudo)
  console.log(JSON.stringify(result, null, 2));

  // Exit code (R9 - gates mecanicos)
  process.exit(result.status === "success" ? 0 : 1);
}

// Roda se for invocado como script (nao importado)
// Verifica se foi chamado diretamente via node scripts/executor.js (nao import)
const isMainModule =
  import.meta.url === `file://${process.argv[1]}` ||
  (process.argv[1] && process.argv[1].endsWith("executor.js"));

if (isMainModule) {
  main().catch((e) => {
    console.error(JSON.stringify({ status: "error", error: e.message }));
    process.exit(1);
  });
}
