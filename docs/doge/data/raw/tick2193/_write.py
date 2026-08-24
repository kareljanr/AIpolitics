# tick2193 SW-WEB Turnhout YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T10:20:00Z"
TICK = "2193"
ENTITY = "vzw_sw_web_turnhout"
SRC_EN = "src_sw_web_jr2025_cw_en"
COMM = "comm_sw_web_jr2025_statutory_maatwerk_pnl_loss_deepen_equity_drop"
LB = "lb_sw_web_omzet_5_72m_pnl_loss_1_53m_equity_drop_jr2025"
GAP = "gap_sw_web_nbb_pdf_assets_debt_pnl_loss_deepen_equity_drop_bruto_gt_omzet_fte_jump_matrix_l5"

OMZET = 5723867
BRUTO = 7553796
PNL = -1527550
EQUITY = 2030983
FTE = 206.1
OMZET24 = 4943779
BRUTO24 = 7035034
PNL24 = -416876
EQUITY24 = 3578755
FTE24 = 172.3


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
            "source_id": "src_sw_web_jr2025_cw_nl",
            "title": "Companyweb NL SW-WEB YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0465707391/sociale-werkplaatsen-web",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl LOSS DEEPEN {PNL} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 30.06.2026; raw docs/doge/data/raw/tick2193/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN SW-WEB YE2025 statutory",
            "url": "https://www.companyweb.be/en/0465707391/sociale-werkplaatsen-web",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 30-06-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_sw_web_jr2025_cw_fr",
            "title": "Companyweb FR SW-WEB YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0465707391/sociale-werkplaatsen-web",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_sw_web_kbo_2193",
            "title": "KBO Sociale Werkplaatsen - WEB 0465.707.391 Actief VZW Turnhout 7 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0465707391",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2193; Actief VZW; Sociale Werkplaatsen - WEB / SW - WEB; Steenweg op Tielen 70 2300 Turnhout; 7 VE; RSZ NACE 88.993; email info@webwerkt.be; www.webwerkt.be",
        },
        {
            "source_id": "src_sw_web_foi_contact_2193",
            "title": "SW-WEB FOI channel info@webwerkt.be",
            "url": "https://webwerkt.be/contact/",
            "publisher": "WEB / webwerkt.be",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2193; info@webwerkt.be (+ coach@webwerkt.be); Steenweg op Tielen 70 2300 Turnhout; Kringwinkel WEB under SW-WEB VZW",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_sw_web_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +15.78% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_sw_web_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +7.37% vs YE2024 {BRUTO24}; bruto≫omzet",
        },
        {
            "budget_id": "bud_sw_web_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl LOSS DEEPEN -266.43% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_sw_web_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity DROP -43.25% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_sw_web_fte_jr2025_statutory",
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
            "title": "SW-WEB Turnhout YE2025 leftover dual (omzet JUMP 5.72m / pnl LOSS DEEPEN -1.53m / equity DROP -43%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / Kringwinkel WEB + social-economy Kempen Turnhout Beerse Hoogstraten Retie Merksplas",
            "legal_basis": "VZW maatwerk (KBO 0465.707.391; Actief; 7 VE; RSZ NACE 88.993; afkorting SW - WEB)",
            "decision_date": "2026-06-30",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0465707391/sociale-werkplaatsen-web",
            "stated_goal": "Sheltered employment / maatwerk + Kringwinkel reuse / circular jobs Kempen",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose LOSS deepen -1.53m vs YE2024 -417k + equity DROP -43% + bruto≫omzet + FTE JUMP while loss path",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Turnhout>SW_WEB>JR2025_statutory_L5",
            "notes": "tick2193 primary; Medium CW; omzet primary envelope; pnl LOSS DEEPEN + equity DROP -43% + bruto≫omzet + FTE JUMP primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW YE2024; deferred FREE BWZ/De Schakel/BosKat/AGE; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "SW-WEB omzet JUMP 5.72m / pnl LOSS DEEPEN -1.53m / equity DROP -43% (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>Turnhout>SW_WEB>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet JUMP envelope 5.72m / bruto 7.55m ≫ omzet / pnl LOSS DEEPEN -1.53m (-266% vs YE2024 -417k) / equity DROP 2.03m (-43%) / FTE JUMP 206.1; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Kempen / public loonkostsubsidie path / Kringwinkel WEB shoppers",
            "stated_goal": "Sheltered employment maatwerk + reuse",
            "measured_outcome": "omzet JUMP +15.8%; bruto JUMP +7.4%; pnl LOSS DEEPEN -266%; equity DROP -43.3%; FTE JUMP +19.6%",
            "absurdity_score": "7.4",
            "cost_score": "5.1",
            "difficulty": "3.0",
            "priority_index": "6.8",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose LOSS deepen -1.53m + equity DROP -43% while FTE JUMP; bruto≫omzet loonkostsubsidie/GESCO/ESF split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK} primary; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Antwerpen maatwerk dual after Mivas; deferred BWZ/De Schakel",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Sociale Werkplaatsen - WEB / SW-WEB VZW (Turnhout)",
            "name_fr": "Sociale Werkplaatsen - WEB / SW-WEB entreprise de travail adapté ASBL (Turnhout)",
            "name_en": "Sociale Werkplaatsen - WEB / SW-WEB sheltered workshop non-profit (Turnhout)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://webwerkt.be/",
            "foi_email": "info@webwerkt.be",
            "foi_postal": "Steenweg op Tielen 70, 2300 Turnhout",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0465.707.391 Actief VZW 7 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet) pnl LOSS DEEPEN {PNL} vs YE2024 {PNL24} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 30.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Kringwinkel WEB under SW-WEB; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Turnhout>SW_WEB>NBB_PDF_assets_debt_pnl_loss_deepen",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); pnl LOSS DEEPEN EUR{PNL} vs YE2024 EUR{PNL24} (-266%); equity DROP EUR{EQUITY24}→{EQUITY} (-43%); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} loonkostsubsidie/GESCO/ESF/VDAB matrix; FTE JUMP {FTE24}→{FTE} while LOSS deepens; 7 VE / Kringwinkel WEB cost allocation",
            "why_it_matters": "Medium CW shows Kempen maatwerk/Kringwinkel VZW with LOSS deepening to -1.53m and equity DROP -43% while FTE JUMP +20% — assets/debt unpublished under public loonkost path",
            "priority": "8",
            "recipient_body": "Sociale Werkplaatsen - WEB VZW (SW-WEB)",
            "recipient_email": "info@webwerkt.be",
            "recipient_postal": "Steenweg op Tielen 70, 2300 Turnhout",
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
    if row.get("task_id") == "rq_2193":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = (
            "leftover dual — SW-WEB YE2025 Medium (omzet JUMP 5.72m / pnl LOSS DEEPEN -1.53m / equity DROP -43%)"
        )
        row["instructions"] = (
            "Tick 2193 after Mivas Lier YE2025 Medium (omzet DROP 11.59m / bruto≫omzet ~2.1x / pnl JUMP +117% / FTE DROP 635). "
            "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS. "
            "Completed leftover SW-WEB after Mivas; preferred AGB Bornem JR2024 / FARO YE2024 / AIESH YE2024 / REW YE2024. "
            "Do NOT redo Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever."
        )
        row["notes"] = (
            "tick2193; SW-WEB 0465.707.391 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "AIESH/REW YE2024; deferred BWZ/De Schakel/BosKat/AGE; next rq_2194; every-10 next 2200"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2193 missing")

if not any(r.get("task_id") == "rq_2194" for r in rows):
    rows.append(
        {
            "task_id": "rq_2194",
            "title": "leftover dual hole-fill after SW-WEB — prefer AGB/FARO-YE2025/AIESH-REW/BWZ-De Schakel-or-unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2194 after SW-WEB Turnhout YE2025 Medium (omzet JUMP 5.72m / pnl LOSS DEEPEN -1.53m / equity DROP -43% / FTE JUMP 206). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else named FREE BWZ Zottegem 0407.657.148 (omzet 10.16m) / De Schakel Balen 0419.461.652 (bruto≫omzet ~7x) / BosKat / Atelier Groot Eiland, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS. "
                "Do NOT redo SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2193 SW-WEB; FARO/AIESH/REW still YE2024; deferred BWZ/De Schakel; next every-10 2200",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2193=done rq_2194=open")

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
    "last_unit_id": "rq_2193",
    "ticks_completed": "2193",
    "paused": "no",
    "notes": (
        "tick2193 leftover SW-WEB 0465.707.391 Medium (omzet JUMP 5.72m; bruto 7.55m ≫ omzet; pnl LOSS DEEPEN -1.53m -266% from -417k; "
        "equity DROP 2.03m -43%; FTE JUMP 206.1; 7 VE Turnhout); AGB Bornem JR2024; FARO YE2024; AIESH/REW YE2024; "
        "deferred BWZ/De Schakel; next rq_2194; next every-10 2200; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2193 DONE")
