# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T16:00:00Z"
TICK = 2138
RQ = "rq_2138"
NEXT_RQ = "rq_2139"
ENTITY = "sc_residence_prestige_chaudfontaine"
GAP = "gap_prestige_chaudfontaine_nbb_pdf_assets_debt_omzet_empty_pnl_profit_flip_thin_equity_matrix_l5"
COMM = "comm_prestige_chaudfontaine_jr2025_statutory_mrs_cv"
LB = "lb_prestige_chaudfontaine_bruto_3_70m_pnl_profit_flip_thin_equity_jr2025"
SRC_EN = "src_prestige_chaudfontaine_jr2025_cw_en"
KBO = "0416.528.391"
KBO_DIGITS = "0416528391"
OMZET = ""  # unpublished
BRUTO = "3700707"
BRUTO_PRIOR = "3142656"
BRUTO_YOY = "+17.76%"
PNL = "57786"
PNL_PRIOR = "-189310"
PNL_YOY = "+130.52%"  # improve vs abs prior loss; PROFIT FLIP
EQUITY = "277599"
EQUITY_PRIOR = "219813"
EQUITY_YOY = "+26.29%"
FTE = "60.6"
FTE_PRIOR = ""  # Unknown
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
                "leftover dual — Residence Prestige Chaudfontaine YE2025 Medium "
                "(bruto JUMP 3.70m / pnl PROFIT flip / thin equity)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Prestige Medium bruto JUMP 3.70m ({BRUTO_YOY}) "
                f"pnl PROFIT FLIP 58k ({PNL_YOY} vs YE2024 LOSS) equity JUMP 0.28m thin "
                f"({EQUITY_YOY}) FTE {FTE}; omzet unpublished; KBO Actief CV 1 VE; FOI ready; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2140"
            )
            r["instructions"] = (
                f"Completed leftover Residence Prestige YE2025 Medium CW after Les Corolles; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet unpublished bruto JUMP {BRUTO} pnl PROFIT FLIP {PNL} equity JUMP {EQUITY} "
                f"thin FTE {FTE}; FOI {GAP}"
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
                    "leftover dual hole-fill after Residence Prestige — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Residence Prestige Chaudfontaine YE2025 Medium "
                    "(bruto JUMP / pnl PROFIT flip / thin equity). Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/"
                    "energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. Do NOT redo Residence Prestige "
                    "Chaudfontaine, Les Corolles Tournai, l'Esplanade Ath, Residence Les Peupliers Seneffe, "
                    "MRS Comte d'Egmont / Residence Comte d'Egmont Chièvres, C.I.G.B. Menen / PC Menen / "
                    "Huize Ter Walle, Maagd Der Armen / Ten Rozen Aalst, L'Orchidée Ittre, Care-Support, "
                    "MPC Sint-Franciscus, Zorghome De Fakkel, Restel Flats, Le Château Vert, SLG Wallonie, "
                    "Famifamenne, Residence Le Castel, R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, "
                    "Le Bosquet, Strebo, Entraide, La Charmille, Charmilles, Sittelles, Les Buissons, "
                    "Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, Sint-Camillus, IDELUX*, "
                    "INTRADEL, Korian*, SLG Operaties VL, SLG Vlaanderen VZW, Always Home, AREWAL, AGB Bornem, "
                    "Armonea holding, emeis holding, Maria's Rustoord Moorslede, Heilig Hart Grimbergen, "
                    "Veilige Have, Molenheide, Huize Sint-Jozef Ieper, PC Gent-Sleidinge, PC Sint-Hiëronymus, "
                    "La Moisson (absorbed)."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Residence Prestige; "
                    "FARO/AIESH/REW still YE2024; next every-10 2140"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_prestige_chaudfontaine_jr2025_cw",
        "title": "Companyweb NL Residence Prestige Chaudfontaine YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/residence-prestige",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet unpublished bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl PROFIT FLIP {PNL} ({PNL_YOY} vs YE2024 LOSS {PNL_PRIOR}) equity JUMP {EQUITY} "
            f"({EQUITY_YOY}) thin FTE {FTE}; neerlegging 04.08.2026; assets/debt Unknown; "
            "raw docs/doge/data/raw/tick2138/prestige_cw_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Residence Prestige Chaudfontaine YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/residence-prestige",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 04-08-2026; Last balance sheet year 2025; "
            f"Turnover unpublished; Gross margin {BRUTO}; Profit/Loss PROFIT FLIP {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; Principal activity nursing homes; raw docs/doge/data/raw/tick2138/prestige_cw_en.html"
        ),
    },
    {
        "source_id": "src_prestige_chaudfontaine_jr2025_cw_fr",
        "title": "Companyweb FR Residence Prestige Chaudfontaine YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/residence-prestige",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2138/prestige_cw_fr.html",
    },
    {
        "source_id": f"src_prestige_chaudfontaine_kbo_{TICK}",
        "title": f"KBO Residence Prestige {KBO} Actief CV Chaudfontaine",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; Coöperatieve vennootschap; Voie de Liège 150 4053 Chaudfontaine; "
            "1 VE; NACE 87.301 ROB; sinds 01.10.1976; 9 functiehouders"
        ),
    },
    {
        "source_id": f"src_prestige_chaudfontaine_commune_{TICK}",
        "title": "Commune Chaudfontaine MRS list — Residence Prestige FOI contact",
        "url": "https://www.chaudfontaine.be/mes-services/senior/maisons-de-repos-residences/",
        "publisher": "Commune de Chaudfontaine",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; lists Résidence Prestige Voie de Liège 150; tel 04.361.52.69; "
            "email info@residence-prestige.be; site www.residence-prestige.be"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Residence Prestige Chaudfontaine (MRS/ROB — CV)",
        "name_fr": "Résidence Prestige Chaudfontaine (MRS/MRPA — SC)",
        "name_en": "Residence Prestige Chaudfontaine (nursing home — cooperative)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.residence-prestige.be/",
        "foi_email": "info@residence-prestige.be",
        "foi_postal": "Voie de Liège 150, 4053 Chaudfontaine",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief CV; "
            f"omzet unpublished bruto JUMP 3.70m ({BRUTO_YOY}) pnl PROFIT FLIP 58k "
            f"({PNL_YOY} vs YE2024 LOSS) equity JUMP 0.28m thin ({EQUITY_YOY}) FTE {FTE}; "
            f"assets/debt Unknown; filed 04.08.2026; 1 VE NACE 87.301; FOI {GAP}; "
            "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "DISTINCT Les Corolles / Esplanade / Peupliers / Comte d'Egmont / CIGB Menen"
        ),
    },
)

for bid, amt, basis in [
    ("bud_prestige_chaudfontaine_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin (primary; omzet unpublished)"),
    ("bud_prestige_chaudfontaine_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss PROFIT FLIP"),
    ("bud_prestige_chaudfontaine_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity thin"),
    ("bud_prestige_chaudfontaine_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
                "tick2138; Medium CW; omzet unpublished; assets/debt Unknown pending NBB PDF"
            ),
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Residence Prestige Chaudfontaine YE2025 leftover dual (bruto 3.70m / pnl profit flip / thin equity)",
        "entity_id": ENTITY,
        "beneficiary": "MRS residents Chaudfontaine (Liège / Wallonie)",
        "legal_basis": f"CV/SC maison de repos MRPA/ROB (KBO {KBO})",
        "decision_date": "2026-08-04",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": BRUTO,
        "cash_by_year": (
            f'{{"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},'
            f'"2024_bruto":{BRUTO_PRIOR},"2024_pnl":{PNL_PRIOR},"2024_equity":{EQUITY_PRIOR},'
            f'"2025_omzet":"unpublished"}}'
        ),
        "remaining_eur": "0",
        "status": "ended",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/residence-prestige",
        "stated_goal": "Nursing home / maison de repos et de soins for elderly (MRPA/ROB)",
        "cut_option": (
            "Publish NBB PDF assets/debt + omzet code 70; disclose AViQ/INAMI vs resident-fee split; "
            "explain profit flip vs thin equity path"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Liege>Chaudfontaine>ResidencePrestige>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope (omzet unpublished); assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT Les Corolles / Esplanade / Peupliers / Comte d'Egmont / CIGB Menen"
        ),
    },
)

# pi ≈ 0.55*5.8 + 0.35*5.1 + 0.10*(11-3.0) = 3.19+1.785+0.80 = 5.775 → 5.8
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": (
            "Residence Prestige Chaudfontaine bruto 3.70m / pnl PROFIT flip / thin equity 0.28m (YE2025)"
        ),
        "level": "L5",
        "type": "mrs_cv",
        "hierarchy_path": "Wallonie>Liege>Chaudfontaine>ResidencePrestige>JR2025",
        "annual_cost_eur": BRUTO,
        "total_cost_eur": BRUTO,
        "tco_notes": (
            f"CW YE2025 omzet unpublished; bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} PROFIT FLIP {PNL_YOY} vs prior LOSS {PNL_PRIOR}; equity {EQUITY} JUMP {EQUITY_YOY} "
            f"thin (~7.5pct bruto); FTE {FTE}; assets/debt Unknown pending NBB PDF"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS residents Chaudfontaine",
        "stated_goal": "Nursing home / maison de repos et de soins for elderly",
        "measured_outcome": (
            f"bruto JUMP {BRUTO_YOY}; pnl PROFIT FLIP {PNL_YOY}; equity JUMP {EQUITY_YOY} thin; "
            f"omzet unpublished; FTE {FTE}"
        ),
        "absurdity_score": "5.8",
        "cost_score": "5.1",
        "difficulty": "3.0",
        "priority_index": "5.8",
        "cut_proposal": (
            "FOI NBB PDF + omzet disclosure + AViQ/INAMI split + thin-equity / profit-flip path"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT Les Corolles / Esplanade / Peupliers / Comte d'Egmont / CIGB Menen"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Liege>Chaudfontaine>ResidencePrestige>NBB_PDF_assets_debt_omzet_empty_pnl_profit_flip_thin_equity"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); omzet code 70 if withheld; "
            "AViQ/INAMI care vs resident fee split vs bruto 3.70m; pnl PROFIT FLIP path vs YE2024 LOSS; "
            "thin equity 0.28m continuity note"
        ),
        "why_it_matters": (
            "Medium CW shows private MRS cooperative with unpublished omzet, bruto JUMP to 3.70m, "
            "profit flip from deep loss, thin equity — public-care opacity while assets/debt unknown"
        ),
        "priority": "8",
        "recipient_body": "Residence Prestige SC",
        "recipient_email": "info@residence-prestige.be",
        "recipient_postal": "Voie de Liège 150, 4053 Chaudfontaine",
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
                f"tick{TICK} leftover Residence Prestige {KBO} Medium CW (omzet unpublished bruto JUMP 3.70m "
                f"pnl PROFIT FLIP 58k equity JUMP thin 0.28m FTE {FTE}; Actief CV 1 VE; assets/debt Unknown); "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2140; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Residence Prestige Chaudfontaine (bruto JUMP 3.70m / pnl PROFIT flip / thin equity / Medium)

- Unit: **{RQ}** race-recover after concurrent took **rq_2137 Les Corolles**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took deferred unused leftover **Residence Prestige SC** YE2025 (KBO **{KBO}**; Voie de Liège 150 Chaudfontaine; **CV/SC** NACE **87.301** / **1 VE**; private MRS coop). Do not redo Les Corolles/l'Esplanade/Les Peupliers/Comte d'Egmont/CIGB Menen/Ten Rozen/L'Orchidée/Care-Support/Restel Flats/De Fakkel.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY} vs YE2024 EUR{BRUTO_PRIOR}; pnl **EUR{PNL}** PROFIT FLIP {PNL_YOY} vs YE2024 LOSS EUR{PNL_PRIOR}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY} thin (~7.5pct bruto); FTE **{FTE}**; neerlegging **04.08.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info@residence-prestige.be (commune listing).
- Wrote: sources (+5); budgets (+4); commitments (+1); leaderboard (+1 pi 5.8); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2138/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2130**; next **2140**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "bruto", BRUTO, "pnl", PNL, "equity", EQUITY)
