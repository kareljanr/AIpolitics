# tick2191 writer — Demival YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T09:40:00Z"
TICK = "2191"
ENTITY = "vzw_demival_deinze"
SRC_EN = "src_demival_jr2025_cw_en"
COMM = "comm_demival_jr2025_statutory_maatwerk_pnl_flip_from_loss"
LB = "lb_demival_omzet_jump_14_76m_pnl_flip_from_loss_jr2025"
GAP = "gap_demival_nbb_pdf_assets_debt_pnl_flip_bruto_gt_omzet_fte_drop_matrix_l5"

OMZET = 14762543
BRUTO = 17592947
PNL = 380811
EQUITY = 13821531
FTE = 449.0
OMZET24 = 13820870
BRUTO24 = 20341759
PNL24 = -1005408
EQUITY24 = 13454050
FTE24 = 474.1


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
            "source_id": "src_demival_jr2025_cw_nl",
            "title": "Companyweb NL Demival YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407409007/demival-werkplaats-voor-aangepaste-arbeid-te-deinze",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl FLIP {PNL} from LOSS equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 01.06.2026; raw docs/doge/data/raw/tick2191/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Demival YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407409007/demival-werkplaats-voor-aangepaste-arbeid-te-deinze",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 01-06-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_demival_jr2025_cw_fr",
            "title": "Companyweb FR Demival YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407409007/demival-werkplaats-voor-aangepaste-arbeid-te-deinze",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_demival_kbo_2191",
            "title": "KBO Demival 0407.409.007 Actief VZW Deinze 1 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407409007",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2191; Actief VZW; Demival Werkplaats voor Aangepaste Arbeid te Deinze; Machelenstraat 169 9800 Deinze; 1 VE; RSZ NACE 88.993; KBO email empty",
        },
        {
            "source_id": "src_demival_foi_contact_2191",
            "title": "Demival FOI channel info@demival.be",
            "url": "https://www.demival.be/nl/contact",
            "publisher": "Demival VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2191; info@demival.be; Machelenstraat 169 9800 Deinze",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_demival_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +6.81% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_demival_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto DROP -13.51% vs YE2024 {BRUTO24}; bruto≫omzet",
        },
        {
            "budget_id": "bud_demival_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl FLIP to profit from YE2024 LOSS {PNL24}",
        },
        {
            "budget_id": "bud_demival_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +2.73% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_demival_fte_jr2025_statutory",
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
            "title": "Demival Deinze YE2025 leftover dual (omzet JUMP 14.76m / pnl FLIP +381k from LOSS -1.01m)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Oost-Vlaanderen Deinze",
            "legal_basis": "VZW maatwerk (KBO 0407.409.007; Actief; 1 VE; RSZ NACE 88.993; afkorting Demival)",
            "decision_date": "2026-06-01",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407409007/demival-werkplaats-voor-aangepaste-arbeid-te-deinze",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose LOSS→profit flip vs bruto DROP + loonkostsubsidie matrix behind bruto≫omzet",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Deinze>Demival>JR2025_statutory_L5",
            "notes": "tick2191; Medium CW; omzet primary envelope; pnl FLIP from LOSS primary absurdity; bruto≫omzet; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; named FREE after De Wroeter; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Demival omzet JUMP 14.76m / pnl FLIP +381k from LOSS -1.01m (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Deinze>Demival>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet JUMP envelope 14.76m / bruto 17.59m ≫ omzet / pnl FLIP +381k from YE2024 LOSS -1.01m / equity JUMP 13.82m / FTE DROP 449; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Deinze / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +6.8%; bruto DROP -13.5%; pnl FLIP from LOSS; equity JUMP +2.7%; FTE DROP -5.3%",
            "absurdity_score": "7.2",
            "cost_score": "5.9",
            "difficulty": "3.0",
            "priority_index": "6.4",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose LOSS→profit flip vs bruto DROP/FTE DROP; loonkostsubsidie/GESCO/ESF split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Oost-Vlaanderen maatwerk dual after De Wroeter/Kringwinkel Antwerpen",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Demival Werkplaats voor Aangepaste Arbeid te Deinze VZW",
            "name_fr": "Demival atelier de travail adapté Deinze ASBL",
            "name_en": "Demival sheltered workshop non-profit (Deinze)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.demival.be/",
            "foi_email": "info@demival.be",
            "foi_postal": "Machelenstraat 169, 9800 Deinze",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.409.007 Actief VZW 1 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet) pnl FLIP {PNL} from YE2024 LOSS {PNL24} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 01.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Deinze>Demival>NBB_PDF_assets_debt_pnl_flip",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); pnl FLIP EUR{PNL} vs YE2024 LOSS EUR{PNL24} recon; bruto DROP EUR{BRUTO} vs YE2024 EUR{BRUTO24} while omzet JUMP EUR{OMZET}; bruto≫omzet loonkostsubsidie/GESCO/ESF/VDAB matrix; FTE DROP {FTE24}→{FTE} path",
            "why_it_matters": "Medium CW shows Oost-Vlaanderen maatwerk VZW flipping from EUR1.01m LOSS to EUR381k profit while bruto DROPS -13.5% and FTE DROPS — assets/debt unpublished under public loonkost path",
            "priority": "8",
            "recipient_body": "DEMIVAL VZW",
            "recipient_email": "info@demival.be",
            "recipient_postal": "Machelenstraat 169, 9800 Deinze",
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
    if row.get("task_id") == "rq_2191":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = "leftover dual — Demival YE2025 Medium (omzet JUMP 14.76m / pnl FLIP +381k from LOSS -1.01m)"
        row["notes"] = (
            "tick2191; Demival 0407.409.007 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "AIESH/REW stall; named FREE after De Wroeter; next rq_2192; every-10 next 2200"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2191 missing")

if not any(r.get("task_id") == "rq_2192" for r in rows):
    rows.append(
        {
            "task_id": "rq_2192",
            "title": "leftover dual hole-fill after Demival — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2192 after Demival Deinze YE2025 Medium (omzet JUMP 14.76m / pnl FLIP +381k from LOSS -1.01m / bruto≫omzet / FTE DROP 449). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(Mivas FREE). "
                "Do NOT redo Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2191 Demival; FARO/AIESH/REW still YE2024; next every-10 2200",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2191=done rq_2192=open")

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
    "last_unit_id": "rq_2191",
    "ticks_completed": "2191",
    "paused": "no",
    "notes": (
        "tick2191 leftover DEMIVAL 0407.409.007 Medium (omzet JUMP 14.76m; bruto 17.59m ≫ omzet; pnl FLIP +381k from YE2024 LOSS -1.01m; "
        "equity JUMP 13.82m; FTE DROP 449; 1 VE Deinze); AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; "
        "next rq_2192; next every-10 2200; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2191 DONE")
