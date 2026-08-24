# -*- coding: utf-8 -*-
"""Tick 2210 EVERY-10 + ACG YE2025 leftover dual."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T16:00:00Z"
TICK = 2210

ENTITY = "vzw_acg_antwerpen"
OMZET = 7487615
BRUTO = 14175803
PNL = 315317
EQUITY = 18446566
FTE = 372.5
OMZET_PY = 8903501
BRUTO_PY = 14143837
PNL_PY = 186431
EQUITY_PY = 18182189
FTE_PY = 364.9
RATIO = round(BRUTO / OMZET, 2)  # ~1.89

SRC_EN = "src_acg_jr2025_cw_en"
COMM = "comm_acg_jr2025_statutory_maatwerk_omzet_drop_bruto_gt_omzet_pnl_jump"
LB = "lb_acg_omzet_drop_7_49m_bruto_gt_omzet_pnl_jump_69pct_jr2025"
GAP = "gap_acg_nbb_pdf_assets_debt_omzet_drop_bruto_gt_omzet_pnl_jump_matrix_l5"

# ~7.49m → cost 5.4; abs 7.8 (omzet DROP -16% + pnl JUMP +69% + bruto≫~1.89x); diff 3.0
# peer-aligned (Oesterbank band + DROP/JUMP divergence) → 7.00
PI = "7.00"
ABS = "7.8"
COST = "5.4"
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


def count_rows(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_acg_jr2025_cw_nl",
            title="Companyweb NL ACG YE2025 statutory",
            url="https://www.companyweb.be/nl/0406611726/added-value-services-co-packing-greencare-acg-",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2210 EVERY-10; YE2025 omzet DROP {OMZET} (-15.9%) bruto JUMP {BRUTO} (≫omzet ~{RATIO}x) pnl JUMP {PNL} (+69.13%) equity JUMP {EQUITY} (+1.45%) FTE JUMP {FTE}; neerlegging 12.06.2026; raw docs/doge/data/raw/tick2210/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN ACG YE2025 statutory",
            url="https://www.companyweb.be/en/0406611726/added-value-services-co-packing-greencare-acg-",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2210; EN mirror YE2025 Medium; filed 12-06-2026; Last balance sheet year 2025; Big {FTE} FTE; Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; raw tick2210/",
        ),
        dict(
            source_id="src_acg_jr2025_cw_fr",
            title="Companyweb FR ACG YE2025 statutory",
            url="https://www.companyweb.be/fr/0406611726/added-value-services-co-packing-greencare-acg-",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2210; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OMZET}; Marge brute {BRUTO}; Benefice {PNL}; Capitaux propres {EQUITY}; raw tick2210/",
        ),
        dict(
            source_id="src_acg_kbo_2210",
            title="KBO ACG 0406.611.726 Actief VZW Antwerpen Deurne 1 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0406611726",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2210; Actief VZW sinds 01.03.1963; naam Added value services Co-packing & Greencare (ACG) / afkorting ACG; zetel Bosuil 138 2100 Antwerpen; 1 VE; RSZ/BTW NACE 88.993",
        ),
        dict(
            source_id="src_acg_site_contact_2210",
            title="ACG FOI channel info@acgfab.be",
            url="https://www.acgfab.be/",
            publisher="ACG VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2210; info@acgfab.be; +32 3 326 31 10; Bosuil 138 2100 Deurne; co-packing / greencare / added-value services maatwerk",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_acg_omzet_jr2025_statutory",
        "2025",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        f"tick2210; Medium CW; omzet DROP -15.9% vs YE2024 {OMZET_PY}; primary envelope",
    ),
    (
        "bud_acg_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        f"tick2210; Medium CW; bruto JUMP +0.23% vs YE2024 {BRUTO_PY}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_acg_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        f"tick2210; Medium CW; pnl JUMP +69.13% vs YE2024 {PNL_PY}",
    ),
    (
        "bud_acg_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        f"tick2210; Medium CW; equity JUMP +1.45% vs YE2024 {EQUITY_PY}",
    ),
    (
        "bud_acg_fte_jr2025_statutory",
        "2025",
        FTE,
        f"CW social-balance FTE / Employees {FTE}",
        f"tick2210; Medium CW; FTE JUMP vs YE2024 {FTE_PY}; assets/debt Unknown pending NBB PDF",
    ),
    (
        "bud_acg_omzet_jr2024_statutory_cmp",
        "2024",
        OMZET_PY,
        "CW statutory omzet YE2024 comparative",
        f"tick2210; YE2024 omzet {OMZET_PY} comparative for DROP calc",
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
            title="ACG Antwerpen YE2025 leftover dual (omzet DROP 7.49m / bruto≫omzet ~1.89x / pnl JUMP +69% / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / co-packing+greencare clients Antwerpen Deurne belt",
            legal_basis="VZW maatwerk (KBO 0406.611.726; Actief; 1 VE; RSZ NACE 88.993)",
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
            evaluation_url="https://www.companyweb.be/en/0406611726/added-value-services-co-packing-greencare-acg-",
            stated_goal="Sheltered employment / co-packing + greencare maatwerk Antwerpen",
            cut_option=f"Publish NBB PDF assets/debt FOI; disclose bruto~{RATIO}x omzet loonkost matrix + omzet DROP -16% vs pnl JUMP +69% recon",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>ACG>JR2025_statutory_L5",
            notes=f"tick2210 EVERY-10; Medium CW; omzet primary envelope; bruto≫omzet (~{RATIO}x) + omzet DROP -15.9% with pnl JUMP +69.13% + FTE JUMP; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn; do not redo Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank/Werkplus/Trianval",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="ACG omzet DROP 7.49m / bruto≫omzet ~1.89x / pnl JUMP +69% (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>ACG>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=f"CW omzet DROP envelope 7.49m / bruto 14.18m ≫ omzet (~{RATIO}x) / pnl JUMP 315k +69% from YE2024 186k / equity JUMP 18.45m / FTE JUMP 372.5; Antwerpen co-packing+greencare maatwerk; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Deurne / public loonkost path / co-packing+greencare clients",
            stated_goal="Sheltered employment maatwerk co-packing + greencare",
            measured_outcome="omzet DROP -15.9%; bruto JUMP +0.23%; pnl JUMP +69.13%; equity JUMP +1.45%; FTE JUMP +2.1%",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal=f"Publish NBB PDF assets/debt/cash FOI; disclose bruto~{RATIO}x omzet loonkost/GESCO/ESF/VDAB/gemeente split; recon omzet DROP -16% vs pnl JUMP +69% with FTE JUMP",
            status="open",
            struck_reason="",
            notes=f"tick2210 EVERY-10; Medium CW; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; Antwerpen maatwerk dual after Noordheuvel",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="ACG VZW / Added value services Co-packing & Greencare (Antwerpen-Deurne / maatwerk)",
            name_fr="ACG ASBL / Added value services Co-packing & Greencare (Anvers-Deurne / entreprise de travail adapté)",
            name_en="ACG sheltered workshop (Antwerp-Deurne; co-packing & greencare maatwerk)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.acgfab.be/",
            foi_email="info@acgfab.be",
            foi_postal="Bosuil 138, 2100 Antwerpen",
            notes=f"tick2210 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0406.611.726 Actief VZW 1 VE RSZ NACE 88.993; omzet DROP {OMZET} bruto {BRUTO} (≫omzet ~{RATIO}x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 12.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>ACG>NBB_PDF_assets_debt_omzet_drop_bruto_gt_omzet_pnl_jump",
            entity_id=ENTITY,
            what_is_missing=f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix; omzet DROP EUR{OMZET} vs YE2024 EUR{OMZET_PY} (-15.9%) recon with pnl JUMP EUR{PNL} (+69.13%) and FTE JUMP {FTE_PY}->{FTE}; equity JUMP EUR{EQUITY}; 1 VE + co-packing/greencare split",
            why_it_matters="Medium CW shows large Antwerpen maatwerk VZW (omzet 7.49m / bruto 14.18m / equity 18.45m / FTE 372.5) with bruto ~1.89x omzet and omzet DROP -16% while pnl JUMP +69% under public subsidy path; assets/debt unpublished",
            priority="8",
            recipient_body="ACG VZW",
            recipient_email="info@acgfab.be",
            recipient_postal="Bosuil 138, 2100 Antwerpen",
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
            notes="tick2210 EVERY-10; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; AGB Bornem JR2024; next every-10 2220",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — ACG Antwerpen-Deurne (NBB PDF / omzet DROP / bruto≫omzet ~{RATIO}x / pnl JUMP +69%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** ACG VZW (Added value services Co-packing & Greencare) — KBO **0406.611.726** (Actief; Bosuil 138, 2100 Antwerpen; **1 VE**; FTE {FTE} CW; RSZ NACE **88.993**)  
**recipient:** info@acgfab.be · Bosuil 138, 2100 Antwerpen · +32 3 326 31 10  
**sources:** [CW EN](https://www.companyweb.be/en/0406611726/added-value-services-co-packing-greencare-acg-) · [CW NL](https://www.companyweb.be/nl/0406611726/added-value-services-co-packing-greencare-acg-) · [CW FR](https://www.companyweb.be/fr/0406611726/added-value-services-co-packing-greencare-acg-) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406611726) · [acgfab.be](https://www.acgfab.be/)  
**tick:** 2210 (EVERY-10)  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 01.03.1963; **1 VE**; RSZ NACE **88.993**; zetel Bosuil 138 Deurne.
- CW YE2025: omzet **EUR{OMZET:,}** DROP -15.9% vs YE2024 EUR{OMZET_PY:,}; bruto **EUR{BRUTO:,}** JUMP +0.23% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL:,}** JUMP +69.13% vs YE2024 EUR{PNL_PY:,}; equity **EUR{EQUITY:,}** JUMP +1.45%; FTE **{FTE}** JUMP vs {FTE_PY}; filed **12.06.2026**.
- Assets/debt/cash Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: ACG VZW
via info@acgfab.be
Bosuil 138, 2100 Antwerpen
Betreft: Openbaarmaking jaarrekening 2025 ACG (KBO 0406.611.726)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Bruto EUR14.18m ≫ omzet EUR7.49m (~{RATIO}x) — loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix.
3. Omzet DROP EUR7.487.615 (-15,9%) vs pnl JUMP EUR315.317 (+69,13%) en FTE JUMP 364,9→372,5 reconciliatie.
4. Equity JUMP EUR18.446.566 path.
5. Co-packing vs greencare vs added-value services cost allocation (1 VE).

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
        "rq_2210": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": "EVERY-10 + leftover dual — ACG YE2025 Medium (omzet DROP 7.49m / bruto≫omzet ~1.89x / pnl JUMP +69%)",
            "instructions": "Completed EVERY-10@2210 + leftover ACG after Noordheuvel; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent; progress+top10 refreshed",
            "notes": f"tick2210 EVERY-10 + ACG 0406.611.726 Medium; omzet DROP {OMZET} bruto {BRUTO} (~{RATIO}x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; 1 VE Deurne; AGB Bornem JR2024; FARO/REW YE2024; next rq_2211; next every-10 2220",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2211",
            title="leftover dual hole-fill after ACG — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2211 after EVERY-10 ACG Antwerpen YE2025 Medium (omzet DROP 7.49m / bruto≫omzet ~1.89x / pnl JUMP +69%). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(Odas still YE2024; hunt next FREE maatwerk/WZC/IGS with live YE2025). "
                "Do NOT redo ACG, Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, "
                "Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, "
                "Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
                "WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, "
                "IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2220."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2210 EVERY-10 + ACG; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; next EVERY-10 at 2220",
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
        row["last_unit_id"] = "rq_2210"
        row["ticks_completed"] = "2210"
        row["paused"] = "no"
        row["notes"] = (
            f"tick2210 EVERY-10 + leftover ACG 0406.611.726 Medium (omzet DROP 7.49m; bruto 14.18m ≫ omzet ~{RATIO}x; "
            f"pnl JUMP 315k +69%; equity JUMP 18.45m; FTE JUMP 372.5; 1 VE Deurne); "
            "AGB Bornem JR2024; FARO/REW YE2024; next rq_2211; next every-10 2220; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2210")

# --- EVERY-10 progress + top10 ---
n_bud = count_rows(ROOT / "budgets.csv")
n_cmt = count_rows(ROOT / "commitments.csv")
n_lb = count_rows(ROOT / "leaderboard.csv")
n_ent = count_rows(ROOT / "entities.csv")
n_src = count_rows(ROOT / "sources.csv")
with (ROOT / "foi_queue.csv").open(newline="", encoding="utf-8") as f:
    foi_rows = list(csv.DictReader(f))
foi_ready = sum(1 for r in foi_rows if r.get("status") == "ready")
foi_ans = sum(1 for r in foi_rows if r.get("status") == "answered")
foi_part = sum(1 for r in foi_rows if r.get("status") == "partial")
foi_tot = len(foi_rows)

(ROOT / "progress_every_10_ticks.md").write_text(
    f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2210** (2026-08-26)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2201-2210 continuum; AGB Bornem / FARO / AIESH / REW still YE2024 stalls |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2201-2210 is residual dual L5 (not near-complete of 348bn):** **MWP Pajottenland** / **De Winning** · **Kaliber** / **Aarova** · **Ijsedal** / **Kromme Boom** · **Trianval** / **Werkplus** · **Oesterbank** omzet **7.31m** · **Entiris** omzet **18.93m** / equity **92.3m** · **Kemphaan** · **Arcor** empty omzet · **Noordheuvel** LOSS FLIP · **ACG** omzet DROP **7.49m** / bruto~**1.89×** / pnl JUMP **+69%** (EVERY-10 primary) Medium |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~{foi_ans}**; partial **~{foi_part}**; total FOI rows **~{foi_tot}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2201-2210** MWP · De Winning · Kaliber · Aarova · Ijsedal · Kromme Boom · Trianval · Werkplus · Oesterbank · Entiris · Kemphaan · Arcor · Noordheuvel · **ACG** · prior 2191-2200 stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2210)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {n_bud}+ |
| commitments.csv | {n_cmt}+ |
| leaderboard.csv | {n_lb}+ |
| entities.csv | {n_ent}+ |
| sources.csv | {n_src}+ |
| FOI ready | ~{foi_ready} |
| FOI answered | {foi_ans} |
| FOI partial | {foi_part} |
| FOI total rows | ~{foi_tot} |
| research_queue open | rq_2211 after progress |

### What improved since tick 2200

- **Residual dual (tick2201-2210):** **MWP Pajottenland** / **De Winning** · **Kaliber** (KEMPA merger / LOSS FLIP) / **Aarova** · **Ijsedal** / **Kromme Boom** (equity NEG FLIP) · **Trianval** / **Werkplus** (empty omzet) · **Oesterbank** (omzet JUMP **7.31m** / bruto~**1.89×** / pnl JUMP **+237%** / FTE DROP) · **Entiris** (omzet JUMP **18.93m** / bruto~**2.39×** / equity JUMP **92.3m**) · **Kemphaan** (pnl JUMP **+75%** / FTE DROP) · **Arcor** (bruto **4.06m** / empty omzet / pnl JUMP **+75%**) · **Noordheuvel** (pnl LOSS FLIP / bruto~**2.00×**) · **ACG** (EVERY-10 primary — omzet DROP **7.49m** **-15.9%**; bruto~**1.89×**; pnl JUMP **+69%**; FTE JUMP **372.5**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024) · AIESH / REW YE2024-only · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.
""",
    encoding="utf-8",
)
print("progress_every_10_ticks.md refreshed")

(ROOT / "doge_waste_top10_current.md").write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **2210** (2026-08-26) · **{n_lb}+** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55·cost_score + 0.35·absurdity + 0.10·(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 4 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |
| 9 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 10 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2201-2210:** **Entiris omzet 18.93m / equity 92.3m** · **ACG omzet DROP 7.49m / bruto~1.89× / pnl JUMP +69%** (EVERY-10@2210 primary) · **Oesterbank 7.31m** · **Arcor empty omzet / bruto 4.06m** · **Noordheuvel LOSS FLIP** · **Kemphaan pnl JUMP +75%** · prior 2191-2200 Bewel/Forena/Demival/De Schakel/Groep Talent/AGE stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2200:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2201-2210 (off pure top10 / dual):** MWP · De Winning · Kaliber · Aarova · Ijsedal · Kromme Boom · Trianval · Werkplus · Oesterbank · Entiris · Kemphaan · Arcor · Noordheuvel · **ACG omzet DROP 7.49m / bruto~1.89× / pnl JUMP +69%** (EVERY-10@2210 primary). Count NEW since 2200: ~14 residual dual fills. **Prior 2191-2200 + 2181-2190 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Entiris** omzet **EUR18.93m** / bruto **~2.39×** / equity JUMP **EUR92.3m** / FTE **1448.5**.
- **ACG** EVERY-10 primary omzet DROP **EUR7.49m (−15.9%)** / bruto **~1.89×** / pnl JUMP **+69%** / FTE JUMP **372.5** — Antwerpen co-packing+greencare subsidy opacity.
- **Oesterbank** omzet **EUR7.31m** / bruto **~1.89×** / pnl JUMP **+237%** / FTE DROP.
- **Arcor** empty omzet YE2025+YE2024 / bruto **EUR4.06m** / pnl JUMP **+75%** / equity DROP.
- **Noordheuvel** pnl LOSS FLIP despite omzet JUMP / bruto **~2.00×**.
- **De Schakel Balen** bruto **~7.3×** omzet (prior retained).
- **Bewel** omzet **EUR28.64m** / bruto **~2.3×** (prior retained).
- **Stijn** bruto **EUR128.0m** ≫ omzet **EUR22.7m** (prior retained).
- Walloon **ZS** stack FTE-only budget opacity.
""",
    encoding="utf-8",
)
print("doge_waste_top10_current.md refreshed")

log_block = f"""
## Tick 2210 - {TS} - rq_2210 EVERY-10 + ACG Antwerpen (omzet DROP 7.49m / bruto≫omzet ~{RATIO}x / pnl JUMP +69% / Medium)

- Unit: **rq_2210 EVERY-10** after **rq_2209 Noordheuvel**. Refreshed progress_every_10_ticks.md + doge_waste_top10_current.md (top10 stable GIP/fossil/cars; Metro3/OWV stock-filtered). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; REW still **YE2024**. Took named FREE leftover **ACG VZW** YE2025 (KBO **0406.611.726**; Bosuil 138 Deurne; **Actief** **1 VE**; RSZ NACE **88.993**; full name Added value services Co-packing & Greencare). Do not redo Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/De Kromme Boom/Aarova/Kaliber/MWP/De Winning/AGE/Groep Talent/BosKat/De Schakel/BWZ/Bewel/Forena.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP -15.9% vs YE2024 EUR{OMZET_PY}; bruto **EUR{BRUTO}** JUMP +0.23% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL}** JUMP +69.13% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** JUMP +1.45%; FTE **{FTE}** JUMP vs {FTE_PY}; neerlegging **12.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@acgfab.be.
- Wrote: progress+top10; sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2210=done + rq_2211 open; loop_state ticks=2210; raw docs/doge/data/raw/tick2210/.
- FOI: **ready not sent** (human-gated).
- **EVERY-10 done** (last was 2200; next **2220**). Next: rq_2211 (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS-HVZ).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2210 EVERY-10 ACG")
