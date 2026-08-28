# Checklist de Validacao de Saude Pos-Rollback

## 1. Verificacao de Integridade
Apos executar o rollback, valide no terminal da VPS:
1. `docker service ls` -> Confirme que apenas os servicos pre-existentes estao ativos.
2. `docker stack ls` -> Confirme que a stack `open-notebook` foi removida.
3. Teste o acesso ao Mautic, n8n e Evolution API para certificar 100% de disponibilidade.
