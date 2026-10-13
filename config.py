"""Credential validation independent of legacy Telegram/OpenAI dependencies."""
import os


def read_credentials(environ=None):
    """Return (OpenAI key, Telegram key) or fail with an actionable error."""
    environment = os.environ if environ is None else environ
    keys = {}
    for name in ("OPENAI_KEY", "TELEGRAM_KEY"):
        value = environment.get(name, "")
        if not isinstance(value, str) or not value.strip():
            raise RuntimeError(f"Missing {name}: set it in the environment before starting the bot.")
        keys[name] = value.strip()
    return keys["OPENAI_KEY"], keys["TELEGRAM_KEY"]
