# Manual de Desinstalação Cirúrgica e Rollback

**Alvo:** Ferramenta buzz  
**Garantia de Isolamento:** 100% de preservação dos demais containers da VPS  
**Tempo de Execução:** Menos de 10 segundos

---

## 1. Princípios de Segurança e Isolamento

Todos os recursos criados para o alvo `Ferramenta buzz` foram encapsulados no namespace `buzz`.
A remoção da stack desconecta os serviços da rede `network_conexao` e revoga os roteadores do Traefik de forma atômica.
**Mautic, Evolution, n8n, MySQL, PostgreSQL global e Portainer continuam operando normalmente sem nenhuma interrupção.**

---

## 2. Procedimento 1: Remoção via Painel Portainer (Interface Gráfica)

1. Acesse: `https://painel.vpsconexao.org`.
2. Clique em **Stacks** no menu lateral esquerdo.
3. Localize a stack `buzz` e marque a caixa de seleção ao lado dela.
4. Clique no botão vermelho **Delete this stack**.
5. Confirme a exclusão na janela pop-up.
6. Em menos de 10 segundos, todos os containers serão finalizados e as rotas web desligadas.

---

## 3. Procedimento 2: Remoção via Linha de Comando (CLI / SSH)

Caso prefira executar via terminal SSH ou Termius:

```bash
# 1. Remover a stack do Docker Swarm
docker stack rm buzz

# 2. Aguardar 10 segundos para finalização completa dos processos
sleep 10

# 3. Verificar que as demais stacks continuam 100% operacionais
docker stack ls
docker service ls
```

---

## 4. Limpeza Opcional de Volumes Persistentes (Liberação de Disco)

Se você não planeja restaurar a aplicação e deseja liberar espaço em disco:

```bash
# Listar e remover apenas os volumes exclusivos da stack removida
docker volume ls --filter name=buzz -q | xargs -r docker volume rm
```

*(Nenhum volume do Mautic, n8n, PostgreSQL global ou MySQL será afetado).*
