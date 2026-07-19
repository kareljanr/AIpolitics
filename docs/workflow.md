# Multi-tool / multi-machine workflow

**AIpolitics** is the canonical GitHub repo. Treat everything else as a checkout.

## Setup on a new machine

```bash
git clone https://github.com/kareljanr/AIpolitics.git
cd AIpolitics
```

Use HTTPS or SSH — whatever you already use for GitHub on that machine.

## Day-to-day

1. `git pull origin main` (or `master`) before you start
2. Work on a short-lived branch: `git checkout -b topic/short-name`
3. Commit with a clear message
4. `git push -u origin HEAD`
5. Open a pull request on GitHub when the change is ready to merge

Prefer small PRs (one doc or one policy theme) over large dumps.

## Cursor

Point a Cursor cloud agent or local Cursor window at **this** repo (`kareljanr/AIpolitics`), not at the old Taxonomy fork.

## Grok / other AI builders

Same rule: clone or open **AIpolitics**, edit files, commit, push. Do not keep a parallel “source of truth” elsewhere.

## What not to do

- Do not continue party work in `kareljanr/Taxonomy` (that name/history is unrelated SEMIC public-service taxonomy)
- Do not maintain long-lived unpushed local copies as the only version of a doc
