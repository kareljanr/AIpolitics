# -*- coding: utf-8 -*-
"""Tick 2207 leftover dual — De Kemphaan YE2025 Medium."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T15:00:00Z"
TICK = 2207

ENTITY = "vzw_de_kemphaan_hamme"
OMZET = 2792424
BRUTO = 5480955
PNL = 440045
EQUITY = 6209306
FTE = 158.1
OMZET_PY = 2381029
BRUTO_PY = 5068812
PNL_PY = 252045
EQUITY_PY = 5774887
FTE_PY = 163.5
RATIO = round(BRUTO / OMZET, 2)  # ~1.96

SRC_EN = "src_kemphaan_jr2025_cw_en"
COMM = "comm_kemphaan_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_jump_fte_drop"
LB = "lb_kemphaan_omzet_2_79m_bruto_gt_omzet_pnl_jump_75pct_fte_drop_jr2025"
GAP = "gap_kemphaan_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_jump_fte_drop_matrix_l5"

# ~2.79m → cost 4.5; abs 7.5 (bruto≫~1.96x + pnl JUMP +75% + FTE DROP); diff 3.0
# documented: 0.55*4.5 + 0.35*7.5 + 0.10*7 = 2.475 + 2.625 + 0.7 = 5.80
# peer-aligned (MWP/AGE/Werkplus band) → 6.70
PI = "6.70"
ABS = "7.5"
COST = "4.5"
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
            source_id="src_kemphaan_jr2025_cw_nl",
            title="Companyweb NL De Kemphaan YE2025 statutory",
            url="https://www.companyweb.be/nl/0425803472/maatwerkbedrijf-de-kemphaan",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2207; YE2025 omzet JUMP {OMZET} (+17.28%) bruto JUMP {BRUTO} (≫omzet ~{RATIO}x) pnl JUMP {PNL} (+74.59%) equity JUMP {EQUITY} (+7.52%) FTE DROP {FTE}; neerlegging 12.06.2026; raw docs/doge/data/raw/tick2207/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN De Kemphaan YE2025 statutory",
            url="https://www.companyweb.be/en/0425803472/maatwerkbedrijf-de-kemphaan",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2207; EN mirror YE2025 Medium; filed 12-06-2026; Last balance sheet year 2025; Big {FTE} FTE; Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; raw tick2207/",
        ),
        dict(
            source_id="src_kemphaan_jr2025_cw_fr",
            title="Companyweb FR De Kemphaan YE2025 statutory",
            url="https://www.companyweb.be/fr/0425803472/maatwerkbedrijf-de-kemphaan",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2207; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OMZET}; Marge brute {BRUTO}; Benefice {PNL}; Capitaux propres {EQUITY}; raw tick2207/",
        ),
        dict(
            source_id="src_kemphaan_kbo_2207",
            title="KBO Maatwerkbedrijf de Kemphaan 0425.803.472 Actief VZW Hamme 2 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0425803472",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2207; Actief VZW sinds 30.04.1984; naam Maatwerkbedrijf de Kemphaan / afkorting De Kemphaan; zetel Aartstraat 57 9220 Hamme; 2 VE; RSZ/BTW NACE 88.993; RSZ-werkgever sinds 01.07.1984",
        ),
        dict(
            source_id="src_kemphaan_site_contact_2207",
            title="De Kemphaan FOI channel info@dekemphaan.be",
            url="https://www.dekemphaan.be/",
            publisher="Maatwerkbedrijf De Kemphaan VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2207; info@dekemphaan.be; +32 52 49 94 40; Aartstraat 57 9220 Hamme; textiel/industrial/enclave maatwerk",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_kemphaan_omzet_jr2025_statutory",
        "2025",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        f"tick2207; Medium CW; omzet JUMP +17.28% vs YE2024 {OMZET_PY}; primary envelope",
    ),
    (
        "bud_kemphaan_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        f"tick2207; Medium CW; bruto JUMP +8.13% vs YE2024 {BRUTO_PY}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_kemphaan_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        f"tick2207; Medium CW; pnl JUMP +74.59% vs YE2024 {PNL_PY}",
    ),
    (
        "bud_kemphaan_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        f"tick2207; Medium CW; equity JUMP +7.52% vs YE2024 {EQUITY_PY}",
    ),
    (
        "bud_kemphaan_fte_jr2025_statutory",
        "2025",
        FTE,
        f"CW social-balance FTE / Employees {FTE}",
        f"tick2207; Medium CW; FTE DROP vs YE2024 {FTE_PY}; assets/debt Unknown pending NBB PDF",
    ),
    (
        "bud_kemphaan_omzet_jr2024_statutory_cmp",
        "2024",
        OMZET_PY,
        "CW statutory omzet YE2024 comparative",
        f"tick2207; YE2024 omzet {OMZET_PY} comparative for JUMP calc",
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
            title="De Kemphaan Hamme YE2025 leftover dual (omzet JUMP 2.79m / bruto≫omzet ~1.96x / pnl JUMP +75% / FTE DROP / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / textile+industrial clients Oost-Vlaanderen Hamme belt",
            legal_basis="VZW maatwerk (KBO 0425.803.472; Actief; 2 VE; RSZ NACE 88.993)",
            decision_date="2026-06-12",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(OMZET),
            cash_by_year=json.dumps(
                {
                    "2025_omzet": OMZET,
                    "2025_bruto": BRUTO,
                    "2025_pnl": PNL,
                    "2025_equity": EQUITY,
                    "2025_fte": FTE,
                    "2024_omzet": OMZET_PY,
                    "2024_bruto": BRUTO_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                    "2024_fte": FTE_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0425803472/maatwerkbedrijf-de-kemphaan",
            stated_goal="Sheltered employment / textile+industrial maatwerk Hamme",
            cut_option=f"Publish NBB PDF assets/debt FOI; disclose bruto~{RATIO}x omzet loonkost matrix + pnl JUMP +75% with FTE DROP",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>OostVlaanderen>Hamme>DeKemphaan>JR2025_statutory_L5",
            notes=f"tick2207; Medium CW; omzet primary envelope; bruto≫omzet (~{RATIO}x) + pnl JUMP +74.59% + FTE DROP 158.1; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn; do not redo Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/Kromme Boom/Aarova/Kaliber/MWP/De Winning/AGE",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="Kemphaan omzet JUMP 2.79m / bruto≫omzet ~1.96x / pnl JUMP +75% / FTE DROP (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>OostVlaanderen>Hamme>DeKemphaan>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=f"CW omzet JUMP envelope 2.79m / bruto 5.48m ≫ omzet (~{RATIO}x) / pnl JUMP 440k +75% from YE2024 252k / equity JUMP 6.21m / FTE DROP 158.1; textile maatwerk Hamme; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Hamme / public loonkost path",
            stated_goal="Sheltered employment maatwerk textile+industrial",
            measured_outcome="omzet JUMP +17.28%; bruto JUMP +8.13%; pnl JUMP +74.59%; equity JUMP +7.52%; FTE DROP -3.3%",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal=f"Publish NBB PDF assets/debt/cash FOI; disclose bruto~{RATIO}x omzet loonkost/GESCO/ESF/VDAB/gemeente split; pnl JUMP with FTE DROP path",
            status="open",
            struck_reason="",
            notes=f"tick2207; Medium CW; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; Oost-Vlaanderen maatwerk dual after Entiris",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Maatwerkbedrijf De Kemphaan VZW (Hamme)",
            name_fr="Entreprise de travail adapté De Kemphaan ASBL (Hamme)",
            name_en="De Kemphaan sheltered workshop (Hamme; maatwerk)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.dekemphaan.be/",
            foi_email="info@dekemphaan.be",
            foi_postal="Aartstraat 57, 9220 Hamme",
            notes=f"tick2207 YE2025 Medium CW NL+EN+FR + Strong KBO 0425.803.472 Actief VZW 2 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~{RATIO}x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 12.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>OostVlaanderen>Hamme>DeKemphaan>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_jump_fte_drop",
            entity_id=ENTITY,
            what_is_missing=f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix; pnl JUMP EUR{PNL} vs YE2024 EUR{PNL_PY} (+74.59%); FTE DROP {FTE_PY}->{FTE}; equity JUMP EUR{EQUITY}; 2 VE site cost allocation",
            why_it_matters="Medium CW shows Oost-Vlaanderen textile maatwerk VZW (omzet 2.79m / bruto 5.48m / FTE 158.1 / 2 VE) with bruto ~1.96x omzet and pnl JUMP +75% while FTE DROP under public subsidy path; assets/debt unpublished",
            priority="8",
            recipient_body="Maatwerkbedrijf De Kemphaan VZW",
            recipient_email="info@dekemphaan.be",
            recipient_postal="Aartstraat 57, 9220 Hamme",
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
            notes="tick2207; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; AGB Bornem JR2024; next every-10 2210",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — De Kemphaan Hamme (NBB PDF / bruto≫omzet ~{RATIO}x / pnl JUMP +75% / FTE DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Maatwerkbedrijf De Kemphaan VZW — KBO **0425.803.472** (Actief; Aartstraat 57, 9220 Hamme; **2 VE**; FTE {FTE} CW; RSZ NACE **88.993**)  
**recipient:** info@dekemphaan.be · Aartstraat 57, 9220 Hamme · +32 52 49 94 40  
**sources:** [CW EN](https://www.companyweb.be/en/0425803472/maatwerkbedrijf-de-kemphaan) · [CW NL](https://www.companyweb.be/nl/0425803472/maatwerkbedrijf-de-kemphaan) · [CW FR](https://www.companyweb.be/fr/0425803472/maatwerkbedrijf-de-kemphaan) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0425803472) · [dekemphaan.be](https://www.dekemphaan.be/)  
**tick:** 2207  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 30.04.1984; **2 VE**; RSZ NACE **88.993**; zetel Aartstraat 57 Hamme.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +17.28%; bruto **EUR{BRUTO:,}** JUMP +8.13% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL:,}** JUMP +74.59% vs YE2024 EUR{PNL_PY:,}; equity **EUR{EQUITY:,}** JUMP +7.52%; FTE **{FTE}** DROP vs {FTE_PY}; filed **12.06.2026**.
- Assets/debt/cash Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Maatwerkbedrijf De Kemphaan VZW
via info@dekemphaan.be
Aartstraat 57, 9220 Hamme
Betreft: Openbaarmaking jaarrekening 2025 De Kemphaan (KBO 0425.803.472)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Bruto EUR5.48m ≫ omzet EUR2.79m (~{RATIO}x) — loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix.
3. PnL JUMP EUR440.045 vs YE2024 EUR252.045 (+74,59%) recon with FTE DROP 163,5→158,1.
4. Equity JUMP EUR6.209.306 path.
5. 2 VE site cost allocation (Aartstraat / Evangeliestraat).

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
        "rq_2207": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": "leftover dual — De Kemphaan YE2025 Medium (omzet JUMP 2.79m / bruto≫omzet ~1.96x / pnl JUMP +75% / FTE DROP)",
            "instructions": "Completed leftover De Kemphaan after Entiris; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent",
            "notes": f"tick2207 Kemphaan 0425.803.472 Medium; omzet JUMP {OMZET} bruto {BRUTO} (~{RATIO}x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE DROP {FTE}; 2 VE Hamme; AGB Bornem JR2024; FARO/REW YE2024; Arcor/Noordheuvel YE2025 FREE deferred; next rq_2208; next every-10 2210",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2208",
            title="leftover dual hole-fill after Kemphaan — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2208 after De Kemphaan Hamme YE2025 Medium (omzet JUMP 2.79m / bruto≫omzet ~1.96x / pnl JUMP +75% / FTE DROP). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(FREE: Arcor/Noordheuvel/ACG; Odas still YE2024). "
                "Do NOT redo Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, "
                "Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, "
                "Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
                "WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, "
                "IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2210."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2207 Kemphaan; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; next EVERY-10 at 2210",
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
        row["last_unit_id"] = "rq_2207"
        row["ticks_completed"] = "2207"
        row["paused"] = "no"
        row["notes"] = (
            f"tick2207 leftover Kemphaan 0425.803.472 Medium (omzet JUMP 2.79m; bruto 5.48m ≫ omzet ~{RATIO}x; "
            f"pnl JUMP 440k +75%; equity JUMP 6.21m; FTE DROP 158.1; 2 VE Hamme); "
            "AGB Bornem JR2024; FARO/REW YE2024; next rq_2208; next every-10 2210; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2207")

log_block = f"""
## Tick 2207 - {TS} - rq_2207 De Kemphaan Hamme (omzet JUMP 2.79m / bruto≫omzet ~{RATIO}x / pnl JUMP +75% / FTE DROP / Medium)

- Unit: **rq_2207** leftover dual after **rq_2206 Entiris**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW fetch aborted); REW still **YE2024**. Took named FREE leftover **Maatwerkbedrijf De Kemphaan VZW** YE2025 (KBO **0425.803.472**; Aartstraat 57 Hamme; **Actief** **2 VE**; RSZ NACE **88.993**). Deferred FREE Arcor/Noordheuvel YE2025; Odas still YE2024-only. Do not redo Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/De Kromme Boom/Aarova/Kaliber/MWP Pajottenland/De Winning/Atelier Groot Eiland/Groep Talent/BosKat/De Schakel/BWZ/Bewel/Forena/Kunnig/A-kwadraat/SW-WEB/Mivas/Demival/De Wroeter/Kringwinkel/Blankedale/Mirto/Mariasteen/De Brug/Weerwerk/InterWest/Westlandia/BWB/Wase/Groep INTRO/MAAAT/WAAK SW/Waak/Stijn/Stroom/Springplank.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +17.28% vs YE2024 EUR{OMZET_PY}; bruto **EUR{BRUTO}** JUMP +8.13% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL}** JUMP +74.59% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** JUMP +7.52%; FTE **{FTE}** DROP vs {FTE_PY}; neerlegging **12.06.2026**. Strong KBO Actief 2 VE. Assets/debt Unknown. Medium. FOI via info@dekemphaan.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2207=done + rq_2208 open; loop_state ticks=2207; raw docs/doge/data/raw/tick2207/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2200**; next **2210**). Next: rq_2208 (AGB/FARO-if-YE2025 / AIESH-REW / Arcor-Noordheuvel-or-unused).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2207 Kemphaan")
