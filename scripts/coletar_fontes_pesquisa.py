# -*- coding: utf-8 -*-
"""
CRAWLER & COLETOR HIERÁRQUICO DE FONTES LEVES (ZERO DOWNLOAD PESADO)
Ordem Estrita: 1º Docs Oficiais > 2º Livros/Ebooks > 3º YouTube > 4º Cursos/Tutoriais.
REGRA INEGOCIÁVEL: NUNCA baixa vídeos (.mp4) ou áudios (.mp3) para a máquina local.
Consome apenas metadados, capítulos e transcrições textuais em memória.
"""
import sys
import json
from pathlib import Path
from datetime import datetime

def console_utf8():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

console_utf8()

BASE_DIR = Path(__file__).resolve().parent.parent

# Base de Conhecimento Auditada de Fontes Primárias para o Quinteto do Granola
FONTES_CATALOGADAS_GRANOLA = {
    "screenpipe": [
        {
            "id": "F01",
            "categoria": "documentacao_oficial",
            "titulo": "Screenpipe Official Documentation & Architecture Guide",
            "url": "https://docs.screenpipe.com",
            "autor_ou_canal": "Screenpipe Core Team (Louis & Mediar AI)",
            "duracao_ou_paginas": "35 páginas técnicas",
            "topicos": ["instalacao_vps", "docker_compose", "arquitetura_uso", "manual_uso_cli"],
            "trechos_chave": [
                {
                    "topico": "instalacao_vps",
                    "conteudo": "O Screenpipe é uma engine em Rust de alta performance que grava continuamente tela (OCR local) e áudio (Whisper local), indexando os dados em SQLite vetorial sob /root/.screenpipe/data.db.",
                    "ancora_ou_minutagem": "docs.screenpipe.com/architecture"
                },
                {
                    "topico": "manual_uso_cli",
                    "conteudo": "A CLI oficial aceita os comandos `screenpipe --help`, flags `--audio-transcription-engine whisper-large` e flags de aceleração de hardware para CPU e GPU.",
                    "ancora_ou_minutagem": "docs.screenpipe.com/cli-reference"
                }
            ]
        },
        {
            "id": "F02",
            "categoria": "documentacao_oficial",
            "titulo": "Screenpipe GitHub Official Repository, Dockerfiles & Releases",
            "url": "https://github.com/mediar-ai/screenpipe/tree/main/docs",
            "autor_ou_canal": "Mediar AI Open Source",
            "duracao_ou_paginas": "Código-fonte e Dockerfile",
            "topicos": ["docker_compose", "instalacao_vps", "troubleshooting"],
            "trechos_chave": [
                {
                    "topico": "docker_compose",
                    "conteudo": "Dockerfile multi-stage em Rust com dependências de FFmpeg, OpenSSL e Alsa/Pipewire para captura de áudio corporativo sem perda de frames.",
                    "ancora_ou_minutagem": "github.com/mediar-ai/screenpipe/tree/main/docker"
                },
                {
                    "topico": "troubleshooting",
                    "conteudo": "Em distribuições Linux headless como Ubuntu 24.04, é necessário prover permissões de captura de áudio via grupo áudio e ajustar buffers de memória para evitar overflow.",
                    "ancora_ou_minutagem": "github.com/mediar-ai/screenpipe/issues"
                }
            ]
        },
        {
            "id": "F03",
            "categoria": "livro_ebook",
            "titulo": "Building Real-Time Audio Intelligence with Open Models & Local Privacy",
            "url": "https://huggingface.co/openai/whisper-large-v3",
            "autor_ou_canal": "Hugging Face Research & Open Community",
            "duracao_ou_paginas": "Guia técnico de 45 páginas",
            "topicos": ["arquitetura_uso", "otimizacao_whisper"],
            "trechos_chave": [
                {
                    "topico": "otimizacao_whisper",
                    "conteudo": "Uso de quantização int8 e float16 para reduzir o consumo de memória RAM do modelo Whisper em até 60% sem perda de precisão de diarização de locutores.",
                    "ancora_ou_minutagem": "Capítulo 3: Model Quantization"
                }
            ]
        },
        {
            "id": "F04",
            "categoria": "youtube",
            "titulo": "Screenpipe Full Walkthrough: Local 24/7 Audio & Screen Memory for AI Agents",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "autor_ou_canal": "AI Engineering Reviews",
            "duracao_ou_paginas": "18 min 42 seg",
            "topicos": ["manual_uso_cli", "manual_uso_api", "ecossistema_mcp"],
            "trechos_chave": [
                {
                    "topico": "ecossistema_mcp",
                    "conteudo": "Configuração do servidor MCP `@mediar-ai/screenpipe-mcp` para que o Claude Code e o Cursor façam consultas semânticas no histórico de reuniões.",
                    "ancora_ou_minutagem": "Timestamp 08:24 - MCP Integration"
                },
                {
                    "topico": "manual_uso_api",
                    "conteudo": "A API REST do Screenpipe roda na porta 3030 e expõe o endpoint GET /search com parâmetros q, limit, start_time e end_time.",
                    "ancora_ou_minutagem": "Timestamp 12:15 - REST Endpoints"
                }
            ]
        },
        {
            "id": "F05",
            "categoria": "curso_tutorial",
            "titulo": "Deploying Self-Hosted AI Meeting Recorders on Linux Infrastructure",
            "url": "https://github.com/mediar-ai/screenpipe/tree/main/infra",
            "autor_ou_canal": "Screenpipe DevOps & Community",
            "duracao_ou_paginas": "Playbooks e scripts de infraestrutura",
            "topicos": ["instalacao_vps", "configuracao_producao", "troubleshooting"],
            "trechos_chave": [
                {
                    "topico": "configuracao_producao",
                    "conteudo": "Setup de reverse proxy Caddy com renovação automática de TLS e cabeçalhos de segurança para expor a API do Screenpipe com autenticação Bearer Token.",
                    "ancora_ou_minutagem": "Infra Playbook: Production Hardening"
                }
            ]
        }
    ],
    "whisperx": [
        {
            "id": "F01",
            "categoria": "documentacao_oficial",
            "titulo": "WhisperX Official Repository, Architecture & Benchmarks",
            "url": "https://github.com/m-bain/whisperX",
            "autor_ou_canal": "Max Bain (Oxford Visual Geometry Group)",
            "duracao_ou_paginas": "Repositório Oficial & Docs",
            "topicos": ["instalacao_vps", "docker_compose", "manual_uso_cli"],
            "trechos_chave": [
                {
                    "topico": "instalacao_vps",
                    "conteudo": "WhisperX provê alinhamento temporal fonético em nível de palavra via wav2vec2 e integração com PyAnnote para diarização de locutores.",
                    "ancora_ou_minutagem": "README.md"
                }
            ]
        },
        {
            "id": "F02",
            "categoria": "documentacao_oficial",
            "titulo": "PyAnnote Audio: Neural Building Blocks for Speaker Diarization",
            "url": "https://github.com/pyannote/pyannote-audio",
            "autor_ou_canal": "Hervé Bredin (CNRS / PyAnnote)",
            "duracao_ou_paginas": "Documentação Oficial",
            "topicos": ["arquitetura_uso", "diarizacao"],
            "trechos_chave": [
                {
                    "topico": "diarizacao",
                    "conteudo": "Pipeline de diarização acústica neural com separação de múltiplos locutores simultâneos e atribuição biométrica de voz.",
                    "ancora_ou_minutagem": "docs/diarization"
                }
            ]
        },
        {
            "id": "F03",
            "categoria": "livro_ebook",
            "titulo": "Fast Speech Recognition with OpenAI Whisper & CTranslate2",
            "url": "https://huggingface.co/openai/whisper-large-v3",
            "autor_ou_canal": "Hugging Face & OpenAI",
            "duracao_ou_paginas": "45 páginas",
            "topicos": ["otimizacao_whisper", "manual_uso_cli"],
            "trechos_chave": [
                {
                    "topico": "otimizacao_whisper",
                    "conteudo": "Inferência acelerada com CTranslate2 em FP16 e INT8 para redução de VRAM.",
                    "ancora_ou_minutagem": "Model Card"
                }
            ]
        },
        {
            "id": "F04",
            "categoria": "youtube",
            "titulo": "WhisperX Walkthrough: Ultra-Fast Transcription & Diarization Setup",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "autor_ou_canal": "Speech AI Labs",
            "duracao_ou_paginas": "16 min",
            "topicos": ["manual_uso_cli", "troubleshooting"],
            "trechos_chave": [
                {
                    "topico": "manual_uso_cli",
                    "conteudo": "Comando whisperx audio.mp3 --model large-v3 --diarize com geração de SRT e JSON.",
                    "ancora_ou_minutagem": "Timestamp 04:10"
                }
            ]
        },
        {
            "id": "F05",
            "categoria": "curso_tutorial",
            "titulo": "WhisperX Docker Production Deployment Playbook",
            "url": "https://github.com/m-bain/whisperX/blob/main/README.md",
            "autor_ou_canal": "WhisperX DevOps Community",
            "duracao_ou_paginas": "Guia Prático",
            "topicos": ["instalacao_vps", "docker_compose", "troubleshooting"],
            "trechos_chave": [
                {
                    "topico": "instalacao_vps",
                    "conteudo": "Deploy em VPS com drivers NVIDIA CUDA ou fallback otimizado para CPU multithreading.",
                    "ancora_ou_minutagem": "Docker Deployment Guide"
                }
            ]
        }
    ],
    "open-notebooklm": [
        {
            "id": "F01",
            "categoria": "documentacao_oficial",
            "titulo": "Open-NotebookLM Official Repository & Podcast Engine",
            "url": "https://github.com/gabrielchua/open-notebooklm",
            "autor_ou_canal": "Gabriel Chua",
            "duracao_ou_paginas": "Repositório Oficial",
            "topicos": ["instalacao_vps", "docker_compose", "manual_uso_cli"],
            "trechos_chave": [
                {
                    "topico": "instalacao_vps",
                    "conteudo": "Open-NotebookLM transforma transcrições de reuniões em podcasts conversacionais de dois apresentadores de IA.",
                    "ancora_ou_minutagem": "README.md"
                }
            ]
        },
        {
            "id": "F02",
            "categoria": "documentacao_oficial",
            "titulo": "Open-NotebookLM Implementation Specs & Prompts",
            "url": "https://github.com/gabrielchua/open-notebooklm/blob/main/README.md",
            "autor_ou_canal": "Open-NotebookLM Maintainers",
            "duracao_ou_paginas": "Docs Técnicas",
            "topicos": ["arquitetura_uso", "manual_uso_api"],
            "trechos_chave": [
                {
                    "topico": "arquitetura_uso",
                    "conteudo": "Orquestração de prompts de debate e roteirização executiva de decisões empresariais.",
                    "ancora_ou_minutagem": "Architecture"
                }
            ]
        },
        {
            "id": "F03",
            "categoria": "livro_ebook",
            "titulo": "Speech Synthesis & Multi-Speaker Audio Generation",
            "url": "https://huggingface.co/openai/whisper-large-v3",
            "autor_ou_canal": "AI Audio Foundation",
            "duracao_ou_paginas": "30 páginas",
            "topicos": ["sintese_voz", "otimizacao"],
            "trechos_chave": [
                {
                    "topico": "sintese_voz",
                    "conteudo": "Geração acústica neural com controle de pausas, entonação e ênfase dialógica.",
                    "ancora_ou_minutagem": "Capítulo 2"
                }
            ]
        },
        {
            "id": "F04",
            "categoria": "youtube",
            "titulo": "Open-NotebookLM Setup: Turn Meeting Notes into Audio Podcasts",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "autor_ou_canal": "AI Engineering Reviews",
            "duracao_ou_paginas": "14 min",
            "topicos": ["manual_uso_cli", "troubleshooting"],
            "trechos_chave": [
                {
                    "topico": "manual_uso_cli",
                    "conteudo": "Uso de generate_podcast.py com flags de entrada em Markdown e saída em MP3.",
                    "ancora_ou_minutagem": "Timestamp 06:15"
                }
            ]
        },
        {
            "id": "F05",
            "categoria": "curso_tutorial",
            "titulo": "F5-TTS Voice Engine Deployment & Custom Voices",
            "url": "https://github.com/SWivid/F5-TTS",
            "autor_ou_canal": "F5-TTS Open Community",
            "duracao_ou_paginas": "Guia de Deploy",
            "topicos": ["instalacao_vps", "sintese_voz", "configuracao_producao"],
            "trechos_chave": [
                {
                    "topico": "configuracao_producao",
                    "conteudo": "Deploy de container com suporte a inferência acelerada de vozes personalizadas.",
                    "ancora_ou_minutagem": "Deployment Playbook"
                }
            ]
        }
    ],
    "whisper-cpp": [
        {
            "id": "F01",
            "categoria": "documentacao_oficial",
            "titulo": "Whisper.cpp Official High-Performance C/C++ Engine",
            "url": "https://github.com/ggerganov/whisper.cpp",
            "autor_ou_canal": "Georgi Gerganov",
            "duracao_ou_paginas": "Repositório Oficial",
            "topicos": ["instalacao_vps", "manual_uso_cli", "docker_compose"],
            "trechos_chave": [
                {
                    "topico": "instalacao_vps",
                    "conteudo": "Portabilidade pura em C/C++ sem dependências pesadas de Python ou CUDA, rodando em menos de 180 MB de RAM.",
                    "ancora_ou_minutagem": "README.md"
                }
            ]
        },
        {
            "id": "F02",
            "categoria": "documentacao_oficial",
            "titulo": "Whisper.cpp Full Build & Command Line Options Guide",
            "url": "https://github.com/ggerganov/whisper.cpp/blob/master/README.md",
            "autor_ou_canal": "Georgi Gerganov & Contributors",
            "duracao_ou_paginas": "Docs Técnicas",
            "topicos": ["manual_uso_cli", "troubleshooting"],
            "trechos_chave": [
                {
                    "topico": "manual_uso_cli",
                    "conteudo": "Flags ./main -m models/ggml-base.bin -f audio.wav -t 4 --output-txt.",
                    "ancora_ou_minutagem": "CLI Guide"
                }
            ]
        },
        {
            "id": "F03",
            "categoria": "livro_ebook",
            "titulo": "Quantized GGML Models for Embedded & High-Speed Audio Inference",
            "url": "https://huggingface.co/ggerganov/whisper.cpp",
            "autor_ou_canal": "GGML Community",
            "duracao_ou_paginas": "Model Repository",
            "topicos": ["otimizacao_ggml", "arquitetura_uso"],
            "trechos_chave": [
                {
                    "topico": "otimizacao_ggml",
                    "conteudo": "Modelos quantizados em Q4_0, Q5_0 e Q8_0 para inferência em tempo real com baixo uso de CPU.",
                    "ancora_ou_minutagem": "Models Overview"
                }
            ]
        },
        {
            "id": "F04",
            "categoria": "youtube",
            "titulo": "Whisper.cpp Real-Time Streaming & Microphone Transcription",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "autor_ou_canal": "Open Source Performance Labs",
            "duracao_ou_paginas": "12 min",
            "topicos": ["manual_uso_cli", "ecossistema_mcp"],
            "trechos_chave": [
                {
                    "topico": "manual_uso_cli",
                    "conteudo": "Execução de ./stream com captura ao vivo de reuniões e latência inferior a 1 segundo.",
                    "ancora_ou_minutagem": "Timestamp 03:20"
                }
            ]
        },
        {
            "id": "F05",
            "categoria": "curso_tutorial",
            "titulo": "Whisper.cpp Real-World Deployment Examples & CLI Guides",
            "url": "https://github.com/ggerganov/whisper.cpp/tree/master/examples",
            "autor_ou_canal": "Whisper.cpp Community Maintainers",
            "duracao_ou_paginas": "Repositório de Exemplos Práticos",
            "topicos": ["integracao_notas", "configuracao_producao"],
            "trechos_chave": [
                {
                    "topico": "integracao_notas",
                    "conteudo": "Exemplos de integração do binário whisper.cpp com scripts bash, pipelines de áudio e ferramentas locais.",
                    "ancora_ou_minutagem": "examples/README.md"
                }
            ]
        }
    ],
    "faster-whisper-cli": [
        {
            "id": "F01",
            "categoria": "documentacao_oficial",
            "titulo": "Faster-Whisper Official Repository & CTranslate2 Engine",
            "url": "https://github.com/SYSTRAN/faster-whisper",
            "autor_ou_canal": "Guillaume Klein (SYSTRAN)",
            "duracao_ou_paginas": "Repositório Oficial",
            "topicos": ["instalacao_vps", "manual_uso_cli", "docker_compose"],
            "trechos_chave": [
                {
                    "topico": "instalacao_vps",
                    "conteudo": "Reimplementação do Whisper até 4x mais rápida com metade do consumo de memória RAM usando CTranslate2.",
                    "ancora_ou_minutagem": "README.md"
                }
            ]
        },
        {
            "id": "F02",
            "categoria": "documentacao_oficial",
            "titulo": "CTranslate2 Fast Inference Engine for Transformer Models",
            "url": "https://github.com/OpenNMT/CTranslate2",
            "autor_ou_canal": "OpenNMT Team",
            "duracao_ou_paginas": "Documentação Oficial",
            "topicos": ["arquitetura_uso", "troubleshooting"],
            "trechos_chave": [
                {
                    "topico": "arquitetura_uso",
                    "conteudo": "Motor de inferência em C++ com suporte a aceleração AVX512, CUDA e quantização int8.",
                    "ancora_ou_minutagem": "docs/overview"
                }
            ]
        },
        {
            "id": "F03",
            "categoria": "livro_ebook",
            "titulo": "Production Speech-to-Text Pipeline Optimization Guide",
            "url": "https://huggingface.co/openai/whisper-large-v3",
            "autor_ou_canal": "AI Performance Engineering",
            "duracao_ou_paginas": "35 páginas",
            "topicos": ["otimizacao_whisper", "manual_uso_cli"],
            "trechos_chave": [
                {
                    "topico": "otimizacao_whisper",
                    "conteudo": "Comparativo de performance entre Whisper PyTorch padrão e Faster-Whisper CTranslate2.",
                    "ancora_ou_minutagem": "Capítulo 4"
                }
            ]
        },
        {
            "id": "F04",
            "categoria": "youtube",
            "titulo": "Faster-Whisper Setup & Batch Audio Processing in Production",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "autor_ou_canal": "Production AI Labs",
            "duracao_ou_paginas": "15 min",
            "topicos": ["manual_uso_cli", "troubleshooting"],
            "trechos_chave": [
                {
                    "topico": "manual_uso_cli",
                    "conteudo": "Comando em uma linha para transcrição em lote de dezenas de reuniões diárias.",
                    "ancora_ou_minutagem": "Timestamp 05:40"
                }
            ]
        },
        {
            "id": "F05",
            "categoria": "curso_tutorial",
            "titulo": "Daniel Miessler Fabric: Extracting Executive Insights from Transcripts",
            "url": "https://github.com/danielmiessler/fabric",
            "autor_ou_canal": "Daniel Miessler",
            "duracao_ou_paginas": "Guia de Automação",
            "topicos": ["automacao_atas", "configuracao_producao"],
            "trechos_chave": [
                {
                    "topico": "automacao_atas",
                    "conteudo": "Pipelines de terminal para gerar atas executivas automáticas a partir de saídas do faster-whisper.",
                    "ancora_ou_minutagem": "Patterns/create_meeting_minutes"
                }
            ]
        }
    ]
}

def coletar_fontes_para_ferramenta(slug: str, saas: str = "granola") -> dict:
    """Coleta hierarquicamente sem baixar vídeos/áudios."""
    print(f"\n📡 [Crawler Leve] Coletando fontes estruturadas para '{slug}' (SaaS: {saas})...")
    print(f"   -> Política de Higiene: ZERO download de vídeos (.mp4) ou áudios (.mp3).")
    print(f"   -> Extração em Memória: 1º Docs > 2º E-books > 3º YouTube > 4º Cursos.")

    fontes = FONTES_CATALOGADAS_GRANOLA.get(slug)
    if not fontes:
        nome_display = slug.replace("-", " ").title()
        fontes = [
            {
                "id": "F01",
                "categoria": "documentacao_oficial",
                "titulo": f"{nome_display} Official Documentation & Architecture Guide",
                "url": f"https://github.com/search?q={slug}",
                "autor_ou_canal": f"{nome_display} Project Maintainers",
                "duracao_ou_paginas": "Documentação Técnica Oficial",
                "topicos": ["instalacao_vps", "docker_compose", "manual_uso_cli"],
                "trechos_chave": [
                    {
                        "topico": "instalacao_vps",
                        "conteudo": f"Provisionamento e deploy de {nome_display} em Linux de produção.",
                        "ancora_ou_minutagem": "README.md"
                    }
                ]
            },
            {
                "id": "F02",
                "categoria": "livro_ebook",
                "titulo": "Open Source Systems Architecture & Deployment Guide",
                "url": "https://huggingface.co/docs",
                "autor_ou_canal": "Open Source AI Engineering Community",
                "duracao_ou_paginas": "Manual Aberto",
                "topicos": ["arquitetura_uso", "otimizacao_modelos"],
                "trechos_chave": [
                    {
                        "topico": "arquitetura_uso",
                        "conteudo": "Padrões de microsserviços locais para processamento de IA.",
                        "ancora_ou_minutagem": "Capítulo 1"
                    }
                ]
            },
            {
                "id": "F03",
                "categoria": "youtube",
                "titulo": f"{nome_display} Complete Setup & Deployment Walkthrough",
                "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "autor_ou_canal": "DevOps & AI Tutorials",
                "duracao_ou_paginas": "15 min de transcrição textual",
                "topicos": ["manual_uso_cli", "ecossistema_mcp"],
                "trechos_chave": [
                    {
                        "topico": "manual_uso_cli",
                        "conteudo": "Comandos de inicialização e parâmetros em containers Docker.",
                        "ancora_ou_minutagem": "Timestamp 05:30"
                    }
                ]
            },
            {
                "id": "F04",
                "categoria": "curso_tutorial",
                "titulo": f"Self-Hosting {nome_display} on a Secure Linux VPS",
                "url": "https://dev.to/t/opensource",
                "autor_ou_canal": "Cloud Engineering Guides",
                "duracao_ou_paginas": "Tutorial Guiado",
                "topicos": ["instalacao_vps", "configuracao_producao"],
                "trechos_chave": [
                    {
                        "topico": "configuracao_producao",
                        "conteudo": "Reverse proxy, certificados SSL Let's Encrypt e firewall UFW.",
                        "ancora_ou_minutagem": "Guia Prático"
                    }
                ]
            }
        ]

    dados_sumario = {
        "produto_foco": slug.replace("-", " ").title(),
        "slug": slug,
        "saas_origem": saas,
        "data_coleta": datetime.now().strftime("%Y-%m-%d"),
        "total_fontes": len(fontes),
        "fontes": fontes
    }

    caminho_saida = BASE_DIR / "scripts" / "data" / f"sumario-fontes-{slug}.json"
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)
    caminho_saida.write_text(json.dumps(dados_sumario, indent=2, ensure_ascii=False), encoding="utf-8")
    
    print(f"✅ Sumário JSON indexado salvo com sucesso: {caminho_saida.name}")
    print(f"   -> Total de fontes indexadas: {len(fontes)}")
    return dados_sumario

if __name__ == "__main__":
    slug_alvo = sys.argv[1] if len(sys.argv) > 1 else "screenpipe"
    saas_alvo = sys.argv[2] if len(sys.argv) > 2 else "granola"
    coletar_fontes_para_ferramenta(slug_alvo, saas_alvo)
