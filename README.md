# MainGem Bot 🤖

A lightweight, production-ready Telegram AI assistant powered by Groq's LLaMA 3.3 70B inference API.

**Live and running** — deployed on Railway.

---

## What It Does

GemBot handles natural language conversations over Telegram in real time. It maintains conversation context within a session, processes messages asynchronously, and responds with sub-second latency thanks to Groq's inference speed.

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.13 |
| Telegram | python-telegram-bot |
| LLM API | Groq (LLaMA 3.3 70B) |
| Deployment | Railway |
| Secrets | Environment variables via Railway config |
| Version control | GitHub (auto-deploy on push) |

---

## Architecture

```
User (Telegram)
     │
     ▼
python-telegram-bot (async handler)
     │
     ▼
Groq API — LLaMA 3.3 70B
     │
     ▼
Response → Telegram
```

Key design decisions:
- **Async message handling** — non-blocking, handles multiple users without queuing
- **Session-based context** — conversation history maintained within a session
- **Zero-cost infra** — Railway free tier + Groq free tier, no running costs
- **Auto-deploy** — GitHub push triggers Railway redeploy automatically

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/kwahyu-sudo/MainGem_Bot.git
cd MainGem_Bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variables

```bash
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
```

Get your Telegram bot token from [@BotFather](https://t.me/BotFather).
Get your Groq API key from [console.groq.com](https://console.groq.com).

### 4. Run locally

```bash
python bot.py
```

### 5. Deploy to Railway

- Connect this repo to Railway
- Add the environment variables in Railway's config panel
- Railway auto-deploys on every push to main

---

## Why Groq?

Groq's inference API consistently returns responses in under 1 second for LLaMA 3.3 70B — significantly faster than OpenAI or Anthropic equivalents at the same model size. For a Telegram bot where response latency is noticeable, this matters.

---

## Limitations

- Context resets when the bot restarts (no persistent memory)
- Single-model setup (no routing between models)

These limitations are addressed in the successor project: **[BirkinBot](https://github.com/kwahyu-sudo)** — built on n8n with persistent Airtable backend and Google Calendar integration.

---

## License

MIT
