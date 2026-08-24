# -*- coding: utf-8 -*-
"""Tick 2217 leftover dual — Werkmmaat Antwerpen YE2025 Medium."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T18:00:00Z"

ENTITY = "vzw_werkmmaat_antwerpen"
BRUTO = 3236013
PNL = 535180
EQUITY = 1670067
FTE = 60.1
BRUTO_PY = 2572213
PNL_PY = 76261
EQUITY_PY = 1139805
FTE_PY = 62.3

SRC_EN = "src_werkmmaat_jr2025_cw_en"
COMM = "comm_werkmmaat_jr2025_statutory_maatwerk_empty_omzet_pnl_jump_602pct_equity_jump"
LB = "lb_werkmmaat_bruto_3_24m_empty_omzet_pnl_jump_602pct_equity_jump_jr2025"
GAP = "gap_werkmmaat_nbb_pdf_assets_debt_empty_omzet_pnl_jump_equity_jump_matrix_l5"

PI = "7.10"
ABS = "8.0"
COST = "4.6"
DIFF = "3.0"


def append_csv(path, rows):
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = r.fieldnames
    idkey = cols[0]
    have = {row[idkey] for row in existing}
    added = 0
    for row in rows:
        if row.get(idkey) in have:
            print("SKIP", path.name, row.get(idkey))
            continue
        existing.append({c: row.get(c, "") for c in cols})
        added += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
    print("append", path.name, "+", added, "total", len(existing))


def update_csv_rows(path, key, updates):
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        cols = r.fieldnames
        rows = list(r)
    n = 0
    for row in rows:
        if row.get(key) in updates:
            row.update(updates[row[key]])
            n += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("update", path.name, n)


append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_werkmmaat_jr2025_cw_nl",
            title="Companyweb NL Werkmmaat YE2025 statutory",
            url="https://www.companyweb.be/nl/0817381683/werkmmaat",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2217; YE2025 omzet empty; bruto JUMP {BRUTO} (+25.81%) pnl JUMP {PNL} (+601.77%) equity JUMP {EQUITY} (+46.52%) FTE DROP {FTE}; neerlegging 26.06.2026; raw docs/doge/data/raw/tick2217/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN Werkmmaat YE2025 statutory",
            url="https://www.companyweb.be/en/0817381683/werkmmaat",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2217; EN mirror YE2025 Medium; filed 26-06-2026; Turnover unpublished; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; Employees {FTE}; raw tick2217/",
        ),
        dict(
            source_id="src_werkmmaat_jr2025_cw_fr",
            title="Companyweb FR Werkmmaat YE2025 statutory",
            url="https://www.companyweb.be/fr/0817381683/werkmmaat",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2217; FR mirror YE2025 Medium; Dernier bilan 2025; CA non publie; Marge brute {BRUTO}; Benefice {PNL}; Capitaux propres {EQUITY}; raw tick2217/",
        ),
        dict(
            source_id="src_werkmmaat_kbo_2217",
            title="KBO Werkmmaat 0817.381.683 Actief VZW Antwerpen 10 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0817381683",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2217; Actief VZW sinds 10.02.2009; zetel Vosstraat 323 2100 Antwerpen; 10 VE; RSZ/BTW NACE 88.993",
        ),
        dict(
            source_id="src_werkmmaat_site_contact_2217",
            title="Werkmmaat FOI channel info@werkmmaat.be",
            url="https://www.werkmmaat.be/",
            publisher="Werkmmaat VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2217; info@werkmmaat.be; Vosstraat 323 2100 Antwerpen; maatwerk",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    ("bud_werkmmaat_bruto_jr2025_statutory", "2025", BRUTO, "CW statutory bruto_marge / Gross margin YE2025 (omzet unpublished)", f"tick2217; Medium CW; bruto JUMP +25.81% vs YE2024 {BRUTO_PY}; primary envelope"),
    ("bud_werkmmaat_pnl_jr2025_statutory", "2025", PNL, "CW statutory winst / Profit-Loss after tax YE2025", f"tick2217; Medium CW; pnl JUMP +601.77% vs YE2024 {PNL_PY}"),
    ("bud_werkmmaat_equity_jr2025_statutory", "2025", EQUITY, "CW statutory eigen_vermogen / Equity YE2025", f"tick2217; Medium CW; equity JUMP +46.52% vs YE2024 {EQUITY_PY}"),
    ("bud_werkmmaat_fte_jr2025_statutory", "2025", FTE, f"CW social-balance FTE / Employees {FTE}", f"tick2217; Medium CW; FTE DROP vs YE2024 {FTE_PY}; assets/debt Unknown"),
    ("bud_werkmmaat_bruto_jr2024_statutory_cmp", "2024", BRUTO_PY, "CW statutory bruto_marge YE2024 comparative", f"tick2217; YE2024 bruto {BRUTO_PY} comparative"),
]:
    budgets.append(
        dict(
            budget_id=bid,
            entity_id=ENTITY,
            year=year,
            amount_eur=str(amount),
            amount_min_eur=str(amount),
            amount_max_eur=str(amount),
            basis=basis,
            source_id=SRC_EN,
            confidence="medium",
            notes=notes,
        )
    )
append_csv(ROOT / "budgets.csv", budgets)

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id=COMM,
            title="Werkmmaat Antwerpen YE2025 leftover dual (bruto JUMP 3.24m / empty omzet / pnl JUMP +602% / equity JUMP +47% / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / clients Antwerpen Deurne belt",
            legal_basis="VZW maatwerk (KBO 0817.381.683; Actief; 10 VE; RSZ NACE 88.993)",
            decision_date="2026-06-26",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(BRUTO),
            cash_by_year=json.dumps(
                {
                    "2025_omzet": None,
                    "2025_bruto": BRUTO,
                    "2025_pnl": PNL,
                    "2025_equity": EQUITY,
                    "2025_fte": FTE,
                    "2024_omzet": None,
                    "2024_bruto": BRUTO_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                    "2024_fte": FTE_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0817381683/werkmmaat",
            stated_goal="Sheltered employment maatwerk Antwerpen",
            cut_option="Publish NBB PDF assets/debt FOI; disclose empty omzet vs bruto 3.24m + pnl JUMP +602% with FTE DROP + 10 VE matrix",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>Werkmmaat>JR2025_statutory_L5",
            notes="tick2217; Medium CW; bruto primary (omzet empty); pnl JUMP +602% + equity JUMP +47% + FTE DROP; 10 VE; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn; do not redo Constructief/Groep Maatwerk/OptimaT/Odas/Ecoso/ACG/Werkhuizen Min",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="Werkmmaat bruto JUMP 3.24m / empty omzet / pnl JUMP +602% / equity JUMP +47% (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>Werkmmaat>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes="CW bruto JUMP envelope 3.24m (omzet unpublished) / pnl JUMP 535k +602% from YE2024 76k / equity JUMP 1.67m +47% / FTE DROP 60.1 / 10 VE; Antwerpen maatwerk; assets/debt Unknown",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Antwerpen / public loonkost path",
            stated_goal="Sheltered employment maatwerk",
            measured_outcome="bruto JUMP +25.81%; omzet unpublished; pnl JUMP +601.77%; equity JUMP +46.52%; FTE DROP -3.5%; 10 VE",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; disclose empty omzet vs bruto 3.24m loonkost/GESCO/ESF/VDAB/gemeente split; pnl JUMP +602% with FTE DROP + 10 VE allocation",
            status="open",
            struck_reason="",
            notes=f"tick2217; Medium CW; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; after Constructief",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Werkmmaat VZW (Antwerpen / maatwerk)",
            name_fr="Werkmmaat ASBL (Anvers / entreprise de travail adapté)",
            name_en="Werkmmaat sheltered workshop (Antwerp; maatwerk)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.werkmmaat.be/",
            foi_email="info@werkmmaat.be",
            foi_postal="Vosstraat 323, 2100 Antwerpen",
            notes=f"tick2217 YE2025 Medium CW NL+EN+FR + Strong KBO 0817.381.683 Actief VZW 10 VE RSZ NACE 88.993; bruto JUMP {BRUTO} pnl JUMP {PNL} (+602%) equity JUMP {EQUITY} FTE DROP {FTE} omzet empty; neerlegging 26.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>Werkmmaat>NBB_PDF_assets_debt_empty_omzet_pnl_jump_equity_jump",
            entity_id=ENTITY,
            what_is_missing=f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); why omzet unpublished while bruto EUR{BRUTO} published; pnl JUMP EUR{PNL} vs YE2024 EUR{PNL_PY} (+601.77%) recon with FTE DROP {FTE_PY}->{FTE}; equity JUMP EUR{EQUITY} (+46.52%); 10 VE cost allocation; loonkost/GESCO/ESF/VDAB/gemeente matrix",
            why_it_matters="Medium CW shows Antwerpen maatwerk VZW (bruto 3.24m / 60.1 FTE / 10 VE) with omzet empty, pnl JUMP +602% and equity JUMP +47% while FTE DROP under public subsidy path; assets/debt unpublished",
            priority="8",
            recipient_body="Werkmmaat VZW",
            recipient_email="info@werkmmaat.be",
            recipient_postal="Vosstraat 323, 2100 Antwerpen",
            draft_letter_path=f"docs/doge/foi/drafts/{GAP}.md",
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id=COMM,
            linked_leaderboard_id=LB,
            created_utc=TS,
            updated_utc=TS,
            notes="tick2217; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; AGB Bornem JR2024; next every-10 2220",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Werkmmaat Antwerpen (NBB PDF / empty omzet / pnl JUMP +602% / equity JUMP +47%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Werkmmaat VZW — KBO **0817.381.683** (Actief; Vosstraat 323, 2100 Antwerpen; **10 VE**; FTE {FTE} CW; RSZ NACE **88.993**)  
**recipient:** info@werkmmaat.be · Vosstraat 323, 2100 Antwerpen  
**sources:** [CW EN](https://www.companyweb.be/en/0817381683/werkmmaat) · [CW NL](https://www.companyweb.be/nl/0817381683/werkmmaat) · [CW FR](https://www.companyweb.be/fr/0817381683/werkmmaat) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0817381683) · [werkmmaat.be](https://www.werkmmaat.be/)  
**tick:** 2217  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown; omzet unpublished)

## Context
- KBO Strong: Actief VZW sinds 10.02.2009; **10 VE**; RSZ NACE **88.993**; zetel Vosstraat 323 Antwerpen.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** JUMP +25.81% vs YE2024 EUR{BRUTO_PY:,}; pnl **EUR{PNL:,}** JUMP +601.77% vs YE2024 EUR{PNL_PY:,}; equity **EUR{EQUITY:,}** JUMP +46.52%; FTE **{FTE}** DROP vs {FTE_PY}; filed **26.06.2026**.
- Assets/debt Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Werkmmaat VZW
via info@werkmmaat.be
Vosstraat 323, 2100 Antwerpen
Betreft: Openbaarmaking jaarrekening 2025 Werkmmaat (KBO 0817.381.683)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Waarom omzet (code 70) niet gepubliceerd is terwijl bruto EUR3.236.013 wel openbaar is.
3. PnL JUMP EUR535.180 vs YE2024 EUR76.261 (+602%) recon with FTE DROP 62,3→60,1.
4. Equity JUMP EUR1.670.067 (+46,52%) path.
5. Cost allocation across **10 VE**.

Periode YE2025 (+ YE2024 comparative). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("FOI draft written")

# Determine actual queue head at apply time
with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    open_ids = [r["task_id"] for r in csv.DictReader(f) if r.get("status") == "open" and r["task_id"].startswith("rq_22")]
print("open heads", open_ids[:5])

# Prefer rq_2217; if already done, use first open
target = "rq_2217" if "rq_2217" in open_ids else (open_ids[0] if open_ids else "rq_2217")
# next id
try:
    n = int(target.split("_")[1]) + 1
except Exception:
    n = 2218
next_id = f"rq_{n}"

update_csv_rows(
    ROOT / "research_queue.csv",
    "task_id",
    {
        target: {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": "leftover dual — Werkmmaat YE2025 Medium (bruto JUMP 3.24m / empty omzet / pnl JUMP +602% / equity JUMP +47%)",
            "instructions": "Completed leftover Werkmmaat after Constructief; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent",
            "notes": f"tick2217 Werkmmaat 0817.381.683 Medium; bruto JUMP {BRUTO} omzet empty pnl JUMP {PNL} (+602%) equity JUMP {EQUITY} FTE DROP {FTE}; 10 VE Antwerpen; AGB Bornem JR2024; FARO/REW YE2024; next {next_id}; next every-10 2220",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id=next_id,
            title="leftover dual hole-fill after Werkmmaat — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick after Werkmmaat Antwerpen YE2025 Medium (bruto JUMP 3.24m / empty omzet / pnl JUMP +602% / equity JUMP +47% / 10 VE). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(FREE: Veerkracht 4 / Opnieuw&Co / NBSW if YE2025). "
                "Do NOT redo Werkmmaat, Constructief, Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, "
                "Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, "
                "Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, "
                "Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, "
                "Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, IPFBW, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, "
                "RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2220."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes=f"spawned after tick2217 Werkmmaat; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; next EVERY-10 at 2220",
        )
    ],
)

with (ROOT / "loop_state.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("state_id") == "main":
        row["mode"] = "continuous"
        row["current_sprint"] = "hole_fill"
        row["last_tick_utc"] = TS
        row["last_unit_id"] = target
        row["ticks_completed"] = target.replace("rq_", "")
        row["paused"] = "no"
        row["notes"] = (
            f"tick2217 leftover Werkmmaat 0817.381.683 Medium (bruto JUMP 3.24m; omzet empty; "
            f"pnl JUMP 535k +602%; equity JUMP 1.67m +47%; FTE DROP 60.1; 10 VE Antwerpen); "
            f"AGB Bornem JR2024; FARO/REW YE2024; next {next_id}; next every-10 2220; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state ->", target)

log_block = f"""
## Tick 2217 - {TS} - {target} Werkmmaat Antwerpen (bruto JUMP 3.24m / empty omzet / pnl JUMP +602% / equity JUMP +47% / Medium)

- Unit: **{target}** leftover dual. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; REW still **YE2024**. Took named FREE leftover **Werkmmaat VZW** YE2025 (KBO **0817.381.683**; Vosstraat 323 Antwerpen; **Actief** **10 VE**; RSZ NACE **88.993**). Deferred FREE Veerkracht 4 / Opnieuw&Co. Do not redo Constructief/Groep Maatwerk/OptimaT/Odas/Ecoso/Werkhuizen Min/ACG.
- Found: Companyweb NL+EN+FR YE2025 - omzet **empty/unpublished**; bruto **EUR{BRUTO}** JUMP +25.81% vs YE2024 EUR{BRUTO_PY}; pnl **EUR{PNL}** JUMP +601.77% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** JUMP +46.52%; FTE **{FTE}** DROP vs {FTE_PY}; neerlegging **26.06.2026**. Strong KBO Actief 10 VE. Assets/debt Unknown. Medium. FOI via info@werkmmaat.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {target}=done + {next_id} open; loop_state; raw docs/doge/data/raw/tick2217/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2210**; next **2220**). Next: {next_id}.

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2217 Werkmmaat", target, next_id)
