---
name: fluxo3-manuais-e-trilhas
description: Especialista no acionamento e orquestração do Fluxo 3 (Esteira de Engenharia, Manuais VPS & Trilhas de Aprendizado). Realiza auditoria de 5 fontes verificadas (G0/G1/G2), gera manuais operacionais com Desinstalação Cirúrgica (isolamento total da VPS) e compila trilhas didáticas de 5 aulas.
alwaysApply: false
---

# Skill Especialista · Fluxo 3: Manuais VPS & Trilhas AIDD

Esta skill governa a **Esteira de Engenharia e Produção**, transformando código open source em manuais operacionais hiperdidáticos e playbooks de deploy em servidores VPS.

## Quando Usar
- Quando o usuário quiser colocar uma ferramenta em produção na VPS;
- Quando o comando `/fluxo3` ou `/manual-vps` for disparado;
- Quando for necessário gerar o manual de instalação, uso exaustivo, desinstalação segura e trilha de 5 aulas de uma ferramenta.

## Protocolo de Execução Agêntica

1. **Identificação da Ferramenta e SaaS (Gate de Entrada):**
   - Verifique a ferramenta informada (ex: `/fluxo3 screenpipe granola`);
   - Se o usuário não informar, pergunte qual ferramenta do Quinteto Soberano será abordada.

2. **Auditoria Mecânica G0, G1 e G2:**
   - Valida 5 fontes de alta autoridade (F01 a F05);
   - Testa disponibilidade HTTP 200 das URLs;
   - Assegura 100% de citações cruzadas sem alucinação.

3. **Acionamento Determinístico via CLI:**
   Execute o runner oficial:
   ```bash
   python scripts/run_fluxo3.py --ferramenta <slug-ferramenta> --saas <saas-slug>
   ```

4. **Verificação da Seção de Desinstalação Cirúrgica:**
   - O manual deve conter obrigatoriamente a *Parte IV: Desinstalação Cirúrgica & Isolamento da VPS (Zero Efeito Colateral)* com os 4 passos seguros e checklist de saúde da VPS.

5. **Entregas em `output/03-manuais-e-trilhas/<saas>/<ferramenta>/`:**
   - `manuais/manual-<ferramenta>-vps-e-uso.{html,md,pdf}`
   - `trilhas/trilha-<ferramenta>-aprendizado.{html,md,pdf}`

6. **Apresentação ao Usuário:**
   Forneça a matriz de comandos essenciais, os dados de hardware da VPS recomendada e os links diretos para os manuais.
