---
name: fabrica-listas
description: >
  Fábrica de compêndios técnicos e apresentações HTML autônomas de alta densidade.
  Gera catálogos auditados de ferramentas, especificações de consumo de hardware,
  substituições de SaaS e boas práticas de engenharia com design editorial e scrollbar 4px.
  Use quando o usuário pedir listas, catálogos comparativos, compêndios técnicos ou invocar /fabrica-listas.
license: MIT
metadata:
  version: 1.0.0
  author: Fábrica Universal
---

# Fábrica de Listas e Apresentações Técnicas (Spec Fabril)

Especificação para gerar apresentações e catálogos técnicos em HTML autocontido com máxima densidade de informação, design editorial tipográfico e conformidade rigorosa com a governança do repositório.

## 1. Estrutura Obrigatória do Documento HTML

Todo arquivo gerado pela fábrica DEVE ser um HTML único, autocontido, responsivo e com suporte nativo a temas Claro e Escuro (via CSS variables).

### Paleta e Tipografia (Design System)

```css
:root {
  --paper: #ECEEF2;
  --surface: #F8F9FC;
  --surface-2: #DFE3EB;
  --ink: #151A26;
  --ink-2: #3B4457;
  --muted: #68738A;
  --rule: #C7CEDB;
  --rule-soft: #DADFE8;
  --accent: #1A446C; /* Personalizar por tema */
  --accent-soft: #DCE7F2;
  --gold: #7A5410;
  --gold-soft: #EFE5CE;
  --flag: #8E2436;
  --flag-soft: #F0D9DD;
  --green: #1B5E3B;
  --green-soft: #D8EFE2;
  --serif: "Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
  --sans: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  --mono: ui-monospace, "Cascadia Mono", "SF Mono", SFMono-Regular, Menlo, Consolas, monospace;
}
```

### Regra Estrita da Scrollbar (4px)

```css
* {
  scrollbar-width: thin;
  scrollbar-color: var(--accent) transparent;
}
::-webkit-scrollbar {
  width: 4px;
  height: 4px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: var(--accent);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: color-mix(in srgb, var(--accent) 80%, black);
}
```

## 2. Seções Padronizadas do Compêndio

1. **Header com Eyebrow:** Tag de auditoria, data, total de itens e chips com estatísticas resumidas.
2. **Parte 1 (Conceito & Dilema):** Rotas comparativas (Custo/Risco vs Solução/Soberania).
3. **Parte 2 (Tabela Panorama):** Tabela com `#`, `Ferramenta`, `Substitui / Categoria`, `Impacto / Economia` e `Licença OSI`.
4. **Parte 3 (Ledger de Cards Detalhados):**
   - Número do card no grid
   - Título e badges (Substituição, Economia Real, Licença OSI)
   - Bloco "O que entrega" com comandos executáveis (`docker run` / `pip` / `npx`)
   - Bloco "Especificação & Realidade" com consumo real de RAM/VRAM em repouso
   - Link oficial para o repositório no GitHub
5. **Parte 4 (Armadilhas & Falsos Open Source):** Lista de 4 a 8 riscos documentados (mudanças para BSL, SSPL, telemetria forçada, SaaS lock-in).
6. **Parte 5 (O Método Fabril):** Arquitetura recomendada de montagem do ambiente em 4 etapas sequenciais.
7. **Footer:** Fontes, órgãos de auditoria (OSI, CNCF, Linux Foundation) e notas de integridade.

## 3. Regras de Rigor Técnico

- **Sem licenças falsas:** Apenas licenças aprovadas pela OSI (MIT, Apache-2.0, BSD, GPL, AGPL, MPL-2.0).
- **Sem comandos fictícios:** Todos os comandos de subida devem ser executáveis e testados.
- **Métricas reais de memória:** Medidas em repouso em ambiente Linux limpo.
- **Persistência dupla:** Salvar sempre em `output/listas-open-source/<slug>.html` e `docs/listas/<slug>.html`.
