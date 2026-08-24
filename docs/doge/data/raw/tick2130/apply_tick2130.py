# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T13:30:00Z"
TICK = 2130
RQ = "rq_2130"
NEXT_RQ = "rq_2131"
ENTITY = "bv_care_support_houthalen"
GAP = "gap_care_support_nbb_pdf_assets_debt_omzet_empty_pnl_jump_matrix_l5"
COMM = "comm_care_support_jr2025_statutory_thuiszorg"
LB = "lb_care_support_bruto_jump_1_85m_pnl_jump_jr2025"
SRC_EN = "src_care_support_jr2025_cw_en"
KBO = "0827.850.260"
KBO_DIGITS = "0827850260"
BRUTO = "1852254"
BRUTO_PRIOR = "1372032"
BRUTO_YOY = "+35%"
PNL = "1091779"
PNL_PRIOR = "831816"
PNL_YOY = "+31.25%"
EQUITY = "2995724"
EQUITY_PRIOR = "1903944"
EQUITY_YOY = "+57.34%"
FTE = "1"
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
            r["title"] = "EVERY-10 + leftover dual — Care-Support YE2025 Medium"
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} EVERY-10 Care-Support Medium bruto JUMP 1.85m pnl JUMP 1.09m equity JUMP 3.00m "
                f"omzet unpublished FTE 1; FOI ready; progress+top10 refreshed; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2140"
            )
            r["instructions"] = (
                f"Completed EVERY-10 progress+top10 + leftover dual Care-Support after MPC Sint-Franciscus; "
                f"preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} omzet unpublished FTE {FTE}; FOI {GAP}"
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
                    "leftover dual hole-fill after Care-Support — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Care-Support YE2025 Medium EVERY-10. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/"
                    "hospital/WZC/psych/MRS/creche/disability/thuiszorg. Do NOT redo Care-Support, MPC Sint-Franciscus, "
                    "Zorghome De Fakkel, Le Château Vert, SLG Wallonie, Famifamenne, Residence Le Castel, R.S.W., "
                    "Home Sebrechts, Unite Jolimont, t Buurthuis, Le Bosquet, Strebo, Entraide, La Charmille, Charmilles, "
                    "Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, Sint-Camillus, "
                    "IDELUX*, INTRADEL, Korian*, SLG Operaties VL, SLG Vlaanderen VZW, Always Home, AREWAL, AGB Bornem, "
                    "Armonea holding, emeis holding, Restel Flats (YE2024)."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} EVERY-10 Care-Support; FARO/AIESH/REW still YE2024; next every-10 2140"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_care_support_jr2025_cw",
        "title": "Companyweb NL Care-Support YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet unpublished bruto JUMP {BRUTO} ({BRUTO_YOY}) pnl JUMP {PNL} ({PNL_YOY}) "
            f"equity JUMP {EQUITY} ({EQUITY_YOY}) FTE {FTE}; neerlegging 05.02.2026; assets/debt Unknown; "
            f"raw docs/doge/data/raw/tick2130/care_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Care-Support YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/care-support",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 05-02-2026; Last balance sheet year 2025; "
            f"Turnover unpublished; Gross margin {BRUTO}; FTE {FTE}; Principal activity social work / "
            f"elderly home care; raw docs/doge/data/raw/tick2130/care_en.html"
        ),
    },
    {
        "source_id": "src_care_support_jr2025_cw_fr",
        "title": "Companyweb FR Care-Support YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2130/care_fr.html",
    },
    {
        "source_id": f"src_care_support_kbo_{TICK}",
        "title": f"KBO Care-Support {KBO} Actief Houthalen-Helchteren",
        "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Actief BV/SRL; Weygaardstraat 26 3530 Houthalen-Helchteren; 2 VE; "
            "RSZ NACE 88.101 elderly home care; bestuurders Pluymers Robert/Stef/Stijn"
        ),
    },
    {
        "source_id": f"src_care_support_site_{TICK}",
        "title": "Care-Support site FOI contact info@care-support.be",
        "url": "https://www.care-support.be/",
        "publisher": "Care-Support SRL",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": f"tick{TICK}; thuiszorg / elderly home-care SRL; FOI info@care-support.be",
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Care-Support (Houthalen-Helchteren / thuiszorg)",
        "name_fr": "Care-Support SRL (Houthalen / soins à domicile aînés)",
        "name_en": "Care-Support SRL (Houthalen; elderly home care)",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.care-support.be/",
        "foi_email": "info@care-support.be",
        "foi_postal": "Weygaardstraat 26, 3530 Houthalen-Helchteren",
        "notes": (
            f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief BV/SRL 2 VE NACE 88.101; "
            f"omzet unpublished bruto JUMP 1.85m ({BRUTO_YOY}) pnl JUMP 1.09m ({PNL_YOY}) equity JUMP 3.00m "
            f"({EQUITY_YOY}) FTE {FTE}; assets/debt Unknown; filed 05.02.2026; FOI {GAP}; "
            "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT MPC Sint-Franciscus / De Fakkel"
        ),
    },
)

for bid, amt, basis in [
    ("bud_care_support_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin (primary; omzet unpublished)"),
    ("bud_care_support_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss"),
    ("bud_care_support_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
    ("bud_care_support_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
            "notes": f"tick{TICK}; Medium CW; omzet unpublished; assets/debt Unknown pending NBB PDF",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Care-Support YE2025 leftover dual EVERY-10 (bruto JUMP 1.85m / pnl JUMP)",
        "entity_id": ENTITY,
        "beneficiary": "Elderly home-care users (2 VE Houthalen-Helchteren)",
        "legal_basis": f"BV/SRL thuiszorg (KBO {KBO}; NACE 88.101; 2 VE)",
        "decision_date": "2026-02-05",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": BRUTO,
        "cash_by_year": (
            f'{{"2025_bruto":{BRUTO},"2025_omzet":"unpublished","2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_bruto":{BRUTO_PRIOR},'
            f'"2024_pnl":{PNL_PRIOR}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/care-support",
        "stated_goal": "Elderly home care without nursing (thuiszorg)",
        "cut_option": (
            "Publish NBB PDF assets/debt + omzet FOI; explain pnl 1.09m on FTE 1 / related-party path"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Limburg>Houthalen>CareSupport>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK} EVERY-10; Medium CW; bruto primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT MPC Sint-Franciscus / De Fakkel / Restel Flats YE2024"
        ),
    },
)

# pi ≈ 0.55*6.5 + 0.35*3.5 + 0.10*6.5 ≈ 3.575+1.225+0.65 = 5.45 → 5.5
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "Care-Support bruto JUMP 1.85m / pnl JUMP 1.09m / FTE 1 (YE2025)",
        "level": "L5",
        "type": "thuiszorg_srl",
        "hierarchy_path": "Vlaanderen>Limburg>Houthalen>CareSupport>JR2025",
        "annual_cost_eur": BRUTO,
        "total_cost_eur": BRUTO,
        "tco_notes": (
            f"CW YE2025 bruto {BRUTO} JUMP {BRUTO_YOY} (primary; omzet unpublished); "
            f"pnl {PNL} JUMP {PNL_YOY}; equity {EQUITY} JUMP {EQUITY_YOY}; FTE {FTE}; "
            "assets/debt Unknown pending NBB PDF; thuiszorg NACE 88.101"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "Elderly home-care users (Houthalen-Helchteren)",
        "stated_goal": "Elderly home care without nursing",
        "measured_outcome": (
            f"bruto JUMP {BRUTO_YOY}; pnl JUMP {PNL_YOY}; equity JUMP {EQUITY_YOY}; "
            f"omzet unpublished; FTE {FTE}"
        ),
        "absurdity_score": "6.5",
        "cost_score": "3.5",
        "difficulty": "3.5",
        "priority_index": "5.5",
        "cut_proposal": (
            "FOI NBB PDF + omzet disclosure; explain pnl ~1.09m on 1 FTE / related-party fees"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} EVERY-10; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
            "DISTINCT MPC Sint-Franciscus / De Fakkel"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Limburg>Houthalen>CareSupport>NBB_PDF_assets_debt_omzet_empty_pnl_jump",
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); omzet/code70 unpublished; "
            "pnl JUMP 1.09m on FTE 1 related-party/fee path; 2 VE activity matrix"
        ),
        "why_it_matters": (
            "Medium CW shows thuiszorg SRL with bruto 1.85m and pnl JUMP 1.09m at FTE 1 while omzet "
            "and assets/debt opaque — margin / related-party transparency gap"
        ),
        "priority": "8",
        "recipient_body": "Care-Support SRL",
        "recipient_email": "info@care-support.be",
        "recipient_postal": "Weygaardstraat 26, 3530 Houthalen-Helchteren",
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
        "notes": f"tick{TICK} EVERY-10; human-send only; Medium CW; next every-10 2140",
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
                f"tick{TICK} EVERY-10 leftover Care-Support {KBO} Medium CW (bruto JUMP 1.85m pnl JUMP 1.09m "
                f"equity JUMP 3.00m omzet unpublished FTE 1; assets/debt Unknown; 2 VE NACE 88.101 "
                f"Houthalen thuiszorg) + progress/top10 refresh; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"MPC Sint-Franciscus taken; Restel Flats YE2024 deferred; next {NEXT_RQ}; next every-10 2140; "
                f"continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} EVERY-10 Care-Support Houthalen (bruto JUMP 1.85m / pnl JUMP 1.09m / Medium)

- Unit: **{RQ}** EVERY-10 + leftover dual after **rq_2129 MPC Sint-Franciscus**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Restel Flats still **YE2024**. Took unused leftover **Care-Support SRL** YE2025 (KBO **{KBO}**; Weygaardstraat 26 Houthalen-Helchteren; **BV/SRL** NACE **88.101** / **2 VE**; thuiszorg). Do not redo MPC Sint-Franciscus/De Fakkel/Château Vert/SLG Wallonie/Famifamenne.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** JUMP {PNL_YOY}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}**; neerlegging **05.02.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info@care-support.be.
- Wrote: sources (+5); budgets (+4); commitments (+1); leaderboard (+1 pi 5.5); entities (+1 {ENTITY}); foi + draft {GAP}; progress_every_10_ticks.md + doge_waste_top10_current.md refreshed; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2130/.
- FOI: **ready not sent** (human-gated).
- **EVERY-10@2130** (last was 2120; **next 2140**). Pure annual top10 stable (GIP/fossil/cars/cheque). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, "EVERY-10", ENTITY, "bruto", BRUTO)
