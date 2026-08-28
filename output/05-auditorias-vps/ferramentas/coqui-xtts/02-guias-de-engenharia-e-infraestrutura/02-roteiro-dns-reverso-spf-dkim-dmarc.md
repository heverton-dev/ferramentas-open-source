# Roteiro de Configuração de DNS, SPF, DKIM e DMARC

## 1. Apontamentos de Zona DNS (Registros A)
Cadastre na sua zona de DNS (Cloudflare, Registro.br ou Route53):

| Subdomínio / Host | Tipo | Destino / Valor | Observação |
| :--- | :--- | :--- | :--- |
| `coqui-xtts.vpsconexao.org` | A | IP da VPS | DNS Only (Nuvem Cinza inicial) |

## 2. Registros para Servidor de E-mail (Se Aplicável)
- **Registro MX:** `mail.vpsconexao.org` -> Prioridade 10
- **Registro TXT (SPF):** `v=spf1 mx a:mail.vpsconexao.org ~all`
- **Registro TXT (DMARC):** `_dmarc.vpsconexao.org` -> `v=DMARC1; p=quarantine; rua=mailto:admin@vpsconexao.org`
- **Registro TXT (DKIM):** Gerado automaticamente no painel web do servidor de e-mail.
