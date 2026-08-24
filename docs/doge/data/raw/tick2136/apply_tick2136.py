# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T15:20:00Z"
TICK = 2136
RQ = "rq_2136"
NEXT_RQ = "rq_2137"
ENTITY = "asbl_lesplanade_ath"
GAP = "gap_esplanade_ath_nbb_pdf_assets_debt_pnl_loss_flip_merger_corolles_matrix_l5"
COMM = "comm_esplanade_ath_jr2025_statutory_mrs_merger"
LB = "lb_esplanade_ath_omzet_7_17m_pnl_loss_flip_merger_corolles_jr2025"
SRC_EN = "src_esplanade_ath_jr2025_cw_en"
KBO = "0409.232.013"
KBO_DIGITS = "0409232013"
COROLLES_KBO = "0440.737.514"
OMZET = "7174459"
OMZET_PRIOR = "7093531"
OMZET_YOY = "+1.14%"
BRUTO = "7656217"
BRUTO_PRIOR = "7344326"
BRUTO_YOY = "+4.25%"
PNL = "-26620"
PNL_PRIOR = "23701"
PNL_YOY = "-212.31%"
EQUITY = "5124859"
EQUITY_PRIOR = "5225488"
EQUITY_YOY = "-1.93%"
FTE = "108.3"
FTE_PRIOR = "110.4"
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
                "leftover dual — l'Esplanade Ath YE2025 Medium "
                "(pnl LOSS flip / Stopgezet fusie Les Corolles)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Esplanade Medium omzet JUMP 7.17m bruto JUMP 7.66m "
                f"pnl LOSS FLIP -27k equity DROP 5.12m FTE 108.3; KBO Stopgezet 31.03.2026 "
                f"fusie→Les Corolles {COROLLES_KBO}; FOI ready; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2140"
            )
            r["instructions"] = (
                f"Completed leftover l'Esplanade Ath YE2025 Medium CW after Les Peupliers; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 confirmed / AIESH/REW YE2024; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Stopgezet fusie→{COROLLES_KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl LOSS FLIP {PNL} equity DROP {EQUITY} "
                f"FTE {FTE}; FOI {GAP}"
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
                    "leftover dual hole-fill after l'Esplanade Ath — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/Les Corolles/Prestige/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after l'Esplanade Ath YE2025 Medium (Stopgezet fusie Les Corolles). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    f"else unused Les Corolles ASBL {COROLLES_KBO} YE2025 (overnemer Ath+La Moisson), else Residence Prestige "
                    "Chaudfontaine 0416.528.391 YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/"
                    "creche/disability/thuiszorg. Do NOT redo l'Esplanade Ath, Residence Les Peupliers Seneffe, "
                    "MRS Comte d'Egmont / Residence Comte d'Egmont Chièvres, C.I.G.B. Menen / PC Menen / Huize Ter Walle, "
                    "Maagd Der Armen / Ten Rozen Aalst, L'Orchidée Ittre, Care-Support, MPC Sint-Franciscus, "
                    "Zorghome De Fakkel, Restel Flats, Le Château Vert, SLG Wallonie, Famifamenne, Residence Le Castel, "
                    "R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, Le Bosquet, Strebo, Entraide, La Charmille, "
                    "Charmilles, Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, "
                    "Sint-Camillus, IDELUX*, INTRADEL, Korian*, SLG Operaties VL, SLG Vlaanderen VZW, Always Home, AREWAL, "
                    "AGB Bornem, Armonea holding, emeis holding, Maria's Rustoord Moorslede, Heilig Hart Grimbergen, "
                    "Veilige Have, Molenheide, Huize Sint-Jozef Ieper, PC Gent-Sleidinge, PC Sint-Hiëronymus."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Esplanade Ath fusie→Les Corolles; "
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
        "source_id": "src_esplanade_ath_jr2025_cw",
        "title": "Companyweb NL l'Esplanade Ath YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/l-esplanade",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl LOSS FLIP {PNL} ({PNL_YOY}) equity DROP {EQUITY} ({EQUITY_YOY}) FTE {FTE}; "
            f"neerlegging 02.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2136/esplanade_cw_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN l'Esplanade Ath YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/l-esplanade",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 02-07-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss LOSS FLIP {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; Principal activity nursing homes MRPA; raw docs/doge/data/raw/tick2136/esplanade_cw_en.html"
        ),
    },
    {
        "source_id": "src_esplanade_ath_jr2025_cw_fr",
        "title": "Companyweb FR l'Esplanade Ath YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/l-esplanade",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2136/esplanade_cw_fr.html",
    },
    {
        "source_id": f"src_esplanade_ath_kbo_{TICK}",
        "title": f"KBO l'Esplanade {KBO} Stopgezet fusie→Les Corolles",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Stopgezet sinds 31.03.2026; Fusie door overneming; "
            f"opgeslorpt door Les Corolles {COROLLES_KBO}; pre-stop VZW/ASBL Rue Jean Jaurès 7 7800 Ath; "
            "1 VE; NACE BTW 87.101 RVT / RSZ 87.301 ROB; 8 functiehouders"
        ),
    },
    {
        "source_id": f"src_esplanade_ath_site_{TICK}",
        "title": "l'Esplanade Ath site FOI info@esplanade-ath.be",
        "url": "https://www.esplanade-ath.be/",
        "publisher": "ASBL l'Esplanade",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Rue Jean Jaurès 7 7800 Ath; FOI info@esplanade-ath.be; "
            f"merger successor Les Corolles {COROLLES_KBO} Tournai"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "l'Esplanade Ath (MRS/RVT — Stopgezet fusie Les Corolles)",
        "name_fr": "l'Esplanade Ath (MRS/MRPA — Stoppée fusion Les Corolles)",
        "name_en": "l'Esplanade Ath (nursing home — stopped / merged into Les Corolles)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.esplanade-ath.be/",
        "foi_email": "info@esplanade-ath.be",
        "foi_postal": "Rue Jean Jaurès 7, 7800 Ath (cc Les Corolles, Chaussée de Renaix 192, 7500 Tournai)",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Stopgezet 31.03.2026 "
            f"Fusie door overneming→Les Corolles {COROLLES_KBO}; omzet JUMP 7.17m ({OMZET_YOY}) "
            f"bruto JUMP 7.66m ({BRUTO_YOY}) pnl LOSS FLIP -27k ({PNL_YOY}) equity DROP 5.12m "
            f"({EQUITY_YOY}) FTE {FTE}; assets/debt Unknown; filed 02.07.2026; FOI {GAP}; "
            "preferred AGB Bornem JR2024; FARO confirmed YE2024; AIESH/REW YE2024; "
            "DISTINCT Les Peupliers / Comte d'Egmont / CIGB Menen / Ten Rozen / L'Orchidée / Prestige"
        ),
    },
)

for bid, amt, basis in [
    ("bud_esplanade_ath_omzet_jr2025_statutory", OMZET, "CW YE2025 Omzet / Turnover"),
    ("bud_esplanade_ath_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin"),
    ("bud_esplanade_ath_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss LOSS FLIP"),
    ("bud_esplanade_ath_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
    ("bud_esplanade_ath_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
                "tick2136; Medium CW; assets/debt Unknown pending NBB PDF; "
                f"entity Stopgezet 31.03.2026 fusie→Les Corolles {COROLLES_KBO}"
            ),
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "l'Esplanade Ath YE2025 leftover dual (omzet 7.17m / pnl loss flip / fusie Les Corolles)",
        "entity_id": ENTITY,
        "beneficiary": "MRS residents Ath (Hainaut / Wallonie) → Les Corolles group",
        "legal_basis": (
            f"ASBL maison de repos MRPA/RVT (KBO {KBO}; Stopgezet fusie→{COROLLES_KBO} 31.03.2026)"
        ),
        "decision_date": "2026-07-02",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET_PRIOR},'
            f'"2024_bruto":{BRUTO_PRIOR},"2024_pnl":{PNL_PRIOR},"2024_equity":{EQUITY_PRIOR},'
            f'"2024_fte":{FTE_PRIOR},"stop_fusie":"2026-03-31","overnemer":"{COROLLES_KBO}"}}'
        ),
        "remaining_eur": "0",
        "status": "ended",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/l-esplanade",
        "stated_goal": "Nursing home / maison de repos et de soins for elderly (MRPA/RVT)",
        "cut_option": (
            "Publish NBB PDF assets/debt; disclose AViQ/INAMI vs resident-fee split; "
            "publish fusie dossier Les Corolles (BS + overgenomen activa/schulden + bedden)"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>Ath>Esplanade>JR2025_statutory_L5_fusie_Corolles",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO YE2024 confirmed; AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT Les Peupliers / Comte d'Egmont / CIGB Menen / Ten Rozen / L'Orchidée / Prestige"
        ),
    },
)

# pi ≈ 0.55*7.0 + 0.35*5.2 + 0.10*(11-3.0) = 3.85+1.82+0.80 = 6.47 → 6.5
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": (
            "l'Esplanade Ath omzet 7.17m / pnl LOSS flip -27k / Stopgezet fusie Les Corolles (YE2025)"
        ),
        "level": "L5",
        "type": "mrs_asbl",
        "hierarchy_path": "Wallonie>Hainaut>Ath>Esplanade>JR2025_fusie_Corolles",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY}; bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} LOSS FLIP {PNL_YOY} vs prior profit {PNL_PRIOR}; equity {EQUITY} DROP {EQUITY_YOY}; "
            f"FTE {FTE}; assets/debt Unknown pending NBB PDF; KBO Stopgezet 31.03.2026 "
            f"fusie→Les Corolles {COROLLES_KBO} (also La Moisson)"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS residents Ath → Les Corolles",
        "stated_goal": "Nursing home / maison de repos et de soins for elderly",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl LOSS FLIP {PNL_YOY}; "
            f"equity DROP {EQUITY_YOY}; FTE {FTE_PRIOR}→{FTE}; entity Stopgezet fusie 31.03.2026"
        ),
        "absurdity_score": "7.0",
        "cost_score": "5.2",
        "difficulty": "3.0",
        "priority_index": "6.5",
        "cut_proposal": (
            "FOI NBB PDF + AViQ/INAMI split + fusie dossier Les Corolles (assets/debt/bedden transfer)"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; FARO confirmed YE2024; AIESH/REW YE2024; "
            "DISTINCT Les Peupliers / Comte d'Egmont / CIGB Menen / Ten Rozen / L'Orchidée / Prestige"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Hainaut>Ath>Esplanade>NBB_PDF_assets_debt_pnl_loss_flip_merger_Corolles"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); AViQ/INAMI care vs resident fee split; "
            "pnl LOSS FLIP -27k path; fusie door overneming 31.03.2026 dossier (BS/akte, overgenomen "
            f"activa/schulden, bedden Ath→Les Corolles {COROLLES_KBO} + La Moisson parallel)"
        ),
        "why_it_matters": (
            "Medium CW shows Ath MRS ASBL with omzet 7.17m flipping to LOSS then Stopgezet via absorption "
            "into Les Corolles — public-care / merger transparency gap while assets/debt opaque"
        ),
        "priority": "8",
        "recipient_body": "ASBL l'Esplanade (ex) / Les Corolles ASBL (overnemer)",
        "recipient_email": "info@esplanade-ath.be",
        "recipient_postal": (
            "Rue Jean Jaurès 7, 7800 Ath (cc Les Corolles, Chaussée de Renaix 192, 7500 Tournai)"
        ),
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
                f"tick{TICK} leftover l'Esplanade Ath {KBO} Medium CW (omzet JUMP 7.17m bruto JUMP 7.66m "
                f"pnl LOSS FLIP -27k equity DROP 5.12m FTE 108.3; Stopgezet 31.03.2026 fusie→Les Corolles "
                f"{COROLLES_KBO}; assets/debt Unknown; 1 VE); AGB Bornem JR2024; FARO YE2024 confirmed; "
                f"AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2140; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} l'Esplanade Ath (omzet JUMP 7.17m / pnl LOSS flip / fusie Les Corolles / Medium)

- Unit: **{RQ}** leftover dual after **rq_2135 Residence Les Peupliers**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO confirmed still **YE2024** (CW last balance 2024); AIESH still **YE2024**; REW still **YE2024**. Took deferred unused leftover **l'Esplanade ASBL Ath** YE2025 (KBO **{KBO}**; Rue Jean Jaurès 7 Ath; **VZW/ASBL** NACE **87.101/87.301** / **1 VE**; Stopgezet **31.03.2026** Fusie door overneming → **Les Corolles {COROLLES_KBO}**). Do not redo Les Peupliers/Comte d'Egmont/CIGB Menen/Ten Rozen/L'Orchidée/Care-Support/Restel Flats/De Fakkel. Deferred live YE2025: Residence Prestige Chaudfontaine + Les Corolles (overnemer).
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY} vs YE2024 EUR{OMZET_PRIOR}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** LOSS FLIP {PNL_YOY} vs YE2024 EUR{PNL_PRIOR}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; FTE **{FTE}** vs {FTE_PRIOR}; neerlegging **02.07.2026**. KBO Strong Stopgezet + fusie (also La Moisson absorbed). Assets/debt Unknown. Medium. FOI via info@esplanade-ath.be (cc Les Corolles).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.5); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2136/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2130**; next **2140**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Les Corolles / Prestige / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "omzet", OMZET, "pnl", PNL, "equity", EQUITY)
