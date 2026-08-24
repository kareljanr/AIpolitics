# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T15:00:00Z"
TICK = 2135
RQ = "rq_2135"
NEXT_RQ = "rq_2136"
ENTITY = "bv_residence_les_peupliers_seneffe"
GAP = "gap_peupliers_nbb_pdf_assets_debt_omzet_empty_neg_equity_loss_matrix_l5"
COMM = "comm_peupliers_jr2025_statutory_mrs"
LB = "lb_peupliers_bruto_3_17m_neg_equity_778k_pnl_loss_jr2025"
SRC_EN = "src_peupliers_jr2025_cw_en"
KBO = "0479.984.011"
KBO_DIGITS = "0479984011"
BRUTO = "3170222"
BRUTO_PRIOR = "3036336"
BRUTO_YOY = "+4.41%"
PNL = "-296036"
PNL_PRIOR = "-377649"
PNL_YOY = "+21.61%"
EQUITY = "-778327"
EQUITY_PRIOR = "-482292"
EQUITY_YOY = "-61.38%"
FTE = "51.1"
FTE_PRIOR = "50.7"
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
                "leftover dual — Residence Les Peupliers Seneffe YE2025 Medium "
                "(neg equity -778k / pnl loss)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Les Peupliers Medium bruto JUMP 3.17m pnl LOSS -296k "
                f"equity NEG -778k FTE 51.1; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2140"
            )
            r["instructions"] = (
                f"Completed leftover Residence Les Peupliers YE2025 Medium CW after Comte d'Egmont; "
                f"preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet empty bruto JUMP {BRUTO} pnl LOSS {PNL} equity NEG {EQUITY} FTE {FTE}; FOI {GAP}"
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
                    "leftover dual hole-fill after Les Peupliers — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Residence Les Peupliers YE2025 Medium. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. Do NOT redo "
                    "Residence Les Peupliers Seneffe, MRS Comte d'Egmont / Residence Comte d'Egmont Chièvres, "
                    "C.I.G.B. Menen / PC Menen / Huize Ter Walle, Maagd Der Armen / Ten Rozen Aalst, L'Orchidée Ittre, "
                    "Care-Support, MPC Sint-Franciscus, Zorghome De Fakkel, Restel Flats, Le Château Vert, SLG Wallonie, "
                    "Famifamenne, Residence Le Castel, R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, Le Bosquet, "
                    "Strebo, Entraide, La Charmille, Charmilles, Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, "
                    "XXe Aout, Ninove, Zilverlinde, Sint-Camillus, IDELUX*, INTRADEL, Korian*, SLG Operaties VL, "
                    "SLG Vlaanderen VZW, Always Home, AREWAL, AGB Bornem, Armonea holding, emeis holding, "
                    "Maria's Rustoord Moorslede, Heilig Hart Grimbergen, Veilige Have, Molenheide, Huize Sint-Jozef Ieper, "
                    "PC Gent-Sleidinge, PC Sint-Hiëronymus. Deferred live YE2025: Residence Prestige / l'Esplanade Ath."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Les Peupliers; FARO/AIESH/REW still YE2024; next every-10 2140"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_peupliers_jr2025_cw",
        "title": "Companyweb NL Residence Les Peupliers YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/residence-les-peupliers",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet empty bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl LOSS {PNL} ({PNL_YOY} narrow vs prior) equity NEG {EQUITY} ({EQUITY_YOY}) FTE {FTE}; "
            f"neerlegging 13.08.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2135/peupliers_cw_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Residence Les Peupliers YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/residence-les-peupliers",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 13-08-2026; Last balance sheet year 2025; "
            f"Turnover unpublished; Gross margin {BRUTO}; Equity NEG {EQUITY}; FTE {FTE}; "
            f"Principal activity nursing homes MRPA; raw docs/doge/data/raw/tick2135/peupliers_cw_en.html"
        ),
    },
    {
        "source_id": "src_peupliers_jr2025_cw_fr",
        "title": "Companyweb FR Residence Les Peupliers YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/residence-les-peupliers",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2135/peupliers_cw_fr.html",
    },
    {
        "source_id": f"src_peupliers_kbo_{TICK}",
        "title": f"KBO Residence Les Peupliers {KBO} Actief MRS",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Actief BV/SRL; Avenue de la Motte Baraffe 6 7180 Seneffe; 1 VE; "
            "NACE 87.301 ROB/MRPA; bestuurder BV 0875.884.264 / Marie-Christine Griveau"
        ),
    },
    {
        "source_id": f"src_peupliers_site_{TICK}",
        "title": "Residence Les Peupliers site FOI residencelespeuplierssprl@hotmail.com",
        "url": "https://www.residence-les-peupliers.be/",
        "publisher": "Residence Les Peupliers",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Avenue de la Motte Baraffe 6 7180 Seneffe; "
            "FOI residencelespeuplierssprl@hotmail.com; tel 064 55 91 00"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Residence Les Peupliers (Seneffe MRS/ROB)",
        "name_fr": "Résidence Les Peupliers (Seneffe MRS/MRPA)",
        "name_en": "Residence Les Peupliers (Seneffe nursing home)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.residence-les-peupliers.be/",
        "foi_email": "residencelespeuplierssprl@hotmail.com",
        "foi_postal": "Avenue de la Motte Baraffe 6, 7180 Seneffe",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief BV/SRL 1 VE NACE 87.301; "
            f"omzet empty; bruto JUMP 3.17m ({BRUTO_YOY}) pnl LOSS -296k ({PNL_YOY} narrow) "
            f"equity NEG -778k ({EQUITY_YOY}) FTE {FTE}; assets/debt Unknown; filed 13.08.2026; FOI {GAP}; "
            "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Comte d'Egmont / CIGB Menen / "
            "Ten Rozen / L'Orchidée / Prestige / Esplanade Ath"
        ),
    },
)

for bid, amt, basis in [
    ("bud_peupliers_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin"),
    ("bud_peupliers_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss LOSS (narrowing)"),
    ("bud_peupliers_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity NEG"),
    ("bud_peupliers_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
            "notes": "tick2135; Medium CW; omzet empty; assets/debt Unknown pending NBB PDF",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Residence Les Peupliers YE2025 leftover dual (bruto 3.17m / neg equity -778k)",
        "entity_id": ENTITY,
        "beneficiary": "MRS residents Seneffe (Hainaut / Wallonie)",
        "legal_basis": f"BV/SRL maison de repos MRPA/ROB (KBO {KBO}; 1 VE)",
        "decision_date": "2026-08-13",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": BRUTO,
        "cash_by_year": (
            f'{{"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_bruto":{BRUTO_PRIOR},'
            f'"2024_pnl":{PNL_PRIOR},"2024_equity":{EQUITY_PRIOR},"2024_fte":{FTE_PRIOR}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/residence-les-peupliers",
        "stated_goal": "Private nursing home / maison de repos for elderly (MRPA)",
        "cut_option": (
            "Publish NBB PDF assets/debt; disclose AViQ/INAMI care vs resident fee split; "
            "explain multi-year LOSS + deepening NEG equity path"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>Seneffe>LesPeupliers>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope (omzet empty); assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT Comte d'Egmont / CIGB Menen / Ten Rozen / L'Orchidée"
        ),
    },
)

# pi ≈ 0.55*7.4 + 0.35*4.1 + 0.10*(11-3.5) = 4.07+1.435+0.75 = 6.255 → 6.3
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "Residence Les Peupliers bruto 3.17m / equity NEG -778k / pnl LOSS -296k (YE2025)",
        "level": "L5",
        "type": "mrs_bv",
        "hierarchy_path": "Wallonie>Hainaut>Seneffe>LesPeupliers>JR2025",
        "annual_cost_eur": BRUTO,
        "total_cost_eur": BRUTO,
        "tco_notes": (
            f"CW YE2025 omzet empty; bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} LOSS NARROW {PNL_YOY} vs prior {PNL_PRIOR}; equity {EQUITY} NEG DEEPEN {EQUITY_YOY}; "
            f"FTE {FTE}; assets/debt Unknown pending NBB PDF; 1 VE MRS"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS residents Seneffe",
        "stated_goal": "Private nursing home / maison de repos for elderly",
        "measured_outcome": (
            f"omzet empty; bruto JUMP {BRUTO_YOY}; pnl LOSS NARROW {PNL_YOY}; "
            f"equity NEG DEEPEN {EQUITY_YOY}; FTE {FTE_PRIOR}→{FTE}"
        ),
        "absurdity_score": "7.4",
        "cost_score": "4.1",
        "difficulty": "3.5",
        "priority_index": "6.3",
        "cut_proposal": (
            "FOI NBB PDF + AViQ/INAMI care vs resident-fee split; explain NEG equity deepen despite LOSS narrow"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
            "DISTINCT Comte d'Egmont / CIGB Menen / Ten Rozen / L'Orchidée / Prestige / Esplanade"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Hainaut>Seneffe>LesPeupliers>NBB_PDF_assets_debt_omzet_empty_neg_equity"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); omzet/code70 (CW empty); "
            "AViQ/INAMI care vs resident fee split; pnl LOSS -296k + equity NEG -778k deepen path; "
            "related-party / management fees / continuity plan"
        ),
        "why_it_matters": (
            "Medium CW shows private MRS BV with bruto 3.17m but multi-year LOSS and equity NEG deepen "
            "to -778k while assets/debt and public-care mix opaque — subsidy/solvency transparency gap"
        ),
        "priority": "8",
        "recipient_body": "BV Residence Les Peupliers / Résidence Les Peupliers",
        "recipient_email": "residencelespeuplierssprl@hotmail.com",
        "recipient_postal": "Avenue de la Motte Baraffe 6, 7180 Seneffe",
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
                f"tick{TICK} leftover Les Peupliers {KBO} Medium CW (bruto JUMP 3.17m pnl LOSS -296k "
                f"equity NEG -778k FTE 51.1 omzet empty; assets/debt Unknown; 1 VE MRS); "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2140; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Residence Les Peupliers Seneffe (bruto JUMP 3.17m / equity NEG -778k / Medium)

- Unit: **{RQ}** leftover dual after **rq_2134 MRS Comte d'Egmont**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (glossy jaarverslag 2025 online but CW/NBB last balance **2024**); AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Residence Les Peupliers BV** YE2025 (KBO **{KBO}**; Avenue de la Motte Baraffe 6 Seneffe; **BV/SRL** NACE **87.301** / **1 VE**; private MRS). Do not redo Comte d'Egmont/CIGB Menen/Ten Rozen/L'Orchidée/Care-Support/Restel Flats/De Fakkel. Deferred live YE2025: Residence Prestige / l'Esplanade Ath.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY} vs YE2024 EUR{BRUTO_PRIOR}; pnl **EUR{PNL}** LOSS NARROW {PNL_YOY} vs YE2024 EUR{PNL_PRIOR}; equity **EUR{EQUITY}** NEG DEEPEN {EQUITY_YOY} vs YE2024 EUR{EQUITY_PRIOR}; FTE **{FTE}** vs {FTE_PRIOR}; neerlegging **13.08.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via residencelespeuplierssprl@hotmail.com.
- Wrote: sources (+5); budgets (+4); commitments (+1); leaderboard (+1 pi 6.3); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2135/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2130**; next **2140**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Prestige-Esplanade / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "bruto", BRUTO, "equity", EQUITY, "pnl", PNL)
