# 06b — DOGE discovery strategy

**How we find (almost) all spending, subsidies, and waste — forever.**  
We will never finish in one pass. The system is a **loop**: map → drill → flag gaps → FOI → fill → re-rank.

Related: [06-doge-belgium.md](06-doge-belgium.md) · data: [doge/](doge/) · loop: [doge/LOOP.md](doge/LOOP.md)

---

## 1. Goal

1. Hierarchical overview of **all public money** in Belgium  
2. Every **subsidy** class (cash, multi-year, tax expenditure, guarantee, in-kind, regulatory privilege)  
3. **L5 waste** — real projects (e.g. €800k podcast / 3 years), not only ministry totals  
4. **Federalism overhead** as a first-class cost  
5. When a flow has **no public output** → queue an **openbaarheid van bestuur** request and track it until answered  

**Honesty rule:** unknown is allowed; invented euros are not.

---

## 2. Why Belgium is a maze

| Layer | Money examples |
|-------|----------------|
| Federal | FOD/SPF budgets, justice, defence, federal fiscal tools |
| Social security | RSZ/ONSS, RIZIV/INAMI, pensions — often larger than “ministries” |
| Communities | Education, culture, media (Vlaamse Gemeenschap, FWB, DG) |
| Regions | Economy, mobility, housing, environment (VL / WAL / BRU) |
| Provinces | Grants + own overhead |
| Local + OCMW/CPAS | Project subsidies, culture, patronage risk |
| Parastatals / SOEs / intercommunales | Soft budgets, annual reports |
| EU / RRF | Multi-year co-financing; double-count risk |
| Tax expenditures | Off-budget cost of rates/exemptions |
| **Structure overhead** | Dual cabinets, parallel NL/FR bodies, advice forests |

A multi-year subsidy may appear only as year-1 cash, an *engagement*, a decision letter, or a line in an agency report. Track the **lifecycle**: decision → commitment → annual cash → evaluation → renew/die.

---

## 3. Drill-down hierarchy

```text
L0  General government (NBB/ESA total)
L1  Sector (federal / SS / Flanders / Wallonia / Brussels / communities / local / other)
L2  Entity (ministry, agency, insurer, city, SOE)
L3  Department / policy function (COFOG or budget title)
L4  Programme / basisallocatie
L5  Real unit: named scheme, grant decision, project, contract
L6  Payment year-slice (cash trail)
```

| Level | Use |
|-------|-----|
| L0–L3 | Navigation: where is the fat? |
| L4 | Prioritise which drawer to open |
| **L5** | **Leaderboard / media** — real waste |
| L6 | Audit trail |

**Voter story:** €100 pie → fat department → open drawer → named absurd project.

---

## 4. What counts as subsidy / waste surface

| Class | Hides in |
|-------|----------|
| Direct grant | Budget articles, steun portals |
| Multi-year commitment | Engagementen, multi-year decisions |
| Tax expenditure | FPS inventory (+ regional) |
| Soft loan / guarantee | Annexes, SOE notes |
| In-kind | Premises, seconded staff (FOI) |
| Regulatory privilege | Not in budget; still cost |
| Cross-layer transfer | Federal→region→city→NGO (double-count) |
| Complexity overhead | Cabinets, dual structures, platforms |

---

## 5. Source catalogue

### Top-down

- NBB / NAI public finance (ESA) — L0–L1  
- Eurostat / OECD COFOG  
- Federal general expenditure budget + policy notes  
- **FPS Finance inventory of federal tax expenditures** (XLSX)  
- Flanders / Wallonia / Brussels / FWB budgets  
- Large city budgets (top spenders first)  
- Court of Audit (Rekenhof / Cour des comptes)  
- EU State aid / RRF dashboards  
- Agency & intercommunale annual reports  

### Bottom-up (L5)

- Grant / steun decision lists  
- e-Procurement / TED  
- Parliamentary questions  
- **Openbaarheid van bestuur / FOI** (see §7)  
- Press → verify → FOI  
- Beneficiary annual accounts listing public grants  

### Horizontal (overhead)

Workstream **OH-1**: cabinets, dual agencies, permanent platforms, “same function three times.”

---

## 6. Multi-year protocol

Store in `docs/doge/data/commitments.csv`:

- total envelope + cash_by_year + remaining  
- beneficiary, legal basis, evaluation Y/N  
- status: `planned` | `active` | `ended` | `renewed`  
- cut_option: kill now / let expire / clawback  

**Display:** `€267k/yr · €800k over 3y` (never hide multi-year totals).

**Future money:** regeerakkoord items, open calls, draft budgets → status `planned`.

---

## 7. Missing information → FOI queue (critical)

We will **not** find everything online. Any money flow that is:

- amount without project/output, or  
- project without amount, or  
- L4 programme with no L5 breakdown, or  
- refused / opaque beneficiary list  

…must create a row in **`docs/doge/data/foi_queue.csv`**.

### FOI queue fields (see schema)

| Field | Purpose |
|-------|---------|
| `gap_id` | Stable id |
| `hierarchy_path` | L2>L3>L4… |
| `entity_id` | Who holds the info |
| `what_is_missing` | Precise ask |
| `why_it_matters` | Waste / transparency |
| `legal_basis_hint` | Openbaarheid van bestuur / FOI law |
| `recipient_body` | Official name |
| `recipient_email` | If known |
| `recipient_postal` | Fallback |
| `draft_letter_path` | Filled template file |
| `status` | `draft` → `ready` → `sent` → `waiting` → `partial` → `answered` → `refused` → `appealed` |
| `date_ready` / `date_sent` / `date_due` / `date_answered` | SLA tracking |
| `response_summary` | What we got |
| `linked_commitment_id` / `linked_leaderboard_id` | After fill |

### Process

1. Discovery finds gap → **always** add FOI row (do not leave as silent Unknown forever).  
2. Agent or human fills letter from [`doge/foi-template-nl.md`](doge/foi-template-nl.md) (FR twin later).  
3. Status `ready` = human may send (email/post). **Agents do not send mail unless explicitly ordered.**  
4. On answer: update commitments/leaderboard; set FOI `answered`; archive letter + reply refs in `docs/doge/foi/archive/`.  
5. On silence past legal deadline: status `overdue`; escalate (reminder letter, appeal path — document only).

### Batch “send day”

Filter `status=ready`, sort by `priority`, export mail-merge list. Humans send; mark `sent` + date.

---

## 8. Recurring research loop (every 15 minutes)

Full agent protocol: [`doge/LOOP.md`](doge/LOOP.md).

```text
┌─────────────────────────────────────────────┐
│  LOOP TICK (target: every 15 min)           │
│  1. Load queues (research + FOI + sprint)   │
│  2. Pick highest-priority open work unit    │
│  3. Gather public sources (web/budget/PDF)  │
│  4. Write facts into CSVs (sourced)         │
│  5. If gap remains → FOI queue row + draft  │
│  6. Promote solid L5 → leaderboard          │
│  7. Log tick in loop_log.md                 │
│  8. Stop when tick budget exhausted         │
└─────────────────────────────────────────────┘
         │
         ▼  (never “done” — only “queue empty of actionable public work”)
```

**Completion definition (honest):**

- Not 100% of Belgian public money itemised (impossible short-term).  
- “Coverage improved” = more L1 mapped, more L5 entries, fewer high-priority FOI gaps.  
- Loop may idle when: no open research tasks **and** FOI only in `waiting` (ball in administration’s court).

**Human gates:** sending FOI letters; legal threats; public accusations of fraud without evidence.

**Git:** each successful tick **commits and pushes** to the remote (see `doge/LOOP.md` §6).

---

## 9. Research sprints (priority order)

| Sprint | Outcome |
|--------|---------|
| **0** Scaffold | Strategy, schema, entities, queues, loop (this PR) |
| **1** Big map | L0–L1 split; top entities by spend |
| **2** Tax expenditures | Import FPS inventory; rank |
| **3** Flanders deep dive | Top programmes + 20 L5 examples |
| **4** Federal discretionary | Cabinets, comms, project subsidies |
| **5** Local absurdity | 5 cities; L5 gold |
| **6** Overhead | Dual structures; triple-subsidy cases |
| **∞** Weekly | ≥1 L5 leaderboard entry; FOI batch |

---

## 10. Quality gates

1. Source URL + access date + confidence on every €  
2. Understate rather than invent  
3. Double-count flags on cross-layer flows  
4. Separate entitlements vs discretionary (politics differ)  
5. Steelman the stated public goal  
6. FOI for persistent opacity — no permanent silent holes on high-€ lines  

---

## 11. Roles

| Role | Job |
|------|-----|
| Loop agent | 30-min ticks: fill data, draft FOI |
| FOI clerk (human) | Send letters, log replies |
| Data lead | Schema integrity, no double-count |
| Editor | Leaderboard narrative quality |
| Counsel | Legal edges on FOI / defamation |

---

## 12. Assumption checks

| Assumption | Confidence | If wrong |
|------------|------------|----------|
| FOI yields usable L5 for high-€ opaque lines | Medium–Strong | Parliamentary questions + press |
| 30-min loop beats big-bang research | Medium | Longer deep-work sessions for PDF budgets |
| CSV-first scales to thousands of rows | Medium | Move to SQLite later |
| Completeness is asymptotic | Strong | — |
