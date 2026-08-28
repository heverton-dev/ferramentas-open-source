# Playbook do Engenheiro Agêntico: Penso Mail & Collaboration Suite

> **Objetivo:** Subir e gerenciar 100% do ecossistema utilizando Agentes de IA autônomos, Termius para acesso seguro e Uptime Kuma para monitoramento contínuo em tempo real.  
> **SaaS Substituído:** `Penso Suite (Zimbra Collaboration, Penso Drive, Penso Antispam)` | **Economia:** `R$ 49.800/ano`  

---

## 1. Visão Geral da Abordagem Agêntica
O Engenheiro Agêntico não executa comandos manuais repetitivos: ele orquestra agentes de IA equipados com ferramentas (MCPs) que executam o ciclo completo de vida da infraestrutura.

---

## 2. Estrutura de Prompts Mestres (Disponíveis em `prompts-mestres/`)
1. `01-prompt-mestre-provisionamento-vps-e-hardened-ssh.md`: Hardening da VPS, UFW, Fail2ban e Docker;
2. `02-prompt-mestre-deploy-cluster-compose-e-traefik.md`: Geração de manifestos, variáveis seguras e subida do cluster;
3. `03-prompt-mestre-configuracao-uptime-kuma-e-alertas.md`: Configuração do monitoramento em tempo real com Uptime Kuma;
4. `04-prompt-mestre-validacao-saude-e-smoke-tests.md`: Testes de fumaça, validação OIDC e teste prático de backup 3-2-1.

---

## 3. Ferramentas Obrigatórias de Gestão & Observabilidade
- **Termius:** Gestão de credenciais SSH (Ed25519), túneis seguros para portas internas e SFTP corporativo;
- **Uptime Kuma:** Monitoramento de saúde 24/7 de todos os serviços com alertas via Webhook no Mattermost / WhatsApp;
- **Servidores MCP:** `@modelcontextprotocol/server-ssh` e `@modelcontextprotocol/server-docker` configurados em `agents-config/.mcp.json`.
