# Email Corporativo Open-Source: Substituindo Locaweb Email

> **Compêndio Temático Open Source · Camada 99 · Infraestrutura de Email Corporativo Soberano · Padrão Diamante R5**  
> Compêndio determinístico de ferramentas open-source para substituição cirúrgica de Locaweb Email. Análise de 8 soluções maduras cobrindo 5 camadas: infraestrutura de servidor (SMTP/IMAP/POP3), plataforma de gerenciamento (painel admin), integrações (LDAP/AD, antispam, antivírus), segurança (TLS, DKIM, SPF, DMARC) e TCO operacional. Foco: autonomia 100% self-hosted, conformidade LGPD, redundância geográfica e deployabilidade em VPS.

---

## 1. Matriz Comparativa de Ferramentas da Camada

| Rank | Ferramenta | Categoria | Licença | Substitui | Economia Estimada |
| :---: | :--- | :--- | :---: | :--- | :--- |
| 01 | **Mailcow Dockerized** | Email Server Suite | `GPL-3.0` | Locaweb Email / cPanel Webmail / Plesk | R$ 24.000/ano |
| 02 | **Mailu** | Email Server | `MIT` | Locaweb Email / Yandex Mail for Domains | R$ 20.000/ano |
| 03 | **Mail-in-a-Box** | Turnkey Email Solution | `MIT` | Locaweb Email / Google Workspace (solo email) | R$ 15.000/ano |
| 04 | **Postfix + Dovecot (Config Manual)** | MTA/MDA (Manual Setup) | `IPL / MIT` | Locaweb Email / Sendgrid (SMTP relay) | R$ 18.000/ano |
| 05 | **Sovereign** | IaC/Automation | `MIT` | Locaweb Email / iCloud Mail / ProtonMail (infraestrutura proprietária) | R$ 12.000/ano |
| 06 | **Modoboa** | Email Server | `MIT` | Locaweb Email / cPanel Webmail | R$ 16.000/ano |
| 07 | **Cuttlefish** | SMTP Relay | `GPL-3.0` | SendGrid / Mailgun / AWS SES | R$ 8.000/ano |
| 08 | **Haraka** | MTA (Node.js) | `MIT` | Locaweb Email / Postmark (infraestrutura) | R$ 30.000/ano |

---

## 2. Detalhamento Técnico das Ferramentas

### #01 · Mailcow Dockerized — *Suite Completa de Email com Painel Web, Segurança e Failover*

- **Categoria:** Email Server Suite | **Senioridade:** `Intermediário`
- **Licença OSI:** `GPL-3.0`
- **SaaS Proprietário Substituído:** Locaweb Email / cPanel Webmail / Plesk
- **Economia Estimada no TCO:** R$ 24.000/ano

#### 1. O Que Faz & Como Funciona
Stack containerizado completo: Postfix (SMTP), Dovecot (IMAP/POP3), Nginx (webmail), Roundcube (cliente web), SOGo (calendário/contatos), gerenciamento de usuários, antispam (Rspamd), antivírus (ClamAV), certificados Let's Encrypt, backup automático e failover geo-redundante.

*Docker Compose orquestra 12+ containers. Nginx reverse-proxy expõe webmail, Admin UI para gerenciar domínios/mailboxes, Postfix recebe e roteia mensagens, Dovecot autentica e entrega via IMAP/POP3. Rspamd aprende padrões de spam em tempo real. ClamAV escaneia anexos.*

```bash
git clone https://github.com/mailcow/mailcow-dockerized.git && cd mailcow-dockerized && ./generate_config.sh && docker-compose up -d
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** Locaweb Email cobra R$ 180-480/mês por domínio com cota limitada. Para 10 domínios: R$ 24.000/ano.
- **Custo Open Source:** VPS 2 vCPU / 4 GB RAM (R$ 60-120/mês) + backup cloud (R$ 50/mês) = R$ 1.320-2.040/ano.
- **Retorno do Investimento (ROI):** Payback em 2 meses. Economia acumulada no ano: R$ 22.000+.
- **Requisitos de Infra:** 4 GB RAM RAM, 2 vCPU CPU (Banco: MariaDB/MySQL (já incluído no compose))
- **Veredito do Arquiteto:** Padrão-ouro da substituição Locaweb. Stack pronta para produção com segurança certificada (DKIM, SPF, DMARC, TLS), gerenciamento de usuários robusto e suporte ativo da comunidade.
- **Repositório Oficial:** [https://github.com/mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Suite Integrada / UI Incluída` (Roundcube + SOGo + Admin UI customizável)
- **Mecânica de Customização:** Roundcube totalmente personalizável via plugins. Logo, cores e domínio do webmail são configuráveis por usuário/domínio.
- **Impacto em Upgrades:** Releases mensais, breaking changes raros. Upgrade via docker-compose pull && docker-compose up -d.

---

### #02 · Mailu — *Email Server Minimalista com Foco em Simplicidade e Conformidade RGPD*

- **Categoria:** Email Server | **Senioridade:** `Principiante`
- **Licença OSI:** `MIT`
- **SaaS Proprietário Substituído:** Locaweb Email / Yandex Mail for Domains
- **Economia Estimada no TCO:** R$ 20.000/ano

#### 1. O Que Faz & Como Funciona
Stack docker minimalista: Postfix, Dovecot, Rainloop (webmail), gerenciamento de usuários via Admin Web UI, antispam, antivírus integrado. Filosofia: simples, seguro e RGPD-compliant (dados na UE por padrão).

*Docker Compose com 6 containers essenciais. Admin UI permite criar domínios e usuários sem SSH. Nginx expõe webmail com TLS obrigatório. Spamassassin (alternativa ao Rspamd) para filtros de spam customizáveis.*

```bash
docker run -it --rm -v mailu:/data mailu/admin:latest admin create -p your_password admin@example.com
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** R$ 20.000/ano em serviços similares com menor robustez.
- **Custo Open Source:** VPS 1 vCPU / 2 GB RAM (R$ 30-60/mês) = R$ 360-720/ano.
- **Retorno do Investimento (ROI):** Payback em 1-2 meses para deployments pequenos.
- **Requisitos de Infra:** 2 GB RAM RAM, 1 vCPU CPU (Banco: PostgreSQL (incluído))
- **Veredito do Arquiteto:** Solução ideal para PMEs e startups que priorizam simplicidade sobre recursos avançados. RGPD-ready, sem overhead de gerenciamento complexo.
- **Repositório Oficial:** [https://github.com/Mailu/Mailu](https://github.com/Mailu/Mailu)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Minimal / UI Nativa` (Rainloop + Admin Web UI)
- **Mecânica de Customização:** Rainloop permite customização de logo e paleta de cores via configuração. Admin UI é acessível e intuitiva.
- **Impacto em Upgrades:** Releases quadrimestrais estáveis. Upgrade simples via docker-compose pull.

---

### #03 · Mail-in-a-Box — *Email + DNS + Certificados: Turnkey Solution para Não-Sysadmins*

- **Categoria:** Turnkey Email Solution | **Senioridade:** `Principiante`
- **Licença OSI:** `MIT`
- **SaaS Proprietário Substituído:** Locaweb Email / Google Workspace (solo email)
- **Economia Estimada no TCO:** R$ 15.000/ano

#### 1. O Que Faz & Como Funciona
Instalador bash all-in-one que configura email (Postfix/Dovecot), DNS (Nsd), webmail (Roundcube), certificados (Let's Encrypt), backup (B2), antispam (Rspamd) e monitoramento em uma única VPS Ubuntu.

*Script bash automatiza setup completo sem docker. Postfix recebe mensagens, Dovecot entrega via IMAP, Roundcube expõe webmail. Box gerencia DNS records internos para MX, DKIM, SPF. Monitoramento de saúde do servidor.*

```bash
curl https://mailinabox.email/setup.sh | sudo bash
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** R$ 15.000-30.000/ano em soluções gerenciadas.
- **Custo Open Source:** VPS 1 vCPU / 2 GB RAM dedicado (R$ 50-100/mês) = R$ 600-1.200/ano.
- **Retorno do Investimento (ROI):** Payback em 1-2 meses. Ideal para pequenos negócios com 1-5 domínios.
- **Requisitos de Infra:** 2 GB RAM RAM, 1 vCPU CPU (Banco: PostgreSQL + OpenLDAP (instalados via script))
- **Veredito do Arquiteto:** Melhor escolha para entusiastas não-sysadmins. Instalação one-command, interface de admin clara, backup automático no Backblaze B2.
- **Repositório Oficial:** [https://github.com/mail-in-a-box/mailinabox](https://github.com/mail-in-a-box/mailinabox)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Turnkey / UI Admin Incluída` (Roundcube + Admin Control Panel nativo)
- **Mecânica de Customização:** Roundcube oferece temas e plugins para white-label. Admin UI é responsiva.
- **Impacto em Upgrades:** Atualizações automáticas de segurança. Upgrades manuais via painel admin.

---

### #04 · Postfix + Dovecot (Config Manual) — *Stack Clássico de Email para Sysadmins Avançados*

- **Categoria:** MTA/MDA (Manual Setup) | **Senioridade:** `Avançado`
- **Licença OSI:** `IPL / MIT`
- **SaaS Proprietário Substituído:** Locaweb Email / Sendgrid (SMTP relay)
- **Economia Estimada no TCO:** R$ 18.000/ano

#### 1. O Que Faz & Como Funciona
Dupla clássica: Postfix (Mail Transfer Agent) recebe/envia mensagens SMTP, Dovecot (Mail Delivery Agent) autentica usuários e entrega via IMAP/POP3. Requer configuração manual de TLS, DKIM, SPF, DMARC, antispam e backup.

*Instalação via apt-get, configuração de /etc/postfix/ e /etc/dovecot/. Spamd ou Rspamd opcional para antispam. Certificados Let's Encrypt para TLS. Banco de dados (MySQL/PostgreSQL) para gerenciar usuários e domínios.*

```bash
apt-get install postfix dovecot-core dovecot-imapd dovecot-pop3d && postfix-config
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** R$ 18.000/ano em alternativas gerenciadas.
- **Custo Open Source:** VPS 2 vCPU / 2 GB RAM (R$ 60-120/mês) + time de SysAdmin (~5-10h/mês) = R$ 1.440/ano + labor.
- **Retorno do Investimento (ROI):** ROI em 8-12 meses para equipes com expertise interna.
- **Requisitos de Infra:** 2 GB RAM RAM, 1 vCPU CPU (Banco: MySQL/PostgreSQL (externo recomendado))
- **Veredito do Arquiteto:** Gold standard para sysadmins experientes. Máxima flexibilidade, controle granular, integração profunda com LDAP/Active Directory. Exige expertise e monitoramento ativo.
- **Repositório Oficial:** [https://github.com/postfix/postfix](https://github.com/postfix/postfix)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `CLI / Sem UI Nativa (requer Roundcube/Rainloop separado)` (Roundcube ou Rainloop como frontend opcional)
- **Mecânica de Customização:** Requer integração manual de webmail. TLS, DKIM, SPF configuráveis via texto. Exige SSH acesso.
- **Impacto em Upgrades:** Upgrade manual de pacotes. Monitoramento via Nagios/Prometheus recomendado.

---

### #05 · Sovereign — *Orquestrador Ansible para Email Soberano em VPS*

- **Categoria:** IaC/Automation | **Senioridade:** `Avançado`
- **Licença OSI:** `MIT`
- **SaaS Proprietário Substituído:** Locaweb Email / iCloud Mail / ProtonMail (infraestrutura proprietária)
- **Economia Estimada no TCO:** R$ 12.000/ano

#### 1. O Que Faz & Como Funciona
Playbooks Ansible que automatizam deploy de stack completo (Postfix, Dovecot, Roundcube, OpenVPN, Monitoring, Backups) em VPS. Configuração como código, versionável e reproduzível.

*Ansible provisiona servidor bare-metal com playbooks declarativos. Define roles para email, webmail, DNS, firewalls, monitoramento. TLS automático via Let's Encrypt. Backup para S3-compatible storage.*

```bash
git clone https://github.com/sovereign/sovereign.git && ansible-playbook -i hosts site.yml
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** R$ 12.000-24.000/ano em infraestrutura gerenciada equivalente.
- **Custo Open Source:** VPS 2 vCPU / 4 GB RAM (R$ 100/mês) = R$ 1.200/ano + Ansible expertise.
- **Retorno do Investimento (ROI):** Payback em 6-12 meses. ROI amplificado em deployments multi-servidor (replicas, failover).
- **Requisitos de Infra:** 2 GB RAM RAM, 2 vCPU CPU (Banco: PostgreSQL (provisionado via Ansible))
- **Veredito do Arquiteto:** Excelente para equipes DevOps/SRE que já usam Ansible. Infraestrutura como código, versionável em Git. Scaling horizontal facilitado (replica em múltiplos servidores).
- **Repositório Oficial:** [https://github.com/sovereign/sovereign](https://github.com/sovereign/sovereign)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `IaC / Declarativo` (Roundcube + Monitoramento nativo (Kibana/Grafana opcional))
- **Mecânica de Customização:** Playbooks Ansible modulares permitem customização profunda. Stack UI é personalizável via override de variáveis.
- **Impacto em Upgrades:** Versionável em Git. Upgrades via ansible-playbook com idempotência garantida.

---

### #06 · Modoboa — *Email Server Modular com Painel Web Intuitivo & Webmail*

- **Categoria:** Email Server | **Senioridade:** `Intermediário`
- **Licença OSI:** `MIT`
- **SaaS Proprietário Substituído:** Locaweb Email / cPanel Webmail
- **Economia Estimada no TCO:** R$ 16.000/ano

#### 1. O Que Faz & Como Funciona
Suite de email com Postfix, Dovecot, Modoboa Admin (painel web Python/Django), Radicale (caldário/contatos), webmail nativo, antispam integrado, backup automático e relatórios de segurança.

*Python/Django backend gerencia domínios e usuários via REST API. Frontend responsivo para admin e usuários. Docker ou setup manual em CentOS/Ubuntu.*

```bash
pip install modoboa && modoboa-admin.py collectstatic && python manage.py runserver 0.0.0.0:8000
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** R$ 16.000-20.000/ano em plataformas SaaS comparáveis.
- **Custo Open Source:** VPS 2 vCPU / 4 GB RAM (R$ 80/mês) = R$ 960/ano.
- **Retorno do Investimento (ROI):** Payback em 2-3 meses. Escalável horizontalmente.
- **Requisitos de Infra:** 4 GB RAM RAM, 2 vCPU CPU (Banco: PostgreSQL/MySQL)
- **Veredito do Arquiteto:** Ótima alternativa com interface moderna (Python/Django) e comunidade ativa. Suporte comercial disponível (Modoboa SAS). Menos maduro que Mailcow, mas mais intuitivo.
- **Repositório Oficial:** [https://github.com/modoboa/modoboa](https://github.com/modoboa/modoboa)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Web-Based UI / Python Backend` (Django + Bootstrap frontend responsivo)
- **Mecânica de Customização:** UI personalizável via temas. REST API permite extensões customizadas.
- **Impacto em Upgrades:** Releases regulares. Upgrade via pip install --upgrade modoboa.

---

### #07 · Cuttlefish — *SMTP Relay Open-Source com Tracking de Entrega*

- **Categoria:** SMTP Relay | **Senioridade:** `Intermediário`
- **Licença OSI:** `GPL-3.0`
- **SaaS Proprietário Substituído:** SendGrid / Mailgun / AWS SES
- **Economia Estimada no TCO:** R$ 8.000/ano

#### 1. O Que Faz & Como Funciona
SMTP relay gerenciado para aplicações (Ruby on Rails, APIs, etc) enviarem emails sem manter própria infraestrutura MTA. Dashboard de estatísticas, tracking de bounces, retry automático.

*Ruby on Rails backend. Aplicações enviam para localhost:2525, Cuttlefish roteia via DNS MX records. Dashboard oferece analytics de entrega, bounce handling e rate limiting.*

```bash
docker run -d -p 2525:2525 -e CUTTLEFISH_DOMAIN=seu-domain.com 1024mb/cuttlefish
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** SendGrid cobra US$ 0,10 por email ou R$ 150-300/mês para planos PRO. Para 100k/mês: R$ 1.200-3.600/ano.
- **Custo Open Source:** VPS 1 vCPU / 2 GB RAM (R$ 40/mês) = R$ 480/ano.
- **Retorno do Investimento (ROI):** Payback em 1-2 meses para volume alto.
- **Requisitos de Infra:** 1 GB RAM RAM, 1 vCPU CPU (Banco: PostgreSQL (incluído no docker))
- **Veredito do Arquiteto:** Excelente para aplicações que precisam de relay SMTP confiável com tracking. Ideal para SaaS internas, startups e integrações programáticas.
- **Repositório Oficial:** [https://github.com/twentyfortyeight/cuttlefish](https://github.com/twentyfortyeight/cuttlefish)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `SMTP Relay / API Nativa` (Rails Admin Dashboard)
- **Mecânica de Customização:** API REST para integrações. Dashboard oferece basic white-label (logo/colors).
- **Impacto em Upgrades:** Releases ocasionais. Upgrade via docker pull.

---

### #08 · Haraka — *MTA de Alta Performance em Node.js para Volumes Massivos*

- **Categoria:** MTA (Node.js) | **Senioridade:** `Avançado`
- **Licença OSI:** `MIT`
- **SaaS Proprietário Substituído:** Locaweb Email / Postmark (infraestrutura)
- **Economia Estimada no TCO:** R$ 30.000/ano

#### 1. O Que Faz & Como Funciona
MTA escrito em Node.js otimizado para throughput massivo. Suporta plugins para antispam, antivírus, SPF/DKIM/DMARC. Ideal para carriers, ISPs e plataformas de email transacional em escala.

*Baseado em eventos Node.js (async I/O). Plugins modular permite estender funcionalidade sem recompilação. Integração com Redis para queues distribuídas.*

```bash
npm install haraka && haraka -i my-mail-server && haraka -c my-mail-server
```

#### 2. Análise Econômica & Infraestrutura
- **Custo Proprietário:** Plataformas transacionais cobram R$ 0,001-0,01 por email ou R$ 500-5.000/mês para volume alto (1M+/mês).
- **Custo Open Source:** VPS 4 vCPU / 8 GB RAM com Redis (R$ 200/mês) = R$ 2.400/ano.
- **Retorno do Investimento (ROI):** Payback em 1-3 meses para carriers/ISPs com volume >10M emails/mês.
- **Requisitos de Infra:** 4 GB RAM RAM, 4 vCPU CPU (Banco: Redis (recomendado para queues))
- **Veredito do Arquiteto:** Solução enterprise para carriers e plataformas de email em escala. Performance não comparável a MTAs tradicionais. Comunidade ativa, usado por empresas Fortune 500.
- **Repositório Oficial:** [https://github.com/haraka/Haraka](https://github.com/haraka/Haraka)

#### 3. Como Usar no Dia a Dia
1. **Passo 1:** 
2. **Passo 2:** 
3. **Passo 3:** 

#### 4. White-Label & Aderência ao Design System Corporativo
- **Esforço de Customização:** `Headless MTA / Plugins Arquiteturais` (Nenhuma UI nativa (CLI-only ou integração customizada))
- **Mecânica de Customização:** Plugins Node.js permitem customização ilimitada. Requer expertise JavaScript.
- **Impacto em Upgrades:** Releases frequentes. Upgrade via npm update haraka.

---

## 3. Governança e Diretrizes de Adoção Corporativa

1. **Soberania Operacional:** 100% das ferramentas catalogadas operam sob licenças OSI livres de royalties para uso corporativo.
2. **Isolamento na VPS:** A implantação recomendada utiliza contêineres Docker isolados com rede interna e proxy reverso Caddy/Traefik com HTTPS automático.
3. **Desinstalação Cirúrgica:** A esteira garante que qualquer ferramenta pode ser removida da infraestrutura sem afetar outros contêineres ou bancos do servidor.