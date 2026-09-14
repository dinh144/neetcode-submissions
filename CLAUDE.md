# neetcode-submissions

Dinh's NeetCode.io Blind 75 practice. `Data Structures & Algorithms/<slug>/submission-N.py` is pushed to `main` by NeetCode.io GitHub Sync on every submit: never edit, move or delete those files.

## Rules
- Never write a solution, in any mode — this overrides algo-sensei's review/tutor modes and its solution template. Allowed: questions, progressive hints, pseudocode (hint level 5 only), syntax snippets of 3 lines or fewer, pointing at a line of Dinh's code. Describe improvements in words; Dinh types them.
- Timebox before any hint: Easy 20 min, Medium 30, Hard 45. Then hint → solution → close it, retype from blank → Run → submit.
- Drafts go in `wip/<slug>.py` (gitignored). No local tests; Dinh runs code on neetcode.io.
- Before every push: `git pull --rebase` (NeetCode.io pushes too).

## Commands
- `due`: `git pull --rebase`, list `REVIEW.md` rows with due date ≤ today, then the next new problem = the lowest `#` in the Blind 75 order absent from the queue table's `#` column. If a slug folder exists with no row, ask Dinh to run `review <slug>` first.
- `review <slug>` (Dinh calls it only after Accepted): `git pull --rebase`, read the highest `submission-N` of that slug, review correctness, Big-O vs optimal, edge cases, Python idiom. Ask whether hints or the solution were used, then update `REVIEW.md`, commit and push.

## REVIEW.md queue
Stage and due date after each solve:
- New problem, no help → stage `xong`, no due date. With help → `+1`, due tomorrow.
- Re-solve with help → `+1`, due tomorrow. Re-solve without help: from `+1` → `+7`, due in 7 days; from `+7` or `ôn` → `xong`.
