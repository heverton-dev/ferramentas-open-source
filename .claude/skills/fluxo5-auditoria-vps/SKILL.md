---
name: fluxo5-auditoria-vps
description: Auditoria de infraestrutura de VPS em tempo real via Portainer API (.env), avaliacao matematica de headroom, geracao de stacks Swarm integradas e manuais de instalacao e desinstalacao cirurgica sem risco com suporte a encadeamento multi-alvo.
---

# Fluxo 5 ? Auditoria, Incorpora??o e Desinstala??o Cir?rgica em VPS (Multi-Alvo)

Este skill gerencia a execu??o do **Fluxo 5**, que conecta ? VPS via API do Portainer, audita hardware, redes e proxy reverso existentes, avalia a viabilidade de hospedar novos ecossistemas ou ferramentas individuais (ou m?ltiplos alvos de forma cumulativa) e gera manuais completos de implanta??o e desinstala??o segura.

## Quando Utilizar

- Quando o usu?rio solicitar an?lise da VPS para saber se cabe uma ferramenta, um ecossistema ou um conjunto deles.
- Para simular a capacidade m?xima e o saldo de vCPU/RAM restante para m?ltiplos alvos.
- Para gerar stacks Swarm / Compose 100% adaptadas ? VPS real (sem conflito de portas ou redes).
- Para fornecer manuais acess?veis a n?o-t?cnicos de instala??o e rollback cir?rgico.

## Modos de Execu??o

### 1. Auditoria de Alvo ?nico
```bash
# Ecossistema ?nico
python scripts/run_fluxo5.py --ecossistema ecos-google-workspace

# Ferramenta ?nica
python scripts/run_fluxo5.py --ferramenta stalwart
```

### 2. Auditoria Encadeada Multi-Alvo (Cumulativa)
```bash
# M?ltiplos ecossistemas espec?ficos
python scripts/run_fluxo5.py --ecossistemas ecos-google-workspace,ecos-crm-marketing

# M?ltiplas ferramentas espec?ficas
python scripts/run_fluxo5.py --ferramentas stalwart,nextcloud,onlyoffice,chatwoot

# Todos os ecossistemas cadastrados
python scripts/run_fluxo5.py --todos-ecossistemas

# Todas as ferramentas cadastradas
python scripts/run_fluxo5.py --todas-ferramentas

# Varredura total simult?nea
python scripts/run_fluxo5.py --todos
```

## Artefatos Gerados por Execu??o

1. **Por Alvo Individual (`output/05-auditorias-vps/[ecossistemas|ferramentas]/<slug>/`):**
   - `01-relatorio-auditoria-viabilidade.md` e `.html`
   - `02-stack-integrada-portainer.yml`
   - `03-manual-instalacao-cirurgica.md` e `.html`
   - `04-manual-desinstalacao-e-rollback.md` e `.html`

2. **No Modo Multi-Alvo (`output/05-auditorias-vps/`):**
   - `00-painel-consolidado-multialvo.md` e `.html` (Balan?o cumulativo de headroom e tabela comparativa)

## Banco de Dados de Estado

Todas as execu??es s?o registradas na tabela `esteira_auditorias_vps` do `estado_esteira.db`.
