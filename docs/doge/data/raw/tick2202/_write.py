# tick2202 writer — Kaliber Herentals YE2025 Medium CW (omzet JUMP +56% / LOSS FLIP / KEMPA merger)
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T13:20:00Z"
TICK = "2202"
ENTITY = "vzw_kaliber_herentals"
SRC_EN = "src_kaliber_jr2025_cw_en"
COMM = "comm_kaliber_jr2025_statutory_maatwerk_omzet_jump_pnl_loss_flip_kempa_merger"
LB = "lb_kaliber_omzet_jump_6_38m_pnl_loss_flip_kempa_merger_jr2025"
GAP = "gap_kaliber_nbb_pdf_assets_debt_omzet_jump_pnl_loss_flip_kempa_merger_matrix_l5"

OMZET = 6384439
BRUTO = 10597344
PNL = -154743
EQUITY = 6056883
FTE = 283.7
OMZET24 = 4100185
BRUTO24 = 9393390
PNL24 = 338584
EQUITY24 = 6259619
FTE24 = 269.4
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
            "source_id": "src_kaliber_jr2025_cw_nl",
            "title": "Companyweb NL Kaliber YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407201941/kaliber",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl LOSS FLIP {PNL} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 11.07.2026; raw docs/doge/data/raw/tick2202/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Kaliber YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407201941/kaliber",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 11-07-2026; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_kaliber_jr2025_cw_fr",
            "title": "Companyweb FR Kaliber YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407201941/kaliber",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_kaliber_kbo_2202",
            "title": "KBO Kaliber 0407.201.941 Actief VZW 2 VE Herentals KEMPA merger",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407201941",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2202; Actief VZW; Herenthoutseweg 136 2200 Herentals; 2 VE; RSZ NACE 88.993; absorbed KEMPA Products 0632.634.295 since 30.12.2025",
        },
        {
            "source_id": "src_kaliber_foi_contact_2202",
            "title": "Kaliber FOI channel info@kalibermaatwerk.be",
            "url": "https://kalibermaatwerk.be/",
            "publisher": "Kaliber VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2202; info@kalibermaatwerk.be; +32 14 21 18 04; Herenthoutseweg 136 2200 Herentals",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_kaliber_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +55.71% vs YE2024 {OMZET24}; KEMPA merger 30.12.2025",
        },
        {
            "budget_id": "bud_kaliber_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +12.82% vs YE2024 {BRUTO24}; bruto≫omzet (~{RATIO}x)",
        },
        {
            "budget_id": "bud_kaliber_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl LOSS FLIP -145.7% vs YE2024 profit {PNL24}",
        },
        {
            "budget_id": "bud_kaliber_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity DROP -3.24% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_kaliber_fte_jr2025_statutory",
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
    "absorbed_kempa": "0632.634.295",
    "kempa_absorbed_date": "2025-12-30",
}

append_csv(
    "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": f"Kaliber Herentals YE2025 leftover dual (omzet JUMP 6.38m +56% / pnl LOSS FLIP -155k / KEMPA merger / bruto≫omzet ~{RATIO}x)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / logistics-packaging clients Antwerpen Herentals",
            "legal_basis": "VZW maatwerk (KBO 0407.201.941; Actief; 2 VE; RSZ NACE 88.993; absorbed KEMPA 0632.634.295 since 30.12.2025)",
            "decision_date": "2026-07-11",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407201941/kaliber",
            "stated_goal": "Sheltered employment / logistics packaging maatwerk",
            "cut_option": f"Publish NBB PDF assets/debt FOI; disclose omzet JUMP +56% vs KEMPA merger + LOSS FLIP + bruto~{RATIO}x omzet loonkost matrix",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Herentals>Kaliber>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; omzet primary envelope; omzet JUMP +56% + LOSS FLIP + KEMPA merger primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; Kromme Boom FREE deferred; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": f"Kaliber omzet JUMP 6.38m +56% / pnl LOSS FLIP -155k / KEMPA merger / bruto≫omzet ~{RATIO}x (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory_merged",
            "hierarchy_path": "Vlaanderen>Antwerpen>Herentals>Kaliber>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": f"CW omzet JUMP envelope 6.38m (+56%) / bruto 10.60m ≫ omzet (~{RATIO}x) / pnl LOSS FLIP -155k from YE2024 profit 339k / equity DROP 6.06m / FTE JUMP 283.7; KEMPA Products absorbed 30.12.2025; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Herentals / public loonkost path",
            "stated_goal": "Sheltered employment maatwerk logistics",
            "measured_outcome": "omzet JUMP +55.7%; bruto JUMP +12.8%; pnl LOSS FLIP -145.7%; equity DROP -3.2%; FTE JUMP +5.3%; KEMPA merger YE2025",
            "absurdity_score": "7.8",
            "cost_score": "5.3",
            "difficulty": "3.0",
            "priority_index": "7.0",
            "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose omzet JUMP +56% KEMPA contribution + LOSS FLIP path + bruto~{RATIO}x omzet loonkost split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/REW YE2024; Herentals maatwerk dual after De Winning/Groep Talent/BosKat; Kromme Boom deferred",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Kaliber VZW (Herentals; KEMPA-fusie)",
            "name_fr": "Kaliber ASBL (Herentals; fusion KEMPA)",
            "name_en": "Kaliber sheltered workshop (Herentals; KEMPA merger)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://kalibermaatwerk.be/",
            "foi_email": "info@kalibermaatwerk.be",
            "foi_postal": "Herenthoutseweg 136, 2200 Herentals",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.201.941 Actief VZW 2 VE RSZ NACE 88.993; absorbed KEMPA 0632.634.295 since 30.12.2025; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~{RATIO}x) pnl LOSS FLIP {PNL} vs YE2024 {PNL24} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 11.07.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Herentals>Kaliber>NBB_PDF_assets_debt_omzet_jump_kempa",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); omzet JUMP EUR{OMZET} vs YE2024 EUR{OMZET24} (+56%) KEMPA Products 0632.634.295 fusion contribution (30.12.2025); pnl LOSS FLIP EUR{PNL} vs YE2024 profit EUR{PNL24}; bruto EUR{BRUTO} ≫ omzet (~{RATIO}x) loonkostsubsidie matrix; FTE JUMP {FTE24}->{FTE}; 2 VE cost allocation",
            "why_it_matters": f"Medium CW shows Herentals maatwerk VZW with omzet JUMP +56% and pnl LOSS FLIP after absorbing KEMPA under bruto~{RATIO}x omzet public subsidy path while assets/debt unpublished",
            "priority": "8",
            "recipient_body": "Kaliber VZW",
            "recipient_email": "info@kalibermaatwerk.be",
            "recipient_postal": "Herenthoutseweg 136, 2200 Herentals",
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
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; KEMPA merger; next every-10 2210",
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
        row["title"] = "leftover dual — Kaliber YE2025 Medium (omzet JUMP 6.38m +56% / pnl LOSS FLIP / KEMPA merger)"
        row["notes"] = (
            "tick2202; Kaliber 0407.201.941 YE2025 Medium CW; KEMPA absorbed 30.12.2025; "
            "AGB Bornem JR2024; FARO/REW YE2024; Kromme Boom FREE deferred; next rq_2203; every-10 next 2210"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2202 missing")

if not any(r.get("task_id") == "rq_2203" for r in rows):
    rows.append(
        {
            "task_id": "rq_2203",
            "title": "leftover dual hole-fill after Kaliber — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2203 after Kaliber Herentals YE2025 Medium (omzet JUMP 6.38m +56% / pnl LOSS FLIP -155k / KEMPA merger / bruto≫omzet). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(De Kromme Boom 0454.426.489 YE2025 FREE equity NEG). "
                "Do NOT redo Kaliber, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2202 Kaliber; FARO/REW still YE2024; next every-10 2210",
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
        f"tick2202 leftover Kaliber 0407.201.941 Medium (omzet JUMP 6.38m +56%; bruto 10.60m ≫ omzet ~{RATIO}x; pnl LOSS FLIP -155k; "
        "equity DROP 6.06m; FTE JUMP 283.7; KEMPA absorbed 30.12.2025; 2 VE Herentals); AGB Bornem JR2024; FARO/REW YE2024; "
        "next rq_2203; next every-10 2210; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2202 DONE")
