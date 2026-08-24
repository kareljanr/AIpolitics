# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T14:40:00Z"
TICK = 2134
RQ = "rq_2134"
NEXT_RQ = "rq_2135"
ENTITY = "nv_mrs_comte_degmont_chievres"
GAP = "gap_comte_degmont_nbb_pdf_assets_debt_omzet_empty_loss_widen_thin_equity_matrix_l5"
COMM = "comm_comte_degmont_jr2025_statutory_mrs"
LB = "lb_comte_degmont_bruto_jump_2_76m_pnl_loss_widen_thin_equity_jr2025"
SRC_EN = "src_comte_degmont_jr2025_cw_en"
KBO = "0454.712.838"
KBO_DIGITS = "0454712838"
OMZET = ""
BRUTO = "2759169"
BRUTO_PRIOR = "2507548"
BRUTO_YOY = "+10.03%"
PNL = "-162383"
PNL_PRIOR = "-103936"
PNL_YOY = "-56.23%"
EQUITY = "235121"
EQUITY_PRIOR = "397504"
EQUITY_YOY = "-40.85%"
FTE = "39"
FTE_PRIOR = "36.5"
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
            r["title"] = "leftover dual — MRS Comte d'Egmont Chièvres YE2025 Medium (loss widen / thin equity)"
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Comte d'Egmont Medium bruto JUMP 2.76m pnl LOSS WIDEN -162k "
                f"equity DROP thin 0.24m FTE 39 omzet empty; FOI ready; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2140"
            )
            r["instructions"] = (
                f"Completed leftover MRS Comte d'Egmont YE2025 Medium CW after CIGB Menen; "
                f"preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"bruto JUMP {BRUTO} pnl LOSS WIDEN {PNL} equity DROP thin {EQUITY} FTE {FTE} omzet empty; FOI {GAP}"
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
                    "leftover dual hole-fill after Comte d'Egmont — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after MRS Comte d'Egmont YE2025 Medium. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. Do NOT redo "
                    "Comte d'Egmont / Residence Comte d'Egmont Chièvres, C.I.G.B. Menen / PC Menen / Huize Ter Walle, "
                    "Maagd Der Armen / Ten Rozen Aalst, L'Orchidée Ittre, Care-Support, MPC Sint-Franciscus, "
                    "Zorghome De Fakkel, Restel Flats, Le Château Vert, SLG Wallonie, Famifamenne, Residence Le Castel, "
                    "R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, Le Bosquet, Strebo, Entraide, La Charmille, "
                    "Charmilles, Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, "
                    "Sint-Camillus, IDELUX*, INTRADEL, Korian*, SLG Operaties VL, SLG Vlaanderen VZW, Always Home, "
                    "AREWAL, AGB Bornem, Armonea holding, emeis holding, Maria's Rustoord Moorslede, Heilig Hart Grimbergen, "
                    "Veilige Have, Molenheide, Huize Sint-Jozef Ieper, PC Gent-Sleidinge, PC Sint-Hiëronymus, "
                    "Residence Prestige Chaudfontaine (deferred live YE2025), Les Peupliers Seneffe (deferred live YE2025), "
                    "l'Esplanade Ath (deferred live YE2025)."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Comte d'Egmont; FARO/AIESH/REW still YE2024; next every-10 2140"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_comte_degmont_jr2025_cw",
        "title": "Companyweb NL MRS Comte d'Egmont Chièvres YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet empty; bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl LOSS WIDEN {PNL} ({PNL_YOY}) equity DROP thin {EQUITY} ({EQUITY_YOY}) FTE {FTE}; "
            f"neerlegging 01.08.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2134/egmont_cw_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN MRS Comte d'Egmont Chièvres YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/maison-de-repos-le-comte-d-egmont",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 01-08-2026; Last balance sheet year 2025; "
            f"Turnover unpublished; Gross margin {BRUTO}; FTE {FTE}; Principal activity nursing homes elderly; "
            f"Commercial name RESIDENCE COMTE D'EGMONT; raw docs/doge/data/raw/tick2134/egmont_cw_en.html"
        ),
    },
    {
        "source_id": "src_comte_degmont_jr2025_cw_fr",
        "title": "Companyweb FR MRS Comte d'Egmont Chièvres YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2134/egmont_cw_fr.html",
    },
    {
        "source_id": f"src_comte_degmont_kbo_{TICK}",
        "title": f"KBO MRS Comte d'Egmont {KBO} Actief NV Chièvres",
        "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Actief NV/SA; Grand'Place 17 7950 Chièvres; 1 VE; "
            "hoofdactiviteit rusthuizen voor ouderen / maisons de repos (MRPA)"
        ),
    },
    {
        "source_id": f"src_comte_degmont_contact_{TICK}",
        "title": "Guide Social contact Résidence Comte d'Egmont jeanmarchendrick@skynet.be",
        "url": "https://annuaire.guidesocial.be/fr-BE/organismes/residence-comte-d-egmont__125854",
        "publisher": "Guide Social (directory)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_directory",
        "notes": (
            f"tick{TICK}; FOI email jeanmarchendrick@skynet.be; tel 068 66 51 12; "
            "privé SA; ~50 beds MR/MRS directory class"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Maison de Repos Le Comte d'Egmont / Résidence Comte d'Egmont (Chièvres)",
        "name_fr": "Maison de Repos Le Comte d'Egmont / Résidence Comte d'Egmont (Chièvres)",
        "name_en": "Nursing home Comte d'Egmont (Chièvres MRS)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "",
        "foi_email": "jeanmarchendrick@skynet.be",
        "foi_postal": "Grand'Place 17, 7950 Chièvres",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief NV/SA 1 VE NACE MRPA; "
            f"omzet empty; bruto JUMP 2.76m ({BRUTO_YOY}) pnl LOSS WIDEN -162k ({PNL_YOY}) "
            f"equity DROP thin 0.24m ({EQUITY_YOY}) FTE {FTE}; assets/debt Unknown; filed 01.08.2026; FOI {GAP}; "
            "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT CIGB Menen / Ten Rozen / L'Orchidée / "
            "Care-Support / Restel Flats / De Fakkel / Castel / Famifamenne"
        ),
    },
)

for bid, amt, basis in [
    ("bud_comte_degmont_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin (omzet unpublished)"),
    ("bud_comte_degmont_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss LOSS widen"),
    ("bud_comte_degmont_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity thin"),
    ("bud_comte_degmont_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
            "notes": f"tick{TICK}; Medium CW; omzet empty; assets/debt Unknown pending NBB PDF",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "MRS Comte d'Egmont YE2025 leftover dual (bruto JUMP 2.76m / loss widen / thin equity)",
        "entity_id": ENTITY,
        "beneficiary": "MRS residents Chièvres (Hainaut / Wallonie)",
        "legal_basis": f"NV/SA maison de repos MRPA (KBO {KBO}; 1 VE)",
        "decision_date": "2026-08-01",
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
        "evaluation_url": (
            f"https://www.companyweb.be/en/{KBO_DIGITS}/maison-de-repos-le-comte-d-egmont"
        ),
        "stated_goal": "Private nursing home / maison de repos for elderly (MRPA)",
        "cut_option": (
            "Publish NBB PDF assets/debt; disclose AViQ/INAMI care vs resident fee split; "
            "explain multi-year LOSS widen + equity DROP thin despite bruto JUMP"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>Chievres>ComteDEgmont>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope (omzet empty); assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT CIGB Menen / Ten Rozen / L'Orchidée / Care-Support / Restel Flats"
        ),
    },
)

# pi ≈ 0.55*6.0 + 0.35*4.0 + 0.10*(11-3.5) = 3.30+1.40+0.75 = 5.45 → 5.5
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "MRS Comte d'Egmont bruto JUMP 2.76m / pnl LOSS widen -162k / thin equity 0.24m (YE2025)",
        "level": "L5",
        "type": "mrs_nv",
        "hierarchy_path": "Wallonie>Hainaut>Chievres>ComteDEgmont>JR2025",
        "annual_cost_eur": BRUTO,
        "total_cost_eur": BRUTO,
        "tco_notes": (
            f"CW YE2025 omzet empty; bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} LOSS WIDEN {PNL_YOY} vs prior {PNL_PRIOR}; equity {EQUITY} DROP {EQUITY_YOY} thin; "
            f"FTE {FTE}; assets/debt Unknown pending NBB PDF; 1 VE MRS"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "MRS residents Chièvres",
        "stated_goal": "Private nursing home / maison de repos for elderly",
        "measured_outcome": (
            f"omzet empty; bruto JUMP {BRUTO_YOY}; pnl LOSS WIDEN {PNL_YOY}; "
            f"equity DROP {EQUITY_YOY} thin; FTE {FTE_PRIOR}→{FTE}"
        ),
        "absurdity_score": "6.0",
        "cost_score": "4.0",
        "difficulty": "3.5",
        "priority_index": "5.5",
        "cut_proposal": (
            "FOI NBB PDF + AViQ/INAMI care vs resident-fee split; explain LOSS widen + thin equity despite bruto JUMP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
            "DISTINCT CIGB Menen / Ten Rozen / L'Orchidée / Care-Support / Restel Flats"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>Hainaut>Chievres>ComteDEgmont>NBB_PDF_assets_debt_omzet_empty_loss_widen",
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); omzet/code70 (CW empty); "
            "AViQ/INAMI care vs resident fee split; pnl LOSS widen -162k + equity DROP thin 0.24m path; 1 VE matrix"
        ),
        "why_it_matters": (
            "Medium CW shows private MRS NV with bruto JUMP 2.76m but multi-year LOSS widen to -162k and equity "
            "DROP thin to 0.24m while assets/debt and public-care vs resident-fee mix opaque"
        ),
        "priority": "8",
        "recipient_body": "SA Maison de Repos Le Comte d'Egmont / Résidence Comte d'Egmont",
        "recipient_email": "jeanmarchendrick@skynet.be",
        "recipient_postal": "Grand'Place 17, 7950 Chièvres",
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
                f"tick{TICK} leftover MRS Comte d'Egmont {KBO} Medium CW (bruto JUMP 2.76m "
                f"pnl LOSS WIDEN -162k equity DROP thin 0.24m FTE 39 omzet empty; assets/debt Unknown; 1 VE MRS); "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2140; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} MRS Comte d'Egmont Chièvres (bruto JUMP 2.76m / LOSS widen -162k / thin equity / Medium)

- Unit: **{RQ}** leftover dual after **rq_2133 C.I.G.B. Menen**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Maison de Repos Le Comte d'Egmont SA** YE2025 (KBO **{KBO}**; Grand'Place 17 Chièvres; **NV/SA** NACE **MRPA** / **1 VE**; commercial name Résidence Comte d'Egmont). Do not redo CIGB Menen/Ten Rozen/L'Orchidée/Care-Support/Restel Flats/De Fakkel/SLG Wallonie/Famifamenne/MPC Sint-Franciscus/Armonea holding. Deferred live YE2025: Residence Prestige / Les Peupliers / l'Esplanade Ath.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY} vs YE2024 EUR{BRUTO_PRIOR}; pnl **EUR{PNL}** LOSS WIDEN {PNL_YOY} vs YE2024 EUR{PNL_PRIOR}; equity **EUR{EQUITY}** DROP {EQUITY_YOY} thin; FTE **{FTE}** vs {FTE_PRIOR}; neerlegging **01.08.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via jeanmarchendrick@skynet.be.
- Wrote: sources (+5); budgets (+4); commitments (+1); leaderboard (+1 pi 5.5); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2134/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2130**; next **2140**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Prestige-Peupliers-Esplanade / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "bruto", BRUTO, "pnl", PNL)
