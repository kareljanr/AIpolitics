# tick2198 writer — BosKat Herentals YE2025 Medium CW (LOSS FLIP + Stopgezet fusie Groep Talent)
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T12:00:00Z"
TICK = "2198"
ENTITY = "vzw_boskat_herentals"
SRC_EN = "src_boskat_jr2025_cw_en"
COMM = "comm_boskat_jr2025_statutory_maatwerk_pnl_loss_flip_stopgezet_fusie"
LB = "lb_boskat_bruto_3_28m_pnl_loss_flip_stopgezet_fusie_jr2025"
GAP = "gap_boskat_nbb_pdf_assets_debt_pnl_loss_flip_stopgezet_fusie_groep_talent_matrix_l5"

BRUTO = 3275562
PNL = -207378
EQUITY = 1551279
FTE = 78.5
BRUTO24 = 2901856
PNL24 = 249628
EQUITY24 = 1758657
FTE24 = 71.9
# omzet empty on CW — bruto is primary envelope
OMZET = None


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
            "source_id": "src_boskat_jr2025_cw_nl",
            "title": "Companyweb NL BosKat Herentals YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0464028204/bos-kat",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 bruto JUMP {BRUTO} pnl LOSS FLIP {PNL} equity DROP {EQUITY} FTE JUMP {FTE}; omzet empty; Status Stopgezet; neerlegging 20.06.2026; raw docs/doge/data/raw/tick2198/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN BosKat Herentals YE2025 statutory",
            "url": "https://www.companyweb.be/en/0464028204/bos-kat",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; Status Closed; filed 20-06-2026; Last balance sheet year 2025; Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}; Turnover not published",
        },
        {
            "source_id": "src_boskat_jr2025_cw_fr",
            "title": "Companyweb FR BosKat Herentals YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0464028204/bos-kat",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025; Status Cessée-class",
        },
        {
            "source_id": "src_boskat_kbo_2198",
            "title": "KBO BosKat 0464.028.204 Stopgezet fusie Groep Talent 0459.644.990",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0464028204",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2198; Stopgezet sinds 4 juni 2026; Fusie door overneming; opgeslorpt door 0459.644.990 Groep Talent; 1 VE; BTW NACE 02.100 + RSZ NACE 88.993; Kamergoor 19/1 2200 Herentals",
        },
        {
            "source_id": "src_boskat_foi_contact_2198",
            "title": "BosKat Herentals FOI channel info@boskat.be + site",
            "url": "https://www.boskat.be/",
            "publisher": "BosKat VZW / gemeente Westerlo dual note",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2198; info@boskat.be; Kamergoor 19/1 2200 Herentals; 014 23 31 36; successor Groep Talent 0459.644.990; Westerlo member dual public",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_boskat_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025 (omzet empty)",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +12.88% vs YE2024 {BRUTO24}; primary envelope (omzet not published)",
        },
        {
            "budget_id": "bud_boskat_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl LOSS FLIP -183.07% vs YE2024 +{PNL24}",
        },
        {
            "budget_id": "bud_boskat_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity DROP -11.79% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_boskat_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW social-balance FTE / Employees {FTE}",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; FTE JUMP vs YE2024 {FTE24}; assets/debt/omzet Unknown",
        },
        {
            "budget_id": "bud_boskat_omzet_jr2025_statutory_empty",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "",
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "CW FAQ: turnover not published YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet empty — FOI NBB PDF; bruto {BRUTO} used as envelope",
        },
    ],
)

cash = {
    "2025_bruto": BRUTO,
    "2025_pnl": PNL,
    "2025_equity": EQUITY,
    "2025_fte": FTE,
    "2025_omzet": "empty",
    "2024_bruto": BRUTO24,
    "2024_pnl": PNL24,
    "2024_equity": EQUITY24,
    "2024_fte": FTE24,
    "stopgezet_fusie": "2026-06-04_Groep_Talent_0459.644.990",
}

append_csv(
    "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": "BosKat Herentals YE2025 leftover dual (bruto JUMP 3.28m / pnl LOSS FLIP -207k / Stopgezet fusie Groep Talent)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers groen/bos / public clients Antwerpen Herentals + municipalities (Westerlo member)",
            "legal_basis": "VZW maatwerk Stopgezet fusie (KBO 0464.028.204; 1 VE; BTW NACE 02.100; RSZ NACE 88.993; absorbed by 0459.644.990 Groep Talent 2026-06-04)",
            "decision_date": "2026-06-20",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(BRUTO),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "closed",
            "evaluation_url": "https://www.companyweb.be/en/0464028204/bos-kat",
            "stated_goal": "Sheltered employment — green/forestry landscaping maatwerk",
            "cut_option": "Publish NBB PDF assets/debt/omzet FOI; disclose LOSS FLIP + fusie Groep Talent ruilverhouding/toelage continuity; bruto JUMP vs pnl LOSS path",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Herentals>BosKat>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; bruto primary envelope (omzet empty); pnl LOSS FLIP primary absurdity + KBO Stopgezet fusie Groep Talent; dual NACE 02.100/88.993; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; REW YE2024; AGE FREE deferred; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "BosKat bruto JUMP 3.28m / pnl LOSS FLIP -207k / Stopgezet fusie Groep Talent (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory_stopgezet_fusie",
            "hierarchy_path": "Vlaanderen>Antwerpen>Herentals>BosKat>JR2025",
            "annual_cost_eur": str(BRUTO),
            "total_cost_eur": str(BRUTO),
            "tco_notes": "CW bruto JUMP envelope 3.28m (omzet empty) / pnl LOSS FLIP -207k from +250k (-183%) / equity DROP 1.55m -12% / FTE JUMP 78.5; KBO Stopgezet 2026-06-04 fusie Groep Talent 0459.644.990; wage/maatwerk subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers groen Herentals / municipal clients / public subsidy path",
            "stated_goal": "Sheltered green/forestry employment",
            "measured_outcome": "bruto JUMP +12.9%; pnl LOSS FLIP -183%; equity DROP -11.8%; FTE JUMP +9.2%; entity Stopgezet fusie 2026-06-04",
            "absurdity_score": "8.2",
            "cost_score": "4.8",
            "difficulty": "3.0",
            "priority_index": "6.8",
            "cut_proposal": "Publish NBB PDF assets/debt/omzet FOI; disclose LOSS FLIP vs bruto JUMP loonkost/maatwerksubsidie matrix; fusie Groep Talent toelage continuity",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO YE2024 REW YE2024; Antwerpen Herentals after De Schakel; AGE FREE deferred",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "BosKat VZW (Herentals) — Stopgezet fusie Groep Talent",
            "name_fr": "BosKat ASBL (Herentals) — cessée fusion Groep Talent",
            "name_en": "BosKat sheltered green workshop non-profit (Herentals) — stopped merger into Groep Talent",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.boskat.be/",
            "foi_email": "info@boskat.be",
            "foi_postal": "Kamergoor 19/1, 2200 Herentals",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0464.028.204 Stopgezet 2026-06-04 Fusie door overneming → 0459.644.990 Groep Talent; 1 VE BTW NACE 02.100 RSZ NACE 88.993; bruto JUMP {BRUTO} pnl LOSS FLIP {PNL} vs YE2024 +{PNL24} equity DROP {EQUITY} FTE JUMP {FTE}; omzet empty; neerlegging 20.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; AGE FREE deferred; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Herentals>BosKat>NBB_PDF_assets_debt_pnl_loss_flip_fusie",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal/omzet); pnl LOSS FLIP EUR{PNL} vs YE2024 EUR+{PNL24} (-183%) recon with bruto JUMP EUR{BRUTO} and FTE JUMP {FTE24}→{FTE}; loonkost/maatwerksubsidie/GESCO/ESF/VDAB/gemeente matrix; Fusie 2026-06-04 naar Groep Talent 0459.644.990 (ruilverhouding/activa/personeel/toelage continuity); dual NACE 02.100/88.993 split",
            "why_it_matters": "Medium CW + Strong KBO: Herentals maatwerk VZW posted LOSS FLIP -207k while bruto JUMP then Stopgezet via merger into Groep Talent; public subsidy path and successor toelage continuity opaque; omzet unpublished",
            "priority": "8",
            "recipient_body": "BosKat VZW / Groep Talent (rechtsopvolger)",
            "recipient_email": "info@boskat.be",
            "recipient_postal": "Kamergoor 19/1, 2200 Herentals",
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
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO Stopgezet/fusie; next every-10 2200",
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
    if row.get("task_id") == "rq_2198":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["blocked_gap_id"] = GAP
        row["title"] = (
            "leftover dual — BosKat YE2025 Medium (bruto JUMP 3.28m / pnl LOSS FLIP -207k / Stopgezet fusie Groep Talent)"
        )
        row["notes"] = (
            "tick2198; BosKat 0464.028.204 YE2025 Medium CW; Stopgezet fusie Groep Talent 0459.644.990; "
            "AGB Bornem JR2024; FARO YE2024; REW YE2024; AGE FREE deferred; next rq_2199; every-10 next 2200"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2198 missing")

if not any(r.get("task_id") == "rq_2199" for r in rows):
    rows.append(
        {
            "task_id": "rq_2199",
            "title": "leftover dual hole-fill after BosKat — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2199 after BosKat Herentals YE2025 Medium (bruto JUMP 3.28m / pnl LOSS FLIP -207k / Stopgezet fusie Groep Talent 0459.644.990 / FTE 78.5). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(Atelier Groot Eiland 0430.686.037 YE2025 FREE — bruto 2.93m / pnl JUMP 24k). "
                "Do NOT redo BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2198 BosKat; FARO/REW still YE2024; AGE YE2025 FREE; next every-10 2200",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2198=done rq_2199=open")

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
    "last_unit_id": "rq_2198",
    "ticks_completed": "2198",
    "paused": "no",
    "notes": (
        "tick2198 leftover BosKat 0464.028.204 Medium (bruto JUMP 3.28m; omzet empty; pnl LOSS FLIP -207k -183%; "
        "equity DROP 1.55m; FTE JUMP 78.5; Stopgezet fusie Groep Talent 0459.644.990 2026-06-04; 1 VE dual NACE 02.100/88.993); "
        "AGB Bornem JR2024; FARO YE2024; REW YE2024; AGE FREE deferred; next rq_2199; next every-10 2200; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2198 DONE")
