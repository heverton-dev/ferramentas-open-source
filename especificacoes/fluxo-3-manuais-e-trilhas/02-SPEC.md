# 02 · Especificação Técnica & Contrato de Schemas

> **Módulo:** Esteira Autônoma de Ingestão de Fontes, Manuais VPS e Trilhas de Aprendizado  
> **Padrão:** JSON Schema Draft 2020-12 & Tipagem Estrita  
> **Status:** Produção Homologada · Nota 10.0 / 10.0

---

## 1. Requisitos Funcionais (RF)

- **RF01 (Ingestão Hierárquica 4 Níveis):** O sistema deve coletar fontes estruturadas cobrindo:
  1. Documentação Oficial / Repositório GitHub;
  2. Livros Técnicos / Guias Arquiteturais / E-books;
  3. Vídeos Práticos do YouTube (walkthroughs e tutoriais);
  4. Cursos, Playbooks e Guias de Implantação.
- **RF02 (Zero Download Pesado):** O crawler deve operar exclusivamente em memória, sendo terminantemente proibido o download de arquivos binários pesados (`.mp4`, `.mp3`, `.tar.gz`).
- **RF03 (Didática Inclusiva / Módulo 0):** O manual deve conter obrigatoriamente uma seção de desmistificação de jargões técnicos para iniciantes, com analogias do cotidiano.
- **RF04 (Roteiro de Primeiro Voo):** O manual deve fornecer um passo a passo guiado de até 3 minutos para permitir ao operador validar o primeiro uso funcional do sistema.
- **RF05 (Brasil First & Acessibilidade PT-BR):** A trilha deve priorizar fontes em português brasileiro e fornecer roteiros de tradução assistida para conteúdos em inglês.
- **RF06 (Compilação Tripartite):** Manuais, trilhas e relatórios devem ser compilados simultaneamente em HTML Interativo, Markdown Limpo e PDF Executivo via Typst (<100ms).
- **RF07 (Relatório de Fechamento com Telemetria):** Cada ferramenta processada deve receber um relatório tripartite registrando tempos, consumo de tokens, modelo de LLM, tools, skills e conformidade dos gates.
- **RF08 (Desinstalação Cirúrgica & Isolamento da VPS):** O manual deve conter obrigatoriamente a Seção 5 detalhando os 4 passos de remoção segura sem afetar outros contêineres, bancos ou serviços da VPS, acompanhado de checklist de validação de saúde do servidor.

---

## 2. Requisitos Não-Funcionais (RNF)

- **RNF01 (Determinismo Radical):** Scripts em Python e Typst devem ser idempotentes e executar sem consumo de tokens de LLM.
- **RNF02 (Tempo de Resposta):** A compilação gráfica completa de um pacote de 9 arquivos deve levar menos de 4 segundos.
- **RNF03 (Portabilidade Windows / Linux):** Todo script deve garantir compatibilidade UTF-8 nativa no Windows (`sys.stdout.reconfigure(encoding="utf-8")`) e respeitar o limite de 260 caracteres de caminho (MAX_PATH).
- **RNF04 (Regra R18 - Soberania em Output & Zero Entulho):** Todos os artefatos residem na pasta soberana única `output/03-manuais-e-trilhas/`, com publicação direta via CI/CD e zero arquivos duplicados ou temporários.

---

## 3. Contratos de Schemas JSON

### 3.1. Schema do Manual Operacional (`schema_manual_operacional.json`)
```json
{
  "produto_foco": "string",
  "slug": "string",
  "saas_origem": "string",
  "saas_substituido": "string",
  "nivelamento_conceitual": [
    {
      "termo": "string",
      "analogia_cotidiana": "string",
      "explicacao_simples": "string"
    }
  ],
  "roteiro_primeiro_voo": [
    {
      "passo": "string",
      "acao": "string",
      "resultado_esperado": "string"
    }
  ],
  "passos_vps": [
    {
      "ordem": "integer",
      "titulo": "string",
      "comando": "string",
      "o_que_acontece_na_tela": "string",
      "como_saber_se_deu_certo": "string"
    }
  ],
  "comandos_cli": [
    {
      "comando": "string",
      "descricao": "string",
      "exemplo": "string",
      "fonte_id": "string (ex: F01)"
    }
  ],
  "referencias_bibliograficas": [
    {
      "id": "string",
      "categoria": "string",
      "titulo": "string",
      "url": "string",
      "autor_ou_canal": "string"
    }
  ]
}
```

### 3.2. Schema da Trilha de Aprendizado (`schema_trilha_aprendizado.json`)
```json
{
  "produto_foco": "string",
  "tempo_total_estimado": "string",
  "fases": [
    {
      "fase_num": "integer",
      "titulo": "string",
      "tempo_estimado": "string",
      "objetivo": "string",
      "recursos": [
        {
          "titulo": "string",
          "tipo_midia": "string",
          "fonte_id": "string",
          "url": "string",
          "aprendizado_chave": "string",
          "duracao": "string",
          "autor": "string",
          "idioma": "string (ex: pt-BR ou en)",
          "dica_traducao_ptbr": "string"
        }
      ]
    }
  ]
}
```

### 3.3. Schema do Relatório de Telemetria (`schema_relatorio_execucao.json`)
```json
{
  "produto_foco": "string",
  "slug": "string",
  "saas_origem": "string",
  "data_execucao": "string (DD-MM-YYYY)",
  "horario_inicio": "string (HH:MM:SS)",
  "horario_fim": "string (HH:MM:SS)",
  "tempo_total_segundos": "number",
  "harness_utilizado": "string",
  "llm_utilizada": "string",
  "tools_utilizadas": ["string"],
  "skills_utilizadas": ["string"],
  "telemetria_tokens": {
    "tokens_input": "integer",
    "tokens_output": "integer",
    "tokens_totais": "integer",
    "taxa_economia_determinismo": "string"
  },
  "materiais_entregues": [
    {
      "tipo": "string",
      "nome_arquivo": "string",
      "formato": "string",
      "caminho_relativo": "string"
    }
  ],
  "gates_status": {
    "gate_g0": { "status": "string", "descricao": "string" },
    "gate_g1": { "status": "string", "descricao": "string" },
    "gate_g2": { "status": "string", "descricao": "string" },
    "gate_r18": { "status": "string", "descricao": "string" }
  }
}
```
