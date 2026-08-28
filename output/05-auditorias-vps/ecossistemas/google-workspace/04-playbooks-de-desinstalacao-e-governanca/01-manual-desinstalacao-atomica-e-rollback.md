# Manual de Desinstalacao Cirurgica e Rollback

**Alvo:** Ecossistema google-workspace  
**Garantia de Isolamento:** 100% de preservacao dos demais containers da VPS  
**Tempo de Execucao:** Menos de 10 segundos

---

## 1. Principios de Seguranca e Isolamento

Todos os recursos criados para o alvo `Ecossistema google-workspace` foram encapsulados no namespace `google-workspace`.
A remo??o da stack desconecta os servicos da rede `network_conexao` e revoga os roteadores do Traefik de forma atomica.
**Mautic, Evolution, n8n, MySQL, PostgreSQL global e Portainer continuam operando normalmente sem nenhuma interrupcao.**

---

## 2. Procedimento 1: Remocao via Painel Portainer (Interface Gr?fica)

1. Acesse: `https://painel.vpsconexao.org`.
2. Clique em **Stacks** no menu lateral esquerdo.
3. Localize a stack `google-workspace` e marque a caixa de sele??o ao lado dela.
4. Clique no bot?o vermelho **Delete this stack**.
5. Confirme a exclusao na janela pop-up.
6. Em menos de 10 segundos, todos os containers serao finalizados e as rotas web desligadas.

---

## 3. Procedimento 2: Remocao via Linha de Comando (CLI / SSH)

Caso prefira executar via terminal SSH ou Termius:

```bash
# 1. Remover a stack do Docker Swarm
docker stack rm google-workspace

# 2. Aguardar 10 segundos para finalizacao completa dos processos
sleep 10

# 3. Verificar que as demais stacks continuam 100% operacionais
docker stack ls
docker service ls
```

---

## 4. Limpeza Opcional de Volumes Persistentes (Liberacao de Disco)

Se voc? n?o planeja restaurar a aplica??o e deseja liberar espa?o em disco:

```bash
# Listar e remover apenas os volumes exclusivos da stack removida
docker volume ls --filter name=google-workspace -q | xargs -r docker volume rm
```

*(Nenhum volume do Mautic, n8n, PostgreSQL global ou MySQL sera afetado).*
