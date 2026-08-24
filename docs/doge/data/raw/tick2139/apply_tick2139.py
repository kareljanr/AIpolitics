# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T16:20:00Z"
TICK = 2139
RQ = "rq_2139"
NEXT_RQ = "rq_2140"
ENTITY = "vzw_zorgcampus_denderrust_aalst"
GAP = "gap_denderrust_nbb_pdf_assets_debt_pnl_drop_omzet_jump_merger_dienstengroep_matrix_l5"
COMM = "comm_denderrust_jr2025_statutory_wzc_vzw"
LB = "lb_denderrust_omzet_11_14m_pnl_drop_bruto_12_10m_jr2025"
SRC_EN = "src_denderrust_jr2025_cw_en"
KBO = "0419.333.572"
KBO_DIGITS = "0419333572"
OMZET = "11135834"
OMZET_PRIOR = "10742203"
OMZET_YOY = "+3.66%"
BRUTO = "12099041"
BRUTO_PRIOR = "11424596"
BRUTO_YOY = "+5.90%"
PNL = "47586"
PNL_PRIOR = "152817"
PNL_YOY = "-68.86%"
EQUITY = "8526706"
EQUITY_PRIOR = "8482380"
EQUITY_YOY = "+0.52%"
FTE = "139.9"
FTE_PRIOR = ""
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
                "leftover dual — Zorgcampus Denderrust Aalst YE2025 Medium "
                "(omzet JUMP 11.14m / pnl DROP / bruto JUMP 12.10m)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Denderrust Medium omzet JUMP 11.14m ({OMZET_YOY}) "
                f"bruto JUMP 12.10m ({BRUTO_YOY}) pnl DROP 48k ({PNL_YOY}) equity JUMP 8.53m "
                f"({EQUITY_YOY}) FTE {FTE}; KBO Actief VZW 1 VE aanbestedende overheid; "
                f"absorbed Dienstengroep 0409.698.009 17.12.2025; FOI ready; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; "
                f"EVERY-10 MUST at 2140"
            )
            r["instructions"] = (
                f"Completed leftover Zorgcampus Denderrust YE2025 Medium CW after Residence Prestige; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} "
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
                    "EVERY-10 progress + leftover dual hole-fill after Denderrust — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} EVERY-10 MANDATORY: refresh progress_every_10_ticks.md "
                    "(layers A-E of EUR 347.956 bn TE) + doge_waste_top10_current.md "
                    "(top 10 by priority_index). Then leftover dual after Zorgcampus Denderrust "
                    "Aalst YE2025 Medium (omzet JUMP / pnl DROP). Prefer leftover AGB/APB if JR2025 "
                    "PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. "
                    "Do NOT redo Zorgcampus Denderrust Aalst, Residence Prestige Chaudfontaine, "
                    "Les Corolles Tournai, l'Esplanade Ath, Residence Les Peupliers Seneffe, "
                    "MRS Comte d'Egmont / Residence Comte d'Egmont Chièvres, C.I.G.B. Menen / "
                    "PC Menen / Huize Ter Walle, Maagd Der Armen / Ten Rozen Aalst, L'Orchidée Ittre, "
                    "Care-Support, MPC Sint-Franciscus, Zorghome De Fakkel, Restel Flats, "
                    "Le Château Vert, SLG Wallonie, Famifamenne, Residence Le Castel, R.S.W., "
                    "Home Sebrechts, Unite Jolimont, t Buurthuis, Le Bosquet, Strebo, Entraide, "
                    "La Charmille, Charmilles, Sittelles, Les Buissons, Residence 3, "
                    "Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, Sint-Camillus, IDELUX*, "
                    "INTRADEL, Korian*, SLG Operaties VL, SLG Vlaanderen VZW, Always Home, AREWAL, "
                    "AGB Bornem, Armonea holding, emeis holding, Maria's Rustoord Moorslede, "
                    "Heilig Hart Grimbergen, Veilige Have, Molenheide, Huize Sint-Jozef Ieper, "
                    "PC Gent-Sleidinge, PC Sint-Hiëronymus, Prinsenhof, Akapella, Familiehof, "
                    "La Moisson (absorbed), Denderrust Dienstengroep (absorbed)."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Denderrust; EVERY-10 MUST; "
                    "FARO/AIESH/REW still YE2024"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_denderrust_jr2025_cw",
        "title": "Companyweb NL Zorgcampus Denderrust YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/zorgcampus-denderrust",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl DROP {PNL} ({PNL_YOY} vs YE2024 {PNL_PRIOR}) equity JUMP {EQUITY} ({EQUITY_YOY}) "
            f"FTE {FTE}; neerlegging 03.06.2026; assets/debt Unknown; "
            "raw docs/doge/data/raw/tick2139/denderrust_cw_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Zorgcampus Denderrust YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/zorgcampus-denderrust",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 03-06-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss DROP {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; Principal activity nursing homes / WZC; "
            "raw docs/doge/data/raw/tick2139/denderrust_cw_en.html"
        ),
    },
    {
        "source_id": "src_denderrust_jr2025_cw_fr",
        "title": "Companyweb FR Zorgcampus Denderrust YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/zorgcampus-denderrust",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2139/denderrust_cw_fr.html",
    },
    {
        "source_id": f"src_denderrust_kbo_{TICK}",
        "title": f"KBO Zorgcampus Denderrust {KBO} Actief VZW Aalst aanbestedende overheid",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; VZW sinds 20.02.1979; Alfons De Cockstraat 12A 9310 Aalst; "
            "1 VE; NACE 87.101 RVT / 87.301 ROB / 88.102; aanbestedende overheid sinds 18.01.2003; "
            "RSZ-werkgever; absorbed Denderrust Dienstengroep 0409.698.009 since 17.12.2025"
        ),
    },
    {
        "source_id": f"src_denderrust_site_{TICK}",
        "title": "Zorgcampus Denderrust site + contact FOI administratie@",
        "url": "https://www.denderrust.be/contact/",
        "publisher": "Zorgcampus Denderrust",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; WZC Aalst campus; FOI administratie@denderrust.be "
            "(Cloudflare-decoded from contact page); tel 053 60 60 40"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Zorgcampus Denderrust (WZC/RVT — VZW Aalst; aanbestedende overheid)",
        "name_fr": "Zorgcampus Denderrust (MRS/MRPA — ASBL Alost; pouvoir adjudicateur)",
        "name_en": "Zorgcampus Denderrust (nursing home campus — VZW Aalst; contracting authority)",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.denderrust.be/",
        "foi_email": "administratie@denderrust.be",
        "foi_postal": "Alfons De Cockstraat 12A, 9310 Aalst",
        "notes": (
            f"tick{TICK} leftover VL WZC after Residence Prestige; Medium CW YE2025; "
            f"KBO {KBO}; omzet JUMP 11.14m pnl DROP 48k bruto JUMP 12.10m equity 8.53m FTE {FTE}; "
            "aanbestedende overheid; absorbed Dienstengroep 0409.698.009 17.12.2025; "
            "FOI ready; DISTINCT Prestige/Corolles/Esplanade/Peupliers/Comte d'Egmont/CIGB/Ten Rozen"
        ),
    },
)

for bid, amt, basis in [
    ("bud_denderrust_omzet_jr2025_statutory", OMZET, "CW YE2025 Omzet / Turnover"),
    ("bud_denderrust_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin"),
    ("bud_denderrust_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss DROP"),
    ("bud_denderrust_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
    ("bud_denderrust_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
                "tick2139; Medium CW; assets/debt Unknown pending NBB PDF; "
                "aanbestedende overheid VZW"
            ),
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Zorgcampus Denderrust YE2025 leftover dual (omzet 11.14m / pnl DROP / bruto 12.10m)",
        "entity_id": ENTITY,
        "beneficiary": "WZC residents Aalst (Dendervallei / Vlaanderen)",
        "legal_basis": f"VZW WZC/RVT ROB (KBO {KBO}); aanbestedende overheid; Bestuursdecreet",
        "decision_date": "2026-06-03",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
            f'"2025_fte":{FTE},"2024_omzet":{OMZET_PRIOR},"2024_bruto":{BRUTO_PRIOR},'
            f'"2024_pnl":{PNL_PRIOR},"2024_equity":{EQUITY_PRIOR}}}'
        ),
        "remaining_eur": "0",
        "status": "ended",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/zorgcampus-denderrust",
        "stated_goal": "Residential care / WZC-RVT for elderly (Aalst campus)",
        "cut_option": (
            "Publish NBB PDF assets/debt; explain pnl DROP vs omzet JUMP; disclose RIZIV/VL subsidy "
            "vs resident-fee split; map Dienstengroep absorption impact"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Aalst>Denderrust>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT Prestige/Corolles/Esplanade/Peupliers/Comte d'Egmont/CIGB/Ten Rozen"
        ),
    },
)

# pi ≈ 0.55*5.9 + 0.35*6.2 + 0.10*(11-3.0) = 3.245+2.17+0.80 = 6.215 → 6.2
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": (
            "Zorgcampus Denderrust omzet JUMP 11.14m / pnl DROP 48k / bruto JUMP 12.10m (YE2025)"
        ),
        "level": "L5",
        "type": "wzc_vzw",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Aalst>Denderrust>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY}; bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} DROP {PNL_YOY} vs prior {PNL_PRIOR}; equity {EQUITY} JUMP {EQUITY_YOY}; "
            f"FTE {FTE}; assets/debt Unknown pending NBB PDF; aanbestedende overheid; "
            "Dienstengroep absorbed 17.12.2025"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "WZC residents Aalst campus",
        "stated_goal": "Residential care / WZC-RVT for elderly",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl DROP {PNL_YOY}; "
            f"equity JUMP {EQUITY_YOY}; FTE {FTE}"
        ),
        "absurdity_score": "5.9",
        "cost_score": "6.2",
        "difficulty": "3.0",
        "priority_index": "6.2",
        "cut_proposal": (
            "FOI NBB PDF + pnl-DROP vs omzet-JUMP path + RIZIV/VL split + Dienstengroep merger map"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT Prestige/Corolles/Esplanade/Peupliers/Comte d'Egmont/CIGB/Ten Rozen"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>OostVlaanderen>Aalst>Denderrust>NBB_PDF_assets_debt_pnl_drop_omzet_jump_merger"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DROP path vs omzet JUMP "
            "11.14m; RIZIV/VL care vs resident fee split vs bruto 12.10m; Denderrust Dienstengroep "
            "0409.698.009 absorption (17.12.2025) assets/debt/FTE impact"
        ),
        "why_it_matters": (
            "Medium CW shows aanbestedende-overheid WZC with omzet JUMP to 11.14m while pnl DROP "
            "−69% and assets/debt unknown — public-care opacity plus mid-year Dienstengroep merger"
        ),
        "priority": "8",
        "recipient_body": "Zorgcampus Denderrust VZW",
        "recipient_email": "administratie@denderrust.be",
        "recipient_postal": "Alfons De Cockstraat 12A, 9310 Aalst",
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
        "notes": f"tick{TICK}; human-send only; Medium CW; EVERY-10 next at 2140",
    },
)

with open(DATA / "loop_state.csv", newline="", encoding="utf-8") as f:
    fields = csv.DictReader(f).fieldnames
with open(DATA / "loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
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
                f"tick{TICK} leftover Denderrust {KBO} Medium CW (omzet JUMP 11.14m bruto JUMP 12.10m "
                f"pnl DROP 48k equity JUMP 8.53m FTE {FTE}; Actief VZW 1 VE aanbestedende overheid; "
                f"Dienstengroep absorbed; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; EVERY-10 MUST 2140; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Zorgcampus Denderrust Aalst (omzet JUMP 11.14m / pnl DROP / bruto JUMP 12.10m / Medium)

- Unit: **{RQ}** leftover dual after **rq_2138 Residence Prestige**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW last balance 2024 / filed 24-11-2025); AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Zorgcampus Denderrust VZW** YE2025 (KBO **{KBO}**; Alfons De Cockstraat 12A Aalst; **VZW** NACE **87.101/87.301/88.102** / **1 VE**; **aanbestedende overheid**; absorbed **Denderrust Dienstengroep 0409.698.009** 17.12.2025). Do not redo Residence Prestige/Les Corolles/l'Esplanade/Les Peupliers/Comte d'Egmont/CIGB Menen/Ten Rozen/L'Orchidée/Care-Support/Restel Flats/De Fakkel/Prinsenhof.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY} vs YE2024 EUR{OMZET_PRIOR}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY} vs YE2024 EUR{BRUTO_PRIOR}; pnl **EUR{PNL}** DROP {PNL_YOY} vs YE2024 EUR{PNL_PRIOR}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}**; neerlegging **03.06.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via administratie@denderrust.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.2); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open (EVERY-10); loop_state ticks={TICK}; raw docs/doge/data/raw/tick2139/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2130**; next **2140 MUST** refresh progress + waste top10). Next: {NEXT_RQ} EVERY-10 then (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "omzet", OMZET, "bruto", BRUTO, "pnl", PNL, "equity", EQUITY)
