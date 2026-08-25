# -*- coding: utf-8 -*-
"""
Atualiza o Hub Central (index.html) com todas as 49 Camadas e Compêndios de Soberania Tecnológica.
"""
import os
import re
import sys
from bs4 import BeautifulSoup

def console_utf8():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

console_utf8()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "listas-open-source")
DOCS_DIR = os.path.join(BASE_DIR, "docs", "listas")

COMPENDIOS_EXTRA = [
    {
        "num": "40", "arquivo": "40-alcance-proprio.html", "categoria": "Marketing & Mensageria",
        "titulo": "Alcance Próprio: Marketing, E-mail & Audiência Soberana",
        "stack": "Postal, Stalwart, Mailcow, Mautic, Listmonk, Ghost, Novu, Plausible, Umami, Shlink.",
        "econ": "Economia: -$ 5.000 a $ 30.000 / ano (Zero taxas por contato)"
    },
    {
        "num": "41", "arquivo": "41-arsenal-do-engenheiro-ia.html", "categoria": "Engenharia de IA",
        "titulo": "Arsenal do Engenheiro de IA: O Stack Completo de Autonomia",
        "stack": "LiteLLM, vLLM, Ollama, Qdrant, FastEmbed, Aider, Cline, CrewAI, Langfuse, Guardrails AI.",
        "econ": "Economia: -$ 20.000 a $ 80.000 / ano (Faturas de APIs e Ferramentas)"
    },
    {
        "num": "42", "arquivo": "42-caixa-aberto.html", "categoria": "Finanças & Fiscal",
        "titulo": "Caixa Aberto: Finanças, Faturamento & Assinaturas Soberanas",
        "stack": "BTCPayServer, SolidInvoice, Akaunting, Lago, Kill Bill, Invoice Ninja, Firefly III, Kresus.",
        "econ": "Economia: Zero comissões de gateway + -$ 12.000 / ano em SaaS financeiro"
    },
    {
        "num": "43", "arquivo": "43-chao-de-fabrica.html", "categoria": "Indústria & Hardware",
        "titulo": "Chão de Fábrica: Hardware Aberto, CAD, EDA & Firmware",
        "stack": "FreeCAD, KiCad, OpenSCAD, LibrePCB, OrcaSlicer, FreeRTOS, Zephyr, ESP-IDF, Klipper.",
        "econ": "Economia: -$ 10.000 a $ 50.000 / ano (Licenças proprietárias CAD/EDA)"
    },
    {
        "num": "44", "arquivo": "44-codigo-autonomo.html", "categoria": "Programação & Autonomia",
        "titulo": "Código Autônomo: Compiladores, WebAssembly & Agentes Coder",
        "stack": "Wasmtime, Wasmer, LLVM, Zig, Rust, Tree-sitter, Aider, OpenHands, Cline, Continue.",
        "econ": "Economia: -$ 2.400 / dev / ano (Copilot, Cursor e IDEs fechadas)"
    },
    {
        "num": "45", "arquivo": "45-fonte-limpa.html", "categoria": "Dados & Scraping",
        "titulo": "Fonte Limpa: Scraping Furtivo, Extração & Ingestão de Dados",
        "stack": "Crawl4AI, Scrapy, Crawlee, Docling, Unstructured, Playwright, Selenium, Trafilatura.",
        "econ": "Economia: -$ 5.000 a $ 40.000 / ano (APIs pagas de scraping e dados)"
    },
    {
        "num": "46", "arquivo": "46-linha-direta.html", "categoria": "Comunicação & Chat",
        "titulo": "Linha Direta: Comunicação Segura, Atendimento & Telefonia",
        "stack": "Chatwoot, Evolution API, Rocket.Chat, Mattermost, Matrix/Synapse, Asterisk, FreePBX.",
        "econ": "Economia: -$ 30.000 a $ 100.000 / ano (Zendesk, Slack, Blip e PABX)"
    },
    {
        "num": "47", "arquivo": "47-peso-e-watt.html", "categoria": "Edge AI & IoT",
        "titulo": "Peso & Watt: IA na Borda, Microcontroladores & Eficiência Extrema",
        "stack": "ExecuTorch, MediaPipe, MLX, Llama.cpp, WhisperKit, LiteRT, NCNN, MNN, Sherpa-ONNX.",
        "econ": "Economia: 100% Offline · Zero custos de banda e inferência em nuvem"
    },
    {
        "num": "48", "arquivo": "48-titas-da-soberania.html", "categoria": "Grandes Infraestruturas",
        "titulo": "Titãs da Soberania: Os 25 Maiores Projetos Open Source do Mundo",
        "stack": "Linux, PostgreSQL, Kubernetes, Redis, Docker, Apache Kafka, DuckDB, vLLM, Keycloak, Supabase.",
        "econ": "Economia: A fundação que economiza bilhões de dólares para o planeta"
    },
    {
        "num": "49", "arquivo": "49-troca-livre.html", "categoria": "Redes & P2P",
        "titulo": "Troca Livre: Redes Descentralizadas, P2P & Armazenamento",
        "stack": "IPFS/Kubo, Libp2p, Syncthing, Nostr, MinIO, Seafile, BitTorrent, Tor, I2P, Yggdrasil.",
        "econ": "Economia: Soberania total contra censura, bloqueios e lock-in de nuvem"
    }
]

def atualizar_index(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    grid = soup.find("div", class_="grid")
    if not grid:
        return

    # Verificar se ja tem os cards 40 a 49
    existentes = [a.get("href") for a in grid.find_all("a", class_="card-link")]
    
    for c in COMPENDIOS_EXTRA:
        if c["arquivo"] not in existentes:
            card_html = f"""
    <a class="card-link" href="{c['arquivo']}">
      <div class="card">
        <div class="card-top"><span class="card-num">{c['num']}</span><span class="card-camada">{c['categoria']}</span></div>
        <h3>{c['titulo']}</h3>
        <p>{c['stack']}</p>
        <div class="card-econ">{c['econ']}</div>
      </div>
    </a>
"""
            grid.append(BeautifulSoup(card_html, "html.parser"))

    # Atualizar footer
    footer = soup.find("footer")
    if footer:
        footer.clear()
        footer.append(BeautifulSoup("<p>Enciclopédia de Soberania Tecnológica gerada pela Fábrica Universal. Todos os 49 compêndios contam com auditoria de licenças OSI, conformidade R5 (Dossiê Executivo) e design editorial padronizado.</p>", "html.parser"))

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"[✓] Hub Central atualizado com 49 camadas em: {filepath}")

def main():
    atualizar_index(os.path.join(OUTPUT_DIR, "index.html"))
    atualizar_index(os.path.join(DOCS_DIR, "index.html"))
    print("\n[OK] Todos os índices atualizados com sucesso!")

if __name__ == "__main__":
    main()
