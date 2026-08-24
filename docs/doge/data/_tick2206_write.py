# -*- coding: utf-8 -*-
"""Tick 2206 leftover dual — Entiris YE2025 Medium."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T14:40:00Z"
TICK = 2206

ENTITY = "vzw_entiris_leuven"
OMZET = 18927215
BRUTO = 45242707
PNL = 3265873
EQUITY = 92293922
FTE = 1448.5
OMZET_PY = 17779342
BRUTO_PY = 44769385
PNL_PY = 3397305
EQUITY_PY = 89091378
FTE_PY = 1434.3
# bruto/omzet ~2.3906
RATIO = round(BRUTO / OMZET, 2)

SRC_EN = "src_entiris_jr2025_cw_en"
COMM = "comm_entiris_jr2025_statutory_maatwerk_bruto_gt_omzet_equity_92m_pnl_drop"
LB = "lb_entiris_omzet_18_93m_bruto_gt_omzet_2_39x_equity_92m_pnl_drop_jr2025"
GAP = "gap_entiris_nbb_pdf_assets_debt_bruto_gt_omzet_equity_92m_pnl_drop_matrix_l5"

# cost ~18.9m → 6.2; abs 7.4 (bruto≫omzet ~2.39x + equity 92m + FTE 1448); diff 3.0
# pi = 0.55*6.2 + 0.35*7.4 + 0.10*(10-3) = 3.41 + 2.59 + 0.7 = 6.70
PI = "6.70"
ABS = "7.4"
COST = "6.2"
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


# --- sources ---
append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_entiris_jr2025_cw_nl",
            title="Companyweb NL Entiris YE2025 statutory",
            url="https://www.companyweb.be/nl/0407841151/entiris",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2206; YE2025 omzet JUMP {OMZET} (+6.46%) bruto JUMP {BRUTO} (≫omzet ~{RATIO}x) pnl DROP {PNL} (-3.87%) equity JUMP {EQUITY} (+3.59%) FTE JUMP {FTE}; neerlegging 18.06.2026; raw docs/doge/data/raw/tick2206/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN Entiris YE2025 statutory",
            url="https://www.companyweb.be/en/0407841151/entiris",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2206; EN mirror YE2025 Medium; filed 18-06-2026; Last balance sheet year 2025; Big {FTE} FTE; Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; raw tick2206/",
        ),
        dict(
            source_id="src_entiris_jr2025_cw_fr",
            title="Companyweb FR Entiris YE2025 statutory",
            url="https://www.companyweb.be/fr/0407841151/entiris",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2206; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OMZET}; Marge brute {BRUTO}; Benefice {PNL}; Capitaux propres {EQUITY}; raw tick2206/",
        ),
        dict(
            source_id="src_entiris_kbo_2206",
            title="KBO Entiris 0407.841.151 Actief VZW Leuven 7 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0407841151",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2206; Actief VZW sinds 18.10.1962; zetel Zavelstraat 45 3010 Leuven; 7 VE; RSZ/BTW NACE 88.993 beschutte/sociale werkplaatsen; RSZ-werkgever sinds 01.10.1963; BTW sinds 01.01.1971; 11 bestuurders",
        ),
        dict(
            source_id="src_entiris_site_contact_2206",
            title="Entiris FOI channel info@entiris.be",
            url="https://entiris.be/",
            publisher="Entiris VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2206; info@entiris.be; +32 16 44 14 60; Zavelstraat 45 3010 Leuven (Kessel-Lo); maatwerk / ex-beschutte werkplaats; sites Aarschot e.a.",
        ),
    ],
)

# --- budgets ---
budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_entiris_omzet_jr2025_statutory",
        "2025",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        f"tick2206; Medium CW; omzet JUMP +6.46% vs YE2024 {OMZET_PY}; primary envelope",
    ),
    (
        "bud_entiris_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        f"tick2206; Medium CW; bruto JUMP +1.06% vs YE2024 {BRUTO_PY}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_entiris_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        f"tick2206; Medium CW; pnl DROP -3.87% vs YE2024 {PNL_PY}",
    ),
    (
        "bud_entiris_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        f"tick2206; Medium CW; equity JUMP +3.59% vs YE2024 {EQUITY_PY}",
    ),
    (
        "bud_entiris_fte_jr2025_statutory",
        "2025",
        FTE,
        f"CW social-balance FTE / Employees {FTE}",
        f"tick2206; Medium CW; FTE JUMP vs YE2024 {FTE_PY}; assets/debt Unknown pending NBB PDF",
    ),
    (
        "bud_entiris_omzet_jr2024_statutory_cmp",
        "2024",
        OMZET_PY,
        "CW statutory omzet YE2024 comparative",
        f"tick2206; YE2024 omzet {OMZET_PY} comparative for JUMP calc",
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

# --- commitments ---
append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id=COMM,
            title="Entiris Leuven YE2025 leftover dual (omzet JUMP 18.93m / bruto≫omzet ~2.39x / equity JUMP 92.3m / pnl DROP / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / industrial supply clients Vlaams-Brabant Leuven-Aarschot belt",
            legal_basis="VZW maatwerk (KBO 0407.841.151; Actief; 7 VE; RSZ NACE 88.993)",
            decision_date="2026-06-18",
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
            evaluation_url="https://www.companyweb.be/en/0407841151/entiris",
            stated_goal="Sheltered employment / industrial toelevering maatwerk Vlaams-Brabant",
            cut_option=f"Publish NBB PDF assets/debt FOI; disclose bruto~{RATIO}x omzet loonkost matrix + equity 92.3m path + pnl DROP recon",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Leuven>Entiris>JR2025_statutory_L5",
            notes=f"tick2206; Medium CW; omzet primary envelope; bruto≫omzet (~{RATIO}x) + equity JUMP 92.3m + pnl DROP -3.87% + FTE JUMP 1448.5; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn; do not redo Oesterbank/Werkplus/Trianval/Ijsedal/Kromme Boom/Aarova/Kaliber/MWP/De Winning/AGE",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="Entiris omzet JUMP 18.93m / bruto≫omzet ~2.39x / equity JUMP 92.3m / pnl DROP (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Leuven>Entiris>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=f"CW omzet JUMP envelope 18.93m / bruto 45.24m ≫ omzet (~{RATIO}x) / equity JUMP 92.29m / pnl DROP 3.27m -3.87% from YE2024 3.40m / FTE JUMP 1448.5; large VL maatwerk; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Leuven-Aarschot / public loonkost path",
            stated_goal="Sheltered employment maatwerk",
            measured_outcome="omzet JUMP +6.46%; bruto JUMP +1.06%; pnl DROP -3.87%; equity JUMP +3.59%; FTE JUMP +1.0%",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal=f"Publish NBB PDF assets/debt/cash FOI; disclose bruto~{RATIO}x omzet loonkost/GESCO/ESF/VDAB/gemeente split; equity 92.3m composition + pnl DROP path",
            status="open",
            struck_reason="",
            notes=f"tick2206; Medium CW; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; Vlaams-Brabant maatwerk dual after Oesterbank",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Entiris VZW (Leuven / maatwerk)",
            name_fr="Entiris ASBL (Louvain / entreprise de travail adapté)",
            name_en="Entiris sheltered workshop (Leuven; maatwerk)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://entiris.be/",
            foi_email="info@entiris.be",
            foi_postal="Zavelstraat 45, 3010 Leuven",
            notes=f"tick2206 YE2025 Medium CW NL+EN+FR + Strong KBO 0407.841.151 Actief VZW 7 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~{RATIO}x) pnl DROP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 18.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>VlaamsBrabant>Leuven>Entiris>NBB_PDF_assets_debt_bruto_gt_omzet_equity_92m",
            entity_id=ENTITY,
            what_is_missing=f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix; equity JUMP EUR{EQUITY} composition; pnl DROP EUR{PNL} vs YE2024 EUR{PNL_PY} (-3.87%); FTE JUMP {FTE_PY}->{FTE}; 7 VE + Aarschot/Leuven site cost allocation",
            why_it_matters="Medium CW shows one of the largest VL maatwerk VZWs (omzet 18.93m / bruto 45.24m / equity 92.3m / FTE 1448.5 / 7 VE) with bruto ~2.39x omzet under public subsidy path; assets/debt unpublished",
            priority="8",
            recipient_body="Entiris VZW",
            recipient_email="info@entiris.be",
            recipient_postal="Zavelstraat 45, 3010 Leuven",
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
            notes="tick2206; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; AGB Bornem JR2024; next every-10 2210",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Entiris Leuven (NBB PDF / bruto≫omzet ~{RATIO}x / equity JUMP 92.3m / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Entiris VZW — KBO **0407.841.151** (Actief; Zavelstraat 45, 3010 Leuven; **7 VE**; FTE {FTE} CW; RSZ NACE **88.993**)  
**recipient:** info@entiris.be · Zavelstraat 45, 3010 Leuven · +32 16 44 14 60  
**sources:** [CW EN](https://www.companyweb.be/en/0407841151/entiris) · [CW NL](https://www.companyweb.be/nl/0407841151/entiris) · [CW FR](https://www.companyweb.be/fr/0407841151/entiris) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407841151) · [entiris.be](https://entiris.be/)  
**tick:** 2206  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 18.10.1962; **7 VE**; RSZ NACE **88.993**; zetel Zavelstraat 45 Leuven; sites Aarschot e.a.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +6.46%; bruto **EUR{BRUTO:,}** JUMP +1.06% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP -3.87% vs YE2024 EUR{PNL_PY:,}; equity **EUR{EQUITY:,}** JUMP +3.59%; FTE **{FTE}** JUMP vs {FTE_PY}; filed **18.06.2026**.
- Assets/debt/cash Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Entiris VZW
via info@entiris.be
Zavelstraat 45, 3010 Leuven
Betreft: Openbaarmaking jaarrekening 2025 Entiris (KBO 0407.841.151)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Bruto EUR45.24m ≫ omzet EUR18.93m (~{RATIO}x) — loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix.
3. Equity JUMP EUR92.293.922 composition (reserves / herwaardering / retained earnings).
4. PnL DROP EUR3.265.873 vs YE2024 EUR3.397.305 (-3,87%) recon with omzet JUMP +6,46% and FTE JUMP 1434,3→1448,5.
5. 7 VE + Leuven/Aarschot site cost allocation.

Periode YE2025 (+ YE2024 comparative). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("FOI draft written")

# --- research_queue: close 2206, open 2207 ---
update_csv_rows(
    ROOT / "research_queue.csv",
    "task_id",
    {
        "rq_2206": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": "leftover dual — Entiris YE2025 Medium (omzet JUMP 18.93m / bruto≫omzet ~2.39x / equity JUMP 92.3m / pnl DROP)",
            "instructions": "Completed leftover Entiris after Oesterbank; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent",
            "notes": f"tick2206 Entiris 0407.841.151 Medium; omzet JUMP {OMZET} bruto {BRUTO} (~{RATIO}x) pnl DROP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; 7 VE Leuven; AGB Bornem JR2024; FARO/REW YE2024; Odas YE2024-only deferred; Kemphaan/Arcor/Noordheuvel YE2025 FREE deferred; next rq_2207; next every-10 2210",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2207",
            title="leftover dual hole-fill after Entiris — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2207 after Entiris Leuven YE2025 Medium (omzet JUMP 18.93m / bruto≫omzet ~2.39x / equity JUMP 92.3m / pnl DROP). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(FREE: Kemphaan/Arcor/Noordheuvel/ACG; Odas still YE2024). "
                "Do NOT redo Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, "
                "Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, "
                "Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
                "WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, "
                "IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2210."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2206 Entiris; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; next EVERY-10 at 2210",
        )
    ],
)

# --- loop_state ---
with (ROOT / "loop_state.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("state_id") == "main":
        row["mode"] = "continuous"
        row["current_sprint"] = "hole_fill"
        row["last_tick_utc"] = TS
        row["last_unit_id"] = "rq_2206"
        row["ticks_completed"] = "2206"
        row["paused"] = "no"
        row["notes"] = (
            f"tick2206 leftover Entiris 0407.841.151 Medium (omzet JUMP 18.93m; bruto 45.24m ≫ omzet ~{RATIO}x; "
            f"pnl DROP 3.27m -3.87%; equity JUMP 92.29m; FTE JUMP 1448.5; 7 VE Leuven); "
            "AGB Bornem JR2024; FARO/REW YE2024; next rq_2207; next every-10 2210; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2206")

# --- loop_log ---
log_block = f"""
## Tick 2206 - {TS} - rq_2206 Entiris Leuven (omzet JUMP 18.93m / bruto≫omzet ~{RATIO}x / equity JUMP 92.3m / pnl DROP / Medium)

- Unit: **rq_2206** leftover dual after **rq_2205 Oesterbank**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW fetch aborted/prior YE2024); REW still **YE2024**. Took named FREE leftover **Entiris VZW** YE2025 (KBO **0407.841.151**; Zavelstraat 45 Leuven; **Actief** **7 VE**; RSZ NACE **88.993**). Deferred FREE Kemphaan/Arcor/Noordheuvel YE2025; Odas still YE2024-only. Do not redo Oesterbank/Werkplus/Trianval/Ijsedal/De Kromme Boom/Aarova/Kaliber/MWP Pajottenland/De Winning/Atelier Groot Eiland/Groep Talent/BosKat/De Schakel/BWZ/Bewel/Forena/Kunnig/A-kwadraat/SW-WEB/Mivas/Demival/De Wroeter/Kringwinkel/Blankedale/Mirto/Mariasteen/De Brug/Weerwerk/InterWest/Westlandia/BWB/Wase/Groep INTRO/MAAAT/WAAK SW/Waak/Stijn/Stroom/Springplank.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +6.46% vs YE2024 EUR{OMZET_PY}; bruto **EUR{BRUTO}** JUMP +1.06% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL}** DROP -3.87% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** JUMP +3.59%; FTE **{FTE}** JUMP vs {FTE_PY}; neerlegging **18.06.2026**. Strong KBO Actief 7 VE. Assets/debt Unknown. Medium. FOI via info@entiris.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2206=done + rq_2207 open; loop_state ticks=2206; raw docs/doge/data/raw/tick2206/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2200**; next **2210**). Next: rq_2207 (AGB/FARO-if-YE2025 / AIESH-REW / Kemphaan-Arcor-Noordheuvel-or-unused).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2206 Entiris")
