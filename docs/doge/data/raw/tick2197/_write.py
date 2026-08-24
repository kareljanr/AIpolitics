# tick2197 writer — De Schakel Balen YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T11:40:00Z"
TICK = "2197"
ENTITY = "vzw_de_schakel_balen"
SRC_EN = "src_de_schakel_jr2025_cw_en"
COMM = "comm_de_schakel_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_drop"
LB = "lb_de_schakel_omzet_1_15m_bruto_gt_omzet_7x_pnl_drop_jr2025"
GAP = "gap_de_schakel_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_drop_matrix_l5"

OMZET = 1152998
BRUTO = 8401955
PNL = 117525
EQUITY = 5997414
FTE = 109.1
OMZET24 = 1092441
BRUTO24 = 8049474
PNL24 = 230036
EQUITY24 = 5975243
FTE24 = 104.8
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
            "source_id": "src_de_schakel_jr2025_cw_nl",
            "title": "Companyweb NL De Schakel Balen YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0419461652/de-schakel",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} (≫omzet ~{RATIO}x) pnl DROP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 16.06.2026; raw docs/doge/data/raw/tick2197/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN De Schakel Balen YE2025 statutory",
            "url": "https://www.companyweb.be/en/0419461652/de-schakel",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 16-06-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_de_schakel_jr2025_cw_fr",
            "title": "Companyweb FR De Schakel Balen YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0419461652/de-schakel",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_de_schakel_kbo_2197",
            "title": "KBO De Schakel 0419.461.652 Actief VZW Balen 2 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419461652",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2197; Actief VZW De Schakel; Schakelveld 20 2490 Balen; 2 VE; BTW NACE 87.202 + RSZ NACE 88.993; KBO email empty",
        },
        {
            "source_id": "src_de_schakel_foi_contact_2197",
            "title": "De Schakel Balen FOI channel info@vzwdeschakel.be",
            "url": "https://www.desocialekaart.be/de-schakel-514640",
            "publisher": "Sociale Kaart / De Schakel VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2197; info@vzwdeschakel.be; Schakelveld 20 2490 Balen; 014 81 37 56; site www.vzwdeschakel.be",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_de_schakel_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +5.54% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_de_schakel_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +4.38% vs YE2024 {BRUTO24}; bruto≫omzet (~{RATIO}x)",
        },
        {
            "budget_id": "bud_de_schakel_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl DROP -48.91% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_de_schakel_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +0.37% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_de_schakel_fte_jr2025_statutory",
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
            "title": f"De Schakel Balen YE2025 leftover dual (omzet JUMP 1.15m / bruto≫omzet ~{RATIO}x / pnl DROP -49%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / residential care clients Antwerpen Balen",
            "legal_basis": "VZW maatwerk+zorg (KBO 0419.461.652; Actief; 2 VE; BTW NACE 87.202; RSZ NACE 88.993)",
            "decision_date": "2026-06-16",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0419461652/de-schakel",
            "stated_goal": "Sheltered employment / residential care for adults with mental disability",
            "cut_option": f"Publish NBB PDF assets/debt FOI; disclose bruto~{RATIO}x omzet loonkost/zorgsubsidie matrix + pnl DROP -49%",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Balen>DeSchakel>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; omzet primary envelope; bruto≫omzet (~{RATIO}x) + pnl DROP primary absurdity; dual NACE 87.202/88.993; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH 404/REW YE2024; BosKat/AGE FREE deferred; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": f"De Schakel omzet JUMP 1.15m / bruto≫omzet ~{RATIO}x / pnl DROP -49% (YE2025)",
            "level": "L5",
            "type": "maatwerk_zorg_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>Balen>DeSchakel>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": f"CW omzet JUMP envelope 1.15m / bruto 8.40m ≫ omzet (~{RATIO}x) / pnl DROP 118k -49% from YE2024 230k / equity JUMP 6.00m / FTE JUMP 109.1; dual zorg+maatwerk NACE; wage/care subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers / residential clients Balen / public subsidy path",
            "stated_goal": "Sheltered employment + residential care",
            "measured_outcome": "omzet JUMP +5.5%; bruto JUMP +4.4%; pnl DROP -48.9%; equity JUMP +0.4%; FTE JUMP +4.1%",
            "absurdity_score": "8.2",
            "cost_score": "4.2",
            "difficulty": "3.0",
            "priority_index": "7.0",
            "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose bruto~{RATIO}x omzet loonkost/zorgsubsidie/GESCO/ESF/VAPH split; pnl DROP path",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO YE2024 AIESH 404 REW YE2024; Antwerpen Balen dual after BWZ/Bewel",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "De Schakel VZW (Balen)",
            "name_fr": "De Schakel ASBL (Balen)",
            "name_en": "De Schakel sheltered workshop / care non-profit (Balen)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.vzwdeschakel.be/",
            "foi_email": "info@vzwdeschakel.be",
            "foi_postal": "Schakelveld 20, 2490 Balen",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0419.461.652 Actief VZW 2 VE BTW NACE 87.202 RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~{RATIO}x) pnl DROP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 16.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW stall; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Balen>DeSchakel>NBB_PDF_assets_debt_bruto_gt_omzet",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) loonkost/zorgsubsidie/GESCO/ESF/VAPH/VDAB/gemeente matrix; pnl DROP EUR{PNL} vs YE2024 EUR{PNL24} (-49%); dual NACE 87.202/88.993 split; 2 VE cost allocation",
            "why_it_matters": f"Medium CW shows Balen maatwerk+zorg VZW with bruto ~{RATIO}x omzet and pnl DROP -49% under public subsidy path while assets/debt unpublished",
            "priority": "8",
            "recipient_body": "De Schakel VZW",
            "recipient_email": "info@vzwdeschakel.be",
            "recipient_postal": "Schakelveld 20, 2490 Balen",
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
    if row.get("task_id") == "rq_2197":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["blocked_gap_id"] = GAP
        row["title"] = f"leftover dual — De Schakel YE2025 Medium (omzet JUMP 1.15m / bruto≫omzet ~{RATIO}x / pnl DROP -49%)"
        row["notes"] = (
            "tick2197; De Schakel 0419.461.652 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "AIESH 404/REW YE2024; BosKat/AGE FREE deferred; next rq_2198; every-10 next 2200"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2197 missing")

if not any(r.get("task_id") == "rq_2198" for r in rows):
    rows.append(
        {
            "task_id": "rq_2198",
            "title": "leftover dual hole-fill after De Schakel — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"Tick 2198 after De Schakel Balen YE2025 Medium (omzet JUMP 1.15m / bruto≫omzet ~{RATIO}x / pnl DROP -49% / FTE 109). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(BosKat / Atelier Groot Eiland 0430.686.037 FREE). "
                "Do NOT redo De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2197 De Schakel; FARO/AIESH/REW still YE2024; next every-10 2200",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2197=done rq_2198=open")

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
    "last_unit_id": "rq_2197",
    "ticks_completed": "2197",
    "paused": "no",
    "notes": (
        f"tick2197 leftover De Schakel 0419.461.652 Medium (omzet JUMP 1.15m; bruto 8.40m ≫ omzet ~{RATIO}x; pnl DROP 118k -49%; "
        "equity JUMP 6.00m; FTE JUMP 109.1; 2 VE Balen dual NACE 87.202/88.993); AGB Bornem JR2024; FARO YE2024; AIESH 404/REW YE2024; "
        "next rq_2198; next every-10 2200; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2197 DONE")
