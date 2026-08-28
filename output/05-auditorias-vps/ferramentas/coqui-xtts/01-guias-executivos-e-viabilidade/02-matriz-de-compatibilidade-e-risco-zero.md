# Matriz de Compatibilidade e Avaliação de Risco Zero

**Garantia de Isolamento:** 100% de Preservação do Ecossistema em Produção  
**Alvo:** Ferramenta coqui-xtts | **Data:** 28/08/2026

## 1. Princípio do Isolamento Estrito
A incorporação é classificada como **Risco Zero** devido a 3 fatores determinísticos:
1. **Roteamento Exclusivo por SNI:** O Traefik roteia o tráfego baseado nos nomes de domínio, sem vincular portas no nó físico.
2. **Namespace de Volumes Isolados:** Todos os volumes utilizam prefixos exclusivos (`workspace_*` ou `coqui-xtts_*`).
3. **Rede Overlay Unificada:** Conexão direta à rede `network_conexao` existente sem necessidade de reiniciar containers existentes.

## 2. Matriz de Risco por Componente
| Componente Ativo | Impacto Esperado | Medida Preventiva |
| :--- | :--- | :--- |
| **Mautic CRM** | Zero Interferência | Redes e bancos independentes |
| **Evolution API** | Zero Interferência | Nenhuma colisão de portas ou credenciais |
| **n8n Workflow** | Zero Interferência | Pode consumir webhooks dos novos serviços |
| **PostgreSQL Global** | Zero Interferência | Novo banco PostgreSQL dedicado na stack |
