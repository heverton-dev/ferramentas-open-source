# Cadastro de Monitoramento no Uptime Kuma

## 1. Configuração de Sondas HTTP(s)
Para cada serviço da stack, cadastre uma sonda no seu Uptime Kuma (`https://monitor.vpsconexao.org`):
1. **Tipo de Monitor:** HTTP(s).
2. **Nome:** `AnythingLLM Enterprise - App Principal`.
3. **URL:** `https://ai.vpsconexao.org`.
4. **Intervalo de Checagem:** 60 segundos.
5. **Notificações:** Configure alerta via Telegram, Discord ou e-mail.
