# 09 — Proposal Radar (Clowns → Genius)

**Sister system to DOGE.** DOGE scores **existing public money**. Proposal Radar scores **new policy ideas** before (or as) they become law — announcements, wetsvoorstellen, coalition “deals”, party bills, ministerial pilots, media trial balloons.

Related: [04-policy-framework.md](04-policy-framework.md) · [06-doge-belgium.md](06-doge-belgium.md) · [08-media-attention.md](08-media-attention.md) · ops: [proposal-radar/](proposal-radar/)

---

## Upgraded goal

| | |
|--|--|
| **Goal** | Maximum truth + maximum sustainable abundance for persons in Belgium |
| **Jurisdiction** | Belgium only (federal / regions / communities / provinces / local). EU proposals only if they bind BE cash or law. |
| **Hard constraints** | No invented facts; confidence tags; “do nothing / abolish” always on the option set; critique incentives not ethnic blocs |
| **Output** | Sourced proposal cards + scores + public leaderboards people can share |

**Original intent:** gather media/political proposals → truth-check them → rate clown→genius → showcase.

---

## 1. Why this exists

| Gap today | What Radar fixes |
|-----------|------------------|
| DOGE audits **spent** euros | Radar audits **proposed** euros and rules **before** capture hardens |
| Media recycles press releases | Force mechanism, cost, falsifier, alternatives |
| Parties market vibes | Public scorecard: same criteria every time |
| “Smart idea” fashion | Separate **rhetoric quality** from **expected abundance** |

**Pair with DOGE:** if a proposal funds an L5 absurdity already on the waste leaderboard, link them. Same euro story, two timestamps (promise → invoice).

---

## 2. What counts as a “proposal”

Include when **at least one** is true:

1. Named **policy action** (law, decree, subsidy, tax, ban, obligation, pilot, agency, envelope)  
2. Attributed to a **Belgian actor** (minister, party, government, parliament, mayor, social partner with BE locus)  
3. **Public** (press, official site, parlement.be / vlaamsparlement.be, social post by official account)  
4. **Material** — affects ≥ ~€1m/year, rights of many people, or a clear precedent (agent judgment OK; log it)

**Exclude:**

| Exclude | Why |
|---------|-----|
| Pure personal scandal | Not a policy mechanism |
| Non-BE foreign politics | Out of scope |
| Vague campaign slogans with no instrument | Too thin until instrument appears |
| Our own draft programme (score later under different track) | Conflict of interest if self-scored without process |
| Satire without real actor | Noise |

**Status lifecycle**

```text
rumoured → announced → tabled (bill) → adopted → implemented → evaluated
                ↘ killed / expired
```

Re-score when status jumps **or** new primary numbers appear. Scores are versioned (`analysis_version`).

---

## 3. System architecture (three layers)

```text
┌─────────────────────────────────────────────────────────────┐
│  A. INGEST (gather)                                         │
│  RSS / open portals / agent search / human seed             │
│  → proposals.csv + sources.csv + raw/ snapshots             │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│  B. ANALYSE (truth-seeking)                                 │
│  Queue → one unit/tick → full memo + scores                 │
│  → analyses/*.md + scores into proposals.csv                │
│  Optional: link doge leaderboard / FOI if money opaque      │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│  C. SHOWCASE (public)                                       │
│  Leaderboards, cards, weekly Clowns/Genius, X/site          │
│  → public/*.md + later static site                          │
└─────────────────────────────────────────────────────────────┘
```

Ops live under [`docs/proposal-radar/`](proposal-radar/) (same CSV-first discipline as DOGE). Agents: skill **proposal-radar** + always **truth-policy**.

---

## 4. Layer A — Gathering (Belgium-only)

### 4.1 Source catalogue (priority order)

| Priority | Class | Examples | How |
|----------|-------|----------|-----|
| P0 | Primary legislative | Kamer/Senaat docs, Vlaams Parlement, Parlement wallon, Brussels, FWB | Portal scrape / open page / RSS |
| P0 | Official government | federal government newsroom, Flanders “nieuws”, regional ARs | RSS + agent |
| P1 | Serious press | De Tijd, L'Echo, Trends, De Standaard, Knack, Le Soir, VRT NWS, RTBF | RSS / search; **never sole € source** |
| P1 | Wire / agency | Belga | When available |
| P2 | Party press releases | Party sites, official X accounts | Capture claim; verify elsewhere |
| P2 | Social (official only) | @Ministers, parties BE | Seed only |
| P3 | Commentariat | Op-eds, think tanks | Mechanism ideas; not “facts” alone |

**Honesty rule:** press can **discover** a proposal; primary docs **anchor** cost, legal form, competence.

### 4.2 Ingest methods (phased)

| Phase | What | Status |
|-------|------|--------|
| **0 — Manual / agent** | Human or agent pastes URL → creates row | **Now** (default) |
| **1 — RSS harvester** | Script polls allowlisted feeds → candidate queue | Scaffold when ready |
| **2 — Portal watcher** | Check new wetsvoorstellen / mededelingen titles | After phase 1 |
| **3 — Semantic filter** | LLM: “is this a policy proposal?” + jurisdiction BE | After noise measured |

**Phase 0 is enough to start scoring.** Do not block analysis on perfect scrapers.

### 4.3 Dedup & identity

- `proposal_id`: stable `prop_YYYYMMDD_shortslug`  
- Same instrument, many articles → **one** proposal, many `sources`  
- Bundle of measures (e.g. “super-nota”) → parent + **child proposals** (score children; parent gets summary only)

### 4.4 Legal / ethical scrape rules

- Prefer **official open data** and **RSS** over aggressive crawling  
- Respect robots.txt; rate-limit; store URL + access date  
- Do **not** bypass paywalls illegally; quote short fair-use excerpts only  
- Attribution always; we critique ideas, not dox private persons  

---

## 5. Layer B — Analysis (maximum truth-seeking)

### 5.1 Mandatory pipeline (from doc 04)

Every scored proposal runs:

1. **Problem claim** — metric, baseline, who is hurt  
2. **Mechanism** — price, barrier, principal–agent, selection, …  
3. **Options** — status quo | abolish/deregulate | price/tax | conditional transfer | public provision | pilot  
4. **Evidence table** — Strong / Medium / Weak / Speculative + source class  
5. **Distribution** — winners/losers + **transfer/exit constraint**  
6. **Fiscal** — static + dynamic; ranges OK; no fake precision  
7. **Belgian competence** — federal / VL / WAL / BRU / community / local / EU  
8. **Recommendation** — support / amend / reject / ignore; may be “do nothing”  
9. **Falsifier** — one sentence  
10. **Open questions** — what would upgrade confidence  

Template: [`proposal-radar/templates/analysis-memo.md`](proposal-radar/templates/analysis-memo.md)

### 5.2 Score model (public)

Two public axes people actually understand:

| Axis | Range | Meaning |
|------|-------|---------|
| **Clownpoints** | 0–10 | How broken is this idea as stated? (10 = pure theatre / inverted incentives / fantasy cost) |
| **Genius score** | 0–10 | How well does it maximise sustainable abundance under BE constraints? (10 = rare; almost never) |

**Composite for ranking:**

```text
policy_index = genius_score − clownpoints
# range roughly −10 … +10
```

| policy_index | Label (NL public) | Label (EN internal) |
|--------------|-------------------|---------------------|
| ≤ −7 | Circus | Clown special |
| −6 … −3 | Dom | Bad |
| −2 … +2 | Twijfel | Mixed / needs work |
| +3 … +6 | Solid | Good |
| ≥ +7 | Zeldzaam geniaal | Rare genius |

### 5.3 Sub-scores (internal, always stored)

| Field | 0–10 | What it measures |
|-------|------|------------------|
| `truth_problem` | accuracy of the problem diagnosis | |
| `mechanism_fit` | does the instrument match the mechanism? | |
| `abundance_ev` | expected effect on sustainable abundance | |
| `fiscal_honesty` | cost/save claims vs realistic accounting | |
| `incentive_quality` | rewards production / reduces waste vs reverse | |
| `competence_fit` | right government level / implementable | |
| `evidence_quality` | strength of supporting evidence | |
| `capture_risk` | clienteles, permanent bureaucracy, lobby lock-in (10 = high risk → hurts genius) | |

**Suggested mapping (agents may override with reason in memo):**

```text
genius_score ≈ 0.25*abundance_ev + 0.20*mechanism_fit + 0.15*incentive_quality
             + 0.15*fiscal_honesty + 0.10*truth_problem + 0.10*competence_fit
             + 0.05*evidence_quality
             − 0.15*capture_risk   # then clamp 0–10

clownpoints  ≈ max of:
  - inverted incentives (subsidise the problem)
  - fantasy euros without source
  - wrong competence theatre
  - pure symbolic spend with zero measurable outcome
  - contradiction with own stated goal
```

**Clownpoints ≠ personal insult.** Score the **instrument**. Harsh language only if the **mechanism** is absurd.

### 5.4 Confidence on the score itself

| `score_confidence` | When |
|--------------------|------|
| `strong` | Primary text + solid evidence base + clear mechanism |
| `medium` | Clear proposal text; evidence partial |
| `weak` | Only press paraphrase; instrument fuzzy |
| `speculative` | Rumour / trial balloon |

If `weak` or lower: still score, but **do not** put in top public “worst/best of week” without a caveat banner.

### 5.5 Anti-bias rules

| Rule | Practice |
|------|----------|
| Same rubric for every party | Including ideas we like |
| Blind first pass optional | Score instrument before reading party brand (when feasible) |
| Steelman required | Best-case reading of proponent in 3–5 lines |
| Kill our priors | If strong evidence supports a “left” or “right” tool, say so |
| No ethnic collective blame | Incentives, selection rules, cohort data only |
| Re-score protocol | New primary data → bump `analysis_version`, keep history in notes |

### 5.6 Linkage to DOGE

| If proposal… | Then |
|--------------|------|
| Creates / expands a subsidy | Create or link `leaderboard` / `commitments` seed when € known |
| Hides cost | Note opacity; optional FOI after adoption |
| Cuts real waste | Positive genius; cite DOGE item IDs |
| Is already paid absurdity rebranded | High clownpoints + DOGE link |

---

## 6. Layer C — Showcase & visualisation

### 6.1 Public surfaces (order of build)

| # | Surface | Format | Audience |
|---|---------|--------|----------|
| 1 | **Repo leaderboards** | Markdown in `proposal-radar/public/` | Us + early followers |
| 2 | **Proposal cards** | One MD page per scored prop | Shareable deep links later |
| 3 | **Weekly Clowns & Genius** | 5 worst + 3 best + 1 “mixed but fixable” | Media / X |
| 4 | **X thread template** | Instrument → 4 facts → score → falsifier | Flanders-first |
| 5 | **Static site** (later) | GitHub Pages / simple Next/Astro | Voters |
| 6 | **Interactive filters** (later) | Party, competence, € band, score | Nerds + press |

### 6.2 Card layout (minimum viable)

```text
┌──────────────────────────────────────────┐
│  [Clownpoints 8.5]  [Genius 1.5]  −7.0   │
│  Title of proposal                        │
│  Actor · party · competence · date        │
│  1-line steelman                          │
│  1-line why it fails / works              │
│  Fiscal: €X–Y /yr (confidence)            │
│  Falsifier: …                             │
│  Sources: [1] [2]                         │
└──────────────────────────────────────────┘
```

Visual direction (from [naming.md](naming.md)): high contrast, data-native, deep blue/black + one accent. **Score bars > cartoon clowns** in serious outlets; clown emoji OK on X only if the **substance** is already paid.

### 6.3 Media integration (doc 08)

New pillar:

| Pillar | Cadence | Hook |
|--------|---------|------|
| **Clowns & Genius** | 1× / week | Same rubric, all parties |
| Falsification Friday | keep | Can use Radar kills |
| DOGE autopsy | keep | Link when proposal = budget line |

**4 facts still bind:** tax wedge, deficit, one concrete absurdity (DOGE or clown proposal), one fix.

### 6.4 What not to ship

- Live “AI decides votes” framing  
- Unreviewed legal conclusions as court fact  
- Fake precision (€3,847,221 without source)  
- Rankings that only roast one side for a month (credibility death)

---

## 7. Operating model

| Mode | Cadence | Who |
|------|---------|-----|
| **Radar tick** | Manual `/proposal-radar` or scheduled (e.g. 6–24h) | Agent |
| **Ingest seed** | Anytime URL lands | Human or agent |
| **Weekly public pack** | Monday or Friday | Agent draft → human publish OK |
| **Re-score** | On adoption / major amend | Agent |

Full protocol: [`proposal-radar/LOOP.md`](proposal-radar/LOOP.md)

**One primary unit per tick** (same discipline as DOGE): either ingest-and-queue **or** full analysis of one proposal — not 15 half-scores.

---

## 8. Data ownership

| Path | Role |
|------|------|
| `docs/proposal-radar/data/proposals.csv` | Master index + scores |
| `docs/proposal-radar/data/sources.csv` | Provenance |
| `docs/proposal-radar/data/ingest_queue.csv` | Unscored candidates |
| `docs/proposal-radar/data/loop_state.csv` | Cursor |
| `docs/proposal-radar/analyses/{id}.md` | Full memos |
| `docs/proposal-radar/public/` | Leaderboards & weekly packs |
| `docs/proposal-radar/raw/` | Feed dumps, HTML/PDF snapshots |
| `docs/proposal-radar/schema.md` | Column dictionary |

---

## 9. Success metrics (honest)

| Metric | Good signal | Bad signal |
|--------|-------------|------------|
| Scored proposals with primary source | Rising | Press-only forever |
| Re-scores when bills change | Happens | Set-and-forget |
| Same-party harsh scores published | Yes | Only opponents roasted |
| Media cites method not just insult | Occasional | “Clown party” only |
| Link rate DOGE ↔ Radar | Growing | Two silos |

---

## 10. Phased build (concrete)

| Phase | Deliverable | Done when |
|-------|-------------|-----------|
| **P0** | Docs + schema + skill + empty queues | Done |
| **P1** | 10 scored Belgian proposals (diverse) | Done 2026-07-27 — human review next |
| **P2** | Weekly public pack automated in tick | Export script live; cadence ongoing |
| **P3** | RSS allowlist harvester → ingest_queue | Live (`scripts/rss_harvest.py`); tune feeds |
| **P4** | Static scoreboard site | Shareable URL |
| **P5** | Optional: parliament bill watcher | New bills auto-seeded |

**Run now:** `python docs/proposal-radar/scripts/run_pipeline.py` then `/proposal-radar` to score queue heads.

---

## 11. Red lines

- Belgium jurisdiction only (EU only if binds BE).  
- No invented membership, polls, or euro savings.  
- No hate content; no violence advocacy.  
- Legal notes = orientation; “verify with counsel”.  
- Human remains accountable for **publish** decisions; agents draft.

---

## 12. One-sentence brand

> **Humans accountable. Machines for truth-checking. Every proposal gets the same exam — from circus to rare genius.**
