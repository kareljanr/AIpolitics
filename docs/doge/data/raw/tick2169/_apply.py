# -*- coding: utf-8 -*-
"""Apply tick2169 Sint-Vincentius Aaigem YE2025 Medium CW (leftover dual after Sint Lodewijk/Lork)."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
NOW = "2026-08-26T02:20:00Z"
TICK = "2169"
RQ = "rq_2169"
NEXT_RQ = "rq_2170"

ENTITY = "vzw_sint_vincentius_aaigem"
BRUTO = 743497
PNL = 97823
EQUITY = 4250630
FTE = 0
BRUTO_2024 = 713540
PNL_2024 = -3297
EQUITY_2024 = 4152807

bruto_pct = (BRUTO - BRUTO_2024) / BRUTO_2024 * 100
equity_pct = (EQUITY - EQUITY_2024) / EQUITY_2024 * 100
# pnl LOSS FLIP from negative — no clean %

GAP = "gap_sint_vincentius_aaigem_nbb_pdf_assets_debt_omzet_empty_pnl_flip_related_wzc_matrix_l5"
COMM = "comm_sint_vincentius_aaigem_jr2025_statutory_wzc_bruto_743k_pnl_flip"
LB = "lb_sint_vincentius_aaigem_bruto_743k_omzet_empty_pnl_flip_jr2025"

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
        "source_id": "src_sint_vincentius_aaigem_jr2025_cw_nl",
        "title": "Companyweb NL Sint-Vincentius Aaigem YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0644843825/sint-vincentius-aaigem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet empty bruto JUMP {BRUTO} pnl LOSS FLIP {PNL} "
            f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 24.07.2026; assets/debt Unknown; "
            f"CW hoofdactiviteit 'Andere drinkgelegenheden' (likely mislabel); "
            f"raw docs/doge/data/raw/tick2169/"
        ),
    },
    {
        "source_id": "src_sint_vincentius_aaigem_jr2025_cw_en",
        "title": "Companyweb EN Sint-Vincentius Aaigem YE2025 statutory",
        "url": "https://www.companyweb.be/en/0644843825",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 24-07-2026; FTE {FTE}; activity Other pubs",
    },
    {
        "source_id": "src_sint_vincentius_aaigem_jr2025_cw_fr",
        "title": "Companyweb FR Sint-Vincentius Aaigem YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0644843825",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium",
    },
    {
        "source_id": "src_sint_vincentius_aaigem_kbo_2169",
        "title": "KBO Sint-Vincentius Aaigem 0644.843.825 Actief VZW Erpe-Mere",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0644843825",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-26",
        "source_class": "official_register",
        "notes": (
            "tick2169; Actief VZW; zetel Aaigemdorp 68 9420 Erpe-Mere; 2 VE; "
            "start 23.12.2015; KBO activities empty; HealthPro link; email/tel/web empty in KBO"
        ),
    },
    {
        "source_id": "src_sint_vincentius_aaigem_foi_contact_2169",
        "title": "Sint-Vincentius Aaigem FOI contact info@sint-vincentius-vzw.be",
        "url": "https://www.sint-vincentius-vzw.be/zorgvormen/woonzorgcentrum/",
        "publisher": "Sint-Vincentius VZW",
        "accessed_date": "2026-08-26",
        "source_class": "foi_contact",
        "notes": (
            "tick2169; info@sint-vincentius-vzw.be; tel 053 60 12 12; "
            "Aaigemdorp 68 Aaigem/Erpe-Mere; dual CoBRHA WZC KBO 0422.620.585"
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
            "name_nl": "Sint-Vincentius Aaigem VZW (Erpe-Mere / WZC path)",
            "name_fr": "Sint-Vincentius Aaigem ASBL (Erpe-Mere / MRS)",
            "name_en": "Sint-Vincentius Aaigem non-profit (Erpe-Mere care path)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.sint-vincentius-vzw.be/",
            "foi_email": "info@sint-vincentius-vzw.be",
            "foi_postal": "Aaigemdorp 68, 9420 Erpe-Mere",
            "notes": (
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0644.843.825 Actief VZW 2 VE; "
                f"omzet empty bruto JUMP {BRUTO/1e3:.1f}k ({bruto_pct:.2f}%) pnl LOSS FLIP {PNL} "
                f"(from YE2024 {PNL_2024}) equity JUMP {EQUITY/1e6:.2f}m FTE {FTE}; "
                f"assets/debt Unknown; neerlegging 24.07.2026; CW activity 'Andere drinkgelegenheden' "
                f"likely mislabel; dual operating WZC CoBRHA KBO 0422.620.585 same address; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Melis Home deferred; "
                f"do not redo Sint Lodewijk/Lork Hoeselt/Anima*/Avondvrede/t Hofke/Zorg-Saam/"
                f"Sint-Bernardus/Ruggeveld/Salvator/Boterlaarhof/WZND/Foyer De Lork Geel"
            ),
        }
    )
write_csv(DATA / "entities.csv", entities, eh)

budgets, bh = read_csv(DATA / "budgets.csv")
new_buds = [
    ("bud_sint_vincentius_aaigem_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge / Gross margin YE2025"),
    ("bud_sint_vincentius_aaigem_pnl_jr2025_statutory", PNL, "CW statutory winst / Profit after tax YE2025 (LOSS FLIP)"),
    ("bud_sint_vincentius_aaigem_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen / Equity YE2025"),
    ("bud_sint_vincentius_aaigem_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees 0"),
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
            "source_id": "src_sint_vincentius_aaigem_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet unpublished; assets/debt Unknown pending NBB PDF",
        }
    )
write_csv(DATA / "budgets.csv", budgets, bh)

comms, ch = read_csv(DATA / "commitments.csv")
if not any(r["commitment_id"] == COMM for r in comms):
    cash = (
        f'{{"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_omzet":null,"2024_bruto":{BRUTO_2024},"2024_pnl":{PNL_2024},'
        f'"2024_equity":{EQUITY_2024},"related_wzc_kbo":"0422620585"}}'
    )
    comms.append(
        {
            "commitment_id": COMM,
            "title": (
                "Sint-Vincentius Aaigem YE2025 leftover dual "
                "(bruto JUMP 743k / omzet empty / pnl LOSS FLIP)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "WZC/RVT path Aaigem Erpe-Mere (dual with operating WZC 0422.620.585)",
            "legal_basis": "VZW (KBO 0644.843.825; Actief; 2 VE; CW activity mislabel pubs)",
            "decision_date": "2026-07-24",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(BRUTO),
            "cash_by_year": cash,
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0644843825",
            "stated_goal": "Care-path VZW at Sint-Vincentius Aaigem WZC address",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose omzet empty + related-party vs "
                "operating WZC 0422.620.585; RIZIV/dagprijs / Erpe-Mere toelage matrix"
            ),
            "source_id": "src_sint_vincentius_aaigem_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>ErpeMere>SintVincentiusAaigem>JR2025_statutory_L5",
            "notes": (
                f"tick{TICK}; Medium CW; bruto primary envelope (omzet empty); assets/debt Unknown; "
                f"preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Melis Home 0787.300.696 FREE deferred; "
                f"not TE-additive of 348bn; DISTINCT Sint Lodewijk/Lork Hoeselt/Anima stack"
            ),
        }
    )
write_csv(DATA / "commitments.csv", comms, ch)

lbs, lh = read_csv(DATA / "leaderboard.csv")
if not any(r["item_id"] == LB for r in lbs):
    lbs.append(
        {
            "item_id": LB,
            "name": "Sint-Vincentius Aaigem bruto JUMP 743k / omzet empty / pnl LOSS FLIP (YE2025)",
            "level": "L5",
            "type": "wzc_vzw_statutory",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>ErpeMere>SintVincentiusAaigem>JR2025",
            "annual_cost_eur": str(BRUTO),
            "total_cost_eur": str(BRUTO),
            "tco_notes": (
                f"CW bruto envelope 743k (omzet empty) / FTE 0 / 2 VE; pnl LOSS FLIP to {PNL} "
                f"from {PNL_2024}; equity JUMP {equity_pct:.1f}%; dual operating WZC 0422620585; "
                f"assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": "src_sint_vincentius_aaigem_jr2025_cw_en",
            "beneficiaries": "WZC clients Aaigem / Sint-Vincentius path",
            "stated_goal": "Care-path VZW / WZC Aaigem dual",
            "measured_outcome": (
                f"omzet empty; bruto JUMP {bruto_pct:.2f}%; pnl LOSS FLIP to {PNL}; "
                f"equity JUMP {equity_pct:.2f}%; FTE {FTE}"
            ),
            "absurdity_score": "5.5",
            "cost_score": "3.8",
            "difficulty": "3.5",
            "priority_index": "5.0",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose related-party vs operating "
                "WZC 0422.620.585; clarify CW pubs mislabel vs HealthPro/care site"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                f"Melis Home FREE deferred"
            ),
        }
    )
write_csv(DATA / "leaderboard.csv", lbs, lh)

foi, fh = read_csv(DATA / "foi_queue.csv")
if not any(r["gap_id"] == GAP for r in foi):
    foi.append(
        {
            "gap_id": GAP,
            "hierarchy_path": (
                "Vlaanderen>OostVlaanderen>ErpeMere>SintVincentiusAaigem>"
                "NBB_PDF_assets_debt_omzet_empty_pnl_flip_related_wzc"
            ),
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "omzet/code70 empty behind bruto 743k; related-party matrix vs operating "
                "WZC Sint.-Vincentius KBO 0422.620.585 (CoBRHA); Erpe-Mere/RIZIV toelage; "
                "NACE/activity clarification vs CW 'Andere drinkgelegenheden'"
            ),
            "why_it_matters": (
                "Medium CW shows care-path VZW at WZC Aaigem address with empty omzet, "
                "bruto 743k, pnl LOSS FLIP, FTE 0 and dual operating WZC KBO — opacity on "
                "where public/care euros sit between the two entities"
            ),
            "priority": "8",
            "recipient_body": "Sint-Vincentius Aaigem VZW / Sint-Vincentius VZW",
            "recipient_email": "info@sint-vincentius-vzw.be",
            "recipient_postal": "Aaigemdorp 68, 9420 Erpe-Mere",
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
            "leftover dual — Sint-Vincentius Aaigem YE2025 Medium "
            "(bruto JUMP 743k / omzet empty / pnl LOSS FLIP)"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "Completed leftover Sint-Vincentius Aaigem after Sint Lodewijk/Lork race; preferred "
            "AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; "
            "FOI ready not sent; Melis Home deferred"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK} Sint-Vincentius Aaigem Medium bruto JUMP {BRUTO/1e3:.1f}k "
            f"({bruto_pct:.2f}%) omzet empty pnl LOSS FLIP {PNL} equity JUMP {EQUITY/1e6:.2f}m "
            f"FTE {FTE}; KBO Actief VZW 2 VE; dual WZC 0422620585; FOI info@sint-vincentius-vzw.be; "
            f"next every-10 2170"
        )
if not any(r["task_id"] == NEXT_RQ for r in rq):
    rq.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "EVERY-10 + leftover dual hole-fill after Sint-Vincentius Aaigem — "
                "prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2170 EVERY-10: refresh progress_every_10_ticks.md + doge_waste_top10_current.md "
                "THEN leftover dual after rq_2169 Sint-Vincentius Aaigem YE2025 Medium (bruto JUMP 743k "
                "/ omzet empty / pnl LOSS FLIP). Prefer leftover AGB/APB if JR2025 PDF live, else FARO "
                "if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS (optional: "
                "Melis Home 0787.300.696 YE2025 FREE bruto 72k / Abdij Affligem 0400.371.161 YE2025 FREE "
                "omzet 565k). Do NOT redo Sint-Vincentius Aaigem/Sint Lodewijk Schilde/Lork Hoeselt/"
                "Anima hold/Avondvrede/Anima Vlaanderen/t Hofke/Zorg-Saam/Sint-Bernardus/Ruggeveld/"
                "Salvator/Boterlaarhof/WZND/Foyer De Lork Geel/Maria Rustoord/Samen Ouder/"
                "Zusters Sint-Vincentius Deinze/Vrijzicht/Wijtshage/Huize Vincent/Christine/"
                "Witte Meren/Molenheide/Vander Stokken/Sint-Barbara Herselt/operating WZC 0422620585 "
                "if still no YE2025."
            ),
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": (
                "spawned after tick2169 Sint-Vincentius Aaigem; FARO/AIESH/REW still YE2024; "
                "EVERY-10 mandatory at 2170"
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
            f"tick{TICK} leftover Sint-Vincentius Aaigem 0644.843.825 Medium (bruto JUMP 743k; "
            f"omzet empty; pnl LOSS FLIP 97.8k; equity JUMP 4.25m; FTE 0; dual WZC 0422620585); "
            f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; Melis FREE deferred; next {NEXT_RQ}; "
            f"EVERY-10 at 2170; continuous hole_fill"
        )
write_csv(DATA / "loop_state.csv", state_rows, sth)
print("DONE tick", TICK, "bruto", BRUTO, "pnl", PNL, f"bruto_pct={bruto_pct:.2f}")
