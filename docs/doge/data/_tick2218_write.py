# -*- coding: utf-8 -*-
"""Tick 2218 leftover dual — Veerkracht 4 Menen YE2025 Medium."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T18:20:00Z"

ENTITY = "vzw_veerkracht4_menen"
BRUTO = 3764584
PNL = 477239
EQUITY = 2883926
FTE = 82.6
BRUTO_PY = 3121096
PNL_PY = 277650
EQUITY_PY = 2401428
FTE_PY = 79.5

SRC_EN = "src_veerkracht4_jr2025_cw_en"
COMM = "comm_veerkracht4_jr2025_statutory_maatwerk_empty_omzet_pnl_jump_72pct_equity_jump"
LB = "lb_veerkracht4_bruto_3_76m_empty_omzet_pnl_jump_72pct_equity_jump_jr2025"
GAP = "gap_veerkracht4_nbb_pdf_assets_debt_empty_omzet_pnl_jump_equity_jump_matrix_l5"

PI = "6.90"
ABS = "7.6"
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
            source_id="src_veerkracht4_jr2025_cw_nl",
            title="Companyweb NL Veerkracht 4 YE2025 statutory",
            url="https://www.companyweb.be/nl/0452454124/veerkracht-4",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2218; YE2025 omzet empty; bruto JUMP {BRUTO} (+20.62%) pnl JUMP {PNL} (+71.89%) equity JUMP {EQUITY} (+20.09%) FTE JUMP {FTE}; neerlegging 23.06.2026; raw docs/doge/data/raw/tick2218/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN Veerkracht 4 YE2025 statutory",
            url="https://www.companyweb.be/en/0452454124/veerkracht-4",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2218; EN mirror YE2025 Medium; filed 23-06-2026; Turnover unpublished; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; Employees {FTE}; raw tick2218/",
        ),
        dict(
            source_id="src_veerkracht4_jr2025_cw_fr",
            title="Companyweb FR Veerkracht 4 YE2025 statutory",
            url="https://www.companyweb.be/fr/0452454124/veerkracht-4",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2218; FR mirror YE2025 Medium; Dernier bilan 2025; CA non publie; Marge brute {BRUTO}; Benefice {PNL}; Capitaux propres {EQUITY}; raw tick2218/",
        ),
        dict(
            source_id="src_veerkracht4_kbo_2218",
            title="KBO Veerkracht 4 0452.454.124 Actief VZW Menen 1 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0452454124",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2218; Actief VZW sinds 28.02.1994; zetel Bruggestraat 465 8930 Menen; 1 VE; RSZ/BTW NACE 88.993",
        ),
        dict(
            source_id="src_veerkracht4_site_contact_2218",
            title="Veerkracht 4 FOI channel info@veerkracht4.be",
            url="https://www.veerkracht4.be/",
            publisher="Veerkracht 4 VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2218; info@veerkracht4.be; Bruggestraat 465 8930 Menen; maatwerk",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    ("bud_veerkracht4_bruto_jr2025_statutory", "2025", BRUTO, "CW statutory bruto_marge / Gross margin YE2025 (omzet unpublished)", f"tick2218; Medium CW; bruto JUMP +20.62% vs YE2024 {BRUTO_PY}; primary envelope"),
    ("bud_veerkracht4_pnl_jr2025_statutory", "2025", PNL, "CW statutory winst / Profit-Loss after tax YE2025", f"tick2218; Medium CW; pnl JUMP +71.89% vs YE2024 {PNL_PY}"),
    ("bud_veerkracht4_equity_jr2025_statutory", "2025", EQUITY, "CW statutory eigen_vermogen / Equity YE2025", f"tick2218; Medium CW; equity JUMP +20.09% vs YE2024 {EQUITY_PY}"),
    ("bud_veerkracht4_fte_jr2025_statutory", "2025", FTE, f"CW social-balance FTE / Employees {FTE}", f"tick2218; Medium CW; FTE JUMP vs YE2024 {FTE_PY}; assets/debt Unknown"),
    ("bud_veerkracht4_bruto_jr2024_statutory_cmp", "2024", BRUTO_PY, "CW statutory bruto_marge YE2024 comparative", f"tick2218; YE2024 bruto {BRUTO_PY} comparative"),
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
            title="Veerkracht 4 Menen YE2025 leftover dual (bruto JUMP 3.76m / empty omzet / pnl JUMP +72% / equity JUMP +20% / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / clients West-Vlaanderen Menen / Stad Menen",
            legal_basis="VZW maatwerk (KBO 0452.454.124; Actief; 1 VE; RSZ NACE 88.993)",
            decision_date="2026-06-23",
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
            evaluation_url="https://www.companyweb.be/en/0452454124/veerkracht-4",
            stated_goal="Sheltered employment maatwerk Menen",
            cut_option="Publish NBB PDF assets/debt FOI; disclose empty omzet vs bruto 3.76m + pnl JUMP +72% + equity JUMP +20%",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>WestVlaanderen>Menen>Veerkracht4>JR2025_statutory_L5",
            notes="tick2218; Medium CW; bruto primary (omzet empty); pnl JUMP +72% + equity JUMP +20% + FTE JUMP; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn; do not redo Werkmmaat/Constructief/Groep Maatwerk/OptimaT/Odas/Ecoso/Forena",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="Veerkracht 4 bruto JUMP 3.76m / empty omzet / pnl JUMP +72% / equity JUMP +20% (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>WestVlaanderen>Menen>Veerkracht4>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes="CW bruto JUMP envelope 3.76m (omzet unpublished) / pnl JUMP 477k +72% from YE2024 278k / equity JUMP 2.88m +20% / FTE JUMP 82.6; Menen maatwerk; assets/debt Unknown",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Menen / public loonkost path / Stad Menen",
            stated_goal="Sheltered employment maatwerk",
            measured_outcome="bruto JUMP +20.62%; omzet unpublished; pnl JUMP +71.89%; equity JUMP +20.09%; FTE JUMP +3.9%",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; disclose empty omzet vs bruto 3.76m loonkost/GESCO/ESF/VDAB/gemeente split; pnl JUMP +72% with equity JUMP path",
            status="open",
            struck_reason="",
            notes=f"tick2218; Medium CW; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; after Werkmmaat",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Veerkracht 4 VZW (Menen / maatwerk)",
            name_fr="Veerkracht 4 ASBL (Menin / entreprise de travail adapté)",
            name_en="Veerkracht 4 sheltered workshop (Menen; maatwerk)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.veerkracht4.be/",
            foi_email="info@veerkracht4.be",
            foi_postal="Bruggestraat 465, 8930 Menen",
            notes=f"tick2218 YE2025 Medium CW NL+EN+FR + Strong KBO 0452.454.124 Actief VZW 1 VE RSZ NACE 88.993; bruto JUMP {BRUTO} pnl JUMP {PNL} (+72%) equity JUMP {EQUITY} FTE JUMP {FTE} omzet empty; neerlegging 23.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>WestVlaanderen>Menen>Veerkracht4>NBB_PDF_assets_debt_empty_omzet_pnl_jump_equity_jump",
            entity_id=ENTITY,
            what_is_missing=f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); why omzet unpublished while bruto EUR{BRUTO} published; pnl JUMP EUR{PNL} vs YE2024 EUR{PNL_PY} (+71.89%); equity JUMP EUR{EQUITY} (+20.09%); FTE JUMP {FTE_PY}->{FTE}; loonkost/GESCO/ESF/VDAB/gemeente/Stad Menen matrix",
            why_it_matters="Medium CW shows Menen maatwerk VZW (bruto 3.76m / 82.6 FTE) with omzet empty, pnl JUMP +72% and equity JUMP +20% under public subsidy path; assets/debt unpublished",
            priority="8",
            recipient_body="Veerkracht 4 VZW",
            recipient_email="info@veerkracht4.be",
            recipient_postal="Bruggestraat 465, 8930 Menen",
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
            notes="tick2218; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; AGB Bornem JR2024; next every-10 2220",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Veerkracht 4 Menen (NBB PDF / empty omzet / pnl JUMP +72% / equity JUMP +20%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Veerkracht 4 VZW — KBO **0452.454.124** (Actief; Bruggestraat 465, 8930 Menen; **1 VE**; FTE {FTE} CW; RSZ NACE **88.993**)  
**recipient:** info@veerkracht4.be · Bruggestraat 465, 8930 Menen  
**sources:** [CW EN](https://www.companyweb.be/en/0452454124/veerkracht-4) · [CW NL](https://www.companyweb.be/nl/0452454124/veerkracht-4) · [CW FR](https://www.companyweb.be/fr/0452454124/veerkracht-4) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0452454124) · [veerkracht4.be](https://www.veerkracht4.be/)  
**tick:** 2218  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown; omzet unpublished)

## Context
- KBO Strong: Actief VZW sinds 28.02.1994; **1 VE**; RSZ NACE **88.993**; zetel Bruggestraat 465 Menen (recent zetel move 09.06.2026).
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** JUMP +20.62% vs YE2024 EUR{BRUTO_PY:,}; pnl **EUR{PNL:,}** JUMP +71.89% vs YE2024 EUR{PNL_PY:,}; equity **EUR{EQUITY:,}** JUMP +20.09%; FTE **{FTE}** JUMP vs {FTE_PY}; filed **23.06.2026**.
- Assets/debt Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Veerkracht 4 VZW
via info@veerkracht4.be
Bruggestraat 465, 8930 Menen
Betreft: Openbaarmaking jaarrekening 2025 Veerkracht 4 (KBO 0452.454.124)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Waarom omzet (code 70) niet gepubliceerd is terwijl bruto EUR3.764.584 wel openbaar is.
3. PnL JUMP EUR477.239 vs YE2024 EUR277.650 (+72%) recon.
4. Equity JUMP EUR2.883.926 (+20%) path.
5. Stad Menen / VDAB / OCMW contract euros + loonkostsubsidie matrix.

Periode YE2025 (+ YE2024 comparative). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("FOI draft written")

with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    open_ids = [
        r["task_id"]
        for r in csv.DictReader(f)
        if r.get("status") == "open" and r["task_id"].startswith("rq_22")
    ]
print("open heads", open_ids[:5])
target = "rq_2218" if "rq_2218" in open_ids else (open_ids[0] if open_ids else "rq_2218")
try:
    n = int(target.split("_")[1]) + 1
except Exception:
    n = 2219
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
            "title": "leftover dual — Veerkracht 4 YE2025 Medium (bruto JUMP 3.76m / empty omzet / pnl JUMP +72% / equity JUMP +20%)",
            "instructions": "Completed leftover Veerkracht 4 after Werkmmaat; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent",
            "notes": f"tick2218 Veerkracht4 0452.454.124 Medium; bruto JUMP {BRUTO} omzet empty pnl JUMP {PNL} (+72%) equity JUMP {EQUITY} FTE JUMP {FTE}; 1 VE Menen; AGB Bornem JR2024; FARO/REW YE2024; next {next_id}; next every-10 2220",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id=next_id,
            title="leftover dual hole-fill after Veerkracht 4 — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick after Veerkracht 4 Menen YE2025 Medium (bruto JUMP 3.76m / empty omzet / pnl JUMP +72% / equity JUMP +20%). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(FREE: Opnieuw&Co / NBSW if YE2025). "
                "Do NOT redo Veerkracht 4, Werkmmaat, Constructief, Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, "
                "Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, "
                "Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, "
                "Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
                "WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, "
                "NLZ, Mobiel, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, "
                "Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2220."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2218 Veerkracht4; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; next EVERY-10 at 2220",
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
            f"tick2218 leftover Veerkracht4 0452.454.124 Medium (bruto JUMP 3.76m; omzet empty; "
            f"pnl JUMP 477k +72%; equity JUMP 2.88m +20%; FTE JUMP 82.6; 1 VE Menen); "
            f"AGB Bornem JR2024; FARO/REW YE2024; next {next_id}; next every-10 2220; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state ->", target)

log_block = f"""
## Tick 2218 - {TS} - {target} Veerkracht 4 Menen (bruto JUMP 3.76m / empty omzet / pnl JUMP +72% / equity JUMP +20% / Medium)

- Unit: **{target}** leftover dual after Werkmmaat. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; REW still **YE2024**. Took named FREE leftover **Veerkracht 4 VZW** YE2025 (KBO **0452.454.124**; Bruggestraat 465 Menen; **Actief** **1 VE**; RSZ NACE **88.993**). Deferred FREE Opnieuw&Co. Do not redo Werkmmaat/Constructief/Groep Maatwerk/OptimaT/Odas/Ecoso/Forena.
- Found: Companyweb NL+EN+FR YE2025 - omzet **empty/unpublished**; bruto **EUR{BRUTO}** JUMP +20.62% vs YE2024 EUR{BRUTO_PY}; pnl **EUR{PNL}** JUMP +71.89% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** JUMP +20.09%; FTE **{FTE}** JUMP vs {FTE_PY}; neerlegging **23.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@veerkracht4.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {target}=done + {next_id} open; loop_state; raw docs/doge/data/raw/tick2218/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2210**; next **2220**). Next: {next_id}.

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("DONE tick2218 Veerkracht4", target, next_id)
