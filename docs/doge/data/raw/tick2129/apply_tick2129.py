# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T13:10:00Z"
TICK = 2129
RQ = "rq_2129"
NEXT_RQ = "rq_2130"
ENTITY = "vzw_mpc_sint_franciscus_roosdaal"
GAP = "gap_mpc_sint_franciscus_nbb_pdf_assets_debt_pnl_drop_bruto_matrix_l5"
COMM = "comm_mpc_sint_franciscus_jr2025_statutory_disability_care"
LB = "lb_mpc_sint_franciscus_bruto_jump_29_41m_pnl_drop_jr2025"
SRC_EN = "src_mpc_sint_franciscus_jr2025_cw_en"
KBO = "0415.850.084"
KBO_DIGITS = "0415850084"
OMZET = "2011499"
OMZET_YOY = "+6.09%"
BRUTO = "29406881"
BRUTO_PRIOR = "27586695"
BRUTO_YOY = "+6.6%"
PNL = "1170348"
PNL_PRIOR = "1491987"
PNL_YOY = "-21.56%"
EQUITY = "16535902"
EQUITY_PRIOR = "15687226"
EQUITY_YOY = "+5.41%"
FTE = "365.1"
FTE_PRIOR = "347.7"
ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def update_rq():
    path = DATA / "research_queue.csv"
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r.get("task_id") == RQ and r.get("status") == "open":
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["title"] = "leftover dual — MPC Sint-Franciscus Roosdaal YE2025 Medium"
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} MPC Sint-Franciscus Medium bruto JUMP 29.41m pnl DROP 1.17m equity JUMP 16.54m "
                f"omzet JUMP 2.01m FTE JUMP 365.1; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ} EVERY-10; next every-10 2130"
            )
            r["instructions"] = (
                f"Completed leftover dual MPC Sint-Franciscus after Zorghome De Fakkel; preferred AGB Bornem JR2024 / "
                f"FARO/AIESH/REW YE2024; live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"bruto JUMP {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} omzet JUMP {OMZET} FTE JUMP {FTE}; FOI {GAP}"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"{RQ} open not found")
    if not any(r.get("task_id") == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "EVERY-10 + leftover dual hole-fill after MPC Sint-Franciscus — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "9",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} EVERY-10 after MPC Sint-Franciscus YE2025 Medium. Refresh "
                    "progress_every_10_ticks.md + doge_waste_top10_current.md. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/"
                    "hospital/WZC/psych/MRS/creche/disability-care. Do NOT redo MPC Sint-Franciscus, Zorghome De Fakkel, "
                    "Le Château Vert, SLG Wallonie, Famifamenne, Residence Le Castel, R.S.W., Home Sebrechts, "
                    "Unite Jolimont, t Buurthuis, Le Bosquet, Strebo, Entraide, La Charmille, Charmilles, Sittelles, "
                    "Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, Sint-Camillus, "
                    "IDELUX*, INTRADEL, Korian*, SLG Operaties VL, SLG Vlaanderen VZW, Always Home, AREWAL, "
                    "AGB Bornem, Armonea holding, emeis holding, PC Gent-Sleidinge."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} MPC Sint-Franciscus; EVERY-10 at 2130; FARO/AIESH/REW still YE2024"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


# move raw from tick2128 probe into tick2129 folder expectation - files already in 2128; copy refs in notes
for s in [
    {
        "source_id": "src_mpc_sint_franciscus_jr2025_cw",
        "title": "Companyweb NL MPC Sint-Franciscus YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl DROP {PNL} ({PNL_YOY}) equity JUMP {EQUITY} ({EQUITY_YOY}) FTE JUMP {FTE} (vs {FTE_PRIOR}); "
            f"neerlegging 16.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2128/mpc_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN MPC Sint-Franciscus YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/medisch-pedagogisch-centrum-sint-franciscus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 16-06-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; FTE {FTE}; Principal activity residential care "
            f"minors mental disability; raw docs/doge/data/raw/tick2128/mpc_en.html"
        ),
    },
    {
        "source_id": "src_mpc_sint_franciscus_jr2025_cw_fr",
        "title": "Companyweb FR MPC Sint-Franciscus YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2128/mpc_fr.html",
    },
    {
        "source_id": f"src_mpc_sint_franciscus_kbo_{TICK}",
        "title": f"KBO MPC Sint-Franciscus {KBO} Actief Roosdaal",
        "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Actief VZW; Lostraat 175 1760 Roosdaal; 8 VE; RSZ NACE 87.201; "
            "aanbestedende overheid since 02.01.1976; email/web empty in KBO"
        ),
    },
    {
        "source_id": f"src_mpc_sint_franciscus_contact_{TICK}",
        "title": "MPC Sint-Franciscus FOI contact info@mpc-sintfranciscus.be",
        "url": "https://mpc-sintfranciscus.be/",
        "publisher": "MPC Sint-Franciscus vzw",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; VAPH disability residential care Roosdaal+Brussels belt; "
            "FOI info@mpc-sintfranciscus.be; tel 053/64.66.66"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "MPC Sint-Franciscus (Roosdaal / mentale handicap)",
        "name_fr": "MPC Saint-François (Roosdaal / handicap mental)",
        "name_en": "MPC Sint-Franciscus VZW (Roosdaal; residential care mental disability)",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://mpc-sintfranciscus.be/",
        "foi_email": "info@mpc-sintfranciscus.be",
        "foi_postal": "Lostraat 175, 1760 Roosdaal",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW 8 VE NACE 87.201; "
            f"omzet JUMP 2.01m ({OMZET_YOY}) bruto JUMP 29.41m ({BRUTO_YOY}) pnl DROP 1.17m ({PNL_YOY}) "
            f"equity JUMP 16.54m ({EQUITY_YOY}) FTE JUMP {FTE} (vs {FTE_PRIOR}); assets/debt Unknown; "
            f"filed 16.06.2026; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "DISTINCT Château Vert / Zorghome De Fakkel / Begralim Tongeren campus"
        ),
    },
)

for bid, amt, basis in [
    ("bud_mpc_sf_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin (primary envelope)"),
    ("bud_mpc_sf_omzet_jr2025_statutory", OMZET, "CW YE2025 omzet / Turnover (partial vs bruto)"),
    ("bud_mpc_sf_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss"),
    ("bud_mpc_sf_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
    ("bud_mpc_sf_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
]:
    append_csv(
        DATA / "budgets.csv",
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": amt,
            "amount_min_eur": amt,
            "amount_max_eur": amt,
            "basis": basis,
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; assets/debt Unknown pending NBB PDF",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "MPC Sint-Franciscus YE2025 leftover dual (bruto JUMP 29.41m / pnl DROP)",
        "entity_id": ENTITY,
        "beneficiary": "Minors/adults with mental disability (VAPH-path; 8 VE Roosdaal+Brussels)",
        "legal_basis": f"VZW MPC residential care (KBO {KBO}; NACE 87.201; 8 VE; aanbestedende overheid)",
        "decision_date": "2026-06-16",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": BRUTO,
        "cash_by_year": (
            f'{{"2025_bruto":{BRUTO},"2025_omzet":{OMZET},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_bruto":{BRUTO_PRIOR},'
            f'"2024_pnl":{PNL_PRIOR},"2024_fte":{FTE_PRIOR}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/medisch-pedagogisch-centrum-sint-franciscus",
        "stated_goal": "Public-interest residential care for persons with mental disability (VAPH)",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; map VAPH vs omzet 2.01m vs bruto 29.41m; "
            "explain pnl DROP −22% with FTE JUMP"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>VlaamsBrabant>Roosdaal>MPC_SintFranciscus>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT Château Vert / Zorghome De Fakkel"
        ),
    },
)

# pi ≈ 0.55*6.6 + 0.35*6.2 + 0.10*6.5 ≈ 3.63+2.17+0.65 = 6.45 → 6.4
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "MPC Sint-Franciscus bruto JUMP 29.41m / pnl DROP −22% / FTE JUMP (YE2025)",
        "level": "L5",
        "type": "disability_care_vzw",
        "hierarchy_path": "Vlaanderen>VlaamsBrabant>Roosdaal>MPC_SintFranciscus>JR2025",
        "annual_cost_eur": BRUTO,
        "total_cost_eur": BRUTO,
        "tco_notes": (
            f"CW YE2025 bruto {BRUTO} JUMP {BRUTO_YOY} (primary); omzet {OMZET} JUMP {OMZET_YOY}; "
            f"pnl {PNL} DROP {PNL_YOY}; equity {EQUITY} JUMP {EQUITY_YOY}; FTE {FTE} JUMP vs {FTE_PRIOR}; "
            "assets/debt Unknown pending NBB PDF; VAPH disability residential care 8 VE"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "Persons with mental disability (VAPH-path Roosdaal+Brussels)",
        "stated_goal": "Public-interest disability residential care",
        "measured_outcome": (
            f"bruto JUMP {BRUTO_YOY}; omzet JUMP {OMZET_YOY}; pnl DROP {PNL_YOY}; "
            f"equity JUMP {EQUITY_YOY}; FTE JUMP {FTE_PRIOR}→{FTE}"
        ),
        "absurdity_score": "6.6",
        "cost_score": "6.2",
        "difficulty": "3.5",
        "priority_index": "6.4",
        "cut_proposal": (
            "FOI NBB PDF + VAPH vs omzet/bruto split; explain pnl DROP with FTE JUMP; publish 8 VE matrix"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
            "DISTINCT Château Vert / Zorghome De Fakkel / Begralim Tongeren"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>VlaamsBrabant>Roosdaal>MPC_SintFranciscus>NBB_PDF_assets_debt_pnl_drop_bruto",
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); VAPH vs omzet 2.01m vs bruto 29.41m split; "
            "pnl DROP −22% path at FTE JUMP; 8 VE address/revenue matrix"
        ),
        "why_it_matters": (
            "Medium CW shows VAPH disability-care VZW (aanbestedende overheid) with bruto 29.41m and pnl DROP "
            "−22% while assets/debt opaque and omzet only 2.01m — subsidy/care-margin transparency gap"
        ),
        "priority": "8",
        "recipient_body": "MPC Sint-Franciscus vzw",
        "recipient_email": "info@mpc-sintfranciscus.be",
        "recipient_postal": "Lostraat 175, 1760 Roosdaal",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-25",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2130",
    },
)

with open(DATA / "loop_state.csv", newline="", encoding="utf-8") as f:
    fields = csv.DictReader(f).fieldnames
with open(DATA / "loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": RQ,
            "ticks_completed": str(TICK),
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover MPC Sint-Franciscus {KBO} Medium CW (bruto JUMP 29.41m pnl DROP 1.17m "
                f"equity JUMP 16.54m omzet JUMP 2.01m FTE JUMP 365.1; assets/debt Unknown; 8 VE NACE 87.201 "
                f"Roosdaal VAPH disability care); AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Fakkel taken; "
                f"next {NEXT_RQ} EVERY-10; next every-10 2130; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} MPC Sint-Franciscus Roosdaal (bruto JUMP 29.41m / pnl DROP −22% / Medium)

- Unit: **{RQ}** leftover dual after **rq_2128 Zorghome De Fakkel** (race: concurrent took 2128). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **MPC Sint-Franciscus VZW** YE2025 (KBO **{KBO}**; Lostraat 175 Roosdaal; **VZW** NACE **87.201** / **8 VE**; VAPH disability residential; aanbestedende overheid). Do not redo De Fakkel/Château Vert/SLG Wallonie/Famifamenne/PC Gent-Sleidinge/Begralim Tongeren campus.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY} (primary); pnl **EUR{PNL}** DROP {PNL_YOY}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}** JUMP vs {FTE_PRIOR}; neerlegging **16.06.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info@mpc-sintfranciscus.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.4); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open EVERY-10; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2128/mpc_*.html.
- FOI: **ready not sent** (human-gated).
- NOT every-10 this tick (**next {NEXT_RQ}=2130 EVERY-10**). Next: {NEXT_RQ} (progress+top10 + AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
    )

print("OK tick", TICK, ENTITY, "bruto", BRUTO)
