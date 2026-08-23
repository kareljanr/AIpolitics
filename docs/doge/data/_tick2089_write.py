# tick 2089 — De Lovie YE2025 Medium CW leftover dual
import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC = "2026-08-25T03:20:00Z"
DATE = "2026-08-25"
ENTITY = "vzw_de_lovie_poperinge"
GAP = "gap_de_lovie_nbb_pdf_assets_debt_omzet_bruto_gap_pnl_drop_matrix_l5"
COMM = "comm_de_lovie_jr2025_statutory_disability_care"
LB = "lb_de_lovie_bruto_jump_67_01m_pnl_drop_fte_jump_jr2025"

OMZET = 8507490
PNL = 5372235
EQUITY = 58139102
BRUTO = 67006189
FTE = 732.6


def append_csv(path: Path, rows: list[dict], id_key: str):
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        existing = list(r)
    have = {row.get(id_key) for row in existing}
    new_rows = [row for row in rows if row.get(id_key) not in have]
    if not new_rows:
        print(f"skip {path.name}: already present")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(existing)
        for row in new_rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})
    print(f"append {path.name}: +{len(new_rows)}")


# --- sources ---
sources = [
    {
        "source_id": "src_de_lovie_jr2025_cw_nl",
        "title": "De Lovie VZW Companyweb NL YE2025",
        "url": "https://www.companyweb.be/nl/0410853396/de-lovie",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2089; YE2025 omzet/pnl/equity/bruto/FTE; neerlegging 11.06.2026; Medium",
    },
    {
        "source_id": "src_de_lovie_jr2025_cw_en",
        "title": "De Lovie ASBL Companyweb EN YE2025",
        "url": "https://www.companyweb.be/en/0410853396/de-lovie",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2089; EN mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_de_lovie_jr2025_cw_fr",
        "title": "De Lovie ASBL Companyweb FR YE2025",
        "url": "https://www.companyweb.be/fr/0410853396/de-lovie",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2089; FR mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_de_lovie_kbo_2089",
        "title": "KBO De Lovie 0410.853.396",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=410853396",
        "publisher": "KBO/BCE",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2089; Actief VZW aanbestedende; 33 VE; NACE 87.202; Strong identity",
    },
    {
        "source_id": "src_de_lovie_site_2089",
        "title": "De Lovie VZW website",
        "url": "https://delovie.be/",
        "publisher": "De Lovie",
        "accessed_date": DATE,
        "source_class": "entity_site",
        "notes": "tick2089; Westhoek multi-site disability care; HQ Krombeekseweg 82 Poperinge; info@delovie.be",
    },
]
append_csv(DATA / "sources.csv", sources, "source_id")

# --- budgets ---
budgets = [
    {
        "budget_id": "bud_de_lovie_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW turnover / Omzet YE2025",
        "source_id": "src_de_lovie_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2089; omzet JUMP 8507490 (+5.06%) vs YE2024 8097494; narrow vs bruto",
    },
    {
        "budget_id": "bud_de_lovie_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW Profit/Loss YE2025",
        "source_id": "src_de_lovie_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2089; pnl PROFIT DROP 5372235 (-23.91%) vs YE2024 7060159",
    },
    {
        "budget_id": "bud_de_lovie_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW Equity / Eigen vermogen YE2025",
        "source_id": "src_de_lovie_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2089; equity JUMP 58139102 (+10.76%) vs YE2024 52489430",
    },
    {
        "budget_id": "bud_de_lovie_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW Gross margin / Brutomarge YE2025 (primary envelope)",
        "source_id": "src_de_lovie_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2089; bruto JUMP 67006189 (+5.66%) vs YE2024 63414583; better disability-VZW envelope than narrow omzet",
    },
    {
        "budget_id": "bud_de_lovie_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE / Employees",
        "source_id": "src_de_lovie_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2089; FTE JUMP 732.6 (+3.42%) vs YE2024 708.4",
    },
]
append_csv(DATA / "budgets.csv", budgets, "budget_id")

# --- entity ---
append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "De Lovie VZW (Poperinge)",
            "name_fr": "De Lovie ASBL (Poperinge)",
            "name_en": "De Lovie VZW (Poperinge)",
            "level": "other",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://delovie.be/",
            "foi_email": "info@delovie.be",
            "foi_postal": "Krombeekseweg 82, 8970 Poperinge",
            "notes": (
                "tick2089 YE2025 Medium CW NL+EN+FR + Strong KBO 0410.853.396 Actief VZW "
                "aanbestedende 33 VE; omzet JUMP 8.51m pnl DROP 5.37m equity JUMP 58.14m "
                "bruto JUMP 67.01m FTE JUMP 732.6; NACE 87.202 disability residential"
            ),
        }
    ],
    "entity_id",
)

# --- commitment ---
append_csv(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": "De Lovie Poperinge YE2025 leftover dual (bruto JUMP 67.01m / pnl DROP)",
            "entity_id": ENTITY,
            "beneficiary": "Westhoek adults with mental disability (De Lovie multi-site, 33 VE)",
            "legal_basis": "VZW disability care / publiek gesubsidieerde zorg / aanbestedende overheid (KBO 0410.853.396)",
            "decision_date": "2026-06-11",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(BRUTO),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0410853396/de-lovie",
            "stated_goal": "Residential and day care for adults with mental disability (Westhoek)",
            "cut_option": "Publish NBB PDF assets/debt + VAPH subsidy vs omzet split FOI; explain omzet<<bruto and pnl DROP -23.91pct",
            "source_id": "src_de_lovie_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>West-Vlaanderen>Poperinge>De_Lovie>JR2025_statutory_L5",
            "notes": (
                "tick2089; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; not TE-additive of 348bn; bruto primary vs narrow omzet"
            ),
        }
    ],
    "commitment_id",
)

# --- leaderboard ---
append_csv(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "De Lovie bruto JUMP 67.01m / pnl DROP + omzet<<bruto gap (YE2025)",
            "level": "L5",
            "type": "disability_vzw_statutory",
            "hierarchy_path": "Vlaanderen>West-Vlaanderen>Poperinge>De_Lovie>JR2025",
            "annual_cost_eur": str(BRUTO),
            "total_cost_eur": str(BRUTO),
            "tco_notes": (
                "CW bruto primary envelope (disability VZW); omzet 8.51m narrow; "
                "assets/debt Unknown pending NBB PDF FOI"
            ),
            "confidence": "medium",
            "source_id": "src_de_lovie_jr2025_cw_en",
            "beneficiaries": "De Lovie multi-site disability clients Westhoek (33 VE)",
            "stated_goal": "Residential care adults with mental disability",
            "measured_outcome": (
                "omzet JUMP +5.06%; pnl DROP -23.91%; equity JUMP +10.76%; "
                "bruto JUMP +5.66%; FTE JUMP 732.6 (+3.42%)"
            ),
            "absurdity_score": "5.0",
            "cost_score": "6.5",
            "difficulty": "4.0",
            "priority_index": "6.2",
            "cut_proposal": (
                "Publish NBB PDF assets/debt FOI; map VAPH/public subsidy vs narrow omzet "
                "across 33 VE; explain pnl -23.91pct with equity +10.76pct"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                "tick2089; Medium CW; FOI "
                f"{GAP}; stall FARO/AIESH/REW YE2024; aanbestedende 33 VE; "
                "do not redo Ocura/Lindelo/Medemens/Halle"
            ),
        }
    ],
    "item_id",
)

# --- foi_queue ---
append_csv(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>West-Vlaanderen>Poperinge>De_Lovie>NBB_PDF_assets_debt_omzet_bruto",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public VAPH subsidy "
                "vs omzet split across 33 VE; explanation of omzet 8.51m vs bruto 67.01m and "
                "pnl DROP -23.91% with equity JUMP +10.76%"
            ),
            "why_it_matters": (
                "Medium CW shows 67.01m bruto aanbestedende multi-site disability VZW with "
                "large omzet<<bruto gap and pnl DROP without balanstotaal/assets/debt; "
                "material L5 residual for FOI"
            ),
            "priority": "8",
            "recipient_body": "De Lovie VZW",
            "recipient_email": "info@delovie.be",
            "recipient_postal": "Krombeekseweg 82, 8970 Poperinge",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": DATE,
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": COMM,
            "linked_leaderboard_id": LB,
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "tick2089; human-send only; Medium CW; next every-10 2090",
        }
    ],
    "gap_id",
)

# --- research_queue: close 2089, open 2090 ---
rq_path = DATA / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

found = False
for row in rows:
    if row["task_id"] == "rq_2089":
        found = True
        row["status"] = "done"
        row["title"] = "leftover dual — De Lovie Poperinge YE2025 Medium"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["instructions"] = (
            "Completed leftover De Lovie Poperinge YE2025 Medium CW; KBO 0410.853.396; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} "
            f"FTE JUMP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024"
        )
        row["notes"] = (
            "tick2089 De Lovie YE2025 Medium; preferred FARO/AIESH/REW still YE2024; "
            "next every-10 2090"
        )
        row["blocked_gap_id"] = GAP

if not any(r.get("task_id") == "rq_2090" for r in rows):
    rows.append(
        {
            "task_id": "rq_2090",
            "title": "EVERY-10 + leftover dual hole-fill after De Lovie — prefer AGB/FARO-YE2025/AIESH-REW/unused WZC",
            "sprint": "hole_fill",
            "priority": "9",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2089 after De Lovie YE2025 Medium. MUST refresh progress_every_10_ticks.md "
                "+ doge_waste_top10_current.md then hole-fill one unit. Prefer leftover AGB/APB "
                "if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. Do NOT redo De Lovie, "
                "Ocura Beringen, WZC Lindelo Lille, De Medemens, WZC Sint-Augustinus Halle, "
                "Ben Woonzorgnetwerk, Home Stuyvenberg, WZC De Wijshage, Mater Dei, Den Akker."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2089 De Lovie; EVERY-10 mandatory at 2090",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
assert found, "rq_2089 not found"

# --- loop_state ---
with (DATA / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ]
    )
    w.writerow(
        [
            "main",
            "continuous",
            "hole_fill",
            UTC,
            "rq_2089",
            "2089",
            "no",
            (
                "tick2089 leftover De Lovie Poperinge 0410.853.396 Medium CW "
                "(omzet JUMP 8.51m pnl DROP 5.37m equity JUMP 58.14m bruto JUMP 67.01m "
                "FTE JUMP 732.6; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2090 EVERY-10; continuous hole_fill"
            ),
        ]
    )

# --- loop_log append ---
if "Tick 2089 -" in LOG.read_text(encoding="utf-8"):
    print("skip loop_log: Tick 2089 already present")
    log_block = None
else:
    log_block = f"""

## Tick 2089 - {UTC} - rq_2089 De Lovie (bruto JUMP 67.01m / pnl DROP 5.37m / Medium)

- Unit: **rq_2089** leftover dual after **rq_2088 Ocura**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred leftover **De Lovie** YE2025 (KBO **0410.853.396**; Krombeekseweg 82 Poperinge; West-Vlaanderen **aanbestedende-overheid VZW** disability residential / **33 VE**; NACE 87.202). Do not redo Ocura/Lindelo/Medemens/Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +5.06%; pnl **PROFIT EUR{PNL}** DROP vs YE2024 PROFIT EUR7060159; equity **EUR{EQUITY}** JUMP +10.76%; bruto **EUR{BRUTO}** JUMP +5.66%; FTE **{FTE}** JUMP +3.42% vs YE2024 708.4; neerlegging **11.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende 33 VE; email info@delovie.be. Bruto used as primary envelope (disability VZW omzet<<bruto).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.2); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2089=done + rq_2090 open; loop_state ticks=2089; raw under docs/doge/data/raw/tick2089/.
- FOI: **ready not sent** (human-gated; info@delovie.be).
- NOT every-10 (**next every-10 is 2090** — MUST refresh progress + waste top10 then hole-fill). Next: rq_2090 (EVERY-10 + AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
if log_block:
    with LOG.open("a", encoding="utf-8") as f:
        f.write(log_block)

print("tick2089 write OK; found=", found)
