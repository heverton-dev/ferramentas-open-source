---
name: fluxo5-auditoria-vps
description: Auditoria de infraestrutura de VPS em tempo real via Portainer API (.env), avaliação matemática de headroom, geração de stacks Swarm integradas e manuais de instalação e desinstalação cirúrgica sem risco com suporte a encadeamento multi-alvo.
---

# Fluxo 5 — Auditoria, Incorporação e Desinstalação Cirúrgica em VPS (Multi-Alvo)

Esta skill gerencia a execução do **Fluxo 5**, que conecta à VPS via API do Portainer, audita hardware, redes e proxy reverso existentes, avalia a viabilidade de hospedar novos ecossistemas ou ferramentas individuais (ou múltiplos alvos de forma cumulativa) e gera manuais completos de implantação e desinstalação segura.

## Quando Utilizar

- Quando o usuário solicitar análise da VPS para saber se cabe uma ferramenta, um ecossistema ou um conjunto deles.
- Para simular a capacidade máxima e o saldo de vCPU/RAM restante para múltiplos alvos.
- Para gerar stacks Swarm / Compose 100% adaptadas à VPS real (sem conflito de portas ou redes).
- Para fornecer manuais acessíveis a não-técnicos de instalação e rollback cirúrgico.

## Modos de Execução

### 1. Auditoria de Alvo Único
```bash
# Ecossistema único
python scripts/run_fluxo5.py --ecossistema ecos-google-workspace

# Ferramenta única
python scripts/run_fluxo5.py --ferramenta stalwart
```

### 2. Auditoria Encadeada Multi-Alvo (Cumulativa)
```bash
# Múltiplos ecossistemas específicos
python scripts/run_fluxo5.py --ecossistemas ecos-google-workspace,ecos-crm-marketing

# Múltiplas ferramentas específicas
python scripts/run_fluxo5.py --ferramentas stalwart,nextcloud,onlyoffice,chatwoot

# Todos os ecossistemas cadastrados
python scripts/run_fluxo5.py --todos-ecossistemas

# Todas as ferramentas cadastradas
python scripts/run_fluxo5.py --todas-ferramentas

# Varredura total simultânea
python scripts/run_fluxo5.py --todos
```

## Artefatos Gerados por Execução (Regra R5-VPS)

1. **Por Alvo Individual (`output/05-auditorias-vps/[ecossistemas|ferramentas]/<slug>/`):** 5 subdiretórios modulares + arquivo `.typ` na raiz + PDF compilado via Typst. Zero arquivos soltos.
   - `00-livro-mestre-compilado/` — `LIVRO-AUDITORIA-E-INCORPORACAO-VPS.{html,md,pdf}` (relatório consolidado)
   - `01-guias-executivos-e-viabilidade/` — dossiê de hardware/headroom, matriz de compatibilidade e risco, análise de TCO/economia
   - `02-guias-de-engenharia-e-infraestrutura/` — `01-stack-swarm-producao-integrada.yml`, roteiro DNS/SPF/DKIM/DMARC, mapa de topologia de redes e volumes
   - `03-playbooks-de-instalacao-e-operacao/` — manual de instalação cirúrgica via Portainer, wizard pós-deploy, cadastro de health check no Uptime Kuma
   - `04-playbooks-de-desinstalacao-e-governanca/` — manual de desinstalação atômica e rollback, script de expurgo de volumes, checklist de validação pós-rollback

2. **No Modo Multi-Alvo (`output/05-auditorias-vps/`):**
   - `00-painel-consolidado-multialvo.md` e `.html` (Balanço cumulativo de headroom e tabela comparativa)

## Registro Declarativo de Perfis (Regra R12)

Toda ferramenta ou ecossistema auditável DEVE ter uma entrada em `TOOL_PROFILES` ou `ECOSYSTEM_PROFILES` (`scripts/modulos/vps_decision_engine.py`) com `req_cpu`, `req_ram_gb`, `host_ports` e `subdomains` reais — derivados do `vps_recomendada` do respectivo `scripts/data/manual-<slug>.json` ou `ecos-<slug>.json`. Sem essa entrada, o motor cai em um perfil genérico de fallback (1.5 vCPU / 1.5 GB, porta 80) que não reflete a arquitetura real da ferramenta. Ferramentas com protocolos não-HTTP (SMTP/IMAP/POP3/DNS) DEVEM preencher `host_ports` — o gerador publica essas portas diretamente no host (`mode: host`) além do roteamento Traefik padrão.

## Banco de Dados de Estado

Todas as execuções são registradas na tabela `esteira_auditorias_vps` do `estado_esteira.db`.
