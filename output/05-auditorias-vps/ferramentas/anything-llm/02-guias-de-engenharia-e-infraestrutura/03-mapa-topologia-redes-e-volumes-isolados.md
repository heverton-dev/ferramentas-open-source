# Mapa de Topologia de Redes, Ingress e Volumes Persistentes

## 1. Fluxo de Requisicao e Ingress Traefik
1. Requisicao HTTPS chega na porta **443** do no manager da VPS.
2. Traefik inspeciona o cabecalho **Host (SNI)** da requisicao.
3. Certificado TLS e verificado/emitido automaticamente via **letsencryptresolver**.
4. Trafego e roteado internamente pela rede overlay **network_conexao** ate o container de destino na porta interna designada.

## 2. Tabela de Volumes Persistentes
Todos os dados persistentes vivem em volumes Docker gerenciados com alta velocidade:
- Dados de banco de dados e arquivos de usuarios residem em `/var/lib/docker/volumes/`.
- Permissoes internas de escrita isoladas por UID/GID dos containers.
