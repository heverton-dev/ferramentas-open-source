# Cadastro de Monitoramento no Uptime Kuma

## 1. Configuracao de Sondas HTTP(s)
Para cada servico da stack, cadastre uma sonda no seu Uptime Kuma (`https://monitor.vpsconexao.org`):
1. **Tipo de Monitor:** HTTP(s).
2. **Nome:** `Ecossistema google-workspace - App Principal`.
3. **URL:** `https://app.vpsconexao.org`.
4. **Intervalo de Checagem:** 60 segundos.
5. **Notificacoes:** Configure alerta via Telegram, Discord ou e-mail.
