# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)

UTC = "2026-08-27T11:35:00Z"
TICK = 2278
ENTITY = "vzw_in_z_genk"
GAP = "gap_inz_nbb_pdf_assets_debt_bruto_gt_omzet_1_67x_pnl_loss_widen_fte_drop_matrix_l5"
LB = "lb_inz_omzet_14_36m_bruto_gt_omzet_1_67x_pnl_loss_widen_jr2025"
COMM = "comm_inz_jr2025_statutory_maatwerk_omzet_14_36m_bruto_gt_omzet_1_67x_pnl_loss_widen"
SRC_EN = "src_inz_jr2025_cw_en"
SRC_NL = "src_inz_jr2025_cw_nl"
SRC_FR = "src_inz_jr2025_cw_fr"
SRC_KBO = "src_inz_kbo_2278"
SRC_SITE = "src_inz_site_contact_2278"

OMZET = 14355222
OMZET24 = 13622265
BRUTO = 24032922
BRUTO24 = 23250794
PNL = -355830
PNL24 = -15581
EQUITY = 4491452
EQUITY24 = 4857282
FTE = 627.5
FTE24 = 647.1
RATIO = round(BRUTO / OMZET, 2)


def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        return list(r), list(r.fieldnames)


def write_csv(path, rows, fields):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


base = Path("docs/doge/data")

# --- sources ---
rows, fields = read_csv(base / "sources.csv")
sources_new = [
    {
        **{k: "" for k in fields},
        "source_id": SRC_EN,
        "title": "Companyweb EN In-Z YE2025 Genk (omzet 14.36m / bruto 24.03m / pnl LOSS WIDEN)",
        "url": "https://www.companyweb.be/en/0457521086/in-z",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "commercial_aggregator",
        "notes": f"tick{TICK}; Medium CW YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 31.07.2026",
    },
    {
        **{k: "" for k in fields},
        "source_id": SRC_NL,
        "title": "Companyweb NL In-Z YE2025 Genk",
        "url": "https://www.companyweb.be/nl/0457521086/in-z",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "commercial_aggregator",
        "notes": f"tick{TICK}; Medium CW NL YE2025 kerncijfers",
    },
    {
        **{k: "" for k in fields},
        "source_id": SRC_FR,
        "title": "Companyweb FR In-Z YE2025 Genk",
        "url": "https://www.companyweb.be/fr/0457521086/in-z",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "commercial_aggregator",
        "notes": f"tick{TICK}; Medium CW FR YE2025",
    },
    {
        **{k: "" for k in fields},
        "source_id": SRC_KBO,
        "title": "KBO In-Z 0457.521.086 Actief Genk 10 VE",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0457521086",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; Actief VZW IN-Z; zetel Welzijnscampus 5 bus 11 3600 Genk; 10 VE; NACE 88.999; aanbestedende overheid; RSZ werkgever",
    },
    {
        **{k: "" for k in fields},
        "source_id": SRC_SITE,
        "title": "In-Z FOI channel info@in-z.be",
        "url": "https://in-z.be/",
        "publisher": "IN-Z vzw",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; info@in-z.be; Welzijnscampus 5 bus 11 3600 Genk; +32 89 32 28 10",
    },
]
existing = {r["source_id"] for r in rows}
for s in sources_new:
    if s["source_id"] not in existing:
        rows.append(s)
write_csv(base / "sources.csv", rows, fields)
print("sources", len(rows))

# --- entities ---
rows, fields = read_csv(base / "entities.csv")
if not any(r["entity_id"] == ENTITY for r in rows):
    rows.append(
        {
            **{k: "" for k in fields},
            "entity_id": ENTITY,
            "name_nl": "IN-Z VZW (Genk / sociale economie / maatwerk-adjacent thuishulp)",
            "name_fr": "IN-Z ASBL (Genk / economie sociale / aide a domicile)",
            "name_en": "IN-Z adapted-work / social-economy ASBL (Genk Flemish maatwerk-adjacent)",
            "level": "parastatal",
            "parent_id": "sec_s1312",
            "community_language": "nl",
            "website": "https://in-z.be/",
            "foi_email": "info@in-z.be",
            "foi_postal": "Welzijnscampus 5 bus 11, 3600 Genk",
            "notes": (
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0457.521.086 Actief 10 VE NACE 88.999; "
                f"omzet JUMP {OMZET} (+5.38%) bruto JUMP {BRUTO} (~{RATIO}x / +3.36%) pnl LOSS WIDEN {PNL} "
                f"(< -1000% vs {PNL24}) equity DROP {EQUITY} (-7.53%) FTE DROP {FTE} (vs {FTE24}); "
                f"neerlegging 31.07.2026; assets/debt Unknown; FOI {GAP}"
            ),
        }
    )
write_csv(base / "entities.csv", rows, fields)
print("entities", len(rows))

# --- budgets ---
rows, fields = read_csv(base / "budgets.csv")
buds = [
    ("bud_inz_omzet_jr2025_statutory", OMZET, "CW statutory omzet YE2025", "2025", f"tick{TICK}; Medium CW; omzet JUMP {OMZET} (+5.38% vs {OMZET24})"),
    ("bud_inz_bruto_jr2025_statutory", BRUTO, "CW statutory bruto YE2025", "2025", f"tick{TICK}; Medium CW; bruto JUMP {BRUTO} (~{RATIO}x omzet / +3.36% vs {BRUTO24})"),
    ("bud_inz_pnl_jr2025_statutory", PNL, "CW statutory pnl YE2025", "2025", f"tick{TICK}; Medium CW; pnl LOSS WIDEN {PNL} (< -1000% vs YE2024 {PNL24})"),
    ("bud_inz_equity_jr2025_statutory", EQUITY, "CW statutory equity YE2025", "2025", f"tick{TICK}; Medium CW; equity DROP {EQUITY} (-7.53% vs {EQUITY24})"),
    ("bud_inz_fte_jr2025_statutory", FTE, "CW social-balance FTE 627.5", "2025", f"tick{TICK}; Medium CW; FTE {FTE} vs YE2024 {FTE24}"),
    ("bud_inz_pnl_jr2024_statutory_cmp", PNL24, "CW statutory pnl YE2024 comparative", "2024", f"tick{TICK}; YE2024 cmp pnl {PNL24}"),
]
existing_b = {r["budget_id"] for r in rows}
for bid, amt, basis, year, notes in buds:
    if bid not in existing_b:
        rows.append(
            {
                **{k: "" for k in fields},
                "budget_id": bid,
                "entity_id": ENTITY,
                "year": year,
                "amount_eur": str(amt),
                "amount_min_eur": str(amt),
                "amount_max_eur": str(amt),
                "basis": basis,
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": notes,
            }
        )
write_csv(base / "budgets.csv", rows, fields)
print("budgets", len(rows))

# --- commitments ---
rows, fields = read_csv(base / "commitments.csv")
cash = (
    '{"2025_omzet":%d,"2025_bruto":%d,"2025_pnl":%d,"2025_equity":%d,"2025_fte":%s,'
    '"2024_omzet":%d,"2024_bruto":%d,"2024_pnl":%d,"2024_equity":%d,"2024_fte":%s}'
    % (OMZET, BRUTO, PNL, EQUITY, FTE, OMZET24, BRUTO24, PNL24, EQUITY24, FTE24)
)
if not any(r["commitment_id"] == COMM for r in rows):
    rows.append(
        {
            **{k: "" for k in fields},
            "commitment_id": COMM,
            "title": f"IN-Z YE2025 leftover dual (omzet JUMP 14.36m / bruto~{RATIO}x / pnl LOSS WIDEN / FTE 627.5 / Medium)",
            "entity_id": ENTITY,
            "beneficiary": "Flemish social-economy / maatwerk-adjacent workers Genk (thuishulp/buurtdiensten path)",
            "legal_basis": "VZW IN-Z (KBO 0457.521.086; Actief; 10 VE; NACE 88.999; Genk; aanbestedende overheid)",
            "decision_date": "2026-07-31",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": cash,
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0457521086/in-z",
            "stated_goal": "Flemish social-economy ASBL Genk (thuishulp / buurtdiensten / local social employment)",
            "cut_option": f"Publish NBB PDF assets/debt FOI; reconcile bruto~{RATIO}x omzet + pnl LOSS WIDEN vs subsidy/maatwerk matrix",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Limburg>Genk>IN_Z>JR2025_statutory_L5",
            "notes": (
                f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; bruto {BRUTO} ~{RATIO}x; "
                f"pnl LOSS WIDEN {PNL}; equity DROP {EQUITY}; FTE {FTE}; FOI {GAP}"
            ),
        }
    )
write_csv(base / "commitments.csv", rows, fields)
print("commitments", len(rows))

# --- leaderboard ---
rows, fields = read_csv(base / "leaderboard.csv")
if not any(r["item_id"] == LB for r in rows):
    rows.append(
        {
            **{k: "" for k in fields},
            "item_id": LB,
            "name": f"IN-Z omzet JUMP 14.36m / bruto~{RATIO}x / pnl LOSS WIDEN -0.36m / FTE 627.5 (YE2025 Genk social-economy)",
            "level": "L5",
            "type": "maatwerk_asbl_statutory",
            "hierarchy_path": "Vlaanderen>Limburg>Genk>IN_Z>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(BRUTO),
            "tco_notes": (
                f"CW omzet JUMP {OMZET} (+5.38%) / bruto JUMP {BRUTO} (~{RATIO}x / +3.36%) / "
                f"pnl LOSS WIDEN {PNL} (< -1000% vs {PNL24}) / equity DROP {EQUITY} (-7.53%) / "
                f"FTE DROP {FTE} (vs {FTE24}) / filed 31.07.2026; assets/debt Unknown"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "Social-economy / maatwerk-adjacent workers Genk (thuishulp/buurtdiensten)",
            "stated_goal": "Flemish social-economy ASBL Genk (local care + employment)",
            "measured_outcome": (
                f"omzet JUMP +5.38%; bruto~{RATIO}x; pnl LOSS WIDEN < -1000%; equity DROP -7.53%; "
                f"FTE DROP {FTE}; filed 31.07.2026"
            ),
            "absurdity_score": "6.8",
            "cost_score": "6.9",
            "difficulty": "3.0",
            "priority_index": "6.80",
            "cut_proposal": f"Publish NBB PDF assets/debt FOI; disclose subsidy/maatwerk matrix behind bruto~{RATIO}x + pnl LOSS WIDEN",
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls FARO/AIESH/Citeco/Foes YE2024; "
                f"AGB Bornem JR2024; after C.A.R.P.@2277"
            ),
        }
    )
write_csv(base / "leaderboard.csv", rows, fields)
print("leaderboard", len(rows))

# --- foi_queue ---
rows, fields = read_csv(base / "foi_queue.csv")
if not any(r["gap_id"] == GAP for r in rows):
    rows.append(
        {
            **{k: "" for k in fields},
            "gap_id": GAP,
            "hierarchy_path": f"Vlaanderen>Limburg>Genk>IN_Z>NBB_PDF_assets_debt_bruto_gt_omzet_{RATIO}x_pnl_loss_widen",
            "entity_id": ENTITY,
            "what_is_missing": (
                f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BRUTO} vs omzet EUR{OMZET} "
                f"(~{RATIO}x); pnl LOSS WIDEN EUR{PNL}; equity DROP EUR{EQUITY}; FTE DROP {FTE}; subsidy/maatwerk matrix Unknown"
            ),
            "why_it_matters": (
                f"Medium CW shows Flemish social-economy ASBL (omzet 14.36m / bruto 24.03m ~{RATIO}x / "
                f"pnl LOSS WIDEN / FTE 627.5) under public path; assets/debt/subsidy matrix opaque"
            ),
            "priority": "8",
            "recipient_body": "IN-Z VZW",
            "recipient_email": "info@in-z.be",
            "recipient_postal": "Welzijnscampus 5 bus 11, 3600 Genk",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-27",
            "linked_commitment_id": COMM,
            "linked_leaderboard_id": LB,
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/Citeco/Foes YE2024; "
                f"AGB Bornem JR2024; after C.A.R.P.@2277"
            ),
        }
    )
write_csv(base / "foi_queue.csv", rows, fields)
print("foi_queue", len(rows))

# --- research_queue ---
rows, fields = read_csv(base / "research_queue.csv")
for r in rows:
    if r["task_id"] == "rq_2278":
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = UTC
        r["title"] = "leftover dual — IN-Z YE2025 Medium (omzet JUMP 14.36m / bruto~1.67x / pnl LOSS WIDEN / FTE 627.5)"
        r["notes"] = (
            f"tick{TICK}; IN-Z VZW Genk 0457.521.086 YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET} (+5.38%); bruto JUMP {BRUTO} (~{RATIO}x / +3.36%); "
            f"pnl LOSS WIDEN {PNL} (< -1000% vs {PNL24}); equity DROP {EQUITY} (-7.53%); "
            f"FTE DROP {FTE} (vs {FTE24}); 10 VE; NACE 88.999; neerlegging 31.07.2026; FOI {GAP} ready; "
            f"preferred stalls FARO/AIESH/Citeco/Foes YE2024; AGB Bornem JR2024; next every-10 2280"
        )
if not any(r["task_id"] == "rq_2279" for r in rows):
    rows.append(
        {
            **{k: "" for k in fields},
            "task_id": "rq_2279",
            "title": "leftover dual after IN-Z — prefer AGB/FARO-YE2025/AIESH-REW/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after rq_2278 IN-Z YE2025 Medium primary (omzet JUMP 14.36m / bruto~{RATIO}x / "
                f"pnl LOSS WIDEN / FTE 627.5). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                f"else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else named FREE Citeco if YE2025 / "
                f"Groupe Foes if YE2025, else unused ETA-VAPH-WZC-maatwerk with live sourced euros. Do NOT redo "
                f"IN-Z/C.A.R.P./Atelier Saint-Vincent/A.P.A.C./Adapta/Atelier 85/La Gaume/De Enter/Fournipac/Le Rucher/"
                f"Metalgroup/APAM/Jeunes Jardiniers/Pilifs/TRAVCO stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} IN-Z primary; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                f"AGB Bornem JR2024; next every-10 2280"
            ),
        }
    )
write_csv(base / "research_queue.csv", rows, fields)
print("research_queue", len(rows))

# --- loop_state ---
rows, fields = read_csv(base / "loop_state.csv")
for r in rows:
    r["mode"] = "continuous"
    r["current_sprint"] = "hole_fill"
    r["last_tick_utc"] = UTC
    r["last_unit_id"] = "rq_2278"
    r["ticks_completed"] = str(TICK)
    r["paused"] = "no"
    r["notes"] = (
        f"tick{TICK} leftover dual IN-Z 0457.521.086 Medium (omzet JUMP {OMZET} +5.38%; bruto JUMP {BRUTO} ~{RATIO}x; "
        f"pnl LOSS WIDEN {PNL}; equity DROP {EQUITY} -7.53%; FTE DROP {FTE}; 10 VE Genk); after C.A.R.P.@2277; "
        f"FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; next rq_2279; next EVERY-10 2280; continuous hole_fill"
    )
write_csv(base / "loop_state.csv", rows, fields)
print("loop_state ok")
print("DONE core CSVs")
