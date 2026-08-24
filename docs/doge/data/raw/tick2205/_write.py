# tick2205 writer — De Oesterbank Oostende YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T14:20:00Z"
TICK = "2205"
ENTITY = "vzw_de_oesterbank_oostende"
SRC_EN = "src_oesterbank_jr2025_cw_en"
COMM = "comm_oesterbank_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_jump_fte_drop"
LB = "lb_oesterbank_omzet_7_31m_bruto_gt_omzet_pnl_jump_237pct_fte_drop_jr2025"
GAP = "gap_oesterbank_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_jump_fte_drop_matrix_l5"

OMZET = 7314640
BRUTO = 13796290
PNL = 285185
EQUITY = 6122570
FTE = 366.8
OMZET24 = 7014758
BRUTO24 = 13096491
PNL24 = 84745
EQUITY24 = 5873471
FTE24 = 379.6
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
            "source_id": "src_oesterbank_jr2025_cw_nl",
            "title": "Companyweb NL De Oesterbank YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407762165/de-oesterbank",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 16.07.2026; raw docs/doge/data/raw/tick2205/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN De Oesterbank YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407762165/de-oesterbank",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 16-07-2026; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_oesterbank_jr2025_cw_fr",
            "title": "Companyweb FR De Oesterbank YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407762165/de-oesterbank",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_oesterbank_kbo_2205",
            "title": "KBO De Oesterbank 0407.762.165 Actief VZW 2 VE Oostende",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407762165",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2205; Actief VZW; Vaartblekersstraat 15 8400 Oostende; 2 VE; RSZ NACE 88.993",
        },
        {
            "source_id": "src_oesterbank_foi_contact_2205",
            "title": "De Oesterbank FOI channel info@deoesterbank.be",
            "url": "https://www.oesterbank.be/nl/contact",
            "publisher": "De Oesterbank VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2205; info@deoesterbank.be / info@oesterbank.be; 059 80 16 73; Vaartblekersstraat 15 8400 Oostende",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_oesterbank_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +4.28% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_oesterbank_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +5.34% vs YE2024 {BRUTO24}; bruto≫omzet (~{RATIO}x)",
        },
        {
            "budget_id": "bud_oesterbank_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl JUMP +236.52% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_oesterbank_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +4.24% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_oesterbank_fte_jr2025_statutory",
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
            "title": f"De Oesterbank Oostende YE2025 leftover dual (omzet JUMP 7.31m / bruto≫omzet ~{RATIO}x / pnl JUMP +237% / FTE DROP)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / industrial supply clients West-Vlaanderen Oostende coast",
            "legal_basis": "VZW maatwerk (KBO 0407.762.165; Actief; 2 VE; RSZ NACE 88.993)",
            "decision_date": "2026-07-16",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407762165/de-oesterbank",
            "stated_goal": "Sheltered employment / industrial toelevering maatwerk",
            "cut_option": f"Publish NBB PDF assets/debt FOI; disclose bruto~{RATIO}x omzet loonkost matrix + pnl JUMP +237% with FTE DROP",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Oostende>DeOesterbank>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; omzet primary envelope; bruto≫omzet (~{RATIO}x) + pnl JUMP +237% with FTE DROP primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": f"Oesterbank omzet JUMP 7.31m / bruto≫omzet ~{RATIO}x / pnl JUMP +237% / FTE DROP (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Oostende>DeOesterbank>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": f"CW omzet JUMP envelope 7.31m / bruto 13.80m ≫ omzet (~{RATIO}x) / pnl JUMP 285k +237% from YE2024 85k / equity JUMP 6.12m / FTE DROP 366.8; coast maatwerk; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Oostende coast / public loonkost path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +4.3%; bruto JUMP +5.3%; pnl JUMP +236.5%; equity JUMP +4.2%; FTE DROP -3.4%",
            "absurdity_score": "7.6",
            "cost_score": "5.4",
            "difficulty": "3.0",
            "priority_index": "6.9",
            "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose bruto~{RATIO}x omzet loonkost/GESCO/ESF split; pnl JUMP with FTE DROP path",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/REW YE2024; West-Vlaanderen maatwerk dual after Werkplus/Trianval",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "De Oesterbank VZW (Oostende)",
            "name_fr": "De Oesterbank ASBL (Ostende)",
            "name_en": "De Oesterbank sheltered workshop non-profit (Ostend)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.oesterbank.be/",
            "foi_email": "info@deoesterbank.be",
            "foi_postal": "Vaartblekersstraat 15, 8400 Oostende",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.762.165 Actief VZW 2 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~{RATIO}x) pnl JUMP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 16.07.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Oostende>DeOesterbank>NBB_PDF_assets_debt_bruto_gt_omzet",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix; pnl JUMP EUR{PNL} vs YE2024 EUR{PNL24} (+237%); FTE DROP {FTE24}->{FTE}; equity JUMP EUR{EQUITY}; 2 VE + site cost allocation",
            "why_it_matters": f"Medium CW shows large coast maatwerk VZW with bruto ~{RATIO}x omzet and pnl JUMP +237% while FTE DROP under public subsidy path; assets/debt unpublished",
            "priority": "8",
            "recipient_body": "De Oesterbank VZW",
            "recipient_email": "info@deoesterbank.be",
            "recipient_postal": "Vaartblekersstraat 15, 8400 Oostende",
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
    if row.get("task_id") == "rq_2205":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["blocked_gap_id"] = GAP
        row["title"] = f"leftover dual — Oesterbank YE2025 Medium (omzet JUMP 7.31m / bruto≫omzet ~{RATIO}x / pnl JUMP +237% / FTE DROP)"
        row["notes"] = (
            "tick2205; Oesterbank 0407.762.165 YE2025 Medium CW; AGB Bornem JR2024; FARO/REW YE2024; "
            "next rq_2206; every-10 next 2210"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2205 missing")

if not any(r.get("task_id") == "rq_2206" for r in rows):
    rows.append(
        {
            "task_id": "rq_2206",
            "title": "leftover dual hole-fill after Oesterbank — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2206 after De Oesterbank Oostende YE2025 Medium (omzet JUMP 7.31m / bruto≫omzet ~1.89x / pnl JUMP +237% / FTE DROP). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(FREE: Entiris/Odas/Arcor/Kemphaan/ACG/Noordheuvel). "
                "Do NOT redo Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2205 Oesterbank; FARO/REW still YE2024; next every-10 2210",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2205=done rq_2206=open")

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
    "last_unit_id": "rq_2205",
    "ticks_completed": "2205",
    "paused": "no",
    "notes": (
        f"tick2205 leftover Oesterbank 0407.762.165 Medium (omzet JUMP 7.31m; bruto 13.80m ≫ omzet ~{RATIO}x; pnl JUMP 285k +237%; "
        "equity JUMP 6.12m; FTE DROP 366.8; 2 VE Oostende); AGB Bornem JR2024; FARO/REW YE2024; "
        "next rq_2206; next every-10 2210; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2205 DONE")
