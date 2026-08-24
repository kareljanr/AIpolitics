# -*- coding: utf-8 -*-
"""Tick 2306: Alvinnenberg Leuven YE2025 — APPEND-ONLY CSVs."""
from __future__ import annotations

import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
RAW = DATA / "raw" / "tick2306"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"

UTC = "2026-08-27T19:45:00Z"
TICK = "2306"
RQ, NEXT_RQ = "rq_2306", "rq_2307"
ENTITY = "vzw_alvinnenberg_leuven"
KBO = "0434.390.150"
GAP = "gap_alvinnenberg_nbb_pdf_assets_debt_bruto_gt_omzet_8_39x_pnl_drop_97pct_fte_jump_vaph_matrix_l5"
LB = "lb_alvinnenberg_bruto_9_38m_omzet_1_12m_8_39x_pnl_drop_97pct_fte_jump_jr2025"
COMM = "comm_alvinnenberg_jr2025_statutory_vaph_bruto_9_38m_8_39x_pnl_drop"

OMZET, OMZET24 = 1118535, 1123057
BRUTO, BRUTO24 = 9383673, 9326560
PNL, PNL24 = 21262, 737745
EQUITY, EQUITY24 = 8224819, 7888020
FTE, FTE24 = 117.6, 112.8
FILED = "10.07.2026"
EMAIL = "directie@alvinnenberg.be"
ADDR = "Gaston Feremanslaan 27, 3001 Leuven"
RATIO = round(BRUTO / OMZET, 2)  # 8.39
# cost 3.5 (<10m) · abs 8.0 (8.39x + pnl DROP -97%) · diff 3 → pi = 0.55*3.5 + 0.35*8 + 0.1*7 = 5.425 → 5.45
ABS, COST, DIFF, PI = 8.0, 3.5, 3.0, 5.45


def append_csv(path: Path, rows: list[dict], id_key: str) -> None:
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames, existing = reader.fieldnames, list(reader)
    have = {r.get(id_key) for r in existing}
    new = [r for r in rows if r.get(id_key) not in have]
    if not new:
        print(path.name, "skip")
        return
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in new:
            w.writerow({k: r.get(k, "") for k in fieldnames})
    print(path.name, "+", len(new))


RAW.mkdir(parents=True, exist_ok=True)
FOI_DRAFTS.mkdir(parents=True, exist_ok=True)

with (DATA / "loop_state.csv").open(encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        if r.get("state_id") == "main" and int(r.get("ticks_completed") or 0) >= 2306:
            raise SystemExit(f"already at {r.get('ticks_completed')}")

(RAW / "cw_en_excerpt.txt").write_text(
    f"Alvinnenberg YE2025 omzet {OMZET} bruto {BRUTO} ~{RATIO}x pnl DROP {PNL} equity {EQUITY} FTE {FTE} filed {FILED}\n"
    "https://www.companyweb.be/en/0434390150/alvinnenberg\n",
    encoding="utf-8",
)

append_csv(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_alvinnenberg_jr2025_cw_en",
            "title": f"Alvinnenberg YE2025 CW EN (bruto 9.38m / omzet 1.12m ~{RATIO}x / pnl DROP -97%)",
            "url": "https://www.companyweb.be/en/0434390150/alvinnenberg",
            "publisher": "Companyweb",
            "accessed_date": "2026-08-27",
            "source_class": "companyweb",
            "notes": f"tick{TICK}; Medium CW EN; omzet DROP {OMZET} (-0.4%); bruto JUMP {BRUTO} (~{RATIO}x); pnl DROP {PNL} (-97.12%); equity JUMP {EQUITY}; FTE JUMP {FTE}; filed {FILED}",
        },
        {
            "source_id": "src_alvinnenberg_jr2025_cw_nl",
            "title": "Alvinnenberg YE2025 Companyweb NL",
            "url": "https://www.companyweb.be/nl/0434390150/alvinnenberg",
            "publisher": "Companyweb",
            "accessed_date": "2026-08-27",
            "source_class": "companyweb",
            "notes": f"tick{TICK}; Medium CW NL; neerlegging {FILED}",
        },
        {
            "source_id": "src_alvinnenberg_jr2025_cw_fr",
            "title": "Alvinnenberg YE2025 Companyweb FR",
            "url": "https://www.companyweb.be/fr/0434390150/alvinnenberg",
            "publisher": "Companyweb",
            "accessed_date": "2026-08-27",
            "source_class": "companyweb",
            "notes": f"tick{TICK}; Medium CW FR; CA {OMZET}; marge {BRUTO}; résultat {PNL}",
        },
        {
            "source_id": "src_alvinnenberg_kbo_0434390150",
            "title": "KBO Alvinnenberg 0434.390.150 Actief VZW NACE 87.202 Leuven",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0434390150",
            "publisher": "KBO / BCE",
            "accessed_date": "2026-08-27",
            "source_class": "kbo",
            "notes": f"tick{TICK}; Strong KBO Actief; VZW 04.11.1987; Gaston Feremanslaan 27 3001 Leuven; RSZ 87.202",
        },
        {
            "source_id": "src_alvinnenberg_site_contact_2306",
            "title": "Alvinnenberg FOI directie@alvinnenberg.be",
            "url": "https://www.alvinnenberg.be/",
            "publisher": "Alvinnenberg VZW",
            "accessed_date": "2026-08-27",
            "source_class": "foi_contact",
            "notes": f"tick{TICK}; {EMAIL}; {ADDR}",
        },
    ],
    "source_id",
)

append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Alvinnenberg VZW (Leuven / VAPH woonondersteuning)",
            "name_fr": "Alvinnenberg ASBL (Louvain / VAPH hébergement)",
            "name_en": "Alvinnenberg VZW (Leuven VAPH residential care)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.alvinnenberg.be/",
            "foi_email": EMAIL,
            "foi_postal": ADDR,
            "notes": (
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW RSZ 87.202; "
                f"omzet DROP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} (-97.12%) equity JUMP {EQUITY} FTE JUMP {FTE}; "
                f"neerlegging {FILED}; FOI {GAP}; after TM Kempen@2305; AGB Bornem JR2024; FARO YE2024; not TE-additive"
            ),
        }
    ],
    "entity_id",
)

append_csv(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_alvinnenberg_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": f"CW bruto YE2025 primary (~{RATIO}x omzet)",
            "source_id": "src_alvinnenberg_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; bruto {BRUTO}",
        },
        {
            "budget_id": "bud_alvinnenberg_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW omzet YE2025",
            "source_id": "src_alvinnenberg_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; omzet {OMZET}",
        },
        {
            "budget_id": "bud_alvinnenberg_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW pnl YE2025 DROP -97%",
            "source_id": "src_alvinnenberg_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; pnl {PNL} vs {PNL24}",
        },
        {
            "budget_id": "bud_alvinnenberg_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW equity YE2025",
            "source_id": "src_alvinnenberg_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; equity {EQUITY}",
        },
        {
            "budget_id": "bud_alvinnenberg_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": "CW FTE YE2025",
            "source_id": "src_alvinnenberg_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; FTE {FTE}",
        },
    ],
    "budget_id",
)

append_csv(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": f"Alvinnenberg YE2025 leftover dual (bruto 9.38m / omzet 1.12m ~{RATIO}x / pnl DROP -97% / Medium)",
            "entity_id": ENTITY,
            "beneficiary": "VAPH cliënten Leuven woon/dag path",
            "legal_basis": f"VZW Alvinnenberg (KBO {KBO}; Actief; RSZ 87.202)",
            "decision_date": "2026-07-10",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(BRUTO),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                f'"2025_fte":{FTE},"2024_omzet":{OMZET24},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},'
                f'"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0434390150/alvinnenberg",
            "stated_goal": "Flemish VAPH residential + day support Leuven",
            "cut_option": f"Publish NBB PDF; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -97% vs VAPH matrix",
            "source_id": "src_alvinnenberg_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Leuven>Alvinnenberg>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO} (~{RATIO}x); after TM Kempen@2305",
        }
    ],
    "commitment_id",
)

append_csv(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": f"Alvinnenberg bruto 9.38m / omzet 1.12m ~{RATIO}x / pnl DROP -97% / FTE JUMP (YE2025)",
            "level": "L5",
            "type": "vaph_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Leuven>Alvinnenberg>JR2025",
            "annual_cost_eur": str(BRUTO),
            "total_cost_eur": str(BRUTO),
            "tco_notes": (
                f"CW omzet DROP {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x) / pnl DROP {PNL} (-97.12% vs {PNL24}) / "
                f"equity JUMP {EQUITY} / FTE JUMP {FTE} / filed {FILED}"
            ),
            "confidence": "medium",
            "source_id": "src_alvinnenberg_jr2025_cw_en",
            "beneficiaries": "VAPH adults mental disability Leuven",
            "stated_goal": "Flemish VAPH residential + day support",
            "measured_outcome": f"bruto÷omzet ~{RATIO}x; pnl DROP -97%; FTE JUMP {FTE}",
            "absurdity_score": str(ABS),
            "cost_score": str(COST),
            "difficulty": str(DIFF),
            "priority_index": str(PI),
            "cut_proposal": f"Publish NBB PDF FOI; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -97%",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after TM Kempen@2305",
        }
    ],
    "item_id",
)

append_csv(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Leuven>Alvinnenberg>NBB_PDF_assets_debt_bruto_gt_omzet_vaph",
            "entity_id": ENTITY,
            "what_is_missing": (
                f"NBB PDF YE2025; why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x); "
                f"pnl DROP EUR{PNL} (-97.12% vs EUR{PNL24}); FTE JUMP {FTE}"
            ),
            "why_it_matters": (
                f"Medium CW VAPH Leuven residential VZW (bruto 9.38m / omzet 1.12m ~{RATIO}x / "
                f"pnl DROP -97% / FTE JUMP 117.6); assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "Alvinnenberg VZW",
            "recipient_email": EMAIL,
            "recipient_postal": ADDR,
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-27",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": COMM,
            "linked_leaderboard_id": LB,
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO",
        }
    ],
    "gap_id",
)

(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — Alvinnenberg (NBB PDF / bruto≫omzet ~{RATIO}x / pnl DROP -97%)

**gap_id:** `{GAP}` · **status:** ready NOT sent · **tick:** {TICK}  
**entity:** Alvinnenberg VZW — KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; RSZ **87.202**)  
**recipient:** {EMAIL}

## Brief
```text
Aan: Alvinnenberg VZW via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 Alvinnenberg (KBO {KBO})

1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — VAPH/PVB-matrix.
3. Toelichting pnl DROP EUR{PNL} (−97.12% vs YE2024 EUR{PNL24}).
4. FTE JUMP {FTE} vs {FTE24} vs care matrix.
5. Schulden LT/KT en liquide middelen YE2025.

Ref: {GAP}
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rqfields, rqrows = list(r.fieldnames or []), list(r)
for row in rqrows:
    if row.get("task_id") == RQ:
        if row.get("status") == "done":
            raise SystemExit("rq_2306 already done")
        row.update(
            {
                "status": "done",
                "entity_id": ENTITY,
                "updated_utc": UTC,
                "blocked_gap_id": GAP,
                "title": f"leftover dual — Alvinnenberg YE2025 Medium (bruto 9.38m / omzet 1.12m ~{RATIO}x / pnl DROP -97%)",
                "notes": f"tick{TICK} Alvinnenberg; bruto {BRUTO} ~{RATIO}x; pnl {PNL}; FOI ready NOT sent",
            }
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": "leftover dual after Alvinnenberg — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"After Alvinnenberg YE2025 Medium (bruto 9.38m ~{RATIO}x / pnl DROP -97%). "
                "Prefer AGB/FARO if YE2025 else unused (Havenzate/Homevil/Huis in de Stad if FREE YE2025). "
                "Do NOT redo Alvinnenberg/TM Kempen/BC Elisabeth/Levensvreugde/Kompas/Voluit/MLP stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK}; next every-10 2310",
        }
    )
with (DATA / "research_queue.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rqfields, extrasaction="ignore")
    w.writeheader()
    for row in rqrows:
        w.writerow({k: row.get(k, "") for k in rqfields})

with (DATA / "loop_state.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    lsfields, lsrows = list(r.fieldnames or []), list(r)
for row in lsrows:
    if row.get("state_id") == "main":
        row.update(
            {
                "last_tick_utc": UTC,
                "last_unit_id": RQ,
                "ticks_completed": TICK,
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover dual Alvinnenberg {KBO} Medium "
                    f"(omzet DROP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -97.12%; "
                    f"equity JUMP {EQUITY}; FTE JUMP {FTE}); after TM Kempen@2305; "
                    f"AGB Bornem JR2024; FARO YE2024; next {NEXT_RQ}; next every-10 2310"
                ),
            }
        )
with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, extrasaction="ignore")
    w.writeheader()
    for row in lsrows:
        w.writerow({k: row.get(k, "") for k in lsfields})

with LOG.open("a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Alvinnenberg Leuven (bruto 9.38m / omzet 1.12m ~{RATIO}x / pnl DROP -97% / Medium)

- Unit: **{RQ}** leftover dual after **rq_2305 TM Kempen**. Stalls YE2024. Took FREE VAPH **Alvinnenberg VZW** YE2025 (KBO **{KBO}**; Leuven; RSZ **87.202**).
- Found: omzet **EUR{OMZET}** DROP -0.4%; bruto **EUR{BRUTO}** (~**{RATIO}x**); pnl **EUR{PNL}** DROP -97.12% vs EUR{PNL24}; equity **EUR{EQUITY}**; FTE **{FTE}**; filed **{FILED}**. Medium. FOI via {EMAIL}.
- Wrote: APPEND sources/budgets/commitments/leaderboard/entities/foi; draft {GAP}; {RQ}=done + {NEXT_RQ} open; ticks={TICK}.
- FOI ready not sent. NOT every-10 (last 2300; next 2310).
"""
    )

n_bud = sum(1 for _ in (DATA / "budgets.csv").open(encoding="utf-8")) - 1
if n_bud < 50000:
    raise SystemExit(f"BUDGETS CORRUPT n={n_bud}")
print(f"OK tick{TICK} {ENTITY} bruto={BRUTO} ratio={RATIO}x pnl={PNL} pi={PI} next={NEXT_RQ} budgets={n_bud}")
