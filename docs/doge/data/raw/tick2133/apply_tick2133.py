# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T14:20:00Z"
TICK = 2133
RQ = "rq_2133"
NEXT_RQ = "rq_2134"
ENTITY = "vzw_cigb_menen"
GAP = "gap_cigb_menen_nbb_pdf_assets_debt_pnl_loss_flip_omzet_jump_matrix_l5"
COMM = "comm_cigb_menen_jr2025_statutory_pc_htw"
LB = "lb_cigb_menen_omzet_jump_35_15m_pnl_loss_flip_jr2025"
SRC_EN = "src_cigb_menen_jr2025_cw_en"
KBO = "0414.747.056"
KBO_DIGITS = "0414747056"
OMZET = "35153897"
OMZET_PRIOR = "33258491"
OMZET_YOY = "+5.7%"
BRUTO = "30658841"
BRUTO_PRIOR = "29396110"
BRUTO_YOY = "+4.3%"
PNL = "-74821"
PNL_PRIOR = "745951"
PNL_YOY = "-110.03%"
EQUITY = "25810986"
EQUITY_PRIOR = "26310934"
EQUITY_YOY = "-1.9%"
FTE = "371.5"
FTE_PRIOR = "367.6"
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
            r["title"] = "leftover dual — C.I.G.B. Menen YE2025 Medium (pnl LOSS flip)"
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} CIGB Menen Medium omzet JUMP 35.15m bruto JUMP 30.66m pnl LOSS FLIP -75k "
                f"equity DROP 25.81m FTE 371.5; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2140"
            )
            r["instructions"] = (
                f"Completed leftover C.I.G.B. Menen YE2025 Medium CW after Maagd Der Armen / Ten Rozen; "
                f"preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl LOSS FLIP {PNL} equity DROP {EQUITY} FTE {FTE}; FOI {GAP}"
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
                    "leftover dual hole-fill after CIGB Menen — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after C.I.G.B. Menen YE2025 Medium. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. Do NOT redo "
                    "C.I.G.B. Menen / PC Menen / Huize Ter Walle, Maagd Der Armen / Ten Rozen Aalst, L'Orchidée Ittre, "
                    "Care-Support, MPC Sint-Franciscus, Zorghome De Fakkel, Restel Flats, Le Château Vert, SLG Wallonie, "
                    "Famifamenne, Residence Le Castel, R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, Le Bosquet, "
                    "Strebo, Entraide, La Charmille, Charmilles, Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, "
                    "XXe Aout, Ninove, Zilverlinde, Sint-Camillus, IDELUX*, INTRADEL, Korian*, SLG Operaties VL, "
                    "SLG Vlaanderen VZW, Always Home, AREWAL, AGB Bornem, Armonea holding, emeis holding, "
                    "Maria's Rustoord Moorslede, Heilig Hart Grimbergen, Veilige Have, Molenheide, Huize Sint-Jozef Ieper, "
                    "PC Gent-Sleidinge, PC Sint-Hiëronymus."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} CIGB Menen; FARO/AIESH/REW still YE2024; next every-10 2140"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_cigb_menen_jr2025_cw",
        "title": "Companyweb NL C.I.G.B. Menen YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl LOSS FLIP {PNL} ({PNL_YOY}) equity DROP {EQUITY} ({EQUITY_YOY}) FTE {FTE}; "
            f"neerlegging 30.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2133/cigb_cw_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN C.I.G.B. Menen YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/christelijke-integrale-gezondheids-en-bejaardenzorg",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 30-06-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; FTE {FTE}; Principal activity psychiatric hospitals; "
            f"raw docs/doge/data/raw/tick2133/cigb_cw_en.html"
        ),
    },
    {
        "source_id": "src_cigb_menen_jr2025_cw_fr",
        "title": "Companyweb FR C.I.G.B. Menen YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2133/cigb_cw_fr.html",
    },
    {
        "source_id": f"src_cigb_menen_kbo_{TICK}",
        "title": f"KBO C.I.G.B. Menen {KBO} Actief PC+WZC",
        "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Actief VZW; Benediktinessenstraat 9 8930 Menen; 2 VE; "
            "hoofdactiviteit psychiatrische ziekenhuizen sinds 01.01.2025; perimeter PC Menen + Huize Ter Walle"
        ),
    },
    {
        "source_id": f"src_cigb_menen_site_{TICK}",
        "title": "PC Menen / Huize Ter Walle site FOI contact info@pcmenen.be",
        "url": "https://www.pcmenen.be/",
        "publisher": "C.I.G.B. / Psychiatrisch Centrum Menen",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; PC Menen + Huize Ter Walle (htw.be); FOI info@pcmenen.be "
            "(algemeen directeur Serge Deboever) / directie@htw.be"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "C.I.G.B. / Christelijke Integrale Gezondheids- en Bejaardenzorg (Menen; PC + Huize Ter Walle)",
        "name_fr": "C.I.G.B. / Soins de santé et aux personnes âgées intégrés chrétiens (Menin; PC + Huize Ter Walle)",
        "name_en": "C.I.G.B. VZW (Menen; psychiatric centre + Huize Ter Walle WZC)",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.pcmenen.be/",
        "foi_email": "info@pcmenen.be",
        "foi_postal": "Benediktinessenstraat 9, 8930 Menen",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW 2 VE psych hospitals; "
            f"omzet JUMP 35.15m ({OMZET_YOY}) bruto JUMP 30.66m ({BRUTO_YOY}) pnl LOSS FLIP -75k ({PNL_YOY}) "
            f"equity DROP 25.81m ({EQUITY_YOY}) FTE {FTE}; assets/debt Unknown; filed 30.06.2026; FOI {GAP}; "
            "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Ten Rozen / L'Orchidée / Care-Support / "
            "Restel Flats / De Fakkel / PC Gent-Sleidinge / Sint-Hiëronymus"
        ),
    },
)

for bid, amt, basis in [
    ("bud_cigb_menen_omzet_jr2025_statutory", OMZET, "CW YE2025 Omzet / Turnover"),
    ("bud_cigb_menen_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin"),
    ("bud_cigb_menen_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss LOSS flip"),
    ("bud_cigb_menen_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
    ("bud_cigb_menen_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
            "notes": f"tick{TICK}; Medium CW; assets/debt Unknown pending NBB PDF",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "C.I.G.B. Menen YE2025 leftover dual (omzet JUMP 35.15m / pnl LOSS flip)",
        "entity_id": ENTITY,
        "beneficiary": "PC Menen patients + Huize Ter Walle WZC residents (West-Vlaanderen)",
        "legal_basis": f"VZW psych hospital + WZC (KBO {KBO}; 2 VE; psychiatric hospitals NACE)",
        "decision_date": "2026-06-30",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET_PRIOR},'
            f'"2024_bruto":{BRUTO_PRIOR},"2024_pnl":{PNL_PRIOR},"2024_equity":{EQUITY_PRIOR}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": (
            f"https://www.companyweb.be/en/{KBO_DIGITS}/christelijke-integrale-gezondheids-en-bejaardenzorg"
        ),
        "stated_goal": "Psychiatric hospital + elderly residential care (PC Menen / Huize Ter Walle)",
        "cut_option": (
            "Publish NBB PDF assets/debt; disclose RIZIV/VL care vs patient/resident fee split; "
            "explain pnl LOSS flip path despite omzet JUMP"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>WestVlaanderen>Menen>CIGB>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT Ten Rozen / L'Orchidée / Care-Support / Restel Flats / De Fakkel"
        ),
    },
)

# pi ≈ 0.55*6.4 + 0.35*5.2 + 0.10*(11-3.5) = 3.52+1.82+0.75 = 6.09 → 6.1
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "C.I.G.B. Menen omzet JUMP 35.15m / pnl LOSS flip -75k (YE2025)",
        "level": "L5",
        "type": "psych_wzc_vzw",
        "hierarchy_path": "Vlaanderen>WestVlaanderen>Menen>CIGB>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY}; bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} LOSS FLIP {PNL_YOY} vs prior {PNL_PRIOR}; equity {EQUITY} DROP {EQUITY_YOY}; "
            f"FTE {FTE}; assets/debt Unknown pending NBB PDF; 2 VE PC+WZC"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "PC Menen patients + Huize Ter Walle residents",
        "stated_goal": "Psychiatric hospital + elderly residential care",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl LOSS FLIP {PNL_YOY}; "
            f"equity DROP {EQUITY_YOY}; FTE {FTE_PRIOR}→{FTE}"
        ),
        "absurdity_score": "6.4",
        "cost_score": "5.2",
        "difficulty": "3.5",
        "priority_index": "6.1",
        "cut_proposal": (
            "FOI NBB PDF + care-subsidy vs patient/resident-fee split; explain LOSS flip despite omzet JUMP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
            "DISTINCT Ten Rozen / L'Orchidée / Care-Support / Restel Flats / De Fakkel"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>WestVlaanderen>Menen>CIGB>NBB_PDF_assets_debt_pnl_loss_flip",
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); RIZIV/VL care vs patient/resident fee split "
            "PC vs WZC; pnl LOSS flip -75k path; 2 VE activity matrix"
        ),
        "why_it_matters": (
            "Medium CW shows psych+WZC VZW with omzet JUMP 35.15m and pnl LOSS flip -75k while assets/debt and "
            "public-care vs private-fee mix opaque — subsidy transparency gap"
        ),
        "priority": "8",
        "recipient_body": "VZW C.I.G.B. / Psychiatrisch Centrum Menen / Huize Ter Walle",
        "recipient_email": "info@pcmenen.be",
        "recipient_postal": "Benediktinessenstraat 9, 8930 Menen",
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
        "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2140",
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
                f"tick{TICK} leftover CIGB Menen {KBO} Medium CW (omzet JUMP 35.15m bruto JUMP 30.66m "
                f"pnl LOSS FLIP -75k equity DROP 25.81m FTE 371.5; assets/debt Unknown; 2 VE PC+WZC); "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2140; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} C.I.G.B. Menen (omzet JUMP 35.15m / pnl LOSS flip -75k / Medium)

- Unit: **{RQ}** leftover dual after **rq_2132 OLV Maagd Der Armen / Ten Rozen**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **C.I.G.B. VZW** YE2025 (KBO **{KBO}**; Benediktinessenstraat 9 Menen; **VZW** psychiatrische ziekenhuizen / **2 VE**; PC Menen + Huize Ter Walle). Do not redo Ten Rozen/L'Orchidée/Care-Support/Restel Flats/De Fakkel/SLG Wallonie/Famifamenne/MPC Sint-Franciscus/Armonea holding/PC Gent-Sleidinge/Sint-Hiëronymus.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY} vs YE2024 EUR{OMZET_PRIOR}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** LOSS FLIP {PNL_YOY} vs YE2024 EUR{PNL_PRIOR}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; FTE **{FTE}** vs {FTE_PRIOR}; neerlegging **30.06.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info@pcmenen.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.1); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2133/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2130**; next **2140**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "omzet", OMZET, "pnl", PNL)
