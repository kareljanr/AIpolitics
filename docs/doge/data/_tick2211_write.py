# -*- coding: utf-8 -*-
"""Tick 2211 leftover dual — Werkhuizen MIN YE2025 Medium (empty omzet / bruto DROP 3.06m / pnl LOSS FLIP)."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T16:20:00Z"
TICK = 2211

ENTITY = "vzw_werkhuizen_min_antwerpen"
BRUTO = 3055393
PNL = -246925
EQUITY = 565216
FTE = 94.3
BRUTO_PY = 3181259
PNL_PY = 92446
EQUITY_PY = 819433
FTE_PY = 93.8

SRC_EN = "src_werkhuizen_min_jr2025_cw_en"
COMM = "comm_werkhuizen_min_jr2025_statutory_maatwerk_empty_omzet_bruto_drop_pnl_loss_flip"
LB = "lb_werkhuizen_min_bruto_3_06m_empty_omzet_pnl_loss_flip_jr2025"
GAP = "gap_werkhuizen_min_nbb_pdf_assets_debt_empty_omzet_bruto_drop_pnl_loss_flip_matrix_l5"

# ~3.06m → cost 4.6; abs 7.9 (empty omzet + LOSS FLIP -367% + equity DROP -31%); diff 3.0 → pi 7.00
PI = "7.00"
ABS = "7.9"
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
            source_id="src_werkhuizen_min_jr2025_cw_nl",
            title="Companyweb NL Werkhuizen MIN YE2025 statutory",
            url="https://www.companyweb.be/nl/0407699908/werkhuizen-min",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2211; YE2025 empty omzet; bruto DROP {BRUTO} (-3.96%) pnl LOSS FLIP {PNL} (-367.1%) equity DROP {EQUITY} (-31.02%) FTE JUMP {FTE}; neerlegging 15.07.2026; raw docs/doge/data/raw/tick2211/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN Werkhuizen MIN YE2025 statutory",
            url="https://www.companyweb.be/en/0407699908/werkhuizen-min",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2211; EN mirror YE2025 Medium; filed 15-07-2026; Last balance sheet year 2025; Big {FTE} FTE; Turnover unpublished; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; raw tick2211/",
        ),
        dict(
            source_id="src_werkhuizen_min_jr2025_cw_fr",
            title="Companyweb FR Werkhuizen MIN YE2025 statutory",
            url="https://www.companyweb.be/fr/0407699908/werkhuizen-min",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2211; FR mirror YE2025 Medium; Dernier bilan 2025; CA unpublished; Marge brute {BRUTO}; Perte {PNL}; Capitaux propres {EQUITY}; raw tick2211/",
        ),
        dict(
            source_id="src_werkhuizen_min_kbo_2211",
            title="KBO Werkhuizen MIN 0407.699.908 Actief VZW Antwerpen Deurne 1 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0407699908",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2211; Actief VZW sinds 09.11.1970; naam WERKHUIZEN MIN; zetel Van Cortbeemdelei 382 2100 Antwerpen; 1 VE; RSZ NACE 88.993; BTW NACE 88.999",
        ),
        dict(
            source_id="src_werkhuizen_min_site_contact_2211",
            title="Werkhuizen MIN FOI channel info@whmin.be",
            url="https://www.whmin.be/",
            publisher="Werkhuizen MIN VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2211; info@whmin.be; +32 3 270 75 00; Van Cortbeemdelei 382 2100 Deurne; leveradres Merksemsesteenweg 177",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_werkhuizen_min_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025 (omzet unpublished)",
        f"tick2211; Medium CW; bruto DROP -3.96% vs YE2024 {BRUTO_PY}; primary envelope (empty omzet)",
    ),
    (
        "bud_werkhuizen_min_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        f"tick2211; Medium CW; pnl LOSS FLIP -367.1% vs YE2024 profit {PNL_PY}",
    ),
    (
        "bud_werkhuizen_min_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        f"tick2211; Medium CW; equity DROP -31.02% vs YE2024 {EQUITY_PY}",
    ),
    (
        "bud_werkhuizen_min_fte_jr2025_statutory",
        "2025",
        FTE,
        f"CW social-balance FTE / Employees {FTE}",
        f"tick2211; Medium CW; FTE JUMP vs YE2024 {FTE_PY}; assets/debt Unknown pending NBB PDF",
    ),
    (
        "bud_werkhuizen_min_bruto_jr2024_statutory_cmp",
        "2024",
        BRUTO_PY,
        "CW statutory bruto YE2024 comparative",
        f"tick2211; YE2024 bruto {BRUTO_PY} comparative for DROP calc",
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
            title="Werkhuizen MIN Deurne YE2025 leftover dual (bruto DROP 3.06m empty-omzet / pnl LOSS FLIP -247k / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / packaging+enclave clients Antwerpen Deurne belt",
            legal_basis="VZW maatwerk (KBO 0407.699.908; Actief; 1 VE; RSZ NACE 88.993)",
            decision_date="2026-07-15",
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
                    "2024_bruto": BRUTO_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                    "2024_fte": FTE_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0407699908/werkhuizen-min",
            stated_goal="Sheltered employment / packaging+enclave maatwerk Antwerpen-Deurne",
            cut_option="Publish NBB PDF assets/debt FOI; disclose empty-omzet vs bruto 3.06m loonkost matrix + pnl LOSS FLIP -247k / equity DROP -31% recon",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>Werkhuizen_MIN>JR2025_statutory_L5",
            notes="tick2211; Medium CW; bruto primary envelope (omzet unpublished); pnl LOSS FLIP -367% + equity DROP -31%; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; ACG already filled tick2210 race; not TE-additive of 348bn; do not redo ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank/Werkplus",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="Werkhuizen MIN bruto DROP 3.06m / empty omzet / pnl LOSS FLIP (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>Werkhuizen_MIN>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes=f"CW bruto DROP envelope 3.06m (omzet unpublished) / pnl LOSS FLIP -247k from YE2024 profit 92k (-367%) / equity DROP 565k (-31%) / FTE JUMP 94.3; Deurne packaging+enclave maatwerk; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Deurne / public loonkost path / packaging+enclave clients",
            stated_goal="Sheltered employment maatwerk packaging + enclave",
            measured_outcome="omzet unpublished; bruto DROP -3.96%; pnl LOSS FLIP -367.1%; equity DROP -31.02%; FTE JUMP +0.5",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; disclose empty-omzet vs bruto loonkost/GESCO/ESF/VDAB/gemeente split; recon LOSS FLIP -247k with equity DROP -31% and FTE JUMP",
            status="open",
            struck_reason="",
            notes=f"tick2211; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; AGB Bornem JR2024; after ACG EVERY-10 race",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Werkhuizen MIN / WERKHUIZEN M.I.N. VZW (Antwerpen-Deurne / maatwerk)",
            name_fr="Werkhuizen MIN ASBL (Anvers-Deurne / entreprise de travail adapté)",
            name_en="Werkhuizen MIN sheltered workshop (Antwerp-Deurne maatwerk)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.whmin.be/",
            foi_email="info@whmin.be",
            foi_postal="Van Cortbeemdelei 382, 2100 Antwerpen",
            notes=f"tick2211 YE2025 Medium CW NL+EN+FR + Strong KBO 0407.699.908 Actief VZW 1 VE RSZ NACE 88.993; empty omzet; bruto DROP {BRUTO} pnl LOSS FLIP {PNL} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 15.07.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>Werkhuizen_MIN>NBB_PDF_assets_debt_empty_omzet_bruto_drop_pnl_loss_flip",
            entity_id=ENTITY,
            what_is_missing=f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); empty/unpublished omzet vs bruto EUR{BRUTO} DROP -3.96% loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix; pnl LOSS FLIP EUR{PNL} vs YE2024 profit EUR{PNL_PY} (-367.1%) recon with equity DROP EUR{EQUITY} (-31.02%) and FTE JUMP {FTE_PY}->{FTE}; 1 VE packaging/enclave split",
            why_it_matters="Medium CW shows Deurne maatwerk VZW (bruto 3.06m / equity 0.57m / FTE 94.3) with unpublished omzet, pnl LOSS FLIP -367% and equity DROP -31% under public subsidy path; assets/debt unpublished",
            priority="8",
            recipient_body="Werkhuizen MIN VZW",
            recipient_email="info@whmin.be",
            recipient_postal="Van Cortbeemdelei 382, 2100 Antwerpen",
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
            notes="tick2211; ready NOT sent; Medium CW + Strong KBO; stall FARO/AIESH/REW YE2024; AGB Bornem JR2024; next every-10 2220",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Werkhuizen MIN Deurne (NBB PDF / empty omzet / bruto DROP 3.06m / pnl LOSS FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Werkhuizen MIN VZW (WERKHUIZEN M.I.N.) — KBO **0407.699.908** (Actief; Van Cortbeemdelei 382, 2100 Antwerpen; **1 VE**; FTE {FTE} CW; RSZ NACE **88.993**)  
**recipient:** info@whmin.be · Van Cortbeemdelei 382, 2100 Antwerpen · +32 3 270 75 00  
**sources:** [CW EN](https://www.companyweb.be/en/0407699908/werkhuizen-min) · [CW NL](https://www.companyweb.be/nl/0407699908/werkhuizen-min) · [CW FR](https://www.companyweb.be/fr/0407699908/werkhuizen-min) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407699908) · [whmin.be](https://www.whmin.be/)  
**tick:** 2211  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 09.11.1970; **1 VE**; RSZ NACE **88.993**; zetel Van Cortbeemdelei 382 Deurne.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** DROP -3.96% vs YE2024 EUR{BRUTO_PY:,}; pnl **EUR{PNL:,}** LOSS FLIP -367.1% vs YE2024 profit EUR{PNL_PY:,}; equity **EUR{EQUITY:,}** DROP -31.02% vs YE2024 EUR{EQUITY_PY:,}; FTE **{FTE}** JUMP vs {FTE_PY}; filed **15.07.2026**.
- Assets/debt/cash Unknown. Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. ACG already filled tick2210 race.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Werkhuizen MIN VZW
via info@whmin.be
Van Cortbeemdelei 382, 2100 Antwerpen
Betreft: Openbaarmaking jaarrekening 2025 Werkhuizen MIN (KBO 0407.699.908)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Unpublished omzet vs bruto EUR3.055.393 — loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix.
3. Pnl LOSS FLIP EUR-246.925 (-367,1%) vs YE2024 winst EUR92.446 reconciliatie met equity DROP EUR565.216 (-31,02%) en FTE JUMP 93,8→94,3.
4. Packaging vs enclave vs montage cost allocation (1 VE).
5. Eventuele herstructurering / fuseepad toelichting 2025-2026.

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
        "rq_2211": dict(
            title="leftover dual — Werkhuizen MIN YE2025 Medium (bruto DROP 3.06m empty-omzet / pnl LOSS FLIP -247k)",
            status="done",
            entity_id=ENTITY,
            updated_utc=TS,
            notes=f"tick2211 Werkhuizen MIN 0407.699.908 Medium; empty omzet; bruto DROP {BRUTO} pnl LOSS FLIP {PNL} equity DROP {EQUITY} FTE JUMP {FTE}; 1 VE Deurne; AGB Bornem JR2024; FARO/AIESH/REW YE2024; ACG done tick2210 race; FOI {GAP} ready not sent",
        )
    },
)

# spawn next
with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)
have = {row["task_id"] for row in rows}
if "rq_2212" not in have:
    rows.append(
        {
            "task_id": "rq_2212",
            "title": "leftover dual hole-fill after Werkhuizen MIN — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "Tick 2212 after rq_2211 Werkhuizen MIN YE2025 Medium (bruto DROP 3.06m empty-omzet / pnl LOSS FLIP). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS with live sourced €. Do not redo Werkhuizen MIN/ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/Aarova/MWP.",
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick2211 Werkhuizen MIN; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; next EVERY-10 2220",
        }
    )
    with (ROOT / "research_queue.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("spawned rq_2212")
else:
    print("rq_2212 already present")

(ROOT / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_2211,2211,no,"
    "tick2211 Werkhuizen MIN 0407.699.908 Medium (empty omzet; bruto DROP 3.06m; pnl LOSS FLIP -247k; equity DROP 0.57m -31%; FTE JUMP 94.3; 1 VE Deurne); "
    "ACG already filled tick2210 race; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2212; next every-10 2220; continuous hole_fill\n",
    encoding="utf-8",
)
print("loop_state -> 2211")

log_entry = f"""
## Tick 2211 - {TS} - rq_2211 Werkhuizen MIN (bruto DROP 3.06m empty-omzet / pnl LOSS FLIP -247k / Medium)

- Unit: **rq_2211** leftover dual after **rq_2210 EVERY-10 (+ACG race)**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. ACG already filled tick2210 race (omzet DROP 7.49m). Took named FREE leftover **Werkhuizen MIN VZW** YE2025 (KBO **0407.699.908**; Van Cortbeemdelei 382 Deurne; **Actief** **1 VE**; RSZ NACE **88.993**). Do not redo ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/De Kromme Boom/Aarova/Kaliber/MWP Pajottenland/De Winning/Atelier Groot Eiland/Groep Talent/BosKat/De Schakel/BWZ/Bewel/Forena/Kunnig/A-kwadraat/SW-WEB/Mivas/Demival/De Wroeter/Kringwinkel/Blankedale/Mirto/Mariasteen/De Brug/Weerwerk/InterWest/Westlandia/BWB/Wase/Groep INTRO/MAAAT/WAAK SW/Waak/Stijn/Stroom/Springplank.
- Found: Companyweb NL+EN+FR YE2025 - omzet **empty/unpublished**; bruto **EUR3055393** DROP -3.96% vs YE2024 EUR3181259; pnl **EUR-246925** LOSS FLIP -367.1% vs YE2024 profit EUR92446; equity **EUR565216** DROP -31.02%; FTE **94.3** JUMP vs 93.8; neerlegging **15.07.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@whmin.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 7.00); entities (+1 vzw_werkhuizen_min_antwerpen); foi + draft {GAP}; rq_2211=done + rq_2212 open; loop_state ticks=2211; raw docs/doge/data/raw/tick2211/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2210**; next **2220**). Next: rq_2212 (AGB/FARO-if-YE2025 / AIESH-REW / unused maatwerk-WZC-IGS).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_entry)
print("log appended")
print("DONE tick2211")
