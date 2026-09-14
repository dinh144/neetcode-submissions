# neetcode-submissions

Dinh's NeetCode.io Blind 75 practice. `Data Structures & Algorithms/<slug>/submission-N.py` is pushed to `main` by NeetCode.io GitHub Sync on every submit: never edit, move or delete those files.

## Rules
- Never write a solution, in any mode — this overrides algo-sensei's review/tutor modes and its solution template. Allowed: questions, progressive hints, pseudocode (hint level 5 only), syntax snippets of 3 lines or fewer, pointing at a line of Dinh's code. Describe improvements in words; Dinh types them. In mock interviews, hints also stop at pseudocode (no "high-level steps").
- Timebox before any hint: Easy 20 min, Medium 30, Hard 45. Then Claude's hints → still stuck: the free NeetCode video for that problem → close it, retype from blank → Run → submit.
- Drafts go in `wip/<slug>.py` (gitignored). No local tests; Dinh runs code on neetcode.io.
- Before every push: `git pull --rebase` (NeetCode.io pushes too).

## Schedule (grill 2026-09-14)
- Mornings: 15–18/09 2h, 19–20/09 1h, 21/09 off, from 22/09 Mon–Fri 45 min. Due reviews first, then the new problem. A missed session is not made up.
- Mock interview: trial 18/09, then the first Friday of each month, replacing that day's new problem.

## Commands
- `due`: `git pull --rebase`, list `REVIEW.md` rows with due date ≤ today, then the next new problem = the lowest `#` in the Blind 75 order absent from the queue table's `#` column (Blind 75 finished → next NeetCode 150 problem on neetcode.io). If a slug folder exists with no row, ask Dinh to run `review <slug>` first. End with `x/75, dự kiến xong ~dd/mm`: remaining new problems × (mean first Phút + 2 × mean later Phút) ÷ 225 min/week; with fewer than 10 Phút entries print `chưa đủ số đo` instead of a date.
- `review <slug>` (Dinh calls it only after Accepted): `git pull --rebase`, read the highest `submission-N` of that slug, review correctness, Big-O vs optimal, edge cases, Python idiom. Write Pattern + Dấu hiệu with algo-sensei's pattern-mapper signals. Ask whether hints or the video were used and the minutes from opening the problem to Accepted; append the minutes to Phút (comma-separated, first = new solve), update stage and due date, commit and push.
- `mock`: algo-sensei interview mode (`modes/interview-mode.md`) on the problem `due` would pick next. Dinh codes on neetcode.io and types his thinking into chat. Afterwards add a row to the Mock table in `REVIEW.md`, then handle the problem like `review <slug>` (any hint = with help); not Accepted → normal loop with the video.
- `anki` (Sundays): write `anki/dsa-patterns.json` as `{"title": "DSA patterns", "cards": [{"front": <Dấu hiệu>, "back": "<Pattern> — <slug>"}]}` from every queue row, run `uv run --no-project --with genanki python ~/scripts/flashcards_to_apkg.py anki/dsa-patterns.json`, tell Dinh to import `anki/dsa-patterns.apkg`.

## REVIEW.md queue
Stage and due date after each solve:
- New problem, no help → `+30`, due in 30 days. With help → `+1`, due tomorrow.
- Re-solve with help → `+1`, due tomorrow. Re-solve without help: from `+1` → `+7`, due in 7 days; from `+7` or `ôn` → `+30`, due in 30 days; from `+30` → `xong`.
