# AIpolitics

**North star: the truth.**  
Build a Belgian political project that seeks the policies that create **the most sustainable abundance for the most people** — including a safety net that does not destroy the productive core that funds it.

This repository is the planning and strategy workspace for that project. It is **docs, not an app**. No fake memberships, registrations, or endorsements.

> Working label: **AIpolitics** (name open — see [docs/naming.md](docs/naming.md)).  
> Positioning: truth-seeking, economically liberal, high freedom, high competence. AI-augmented — not AI worship.

## The problem (checked)

Belgium is not failing for mysterious reasons. Incentives + fiscal arithmetic explain most of it:

| Fact | Status | Source class |
|------|--------|--------------|
| Highest (or near-highest) OECD **labour tax wedge** for average single workers (~52–53%) | **Strong** | OECD *Taxing Wages* 2025/2026 |
| Structural **general government deficit** (~4–5%+ of GDP; debt >100% GDP) | **Strong** | National Bank of Belgium / EU notifications |
| High public spending ratio vs OECD peers | **Strong** | OECD / Eurostat |
| System rewards non-work, complexity, and clienteles more than production | **Medium–Strong** | Incentive analysis + fiscal structure (see diagnosis) |
| “Anyone or anything (#AI) would do better” | **Unchecked slogan** | Useful as media hook; not a policy claim until proven |

Full diagnosis with assumption checks: [docs/01-diagnosis.md](docs/01-diagnosis.md).

## What we optimise for

1. **Truth over tribe** — every claim has a confidence level; wrong models get retired.
2. **Abundance** — growth, housing, energy, talent, innovation — not zero-sum redistribution theatre.
3. **Incentive-compatible safety net** — support people who cannot handle high-pressure society **without** making non-contribution the rational default.
4. **Freedom + safety + simple rules** — markets where they work; state monopoly on force and core public goods; cut everything else that fails a cost-benefit test.
5. **If no policy is best, choose no policy** — default to liberty when the state cannot demonstrate value.

Method: [docs/00-north-star.md](docs/00-north-star.md) · [docs/04-policy-framework.md](docs/04-policy-framework.md)

## Document map

| # | Document | Purpose |
|---|----------|---------|
| 00 | [North star](docs/00-north-star.md) | Truth, abundance, red lines |
| 01 | [Diagnosis](docs/01-diagnosis.md) | Why Belgium is spiralling (checked claims) |
| 02 | [Party formation](docs/02-party-formation.md) | How to create a party in Belgium (legal path) |
| 03 | [Strategy](docs/03-strategy.md) | Votes, power, media, timeline |
| 04 | [Policy framework](docs/04-policy-framework.md) | How we design and kill policies |
| 05 | [Programme](docs/05-programme.md) | Draft positions (federal / Flanders / local) |
| 06 | [DOGE Belgium](docs/06-doge-belgium.md) | Waste leaderboard: subsidies, laws, absurd incentives |
| 06b | [DOGE discovery strategy](docs/06b-doge-discovery-strategy.md) | Map all spending → L5 waste; FOI gaps; research loop |
| — | [DOGE data & loop](docs/doge/README.md) | CSVs, FOI queue, 15-min loop protocol |
| 07 | [Coalitions & negotiation](docs/07-coalitions-negotiation.md) | Getting into government without selling the soul |
| 08 | [Media & AI positioning](docs/08-media-attention.md) | Attention without becoming a joke |
| 09 | [Naming](docs/naming.md) | Brand shortlist |
| — | [Manifesto draft](docs/manifesto-draft.md) | Public one-pager (NL) |
| — | [Workflow](docs/workflow.md) | Multi-tool / multi-machine git workflow |
| — | [Skill: truth-policy](.grok/skills/truth-policy/SKILL.md) | Upgrade every prompt to truth-seeking policy mode |

## The crazy-but-coherent strategy (one paragraph)

Become the **truth + DOGE** party: publish a permanent **Absurdity & Waste Leaderboard** backed by open data; run as an **AI-augmented** project that forces every proposal through a public falsification pipeline; enter via **Flanders-first lists** (signatures are the only real gate — Belgium has no formal party-registration law); use AI novelty for earned media, then convert attention into **votes among net taxpayers**; trade coalition seats only for structural fiscal reform, not for vanity ministries. Details: [docs/03-strategy.md](docs/03-strategy.md).

## Active workstream: DOGE discovery

**Next move (running):** hierarchical spending map + subsidy hunt + FOI queue for missing flows.

- Strategy: [docs/06b-doge-discovery-strategy.md](docs/06b-doge-discovery-strategy.md)  
- Loop: [docs/doge/LOOP.md](docs/doge/LOOP.md) · skill `/doge-loop`  
- Queues: `docs/doge/data/research_queue.csv`, `foi_queue.csv`  
- Agents draft openbaarheid letters; **humans send** them.

## Status

🟡 **Strategy & doctrine + DOGE scaffold** — discovery loop ready; amounts still being filled.  
No formal party, no candidates, no public funding claim. Get a lawyer before filing anything.

## Language

- **Dutch** for manifesto / voter-facing programme text  
- **English** OK for strategy, agent notes, README, methods  
- Numbers always cite a source class (OECD, NBB, FPS, city budget, …)

## For agents (Cursor, Grok, etc.)

Read [AGENTS.md](AGENTS.md). Use the project skill **truth-policy** so every policy prompt is upgraded: check assumptions, prefer evidence, and allow “do nothing” as a valid answer.

## License

[CC BY-SA 4.0](LICENSE) unless stated otherwise.
