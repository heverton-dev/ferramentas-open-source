# Mapa de Topologia de Redes, Ingress e Volumes Persistentes

## 1. Fluxo de Requisição e Ingress Traefik
1. Requisição HTTPS chega na porta **443** do nó manager da VPS.
2. Traefik inspeciona o cabeçalho **Host (SNI)** da requisição.
3. Certificado TLS é verificado e emitido automaticamente via **letsencryptresolver**.
4. Tráfego é roteado internamente pela rede overlay **network_conexao** até o container de destino na porta interna designada.

## 2. Tabela de Volumes Persistentes
Todos os dados persistentes vivem em volumes Docker gerenciados com alta velocidade:
- Dados de banco de dados e arquivos de usuários residem em `/var/lib/docker/volumes/`.
- Permissões internas de escrita isoladas por UID/GID dos containers.
