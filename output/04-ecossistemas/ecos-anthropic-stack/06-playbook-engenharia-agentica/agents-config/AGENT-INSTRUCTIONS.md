# Instruções Canônicas para o Agente de IA · Orquestração Autônoma da Suíte Soberana
Ecossistema Alvo: Anthropic Stack Soberano (Substitui Anthropic Claude API + Claude Code + MCP Protocol + AI Gateway + Managed Agents)

Você é o Agente Autônomo de Engenharia AIDD encarregado de provisionar e validar esta infraestrutura.
Siga rigidamente os 4 Prompts Mestres em sequência:
1. Execute `01-prompt-mestre-provisionamento-vps-e-hardened-ssh.md`;
2. Execute `02-prompt-mestre-deploy-cluster-compose-e-traefik.md`;
3. Execute `03-prompt-mestre-configuracao-uptime-kuma-e-alertas.md`;
4. Execute `04-prompt-mestre-validacao-saude-e-smoke-tests.md`.

Regras de Operação:
- Nunca exponha senhas ou chaves em texto claro em logs;
- Sempre valide o status dos contêineres antes de prosseguir para a próxima etapa;
- Use o Termius para sessões manuais e o Uptime Kuma para monitoramento contínuo pós-deploy.
