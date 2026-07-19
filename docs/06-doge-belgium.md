# 06 — DOGE Belgium & Absurdity Leaderboard

## Mission

Create a permanent, public, evidence-based **Department of Government Efficiency (Belgium)** — not as a meme alone, but as:

1. A **kill-list** of subsidies, tax expenditures, agencies, and rules with terrible ROI  
2. A **leaderboard** ranked by *cost × absurdity*  
3. A **legislative pipeline** so cuts are bill-shaped, not tweet-shaped  

If we ever hold executive power, this becomes a real office with a quarterly public scorecard. Until then, it is the brand and the research engine.

### How we fill this board

| Doc / path | Role |
|------------|------|
| [06b-doge-discovery-strategy.md](06b-doge-discovery-strategy.md) | Full map: hierarchy, sources, multi-year, overhead |
| [doge/LOOP.md](doge/LOOP.md) | Recurring research loop (target every 30 min) |
| [doge/notes-middleman-systems.md](doge/notes-middleman-systems.md) | Cheques + union unemployment payment (middleman waste) |
| [doge/](doge/) | CSV data, FOI queue, letter drafts |
| `/doge-loop` skill | One automated tick |

**Missing public detail → FOI queue** (`doge/data/foi_queue.csv`), never silent forever on high-€ opacity.

---

## Rules of the game (no vibes-only)

### Every entry must have

| Field | Required |
|-------|----------|
| Name | What exactly |
| Level | Federal / Flanders / Wallonia / Brussels / local / EU-funded |
| Type | Subsidy / tax expenditure / agency / regulation / procurement / overhead-federalism / other |
| Hierarchy path | L2>L3>L4>L5 when known |
| Annual cost (range) | € run-rate; **Unknown** allowed if honest |
| Total / multi-year cost (TCO) | Full envelope if multi-year (e.g. €800k / 3y) |
| Confidence | Strong / Medium / Weak |
| Source class | Budget line, audit, press + FOI, academic, … |
| Beneficiaries | Who captures value |
| Stated goal | What politicians claim |
| Measured outcome | What we can show |
| Absurdity score | 1–10 (rubric below) |
| Cut proposal | Abolish / reform / sunset / privatise |
| Political difficulty | 1–10 |
| Net priority | computed |
| FOI gap id | If still opaque — link to `foi_queue` |

### Forbidden

- Invented euro amounts  
- Double-counting the same euro in three entries  
- Racist framing of beneficiaries  
- Ranking only “left” waste while ignoring business-client subsidies  

### Corrections log

Wrong entries get **struck with date + reason**, not silently edited. Truth brand dies if we cheat.

---

## Scoring rubric

### Cost score (0–10)

| Annual cost (order of magnitude) | Score |
|----------------------------------|-------|
| < €1M | 1–2 |
| €1–10M | 3–4 |
| €10–100M | 5–6 |
| €100M–1B | 7–8 |
| > €1B | 9–10 |

Use ranges; prefer understatement.

### Absurdity score (1–10)

Average of:

1. **Goal failure** — does it miss its stated purpose?  
2. **Perverse incentive** — does it reward harm (non-work, pollution theatre, cartelisation)?  
3. **Capture** — concentrated private gain, diffuse public cost  
4. **Duplication** — three agencies, one job  
5. **Complexity tax** — admin cost larger than transfer value  
6. **Moral hazard** — encourages risk dumped on taxpayers  

### Priority index

```text
priority = 0.55 * cost_score + 0.35 * absurdity_score + 0.10 * (10 - difficulty)
```

Sort leaderboard by `priority` descending.  
**Also publish** pure cost ranking and pure absurdity ranking (different stories).

---

## Leaderboard v0 (seed — VERIFY before campaign use)

> These are **starting hypotheses** for research, not audited campaign claims.  
> Replace “TBD” with budget lines. Promote to Strong only with sources.

| Rank | Item | Level | Type | Cost/yr | Conf. | Absurdity | Why it’s on the list | Cut proposal |
|------|------|-------|------|---------|-------|-----------|----------------------|--------------|
| 1 | **Labour-tax + benefit interaction traps** | Fed | System design | Systemic (wedge ~highest OECD) | Strong on wedge; Med on trap € | 9 | Punishes work; fuels black economy | Redesign wedge + smooth phase-outs |
| 2 | **Company car / mobility fiscal privilege stack** | Fed | Tax expenditure | High (TBD €B class historically) | Med–Strong | 8 | Distorts wages & congestion; complex | Cash-out / equalise; simplify |
| 3 | **Overlapping economic subsidies to firms** (regions + fed + EU) | Multi | Subsidy | High TBD | Med | 8 | Often relocates activity, doesn’t create it | Publish all; kill below ROI hurdle |
| 4 | **Early labour-market exit / pension special schemes** | Fed | Entitlement design | High TBD | Med–Strong | 8 | Shifts ageing cost onto workers | Close schemes; automatic adjusters |
| 5 | **Multi-layer advisory bodies & political cabinets culture** | Multi | Admin | Med–High TBD | Med | 9 | Talk shops; blurred accountability | Cap cabinets; merge bodies |
| 6 | **Energy subsidy stacks with poor targeting** | Multi | Subsidy | High TBD | Med | 7 | Regressive + intermediary capture risk | Price signals; target poor only |
| 7 | **Housing supply blocks + compensatory subsidies** | Multi | Reg + subsidy | High indirect | Med | 9 | Cause scarcity, then subsidise victims of scarcity | YIMBY first; then retarget aid |
| 8 | **Inactive non-profit / project subsidy long tail** | Multi | Subsidy | Med sum of small | Med | 8 | Death by a thousand grants | Publish; sunset; competitive outcomes |
| 9 | **Duplicate digital & IT projects across governments** | Multi | Procurement | Med TBD | Med | 7 | Same portal, fifth time | Shared platforms; kill zombies |
| 10 | **Professional order / permit denseness for entry** | Multi | Regulation | Indirect | Med | 7 | Protects insiders | Sunrise reviews; mutual recognition |
| 11 | **Local vanity infrastructure with weak CBA** | Local | Capex | Varies | Med | 8 | Ribbon-cutting > NPV | Mandatory published CBA |
| 12 | **Training vouchers / activation with weak job placement** | Multi | Subsidy | Med TBD | Med | 7 | Attendance ≠ employment | Pay for placement outcomes |
| 13 | **Sectoral support that survives after crisis** | Multi | Subsidy | Med TBD | Med | 8 | Temporary becomes permanent | Hard sunsets |
| 14 | **Foreigner/policy NGO funding without outcome KPIs** | Multi | Subsidy | Low–Med | Weak–Med | 7 | Unclear ROI | KPI or cut |
| 15 | **Agricultural / land schemes with perverse land prices** | Multi/EU | Subsidy | Med–High | Med | 6 | Capitalised into land | Align with productivity + environment metrics |
| 16 | **Media & party-adjacent transfers opacity** | Multi | Transfer | TBD | Weak–Med | 8 | Speech + money entanglement | Radical transparency |
| 17 | **Health billing waste & low-value care** | Fed | System | High TBD | Med | 7 | Volume ≠ health | Transparency + contestability |
| 18 | **Empty building public estate** | Multi | Asset waste | Med TBD | Med | 7 | Capital idle | Sell/lease; housing conversion |
| 19 | **Municipal shareholdings in zombie companies** | Local | SOE | Varies | Med | 7 | Soft budget constraint | Divest non-core |
| 20 | **“Awareness campaigns” with no behaviour change** | Multi | Opex | Low–Med | Med | 9 | Poster politics | Kill unless RCT/evidence |

**Next research sprints:** attach official budget codes from:

- Federal general expenditure budget  
- Flemish budget & tax expenditures  
- Court of Audit (*Rekenhof / Cour des comptes*) reports  
- NBB public finance breakdowns  
- EU State aid cases involving Belgian measures  

---

## Product: public leaderboard site (later)

Minimum viable:

1. Sortable table (cost, absurdity, priority)  
2. One-page autopsy per top 25  
3. “Submit a waste” form → GitHub issue  
4. API dump (CSV)  
5. Party voting tracker: did MPs protect the waste?

Repo can start as markdown; site later.

---

## Institutional design of DOGE-BE (in power)

| Element | Design |
|---------|--------|
| Head | Fixed term; public KPI: € cut + rules repealed |
| Staff | Auditors, data, lawyers — not patronage |
| Powers | Propose freezes; require public justification for each kept line |
| Limits | Cannot break statutes alone; parliament still votes |
| Transparency | Weekly open data; no secret carve-outs |
| Anti-capture | Staff rotation; ban recent beneficiaries as advisors |

### First 100-day DOGE package (template)

1. Freeze new discretionary subsidies  
2. Publish full tax expenditure list  
3. Kill bottom 50 programmes under €X with no statutory mandate  
4. Merge duplicate agencies  
5. Cabinet size hard cap  
6. One-in-two-out regulation order  
7. Public dashboard  

---

## Points game (engagement)

Community can earn **public points** (leaderboard of hunters, not money — legal caution):

| Action | Points |
|--------|--------|
| Documented waste entry with source | +10 |
| Official budget line found for TBD item | +20 |
| Court of Audit citation | +25 |
| Draft repeal article text | +30 |
| Successful FOI that unblocks a number | +40 |
| Entry retracted as wrong | −15 to submitter (honesty culture) |

No payments for points without legal review (party finance risk).

---

## How this elects people

1. **Weekly content engine** — endless concrete stories  
2. **Media magnet** — journalists love ranked absurdity  
3. **Coalition weapon** — “vote for our cut list or no deal”  
4. **Trust** — when we admit errors, we look unlike legacy parties  

Link every campaign ad to **three live leaderboard items**.

---

## Open research issues

1. Best single open dataset for federal tax expenditures? → FPS inventory XLSX (sprint 2)  
2. How to attribute regional vs federal double subsidies? → `attribution_key` in flows  
3. Standard method for “indirect cost” of regulation (hours × wage)?  
4. Local budget scraping for top 20 cities?  
5. Keep `foi_queue` empty of high-priority `draft` items (always convert opacity to letters)

Track in `docs/doge/data/research_queue.csv` and GitHub issues with label `doge`.

## FOI / openbaarheid

We cannot scrape paradise. For any material flow without public L5 output:

1. Log gap in `docs/doge/data/foi_queue.csv`  
2. Draft letter from `docs/doge/foi-template-nl.md`  
3. Human sends; track `sent` → `waiting` → `answered`  
4. Fill commitments/leaderboard from the reply  

Institutions are generally **obliged** to handle openbaarheid requests under applicable federal/regional/local rules (deadlines and exceptions vary — verify per body).
