# tick2199 writer — Groep Talent Herentals YE2025 Medium CW (BosKat successor)
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T12:20:00Z"
TICK = "2199"
ENTITY = "vzw_groep_talent_herentals"
SRC_EN = "src_groep_talent_jr2025_cw_en"
COMM = "comm_groep_talent_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_drop_merger"
LB = "lb_groep_talent_omzet_6_24m_bruto_gt_omzet_pnl_drop_boskat_merger_jr2025"
GAP = "gap_groep_talent_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_drop_boskat_merger_matrix_l5"

OMZET = 6237312
BRUTO = 9237780
PNL = 292878
EQUITY = 5072589
FTE = 211.3
OMZET24 = 6121527
BRUTO24 = 8611443
PNL24 = 426827
EQUITY24 = 4217771
FTE24 = 200.0
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
            "source_id": "src_groep_talent_jr2025_cw_nl",
            "title": "Companyweb NL Groep Talent YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0459644990/groep-talent",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} (≫omzet ~{RATIO}x) pnl DROP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 23.06.2026; raw docs/doge/data/raw/tick2199/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Groep Talent YE2025 statutory",
            "url": "https://www.companyweb.be/en/0459644990/groep-talent",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 23-06-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_groep_talent_jr2025_cw_fr",
            "title": "Companyweb FR Groep Talent YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0459644990/groep-talent",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_groep_talent_kbo_2199",
            "title": "KBO Groep Talent 0459.644.990 Actief VZW 13 VE Herentals",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0459644990",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2199; Actief VZW; naam Groep Talent sinds 04.06.2026; Lichtaartseweg 22 Herentals; 13 VE; RSZ NACE 88.993; absorbed BosKat 0464.028.204 + BOSPAD + TWERK + Milieu en Werk + De Klus",
        },
        {
            "source_id": "src_groep_talent_foi_contact_2199",
            "title": "Groep Talent FOI channel info@groeptalent.be",
            "url": "https://groeptalent.be/",
            "publisher": "Groep Talent VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2199; info@groeptalent.be; Lichtaartseweg 22 2200 Herentals; +32 14 28 57 44",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_groep_talent_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +1.89% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_groep_talent_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +7.27% vs YE2024 {BRUTO24}; bruto≫omzet (~{RATIO}x)",
        },
        {
            "budget_id": "bud_groep_talent_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl DROP -31.38% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_groep_talent_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +20.27% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_groep_talent_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW social-balance FTE / Employees {FTE}",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; FTE JUMP vs YE2024 {FTE24}; assets/debt Unknown; post-YE2025 absorbed BosKat/BOSPAD/TWERK",
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
    "absorbed_2026": ["0464.028.204", "0830.795.694", "0447.553.545", "0459.240.362"],
}

append_csv(
    "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": f"Groep Talent Herentals YE2025 leftover dual (omzet JUMP 6.24m / bruto≫omzet ~{RATIO}x / pnl DROP -31% / BosKat merger)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Antwerpen Herentals Kempen / municipal partners",
            "legal_basis": "VZW maatwerk (KBO 0459.644.990; Actief; 13 VE; RSZ NACE 88.993; naam Groep Talent sinds 04.06.2026; absorbed BosKat/BOSPAD/TWERK)",
            "decision_date": "2026-06-23",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0459644990/groep-talent",
            "stated_goal": "Sheltered employment / maatwerk group consolidating regional workshops",
            "cut_option": f"Publish NBB PDF assets/debt FOI; disclose bruto~{RATIO}x omzet loonkost matrix + pnl DROP -31% + post-YE2025 BosKat/BOSPAD/TWERK merger continuity",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Herentals>GroepTalent>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; omzet primary envelope; bruto≫omzet (~{RATIO}x) + pnl DROP + multi-entity absorption primary absurdity; YE2025 pre-BosKat merger; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; AGE FREE deferred; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": f"Groep Talent omzet JUMP 6.24m / bruto≫omzet ~{RATIO}x / pnl DROP -31% / BosKat merger (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory_group",
            "hierarchy_path": "Vlaanderen>Antwerpen>Herentals>GroepTalent>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": f"CW omzet JUMP envelope 6.24m / bruto 9.24m ≫ omzet (~{RATIO}x) / pnl DROP 293k -31% from YE2024 427k / equity JUMP 5.07m +20% / FTE JUMP 211.3; post-YE2025 absorbed BosKat+BOSPAD+TWERK+Milieu en Werk; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Kempen / municipal contracts / public loonkost path",
            "stated_goal": "Sheltered employment maatwerk group",
            "measured_outcome": "omzet JUMP +1.9%; bruto JUMP +7.3%; pnl DROP -31.4%; equity JUMP +20.3%; FTE JUMP +5.7%; then multi-entity fusie 2026",
            "absurdity_score": "7.2",
            "cost_score": "5.5",
            "difficulty": "3.0",
            "priority_index": "6.6",
            "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose bruto~{RATIO}x omzet loonkost/GESCO/ESF split; pnl DROP while scale-up; BosKat merger subsidy continuity",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/REW YE2024; BosKat successor after tick2198; AGE deferred",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Groep Talent VZW (Herentals; opvolger BosKat/BOSPAD/TWERK)",
            "name_fr": "Groep Talent ASBL (Herentals; successeur BosKat/BOSPAD/TWERK)",
            "name_en": "Groep Talent sheltered workshop group (Herentals; BosKat successor)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://groeptalent.be/",
            "foi_email": "info@groeptalent.be",
            "foi_postal": "Lichtaartseweg 22, 2200 Herentals",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0459.644.990 Actief VZW 13 VE RSZ NACE 88.993; naam Groep Talent sinds 04.06.2026; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~{RATIO}x) pnl DROP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE JUMP {FTE}; absorbed BosKat/BOSPAD/TWERK/Milieu en Werk; neerlegging 23.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Herentals>GroepTalent>NBB_PDF_assets_debt_bruto_gt_omzet_merger",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix; pnl DROP EUR{PNL} vs YE2024 EUR{PNL24} (-31%); equity JUMP EUR{EQUITY}; FTE JUMP {FTE24}->{FTE}; post-YE2025 fusie matrix BosKat 0464.028.204 + BOSPAD + TWERK + Milieu en Werk continuity",
            "why_it_matters": f"Medium CW shows Herentals maatwerk group (6.24m omzet / 211 FTE / 13 VE) with bruto ~{RATIO}x omzet and pnl DROP -31% then absorbing BosKat and peers — public subsidy consolidation opaque",
            "priority": "8",
            "recipient_body": "Groep Talent VZW",
            "recipient_email": "info@groeptalent.be",
            "recipient_postal": "Lichtaartseweg 22, 2200 Herentals",
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
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; BosKat successor; next every-10 2200",
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
    if row.get("task_id") == "rq_2199":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["blocked_gap_id"] = GAP
        row["title"] = f"leftover dual — Groep Talent YE2025 Medium (omzet JUMP 6.24m / bruto≫omzet ~{RATIO}x / pnl DROP -31%)"
        row["notes"] = (
            "tick2199; Groep Talent 0459.644.990 YE2025 Medium CW; BosKat successor 13 VE; "
            "AGB Bornem JR2024; FARO/REW YE2024; AGE FREE deferred; next rq_2200 EVERY-10; every-10 next 2200"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2199 missing")

if not any(r.get("task_id") == "rq_2200" for r in rows):
    rows.append(
        {
            "task_id": "rq_2200",
            "title": "EVERY-10 + leftover dual hole-fill after Groep Talent — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2200 EVERY-10 after Groep Talent Herentals YE2025 Medium (omzet JUMP 6.24m / bruto≫omzet / pnl DROP -31% / BosKat merger). "
                "MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(Atelier Groot Eiland 0430.686.037 YE2025 FREE). "
                "Do NOT redo Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2199 Groep Talent; EVERY-10 mandatory; FARO/REW still YE2024; next every-10 2210",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2199=done rq_2200=open EVERY-10")

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
    "last_unit_id": "rq_2199",
    "ticks_completed": "2199",
    "paused": "no",
    "notes": (
        f"tick2199 leftover Groep Talent 0459.644.990 Medium (omzet JUMP 6.24m; bruto 9.24m ≫ omzet ~{RATIO}x; pnl DROP 293k -31%; "
        "equity JUMP 5.07m; FTE JUMP 211.3; 13 VE; BosKat/BOSPAD/TWERK absorber); AGB Bornem JR2024; FARO/REW YE2024; "
        "next rq_2200 EVERY-10; next every-10 2200; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2199 DONE")
