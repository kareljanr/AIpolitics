# tick2201 writer — De Winning Maatwerk Lummen YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T13:00:00Z"
TICK = "2201"
ENTITY = "vzw_de_winning_maatwerk_lummen"
SRC_EN = "src_de_winning_jr2025_cw_en"
COMM = "comm_de_winning_jr2025_statutory_maatwerk_equity_jump_pnl_jump_bruto_gt_omzet"
LB = "lb_de_winning_omzet_7_96m_equity_jump_87pct_pnl_jump_jr2025"
GAP = "gap_de_winning_nbb_pdf_assets_debt_equity_jump_pnl_jump_bruto_gt_omzet_matrix_l5"

OMZET = 7961603
BRUTO = 11461879
PNL = 1762111
EQUITY = 3585952
FTE = 281.5
OMZET24 = 6265903
BRUTO24 = 10339007
PNL24 = 843942
EQUITY24 = 1918075
FTE24 = 280.3
RATIO = round(BRUTO / OMZET, 2)


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
            "source_id": "src_de_winning_jr2025_cw_nl",
            "title": "Companyweb NL De Winning Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0465903173/de-winning-maatwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 25.06.2026; raw docs/doge/data/raw/tick2201/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN De Winning Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/en/0465903173/de-winning-maatwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 25-06-2026; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_de_winning_jr2025_cw_fr",
            "title": "Companyweb FR De Winning Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0465903173/de-winning-maatwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_de_winning_kbo_2201",
            "title": "KBO De Winning Maatwerk 0465.903.173 Actief VZW 5 VE Lummen",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0465903173",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2201; Actief VZW; St.-Ferdinandstraat 1 3560 Lummen; 5 VE; RSZ NACE 88.993; BTW 01.500/56.111/88.993",
        },
        {
            "source_id": "src_de_winning_foi_contact_2201",
            "title": "De Winning FOI channel info@dewinning.be",
            "url": "https://www.dewinning.be/contact",
            "publisher": "De Winning Maatwerk VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2201; info@dewinning.be; +32 13 531 159; St.-Ferdinandstraat 1 3560 Lummen",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_de_winning_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +27.06% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_de_winning_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +10.86% vs YE2024 {BRUTO24}; bruto≫omzet (~{RATIO}x)",
        },
        {
            "budget_id": "bud_de_winning_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl JUMP +108.8% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_de_winning_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +86.96% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_de_winning_fte_jr2025_statutory",
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
            "title": f"De Winning Maatwerk Lummen YE2025 leftover dual (omzet JUMP 7.96m / equity JUMP +87% / pnl JUMP +109% / bruto≫omzet ~{RATIO}x)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / green-farming-horeca clients Limburg Lummen",
            "legal_basis": "VZW maatwerk (KBO 0465.903.173; Actief; 5 VE; RSZ NACE 88.993; BTW farming/horeca)",
            "decision_date": "2026-06-25",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0465903173/de-winning-maatwerk",
            "stated_goal": "Sheltered employment / inclusive green + catering maatwerk",
            "cut_option": f"Publish NBB PDF assets/debt FOI; disclose equity JUMP +87% and bruto~{RATIO}x omzet loonkost matrix",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Limburg>Lummen>DeWinning>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; omzet primary envelope; equity JUMP +87% + pnl JUMP +109% + bruto≫omzet primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": f"De Winning omzet JUMP 7.96m / equity JUMP +87% / pnl JUMP +109% / bruto≫omzet ~{RATIO}x (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Limburg>Lummen>DeWinning>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": f"CW omzet JUMP envelope 7.96m / bruto 11.46m ≫ omzet (~{RATIO}x) / pnl JUMP 1.76m +109% / equity JUMP 3.59m +87% / FTE 281.5; Limburg maatwerk+farming; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Lummen / public loonkost path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +27.1%; bruto JUMP +10.9%; pnl JUMP +108.8%; equity JUMP +87.0%; FTE JUMP +0.4%",
            "absurdity_score": "7.6",
            "cost_score": "5.2",
            "difficulty": "3.0",
            "priority_index": "6.9",
            "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose equity JUMP +87% path + bruto~{RATIO}x omzet loonkost/GESCO/ESF split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/REW YE2024; Limburg maatwerk dual after AGE/Groep Talent/Bewel",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "De Winning Maatwerk VZW (Lummen)",
            "name_fr": "De Winning Maatwerk ASBL (Lummen)",
            "name_en": "De Winning sheltered workshop non-profit (Lummen)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.dewinning.be/",
            "foi_email": "info@dewinning.be",
            "foi_postal": "St.-Ferdinandstraat 1, 3560 Lummen",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0465.903.173 Actief VZW 5 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~{RATIO}x) pnl JUMP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 25.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Limburg>Lummen>DeWinning>NBB_PDF_assets_debt_equity_jump",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); equity JUMP EUR{EQUITY} vs YE2024 EUR{EQUITY24} (+87%); pnl JUMP EUR{PNL} vs YE2024 EUR{PNL24} (+109%); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) loonkostsubsidie/GESCO/ESF/VDAB matrix; 5 VE cost allocation",
            "why_it_matters": f"Medium CW shows Limburg maatwerk VZW with equity nearly doubling (+87%) and pnl JUMP +109% under bruto~{RATIO}x omzet public subsidy path while assets/debt unpublished",
            "priority": "8",
            "recipient_body": "De Winning Maatwerk VZW",
            "recipient_email": "info@dewinning.be",
            "recipient_postal": "St.-Ferdinandstraat 1, 3560 Lummen",
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
    if row.get("task_id") == "rq_2201":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["blocked_gap_id"] = GAP
        row["title"] = f"leftover dual — De Winning YE2025 Medium (omzet JUMP 7.96m / equity JUMP +87% / pnl JUMP +109%)"
        row["notes"] = (
            "tick2201; De Winning 0465.903.173 YE2025 Medium CW; AGB Bornem JR2024; FARO/REW YE2024; "
            "next rq_2202; every-10 next 2210"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2201 missing")

if not any(r.get("task_id") == "rq_2202" for r in rows):
    rows.append(
        {
            "task_id": "rq_2202",
            "title": "leftover dual hole-fill after De Winning — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2202 after De Winning Maatwerk Lummen YE2025 Medium (omzet JUMP 7.96m / equity JUMP +87% / pnl JUMP +109% / bruto≫omzet). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS. "
                "Do NOT redo De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2201 De Winning; FARO/REW still YE2024; next every-10 2210",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2201=done rq_2202=open")

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
    "last_unit_id": "rq_2201",
    "ticks_completed": "2201",
    "paused": "no",
    "notes": (
        f"tick2201 leftover De Winning 0465.903.173 Medium (omzet JUMP 7.96m; bruto 11.46m ≫ omzet ~{RATIO}x; pnl JUMP 1.76m +109%; "
        "equity JUMP 3.59m +87%; FTE 281.5; 5 VE Lummen); AGB Bornem JR2024; FARO/REW YE2024; "
        "next rq_2202; next every-10 2210; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2201 DONE")
