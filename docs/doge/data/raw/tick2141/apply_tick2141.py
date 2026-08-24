# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T17:00:00Z"
TICK = 2141
RQ = "rq_2141"
NEXT_RQ = "rq_2142"
ENTITY = "asbl_denderrust_dienstengroep"
GAP = "gap_denderrust_dienstengroep_nbb_pdf_assets_debt_omzet_serviceflat_absorption_matrix_l5"
COMM = "comm_denderrust_dienstengroep_jr2025_statutory_serviceflat_absorption"
LB = "lb_denderrust_dienstengroep_omzet_0_63m_stopgezet_absorption_jr2025"
SRC_EN = "src_denderrust_dienstengroep_jr2025_cw_en"
KBO = "0409.698.009"
KBO_DIGITS = "0409698009"
CAMPUS = "0419.333.572"
OMZET = "627905"
OMZET_PRIOR = "617808"
OMZET_YOY = "+1.63%"
BRUTO = "317497"
BRUTO_PRIOR = "324000"
BRUTO_YOY = "-2.01%"
PNL = "82762"
PNL_PRIOR = "81539"
PNL_YOY = "+1.50%"
EQUITY = "1098146"
EQUITY_PRIOR = "1015384"
EQUITY_YOY = "+8.15%"
FTE = "0"
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
                "leftover dual — Denderrust Dienstengroep YE2025 Medium "
                "(omzet 0.63m / Stopgezet absorption campus)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Dienstengroep Medium omzet JUMP 0.63m bruto DROP 0.32m pnl JUMP 83k "
                f"equity JUMP 1.10m FTE 0; KBO Stopgezet 17.12.2025 fusie→{CAMPUS}; FOI ready; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2150"
            )
            r["instructions"] = (
                f"Completed leftover Denderrust Dienstengroep YE2025 Medium CW after Denderrust campus; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Stopgezet; "
                f"omzet JUMP {OMZET} bruto DROP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE {FTE}; FOI {GAP}"
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
                    "leftover dual hole-fill after Dienstengroep — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Denderrust Dienstengroep YE2025 Medium (Stopgezet absorption). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. "
                    "Do NOT redo Denderrust Dienstengroep, Zorgcampus Denderrust Aalst, Maison De Repos En Famille, "
                    "Residence Prestige, Les Corolles, l'Esplanade, Les Peupliers, Comte d'Egmont, CIGB Menen, "
                    "Ten Rozen, L'Orchidée, Care-Support, MPC Sint-Franciscus, De Fakkel, Restel Flats, Château Vert, "
                    "SLG Wallonie, Famifamenne, Le Castel, R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, "
                    "Prinsenhof, Maison Dieu, AGB Bornem, Armonea/emeis/Korian holdings, IPFBW, Aquiris, SPGE, IRE*, "
                    "FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                    "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Dienstengroep; FARO/AIESH/REW still YE2024; next every-10 2150"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_denderrust_dienstengroep_jr2025_cw",
        "title": "Companyweb NL Denderrust Dienstengroep YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto DROP {BRUTO} ({BRUTO_YOY}) "
            f"pnl JUMP {PNL} ({PNL_YOY}) equity JUMP {EQUITY} ({EQUITY_YOY}) FTE {FTE}; "
            f"neerlegging 04.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2141/dg_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Denderrust Dienstengroep YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 04-06-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss JUMP {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; Principal activity service flats; raw docs/doge/data/raw/tick2141/dg_en.html"
        ),
    },
    {
        "source_id": "src_denderrust_dienstengroep_jr2025_cw_fr",
        "title": "Companyweb FR Denderrust Dienstengroep YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2141/dg_fr.html",
    },
    {
        "source_id": f"src_denderrust_dienstengroep_kbo_{TICK}",
        "title": f"KBO Denderrust Dienstengroep {KBO} Stopgezet absorption campus",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Stopgezet sinds 17.12.2025; opgeslorpt door Zorgcampus Denderrust {CAMPUS}; "
            "ASBL DENDERRUST DIENSTENGROEP; Alfons De Cockstraat 12 9310 Aalst; 0 VE; NACE BTW 87.302 serviceflats"
        ),
    },
    {
        "source_id": f"src_denderrust_dienstengroep_campus_{TICK}",
        "title": "Zorgcampus Denderrust FOI contact (overnemer Dienstengroep)",
        "url": "https://www.denderrust.be/contact/",
        "publisher": "Zorgcampus Denderrust VZW",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; FOI administratie@denderrust.be; overnemer of Dienstengroep {KBO} since 17.12.2025"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Denderrust Dienstengroep (serviceflats — Stopgezet fusie Zorgcampus)",
        "name_fr": "Denderrust Dienstengroep (flats-services — Stoppée fusion campus)",
        "name_en": "Denderrust Dienstengroep (service flats — stopped / merged into campus)",
        "level": "other",
        "parent_id": "vzw_zorgcampus_denderrust_aalst",
        "community_language": "nl",
        "website": "https://www.denderrust.be/",
        "foi_email": "administratie@denderrust.be",
        "foi_postal": "Alfons De Cockstraat 12, 9310 Aalst",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Stopgezet 17.12.2025 "
            f"Fusie door overneming→{CAMPUS}; omzet JUMP 0.63m ({OMZET_YOY}) bruto DROP 0.32m ({BRUTO_YOY}) "
            f"pnl JUMP 83k ({PNL_YOY}) equity JUMP 1.10m ({EQUITY_YOY}) FTE {FTE}; assets/debt Unknown; "
            f"filed 04.06.2026; 0 VE NACE 87.302; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "DISTINCT Zorgcampus Denderrust campus (tick2140)"
        ),
    },
)

for bid, amt, basis in [
    ("bud_denderrust_dienstengroep_omzet_jr2025_statutory", OMZET, "CW YE2025 Omzet / Turnover"),
    ("bud_denderrust_dienstengroep_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin DROP"),
    ("bud_denderrust_dienstengroep_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss JUMP"),
    ("bud_denderrust_dienstengroep_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
    ("bud_denderrust_dienstengroep_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
                f"entity Stopgezet 17.12.2025 fusie→{CAMPUS}"
            ),
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": (
            "Denderrust Dienstengroep YE2025 leftover dual (omzet 0.63m / Stopgezet absorption campus)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "Service-flat seniors Aalst → Zorgcampus Denderrust group",
        "legal_basis": (
            f"ASBL serviceflats (KBO {KBO}; Stopgezet fusie→{CAMPUS} 17.12.2025; NACE 87.302)"
        ),
        "decision_date": "2026-06-04",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET_PRIOR},'
            f'"2024_bruto":{BRUTO_PRIOR},"2024_pnl":{PNL_PRIOR},"2024_equity":{EQUITY_PRIOR},'
            f'"stop_fusie":"2025-12-17","overnemer":"{CAMPUS}"}}'
        ),
        "remaining_eur": "0",
        "status": "ended",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "stated_goal": "Service flats for elderly (assistentiewoningen) — pre-merger shell",
        "cut_option": (
            "Publish NBB PDF assets/debt; disclose serviceflat vs other receipts; "
            "publish fusie dossier to Zorgcampus Denderrust (BS + overgenomen activa/schulden)"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Aalst>DenderrustDienstengroep>JR2025_statutory_L5_fusie",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT Zorgcampus Denderrust campus"
        ),
    },
)

# pi ≈ 0.55*4.2 + 0.35*5.5 + 0.10*(11-3.0) = 2.31+1.925+0.80 = 5.035 → 5.0
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": (
            "Denderrust Dienstengroep omzet 0.63m / Stopgezet fusie Zorgcampus / FTE 0 (YE2025)"
        ),
        "level": "L5",
        "type": "serviceflat_asbl",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Aalst>DenderrustDienstengroep>JR2025_fusie",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY}; bruto {BRUTO} DROP {BRUTO_YOY}; "
            f"pnl {PNL} JUMP {PNL_YOY}; equity {EQUITY} JUMP {EQUITY_YOY}; FTE {FTE}; "
            f"assets/debt Unknown pending NBB PDF; KBO Stopgezet 17.12.2025 fusie→{CAMPUS}"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "Service-flat seniors Aalst → campus",
        "stated_goal": "Service flats for elderly (assistentiewoningen)",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto DROP {BRUTO_YOY}; pnl JUMP {PNL_YOY}; "
            f"equity JUMP {EQUITY_YOY}; FTE {FTE}; entity Stopgezet fusie 17.12.2025"
        ),
        "absurdity_score": "5.5",
        "cost_score": "3.2",
        "difficulty": "3.0",
        "priority_index": "5.0",
        "cut_proposal": (
            "FOI NBB PDF + serviceflat split + fusie dossier Zorgcampus Denderrust"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT Zorgcampus Denderrust campus (tick2140)"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>OostVlaanderen>Aalst>DenderrustDienstengroep>NBB_PDF_assets_debt_serviceflat_absorption"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); serviceflat omzet vs other receipts; "
            f"fusie 17.12.2025 dossier (BS/akte, overgenomen activa/schulden) to Zorgcampus {CAMPUS}; "
            "bruto DROP path at FTE 0"
        ),
        "why_it_matters": (
            "Medium CW shows Aalst serviceflat ASBL with omzet 0.63m then Stopgezet via absorption into "
            "Zorgcampus Denderrust — public-care / merger transparency gap while assets/debt opaque"
        ),
        "priority": "8",
        "recipient_body": "Zorgcampus Denderrust VZW (overnemer Denderrust Dienstengroep)",
        "recipient_email": "administratie@denderrust.be",
        "recipient_postal": "Alfons De Cockstraat 12, 9310 Aalst",
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
                f"tick{TICK} leftover Denderrust Dienstengroep {KBO} Medium CW (omzet JUMP 0.63m bruto DROP 0.32m "
                f"pnl JUMP 83k equity JUMP 1.10m FTE 0; Stopgezet 17.12.2025 fusie→{CAMPUS}; assets/debt Unknown); "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2150; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Denderrust Dienstengroep (omzet JUMP 0.63m / Stopgezet fusie campus / Medium)

- Unit: **{RQ}** leftover dual after **rq_2140 Zorgcampus Denderrust EVERY-10**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Denderrust Dienstengroep ASBL** YE2025 (KBO **{KBO}**; Alfons De Cockstraat 12 Aalst; **ASBL** NACE **87.302** / **0 VE**; Stopgezet **17.12.2025** Fusie door overneming → **Zorgcampus {CAMPUS}**). Do not redo Zorgcampus Denderrust campus/En Famille/Prestige/Corolles/Esplanade.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** DROP {BRUTO_YOY}; pnl **EUR{PNL}** JUMP {PNL_YOY}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}**; neerlegging **04.06.2026**. KBO Strong Stopgezet + absorption. Assets/debt Unknown. Medium. FOI via administratie@denderrust.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.0); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2141/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2140**; next **2150**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "omzet", OMZET, "pnl", PNL, "equity", EQUITY)
