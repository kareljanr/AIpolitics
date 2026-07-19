# Multi-tool / multi-machine workflow

**AIpolitics** is the canonical GitHub repo. Treat everything else as a checkout.

## Canonical local layout (this machine)

Keep all shared projects under one parent folder:

```text
C:\Users\karel\dev\
  AIpolitics\          # this repo
  <other-repos>\
```

Same path for **Cursor** (Open Folder) and **Grok Build** (`grok` launched from that folder).

## Setup on a new machine

```bash
# macOS / Linux / Git Bash
mkdir -p ~/dev && cd ~/dev
git clone https://github.com/kareljanr/AIpolitics.git
cd AIpolitics
```

```powershell
# Windows PowerShell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\dev" | Out-Null
Set-Location "$env:USERPROFILE\dev"
git clone https://github.com/kareljanr/AIpolitics.git
Set-Location AIpolitics
```

Use HTTPS or SSH — whatever you already use for GitHub on that machine. Ensure `git` is on your PATH (Git for Windows: `C:\Program Files\Git\cmd`).

## Day-to-day

1. `git pull origin main` before you start
2. Work on a short-lived branch: `git checkout -b topic/short-name`
3. Commit with a clear message
4. `git push -u origin HEAD`
5. Open a pull request on GitHub when the change is ready to merge

Prefer small PRs (one doc or one policy theme) over large dumps.

## Cursor

Open folder: `C:\Users\karel\dev\AIpolitics` (or your clone path).

Point a Cursor cloud agent or local Cursor window at **this** repo (`kareljanr/AIpolitics`), not at the old Taxonomy fork.

## Grok Build

From the repo root:

```powershell
cd C:\Users\karel\dev\AIpolitics
grok
```

Or from anywhere:

```powershell
grok --cwd C:\Users\karel\dev\AIpolitics
```

Confirm project rules load:

```powershell
grok inspect
```

Grok reads root `AGENTS.md` automatically (and `.cursor/rules/` if present). Same rule as Cursor: edit files here, commit, push. Do not keep a parallel “source of truth” elsewhere.

## Switching tools mid-task

1. Commit or stash in the tool you leave
2. `git pull` in the tool you open next
3. Continue on the same branch

Optional: isolated Grok worktree while Cursor keeps the main checkout:

```powershell
grok --worktree=topic-x --ref main "your task"
```

## What not to do

- Do not continue party work in `kareljanr/Taxonomy` (that name/history is unrelated SEMIC public-service taxonomy)
- Do not maintain long-lived unpushed local copies as the only version of a doc
