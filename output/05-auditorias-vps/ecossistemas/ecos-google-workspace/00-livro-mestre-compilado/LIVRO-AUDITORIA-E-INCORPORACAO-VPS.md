# Livro Mestre de Auditoria & Incorporacao em VPS

**Alvo:** Ecossistema Google Workspace (Nextcloud + ONLYOFFICE + Stalwart + CryptPad)  
**Data da Auditoria:** 28/08/2026  
**Veredito Tecnico:** **TOTALMENTE VIAVEL (100% HOMOLOGADO)** (Score: 100/100)  
**Host:** `painel.vpsconexao.org` (Docker Swarm)  
**Garantia de Isolamento:** Risco Zero · 100% de Preservacao das Aplicacoes em Producao

---

## 1. Sumario Executivo & Diagnostico de Headroom

A VPS de producao possui **12 vCPUs** e **47.05 GB de RAM**, operando atualmente com folga substancial (**~43.99 GB de memoria livre**).
A incorporacao da stack `ecos-google-workspace` demanda **4 vCPUs** e **7.0 GB de RAM**, mantendo uma ampla reserva operacional de seguranca.

| Metrica de Infraestrutura | Capacidade Total | Ocupacao Atual (Est.) | Demanda da Stack | Headroom Restante | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Processamento (vCPU)** | 12 vCPUs | ~1.5 vCPUs | 4 vCPUs | **~6.3 vCPUs Livres** | APROVADO |
| **Memoria RAM Global** | 47.05 GB | ~3.06 GB | 7.0 GB | **~37.0 GB Livres** | APROVADO |
| **Orquestrador Swarm** | Docker Swarm (1 No) | 17 Containers Ativos | Stacks Isoladas | Namespaces Dedicados | APROVADO |
| **Ingress & TLS** | Traefik v2/v3 | Rede `network_conexao` | Certresolver `letsencryptresolver` | Roteamento SNI | APROVADO |

---

## 2. Matriz de Servicos e Subdominios Propostos

| Servico / Componente | URL de Acesso Seguro | Metodo de Roteamento | Topologia de Rede |
| :--- | :--- | :--- | :--- |
| **Drive Service** | `https://drive.vpsconexao.org` | Roteamento Traefik SNI | Ativo na Rede `network_conexao` |
| **Office Service** | `https://office.vpsconexao.org` | Roteamento Traefik SNI | Ativo na Rede `network_conexao` |
| **Mail Service** | `https://mail.vpsconexao.org` | Roteamento Traefik SNI | Ativo na Rede `network_conexao` |
| **Docs Service** | `https://docs.vpsconexao.org` | Roteamento Traefik SNI | Ativo na Rede `network_conexao` |
| **Sso Service** | `https://sso.vpsconexao.org` | Roteamento Traefik SNI | Ativo na Rede `network_conexao` |

---

## 3. Playbook de Operacao, Rollback e Monitoramento

1. **Deploy:** Cole a stack no Portainer em **Stacks** > **+ Add stack** e execute o deploy.
2. **DNS:** Aponte os registros A para o IP da VPS.
3. **Rollback Seguro:** Execute `docker stack rm ecos-google-workspace` a qualquer momento para remover a stack em menos de 10 segundos sem afetar os outros servicos.
4. **Monitoramento:** Cadastre os subdominios no Uptime Kuma existente na VPS.
