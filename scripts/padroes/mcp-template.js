#!/usr/bin/env node
/**
 * <seu-mcp>: MCP server minimo (stdio) — template.
 *
 * Por que um MCP e nao um script: use MCP quando o agente precisa consultar
 * ESTADO ao vivo ou executar uma acao com efeito colateral controlado, varias
 * vezes numa mesma sessao. Para transformacao pura de arquivo, um script Python
 * (scripts/padroes/script-template.py) e mais barato e mais testavel (R8).
 *
 * Registro em `.mcp.json` na raiz do projeto:
 *
 *   {
 *     "mcpServers": {
 *       "<seu-mcp>": {
 *         "command": "node",
 *         "args": ["scripts/mcp/<seu-mcp>.js"]
 *       }
 *     }
 *   }
 *
 * Depois de editar `.mcp.json`, rodar scripts/setup-links.* para propagar o
 * espelho `.cursor/mcp.json` (hardlink) e gerar os schemas divergentes
 * (.vscode/mcp.json, opencode.json).
 *
 * Dependencia: npm i @modelcontextprotocol/sdk
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  { name: "<seu-mcp>", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// --- Catalogo de tools -----------------------------------------------------
// A description e o unico texto que o agente le para decidir chamar a tool.
// Diga o que ela FAZ e QUANDO usar; nao repita o nome.
const TOOLS = [
  {
    name: "<sua_tool>",
    description:
      "<O que faz e quando usar. Ex.: 'Le o estado atual da esteira e retorna " +
      "os itens pendentes. Use antes de decidir o proximo lote.'>",
    inputSchema: {
      type: "object",
      properties: {
        alvo: { type: "string", description: "<o que identifica o item>" },
        estrito: { type: "boolean", description: "avisos tambem reprovam", default: false },
      },
      required: ["alvo"],
    },
  },
];

server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools: TOOLS }));

// --- Implementacao ---------------------------------------------------------
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case "<sua_tool>": {
        // ==== SUA LOGICA AQUI ====
        const resultado = { alvo: args.alvo, status: "sucesso", itens: [] };
        return {
          content: [{ type: "text", text: JSON.stringify(resultado, null, 2) }],
        };
      }
      default:
        throw new Error(`tool desconhecida: ${name}`);
    }
  } catch (e) {
    // Erro vira resposta com isError, nao excecao solta: excecao derruba o
    // servidor e o agente perde a sessao inteira do MCP.
    return {
      isError: true,
      content: [{ type: "text", text: `${e.name}: ${e.message}` }],
    };
  }
});

// --- Boot ------------------------------------------------------------------
// stdio: NUNCA escrever em stdout fora do protocolo (um console.log solto
// corrompe o frame JSON-RPC). Log de diagnostico vai em stderr.
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("<seu-mcp> pronto (stdio)");
}

main().catch((e) => {
  console.error("falha ao iniciar <seu-mcp>:", e);
  process.exit(1);
});
