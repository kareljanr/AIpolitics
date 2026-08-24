# tick2202 writer — Aarova YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T13:20:00Z"
TICK = "2202"
ENTITY = "vzw_aarova_oudenaarde"
SRC_EN = "src_aarova_jr2025_cw_en"
COMM = "comm_aarova_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_loss"
LB = "lb_aarova_omzet_5_62m_bruto_gt_omzet_pnl_loss_jr2025"
GAP = "gap_aarova_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_loss_matrix_l5"

OMZET = 5621617
BRUTO = 11761773
PNL = -139353
EQUITY = 2474538
FTE = 306.2
OMZET24 = 5347759
BRUTO24 = 11804879
PNL24 = -212418
EQUITY24 = 2649644
FTE24 = 302.7
ENVELOPE = OMZET


def append_csv(path, rows):
    path = ROOT / path
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = r.fieldnames
    key = list(rows[0].keys())[0]
    for row in rows:
        if any(e.get(key) == row.get(key) for e in existing):
            print("SKIP", row.get(key))
            return False
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
        for row in rows:
            w.writerow({c: row.get(c, "") for c in cols})
    print("APPENDED", path.name, len(rows))
    return True


append_csv(
    "sources.csv",
    [
        {
            "source_id": "src_aarova_jr2025_cw_nl",
            "title": "Companyweb NL Aarova YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0451263992/aarova",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl LOSS {PNL} equity DROP {EQUITY} FTE {FTE}; neerlegging 30.04.2026; raw docs/doge/data/raw/tick2202/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Aarova YE2025 statutory",
            "url": "https://www.companyweb.be/en/0451263992/aarova",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 30-04-2026; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} Employees {FTE}",
        },
        {
            "source_id": "src_aarova_jr2025_cw_fr",
            "title": "Companyweb FR Aarova YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0451263992/aarova",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; CA {OMZET}",
        },
        {
            "source_id": "src_aarova_kbo_2202",
            "title": "KBO Aarova 0451.263.992 Actief VZW 6 VE Oudenaarde",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=451263992",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2202; Actief VZW; Industriepark De Bruwaan 85 9700 Oudenaarde; 6 VE; RSZ NACE 88.993; BTW 18.120/56.111/14.210; dagelijks bestuur De Vleeschouwer Ellen sinds 01.07.2025",
        },
        {
            "source_id": "src_aarova_foi_contact_2202",
            "title": "Aarova FOI channel info@aarova.be",
            "url": "https://www.aarova.be/",
            "publisher": "Aarova VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2202; info@aarova.be / privacy@aarova.be; Industriepark De Bruwaan 85 9700 Oudenaarde; 055 31 13 45",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_aarova_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +5.12% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_aarova_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025 (bruto≫omzet ~2.09x)",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto DROP -0.37% vs YE2024 {BRUTO24}; bruto≫omzet",
        },
        {
            "budget_id": "bud_aarova_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl LOSS IMPROVE +34.4% vs YE2024 {PNL24} (still negative)",
        },
        {
            "budget_id": "bud_aarova_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity DROP -6.61% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_aarova_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW social-balance FTE / Employees {FTE}",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; FTE JUMP vs YE2024 {FTE24}; assets/debt Unknown",
        },
    ],
)

cash = {
    "2025_omzet": OMZET,
    "2025_bruto": BRUTO,
    "2025_pnl": PNL,
    "2025_equity": EQUITY,
    "2025_fte": FTE,
    "2024_omzet": OMZET24,
    "2024_bruto": BRUTO24,
    "2024_pnl": PNL24,
    "2024_equity": EQUITY24,
    "2024_fte": FTE24,
}

append_csv(
    "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": "Aarova YE2025 leftover dual (omzet JUMP 5.62m / bruto≫omzet ~2.09x / pnl LOSS -139k)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Oudenaarde Vlaamse Ardennen",
            "legal_basis": "VZW maatwerk (KBO 0451.263.992; Actief; 6 VE; RSZ NACE 88.993)",
            "decision_date": "2026-04-30",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(ENVELOPE),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0451263992/aarova",
            "stated_goal": "Sheltered employment / maatwerk Oudenaarde",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose bruto≫omzet ~2.09x + multi-year pnl LOSS subsidy matrix",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Oudenaarde>Aarova>JR2025_statutory_L5",
            "notes": "tick2202; Medium CW; omzet primary envelope; bruto≫omzet ~2.09x + pnl LOSS while FTE JUMP primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Aarova omzet JUMP 5.62m / bruto≫omzet ~2.09x / pnl LOSS -139k (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Oudenaarde>Aarova>JR2025",
            "annual_cost_eur": str(ENVELOPE),
            "total_cost_eur": str(ENVELOPE),
            "tco_notes": "CW omzet JUMP envelope 5.62m / bruto 11.76m ≫omzet ~2.09x / pnl LOSS -139k improve from YE2024 -212k / equity DROP 2.47m / FTE JUMP 306.2; VL maatwerk Oudenaarde; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Oudenaarde / VDAB-ESF path / commercial clients",
            "stated_goal": "Sheltered employment maatwerk Oudenaarde",
            "measured_outcome": "omzet JUMP +5.1%; bruto≫omzet ~2.09x; pnl LOSS improve 34%; equity DROP -6.6%; FTE JUMP +1.2%",
            "absurdity_score": "7.6",
            "cost_score": "5.1",
            "difficulty": "3.0",
            "priority_index": "6.8",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet + multi-year LOSS path; VDAB/ESF/gemeente subsidy split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK} primary; Medium CW; FOI {GAP}; stall FARO YE2024; VL maatwerk dual after MWP/De Winning",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Aarova VZW (maatwerk / Oudenaarde)",
            "name_fr": "Aarova ASBL (entreprise de travail adapté / Audenarde)",
            "name_en": "Aarova sheltered workshop (Oudenaarde)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.aarova.be/",
            "foi_email": "info@aarova.be",
            "foi_postal": "Industriepark De Bruwaan 85, 9700 Oudenaarde",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0451.263.992 Actief VZW 6 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO}≫omzet pnl LOSS {PNL} vs YE2024 {PNL24} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 30.04.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Oudenaarde>Aarova>NBB_PDF_assets_debt_bruto_gt_omzet",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} vs omzet EUR{OMZET} (~2.09x); pnl LOSS EUR{PNL} vs YE2024 EUR{PNL24} (improve 34% still negative); FTE JUMP {FTE24}->{FTE}; VDAB/ESF/gemeente/provincie subsidy matrix",
            "why_it_matters": "Medium CW shows VL maatwerk VZW with bruto≫omzet ~2.09x and multi-year pnl LOSS while FTE JUMP — public subsidy path opaque",
            "priority": "8",
            "recipient_body": "Aarova VZW",
            "recipient_email": "info@aarova.be",
            "recipient_postal": "Industriepark De Bruwaan 85, 9700 Oudenaarde",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-26",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": COMM,
            "linked_leaderboard_id": LB,
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; next every-10 2210",
        }
    ],
)

rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)

found = False
for row in rows:
    if row.get("task_id") == "rq_2202":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["blocked_gap_id"] = GAP
        row["title"] = (
            "leftover dual — Aarova YE2025 Medium (omzet JUMP 5.62m / bruto≫omzet ~2.09x / pnl LOSS -139k)"
        )
        row["notes"] = (
            "tick2202; Aarova 0451.263.992 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "next rq_2203; every-10 next 2210"
        )
        row["instructions"] = (
            "Tick 2202 after concurrent tick2201 race MWP Pajottenland + De Winning. Prefer leftover AGB/APB if JR2025 PDF live, "
            "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
            "(Aarova 0451.263.992 YE2025 FREE taken). Do NOT redo MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, "
            "BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, "
            "Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
            "WAAK SW, Waak, Stijn, Stroom, Springplank."
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2202 missing")

if not any(r.get("task_id") == "rq_2203" for r in rows):
    rows.append(
        {
            "task_id": "rq_2203",
            "title": "leftover dual hole-fill after Aarova — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2203 after Aarova YE2025 Medium (omzet JUMP 5.62m / bruto≫omzet ~2.09x / pnl LOSS -139k / FTE JUMP). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(FREE: Kaliber YE2024-only stall / Oesterbank/Werkhuizen MIN/Trianval/Noordheuvel/Arcor/ACG/Entiris/Odas/Kemphaan/…). "
                "Do NOT redo Aarova, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, "
                "A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, "
                "Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, "
                "Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2202 Aarova; FARO still YE2024; next every-10 2210",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2202=done rq_2203=open")

ls_path = ROOT / "loop_state.csv"
with ls_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)
rows[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": UTC,
    "last_unit_id": "rq_2202",
    "ticks_completed": "2202",
    "paused": "no",
    "notes": (
        "tick2202 leftover Aarova 0451.263.992 Medium (omzet JUMP 5.62m; bruto≫omzet ~2.09x 11.76m; "
        "pnl LOSS -139k improve 34%; equity DROP 2.47m; FTE JUMP 306.2; 6 VE Oudenaarde); AGB Bornem JR2024; FARO YE2024; "
        "next rq_2203; next every-10 2210; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2202 DONE")
