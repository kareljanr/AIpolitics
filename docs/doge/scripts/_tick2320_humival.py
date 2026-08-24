# tick 2320 EVERY-10 + Humival Lievegem YE2025
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path("docs/doge/data")
TICK = "2320"
TS = "2026-08-27T23:20:00Z"
ENTITY = "vzw_humival_lievegem"
GAP = "gap_humival_nbb_pdf_assets_debt_bruto_gt_omzet_7_80x_pnl_jump_vaph_matrix_l5"
LB = "lb_humival_bruto_5_78m_omzet_0_74m_7_80x_pnl_jump_jr2025"
COMM = "comm_humival_jr2025_statutory_vaph_lievegem_bruto_gt_omzet"
SRC_EN = "src_humival_jr2025_cw_en"

OMZET = 740845
BRUTO = 5780489
PNL = 539105
EQUITY = 6458105
FTE = 64.6
OMZET24 = 703476
BRUTO24 = 5299165
PNL24 = 511155
EQUITY24 = 5952631
FTE24 = 64.2
RATIO = round(BRUTO / OMZET, 2)
PI = 6.25


def append_csv(path, fieldnames, rows):
    path = Path(path)
    data = path.read_bytes()
    if data and not data.endswith(b"\n"):
        path.write_bytes(data + b"\n")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in rows:
            w.writerow(r)


rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

ok = False
for r in rq_rows:
    if r.get("task_id") == "rq_2320":
        st = r.get("status")
        eid = (r.get("entity_id") or "").strip()
        if st == "done":
            raise SystemExit("rq_2320 already done")
        if st == "in_progress" and eid == ENTITY:
            ok = True
        elif st == "open" or (st == "in_progress" and not eid):
            r["status"] = "in_progress"
            r["entity_id"] = ENTITY
            r["updated_utc"] = TS
            r["priority"] = "10"
            r["notes"] = (r.get("notes") or "") + f"; tick{TICK} CLAIM Humival EVERY-10"
            ok = True
        else:
            raise SystemExit(f"rq_2320 blocked status={st} entity={eid}")
        break
if not ok:
    raise SystemExit("rq_2320 not found")

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rq_rows)

with (ROOT / "entities.csv").open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row.get("entity_id") == ENTITY:
            raise SystemExit(f"entity {ENTITY} already exists")

print(f"VERIFIED claim rq_2320 -> {ENTITY}")

append_csv(
    ROOT / "sources.csv",
    ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"],
    [
        {
            "source_id": SRC_EN,
            "title": "Humival YE2025 Companyweb EN",
            "url": "https://www.companyweb.be/en/0416237589/humival",
            "publisher": "Companyweb",
            "accessed_date": "2026-08-27",
            "source_class": "company_register_aggregator",
            "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 12-06-2026",
        },
        {
            "source_id": "src_humival_jr2025_cw_nl",
            "title": "Humival YE2025 Companyweb NL",
            "url": "https://www.companyweb.be/nl/0416237589/humival",
            "publisher": "Companyweb",
            "accessed_date": "2026-08-27",
            "source_class": "company_register_aggregator",
            "notes": f"tick{TICK}; Medium CW NL YE2025; omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl JUMP {PNL}",
        },
        {
            "source_id": "src_humival_jr2025_cw_fr",
            "title": "Humival YE2025 Companyweb FR",
            "url": "https://www.companyweb.be/fr/0416237589/humival",
            "publisher": "Companyweb",
            "accessed_date": "2026-08-27",
            "source_class": "company_register_aggregator",
            "notes": f"tick{TICK}; Medium CW FR YE2025; CA {OMZET}; marge brute {BRUTO}",
        },
        {
            "source_id": "src_humival_kbo_0416237589",
            "title": "KBO Humival 0416.237.589",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0416237589",
            "publisher": "FOD Economie KBO",
            "accessed_date": "2026-08-27",
            "source_class": "official_register",
            "notes": f"tick{TICK}; Strong KBO Actief VZW 1 VE RSZ 87.202; Nijverheidsstraat 9 9950 Lievegem",
        },
        {
            "source_id": "src_humival_site_foi_2320",
            "title": "Humival site FOI channel",
            "url": "https://www.vzw-humival.be/",
            "publisher": "Humival vzw",
            "accessed_date": "2026-08-27",
            "source_class": "foi_contact",
            "notes": f"tick{TICK}; site vzw-humival.be; postal Nijverheidsstraat 9 9950 Lievegem; FOI via site/contact",
        },
    ],
)

append_csv(
    ROOT / "budgets.csv",
    [
        "budget_id",
        "entity_id",
        "year",
        "amount_eur",
        "amount_min_eur",
        "amount_max_eur",
        "basis",
        "source_id",
        "confidence",
        "notes",
    ],
    [
        {
            "budget_id": "bud_humival_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": OMZET,
            "amount_min_eur": OMZET,
            "amount_max_eur": OMZET,
            "basis": "CW omzet YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; JUMP +5.31% vs {OMZET24}",
        },
        {
            "budget_id": "bud_humival_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": BRUTO,
            "amount_min_eur": BRUTO,
            "amount_max_eur": BRUTO,
            "basis": f"CW bruto YE2025 ~{RATIO}x",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; JUMP +9.08% vs {BRUTO24}; ~{RATIO}x",
        },
        {
            "budget_id": "bud_humival_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": PNL,
            "amount_min_eur": PNL,
            "amount_max_eur": PNL,
            "basis": "CW pnl YE2025 JUMP",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; JUMP +5.47% vs {PNL24}",
        },
        {
            "budget_id": "bud_humival_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": EQUITY,
            "amount_min_eur": EQUITY,
            "amount_max_eur": EQUITY,
            "basis": "CW equity YE2025 JUMP",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; JUMP +8.49% vs {EQUITY24}",
        },
        {
            "budget_id": "bud_humival_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": FTE,
            "amount_min_eur": FTE,
            "amount_max_eur": FTE,
            "basis": f"CW FTE {FTE}",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; FTE {FTE} vs {FTE24}; assets/debt Unknown",
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
    ROOT / "commitments.csv",
    [
        "commitment_id",
        "title",
        "entity_id",
        "beneficiary",
        "legal_basis",
        "decision_date",
        "start_year",
        "end_year",
        "total_envelope_eur",
        "cash_by_year",
        "remaining_eur",
        "status",
        "evaluation_url",
        "stated_goal",
        "cut_option",
        "source_id",
        "confidence",
        "hierarchy_path",
        "notes",
    ],
    [
        {
            "commitment_id": COMM,
            "title": f"Humival YE2025 EVERY-10 bruto 5.78m ~{RATIO}x / pnl JUMP Medium",
            "entity_id": ENTITY,
            "beneficiary": "VAPH users Lievegem adults intellectual disability",
            "legal_basis": "VZW Humival 0416.237.589 Actief 1 VE RSZ 87.202",
            "decision_date": "2026-06-12",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": BRUTO,
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": 0,
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0416237589/humival",
            "stated_goal": "VAPH residential + day support adults with intellectual disability",
            "cut_option": "NBB PDF assets/debt; VAPH/PVF matrix behind bruto~7.8x",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Lievegem>Humival>JR2025",
            "notes": f"tick{TICK} EVERY-10; after Kindervriend@2319; AGB/FARO YE2024",
        }
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        "item_id",
        "name",
        "level",
        "type",
        "hierarchy_path",
        "annual_cost_eur",
        "total_cost_eur",
        "tco_notes",
        "confidence",
        "source_id",
        "beneficiaries",
        "stated_goal",
        "measured_outcome",
        "absurdity_score",
        "cost_score",
        "difficulty",
        "priority_index",
        "cut_proposal",
        "status",
        "struck_reason",
        "notes",
    ],
    [
        {
            "item_id": LB,
            "name": f"Humival bruto 5.78m / omzet 0.74m ~{RATIO}x / pnl JUMP (YE2025 VAPH Lievegem)",
            "level": "L5",
            "type": "vaph_mpi_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Lievegem>Humival>JR2025",
            "annual_cost_eur": BRUTO,
            "total_cost_eur": BRUTO,
            "tco_notes": f"omzet JUMP {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x) / pnl JUMP {PNL} / equity JUMP {EQUITY} / FTE {FTE}",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "VAPH Lievegem",
            "stated_goal": "VAPH residential disability care",
            "measured_outcome": f"bruto~{RATIO}x; pnl JUMP +5.5%; FTE {FTE}",
            "absurdity_score": 6.8,
            "cost_score": 5.2,
            "difficulty": 2.5,
            "priority_index": PI,
            "cut_proposal": "FOI NBB PDF; reconcile bruto÷omzet ~7.8x + VAPH subsidy opacity",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK} EVERY-10; FOI {GAP}",
        }
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        "entity_id",
        "name_nl",
        "name_fr",
        "name_en",
        "level",
        "parent_id",
        "community_language",
        "website",
        "foi_email",
        "foi_postal",
        "notes",
    ],
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Humival VZW (Lievegem / VAPH)",
            "name_fr": "Humival ASBL (Lievegem / VAPH)",
            "name_en": "Humival VZW (Lievegem / VAPH residential)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.vzw-humival.be/",
            "foi_email": "",
            "foi_postal": "Nijverheidsstraat 9, 9950 Lievegem",
            "notes": f"tick{TICK} EVERY-10 YE2025 Medium CW+Strong KBO 0416.237.589 Actief 1 VE RSZ 87.202; omzet JUMP {OMZET}; bruto JUMP {BRUTO} (~{RATIO}x); pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; FOI {GAP}; after Kindervriend@2319",
        }
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        "gap_id",
        "hierarchy_path",
        "entity_id",
        "what_is_missing",
        "why_it_matters",
        "priority",
        "recipient_body",
        "recipient_email",
        "recipient_postal",
        "draft_letter_path",
        "status",
        "date_ready",
        "date_sent",
        "date_due",
        "date_answered",
        "response_summary",
        "linked_commitment_id",
        "linked_leaderboard_id",
        "created_utc",
        "updated_utc",
        "notes",
    ],
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Lievegem>Humival>NBB_PDF",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF YE2025 assets/debt; bruto {BRUTO} (~{RATIO}x omzet {OMZET}); VAPH matrix; FOI email channel",
            "why_it_matters": f"VAPH Lievegem bruto÷omzet ~{RATIO}x opacity; EVERY-10@2320 primary",
            "priority": 8,
            "recipient_body": "Humival VZW",
            "recipient_email": "",
            "recipient_postal": "Nijverheidsstraat 9, 9950 Lievegem",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-27",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": COMM,
            "linked_leaderboard_id": LB,
            "created_utc": TS,
            "updated_utc": TS,
            "notes": f"tick{TICK}; ready NOT sent; FOI via postal/site contact",
        }
    ],
)

with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

for r in rq_rows:
    if r.get("task_id") == "rq_2320":
        eid = (r.get("entity_id") or "").strip()
        if r.get("status") == "done":
            raise SystemExit("stolen done")
        if eid not in ("", ENTITY):
            raise SystemExit(f"stolen {eid}")
        r["title"] = (
            f"EVERY-10 + leftover dual — Humival YE2025 Medium (bruto 5.78m / omzet 0.74m ~{RATIO}x / pnl JUMP / FTE {FTE})"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["priority"] = "10"
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = TS
        r["notes"] = (
            f"tick{TICK} EVERY-10; Humival 0416.237.589 YE2025 Medium; omzet JUMP {OMZET}; bruto JUMP {BRUTO} (~{RATIO}x); "
            f"pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; FOI {GAP} ready NOT sent; progress+waste refreshed; next EVERY-10 2330"
        )
        break

if not any(x.get("task_id") == "rq_2321" for x in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_2321",
            "title": "leftover dual after Humival EVERY-10 — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"After Humival YE2025 Medium (bruto 5.78m ~{RATIO}x). Prefer AGB/FARO YE2025 else unused "
                "Heder/Gandae/Aralea/Manupal/De Ploeg/Vlotter/Het Eepos if YE2025. "
                "Do NOT redo Humival/Kindervriend/Homevil/Schoonderhage/Olo-Rotonde/Havenzate stack."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick2320 Humival EVERY-10; next EVERY-10 2330",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rq_rows)

with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_2320",
            "ticks_completed": "2320",
            "paused": "no",
            "notes": (
                f"tick{TICK} EVERY-10 leftover dual Humival 0416.237.589 Medium "
                f"(omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 1 VE Lievegem VAPH); "
                f"after Kindervriend@2319; AGB/FARO YE2024; next rq_2321; next EVERY-10 2330"
            ),
        }
    )

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Humival Lievegem (EVERY-10)

**gap_id:** `{GAP}` · ready NOT sent · tick {TICK}
**KBO:** 0416.237.589 · postal Nijverheidsstraat 9, 9950 Lievegem · site https://www.vzw-humival.be/
CW YE2025: omzet {OMZET}; bruto {BRUTO} (~{RATIO}x); pnl {PNL}; equity {EQUITY}; FTE {FTE}; filed 12.06.2026.
Ask NBB PDF assets/debt/cash; VAPH/PVF matrix; confirm FOI email. Ref {GAP}
""",
    encoding="utf-8",
)

raw = ROOT / "raw" / f"tick{TICK}"
raw.mkdir(parents=True, exist_ok=True)
(raw / "summary.json").write_text(
    json.dumps(
        {
            "tick": TICK,
            "every_10": True,
            "entity_id": ENTITY,
            "omzet": OMZET,
            "bruto": BRUTO,
            "pnl": PNL,
            "equity": EQUITY,
            "fte": FTE,
            "ratio": RATIO,
            "gap_id": GAP,
            "confidence": "medium",
        },
        indent=2,
    ),
    encoding="utf-8",
)

print(f"CSV DONE Humival bruto {BRUTO} ~{RATIO}x PI {PI}")
