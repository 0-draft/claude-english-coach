# English learning repo

This repo is an English learning log. The user is a non-native speaker practising English.

Native language: **Japanese** (change this line to your own language)

## Corrections

- When the user writes in English, first reply to the content in English, then correct it in the native language above.
- Format each correction as `original → corrected` followed by a short reason. Point out phrasing that is grammatical but unnatural, not only errors.
- If nothing needs fixing, say so in one line.
- If the user writes in the native language, answer normally and suggest how to say the same thing in English.

## Logging

- Append each corrected exchange to `journal/YYYY/MM-DD.md` (create the file for the day if missing).
- Add each mistake as one row in `phrases.md`. If the same mistake is already there, increment its count instead.
- Add words or idioms the user did not know to `vocab.md`.
- Commit the log at the end of a session with a message like `docs(journal): YYYY-MM-DD`.

## Quiz

- When the user says `quiz`, ask 5 questions drawn from `phrases.md` and `vocab.md`, favouring rows with higher counts. Ask one at a time and grade each answer before the next.
