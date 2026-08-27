# Guia Universal de Deploy da Documentação Soberana (output/)

> **Pasta Soberana de Publicação:** `output/`  
> **Filosofia:** Zero Duplicação de Arquivos · Publicação Direta e Leve

---

## 1. GitHub Pages (Automatizado via Action)

O arquivo [`.github/workflows/deploy-pages.yml`](file:///C:/Users/trcnologia/orca/projects/open-source/.github/workflows/deploy-pages.yml) já está configurado.
1. No repositório GitHub, vá em **Settings** ➔ **Pages**;
2. Em **Build and deployment** ➔ **Source**, selecione **GitHub Actions**;
3. Todo commit na branch `main` publicará automaticamente o conteúdo de `output/`.

---

## 2. Cloudflare Pages (Grátis, Global & Instantâneo)

1. No painel da Cloudflare, vá em **Workers & Pages** ➔ **Create Application** ➔ **Pages**;
2. Conecte seu repositório Git;
3. Em **Build settings**:
   - **Framework preset:** `None`;
   - **Build command:** *(deixe em branco)*;
   - **Build output directory:** `output`.
4. Clique em **Save and Deploy**. A documentação será servida na CDN global da Cloudflare.

---

## 3. Vercel

1. Importe o projeto no painel da Vercel;
2. Em **Project Settings** ➔ **General**:
   - **Output Directory:** `output`;
3. Deploy imediato com suporte a HTTPS e domínios customizados.

---

## 4. VPS Própria (Nginx / Caddy / Docker)

### Via Caddy (HTTPS Automático):
```caddyfile
docs.seudominio.com.br {
    root * /caminho/do/projeto/output
    file_server
}
```

### Via Nginx:
```nginx
server {
    listen 80;
    server_name docs.seudominio.com.br;
    root /caminho/do/projeto/output;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```
