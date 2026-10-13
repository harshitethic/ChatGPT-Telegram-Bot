# Security guidance

**Legacy reference:** This Python Telegram/OpenAI project uses older provider SDK interfaces. CI covers syntax and configuration boundaries, not current live bot functionality or a hardened public deployment.

## Historical exposed credentials — 14 October 2026

Two historical public pull requests proposed embedding credential-like OpenAI and Telegram bot tokens directly into the application. Those PRs were **closed without merging**. However, public PR diffs and commits may remain accessible. If any exposed credential belongs to you, **revoke/rotate it immediately**, even if the code no longer displays it on the default branch.

- **Telegram:** Contact the official @BotFather account and use its token-management or revoke flow to issue a new bot token. Update your local ignored environment configuration; verify the old token is invalid.
- **OpenAI:** Revoke the affected API key from your OpenAI API-key dashboard, create a replacement, and inspect usage for unexpected activity.
- Never paste secrets in GitHub PRs, issues, example files, stack traces, logs or screenshots. A placeholder must not be a real token.
- Deleting keys from the current source does **not** remove them from old forks, reviews and commit history. Rotation is required even if history cleanup is later requested.

## Limitations

The repository does not currently implement quotas, audit logging, moderation, contemporary SDK migrations or protections suitable for exposing a bot to arbitrary untrusted users. Do not deploy it as a production service without reviewing current dependencies and provider requirements.

Report security concerns privately to `contact@harshitethic.com` with **sanitized** reproduction steps.
