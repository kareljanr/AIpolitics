# Multi-tool / multi-machine workflow

**AIpolitics** is the canonical GitHub repo. Treat everything else as a checkout.

## Canonical local layout

```text
C:\Users\karel\dev\
  AIpolitics\          # this repo
  <other-repos>\
```

Same path for **Cursor** and **Grok Build**.

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

## Day-to-day

1. `git pull origin main` before you start  
2. Branch: `git checkout -b topic/short-name`  
3. Commit clearly  
4. `git push -u origin HEAD`  
5. Open a PR for non-trivial changes  

Prefer small PRs (one doc or one DOGE theme).

## Policy work

1. Load skill **truth-policy** (`.grok/skills/truth-policy/`)  
2. Follow [04-policy-framework.md](04-policy-framework.md)  
3. Tag claims with confidence + source class  
4. Never invent € savings  

## Cursor

Open folder: `C:\Users\karel\dev\AIpolitics`  
Remote: `kareljanr/AIpolitics` only.

## Grok Build

```powershell
cd C:\Users\karel\dev\AIpolitics
grok
```

```powershell
grok --cwd C:\Users\karel\dev\AIpolitics
grok inspect
```

Grok loads root `AGENTS.md` and project skills under `.grok/skills/`.

## Switching tools

1. Commit or stash  
2. `git pull` in the next tool  
3. Same branch  

Optional isolated worktree:

```powershell
grok --worktree=topic-x --ref main "your task"
```

## What not to do

- Parallel “source of truth” outside this repo  
- Fake membership / registration claims in docs  
- Long unpushed local-only doctrine  
