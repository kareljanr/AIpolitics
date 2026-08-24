# tick2201 writer — MWP Pajottenland YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T13:00:00Z"
TICK = "2201"
ENTITY = "vzw_mwp_pajottenland"
SRC_EN = "src_mwp_pajottenland_jr2025_cw_en"
COMM = "comm_mwp_pajottenland_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_jump"
LB = "lb_mwp_pajottenland_omzet_2_65m_bruto_gt_omzet_pnl_jump_299pct_jr2025"
GAP = "gap_mwp_pajottenland_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_jump_matrix_l5"

OMZET = 2653635
BRUTO = 4659880
PNL = 135947
EQUITY = 2578716
FTE = 125.0
OMZET24 = 2517102
BRUTO24 = 4670942
PNL24 = 34103
EQUITY24 = 2442769
FTE24 = 129.7
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
            "source_id": "src_mwp_pajottenland_jr2025_cw_nl",
            "title": "Companyweb NL Maatwerkbedrijf Pajottenland YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0413313535/maatwerkbedrijf-pajottenland",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 04.07.2026; raw docs/doge/data/raw/tick2201/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Maatwerkbedrijf Pajottenland YE2025 statutory",
            "url": "https://www.companyweb.be/en/0413313535/maatwerkbedrijf-pajottenland",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 04-07-2026; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} Employees {FTE}",
        },
        {
            "source_id": "src_mwp_pajottenland_jr2025_cw_fr",
            "title": "Companyweb FR Maatwerkbedrijf Pajottenland YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0413313535/maatwerkbedrijf-pajottenland",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; CA {OMZET}",
        },
        {
            "source_id": "src_mwp_pajottenland_kbo_2201",
            "title": "KBO Maatwerkbedrijf Pajottenland 0413.313.535 Actief VZW 1 VE Lennik",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413313535",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2201; Actief VZW; Luitenant Jacopsstraat 11 1750 Lennik; 1 VE; RSZ/BTW NACE 88.993; afkorting MWP",
        },
        {
            "source_id": "src_mwp_pajottenland_foi_contact_2201",
            "title": "MWP Pajottenland FOI channel mwpajot@mwpajot.be",
            "url": "https://www.mwpajottenland.be/",
            "publisher": "Maatwerkbedrijf Pajottenland VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2201; mwpajot@mwpajot.be; 02 532 12 40; Luitenant Jacopsstraat 11 1750 Sint-Kwintens-Lennik",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_mwp_pajottenland_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +5.42% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_mwp_pajottenland_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025 (bruto≫omzet ~1.76x)",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto DROP -0.24% vs YE2024 {BRUTO24}; bruto≫omzet",
        },
        {
            "budget_id": "bud_mwp_pajottenland_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl JUMP +298.64% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_mwp_pajottenland_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +5.57% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_mwp_pajottenland_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW social-balance FTE / Employees {FTE}",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; FTE DROP vs YE2024 {FTE24}; assets/debt Unknown",
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
            "title": "MWP Pajottenland YE2025 leftover dual (omzet JUMP 2.65m / bruto≫omzet ~1.76x / pnl JUMP +299%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Pajottenland Lennik",
            "legal_basis": "VZW maatwerk (KBO 0413.313.535; Actief; 1 VE; RSZ/BTW NACE 88.993; afkorting MWP)",
            "decision_date": "2026-07-04",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(ENVELOPE),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0413313535/maatwerkbedrijf-pajottenland",
            "stated_goal": "Sheltered employment / maatwerk Pajottenland",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose bruto≫omzet ~1.76x + pnl JUMP +299% subsidy matrix",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Lennik>MWP_Pajottenland>JR2025_statutory_L5",
            "notes": "tick2201; Medium CW; omzet primary envelope; bruto≫omzet ~1.76x + pnl JUMP +299% with FTE DROP primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; AIESH 404; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "MWP Pajottenland omzet JUMP 2.65m / bruto≫omzet ~1.76x / pnl JUMP +299% (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Lennik>MWP_Pajottenland>JR2025",
            "annual_cost_eur": str(ENVELOPE),
            "total_cost_eur": str(ENVELOPE),
            "tco_notes": "CW omzet JUMP envelope 2.65m / bruto 4.66m ≫omzet ~1.76x / pnl JUMP 136k +299% from YE2024 34k / equity JUMP 2.58m / FTE DROP 125; VL maatwerk Lennik; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Pajottenland / VDAB-ESF path / commercial clients",
            "stated_goal": "Sheltered employment maatwerk Pajottenland",
            "measured_outcome": "omzet JUMP +5.4%; bruto≫omzet ~1.76x; pnl JUMP +299%; equity JUMP +5.6%; FTE DROP -3.6%",
            "absurdity_score": "7.3",
            "cost_score": "4.3",
            "difficulty": "3.0",
            "priority_index": "6.5",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet + pnl JUMP path; VDAB/ESF/gemeente subsidy split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK} primary; Medium CW; FOI {GAP}; stall FARO/REW YE2024 AIESH 404; VL maatwerk dual after AGE",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Maatwerkbedrijf Pajottenland VZW (MWP / Lennik)",
            "name_fr": "Entreprise de travail adapté Pajottenland ASBL (MWP / Lennik)",
            "name_en": "Maatwerkbedrijf Pajottenland sheltered workshop (MWP / Lennik)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.mwpajottenland.be/",
            "foi_email": "mwpajot@mwpajot.be",
            "foi_postal": "Luitenant Jacopsstraat 11, 1750 Lennik",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0413.313.535 Actief VZW 1 VE RSZ/BTW NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO}≫omzet pnl JUMP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 04.07.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; AIESH 404; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Lennik>MWP_Pajottenland>NBB_PDF_assets_debt_bruto_gt_omzet",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} vs omzet EUR{OMZET} (~1.76x); pnl JUMP EUR{PNL} vs YE2024 EUR{PNL24} (+299%); FTE DROP {FTE24}->{FTE}; VDAB/ESF/gemeente/provincie subsidy matrix",
            "why_it_matters": "Medium CW shows VL maatwerk VZW with bruto≫omzet ~1.76x and pnl JUMP +299% while FTE DROP — public subsidy path opaque",
            "priority": "8",
            "recipient_body": "Maatwerkbedrijf Pajottenland VZW",
            "recipient_email": "mwpajot@mwpajot.be",
            "recipient_postal": "Luitenant Jacopsstraat 11, 1750 Lennik",
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
        row["title"] = (
            "leftover dual — MWP Pajottenland YE2025 Medium (omzet JUMP 2.65m / bruto≫omzet ~1.76x / pnl JUMP +299%)"
        )
        row["notes"] = (
            "tick2201; MWP 0413.313.535 YE2025 Medium CW; AGB Bornem JR2024; FARO/REW YE2024; AIESH 404; "
            "next rq_2202; every-10 next 2210"
        )
        row["instructions"] = (
            "Tick 2201 after EVERY-10 Atelier Groot Eiland YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
            "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
            "(MWP Pajottenland 0413.313.535 YE2025 FREE taken). Do NOT redo Atelier Groot Eiland, Groep Talent, BosKat, "
            "De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, "
            "Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
            "WAAK SW, Waak, Stijn, Stroom, Springplank."
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2201 missing")

if not any(r.get("task_id") == "rq_2202" for r in rows):
    rows.append(
        {
            "task_id": "rq_2202",
            "title": "leftover dual hole-fill after MWP Pajottenland — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2202 after MWP Pajottenland YE2025 Medium (omzet JUMP 2.65m / bruto≫omzet ~1.76x / pnl JUMP +299% / FTE DROP). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(FREE candidates from prior probes: Kaliber/Aarova/Oesterbank/Werkhuizen MIN/Trianval/Noordheuvel/Arcor/ACG/Entiris/Odas/Kemphaan/…). "
                "Do NOT redo MWP Pajottenland, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, "
                "A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, "
                "Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, "
                "Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2201 MWP; FARO/REW still YE2024; AIESH 404; next every-10 2210",
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
        "tick2201 leftover MWP Pajottenland 0413.313.535 Medium (omzet JUMP 2.65m; bruto≫omzet ~1.76x 4.66m; "
        "pnl JUMP 136k +299%; equity JUMP 2.58m; FTE DROP 125; 1 VE Lennik); AGB Bornem JR2024; FARO/REW YE2024; AIESH 404; "
        "next rq_2202; next every-10 2210; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2201 DONE")
