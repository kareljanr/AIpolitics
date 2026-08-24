# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T12:40:00Z"
TICK = 2127
RQ = "rq_2127"
NEXT_RQ = "rq_2128"
ENTITY = "asbl_le_chateau_vert_huy"
GAP = "gap_chateau_vert_nbb_pdf_assets_debt_omzet_empty_pnl_jump_matrix_l5"
COMM = "comm_chateau_vert_jr2025_statutory_disability_care"
LB = "lb_chateau_vert_bruto_jump_8_00m_pnl_jump_jr2025"
SRC_EN = "src_chateau_vert_jr2025_cw_en"
KBO = "0448.033.201"
KBO_DIGITS = "0448033201"
BRUTO = "7999317"
BRUTO_PRIOR = "7814110"
BRUTO_YOY = "+2.37%"
PNL = "94047"
PNL_PRIOR = "13740"
PNL_YOY = "+584.48%"
EQUITY = "4676318"
EQUITY_PRIOR = "4450476"
EQUITY_YOY = "+5.07%"
FTE = "111.5"
FTE_PRIOR = "111.3"
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
            r["title"] = "leftover dual — Le Château Vert Huy YE2025 Medium"
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Le Château Vert Medium bruto JUMP 8.00m pnl JUMP 94k equity JUMP 4.68m "
                f"omzet unpublished FTE 111.5; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2130"
            )
            r["instructions"] = (
                f"Completed leftover dual Le Château Vert after SLG Wallonie; preferred AGB Bornem JR2024 / "
                f"FARO/AIESH/REW YE2024; live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
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
                    "leftover dual hole-fill after Château Vert — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Le Château Vert YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/"
                    "hospital/WZC/psych/MRS/creche/disability-care. Do NOT redo Le Château Vert, SLG Wallonie, "
                    "Famifamenne, Residence Le Castel, R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, "
                    "Le Bosquet, Strebo, Entraide, La Charmille, Charmilles, Sittelles, Les Buissons, Residence 3, "
                    "Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, Sint-Camillus, IDELUX*, INTRADEL, "
                    "Korian Belgium holding, SLG Operaties Vlaanderen, SLG Vlaanderen VZW, Always Home, AREWAL, "
                    "AGB Bornem, Armonea holding, emeis holding."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Château Vert fill; FARO/AIESH/REW still YE2024; next every-10 2130"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_chateau_vert_jr2025_cw",
        "title": "Companyweb NL Le Château Vert YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet unpublished bruto JUMP {BRUTO} ({BRUTO_YOY}) pnl JUMP {PNL} ({PNL_YOY}) "
            f"equity JUMP {EQUITY} ({EQUITY_YOY}) FTE {FTE}; neerlegging 08.07.2026; assets/debt Unknown; "
            f"raw docs/doge/data/raw/tick2127/chateau_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Le Château Vert YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/le-chateau-vert",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 08-07-2026; Last balance sheet year 2025; "
            f"Turnover unpublished; Gross margin {BRUTO}; FTE {FTE}; Principal activity residential care "
            f"minors motor disabilities; raw docs/doge/data/raw/tick2127/chateau_en.html"
        ),
    },
    {
        "source_id": "src_chateau_vert_jr2025_cw_fr",
        "title": "Companyweb FR Le Château Vert YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2127/chateau_fr.html",
    },
    {
        "source_id": f"src_chateau_vert_kbo_{TICK}",
        "title": f"KBO Le Château Vert {KBO} Actief Huy",
        "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Actief ASBL CHATEAU VERT; Chemin de Perwez 16 4500 Huy; 2 VE; "
            "RSZ NACE 87.303 residential care minors motor disabilities; bestuurders Colemans Didier + Debaty Veronique"
        ),
    },
    {
        "source_id": f"src_chateau_vert_site_{TICK}",
        "title": "Le Château Vert site FOI contact info@chateauvert.be",
        "url": "https://chateauvert.be/",
        "publisher": "ASBL Le Château Vert",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": f"tick{TICK}; AViQ-path disability residential care Huy; FOI info@chateauvert.be",
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Le Château Vert (Huy / handicap-residentieel)",
        "name_fr": "ASBL Le Château Vert (Huy / hébergement handicap moteur)",
        "name_en": "Le Château Vert ASBL (Huy; residential care motor disabilities)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://chateauvert.be/",
        "foi_email": "info@chateauvert.be",
        "foi_postal": "Chemin de Perwez 16, 4500 Huy",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief ASBL 2 VE NACE 87.303; "
            f"omzet unpublished bruto JUMP 8.00m ({BRUTO_YOY}) pnl JUMP 94k ({PNL_YOY}) equity JUMP 4.68m "
            f"({EQUITY_YOY}) FTE {FTE}; assets/debt Unknown; filed 08.07.2026; FOI {GAP}; "
            "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT SLG Wallonie / Jolimont / HELORA"
        ),
    },
)

for bid, amt, basis in [
    ("bud_chateau_vert_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin (primary; omzet unpublished)"),
    ("bud_chateau_vert_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss"),
    ("bud_chateau_vert_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
    ("bud_chateau_vert_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
        "title": "Le Château Vert YE2025 leftover dual (bruto JUMP 8.00m / pnl JUMP / omzet empty)",
        "entity_id": ENTITY,
        "beneficiary": "Minors/adults with motor disabilities (AViQ-path; 2 VE Huy)",
        "legal_basis": f"ASBL hébergement handicap (KBO {KBO}; NACE 87.303; 2 VE)",
        "decision_date": "2026-07-08",
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
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/le-chateau-vert",
        "stated_goal": "Public-interest residential care for persons with motor disabilities (AViQ)",
        "cut_option": (
            "Publish NBB PDF assets/debt + omzet FOI; explain pnl JUMP +584% with flat FTE; "
            "map AViQ points vs other receipts"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Liege>Huy>ChateauVert>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope (omzet unpublished); assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT SLG Wallonie"
        ),
    },
)

# pi ≈ 0.55*6.2 + 0.35*4.8 + 0.10*6.5 ≈ 3.41+1.68+0.65 = 5.74 → round 5.8
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "Le Château Vert bruto JUMP 8.00m / pnl JUMP +584% / omzet empty (YE2025)",
        "level": "L5",
        "type": "disability_care_asbl",
        "hierarchy_path": "Wallonie>Liege>Huy>ChateauVert>JR2025",
        "annual_cost_eur": BRUTO,
        "total_cost_eur": BRUTO,
        "tco_notes": (
            f"CW YE2025 bruto {BRUTO} JUMP {BRUTO_YOY} (primary; omzet unpublished); "
            f"pnl {PNL} JUMP {PNL_YOY}; equity {EQUITY} JUMP {EQUITY_YOY}; FTE {FTE}; "
            "assets/debt Unknown pending NBB PDF; AViQ disability residential care"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "Persons with motor disabilities (AViQ-path Huy)",
        "stated_goal": "Public-interest disability residential care",
        "measured_outcome": (
            f"bruto JUMP {BRUTO_YOY}; pnl JUMP {PNL_YOY}; equity JUMP {EQUITY_YOY}; "
            f"omzet unpublished; FTE flat {FTE_PRIOR}→{FTE}"
        ),
        "absurdity_score": "6.2",
        "cost_score": "4.8",
        "difficulty": "3.5",
        "priority_index": "5.8",
        "cut_proposal": (
            "FOI NBB PDF + omzet disclosure + AViQ vs other receipts; explain pnl JUMP at flat FTE"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
            "DISTINCT SLG Wallonie / Jolimont / HELORA"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>Liege>Huy>ChateauVert>NBB_PDF_assets_debt_omzet_empty_pnl_jump",
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); omzet/code70 unpublished; "
            "AViQ points vs other receipts; pnl JUMP +584% path at flat FTE"
        ),
        "why_it_matters": (
            "Medium CW shows Walloon AViQ disability-care ASBL with bruto 8.00m and pnl JUMP +584% "
            "while omzet and assets/debt opaque — subsidy/care-margin transparency gap"
        ),
        "priority": "8",
        "recipient_body": "ASBL Le Château Vert",
        "recipient_email": "info@chateauvert.be",
        "recipient_postal": "Chemin de Perwez 16, 4500 Huy",
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
                f"tick{TICK} leftover Le Château Vert {KBO} Medium CW (bruto JUMP 8.00m pnl JUMP 94k "
                f"equity JUMP 4.68m omzet unpublished FTE 111.5; assets/debt Unknown; 2 VE NACE 87.303 Huy "
                f"AViQ disability care); AGB Bornem JR2024; FARO/AIESH/REW YE2024; SLG Wallonie taken; "
                f"next {NEXT_RQ}; next every-10 2130; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Le Château Vert Huy (bruto JUMP 8.00m / pnl JUMP +584% / omzet empty / Medium)

- Unit: **{RQ}** leftover dual after **rq_2126 SLG Wallonie**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Le Château Vert ASBL** YE2025 (KBO **{KBO}**; Chemin de Perwez 16 Huy; **ASBL** NACE **87.303** / **2 VE**; AViQ disability residential care). Do not redo SLG Wallonie/Famifamenne/Le Castel/RSW/Sebrechts/Jolimont continuum.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** JUMP {PNL_YOY}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}**; neerlegging **08.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info@chateauvert.be.
- Wrote: sources (+5); budgets (+4); commitments (+1); leaderboard (+1 pi 5.8); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2127/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2120**; next **2130**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "bruto", BRUTO)
