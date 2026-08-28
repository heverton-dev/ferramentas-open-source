# Checklist de Validação de Saúde Pós-Rollback

## 1. Verificação de Integridade
Após executar o rollback, valide no terminal da VPS:
1. `docker service ls` -> Confirme que apenas os serviços pré-existentes estão ativos.
2. `docker stack ls` -> Confirme que a stack `khoj` foi removida.
3. Teste o acesso ao Mautic, n8n e Evolution API para certificar 100% de disponibilidade.
