# -*- coding: utf-8 -*-
"""Apply tick2168 Zorgcentrum Sint Lodewijk Schilde YE2025 Medium CW (race-recover after Anima hold)."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
NOW = "2026-08-26T02:00:00Z"
TICK = "2168"
RQ = "rq_2168"
NEXT_RQ = "rq_2169"

ENTITY = "vzw_zorgcentrum_sint_lodewijk_schilde"
OMZET = 8433732
BRUTO = 8553797
PNL = 169197
EQUITY = 12565130
FTE = 120.7
OMZET_2024 = 7979173
PNL_2024 = 483844
EQUITY_2024 = 12403999
BRUTO_2024 = 8429239

omzet_pct = (OMZET - OMZET_2024) / OMZET_2024 * 100
pnl_pct = (PNL - PNL_2024) / PNL_2024 * 100
equity_pct = (EQUITY - EQUITY_2024) / EQUITY_2024 * 100
bruto_pct = (BRUTO - BRUTO_2024) / BRUTO_2024 * 100

GAP = "gap_sint_lodewijk_schilde_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
COMM = "comm_sint_lodewijk_schilde_jr2025_statutory_wzc_pnl_drop_omzet_8_43m"
LB = "lb_sint_lodewijk_schilde_omzet_8_43m_pnl_drop_jr2025"

csv.field_size_limit(10**7)


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames


def write_csv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


sources, sh = read_csv(DATA / "sources.csv")
new_sources = [
    {
        "source_id": "src_sint_lodewijk_schilde_jr2025_cw_nl",
        "title": "Companyweb NL Zorgcentrum Sint Lodewijk Schilde YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0410127084/zorgcentrum-sint-lodewijk",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} "
            f"bruto JUMP {BRUTO} FTE {FTE}; neerlegging 03.08.2026; assets/debt Unknown; "
            f"raw docs/doge/data/raw/tick2168/"
        ),
    },
    {
        "source_id": "src_sint_lodewijk_schilde_jr2025_cw_en",
        "title": "Companyweb EN Zorgcentrum Sint Lodewijk Schilde YE2025 statutory",
        "url": "https://www.companyweb.be/en/0410127084",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 03-08-2026; FTE {FTE}",
    },
    {
        "source_id": "src_sint_lodewijk_schilde_jr2025_cw_fr",
        "title": "Companyweb FR Zorgcentrum Sint Lodewijk Schilde YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0410127084",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium",
    },
    {
        "source_id": "src_sint_lodewijk_schilde_kbo_2168",
        "title": "KBO Zorgcentrum Sint Lodewijk 0410.127.084 Actief VZW Schilde",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0410127084",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-26",
        "source_class": "official_register",
        "notes": (
            "tick2168; Actief VZW; zetel Kerkstraat 61 2970 Schilde; 1 VE; NACE 87.101 RVT; "
            "start 14.09.1928; KBO email/tel/web empty"
        ),
    },
    {
        "source_id": "src_sint_lodewijk_schilde_foi_contact_2168",
        "title": "Sint Lodewijk Schilde FOI contact info@rvtsintlodewijk.be",
        "url": "https://www.schilde.be/rvt-sint-lodewijk",
        "publisher": "Gemeente Schilde / RVT Sint-Lodewijk",
        "accessed_date": "2026-08-26",
        "source_class": "foi_contact",
        "notes": (
            "tick2168; info@rvtsintlodewijk.be; tel 03 658 85 22; site rvtsintlodewijk.be; "
            "Kerkstraat 61 Schilde ('s-Gravenwezel)"
        ),
    },
]
existing_src = {r["source_id"] for r in sources}
for s in new_sources:
    if s["source_id"] not in existing_src:
        sources.append(s)
write_csv(DATA / "sources.csv", sources, sh)

entities, eh = read_csv(DATA / "entities.csv")
if not any(r["entity_id"] == ENTITY for r in entities):
    entities.append(
        {
            "entity_id": ENTITY,
            "name_nl": "Zorgcentrum Sint Lodewijk VZW (Schilde / 's-Gravenwezel)",
            "name_fr": "Centre de soins Sint Lodewijk ASBL (Schilde)",
            "name_en": "Sint Lodewijk care centre non-profit (Schilde)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://rvtsintlodewijk.be/",
            "foi_email": "info@rvtsintlodewijk.be",
            "foi_postal": "Kerkstraat 61, 2970 Schilde",
            "notes": (
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0410.127.084 Actief VZW 1 VE "
                f"NACE 87.101 RVT; omzet JUMP {OMZET/1e6:.2f}m ({omzet_pct:.2f}%) pnl DROP {PNL} "
                f"({pnl_pct:.2f}%) equity JUMP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m FTE {FTE}; "
                f"assets/debt Unknown; neerlegging 03.08.2026; FOI {GAP}; preferred AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; do not redo Anima hold/Avondvrede/Anima Vlaanderen/t Hofke/"
                f"Zorg-Saam/Sint-Bernardus/Ruggeveld/Salvator/Boterlaarhof/WZND/Foyer De Lork"
            ),
        }
    )
write_csv(DATA / "entities.csv", entities, eh)

budgets, bh = read_csv(DATA / "budgets.csv")
new_buds = [
    ("bud_sint_lodewijk_schilde_omzet_jr2025_statutory", OMZET, "CW statutory omzet / Turnover YE2025"),
    ("bud_sint_lodewijk_schilde_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge / Gross margin YE2025"),
    ("bud_sint_lodewijk_schilde_pnl_jr2025_statutory", PNL, "CW statutory winst / Profit after tax YE2025"),
    ("bud_sint_lodewijk_schilde_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen / Equity YE2025"),
    ("bud_sint_lodewijk_schilde_fte_jr2025_statutory", FTE, f"CW social-balance FTE / Employees {FTE}"),
]
existing_b = {r["budget_id"] for r in budgets}
for bid, amt, basis in new_buds:
    if bid in existing_b:
        continue
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(amt),
            "amount_min_eur": str(amt),
            "amount_max_eur": str(amt),
            "basis": basis,
            "source_id": "src_sint_lodewijk_schilde_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; assets/debt Unknown pending NBB PDF",
        }
    )
write_csv(DATA / "budgets.csv", budgets, bh)

comms, ch = read_csv(DATA / "commitments.csv")
if not any(r["commitment_id"] == COMM for r in comms):
    cash = (
        f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_omzet":{OMZET_2024},"2024_pnl":{PNL_2024},'
        f'"2024_equity":{EQUITY_2024},"2024_bruto":{BRUTO_2024}}}'
    )
    comms.append(
        {
            "commitment_id": COMM,
            "title": (
                "Zorgcentrum Sint Lodewijk Schilde YE2025 leftover dual "
                "(omzet JUMP 8.43m / pnl DROP -65%)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "WZC/RVT residents Schilde ('s-Gravenwezel) Sint Lodewijk",
            "legal_basis": "VZW RVT (KBO 0410.127.084; Actief; 1 VE; NACE 87.101)",
            "decision_date": "2026-08-03",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": cash,
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0410127084",
            "stated_goal": "Residential elderly care Schilde Sint Lodewijk",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; explain pnl DROP -65% despite omzet JUMP; "
                "RIZIV/dagprijs + Schilde toelage matrix"
            ),
            "source_id": "src_sint_lodewijk_schilde_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Schilde>SintLodewijk>JR2025_statutory_L5",
            "notes": (
                f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; preferred "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT "
                f"Anima hold/Avondvrede/Zorg-Saam; Sint-Vincentius Aaigem 0644.843.825 FREE deferred"
            ),
        }
    )
write_csv(DATA / "commitments.csv", comms, ch)

lbs, lh = read_csv(DATA / "leaderboard.csv")
if not any(r["item_id"] == LB for r in lbs):
    lbs.append(
        {
            "item_id": LB,
            "name": "Sint Lodewijk Schilde omzet JUMP 8.43m / pnl DROP -65% (YE2025)",
            "level": "L5",
            "type": "wzc_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>Schilde>SintLodewijk>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                f"CW omzet envelope 8.43m / {FTE} FTE; pnl DROP {pnl_pct:.1f}% despite omzet JUMP; "
                f"equity JUMP {equity_pct:.1f}%; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": "src_sint_lodewijk_schilde_jr2025_cw_en",
            "beneficiaries": "WZC clients Schilde Sint Lodewijk",
            "stated_goal": "Residential elderly care Schilde",
            "measured_outcome": (
                f"omzet JUMP {omzet_pct:.2f}%; bruto JUMP {bruto_pct:.2f}%; "
                f"pnl DROP {pnl_pct:.2f}%; equity JUMP {equity_pct:.2f}%; FTE {FTE}"
            ),
            "absurdity_score": "5.8",
            "cost_score": "5.4",
            "difficulty": "3.5",
            "priority_index": "5.5",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose pnl DROP path despite rising omzet; "
                "Schilde toelage/RIZIV split"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                f"Sint-Vincentius Aaigem FREE deferred"
            ),
        }
    )
write_csv(DATA / "leaderboard.csv", lbs, lh)

foi, fh = read_csv(DATA / "foi_queue.csv")
if not any(r["gap_id"] == GAP for r in foi):
    foi.append(
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Schilde>SintLodewijk>NBB_PDF_assets_debt_pnl_drop",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "RIZIV/Vlaams vs dagprijs split; explanation of pnl DROP EUR169k (−65% vs YE2024 "
                "EUR484k) despite omzet JUMP +5.7%; Schilde toelage matrix"
            ),
            "why_it_matters": (
                "Medium CW shows EUR8.43m Schilde RVT with sharp pnl DROP while omzet rises — "
                "no balanstotaal/assets/debt; municipal-subsidy opacity material for FOI"
            ),
            "priority": "8",
            "recipient_body": "Zorgcentrum Sint Lodewijk VZW",
            "recipient_email": "info@rvtsintlodewijk.be",
            "recipient_postal": "Kerkstraat 61, 2970 Schilde",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-26",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": COMM,
            "linked_leaderboard_id": LB,
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; next every-10 2170",
        }
    )
write_csv(DATA / "foi_queue.csv", foi, fh)

rq, rh = read_csv(DATA / "research_queue.csv")
for r in rq:
    if r["task_id"] == RQ:
        r["title"] = (
            "leftover dual — Zorgcentrum Sint Lodewijk Schilde YE2025 Medium "
            "(omzet JUMP 8.43m / pnl DROP -65%)"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "Completed leftover Sint Lodewijk Schilde after Anima hold; preferred AGB Bornem JR2024 / "
            "FARO/AIESH/REW still YE2024; skipped Oudenburg NACE 55; Medium CW YE2025 + Strong KBO; "
            "FOI ready not sent; Sint-Vincentius Aaigem deferred"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK} Sint Lodewijk Schilde Medium omzet JUMP {OMZET/1e6:.2f}m ({omzet_pct:.2f}%) "
            f"bruto JUMP pnl DROP {PNL} ({pnl_pct:.2f}%) equity JUMP {EQUITY/1e6:.2f}m FTE {FTE}; "
            f"KBO Actief VZW 1 VE NACE 87.101; FOI info@rvtsintlodewijk.be; next every-10 2170"
        )
if not any(r["task_id"] == NEXT_RQ for r in rq):
    rq.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual hole-fill after Sint Lodewijk Schilde — prefer "
                "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2169 after Sint Lodewijk Schilde YE2025 Medium (omzet JUMP 8.43m / pnl DROP -65%). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW "
                "if YE2025, else unused IGS/DSO/WZC/MRS (optional: Sint-Vincentius Aaigem 0644.843.825 "
                "YE2025 FREE bruto 0.74m / Melis Home 0787.300.696). Do NOT redo Sint Lodewijk Schilde/"
                "Anima hold/Avondvrede/Anima Vlaanderen/t Hofke/Zorg-Saam/Sint-Bernardus De Panne/"
                "Ruggeveld/Salvator/Boterlaarhof/WZND/Foyer De Lork/Maria Rustoord/Samen Ouder/"
                "Zusters Sint-Vincentius Deinze/Vrijzicht/Wijtshage/Huize Vincent/Christine/"
                "Witte Meren/Molenheide/Vander Stokken/Sint-Barbara Herselt."
            ),
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": (
                "spawned after tick2168 Sint Lodewijk Schilde; FARO/AIESH/REW still YE2024; "
                "next every-10 2170"
            ),
        }
    )
write_csv(DATA / "research_queue.csv", rq, rh)

state_rows, sth = read_csv(DATA / "loop_state.csv")
for r in state_rows:
    if r["state_id"] == "main":
        r["mode"] = "continuous"
        r["current_sprint"] = "hole_fill"
        r["last_tick_utc"] = NOW
        r["last_unit_id"] = RQ
        r["ticks_completed"] = TICK
        r["paused"] = "no"
        r["notes"] = (
            f"tick{TICK} leftover Sint Lodewijk Schilde 0410.127.084 Medium (omzet JUMP 8.43m; "
            f"pnl DROP 169k -65%; equity JUMP 12.57m; FTE 120.7; NACE 87.101); AGB Bornem JR2024; "
            f"FARO/AIESH/REW YE2024; Aaigem/Melis FREE deferred; next {NEXT_RQ}; next every-10 2170; "
            f"continuous hole_fill"
        )
write_csv(DATA / "loop_state.csv", state_rows, sth)
print("DONE tick", TICK, "omzet", OMZET, "pnl", PNL, f"pnl_pct={pnl_pct:.2f}")
