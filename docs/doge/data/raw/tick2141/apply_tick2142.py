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
COMM = "comm_groep_sint_franciscus_jr2025_statutory_wzc_vzw"
LB = "lb_groep_sint_franciscus_omzet_31_0m_pnl_flip_bruto_32_9m_jr2025"
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
PNL_YOY = "+167.04%"
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
                "(omzet JUMP 31.0m / pnl FLIP PROFIT / bruto JUMP 32.9m)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Groep SF Medium omzet JUMP 31.0m ({OMZET_YOY}) "
                f"bruto JUMP 32.9m ({BRUTO_YOY}) pnl FLIP PROFIT 164k ({PNL_YOY}) "
                f"equity DROP 25.15m ({EQUITY_YOY}) FTE DROP {FTE} (vs {FTE_PRIOR}); "
                f"KBO Actief VZW 5 VE aanbestedende overheid; FOI ready; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; "
                f"next every-10 2150"
            )
            r["instructions"] = (
                f"Completed leftover Groep Sint-Franciscus Brakel YE2025 Medium CW after "
                f"Dienstengroep; preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl FLIP {PNL} equity DROP {EQUITY} "
                f"FTE {FTE}; FOI {GAP}"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"{RQ} open not found — race?")
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
                    "(omzet JUMP / pnl FLIP). Prefer leftover AGB/APB if JR2025 PDF live, else "
                    "FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. "
                    "Do NOT redo Groep Sint-Franciscus Brakel / Groep van Voorzieningen "
                    "Sint-Franciscus, Denderrust Dienstengroep, Zorgcampus Denderrust Aalst, "
                    "Maison De Repos En Famille Vaux, Residence Prestige Chaudfontaine, "
                    "Les Corolles Tournai, l'Esplanade Ath, Residence Les Peupliers Seneffe, "
                    "MRS Comte d'Egmont, C.I.G.B. Menen, Maagd Der Armen / Ten Rozen, "
                    "L'Orchidée Ittre, Care-Support, MPC Sint-Franciscus Roosdaal, "
                    "Zorghome De Fakkel, Restel Flats, Le Château Vert, SLG Wallonie, "
                    "Famifamenne, Residence Le Castel, R.S.W., Home Sebrechts, Unite Jolimont, "
                    "t Buurthuis, Le Bosquet, Strebo, Entraide, La Charmille, Charmilles, "
                    "Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, "
                    "Zilverlinde Olen, Sint-Camillus, IDELUX*, INTRADEL, Korian*, Always Home, "
                    "AREWAL, AGB Bornem, Armonea holding, emeis holding, Prinsenhof, Akapella, "
                    "Familiehof, La Moisson (absorbed), Denderrust Dienstengroep (absorbed), "
                    "Zusterhof Geel, Den Akker, Mater Dei, Vander Stokken."
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
            f"pnl FLIP {PNL} ({PNL_YOY} vs YE2024 {PNL_PRIOR}) equity DROP {EQUITY} ({EQUITY_YOY}) "
            f"FTE DROP {FTE} (vs {FTE_PRIOR}); neerlegging 24.06.2026; assets/debt Unknown; "
            "raw docs/doge/data/raw/tick2141/franciscus_cw_nl.html"
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
            f"Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss FLIP {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; Principal activity nursing homes ROB/RVT; "
            "raw docs/doge/data/raw/tick2141/franciscus_cw_en.html"
        ),
    },
    {
        "source_id": "src_groep_sint_franciscus_jr2025_cw_fr",
        "title": "Companyweb FR Groep Sint-Franciscus YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/groep-van-voorzieningen-sint-franciscus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; FR mirror YE2025 Medium; "
            "raw docs/doge/data/raw/tick2141/franciscus_cw_fr.html"
        ),
    },
    {
        "source_id": f"src_groep_sint_franciscus_kbo_{TICK}",
        "title": f"KBO Groep Sint-Franciscus {KBO} Actief VZW Brakel aanbestedende overheid",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; VZW sinds 08.11.1972; St.-Martensstraat 3 9660 Brakel; "
            "5 VE; NACE 87.101 RVT / 87.301 ROB / 87.302 serviceflats / 88.102; "
            "aanbestedende overheid sinds 08.11.1972; RSZ-werkgever"
        ),
    },
    {
        "source_id": f"src_groep_sint_franciscus_site_{TICK}",
        "title": "Groep Sint-Franciscus site + contact FOI info.sft@",
        "url": "https://www.groepsf.be/contact",
        "publisher": "Groep Sint-Franciscus",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; 5 WZC campuses Zuid-Oost-Vlaanderen; FOI info.sft@groepsf.be "
            "(Brakel HQ / Sint-Franciscustehuis); tel 055 43 21 11; form on groepsf.be/contact"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": (
            "Groep van Voorzieningen Sint-Franciscus (WZC-koepel Brakel/Oosterzele/Haaltert; "
            "aanbestedende overheid)"
        ),
        "name_fr": (
            "Groupe de Services Sint-Franciscus (groupe MRS Brakel/Oosterzele/Haaltert; "
            "pouvoir adjudicateur)"
        ),
        "name_en": (
            "Groep Sint-Franciscus (nursing-home group Brakel/Oosterzele/Haaltert; "
            "contracting authority)"
        ),
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.groepsf.be/",
        "foi_email": "info.sft@groepsf.be",
        "foi_postal": "St.-Martensstraat 3, 9660 Brakel",
        "notes": (
            f"tick{TICK} leftover VL WZC koepel after Dienstengroep; Medium CW YE2025; "
            f"KBO {KBO}; omzet JUMP 31.0m pnl FLIP 164k bruto JUMP 32.9m equity DROP 25.15m "
            f"FTE DROP {FTE}; aanbestedende overheid 5 VE; FOI ready; "
            "DISTINCT MPC Sint-Franciscus Roosdaal / Zilverlinde Olen / Denderrust"
        ),
    },
)

for bid, amt, basis in [
    ("bud_groep_sint_franciscus_omzet_jr2025_statutory", OMZET, "CW YE2025 Omzet / Turnover"),
    ("bud_groep_sint_franciscus_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin"),
    ("bud_groep_sint_franciscus_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss FLIP PROFIT"),
    ("bud_groep_sint_franciscus_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
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
            "notes": (
                f"tick{TICK}; Medium CW; assets/debt Unknown pending NBB PDF; "
                "aanbestedende overheid VZW 5 VE"
            ),
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": (
            "Groep Sint-Franciscus YE2025 leftover dual "
            "(omzet JUMP 31.0m / pnl FLIP / bruto JUMP 32.9m)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "WZC residents Zuid-Oost-Vlaanderen (Brakel/Oosterzele/Haaltert campuses)",
        "legal_basis": f"VZW WZC/RVT ROB (KBO {KBO}); aanbestedende overheid; Bestuursdecreet",
        "decision_date": "2026-06-24",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
            f'"2025_fte":{FTE},"2024_omzet":{OMZET_PRIOR},"2024_bruto":{BRUTO_PRIOR},'
            f'"2024_pnl":{PNL_PRIOR},"2024_equity":{EQUITY_PRIOR},"2024_fte":{FTE_PRIOR}}}'
        ),
        "remaining_eur": "0",
        "status": "ended",
        "evaluation_url": (
            f"https://www.companyweb.be/en/{KBO_DIGITS}/groep-van-voorzieningen-sint-franciscus"
        ),
        "stated_goal": "Multi-campus residential care / WZC-RVT for elderly (5 VE)",
        "cut_option": (
            "Publish NBB PDF assets/debt; explain pnl FLIP vs omzet JUMP; disclose RIZIV/VL "
            "subsidy vs resident-fee split; campus-level matrix across 5 VE"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": (
            "Vlaanderen>OostVlaanderen>Brakel>GroepSintFranciscus>JR2025_statutory_L5"
        ),
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT MPC Sint-Franciscus Roosdaal / Zilverlinde Olen / Denderrust"
        ),
    },
)

# pi ≈ 0.55*6.0 + 0.35*6.6 + 0.10*(11-3.0) = 3.30+2.31+0.80 = 6.41 → 6.4
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": (
            "Groep Sint-Franciscus omzet JUMP 31.0m / pnl FLIP PROFIT 164k / "
            "bruto JUMP 32.9m (YE2025)"
        ),
        "level": "L5",
        "type": "wzc_vzw",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Brakel>GroepSintFranciscus>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY}; bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} FLIP {PNL_YOY} vs prior LOSS {PNL_PRIOR}; equity {EQUITY} DROP "
            f"{EQUITY_YOY}; FTE DROP {FTE} (vs {FTE_PRIOR}); assets/debt Unknown pending "
            "NBB PDF; aanbestedende overheid 5 VE"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "WZC residents Brakel/Oosterzele/Haaltert campuses",
        "stated_goal": "Multi-campus residential care / WZC-RVT for elderly",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl FLIP {PNL_YOY}; "
            f"equity DROP {EQUITY_YOY}; FTE DROP {FTE}"
        ),
        "absurdity_score": "6.0",
        "cost_score": "6.6",
        "difficulty": "3.0",
        "priority_index": "6.4",
        "cut_proposal": (
            "FOI NBB PDF + pnl-FLIP path + RIZIV/VL split + campus matrix across 5 VE"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT MPC Sint-Franciscus Roosdaal / Zilverlinde Olen / Denderrust"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>OostVlaanderen>Brakel>GroepSintFranciscus>"
            "NBB_PDF_assets_debt_pnl_flip_omzet_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl FLIP PROFIT path vs "
            "omzet JUMP 31.0m; RIZIV/VL care vs resident fee split vs bruto 32.9m; campus-level "
            "matrix across 5 VE"
        ),
        "why_it_matters": (
            "Medium CW shows aanbestedende-overheid WZC koepel with omzet JUMP to 31.0m while "
            "pnl FLIP from LOSS −245k to PROFIT 164k and assets/debt unknown — public-care opacity"
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
                f"tick{TICK} leftover Groep Sint-Franciscus {KBO} Medium CW "
                f"(omzet JUMP 31.0m bruto JUMP 32.9m pnl FLIP 164k equity DROP 25.15m "
                f"FTE DROP {FTE}; Actief VZW 5 VE aanbestedende overheid; assets/debt Unknown); "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; "
                f"next every-10 2150; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Groep Sint-Franciscus Brakel (omzet JUMP 31.0m / pnl FLIP PROFIT / bruto JUMP 32.9m / Medium)

- Unit: **{RQ}** leftover dual after **rq_2141 Denderrust Dienstengroep** (race: concurrent closed 2141 as Dienstengroep while this agent had preferred FARO/AIESH/REW still YE2024). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Groep van Voorzieningen Sint-Franciscus VZW** YE2025 (KBO **{KBO}**; St.-Martensstraat 3 Brakel; **VZW** NACE **87.101/87.301/87.302/88.102** / **5 VE**; **aanbestedende overheid**; campuses Brakel/Oosterzele/Haaltert). Do not redo Dienstengroep/Denderrust/En Famille/Prestige/Corolles/Esplanade/Peupliers/Comte d'Egmont/CIGB/Ten Rozen/MPC Sint-Franciscus Roosdaal/Zilverlinde Olen.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY} vs YE2024 EUR{OMZET_PRIOR}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY} vs YE2024 EUR{BRUTO_PRIOR}; pnl **EUR{PNL}** FLIP PROFIT {PNL_YOY} vs YE2024 LOSS EUR{PNL_PRIOR}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; FTE **{FTE}** DROP vs {FTE_PRIOR}; neerlegging **24.06.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info.sft@groepsf.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.4); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2141/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2140**; next **2150**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "omzet", OMZET, "bruto", BRUTO, "pnl", PNL, "equity", EQUITY)
