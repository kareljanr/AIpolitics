# -*- coding: utf-8 -*-
"""Tick 2208 leftover dual — Arcor Ronse YE2025 Medium."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T15:20:00Z"
TICK = 2208

ENTITY = "vzw_arcor_ronse"
# omzet unpublished YE2025+YE2024; bruto primary envelope
OMZET = ""
BRUTO = 4056616
PNL = 44477
EQUITY = 3633846
FTE = 116.3
BRUTO_PY = 3811915
PNL_PY = 25386
EQUITY_PY = 3703624
FTE_PY = 119.6
OMZET_PY3 = 1389400  # YE2023 last published omzet (not YE2024)

SRC_EN = "src_arcor_jr2025_cw_en"
COMM = "comm_arcor_jr2025_statutory_maatwerk_empty_omzet_bruto_pnl_jump_equity_drop"
LB = "lb_arcor_bruto_4_06m_empty_omzet_pnl_jump_75pct_equity_drop_jr2025"
GAP = "gap_arcor_nbb_pdf_assets_debt_empty_omzet_bruto_pnl_jump_equity_drop_matrix_l5"

# ~4.06m bruto → cost 4.8; abs 7.7 (empty omzet + pnl JUMP +75% + equity DROP + FTE DROP); diff 3.0
# peer-aligned (AGE/Werkplus empty-omzet band) → 6.90
PI = "6.90"
ABS = "7.7"
COST = "4.8"
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
    return len(existing)


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
            source_id="src_arcor_jr2025_cw_nl",
            title="Companyweb NL Arcor YE2025 statutory",
            url="https://www.companyweb.be/nl/0410962274/arcor",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2208; YE2025 omzet empty; bruto JUMP {BRUTO} (+6.42%) pnl JUMP {PNL} (+75.2%) equity DROP {EQUITY} (-1.88%) FTE DROP {FTE}; neerlegging 20.05.2026; raw docs/doge/data/raw/tick2208/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN Arcor YE2025 statutory",
            url="https://www.companyweb.be/en/0410962274/arcor",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2208; EN mirror YE2025 Medium; filed 20-05-2026; Last balance sheet year 2025; Big {FTE} FTE; Turnover unpublished; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; raw tick2208/",
        ),
        dict(
            source_id="src_arcor_jr2025_cw_fr",
            title="Companyweb FR Arcor YE2025 statutory",
            url="https://www.companyweb.be/fr/0410962274/arcor",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2208; FR mirror YE2025 Medium; Dernier bilan 2025; CA non publie; Marge brute {BRUTO}; Benefice {PNL}; Capitaux propres {EQUITY}; raw tick2208/",
        ),
        dict(
            source_id="src_arcor_kbo_2208",
            title="KBO Arcor 0410.962.274 Actief VZW Ronse 1 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0410962274",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2208; Actief VZW sinds 08.11.1966; zetel Ninovestraat 106 9600 Ronse; 1 VE; RSZ/BTW NACE 88.993; info@arcor.be; tel 055/21.45.33; www.arcor.be",
        ),
        dict(
            source_id="src_arcor_site_contact_2208",
            title="Arcor FOI channel info@arcor.be",
            url="https://www.arcor.be/",
            publisher="Arcor VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2208; info@arcor.be; +32 55 21 45 33; Ninovestraat 106 9600 Ronse; maatwerk packaging/textile/montage",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_arcor_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025 (omzet unpublished)",
        f"tick2208; Medium CW; bruto JUMP +6.42% vs YE2024 {BRUTO_PY}; primary envelope (omzet empty YE2025+YE2024)",
    ),
    (
        "bud_arcor_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        f"tick2208; Medium CW; pnl JUMP +75.2% vs YE2024 {PNL_PY}",
    ),
    (
        "bud_arcor_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        f"tick2208; Medium CW; equity DROP -1.88% vs YE2024 {EQUITY_PY}",
    ),
    (
        "bud_arcor_fte_jr2025_statutory",
        "2025",
        FTE,
        f"CW social-balance FTE / Employees {FTE}",
        f"tick2208; Medium CW; FTE DROP vs YE2024 {FTE_PY}; assets/debt Unknown pending NBB PDF",
    ),
    (
        "bud_arcor_bruto_jr2024_statutory_cmp",
        "2024",
        BRUTO_PY,
        "CW statutory bruto_marge YE2024 comparative",
        f"tick2208; YE2024 bruto {BRUTO_PY} comparative for JUMP calc; omzet also unpublished YE2024",
    ),
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
            title="Arcor Ronse YE2025 leftover dual (bruto JUMP 4.06m / empty omzet / pnl JUMP +75% / equity DROP / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / packaging+textile+montage clients Oost-Vlaanderen Ronse belt",
            legal_basis="VZW maatwerk (KBO 0410.962.274; Actief; 1 VE; RSZ NACE 88.993)",
            decision_date="2026-05-20",
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
                    "2023_omzet": OMZET_PY3,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0410962274/arcor",
            stated_goal="Sheltered employment / packaging+textile+montage maatwerk Ronse",
            cut_option="Publish NBB PDF assets/debt FOI; disclose empty omzet vs bruto 4.06m loonkost matrix + pnl JUMP +75% with equity DROP / FTE DROP",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>OostVlaanderen>Ronse>Arcor>JR2025_statutory_L5",
            notes="tick2208; Medium CW; bruto primary envelope (omzet unpublished YE2025+YE2024); pnl JUMP +75.2% + equity DROP -1.88% + FTE DROP; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn; do not redo Kemphaan/Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/Kromme Boom/Aarova/Kaliber/MWP/De Winning/AGE",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="Arcor bruto JUMP 4.06m / empty omzet / pnl JUMP +75% / equity DROP (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>OostVlaanderen>Ronse>Arcor>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes="CW bruto JUMP envelope 4.06m (omzet unpublished YE2025+YE2024) / pnl JUMP 44k +75% from YE2024 25k / equity DROP 3.63m -1.88% / FTE DROP 116.3; Ronse maatwerk; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Ronse / public loonkost path",
            stated_goal="Sheltered employment maatwerk packaging+textile+montage",
            measured_outcome="bruto JUMP +6.42%; omzet unpublished; pnl JUMP +75.2%; equity DROP -1.88%; FTE DROP -2.8%",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; disclose empty omzet vs bruto 4.06m loonkost/GESCO/ESF/VDAB/gemeente split; pnl JUMP with equity DROP / FTE DROP path",
            status="open",
            struck_reason="",
            notes=f"tick2208; Medium CW; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; Oost-Vlaanderen maatwerk dual after Kemphaan",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Arcor VZW (Ronse / maatwerk)",
            name_fr="Arcor ASBL (Renaix / entreprise de travail adapté)",
            name_en="Arcor sheltered workshop (Ronse; maatwerk)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.arcor.be/",
            foi_email="info@arcor.be",
            foi_postal="Ninovestraat 106, 9600 Ronse",
            notes=f"tick2208 YE2025 Medium CW NL+EN+FR + Strong KBO 0410.962.274 Actief VZW 1 VE RSZ NACE 88.993; bruto JUMP {BRUTO} pnl JUMP {PNL} equity DROP {EQUITY} FTE DROP {FTE} omzet empty; neerlegging 20.05.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>OostVlaanderen>Ronse>Arcor>NBB_PDF_assets_debt_empty_omzet_bruto_pnl_jump_equity_drop",
            entity_id=ENTITY,
            what_is_missing=f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); why omzet (code70) unpublished YE2025+YE2024 while bruto EUR{BRUTO} published; loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix; pnl JUMP EUR{PNL} vs YE2024 EUR{PNL_PY} (+75.2%); equity DROP EUR{EQUITY} (-1.88%); FTE DROP {FTE_PY}->{FTE}; 1 VE cost allocation",
            why_it_matters="Medium CW shows Ronse maatwerk VZW (bruto 4.06m / 116.3 FTE / 1 VE) with omzet empty two consecutive years, pnl JUMP +75% and equity DROP under public subsidy path; assets/debt unpublished",
            priority="8",
            recipient_body="Arcor VZW",
            recipient_email="info@arcor.be",
            recipient_postal="Ninovestraat 106, 9600 Ronse",
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
            notes="tick2208; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; AGB Bornem JR2024; next every-10 2210",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Arcor Ronse (NBB PDF / empty omzet / bruto JUMP 4.06m / pnl JUMP +75% / equity DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Arcor VZW — KBO **0410.962.274** (Actief; Ninovestraat 106, 9600 Ronse; **1 VE**; FTE {FTE} CW; RSZ NACE **88.993**)  
**recipient:** info@arcor.be · Ninovestraat 106, 9600 Ronse · +32 55 21 45 33  
**sources:** [CW EN](https://www.companyweb.be/en/0410962274/arcor) · [CW NL](https://www.companyweb.be/nl/0410962274/arcor) · [CW FR](https://www.companyweb.be/fr/0410962274/arcor) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410962274) · [arcor.be](https://www.arcor.be/)  
**tick:** 2208  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown; omzet unpublished)

## Context
- KBO Strong: Actief VZW sinds 08.11.1966; **1 VE**; RSZ NACE **88.993**; zetel Ninovestraat 106 Ronse; info@arcor.be in KBO.
- CW YE2025: omzet **unpublished** (also YE2024); bruto **EUR{BRUTO:,}** JUMP +6.42% vs YE2024 EUR{BRUTO_PY:,}; pnl **EUR{PNL:,}** JUMP +75.2% vs YE2024 EUR{PNL_PY:,}; equity **EUR{EQUITY:,}** DROP -1.88%; FTE **{FTE}** DROP vs {FTE_PY}; filed **20.05.2026**. Last published omzet YE2023 EUR{OMZET_PY3:,}.
- Assets/debt/cash Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Arcor VZW
via info@arcor.be
Ninovestraat 106, 9600 Ronse
Betreft: Openbaarmaking jaarrekening 2025 Arcor (KBO 0410.962.274)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Waarom omzet (code 70) niet gepubliceerd is voor YE2025 én YE2024 terwijl bruto EUR4.056.616 wel openbaar is.
3. Loonkostsubsidie/GESCO/ESF/VDAB/gemeente-toelage matrix achter bruto EUR4.06m.
4. PnL JUMP EUR44.477 (+75,2%) vs equity DROP EUR3.633.846 (-1,88%) en FTE DROP 119,6→116,3 reconciliatie.
5. 1 VE cost allocation (Ninovestraat Ronse).

Periode YE2025 (+ YE2024 comparative). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("FOI draft written")

update_csv_rows(
    ROOT / "research_queue.csv",
    "task_id",
    {
        "rq_2208": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": "leftover dual — Arcor YE2025 Medium (bruto JUMP 4.06m / empty omzet / pnl JUMP +75% / equity DROP)",
            "instructions": "Completed leftover Arcor after Kemphaan; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent",
            "notes": f"tick2208 Arcor 0410.962.274 Medium; bruto JUMP {BRUTO} omzet empty pnl JUMP {PNL} equity DROP {EQUITY} FTE DROP {FTE}; 1 VE Ronse; AGB Bornem JR2024; FARO/REW YE2024; Noordheuvel YE2025 FREE deferred; next rq_2209; next every-10 2210",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2209",
            title="leftover dual hole-fill after Arcor — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2209 after Arcor Ronse YE2025 Medium (bruto JUMP 4.06m / empty omzet / pnl JUMP +75% / equity DROP). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(FREE: Noordheuvel YE2025 / ACG; Odas still YE2024). "
                "Do NOT redo Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, "
                "Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, "
                "Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
                "WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, "
                "IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2210."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2208 Arcor; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; next EVERY-10 at 2210",
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
        row["last_unit_id"] = "rq_2208"
        row["ticks_completed"] = "2208"
        row["paused"] = "no"
        row["notes"] = (
            "tick2208 leftover Arcor 0410.962.274 Medium (bruto JUMP 4.06m; omzet empty YE2025+YE2024; "
            "pnl JUMP 44k +75%; equity DROP 3.63m; FTE DROP 116.3; 1 VE Ronse); "
            "AGB Bornem JR2024; FARO/REW YE2024; next rq_2209; next every-10 2210; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2208")

log_block = f"""
## Tick 2208 - {TS} - rq_2208 Arcor Ronse (bruto JUMP 4.06m / empty omzet / pnl JUMP +75% / equity DROP / Medium)

- Unit: **rq_2208** leftover dual after **rq_2207 Kemphaan**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; REW still **YE2024**. Took named FREE leftover **Arcor VZW** YE2025 (KBO **0410.962.274**; Ninovestraat 106 Ronse; **Actief** **1 VE**; RSZ NACE **88.993**). Deferred FREE Noordheuvel YE2025; Odas still YE2024-only. Do not redo Kemphaan/Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/De Kromme Boom/Aarova/Kaliber/MWP Pajottenland/De Winning/Atelier Groot Eiland/Groep Talent/BosKat/De Schakel/BWZ/Bewel/Forena/Kunnig/A-kwadraat/SW-WEB/Mivas/Demival/De Wroeter/Kringwinkel/Blankedale/Mirto/Mariasteen/De Brug/Weerwerk/InterWest/Westlandia/BWB/Wase/Groep INTRO/MAAAT/WAAK SW/Waak/Stijn/Stroom/Springplank.
- Found: Companyweb NL+EN+FR YE2025 - omzet **empty/unpublished** (also YE2024); bruto **EUR{BRUTO}** JUMP +6.42% vs YE2024 EUR{BRUTO_PY}; pnl **EUR{PNL}** JUMP +75.2% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** DROP -1.88%; FTE **{FTE}** DROP vs {FTE_PY}; neerlegging **20.05.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@arcor.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2208=done + rq_2209 open; loop_state ticks=2208; raw docs/doge/data/raw/tick2208/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2200**; next **2210**). Next: rq_2209 (AGB/FARO-if-YE2025 / AIESH-REW / Noordheuvel-or-unused).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2208 Arcor")
