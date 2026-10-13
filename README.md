# ChatGPT Telegram Bot — legacy Python example

[![Python checks](https://github.com/harshitethic/ChatGPT-Telegram-Bot/actions/workflows/checks.yml/badge.svg)](https://github.com/harshitethic/ChatGPT-Telegram-Bot/actions/workflows/checks.yml)

A historical Python Telegram bot project, originally created for early OpenAI completion models and the older `python-telegram-bot` API.

> **Maintenance notice (October 2026):** This code demonstrates the older integration style. Its original completion endpoint, model settings, and Telegram dependency patterns may no longer run with current packages. Treat it as a legacy reference, not a tested modern production bot. For a newer Node.js sample with the current OpenAI API, see [chatgpt-bot-telegram](https://github.com/harshitethic/chatgpt-bot-telegram).

## Security

Credentials are now read only from environment variables. The bot no longer prints keys to the console and no longer embeds fallback key strings in the script.

- `OPENAI_KEY` — API key from your OpenAI account.
- `TELEGRAM_KEY` — Telegram bot token issued by BotFather.

Set both variables in your environment **before** starting the bot. If either variable is missing, startup fails with a useful error message. Do **not** put real keys in a public fork or issue.

```bash
git clone https://github.com/harshitethic/ChatGPT-Telegram-Bot.git
cd ChatGPT-Telegram-Bot
cp .env.example .env
# Edit .env locally; keep credentials out of Git.
set -a; . ./.env; set +a
```

**Note:** Modern Python/OpenAI/Telegram releases have breaking API changes relative to this legacy example. Installation of the old dependencies and end-to-end bot behavior are **not covered by the current checks**; updating those integrations requires a separate migration. The old Heroku dyno instructions have been removed because that deployment workflow no longer represents a reliable supported setup.

## Source structure

- `harshitethic.py` — historical bot handlers and conversation state.
- `config.py` — environment validation with explicit missing-key errors.
- `tests/test_config.py` — isolated credential configuration tests.

## Verify without API credentials

```bash
python3 -m compileall -q config.py harshitethic.py tests
python3 -m unittest discover -s tests -v
```

These checks need only Python's standard library. They verify syntax and configuration—not the legacy API's compatibility with live Telegram/OpenAI services.

## Reporting issues

Please provide a minimal reproducer, Python and dependency versions, and redacted logs. **Never** include tokens or personal chat data. See [SECURITY.md](SECURITY.md).
