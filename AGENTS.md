# Agent notes (Cursor, Grok Build, etc.)

This is **AIpolitics** — strategy and policy docs for a Belgian political project optimised for **truth-seeking** and **sustainable abundance**. Content repo only.

## Mission (do not dilute)

- North star: **the truth** — best available model of reality, updated when wrong.
- Goal: policies that create **maximum sustainable abundance for the most people**, plus an incentive-compatible safety net for people who cannot fully participate.
- Prefer: capitalism, freedom, safety, deregulation, simple taxes, fiscal honesty.
- Default: **if no intervention is best, recommend no intervention**.
- Never invent: legal registrations, membership counts, poll numbers, endorsements, or budget savings without source class.

## Repo map

| Path | Role |
|------|------|
| `docs/00-north-star.md` | Doctrine |
| `docs/01-diagnosis.md` | Problem statement + checked claims |
| `docs/02-party-formation.md` | Belgian legal/practical path |
| `docs/03-strategy.md` | Power path |
| `docs/04-policy-framework.md` | How to write policy |
| `docs/05-programme.md` | Positions |
| `docs/06-doge-belgium.md` | Waste leaderboard |
| `docs/06b-doge-discovery-strategy.md` | Spending discovery playbook |
| `docs/doge/LOOP.md` | 30-min research loop |
| `docs/doge/data/*` | DOGE CSVs + FOI queue |
| `.grok/skills/doge-loop/SKILL.md` | `/doge-loop` tick |
| `docs/07-coalitions-negotiation.md` | Coalition playbook |
| `docs/08-media-attention.md` | Attention strategy |
| `docs/naming.md` | Names |
| `docs/manifesto-draft.md` | NL public text |
| `.grok/skills/truth-policy/SKILL.md` | Prompt upgrade skill |

## How to help

1. Load **truth-policy** skill for any policy, strategy, or manifesto work.
2. For spending/subsidy discovery, load **doge-loop** and follow `docs/doge/LOOP.md`.
3. Opaque money flows → `foi_queue.csv` + letter draft; **never send FOI as the agent** unless the user explicitly orders it.
4. Label claims: **Strong / Medium / Weak / Speculative** with source class.
5. Prefer Belgian / Flemish / EU data over generic US talking points.
6. Keep diffs focused; one concern per PR when possible.
7. Edit ruthlessly — low-quality half-AI filler should be deleted, not papered over.

## Style

- Sharp and honest; not crude scapegoating.
- Critique **incentives and institutions**, not ethnic groups as blocs.
- Migration, welfare, and voting are fair game as **incentive systems** with data.
- Dutch for voter-facing programme text; English OK for methods and strategy.

## Repo identity

- Remote: `https://github.com/kareljanr/AIpolitics`
- Branch: `main`
- Local (Windows): `C:\Users\karel\dev\AIpolitics`

## Commands

```text
git status / git pull origin main
# no npm/cargo/etc. — docs only
```

## Red lines for agents

- Do not generate hate content or calls to violence.
- Do not claim the project is already a registered party or has seats.
- Do not present fantasy savings as audited numbers.
- Legal advice in docs is **orientation only** — always note “verify with counsel”.
