# Manual de Desinstala??o Cir?rgica e Rollback

**Alvo:** CryptPad  
**Garantia de Isolamento:** 100% de preserva??o dos demais containers da VPS  
**Tempo de Execu??o:** Menos de 10 segundos

---

## 1. Princ?pios de Seguran?a e Isolamento

Todos os recursos criados para o alvo `CryptPad` foram encapsulados no namespace `cryptpad`.
A remo??o da stack desconecta os servi?os da rede `network_conexao` e revoga os roteadores do Traefik de forma at?mica.
**Mautic, Evolution, n8n, MySQL, PostgreSQL global e Portainer continuam operando normalmente sem nenhuma interrup??o.**

---

## 2. Procedimento 1: Remo??o via Painel Portainer (Interface Gr?fica)

1. Acesse: `https://painel.vpsconexao.org`.
2. Clique em **Stacks** no menu lateral esquerdo.
3. Localize a stack `cryptpad` e marque a caixa de sele??o ao lado dela.
4. Clique no bot?o vermelho **Delete this stack**.
5. Confirme a exclus?o na janela pop-up.
6. Em menos de 10 segundos, todos os containers ser?o finalizados e as rotas web desligadas.

---

## 3. Procedimento 2: Remo??o via Linha de Comando (CLI / SSH)

Caso prefira executar via terminal SSH ou Termius:

```bash
# 1. Remover a stack do Docker Swarm
docker stack rm cryptpad

# 2. Aguardar 10 segundos para finalizacao completa dos processos
sleep 10

# 3. Verificar que as demais stacks continuam 100% operacionais
docker stack ls
docker service ls
```

---

## 4. Limpeza Opcional de Volumes Persistentes (Libera??o de Disco)

Se voc? n?o planeja restaurar a aplica??o e deseja liberar espa?o em disco:

```bash
# Listar e remover apenas os volumes exclusivos da stack removida
docker volume ls --filter name=cryptpad -q | xargs -r docker volume rm
```

*(Nenhum volume do Mautic, n8n, PostgreSQL global ou MySQL ser? afetado).*
