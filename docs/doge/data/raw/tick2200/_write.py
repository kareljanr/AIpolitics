# tick2200 writer — EVERY-10 + Atelier Groot Eiland YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T12:40:00Z"
TICK = "2200"
ENTITY = "vzw_atelier_groot_eiland"
SRC_EN = "src_atelier_groot_eiland_jr2025_cw_en"
COMM = "comm_atelier_groot_eiland_jr2025_statutory_maatwerk_empty_omzet_pnl_jump"
LB = "lb_atelier_groot_eiland_bruto_2_93m_empty_omzet_pnl_jump_263pct_jr2025"
GAP = "gap_atelier_groot_eiland_nbb_pdf_assets_debt_empty_omzet_pnl_jump_matrix_l5"

BRUTO = 2934111
PNL = 23906
EQUITY = 1014772
FTE = 53.6
BRUTO24 = 2719635
PNL24 = 6583
EQUITY24 = 1069202
FTE24 = 55.4
ENVELOPE = BRUTO


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
            "source_id": "src_atelier_groot_eiland_jr2025_cw_nl",
            "title": "Companyweb NL Atelier Groot Eiland YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0430686037/atelier-groot-eiland",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet empty bruto JUMP {BRUTO} pnl JUMP {PNL} equity DROP {EQUITY} FTE DROP {FTE}; neerlegging 24.06.2026; raw docs/doge/data/raw/tick2200/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Atelier Groot Eiland YE2025 statutory",
            "url": "https://www.companyweb.be/en/0430686037/atelier-groot-eiland",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 24-06-2026; Turnover unpublished Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} Employees {FTE}",
        },
        {
            "source_id": "src_atelier_groot_eiland_jr2025_cw_fr",
            "title": "Companyweb FR Atelier Groot Eiland YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0430686037/atelier-groot-eiland",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; CA non publie",
        },
        {
            "source_id": "src_atelier_groot_eiland_kbo_2200",
            "title": "KBO Atelier Groot Eiland 0430.686.037 Actief VZW 4 VE Molenbeek",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0430686037",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2200; Actief VZW; Henegouwenkaai 29 1080 Sint-Jans-Molenbeek; 4 VE; RSZ NACE 88.993; BTW 01.130/56.111/56.112",
        },
        {
            "source_id": "src_atelier_groot_eiland_foi_contact_2200",
            "title": "Atelier Groot Eiland FOI channel info@grooteiland.brussels",
            "url": "https://www.grooteiland.brussels/en/Contact",
            "publisher": "Atelier Groot Eiland VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2200; info@grooteiland.brussels; 02 511 72 10; Henegouwenkaai 29 1080 Molenbeek",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_atelier_groot_eiland_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025 (omzet empty)",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +7.89% vs YE2024 {BRUTO24}; omzet unpublished",
        },
        {
            "budget_id": "bud_atelier_groot_eiland_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl JUMP +263.14% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_atelier_groot_eiland_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity DROP -5.09% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_atelier_groot_eiland_fte_jr2025_statutory",
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
    "2025_omzet": None,
    "2025_bruto": BRUTO,
    "2025_pnl": PNL,
    "2025_equity": EQUITY,
    "2025_fte": FTE,
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
            "title": "Atelier Groot Eiland YE2025 leftover dual EVERY-10 (bruto JUMP 2.93m / empty omzet / pnl JUMP +263%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / urban farming / social-economy clients Brussels Molenbeek",
            "legal_basis": "VZW maatwerk (KBO 0430.686.037; Actief; 4 VE; RSZ NACE 88.993; BTW farming/horeca)",
            "decision_date": "2026-06-24",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(ENVELOPE),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0430686037/atelier-groot-eiland",
            "stated_goal": "Sheltered employment / inclusive urban farming and catering",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose empty omzet vs bruto 2.93m + pnl JUMP +263% subsidy matrix",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Bruxelles>Molenbeek>AtelierGrootEiland>JR2025_statutory_L5",
            "notes": "tick2200 EVERY-10; Medium CW; bruto primary envelope (omzet empty); empty omzet + pnl JUMP +263% with equity/FTE DROP primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Atelier Groot Eiland bruto JUMP 2.93m / empty omzet / pnl JUMP +263% (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Bruxelles>Molenbeek>AtelierGrootEiland>JR2025",
            "annual_cost_eur": str(ENVELOPE),
            "total_cost_eur": str(ENVELOPE),
            "tco_notes": "CW bruto JUMP envelope 2.93m / omzet empty / pnl JUMP 24k +263% from YE2024 6.6k / equity DROP 1.01m / FTE DROP 53.6; Brussels maatwerk+urban farming; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Molenbeek / Actiris-ESF path / urban farming clients",
            "stated_goal": "Sheltered employment + inclusive urban farming",
            "measured_outcome": "bruto JUMP +7.9%; omzet empty; pnl JUMP +263%; equity DROP -5.1%; FTE DROP -3.2%",
            "absurdity_score": "7.4",
            "cost_score": "4.5",
            "difficulty": "3.0",
            "priority_index": "6.5",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose empty omzet vs bruto + pnl JUMP path; Actiris/ESF/gewest subsidy split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK} EVERY-10 primary; Medium CW; FOI {GAP}; stall FARO/REW YE2024; Brussels maatwerk dual after Groep Talent/BosKat",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Atelier Groot Eiland VZW (Molenbeek)",
            "name_fr": "Atelier Groot Eiland ASBL (Molenbeek)",
            "name_en": "Atelier Groot Eiland sheltered workshop / urban farm (Molenbeek)",
            "level": "parastatal",
            "parent_id": "sec_brussels",
            "community_language": "nl",
            "website": "https://www.grooteiland.brussels/",
            "foi_email": "info@grooteiland.brussels",
            "foi_postal": "Henegouwenkaai 29, 1080 Sint-Jans-Molenbeek",
            "notes": f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0430.686.037 Actief VZW 4 VE RSZ NACE 88.993; omzet empty bruto JUMP {BRUTO} pnl JUMP {PNL} vs YE2024 {PNL24} equity DROP {EQUITY} FTE DROP {FTE}; neerlegging 24.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Bruxelles>Molenbeek>AtelierGrootEiland>NBB_PDF_assets_debt_empty_omzet",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); empty omzet vs bruto EUR{BRUTO}; pnl JUMP EUR{PNL} vs YE2024 EUR{PNL24} (+263%); equity DROP EUR{EQUITY}; FTE DROP {FTE24}->{FTE}; Actiris/ESF/gewest/gemeente subsidy matrix; 4 VE cost allocation",
            "why_it_matters": "Medium CW shows Brussels maatwerk+urban farming VZW with empty omzet, bruto 2.93m and pnl JUMP +263% while equity/FTE DROP — public subsidy path opaque",
            "priority": "8",
            "recipient_body": "Atelier Groot Eiland VZW",
            "recipient_email": "info@grooteiland.brussels",
            "recipient_postal": "Henegouwenkaai 29, 1080 Sint-Jans-Molenbeek",
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
            "notes": f"tick{TICK} EVERY-10; ready NOT sent; Medium CW + Strong KBO; next every-10 2210",
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
    if row.get("task_id") == "rq_2200":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["blocked_gap_id"] = GAP
        row["title"] = "EVERY-10 + leftover dual — Atelier Groot Eiland YE2025 Medium (bruto JUMP 2.93m / empty omzet / pnl JUMP +263%)"
        row["notes"] = (
            "tick2200 EVERY-10; Atelier Groot Eiland 0430.686.037 YE2025 Medium CW; progress+top10 refreshed; "
            "AGB Bornem JR2024; FARO/REW YE2024; next rq_2201; every-10 next 2210"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2200 missing")

if not any(r.get("task_id") == "rq_2201" for r in rows):
    rows.append(
        {
            "task_id": "rq_2201",
            "title": "leftover dual hole-fill after Atelier Groot Eiland — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2201 after EVERY-10 Atelier Groot Eiland YE2025 Medium (bruto JUMP 2.93m / empty omzet / pnl JUMP +263% / FTE DROP). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS. "
                "Do NOT redo Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2200 EVERY-10 AGE; FARO/REW still YE2024; next every-10 2210",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2200=done rq_2201=open")

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
    "last_unit_id": "rq_2200",
    "ticks_completed": "2200",
    "paused": "no",
    "notes": (
        "tick2200 EVERY-10 leftover Atelier Groot Eiland 0430.686.037 Medium (bruto JUMP 2.93m; omzet empty; pnl JUMP 24k +263%; "
        "equity DROP 1.01m; FTE DROP 53.6; 4 VE Molenbeek); progress+top10 refreshed; AGB Bornem JR2024; FARO/REW YE2024; "
        "next rq_2201; next every-10 2210; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2200 DONE")
