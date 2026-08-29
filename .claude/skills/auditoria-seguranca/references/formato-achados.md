# Schema de achados

Formato unico usado por `baseline.json`, `pos-correcao.json` e pelos scripts de
fingerprint, comparacao e renderizacao.

```json
{
  "projeto": "nome-do-projeto",
  "data": "2026-08-28",
  "estagio": "baseline",
  "stack": {
    "linguagens": ["python", "javascript"],
    "framework": "nenhum (CLI/batch)",
    "orm": "sqlite3 (SQL cru, parametrizado)",
    "auth": "nenhuma",
    "frontend": "HTML estatico gerado",
    "deploy": []
  },
  "categorias_nao_aplicaveis": [
    {
      "categoria": "permissao-navegador",
      "razao": "Nao ha frontend com autenticacao nem papeis de usuario."
    }
  ],
  "achados": [
    {
      "id": "a1b2c3d4",
      "categoria": "chaves-expostas",
      "titulo": "Credenciais de producao em .env versionado",
      "arquivo": ".env",
      "linhas": [3, 8, 13, 18],
      "trecho": "GITHUB_TOKEN=\"ghp_****\"",
      "severidade": "critica",
      "por_que_exploravel": "Leitura direta do arquivo entrega PAT do GitHub e acesso root a VPS.",
      "impacto": "Controle do repositorio, do orquestrador de containers e do servidor.",
      "condicoes": "Nenhuma. Explorável por qualquer um com acesso de leitura ao repositorio.",
      "correcao": "Rotacionar as credenciais, remover do historico, criar .env.example e gate de startup.",
      "faixa": "humano"
    }
  ],
  "pontos_fortes": [
    {
      "descricao": "Todas as queries SQLite usam statements parametrizados",
      "evidencia": "scripts/estado_esteira.py:189 - cursor.execute(\"... WHERE slug = ?\", (slug,))"
    }
  ]
}
```

## Campos

| Campo | Obrigatorio | Nota |
|---|---|---|
| `id` | gerado | Fingerprint, preenchido por `fingerprint.py` |
| `categoria` | sim | Um dos slugs abaixo |
| `titulo` | sim | Uma linha, especifica |
| `arquivo` | sim | Caminho relativo a raiz, com `/` |
| `linhas` | sim | Lista de inteiros. Use `[]` para achado estrutural |
| `trecho` | sim | Codigo real. **Segredo sempre mascarado** |
| `severidade` | sim | `critica`, `alta`, `media`, `baixa`, `informativa` |
| `por_que_exploravel` | sim | O caminho do ataque, concreto |
| `impacto` | sim | O que o atacante obtem |
| `condicoes` | sim | Pre-requisitos. `"Nenhuma"` se explorável direto |
| `correcao` | sim | O que fazer |
| `faixa` | sim | `auto`, `confirmar` ou `humano` |

### Slugs de categoria

`banco-sem-tranca`, `permissao-navegador`, `idor`, `chaves-expostas`, `inputs-sem-tratamento`

### Severidades

| Nivel | Criterio |
|---|---|
| `critica` | Explorável agora, sem pre-requisito relevante; ou credencial viva exposta; ou escrita/exclusao de dado alheio |
| `alta` | Explorável com pre-requisito comum, ou leitura de dado alheio, ou default publico de segredo sem validacao |
| `media` | Exige condicao incomum, ou impacto limitado |
| `baixa` | Padrao arriscado com explorabilidade dependente de mudanca futura |
| `informativa` | Divida arquitetural ou observacao. **Nao conta como vulnerabilidade** |

Nao infle severidade para dar peso ao relatorio: relatorio inflado e ignorado, e o
critico real se perde no meio.

## Fingerprint

`hash(categoria + arquivo + regra_normalizada)`, onde `regra_normalizada` deriva do
titulo reduzido a forma canonica.

Numero de linha fica **fora** de proposito: um achado que so desceu tres linhas nao pode
ser contado como corrigido. O preco e que duas ocorrencias da mesma regra no mesmo
arquivo colidem — aceitavel, porque a correcao trata ambas.

## Comparativo

`comparar.py` emite:

```json
{
  "corrigidos":   [ { "id": "...", "titulo": "...", "severidade": "..." } ],
  "persistentes": [ ... ],
  "novos":        [ ... ],
  "resumo": {
    "baseline":      { "critica": 3, "alta": 2, "media": 2, "baixa": 1 },
    "pos":           { "critica": 0, "alta": 1, "media": 0, "baixa": 1 },
    "gate":          "aprovado",
    "gate_motivos":  []
  }
}
```

Gate `reprovado` quando sobra critico do baseline sem resolver, ou quando aparece
qualquer achado novo. `gate_motivos` lista o que reprovou.
