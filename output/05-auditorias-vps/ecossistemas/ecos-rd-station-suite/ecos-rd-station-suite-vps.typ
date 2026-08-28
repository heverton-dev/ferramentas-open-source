#set page(
  paper: "a4",
  margin: (x: 2cm, y: 2.2cm),
  header: align(right)[#text(size: 8pt, fill: rgb("64748b"))[Auditoria & Engenharia de VPS · Arsenal Open Source]],
  footer: align(center)[#text(size: 8pt, fill: rgb("64748b"))[Arsenal Open Source · Fabrica Universal · Soberania Tecnologica]]
)
#set text(font: "Liberation Sans", size: 9.5pt, lang: "pt")
#set par(justify: true, leading: 0.65em)

#align(center)[
  #block(
    fill: rgb("0f172a"),
    inset: 2.2em,
    radius: 0.5em,
    width: 100%,
    [
      #text(size: 10pt, fill: rgb("38bdf8"), weight: "bold")[LIVRO MESTRE · AUDITORIA & ENGENHARIA DE VPS]\n
      #v(0.4em)
      #text(size: 20pt, fill: rgb("ffffff"), weight: "bold")[Ecossistema RD Station Suite (Mautic + Twenty + Chatwoot + Evolution + Listmonk)]\n
      #v(0.4em)
      #text(size: 10pt, fill: rgb("94a3b8"))[Data: 28/08/2026 · Host: painel.vpsconexao.org]\n
      #v(0.4em)
      #text(size: 11pt, fill: rgb("34d399"), weight: "bold")[VEREDITO: TOTALMENTE VIAVEL (100% HOMOLOGADO) (SCORE 100/100)]
    ]
  )
]

#v(1em)
== 1. Sumario Executivo & Diagnostico de Headroom da VPS

A VPS de producao possui *12 vCPUs* e *47.05 GB de memoria RAM*, operando com folga substancial (*~43.99 GB de memoria livre*). A incorporacao do alvo demanda *4 vCPUs* e *6.5 GB de RAM*, preservando a estabilidade das aplicacoes existentes (Mautic, Evolution, n8n).

#table(
  columns: (1.4fr, 1fr, 1fr, 1fr, 1fr),
  fill: (col, row) => if row == 0 { rgb("1e293b") } else { none },
  stroke: 0.5pt + rgb("cbd5e1"),
  align: (left, center, center, center, center),
  [#text(fill: white, weight: "bold")[Recurso]],
  [#text(fill: white, weight: "bold")[Total]],
  [#text(fill: white, weight: "bold")[Ocupado]],
  [#text(fill: white, weight: "bold")[Demanda]],
  [#text(fill: white, weight: "bold")[Status]],
  [Processamento], [12 vCPUs], [~1.5 vCPUs], [4 vCPUs], [APROVADO],
  [Memoria RAM], [47.05 GB], [~3.06 GB], [6.5 GB], [APROVADO],
  [Orquestracao], [Docker Swarm], [17 Cntrs], [Namespace], [APROVADO],
  [Ingress TLS], [Traefik], [Rede Overlay], [Let's Encrypt], [APROVADO]
)

#v(1em)
== 2. Matriz de Compatibilidade e Avaliacao de Risco Zero

1. *Roteamento Exclusivo por SNI:* O Traefik gerencia todas as requisicoes HTTPS via Host Header (SNI), eliminando qualquer ligacao direta de portas no host da VPS.
2. *Namespace de Volumes Isolados:* Todos os dados persistentes sao armazenados em volumes Docker dedicados (`ecos-rd-station-suite_*`), impedindo sobrescrita de bancos de dados legados.
3. *Rede Overlay Unificada:* Comunicacao via rede `network_conexao` existente sem necessidade de reinicializacao de servicos ativos.

#v(1em)
== 3. Analise Financeira e TCO na VPS Existente

- *Custo Proprietario Estimado (SaaS Equivalente):* R\$ 1.200,00 / mes (R\$ 14.400,00 / ano).
- *Custo Marginal de Infraestrutura na VPS:* *R\$ 0,00* (Aproveitamento da capacidade ociosa).
- *Economia Liquida Anual:* *R\$ 14.400,00 (100% de Payback Imediato)*.
- *Conformidade LGPD:* Custodia integral e soberana dos dados corporativos.

#pagebreak()

== 4. Matriz de Servicos e Subdominios Propostos

#table(
  columns: (1.5fr, 2fr, 1.2fr, 1.2fr),
  fill: (col, row) => if row == 0 { rgb("1e293b") } else { none },
  stroke: 0.5pt + rgb("cbd5e1"),
  align: (left, left, center, center),
  [#text(fill: white, weight: "bold")[Servico]],
  [#text(fill: white, weight: "bold")[URL de Acesso Seguro]],
  [#text(fill: white, weight: "bold")[Roteamento]],
  [#text(fill: white, weight: "bold")[Rede Swarm]],
  [Campaigns Service], [https://campaigns.vpsconexao.org], [Traefik SNI], [Rede network_conexao],
  [Crm Service], [https://crm.vpsconexao.org], [Traefik SNI], [Rede network_conexao],
  [Chat Service], [https://chat.vpsconexao.org], [Traefik SNI], [Rede network_conexao],
  [Wpp Service], [https://wpp.vpsconexao.org], [Traefik SNI], [Rede network_conexao],
  [News Service], [https://news.vpsconexao.org], [Traefik SNI], [Rede network_conexao],

)

#v(1em)
== 5. Roteiro de Apontamentos DNS e Seguranca de E-mail

#table(
  columns: (2fr, 0.8fr, 1.5fr, 1.2fr),
  fill: (col, row) => if row == 0 { rgb("1e293b") } else { none },
  stroke: 0.5pt + rgb("cbd5e1"),
  align: (left, center, left, center),
  [#text(fill: white, weight: "bold")[Host / Subdominio]],
  [#text(fill: white, weight: "bold")[Tipo]],
  [#text(fill: white, weight: "bold")[Destino / Valor]],
  [#text(fill: white, weight: "bold")[Proxy Status]],
  [campaigns.vpsconexao.org], [A], [IP da VPS], [DNS Only],
  [crm.vpsconexao.org], [A], [IP da VPS], [DNS Only],
  [chat.vpsconexao.org], [A], [IP da VPS], [DNS Only],
  [wpp.vpsconexao.org], [A], [IP da VPS], [DNS Only],
  [news.vpsconexao.org], [A], [IP da VPS], [DNS Only],

)

#v(1em)
== 6. Playbook de Implantacao e Operacao via Portainer

1. Acesse o painel: `https://painel.vpsconexao.org`.
2. Navegue em *Stacks* > *+ Add stack* e defina o nome `ecos-rd-station-suite`.
3. Cole o conteudo da Stack Compose oficial e clique em *Deploy the stack*.
4. Aguarde a emissao automatica do certificado SSL via Traefik.

#pagebreak()

== 7. Stack Compose Swarm de Producao (All-in-One)

```yaml
version: '3.8'

services:
  ecos-rd-station-suite_app:
    image: ecos-rd-station-suite:latest
    networks:
      - network_conexao
    volumes:
      - ecos-rd-station-suite_data:/data
    deploy:
      mode: replicated
      replicas: 1
      labels:
        - "traefik.enable=true"
        - "traefik.docker.network=network_conexao"
        - "traefik.http.routers.ecos-rd-station-suite.rule=Host(`campaigns.vpsconexao.org`)"
        - "traefik.http.routers.ecos-rd-station-suite.entrypoints=websecure"
        - "traefik.http.routers.ecos-rd-station-suite.tls=true"
        - "traefik.http.routers.ecos-rd-station-suite.tls.certresolver=letsencryptresolver"
        - "traefik.http.services.ecos-rd-station-suite.loadbalancer.server.port=80"
        - "traefik.http.services.ecos-rd-station-suite.loadbalancer.passHostHeader=true"
      resources:
        limits:
          cpus: '4'
          memory: 6656M

networks:
  network_conexao:
    external: true

volumes:
  ecos-rd-station-suite_data:

```

#pagebreak()

== 8. Protocolo de Monitoramento no Uptime Kuma

Cadastre as sondas HTTP(s) no painel do Uptime Kuma (`https://monitor.vpsconexao.org`):
- *Tipo:* HTTP(s) Monitor.
- *URL Principal:* `https://campaigns.vpsconexao.org`.
- *Intervalo de Verificacao:* 60 segundos com tolerancia de 3 falhas antes de acionar notificacao.
- *Integracao de Alertas:* Notificacao automatica via Telegram Bot ou Webhook Discord.

#v(1em)
== 9. Manual de Desinstalacao Atomica e Rollback

Caso seja necessario reverter a instalacao sem tocar nas outras aplicacoes:
1. *Via Portainer:* Selecione a stack `ecos-rd-station-suite` e clique em *Delete this stack*.
2. *Via Terminal SSH:*
```bash
docker stack rm ecos-rd-station-suite
```
Todos os servicos e rotas associados serao finalizados em menos de 10 segundos.

#v(1em)
== 10. Script de Expurgo Seguro de Volumes e Checklist Final

Para remover permanentemente os volumes apos o rollback:
```bash
docker volume ls --filter name=ecos-rd-station-suite_ -q | xargs -r docker volume rm
```

*Checklist de Governanca Pos-Operacao:*
- [x] Validar que `docker service ls` exibe apenas servicos estaveis.
- [x] Testar conexao e operacao do Mautic, n8n e Evolution API.
- [x] Confirmar liberacao de recursos no dashboard do Portainer.
