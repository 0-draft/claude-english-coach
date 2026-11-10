# claude-english-coach

A template repo for learning English with [Claude Code](https://code.claude.com/docs/en/overview). Write to Claude in English, get corrections, and keep every mistake and new word in plain Markdown so you can review them later.

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
| `app/rounds.html` | English Rounds, a drill app for daily practice (see below) |
| `docs/research-ja.md` | The SLA research these rules are built on (Japanese) |
| `docs/apps-research-ja.md` | What was taken from Duolingo-style apps and why (Japanese) |

## Getting started

1. Click **Use this template** on GitHub and create your own copy. Make it private if you'd rather keep your diary to yourself.
2. Clone it and run `claude` inside.
3. Set your native language at the top of `CLAUDE.md` (default: Japanese).
4. Write something in English.

## Drill app

`app/rounds.html` is a single-page app built to run as a [Claude artifact](https://claude.ai). Build an ASCII-only copy with `python3 app/build.py app/rounds.html /tmp/rounds.html`, then ask Claude Code to publish that copy as an artifact with the `db`, `user` and `sample` capabilities. The ASCII build matters: the artifact viewer can read the page in a charset other than UTF-8, and the raw file then shows Japanese as mojibake. Opened outside claude.ai, either file works and saves to the browser.

- **Review**: spaced repetition with FSRS ([ts-fsrs](https://github.com/open-spaced-repetition/ts-fsrs) 5.4.2). Every card asks you to produce the English, never to pick it.
- **Listen**: dictation sentence by sentence. Words you miss become review cards automatically.
- **Speak**: role-play work conversations with Claude (stand-up, PR walkthrough, incident report) and track how many words you speak, or run the 4/3/2 fluency drill. Claude marks errors with hints first and shows the correction only after you try.
- **Adaptive dictation**: playback speed moves up or down to keep you at 80-90% of words correct.
- **Habit**: a 66-day grid. Five minutes keeps the streak, 15 minutes meets the goal, and one missed day a week is forgiven. No XP, leagues, hearts or streak-loss nags.
- **Monthly check**: the same listening and 2-minute speaking test every month, so progress is measured as ability rather than points.

`docs/apps-research-ja.md` lists which Duolingo-style mechanics made it in, which did not, and the evidence for each.

Artifact frames block the microphone, so the app has no recording. Use your OS dictation (on macOS, press fn twice) to get speech into the text box.

## License

[MIT](LICENSE)
