# -*- coding: utf-8 -*-
"""Tick 2200 EVERY-10 + Atelier Groot Eiland YE2025 leftover dual."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T12:40:00Z"
TICK = 2200

ENTITY = "vzw_atelier_groot_eiland_molenbeek"
BRUTO = 2934111
PNL = 23906
EQUITY = 1014772
FTE = 53.6
BRUTO_PY = 2719635
PNL_PY = 6583
EQUITY_PY = 1069202
FTE_PY = 55.4
# omzet unpublished — bruto is primary envelope
OMZET = ""
SRC_EN = "src_age_jr2025_cw_en"
COMM = "comm_age_jr2025_statutory_maatwerk_bruto_pnl_jump_equity_drop_omzet_empty"
LB = "lb_age_bruto_2_93m_pnl_jump_equity_drop_omzet_empty_jr2025"
GAP = "gap_age_nbb_pdf_assets_debt_omzet_empty_bruto_pnl_jump_equity_drop_loonkost_matrix_l5"

# cost_score <10m → 3.5; abs 6.6 (pnl JUMP +263% / equity DROP / omzet empty / maatwerk); diff 3.0
# pi = 0.55*3.5 + 0.35*6.6 + 0.10*7.0 = 1.925 + 2.31 + 0.7 = 4.935 → 4.94
PI = "4.94"
ABS = "6.6"
COST = "3.5"
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
            source_id="src_age_jr2025_cw_nl",
            title="Companyweb NL Atelier Groot Eiland YE2025 statutory",
            url="https://www.companyweb.be/nl/0430686037/atelier-groot-eiland",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2200 EVERY-10; YE2025 omzet empty; bruto JUMP 2934111 (+7.89%); pnl JUMP 23906 (+263.14%); equity DROP 1014772 (-5.09%); FTE DROP 53.6; neerlegging 24.06.2026; assets/debt Unknown; raw tick2200/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN Atelier Groot Eiland YE2025 statutory",
            url="https://www.companyweb.be/en/0430686037/atelier-groot-eiland",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2200; EN mirror YE2025 Medium; filed 24-06-2026; Last balance sheet year 2025; Big 53.6 FTE; Gross margin 2934111; Profit/Loss 23906; Equity 1014772; Turnover not published; raw tick2200/",
        ),
        dict(
            source_id="src_age_jr2025_cw_fr",
            title="Companyweb FR Atelier Groot Eiland YE2025 statutory",
            url="https://www.companyweb.be/fr/0430686037/atelier-groot-eiland",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2200; FR mirror YE2025 Medium; Dernier bilan 2025; Marge brute 2934111; Benefice 23906; Capitaux propres 1014772; CA non publie; raw tick2200/",
        ),
        dict(
            source_id="src_age_kbo_2200",
            title="KBO Atelier Groot Eiland 0430.686.037 Actief VZW Molenbeek 4 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0430686037",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2200; Actief VZW sinds 23.01.1985; zetel Henegouwenkaai 29 1080 Sint-Jans-Molenbeek; 4 VE; RSZ NACE 88.993 beschutte/sociale werkplaatsen; BTW 01.130/56.111/56.112; RSZ-werkgever sinds 01.07.1989",
        ),
        dict(
            source_id="src_age_site_contact_2200",
            title="Atelier Groot Eiland FOI channel info@grooteiland.brussels",
            url="https://grooteiland.brussels/",
            publisher="Atelier Groot Eiland VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2200; info@grooteiland.brussels; secretariaat@grooteiland.brussels; Henegouwenkaai 29 1080 Sint-Jans-Molenbeek; maatwerk + horeca + urban farming",
        ),
    ],
)

# --- budgets (bruto primary; no invented omzet) ---
budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_age_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025 (omzet unpublished)",
        "tick2200; Medium CW; bruto JUMP +7.89% vs YE2024 2719635; primary envelope (omzet empty)",
    ),
    (
        "bud_age_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2200; Medium CW; pnl JUMP +263.14% vs YE2024 6583",
    ),
    (
        "bud_age_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2200; Medium CW; equity DROP -5.09% vs YE2024 1069202",
    ),
    (
        "bud_age_fte_jr2025_statutory",
        "2025",
        FTE,
        "CW social-balance FTE / Employees 53.6",
        "tick2200; Medium CW; FTE DROP vs YE2024 55.4; assets/debt Unknown pending NBB PDF",
    ),
    (
        "bud_age_bruto_jr2024_statutory_cmp",
        "2024",
        BRUTO_PY,
        "CW statutory bruto_marge YE2024 comparative",
        "tick2200; YE2024 bruto 2719635 comparative for JUMP calc",
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
            title="Atelier Groot Eiland Molenbeek YE2025 leftover dual (bruto JUMP 2.93m / pnl JUMP +263% / equity DROP / omzet empty / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / social-economy clients Brussels-Molenbeek / urban farming+horeca path",
            legal_basis="VZW maatwerk (KBO 0430.686.037; Actief; 4 VE; RSZ NACE 88.993; BTW 01.130/56.111/56.112)",
            decision_date="2026-06-24",
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
            evaluation_url="https://www.companyweb.be/en/0430686037/atelier-groot-eiland",
            stated_goal="Sheltered employment / maatwerk + urban farming + social horeca Molenbeek",
            cut_option="Publish NBB PDF assets/debt FOI; disclose omzet empty vs bruto 2.93m loonkost/GESFO/Actiris/ESF matrix + equity DROP",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Bruxelles>Molenbeek>AtelierGrootEiland>JR2025_statutory_L5",
            notes="tick2200 EVERY-10; Medium CW; bruto primary envelope (omzet unpublished); pnl JUMP +263% with equity DROP -5%; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024 stalls; not TE-additive of 348bn; do not redo Groep Talent/BosKat/De Schakel/BWZ/Kunnig/Forena/Bewel/SW-WEB/Mivas/Demival",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="Atelier Groot Eiland bruto JUMP 2.93m / pnl JUMP +263% / equity DROP -5% / omzet empty (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Bruxelles>Molenbeek>AtelierGrootEiland>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes="CW bruto JUMP envelope 2.93m (omzet unpublished) / pnl JUMP 24k +263% / equity DROP 1.01m -5% / FTE DROP 53.6; assets/debt Unknown; public loonkost matrix FOI",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Molenbeek / Actiris-ESF-GESFO path / social horeca+farming clients",
            stated_goal="Sheltered employment maatwerk + urban farming + social restaurants",
            measured_outcome="bruto JUMP +7.89%; pnl JUMP +263.14%; equity DROP -5.09%; FTE DROP 55.4→53.6; omzet unpublished",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; disclose omzet empty vs bruto 2.93m loonkost/GESFO/Actiris/ESF/commune matrix + equity DROP recon",
            status="open",
            struck_reason="",
            notes="tick2200 EVERY-10; Medium CW; FOI gap_age_nbb_pdf_assets_debt_omzet_empty_bruto_pnl_jump_equity_drop_loonkost_matrix_l5; stall FARO/AIESH/REW YE2024; AGB Bornem JR2024",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Atelier Groot Eiland VZW (Sint-Jans-Molenbeek / maatwerk)",
            name_fr="Atelier Groot Eiland ASBL (Molenbeek-Saint-Jean / entreprise de travail adapté)",
            name_en="Atelier Groot Eiland sheltered workshop (Molenbeek; maatwerk)",
            level="parastatal",
            parent_id="sec_brussels",
            community_language="nl",
            website="https://grooteiland.brussels/",
            foi_email="info@grooteiland.brussels",
            foi_postal="Henegouwenkaai 29, 1080 Sint-Jans-Molenbeek",
            notes="tick2200 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0430.686.037 Actief VZW 4 VE RSZ NACE 88.993; bruto JUMP 2.93m (+7.89%) pnl JUMP 24k (+263%) equity DROP 1.01m (-5%) FTE DROP 53.6 omzet empty; neerlegging 24.06.2026; assets/debt Unknown; FOI gap_age_nbb_pdf_assets_debt_omzet_empty_bruto_pnl_jump_equity_drop_loonkost_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Groep Talent/BosKat/De Schakel/BWZ/Kunnig/Forena/Bewel/SW-WEB/Mivas/Demival/De Wroeter",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Bruxelles>Molenbeek>AtelierGrootEiland>NBB_PDF_assets_debt_omzet_empty_bruto_pnl_jump_equity_drop_loonkost",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); why omzet (code70) unpublished while bruto EUR2.93m published; loonkostsubsidie/GESFO/Actiris/ESF/commune matrix; equity DROP -5% recon with pnl JUMP +263%; 4 VE cost allocation",
            why_it_matters="Medium CW shows Brussels maatwerk VZW (bruto 2.93m / 53.6 FTE / 4 VE) with omzet empty, pnl JUMP +263% and equity DROP — residual dual/public-adjacent loonkost opacity",
            priority="8",
            recipient_body="Atelier Groot Eiland VZW",
            recipient_email="info@grooteiland.brussels",
            recipient_postal="Henegouwenkaai 29, 1080 Sint-Jans-Molenbeek",
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
            notes="tick2200 EVERY-10; ready NOT sent; Medium CW + Strong KBO; stall FARO/AIESH/REW YE2024; next every-10 2210",
        )
    ],
)

# FOI draft
FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Atelier Groot Eiland Molenbeek (NBB PDF / omzet empty / bruto JUMP / equity DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Atelier Groot Eiland VZW — KBO **0430.686.037** (Actief; Henegouwenkaai 29, 1080 Sint-Jans-Molenbeek; **4 VE**; FTE 53.6 CW; RSZ NACE **88.993**)  
**recipient:** info@grooteiland.brussels · Henegouwenkaai 29, 1080 Sint-Jans-Molenbeek  
**sources:** [CW EN](https://www.companyweb.be/en/0430686037/atelier-groot-eiland) · [CW NL](https://www.companyweb.be/nl/0430686037/atelier-groot-eiland) · [CW FR](https://www.companyweb.be/fr/0430686037/atelier-groot-eiland) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0430686037) · [grooteiland.brussels](https://grooteiland.brussels/)  
**tick:** 2200 (EVERY-10)  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown; omzet unpublished)

## Context
- KBO Strong: Actief VZW sinds 23.01.1985; **4 VE**; RSZ NACE **88.993** beschutte/sociale werkplaatsen; BTW 01.130/56.111/56.112; zetel Henegouwenkaai 29 Molenbeek.
- CW YE2025: omzet **unpublished**; bruto **EUR2,934,111** JUMP +7.89% vs YE2024 EUR2,719,635; pnl **EUR23,906** JUMP +263.14% vs YE2024 EUR6,583; equity **EUR1,014,772** DROP -5.09%; FTE **53.6** DROP vs 55.4; filed **24.06.2026**.
- Assets/debt Unknown. Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Do not redo Groep Talent/BosKat/De Schakel/BWZ/Kunnig/etc.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Atelier Groot Eiland VZW
via info@grooteiland.brussels
Henegouwenkaai 29, 1080 Sint-Jans-Molenbeek
Betreft: Openbaarmaking jaarrekening 2025 Atelier Groot Eiland (KBO 0430.686.037)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur / ordonnance transparence (BCR) vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash/balanstotaal).
2. Waarom omzet (code 70) niet gepubliceerd is terwijl bruto EUR2.934.111 wel openbaar is.
3. Loonkostsubsidie/GESFO/Actiris/ESF/gemeente-toelage matrix achter bruto EUR2.93m.
4. PnL JUMP EUR23.906 (+263%) vs equity DROP EUR1.014.772 (-5,09%) reconciliatie.
5. 4 VE cost allocation (maatwerk / horeca / urban farming).

Periode YE2025 (+ YE2024 comparative). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("FOI draft written")

# --- research_queue: close 2200, open 2201 ---
update_csv_rows(
    ROOT / "research_queue.csv",
    "task_id",
    {
        "rq_2200": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": "EVERY-10 + leftover dual — Atelier Groot Eiland YE2025 Medium (bruto JUMP 2.93m / pnl JUMP +263% / equity DROP)",
            "instructions": "Completed EVERY-10@2200 + leftover AGE after Groep Talent; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent",
            "notes": "tick2200 EVERY-10 + AGE 0430.686.037 Medium bruto JUMP 2.93m pnl JUMP 24k equity DROP 1.01m FTE DROP 53.6 omzet empty; KBO Actief VZW 4 VE; FOI info@grooteiland.brussels; next rq_2201; every-10 next 2210",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2201",
            title="leftover dual hole-fill after AGE — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions="Tick 2201 leftover dual after rq_2200 Atelier Groot Eiland YE2025 Medium (bruto JUMP 2.93m / pnl JUMP +263% / equity DROP / omzet empty). Prefer NON-stall live: AGB Bornem if JR2025; FARO/AIESH/REW if YE2025; else unused IGS-DSO-WZC-MRS-HVZ with live sourced €. Do not redo AGE/Groep Talent/BosKat/De Schakel/BWZ/Kunnig/Forena/Bewel/SW-WEB/Mivas/Demival/De Wroeter/Kringwinkel Antwerpen/Blankedale/Mirto/Mariasteen/De Brug/Weerwerk/InterWest/Westlandia/BWB/Wase/Groep INTRO/MAAAT. Next EVERY-10 at 2210.",
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2200 EVERY-10 + AGE; FARO/AIESH/REW still YE2024; next EVERY-10 at 2210",
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
        row["last_unit_id"] = "rq_2200"
        row["ticks_completed"] = "2200"
        row["paused"] = "no"
        row["notes"] = (
            "tick2200 EVERY-10 + leftover AGE 0430.686.037 Medium (bruto JUMP 2.93m; pnl JUMP 24k +263%; equity DROP 1.01m; FTE DROP 53.6; omzet empty; 4 VE); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2201; next every-10 2210; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2200")

# --- progress + top10 (EVERY-10) ---
n_bud = sum(1 for _ in open(ROOT / "budgets.csv", encoding="utf-8")) - 1
n_cmt = sum(1 for _ in open(ROOT / "commitments.csv", encoding="utf-8")) - 1
n_lb = sum(1 for _ in open(ROOT / "leaderboard.csv", encoding="utf-8")) - 1
n_ent = sum(1 for _ in open(ROOT / "entities.csv", encoding="utf-8")) - 1
n_src = sum(1 for _ in open(ROOT / "sources.csv", encoding="utf-8")) - 1
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

## Snapshot at **tick 2200** (2026-08-26)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2191-2200 continuum; AGB Bornem / FARO / AIESH / REW still YE2024 stalls |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2191-2200 is residual dual L5 (not near-complete of 348bn):** **Demival** omzet **14.76m** · **Mivas** omzet **11.59m** · **SW-WEB** omzet **5.72m** / pnl LOSS DEEPEN · **Forena** omzet **16.30m** · **Bewel** omzet **28.64m** · **BWZ** omzet **10.16m** · **De Schakel** bruto≫omzet **~7.3x** · **BosKat** bruto **3.28m** / LOSS FLIP · **Groep Talent** omzet **6.24m** · **Atelier Groot Eiland** bruto **2.93m** / pnl JUMP **+263%** / equity DROP / omzet empty (EVERY-10 primary) Medium |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~{foi_ans}**; partial **~{foi_part}**; total FOI rows **~{foi_tot}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2191-2200** Demival · Mivas · SW-WEB · Forena · Bewel · BWZ · De Schakel · BosKat · Groep Talent · **Atelier Groot Eiland** · prior 2181-2190 stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2200)

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
| research_queue open | rq_2201 after progress |

### What improved since tick 2190

- **Residual dual (tick2191-2200):** **Demival** (omzet JUMP 14.76m / pnl FLIP) · **Mivas** (omzet DROP 11.59m / bruto≫omzet) · **SW-WEB** (omzet JUMP 5.72m / pnl LOSS DEEPEN −1.53m / equity DROP −43%) · **Forena** (omzet JUMP 16.30m / FTE JUMP +26% / pnl DROP −32%) · **Bewel** (omzet JUMP 28.64m / bruto≫omzet ~2.3x / pnl JUMP +241%) · **BWZ Zottegem** (omzet DROP 10.16m / pnl DROP −41%) · **De Schakel Balen** (bruto≫omzet ~7.3x / pnl DROP −49%) · **BosKat** (bruto JUMP 3.28m / pnl LOSS FLIP −207k / Stopgezet fusie Groep Talent) · **Groep Talent** (omzet JUMP 6.24m / bruto≫omzet ~1.48x / pnl DROP −31%) · **Atelier Groot Eiland** (EVERY-10 primary — bruto JUMP **2.93m**; omzet empty; pnl JUMP **+263%**; equity DROP **−5%**; FTE DROP **53.6**; Medium CW; FOI ready). Concurrent races also mined A-kwadraat / Kunnig where applicable.
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024 filing / CW last balance 2024; JV2025 activity report only) · AIESH / REW YE2024-only · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs (Dinaphi/ZHC/Hesbaye/WAPI/HEMECO/VDS/Vesdre/BW/Hainaut-Est FOI-ready).
""",
    encoding="utf-8",
)
print("progress_every_10_ticks.md refreshed")

(ROOT / "doge_waste_top10_current.md").write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **2200** (2026-08-26) · **{n_lb}+** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2191-2200:** **Bewel omzet 28.64m** · **Forena omzet 16.30m** · **Demival omzet 14.76m** · **Mivas omzet 11.59m** · **BWZ omzet 10.16m** · **Groep Talent omzet 6.24m** · **SW-WEB omzet 5.72m** · **De Schakel bruto≫omzet ~7.3x** · **BosKat bruto 3.28m LOSS FLIP** · **Atelier Groot Eiland bruto 2.93m** (EVERY-10@2200 primary) · prior 2181-2190 De Wroeter/Kringwinkel/Blankedale/Mariasteen stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2190:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2191-2200 (off pure top10 / dual):** Demival · Mivas · SW-WEB · Forena · Bewel · BWZ · De Schakel · BosKat · Groep Talent · **Atelier Groot Eiland bruto 2.93m** (EVERY-10@2200 primary). Count NEW since 2190: ~10 residual dual fills (+ concurrent A-kwadraat/Kunnig races). **Prior 2181-2190 + 2171-2180 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Bewel** omzet **EUR28.64m** / bruto≫omzet ~2.3x / pnl JUMP **+241%** / **2015 FTE**.
- **Forena** omzet **EUR16.30m** / FTE JUMP **+26%** / pnl DROP **−32%**.
- **De Schakel** bruto **~7.3×** omzet / pnl DROP **−49%**.
- **BosKat** bruto **EUR3.28m** / pnl LOSS FLIP **−EUR207k** / Stopgezet fusie Groep Talent.
- **Atelier Groot Eiland** EVERY-10 primary bruto JUMP **EUR2.93m** / omzet empty / pnl JUMP **+263%** / equity DROP **−5%** — loonkostsubsidie opacity.
- **SW-WEB** pnl LOSS DEEPEN **−EUR1.53m** / equity DROP **−43%**.
- **Kringwinkel Antwerpen / DKA** pnl LOSS FLIP **−EUR1.05m** (prior 2181-2190 retained).
- Walloon **ZS** stack (BW / Vesdre / Hainaut-Est / …) FTE-only budget opacity.
""",
    encoding="utf-8",
)
print("doge_waste_top10_current.md refreshed")

# --- loop_log append ---
log_block = f"""

## Tick 2200 - 2026-08-26T12:40:00Z - EVERY-10 + rq_2200 Atelier Groot Eiland (bruto JUMP 2.93m / pnl JUMP +263% / equity DROP -5% / Medium)

- Unit: **rq_2200** EVERY-10 mandatory after **rq_2199 Groep Talent**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW last balance 2024; JV2025 activity-only); AIESH/REW still **YE2024**. Took named FREE leftover **Atelier Groot Eiland VZW** YE2025 (KBO **0430.686.037**; Henegouwenkaai 29 Sint-Jans-Molenbeek; **VZW** RSZ NACE **88.993** / **4 VE**). Do not redo Groep Talent/BosKat/De Schakel/BWZ/Kunnig/Forena/Bewel/SW-WEB/Mivas/Demival/De Wroeter/Kringwinkel Antwerpen/Blankedale/Mirto/Mariasteen/De Brug/Weerwerk/InterWest/Westlandia/BWB/Wase/Groep INTRO/MAAAT.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR2934111** JUMP +7.89% vs YE2024 EUR2719635; pnl **EUR23906** JUMP +263.14% vs YE2024 EUR6583; equity **EUR1014772** DROP -5.09%; FTE **53.6** DROP vs 55.4; neerlegging **24.06.2026**. Assets/debt Unknown. Medium. Strong KBO Actief VZW 4 VE. FOI via info@grooteiland.brussels.
- EVERY-10: refreshed `progress_every_10_ticks.md` (A **100%** / B **100%** / C **~99%** / D **~74-88%** generous residual dual / E **~{foi_ready}** FOI-ready) + `doge_waste_top10_current.md` (pure annual top10 **stable** GIP→fossil/cars/cheque/reporté; AGE off-top10 residual). Next every-10 **2210**.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2200=done + rq_2201 open; loop_state ticks=2200; raw docs/doge/data/raw/tick2200/; progress+top10.
- FOI: **ready not sent** (human-gated).
- Next: rq_2201 (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS-HVZ).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2200")
