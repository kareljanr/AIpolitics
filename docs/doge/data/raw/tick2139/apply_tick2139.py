# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T16:20:00Z"
TICK = 2139
RQ = "rq_2139"
NEXT_RQ = "rq_2140"
ENTITY = "srl_maison_de_repos_en_famille_vaux"
GAP = "gap_en_famille_vaux_nbb_pdf_assets_debt_omzet_empty_pnl_flip_loss_matrix_l5"
COMM = "comm_en_famille_vaux_jr2025_statutory_mrs_pnl_flip_loss"
LB = "lb_en_famille_vaux_bruto_jump_1_03m_pnl_flip_loss_jr2025"
SRC_EN = "src_en_famille_vaux_jr2025_cw_en"
KBO = "0466.114.791"
KBO_DIGITS = "0466114791"
BRUTO = "1033029"
BRUTO_PRIOR = "988068"
BRUTO_YOY = "+4.55%"
PNL = "-19390"
PNL_PRIOR = "9411"
PNL_YOY = "FLIP_LOSS"
EQUITY = "197533"
EQUITY_PRIOR = "216923"
EQUITY_YOY = "-8.94%"
FTE = "12.9"
FTE_PRIOR = "13.4"
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
                "leftover dual — Maison De Repos En Famille Vaux YE2025 Medium "
                "(bruto JUMP 1.03m / pnl FLIP LOSS)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} En Famille Medium bruto JUMP 1.03m pnl FLIP LOSS -19k "
                f"equity DROP 0.20m FTE 12.9 omzet empty; KBO Actief BV aanbestedende overheid "
                f"1 VE Salvacourt; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ} EVERY-10; next every-10 after that 2150"
            )
            r["instructions"] = (
                f"Completed leftover Maison De Repos En Famille YE2025 Medium CW after Prestige; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief; "
                f"bruto JUMP {BRUTO} pnl FLIP LOSS {PNL} equity DROP {EQUITY} FTE {FTE}; FOI {GAP}"
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
                    "EVERY-10 + leftover dual hole-fill after En Famille — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "9",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} EVERY-10 after Maison De Repos En Famille Vaux YE2025 Medium. "
                    "MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. "
                    "Do NOT redo Maison De Repos En Famille Vaux-sur-Sûre, Residence Prestige Chaudfontaine, "
                    "Les Corolles Tournai, l'Esplanade Ath, Residence Les Peupliers Seneffe, MRS Comte d'Egmont Chièvres, "
                    "C.I.G.B. Menen / PC Menen, Maagd Der Armen / Ten Rozen Aalst, L'Orchidée Ittre, Care-Support, "
                    "MPC Sint-Franciscus, Zorghome De Fakkel, Restel Flats, Le Château Vert, SLG Wallonie, Famifamenne, "
                    "Residence Le Castel, R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, Le Bosquet, Strebo, "
                    "Entraide, La Charmille, Always Home, AREWAL, AGB Bornem, Armonea holding, emeis holding, "
                    "La Moisson (absorbed), IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, "
                    "Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, "
                    "Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Seniors Care-Ion (YE2024-only)."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} En Famille; EVERY-10@2140 required; "
                    "FARO/AIESH/REW still YE2024; next every-10 after 2150"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_en_famille_vaux_jr2025_cw",
        "title": "Companyweb NL Maison De Repos En Famille YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/maison-de-repos-en-famille",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet unpublished bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl FLIP LOSS {PNL} (vs YE2024 {PNL_PRIOR}) equity DROP {EQUITY} ({EQUITY_YOY}) FTE {FTE}; "
            f"neerlegging 16.04.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2139/enfamille_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Maison De Repos En Famille YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/maison-de-repos-en-famille",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 16-04-2026; Last balance sheet year 2025; "
            f"Turnover unpublished; Gross margin {BRUTO}; Profit/Loss FLIP LOSS {PNL}; Equity {EQUITY}; "
            f"FTE {FTE}; Principal activity MRPA nursing homes; "
            f"raw docs/doge/data/raw/tick2139/enfamille_en.html"
        ),
    },
    {
        "source_id": "src_en_famille_vaux_jr2025_cw_fr",
        "title": "Companyweb FR Maison De Repos En Famille YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/maison-de-repos-en-famille",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2139/enfamille_fr.html",
    },
    {
        "source_id": f"src_en_famille_vaux_kbo_{TICK}",
        "title": f"KBO Maison De Repos En Famille {KBO} Actief Vaux-sur-Sûre",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; Normale toestand; BV/SRL MAISON DE REPOS EN FAMILLE; "
            "Salvacourt 11 6640 Vaux-sur-Sûre; 1 VE; NACE RSZ 87.301 ROB; "
            "aanbestedende overheid sinds 25.05.1999; start 27.05.1999; bestuurder Chavez Anne-Frédérique"
        ),
    },
    {
        "source_id": f"src_en_famille_vaux_site_{TICK}",
        "title": "Maison De Repos En Famille site FOI info@residenceenfamille.be",
        "url": "https://maisondereposenfamille.be/",
        "publisher": "Maison De Repos En Famille SRL",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Salvacourt 11 6640 Vaux-sur-Sûre; FOI info@residenceenfamille.be; "
            "tel 061 26 66 49; commercial name EN FAMILLE"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Maison De Repos En Famille (Vaux-sur-Sûre / Salvacourt)",
        "name_fr": "Maison De Repos En Famille (Vaux-sur-Sûre / Salvacourt)",
        "name_en": "Maison De Repos En Famille (Vaux-sur-Sûre nursing home)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://maisondereposenfamille.be/",
        "foi_email": "info@residenceenfamille.be",
        "foi_postal": "Salvacourt 11, 6640 Vaux-sur-Sûre",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief BV aanbestedende overheid; "
            f"omzet unpublished bruto JUMP 1.03m ({BRUTO_YOY}) pnl FLIP LOSS -19k "
            f"equity DROP 0.20m ({EQUITY_YOY}) FTE {FTE}; assets/debt Unknown; filed 16.04.2026; "
            f"1 VE NACE 87.301; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "DISTINCT Prestige / Corolles / Esplanade / Les Peupliers / Comte d'Egmont"
        ),
    },
)

for bid, amt, basis in [
    ("bud_en_famille_vaux_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin (omzet unpublished)"),
    ("bud_en_famille_vaux_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss FLIP LOSS"),
    ("bud_en_famille_vaux_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity DROP"),
    ("bud_en_famille_vaux_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
            "notes": "tick2139; Medium CW; assets/debt Unknown pending NBB PDF; omzet unpublished",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": (
            "Maison De Repos En Famille YE2025 leftover dual (bruto JUMP 1.03m / pnl FLIP LOSS)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "MRS residents Vaux-sur-Sûre / Luxembourg province (Wallonie)",
        "legal_basis": f"SRL maison de repos ROB/MRPA (KBO {KBO}; Actief; aanbestedende overheid; 1 VE)",
        "decision_date": "2026-04-16",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": BRUTO,
        "cash_by_year": (
            f'{{"2025_bruto":{BRUTO},"2025_omzet":"unpublished","2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_bruto":{BRUTO_PRIOR},'
            f'"2024_pnl":{PNL_PRIOR},"2024_equity":{EQUITY_PRIOR},"2024_fte":{FTE_PRIOR},"ve":1}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/maison-de-repos-en-famille",
        "stated_goal": "Nursing home / maison de repos for elderly (MRPA/ROB) — familial model",
        "cut_option": (
            "Publish NBB PDF assets/debt; disclose omzet/code70 + AViQ/INAMI vs resident-fee split; "
            "explain pnl FLIP LOSS path; clarify aanbestedende overheid status"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Luxembourg>VauxSurSure>EnFamille>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope (omzet unpublished); assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT Prestige / Corolles / Esplanade / Les Peupliers / Comte d'Egmont"
        ),
    },
)

# pi ≈ 0.55*5.8 + 0.35*3.8 + 0.10*(11-3.0) = 3.19+1.33+0.80 = 5.32 → 5.3
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": (
            "Maison De Repos En Famille bruto JUMP 1.03m / pnl FLIP LOSS -19k / omzet empty (YE2025)"
        ),
        "level": "L5",
        "type": "mrs_srl",
        "hierarchy_path": "Wallonie>Luxembourg>VauxSurSure>EnFamille>JR2025",
        "annual_cost_eur": BRUTO,
        "total_cost_eur": BRUTO,
        "tco_notes": (
            f"CW YE2025 bruto {BRUTO} JUMP {BRUTO_YOY} (primary; omzet unpublished); "
            f"pnl {PNL} FLIP LOSS from YE2024 PROFIT {PNL_PRIOR}; equity {EQUITY} DROP {EQUITY_YOY}; "
            f"FTE {FTE}; assets/debt Unknown pending NBB PDF; KBO Actief BV aanbestedende overheid 1 VE"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS residents Vaux-sur-Sûre / Salvacourt",
        "stated_goal": "Nursing home / maison de repos for elderly (MRPA)",
        "measured_outcome": (
            f"bruto JUMP {BRUTO_YOY}; pnl FLIP LOSS; equity DROP {EQUITY_YOY}; "
            f"FTE {FTE_PRIOR}→{FTE}; omzet unpublished"
        ),
        "absurdity_score": "5.8",
        "cost_score": "3.8",
        "difficulty": "3.0",
        "priority_index": "5.3",
        "cut_proposal": (
            "FOI NBB PDF + omzet disclosure + AViQ/INAMI split; explain pnl FLIP LOSS; "
            "clarify aanbestedende overheid vs private SRL"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT Prestige / Corolles / Esplanade / Les Peupliers / Comte d'Egmont"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Luxembourg>VauxSurSure>EnFamille>NBB_PDF_assets_debt_omzet_empty_pnl_flip_loss"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); omzet/code70 unpublished; "
            "AViQ/INAMI care vs resident fee split; pnl FLIP LOSS -19k path; aanbestedende overheid "
            "status vs private SRL; bedden/FTE matrix"
        ),
        "why_it_matters": (
            "Medium CW shows small Luxembourg MRS SRL (aanbestedende overheid) with bruto 1.03m JUMP "
            "flipping to LOSS while omzet/assets/debt opaque — public-procurement / care-margin gap"
        ),
        "priority": "8",
        "recipient_body": "Maison De Repos En Famille SRL",
        "recipient_email": "info@residenceenfamille.be",
        "recipient_postal": "Salvacourt 11, 6640 Vaux-sur-Sûre",
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
        "notes": f"tick{TICK}; human-send only; Medium CW; next EVERY-10 2140",
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
                f"tick{TICK} leftover Maison De Repos En Famille {KBO} Medium CW (bruto JUMP 1.03m "
                f"pnl FLIP LOSS -19k equity DROP 0.20m FTE 12.9 omzet unpublished; Actief BV "
                f"aanbestedende overheid 1 VE Salvacourt; assets/debt Unknown); AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; next {NEXT_RQ} EVERY-10; next every-10 after 2150; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Maison De Repos En Famille Vaux (bruto JUMP 1.03m / pnl FLIP LOSS -19k / Medium)

- Unit: **{RQ}** leftover dual after **rq_2138 Residence Prestige** (race: concurrent took Prestige as 2138). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; La Moisson absorbed blocked. Took unused leftover **Maison De Repos En Famille SRL** YE2025 (KBO **{KBO}**; Salvacourt 11 Vaux-sur-Sûre; **BV/SRL** NACE **87.301** / **1 VE**; **aanbestedende overheid**). Do not redo Prestige/Corolles/Esplanade/Les Peupliers/Comte d'Egmont/CIGB/Ten Rozen/L'Orchidée/La Moisson.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY} vs YE2024 EUR{BRUTO_PRIOR}; pnl **EUR{PNL}** FLIP LOSS from YE2024 PROFIT EUR{PNL_PRIOR}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; FTE **{FTE}** vs {FTE_PRIOR}; neerlegging **16.04.2026**. KBO Strong Actief + aanbestedende overheid. Assets/debt Unknown. Medium. FOI via info@residenceenfamille.be.
- Wrote: sources (+5); budgets (+4); commitments (+1); leaderboard (+1 pi 5.3); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open EVERY-10; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2139/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 this tick (**next rq_2140=2140 EVERY-10** must refresh progress+top10). Next: {NEXT_RQ} (progress+top10 + AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
    )

print("OK tick", TICK, ENTITY, "bruto", BRUTO, "pnl", PNL, "equity", EQUITY)
