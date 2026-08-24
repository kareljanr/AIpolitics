# tick2203 writer — De Kromme Boom Gent YE2025 Medium CW (equity NEG FLIP)
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T13:40:00Z"
TICK = "2203"
ENTITY = "vzw_de_kromme_boom_gent"
SRC_EN = "src_kromme_boom_jr2025_cw_en"
COMM = "comm_kromme_boom_jr2025_statutory_maatwerk_equity_neg_flip_pnl_loss"
LB = "lb_kromme_boom_omzet_1_20m_equity_neg_flip_pnl_loss_jr2025"
GAP = "gap_kromme_boom_nbb_pdf_assets_debt_equity_neg_flip_pnl_loss_matrix_l5"

OMZET = 1195537
BRUTO = 996352
PNL = -86344
EQUITY = -78999
FTE = 27.5
BRUTO24 = 877185
PNL24 = -155302
EQUITY24 = 7345
FTE24 = 26.2


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
            "source_id": "src_kromme_boom_jr2025_cw_nl",
            "title": "Companyweb NL De Kromme Boom YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0454426489/maatwerkbedrijf-de-kromme-boom",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet {OMZET} bruto JUMP {BRUTO} pnl LOSS IMPROVED {PNL} equity NEG FLIP {EQUITY} FTE JUMP {FTE}; neerlegging 12.06.2026; prior omzet unpublished on CW; raw docs/doge/data/raw/tick2203/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN De Kromme Boom YE2025 statutory",
            "url": "https://www.companyweb.be/en/0454426489/maatwerkbedrijf-de-kromme-boom",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 12-06-2026; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_kromme_boom_jr2025_cw_fr",
            "title": "Companyweb FR De Kromme Boom YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0454426489/maatwerkbedrijf-de-kromme-boom",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_kromme_boom_kbo_2203",
            "title": "KBO De Kromme Boom 0454.426.489 Actief VZW 4 VE Gent",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0454426489",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2203; Actief VZW Maatwerkbedrijf De Kromme Boom; Eikstraat 81 9041 Gent; 4 VE; RSZ NACE 88.993; BTW farming/groothandel",
        },
        {
            "source_id": "src_kromme_boom_foi_contact_2203",
            "title": "De Kromme Boom FOI channel dekrommeboom@telenet.be",
            "url": "https://www.desocialekaart.be/de-kromme-boom-sociale-werkplaats-533686",
            "publisher": "Sociale Kaart / De Kromme Boom VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2203; dekrommeboom@telenet.be; 09 251 64 54; Eikstraat 81 9041 Oostakker; site www.dekrommeboom.be",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_kromme_boom_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; prior-year omzet unpublished on CW",
        },
        {
            "budget_id": "bud_kromme_boom_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +13.59% vs YE2024 {BRUTO24}",
        },
        {
            "budget_id": "bud_kromme_boom_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl LOSS IMPROVED +44.4% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_kromme_boom_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity NEG FLIP vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_kromme_boom_fte_jr2025_statutory",
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
    "2024_bruto": BRUTO24,
    "2024_pnl": PNL24,
    "2024_equity": EQUITY24,
    "2024_fte": FTE24,
    "2024_omzet": None,
}

append_csv(
    "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": "De Kromme Boom Gent YE2025 leftover dual (omzet 1.20m / equity NEG FLIP -79k / pnl LOSS IMPROVED -86k)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / mushroom farming clients Oost-Vlaanderen Gent Oostakker",
            "legal_basis": "VZW maatwerk (KBO 0454.426.489; Actief; 4 VE; RSZ NACE 88.993; BTW farming/groothandel)",
            "decision_date": "2026-06-12",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0454426489/maatwerkbedrijf-de-kromme-boom",
            "stated_goal": "Sheltered employment / circular oyster-mushroom farming maatwerk",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose equity NEG FLIP continuity and persistent LOSS subsidy path",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>DeKrommeBoom>JR2025_statutory_L5",
            "notes": "tick2203; Medium CW; omzet primary envelope; equity NEG FLIP primary absurdity; prior omzet unpublished; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "De Kromme Boom omzet 1.20m / equity NEG FLIP -79k / pnl LOSS IMPROVED -86k (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>DeKrommeBoom>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet envelope 1.20m / bruto 1.00m / pnl LOSS IMPROVED -86k from YE2024 -155k / equity NEG FLIP -79k from +7k / FTE 27.5; Gent oyster-mushroom maatwerk; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Gent Oostakker / public loonkost path",
            "stated_goal": "Sheltered employment + circular mushroom farming",
            "measured_outcome": "omzet 1.20m (prior unpublished); bruto JUMP +13.6%; pnl LOSS IMPROVED +44.4%; equity NEG FLIP; FTE JUMP +5.0%",
            "absurdity_score": "8.0",
            "cost_score": "3.8",
            "difficulty": "3.0",
            "priority_index": "6.7",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose equity NEG FLIP continuity + persistent LOSS under public subsidy path",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/REW YE2024; Gent maatwerk dual after Kaliber/Aarova/De Winning",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Maatwerkbedrijf De Kromme Boom VZW (Gent Oostakker)",
            "name_fr": "Maatwerkbedrijf De Kromme Boom ASBL (Gand)",
            "name_en": "De Kromme Boom sheltered workshop / mushroom farm (Ghent)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.dekrommeboom.be/",
            "foi_email": "dekrommeboom@telenet.be",
            "foi_postal": "Eikstraat 81, 9041 Gent",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0454.426.489 Actief VZW 4 VE RSZ NACE 88.993; omzet {OMZET} bruto JUMP {BRUTO} pnl LOSS IMPROVED {PNL} vs YE2024 {PNL24} equity NEG FLIP {EQUITY} vs {EQUITY24} FTE JUMP {FTE}; neerlegging 12.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>DeKrommeBoom>NBB_PDF_assets_debt_equity_neg_flip",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); equity NEG FLIP EUR{EQUITY} vs YE2024 EUR{EQUITY24}; pnl LOSS EUR{PNL} vs YE2024 EUR{PNL24}; omzet EUR{OMZET} (prior years unpublished on CW); bruto EUR{BRUTO}; FTE JUMP {FTE24}->{FTE}; loonkostsubsidie/Actiris/ESF/gemeente matrix; 4 VE cost allocation",
            "why_it_matters": "Medium CW shows Gent maatwerk VZW with equity NEG FLIP and multi-year LOSS under public subsidy path while assets/debt unpublished",
            "priority": "8",
            "recipient_body": "Maatwerkbedrijf De Kromme Boom VZW",
            "recipient_email": "dekrommeboom@telenet.be",
            "recipient_postal": "Eikstraat 81, 9041 Gent",
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
    if row.get("task_id") == "rq_2203":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["blocked_gap_id"] = GAP
        row["title"] = "leftover dual — De Kromme Boom YE2025 Medium (omzet 1.20m / equity NEG FLIP -79k / pnl LOSS IMPROVED)"
        row["notes"] = (
            "tick2203; De Kromme Boom 0454.426.489 YE2025 Medium CW; AGB Bornem JR2024; FARO/REW YE2024; "
            "next rq_2204; every-10 next 2210"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2203 missing")

if not any(r.get("task_id") == "rq_2204" for r in rows):
    rows.append(
        {
            "task_id": "rq_2204",
            "title": "leftover dual hole-fill after De Kromme Boom — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2204 after De Kromme Boom Gent YE2025 Medium (omzet 1.20m / equity NEG FLIP -79k / pnl LOSS IMPROVED -86k). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(FREE: Oesterbank/Werkhuizen MIN/Trianval/Noordheuvel/Arcor/ACG/Entiris/Odas/Kemphaan). "
                "Do NOT redo De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2203 De Kromme Boom; FARO/REW still YE2024; next every-10 2210",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2203=done rq_2204=open")

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
    "last_unit_id": "rq_2203",
    "ticks_completed": "2203",
    "paused": "no",
    "notes": (
        "tick2203 leftover De Kromme Boom 0454.426.489 Medium (omzet 1.20m; bruto JUMP 1.00m; pnl LOSS IMPROVED -86k; "
        "equity NEG FLIP -79k; FTE JUMP 27.5; 4 VE Gent); AGB Bornem JR2024; FARO/REW YE2024; "
        "next rq_2204; next every-10 2210; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2203 DONE")
