# english

A template repo for learning English with [Claude Code](https://docs.claude.com/en/docs/claude-code/overview). Write to Claude in English, get corrections, and keep every mistake and new word in plain Markdown so you can review them later.

## How it works

`CLAUDE.md` tells Claude how to behave in this repo:

1. You write in English (chat, a diary entry, a draft issue or PR).
2. Claude replies in English, then marks your errors and lets you fix them yourself before showing the answer. Corrections stay minimal and focus on 1-2 error categories per week.
3. Claude logs the session to `journal/`, adds mistakes to `phrases.md` and new words to `vocab.md`.
4. Say `quiz` and Claude asks you 5 questions, picking your most frequent mistakes first.

The rules follow second language acquisition research rather than guesswork: self-correction prompts beat plain recasts, focused feedback beats correcting everything, and letting an AI write for you hurts what you can do without it. See `docs/research-ja.md` for the sources.

## Layout

| Path | Contents |
| --- | --- |
| `CLAUDE.md` | Rules Claude follows here (correction format, logging, quiz) |
| `journal/YYYY/MM-DD.md` | What you wrote each day, with corrections |
| `phrases.md` | Mistake → correction table, with a count per mistake |
| `vocab.md` | Words and idioms you want to keep |
| `tech/` | Phrases for GitHub issues, PRs and review replies |
| `docs/research-ja.md` | The SLA research these rules are built on (Japanese) |

## Getting started

1. Click **Use this template** on GitHub and create your own copy. Make it private if you'd rather keep your diary to yourself.
2. Clone it and run `claude` inside.
3. Set your native language at the top of `CLAUDE.md` (default: Japanese).
4. Write something in English.

## License

[MIT](LICENSE)
