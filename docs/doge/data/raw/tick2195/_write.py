# tick2195 writer — Bewel YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T11:00:00Z"
TICK = "2195"
ENTITY = "vzw_bewel_diepenbeek"
SRC_EN = "src_bewel_jr2025_cw_en"
COMM = "comm_bewel_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_jump"
LB = "lb_bewel_omzet_jump_28_64m_bruto_gt_omzet_pnl_jump_jr2025"
GAP = "gap_bewel_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_jump_matrix_l5"

OMZET = 28644666
BRUTO = 66776088
PNL = 2877726
EQUITY = 37352223
FTE = 2015.6
OMZET24 = 24995886
BRUTO24 = 61171637
PNL24 = 844089
EQUITY24 = 34518325
FTE24 = 1971.5


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
            "source_id": "src_bewel_jr2025_cw_nl",
            "title": "Companyweb NL Bewel YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407229358/bewel",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 09.07.2026; raw docs/doge/data/raw/tick2195/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Bewel YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407229358/bewel",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 09-07-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_bewel_jr2025_cw_fr",
            "title": "Companyweb FR Bewel YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407229358/bewel",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_bewel_kbo_2195",
            "title": "KBO Bewel 0407.229.358 Actief VZW Diepenbeek 9 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407229358",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2195; Actief VZW BEWEL; Ginderoverstraat 143 3590 Diepenbeek; 9 VE; RSZ NACE 88.993; KBO email empty",
        },
        {
            "source_id": "src_bewel_foi_contact_2195",
            "title": "Bewel FOI channel info@bewel.be",
            "url": "https://www.bewel.be/contact/",
            "publisher": "Bewel VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2195; info@bewel.be; Ginderoverstraat 143 3590 Diepenbeek",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_bewel_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +14.6% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_bewel_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +9.16% vs YE2024 {BRUTO24}; bruto≫omzet (~2.33x)",
        },
        {
            "budget_id": "bud_bewel_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl JUMP +240.93% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_bewel_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +8.21% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_bewel_fte_jr2025_statutory",
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
            "title": "Bewel Diepenbeek YE2025 leftover dual (omzet JUMP 28.64m / bruto≫omzet ~2.3x / pnl JUMP +241%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Limburg Diepenbeek",
            "legal_basis": "VZW maatwerk (KBO 0407.229.358; Actief; 9 VE; RSZ NACE 88.993; BEWEL)",
            "decision_date": "2026-07-09",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407229358/bewel",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose bruto~2.3x omzet loonkostsubsidie matrix + pnl JUMP +241%",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Limburg>Diepenbeek>Bewel>JR2025_statutory_L5",
            "notes": "tick2195; Medium CW; omzet primary envelope; bruto≫omzet (~2.33x) + pnl JUMP primary absurdity; 2016 FTE; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; Kunnig already mined; Pajottenland/BW Zottegem FREE deferred; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Bewel omzet JUMP 28.64m / bruto≫omzet ~2.3x / pnl JUMP +241% (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Limburg>Diepenbeek>Bewel>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet JUMP envelope 28.64m / bruto 66.78m ≫ omzet (~2.33x) / pnl JUMP 2.88m +241% from YE2024 0.84m / equity JUMP 37.4m / FTE JUMP 2015.6; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Limburg / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +14.6%; bruto JUMP +9.2%; pnl JUMP +240.9%; equity JUMP +8.2%; FTE JUMP +2.2%",
            "absurdity_score": "7.6",
            "cost_score": "6.3",
            "difficulty": "3.0",
            "priority_index": "6.8",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose bruto~2.3x omzet loonkostsubsidie/GESCO/ESF split; pnl JUMP path",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Limburg maatwerk dual after Forena/Kunnig/De Wroeter",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Bewel VZW (Diepenbeek)",
            "name_fr": "Bewel ASBL (Diepenbeek)",
            "name_en": "Bewel sheltered workshop non-profit (Diepenbeek)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.bewel.be/",
            "foi_email": "info@bewel.be",
            "foi_postal": "Ginderoverstraat 143, 3590 Diepenbeek",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.229.358 Actief VZW 9 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~2.33x) pnl JUMP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 09.07.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Limburg>Diepenbeek>Bewel>NBB_PDF_assets_debt_bruto_gt_omzet",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~2.33x) loonkostsubsidie/GESCO/ESF/VDAB matrix; pnl JUMP EUR{PNL} vs YE2024 EUR{PNL24} (+241%); equity JUMP EUR{EQUITY}; FTE JUMP {FTE24}→{FTE}; 9 VE cost allocation",
            "why_it_matters": "Medium CW shows large Limburg maatwerk VZW (28.6m omzet / 2016 FTE) with bruto ~2.3x omzet and pnl JUMP +241% — assets/debt unpublished under public loonkost path",
            "priority": "8",
            "recipient_body": "BEWEL VZW",
            "recipient_email": "info@bewel.be",
            "recipient_postal": "Ginderoverstraat 143, 3590 Diepenbeek",
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
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; next every-10 2200",
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
    if row.get("task_id") == "rq_2195":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = "leftover dual — Bewel YE2025 Medium (omzet JUMP 28.64m / bruto≫omzet ~2.3x / pnl JUMP +241%)"
        row["notes"] = (
            "tick2195; Bewel 0407.229.358 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "AIESH/REW stall; Kunnig already mined; Pajottenland/BW Zottegem FREE deferred; next rq_2196; every-10 next 2200"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2195 missing")

if not any(r.get("task_id") == "rq_2196" for r in rows):
    rows.append(
        {
            "task_id": "rq_2196",
            "title": "leftover dual hole-fill after Bewel — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2196 after Bewel Diepenbeek YE2025 Medium (omzet JUMP 28.64m / bruto≫omzet ~2.3x / pnl JUMP +241% / FTE 2016). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(Pajottenland/BW Zottegem FREE). "
                "Do NOT redo Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2195 Bewel; FARO/AIESH/REW still YE2024; next every-10 2200",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2195=done rq_2196=open")

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
    "last_unit_id": "rq_2195",
    "ticks_completed": "2195",
    "paused": "no",
    "notes": (
        "tick2195 leftover BEWEL 0407.229.358 Medium (omzet JUMP 28.64m; bruto 66.78m ≫ omzet ~2.33x; pnl JUMP 2.88m +241%; "
        "equity JUMP 37.4m; FTE JUMP 2015.6; 9 VE Diepenbeek); AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; "
        "next rq_2196; next every-10 2200; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2195 DONE")
