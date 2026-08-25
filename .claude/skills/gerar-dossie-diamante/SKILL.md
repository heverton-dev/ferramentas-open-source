---
name: gerar-dossie-diamante
description: Gera compêndios técnicos de ferramentas open-source no Padrão Dossiê Executivo Diamante R5 usando o compilador determinístico.
---

# Skill: Gerar Dossiê Diamante (Regra R5)

Esta skill garante a produção de compêndios técnicos de alta qualidade visual, eliminando 100% de discrepâncias entre diferentes LLMs.

## 🎯 O Método Determinístico Obrigatório (Regra R8)

**NUNCA gere HTML solto de memória.** Siga sempre o fluxo de 2 etapas:

### Etapa 1: Estruturar os Dados da Camada em JSON
Crie um arquivo JSON com as 20 ferramentas seguindo a estrutura:

```json
{
  "numero": 50,
  "titulo": "Ferramentas Open-Source de Produtividade Soberana",
  "slug": "ferramentas-produtividade",
  "deck": "Compêndio executivo dos 20 maiores motores de código aberto para produtividade pessoal, automação de tarefas e soberania de dados.",
  "ferramentas": [
    {
      "rank": 1,
      "nome": "Obsidian",
      "slug": "obsidian",
      "saas_substituido": "Notion / Roam Research ($120/ano)",
      "economia_anual_str": "R$ 36.000/ano",
      "licenca_osi": "Proprietário/Local",
      "categoria": "PKM / Gestão do Conhecimento",
      "senioridade": "Pleno",
      "o_que_faz": "Base de conhecimento em Markdown local com grafos bidirecionais de conexões.",
      "como_funciona": "Arquivos 100% locais em texto puro sem dependência de nuvem proprietária.",
      "comando_rapido": "winget install Obsidian.Obsidian # ou flatpak install md.obsidian.Obsidian",
      "repositorio_github": "https://github.com/obsidianmd",
      "veredito": "Padrão da indústria para notas atômicas e escrita em Markdown soberana.",
      "passos_praticos": [
        {"passo": 1, "titulo": "Crie o Cofre Local", "descricao": "Abra uma pasta local do disco para gerenciar seus arquivos Markdown."},
        {"passo": 2, "titulo": "Conecte Ideias com Links", "descricao": "Use colchetes duplos [[nota]] para criar grafos visuais de conhecimento."},
        {"passo": 3, "titulo": "Sincronize com Git", "descricao": "Use o plugin Obsidian Git para versionamento gratuito e seguro."}
      ]
    }
  ]
}
```

### Etapa 2: Executar o Compilador Determinístico
```bash
python scripts/compilar_compendio_diamante.py dados_50.json
```

O script gerará o arquivo `output/listas-open-source/50-ferramentas-produtividade.html` 100% no Padrão Diamante R5.

### Etapa 3: Sincronizar Espelhos e Auditar
```bash
python scripts/limpar_entulho.py
python scripts/auditar_r5_dossie.py
```
