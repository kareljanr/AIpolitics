# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T15:40:00Z"
TICK = 2137
RQ = "rq_2137"
NEXT_RQ = "rq_2138"
ENTITY = "asbl_les_corolles_tournai"
GAP = "gap_les_corolles_nbb_pdf_assets_debt_merger_absorption_esplanade_moisson_matrix_l5"
COMM = "comm_les_corolles_jr2025_statutory_mrs_merger_overnemer"
LB = "lb_les_corolles_omzet_9_74m_pnl_jump_merger_overnemer_jr2025"
SRC_EN = "src_les_corolles_jr2025_cw_en"
KBO = "0440.737.514"
KBO_DIGITS = "0440737514"
ESPLANADE_KBO = "0409.232.013"
MOISSON_KBO = "0434.384.014"
OMZET = "9741365"
OMZET_PRIOR = "9385583"
OMZET_YOY = "+3.79%"
BRUTO = "10263326"
BRUTO_PRIOR = "9813565"
BRUTO_YOY = "+4.58%"
PNL = "467552"
PNL_PRIOR = "424611"
PNL_YOY = "+10.11%"
EQUITY = "9934798"
EQUITY_PRIOR = "9613283"
EQUITY_YOY = "+3.34%"
FTE = "140.4"
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
                "leftover dual — Les Corolles Tournai YE2025 Medium "
                "(omzet JUMP 9.74m / merger overnemer Esplanade+Moisson)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Les Corolles Medium omzet JUMP 9.74m bruto JUMP 10.26m "
                f"pnl JUMP 0.47m equity JUMP 9.93m FTE 140.4; KBO Actief 5 VE; "
                f"overnemer Esplanade {ESPLANADE_KBO}+La Moisson {MOISSON_KBO} 31.03.2026; "
                f"FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; "
                "next every-10 2140"
            )
            r["instructions"] = (
                f"Completed leftover Les Corolles YE2025 Medium CW after l'Esplanade Ath; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} "
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
                    "leftover dual hole-fill after Les Corolles — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/Prestige/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Les Corolles YE2025 Medium (overnemer Esplanade+Moisson). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused Residence Prestige Chaudfontaine 0416.528.391 YE2025, else unused "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. "
                    "Do NOT redo Les Corolles Tournai, l'Esplanade Ath, Residence Les Peupliers Seneffe, "
                    "MRS Comte d'Egmont / Residence Comte d'Egmont Chièvres, C.I.G.B. Menen / PC Menen / Huize Ter Walle, "
                    "Maagd Der Armen / Ten Rozen Aalst, L'Orchidée Ittre, Care-Support, MPC Sint-Franciscus, "
                    "Zorghome De Fakkel, Restel Flats, Le Château Vert, SLG Wallonie, Famifamenne, Residence Le Castel, "
                    "R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, Le Bosquet, Strebo, Entraide, La Charmille, "
                    "Charmilles, Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, "
                    "Sint-Camillus, IDELUX*, INTRADEL, Korian*, SLG Operaties VL, SLG Vlaanderen VZW, Always Home, AREWAL, "
                    "AGB Bornem, Armonea holding, emeis holding, Maria's Rustoord Moorslede, Heilig Hart Grimbergen, "
                    "Veilige Have, Molenheide, Huize Sint-Jozef Ieper, PC Gent-Sleidinge, PC Sint-Hiëronymus, "
                    "La Moisson (absorbed), IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, "
                    "Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, "
                    "Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Les Corolles overnemer; "
                    "FARO/AIESH/REW still YE2024; Prestige Chaudfontaine deferred YE2025; next every-10 2140"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_les_corolles_jr2025_cw",
        "title": "Companyweb NL Les Corolles YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/les-corolles",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl JUMP {PNL} ({PNL_YOY}) equity JUMP {EQUITY} ({EQUITY_YOY}) FTE {FTE}; "
            f"neerlegging 07.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2137/corolles_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Les Corolles YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/les-corolles",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 07-07-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss JUMP {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; companySize Big; Principal activity nursing homes ROB; "
            f"raw docs/doge/data/raw/tick2137/corolles_en.html"
        ),
    },
    {
        "source_id": "src_les_corolles_jr2025_cw_fr",
        "title": "Companyweb FR Les Corolles YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/les-corolles",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2137/corolles_fr.html",
    },
    {
        "source_id": f"src_les_corolles_kbo_{TICK}",
        "title": f"KBO Les Corolles {KBO} Actief overnemer Esplanade+Moisson",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; Normale toestand; ASBL LES COROLLES; "
            "Chaussée de Renaix(TOU) 192 7500 Tournai; 5 VE; NACE BTW/RSZ 87.301 ROB; "
            f"start 23.06.1989; web www.lavertefeuille.be; email info@vertefeuille.be; "
            f"absorbed Esplanade {ESPLANADE_KBO} + La Moisson {MOISSON_KBO} sinds 31.03.2026; "
            "20 functiehouders"
        ),
    },
    {
        "source_id": f"src_les_corolles_site_{TICK}",
        "title": "Les Corolles / La Verte Feuille site FOI info@vertefeuille.be",
        "url": "https://www.lavertefeuille.be/",
        "publisher": "ASBL Les Corolles / Groupe La Verte Feuille",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Chaussée de Renaix 192 7500 Tournai; FOI info@vertefeuille.be; "
            f"overnemer of Esplanade {ESPLANADE_KBO} + La Moisson {MOISSON_KBO}"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Les Corolles Tournai (MRS/ROB — overnemer Esplanade+Moisson)",
        "name_fr": "Les Corolles Tournai (MRS/MRPA — absorbeur Esplanade+Moisson)",
        "name_en": "Les Corolles Tournai (nursing home — absorber of Esplanade+Moisson)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.lavertefeuille.be/",
        "foi_email": "info@vertefeuille.be",
        "foi_postal": "Chaussée de Renaix 192, 7500 Tournai",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief; "
            f"omzet JUMP 9.74m ({OMZET_YOY}) bruto JUMP 10.26m ({BRUTO_YOY}) "
            f"pnl JUMP 0.47m ({PNL_YOY}) equity JUMP 9.93m ({EQUITY_YOY}) FTE {FTE}; "
            f"assets/debt Unknown; filed 07.07.2026; 5 VE NACE 87.301; "
            f"overnemer Esplanade {ESPLANADE_KBO}+La Moisson {MOISSON_KBO} 31.03.2026; "
            f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "DISTINCT Prestige Chaudfontaine deferred; La Moisson absorbed not separately mined"
        ),
    },
)

for bid, amt, basis in [
    ("bud_les_corolles_omzet_jr2025_statutory", OMZET, "CW YE2025 Omzet / Turnover"),
    ("bud_les_corolles_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin"),
    ("bud_les_corolles_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss JUMP"),
    ("bud_les_corolles_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
    ("bud_les_corolles_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
                "tick2137; Medium CW; assets/debt Unknown pending NBB PDF; "
                f"overnemer Esplanade {ESPLANADE_KBO}+La Moisson {MOISSON_KBO} 31.03.2026"
            ),
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": (
            "Les Corolles YE2025 leftover dual (omzet JUMP 9.74m / merger overnemer Esplanade+Moisson)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "MRS residents Tournai group (Hainaut / Wallonie) incl. absorbed Ath/Moisson sites",
        "legal_basis": (
            f"ASBL maison de repos ROB (KBO {KBO}; Actief; overnemer {ESPLANADE_KBO}+{MOISSON_KBO} 31.03.2026)"
        ),
        "decision_date": "2026-07-07",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET_PRIOR},'
            f'"2024_bruto":{BRUTO_PRIOR},"2024_pnl":{PNL_PRIOR},"2024_equity":{EQUITY_PRIOR},'
            f'"ve":5,"fusie_date":"2026-03-31","absorbed":["{ESPLANADE_KBO}","{MOISSON_KBO}"]}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/les-corolles",
        "stated_goal": "Nursing home / maison de repos for elderly (ROB) — group La Verte Feuille",
        "cut_option": (
            "Publish NBB PDF assets/debt; disclose AViQ/INAMI vs resident-fee split; "
            "publish fusie dossier Esplanade+Moisson (BS + overgenomen activa/schulden + 5 VE bedden matrix)"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>Tournai>LesCorolles>JR2025_statutory_L5_overnemer",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT Prestige deferred; YE2025 pre-dates 31.03.2026 absorption (capacity jump post-YE)"
        ),
    },
)

# pi ≈ 0.55*6.2 + 0.35*5.6 + 0.10*(11-3.0) = 3.41+1.96+0.80 = 6.17 → 6.2
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": (
            "Les Corolles omzet JUMP 9.74m / pnl JUMP +10% / merger overnemer Esplanade+Moisson (YE2025)"
        ),
        "level": "L5",
        "type": "mrs_asbl",
        "hierarchy_path": "Wallonie>Hainaut>Tournai>LesCorolles>JR2025_overnemer",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY}; bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} JUMP {PNL_YOY}; equity {EQUITY} JUMP {EQUITY_YOY}; FTE {FTE}; "
            f"assets/debt Unknown pending NBB PDF; KBO Actief 5 VE; overnemer "
            f"Esplanade {ESPLANADE_KBO}+La Moisson {MOISSON_KBO} 31.03.2026"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS residents Tournai group (+ absorbed Ath/Moisson)",
        "stated_goal": "Nursing home / maison de repos for elderly (ROB)",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl JUMP {PNL_YOY}; "
            f"equity JUMP {EQUITY_YOY}; FTE {FTE}; Actief overnemer 31.03.2026"
        ),
        "absurdity_score": "6.2",
        "cost_score": "5.6",
        "difficulty": "3.0",
        "priority_index": "6.2",
        "cut_proposal": (
            "FOI NBB PDF + AViQ/INAMI split + fusie dossier Esplanade+Moisson (assets/debt/5 VE bedden)"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT Prestige deferred; YE2025 figures pre-absorption"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Hainaut>Tournai>LesCorolles>NBB_PDF_assets_debt_merger_Esplanade_Moisson"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); AViQ/INAMI care vs resident fee split; "
            "fusie door overneming 31.03.2026 dossier (BS/akte, overgenomen activa/schulden, bedden) for "
            f"Esplanade {ESPLANADE_KBO} + La Moisson {MOISSON_KBO}; 5 VE matrix post-fusie"
        ),
        "why_it_matters": (
            "Medium CW shows Tournai MRS ASBL with omzet 9.74m profitable JUMP while absorbing two MRS "
            "(Esplanade+Moisson) — public-care / merger transparency gap while assets/debt opaque"
        ),
        "priority": "8",
        "recipient_body": "ASBL Les Corolles / Groupe La Verte Feuille",
        "recipient_email": "info@vertefeuille.be",
        "recipient_postal": "Chaussée de Renaix 192, 7500 Tournai",
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
                f"tick{TICK} leftover Les Corolles {KBO} Medium CW (omzet JUMP 9.74m bruto JUMP 10.26m "
                f"pnl JUMP 0.47m equity JUMP 9.93m FTE 140.4; Actief 5 VE; overnemer Esplanade "
                f"{ESPLANADE_KBO}+La Moisson {MOISSON_KBO} 31.03.2026; assets/debt Unknown); "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; Prestige deferred; next {NEXT_RQ}; "
                "next every-10 2140; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Les Corolles Tournai (omzet JUMP 9.74m / pnl JUMP +10% / overnemer Esplanade+Moisson / Medium)

- Unit: **{RQ}** leftover dual after **rq_2136 l'Esplanade Ath**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred unused leftover **Les Corolles ASBL Tournai** YE2025 (KBO **{KBO}**; Chaussée de Renaix 192 Tournai; **ASBL** NACE **87.301** / **5 VE**; Actief overnemer **Esplanade {ESPLANADE_KBO}** + **La Moisson {MOISSON_KBO}** sinds **31.03.2026**; Groupe La Verte Feuille). Do not redo Esplanade/Les Peupliers/Comte d'Egmont/CIGB Menen/Ten Rozen/L'Orchidée/Care-Support. Deferred live YE2025: Residence Prestige Chaudfontaine 0416.528.391.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY} vs YE2024 EUR{OMZET_PRIOR}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** JUMP {PNL_YOY}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}**; neerlegging **07.07.2026**. KBO Strong Actief + absorption links. Assets/debt Unknown. Medium. FOI via info@vertefeuille.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.2); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2137/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2130**; next **2140**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Prestige / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "omzet", OMZET, "pnl", PNL, "equity", EQUITY)
