# english

A template repo for learning English with [Claude Code](https://docs.claude.com/en/docs/claude-code/overview). Write to Claude in English, get corrections, and keep every mistake and new word in plain Markdown so you can review them later.

## How it works

`CLAUDE.md` tells Claude how to behave in this repo:

1. You write in English (chat, a diary entry, a draft issue or PR).
2. Claude replies in English, then corrects your text in your native language.
3. Claude logs the session to `journal/`, adds mistakes to `phrases.md` and new words to `vocab.md`.
4. Say `quiz` and Claude asks you 5 questions, picking your most frequent mistakes first.

## Layout

| Path | Contents |
| --- | --- |
| `CLAUDE.md` | Rules Claude follows here (correction format, logging, quiz) |
| `journal/YYYY/MM-DD.md` | What you wrote each day, with corrections |
| `phrases.md` | Mistake → correction table, with a count per mistake |
| `vocab.md` | Words and idioms you want to keep |
| `tech/` | Phrases for GitHub issues, PRs and review replies |

## Getting started

1. Click **Use this template** on GitHub and create your own copy. Make it private if you'd rather keep your diary to yourself.
2. Clone it and run `claude` inside.
3. Set your native language at the top of `CLAUDE.md` (default: Japanese).
4. Write something in English.

## License

[MIT](LICENSE)
