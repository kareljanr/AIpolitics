# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T17:20:00Z"
TICK = 2142
RQ = "rq_2142"
NEXT_RQ = "rq_2143"
ENTITY = "vzw_groep_sint_franciscus_brakel"
GAP = "gap_groep_sint_franciscus_nbb_pdf_assets_debt_pnl_flip_omzet_jump_matrix_l5"
COMM = "comm_groep_sint_franciscus_jr2025_statutory_wzc_pnl_flip"
LB = "lb_groep_sint_franciscus_omzet_30_98m_pnl_flip_profit_jr2025"
SRC_EN = "src_groep_sint_franciscus_jr2025_cw_en"
KBO = "0412.763.704"
KBO_DIGITS = "0412763704"
OMZET = "30982834"
OMZET_PRIOR = "29637372"
OMZET_YOY = "+4.54%"
BRUTO = "32903309"
BRUTO_PRIOR = "31584808"
BRUTO_YOY = "+4.17%"
PNL = "164386"
PNL_PRIOR = "-245197"
PNL_YOY = "FLIP_PROFIT"
EQUITY = "25153623"
EQUITY_PRIOR = "25266634"
EQUITY_YOY = "-0.45%"
FTE = "416"
FTE_PRIOR = "427.4"
ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def update_rq():
    path = DATA / "research_queue.csv"
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r.get("task_id") == RQ and r.get("status") == "open":
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["title"] = (
                "leftover dual — Groep Sint-Franciscus Brakel YE2025 Medium "
                "(omzet JUMP 30.98m / pnl FLIP PROFIT)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Groep SF Medium omzet JUMP 30.98m bruto JUMP 32.90m "
                f"pnl FLIP PROFIT 164k equity DROP 25.15m FTE 416; KBO Actief VZW 5 VE "
                f"aanbestedende overheid Brakel; FOI ready; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2150"
            )
            r["instructions"] = (
                f"Completed leftover Groep Sint-Franciscus YE2025 Medium CW after Dienstengroep; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl FLIP {PNL} equity DROP {EQUITY} FTE {FTE}; FOI {GAP}"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"{RQ} open not found")
    if not any(r.get("task_id") == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after Groep Sint-Franciscus — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Groep Sint-Franciscus Brakel YE2025 Medium "
                    "(omzet JUMP / pnl FLIP PROFIT). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. "
                    "Do NOT redo Groep Sint-Franciscus Brakel / Zilverlinde Oosterzele / OLV Ter Veldbloemen / "
                    "Sint-Jozef Haaltert / Sint-Anna Haaltert, Denderrust Dienstengroep, Zorgcampus Denderrust, "
                    "Maison De Repos En Famille, Residence Prestige, Les Corolles, l'Esplanade, Les Peupliers, "
                    "Comte d'Egmont, CIGB Menen, Ten Rozen, L'Orchidée, Care-Support, MPC Sint-Franciscus Roosdaal, "
                    "De Fakkel, Restel Flats, Château Vert, SLG Wallonie, Famifamenne, Le Castel, R.S.W., "
                    "Home Sebrechts, Unite Jolimont, t Buurthuis, Prinsenhof, Maison Dieu, AGB Bornem, "
                    "Armonea/emeis/Korian holdings, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, "
                    "Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, "
                    "Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Groep Sint-Franciscus; "
                    "FARO/AIESH/REW still YE2024; next every-10 2150"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_groep_sint_franciscus_jr2025_cw",
        "title": "Companyweb NL Groep Sint-Franciscus YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/groep-van-voorzieningen-sint-franciscus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl FLIP PROFIT {PNL} (vs YE2024 {PNL_PRIOR}) equity DROP {EQUITY} ({EQUITY_YOY}) FTE {FTE}; "
            f"neerlegging 24.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2142/franciscus_cw_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Groep Sint-Franciscus YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/groep-van-voorzieningen-sint-franciscus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 24-06-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss FLIP PROFIT {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; Principal activity nursing homes; raw docs/doge/data/raw/tick2142/franciscus_cw_en.html"
        ),
    },
    {
        "source_id": "src_groep_sint_franciscus_jr2025_cw_fr",
        "title": "Companyweb FR Groep Sint-Franciscus YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/groep-van-voorzieningen-sint-franciscus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2142/franciscus_cw_fr.html",
    },
    {
        "source_id": f"src_groep_sint_franciscus_kbo_{TICK}",
        "title": f"KBO Groep Sint-Franciscus {KBO} Actief Brakel aanbestedende overheid",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; VZW Groep van Voorzieningen Sint-Franciscus; "
            "St.-Martensstraat 3 9660 Brakel; 5 VE; NACE RVT/ROB; aanbestedende overheid sinds 08.11.1972; "
            "campuses Brakel / Oosterzele / Haaltert"
        ),
    },
    {
        "source_id": f"src_groep_sint_franciscus_site_{TICK}",
        "title": "Groep Sint-Franciscus site FOI info.sft@groepsf.be",
        "url": "https://www.groepsf.be/",
        "publisher": "Groep van Voorzieningen Sint-Franciscus VZW",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; St.-Martensstraat 3 9660 Brakel; FOI info.sft@groepsf.be; "
            "campuses Brakel / Zilverlinde Oosterzele / OLV Ter Veldbloemen / Sint-Jozef+Sint-Anna Haaltert"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Groep van Voorzieningen Sint-Franciscus (Brakel multi-campus WZC)",
        "name_fr": "Groupe de provisions Sint-Franciscus (Brakel multi-campus MRS)",
        "name_en": "Groep Sint-Franciscus (Brakel multi-campus nursing homes)",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.groepsf.be/",
        "foi_email": "info.sft@groepsf.be",
        "foi_postal": "St.-Martensstraat 3, 9660 Brakel",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW aanbestedende overheid; "
            f"omzet JUMP 30.98m ({OMZET_YOY}) bruto JUMP 32.90m ({BRUTO_YOY}) pnl FLIP PROFIT 164k "
            f"(vs LOSS -245k) equity DROP 25.15m ({EQUITY_YOY}) FTE {FTE} (vs {FTE_PRIOR}); "
            f"assets/debt Unknown; filed 24.06.2026; 5 VE; FOI {GAP}; preferred AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; DISTINCT MPC Sint-Franciscus Roosdaal 0415.850.084 / Denderrust"
        ),
    },
)

for bid, amt, basis in [
    ("bud_groep_sint_franciscus_omzet_jr2025_statutory", OMZET, "CW YE2025 Omzet / Turnover"),
    ("bud_groep_sint_franciscus_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin"),
    ("bud_groep_sint_franciscus_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss FLIP PROFIT"),
    ("bud_groep_sint_franciscus_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity DROP"),
    ("bud_groep_sint_franciscus_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
]:
    append_csv(
        DATA / "budgets.csv",
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": amt,
            "amount_min_eur": amt,
            "amount_max_eur": amt,
            "basis": basis,
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2142; Medium CW; assets/debt Unknown pending NBB PDF; aanbestedende overheid VZW",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": (
            "Groep Sint-Franciscus YE2025 leftover dual (omzet JUMP 30.98m / pnl FLIP PROFIT)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "WZC residents Brakel / Oosterzele / Haaltert (Oost-Vlaanderen)",
        "legal_basis": (
            f"VZW WZC/RVT multi-campus (KBO {KBO}; Actief; aanbestedende overheid; 5 VE)"
        ),
        "decision_date": "2026-06-24",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET_PRIOR},'
            f'"2024_bruto":{BRUTO_PRIOR},"2024_pnl":{PNL_PRIOR},"2024_equity":{EQUITY_PRIOR},'
            f'"2024_fte":{FTE_PRIOR},"ve":5}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": (
            f"https://www.companyweb.be/en/{KBO_DIGITS}/groep-van-voorzieningen-sint-franciscus"
        ),
        "stated_goal": "Residential care / WZC-RVT for elderly (multi-campus Oost-Vlaanderen)",
        "cut_option": (
            "Publish NBB PDF assets/debt; disclose RIZIV/VL subsidy vs resident-fee split; "
            "explain pnl FLIP PROFIT path; publish 5 VE campus matrix"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Brakel>GroepSintFranciscus>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT MPC Sint-Franciscus Roosdaal / Denderrust / Prestige"
        ),
    },
)

# pi ≈ 0.55*6.5 + 0.35*6.2 + 0.10*(11-3.0) = 3.575+2.17+0.80 = 6.545 → 6.5
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": (
            "Groep Sint-Franciscus omzet JUMP 30.98m / pnl FLIP PROFIT 164k / FTE DROP (YE2025)"
        ),
        "level": "L5",
        "type": "wzc_vzw",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Brakel>GroepSintFranciscus>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY}; bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} FLIP PROFIT vs YE2024 LOSS {PNL_PRIOR}; equity {EQUITY} DROP {EQUITY_YOY}; "
            f"FTE {FTE} DROP vs {FTE_PRIOR}; assets/debt Unknown pending NBB PDF; "
            "aanbestedende overheid; 5 VE multi-campus"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "WZC residents Brakel / Oosterzele / Haaltert",
        "stated_goal": "Residential care / WZC-RVT for elderly",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl FLIP PROFIT; "
            f"equity DROP {EQUITY_YOY}; FTE {FTE_PRIOR}→{FTE}"
        ),
        "absurdity_score": "6.2",
        "cost_score": "6.5",
        "difficulty": "3.0",
        "priority_index": "6.5",
        "cut_proposal": (
            "FOI NBB PDF + RIZIV/VL split + pnl-FLIP path + 5 VE campus matrix"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT MPC Sint-Franciscus Roosdaal / Denderrust / Prestige"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>OostVlaanderen>Brakel>GroepSintFranciscus>NBB_PDF_assets_debt_pnl_flip_omzet_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl FLIP PROFIT path vs omzet JUMP 30.98m; "
            "RIZIV/VL care vs resident fee split vs bruto 32.90m; 5 VE campus matrix "
            "(Brakel / Zilverlinde Oosterzele / OLV Ter Veldbloemen / Sint-Jozef+Sint-Anna Haaltert); FTE DROP path"
        ),
        "why_it_matters": (
            "Medium CW shows aanbestedende-overheid multi-campus WZC with omzet JUMP to 30.98m flipping to PROFIT "
            "while assets/debt unknown — public-care opacity across 5 VE"
        ),
        "priority": "8",
        "recipient_body": "Groep van Voorzieningen Sint-Franciscus VZW",
        "recipient_email": "info.sft@groepsf.be",
        "recipient_postal": "St.-Martensstraat 3, 9660 Brakel",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-25",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2150",
    },
)

with open(DATA / "loop_state.csv", "w", newline="", encoding="utf-8") as f:
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
            "last_tick_utc": UTC,
            "last_unit_id": RQ,
            "ticks_completed": str(TICK),
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover Groep Sint-Franciscus {KBO} Medium CW (omzet JUMP 30.98m bruto JUMP 32.90m "
                f"pnl FLIP PROFIT 164k equity DROP 25.15m FTE 416; Actief VZW 5 VE aanbestedende overheid Brakel; "
                f"assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; "
                "next every-10 2150; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Groep Sint-Franciscus Brakel (omzet JUMP 30.98m / pnl FLIP PROFIT 164k / Medium)

- Unit: **{RQ}** leftover dual after **rq_2141 Denderrust Dienstengroep**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Groep van Voorzieningen Sint-Franciscus VZW** YE2025 (KBO **{KBO}**; St.-Martensstraat 3 Brakel; **VZW** NACE RVT/ROB / **5 VE**; **aanbestedende overheid**; campuses Brakel / Oosterzele / Haaltert). Do not redo Denderrust Dienstengroep/Zorgcampus Denderrust/En Famille/Prestige/Corolles/MPC Sint-Franciscus Roosdaal.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY} vs YE2024 EUR{OMZET_PRIOR}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** FLIP PROFIT vs YE2024 LOSS EUR{PNL_PRIOR}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; FTE **{FTE}** vs {FTE_PRIOR}; neerlegging **24.06.2026**. KBO Strong Actief + aanbestedende overheid. Assets/debt Unknown. Medium. FOI via info.sft@groepsf.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.5); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2142/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2140**; next **2150**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "omzet", OMZET, "pnl", PNL, "equity", EQUITY)
