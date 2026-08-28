# Manual de Desinstala??o Cir?rgica e Rollback

**Alvo:** Ecossistema DevOps & Engenharia de Dados (NocoDB + Supabase + n8n + Directus)  
**Garantia de Isolamento:** 100% de preserva??o dos demais containers da VPS

---

## 1. Por que este procedimento ? seguro?

Todos os servi?os foram criados dentro do namespace exclusivo da stack `ecos-devops-infra`.
A remo??o da stack desconecta os containers da rede `network_conexao` e remove as regras do Traefik de forma limpa e at?mica.
**Mautic, Evolution, n8n, MySQL, PostgreSQL global e Portainer continuam operando normalmente sem interrup??o.**

---

## 2. Procedimento de Remo??o via Interface Portainer

1. Acesse: `https://painel.vpsconexao.org`.
2. Clique em **Stacks** no menu lateral esquerdo.
3. Localize a stack `ecos-devops-infra` e marque a caixa de sele??o ao lado dela.
4. Clique no bot?o vermelho **Delete this stack**.
5. Confirme a exclus?o na janela pop-up.
6. Em menos de 10 segundos, todos os containers da stack ser?o desligados e suas rotas web desativadas.

---

## 3. Limpeza de Volumes Persistentes (Opcional - Libera??o de Disco)

Se voc? n?o planeja reinstalar a stack e deseja liberar espa?o em disco:

1. No menu lateral do Portainer, clique em **Volumes**.
2. No campo de busca/filtro no topo, digite: `ecos-devops-infra_`.
3. Selecione todos os volumes filtrados.
4. Clique em **Remove** e confirme.

---

## 4. Procedimento Alternativo via Linha de Comando (CLI / SSH)

Caso prefira executar via terminal SSH / Termius:

```bash
# 1. Remover a stack do Docker Swarm
docker stack rm ecos-devops-infra

# 2. Aguardar 10 segundos para a finaliza??o dos containers
sleep 10

# 3. (Opcional) Remover volumes da stack
docker volume ls --filter name=ecos-devops-infra -q | xargs -r docker volume rm
```
