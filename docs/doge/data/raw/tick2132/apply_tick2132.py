# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T14:00:00Z"
TICK = 2132
RQ = "rq_2132"
NEXT_RQ = "rq_2133"
ENTITY = "vzw_olv_maagd_der_armen_aalst"
GAP = "gap_maagd_der_armen_nbb_pdf_assets_debt_omzet_jump_pnl_jump_matrix_l5"
COMM = "comm_maagd_der_armen_jr2025_statutory_wzc_ten_rozen"
LB = "lb_maagd_der_armen_omzet_jump_6_91m_pnl_jump_jr2025"
SRC_EN = "src_maagd_der_armen_jr2025_cw_en"
KBO = "0446.222.962"
KBO_DIGITS = "0446222962"
OMZET = "6906734"
OMZET_PRIOR = "6375644"
OMZET_YOY = "+8.33%"
BRUTO = "7122013"
BRUTO_PRIOR = "6576209"
BRUTO_YOY = "+8.3%"
PNL = "863354"
PNL_PRIOR = "611780"
PNL_YOY = "+41.12%"
EQUITY = "5617266"
EQUITY_PRIOR = "4784534"
EQUITY_YOY = "+17.4%"
FTE = "92.1"
FTE_PRIOR = "88.3"
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
            r["title"] = "leftover dual — OLV Maagd Der Armen / Ten Rozen Aalst YE2025 Medium"
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Maagd Der Armen Medium omzet JUMP 6.91m bruto JUMP 7.12m pnl JUMP 0.86m "
                f"equity JUMP 5.62m FTE 92.1; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2140"
            )
            r["instructions"] = (
                f"Completed leftover OLV Maagd Der Armen / Ten Rozen Aalst YE2025 Medium CW after L'Orchidée; "
                f"preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE {FTE}; FOI {GAP}"
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
                    "leftover dual hole-fill after Maagd Der Armen — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after OLV Maagd Der Armen / Ten Rozen Aalst YE2025 Medium. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. Do NOT redo "
                    "Maagd Der Armen / Ten Rozen Aalst, L'Orchidée Ittre, Care-Support, MPC Sint-Franciscus, "
                    "Zorghome De Fakkel, Restel Flats, Le Château Vert, SLG Wallonie, Famifamenne, Residence Le Castel, "
                    "R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, Le Bosquet, Strebo, Entraide, La Charmille, "
                    "Charmilles, Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, "
                    "Sint-Camillus, IDELUX*, INTRADEL, Korian*, SLG Operaties VL, SLG Vlaanderen VZW, Always Home, "
                    "AREWAL, AGB Bornem, Armonea holding, emeis holding, Maria's Rustoord Moorslede, Heilig Hart "
                    "Grimbergen, Veilige Have, Molenheide, Huize Sint-Jozef Ieper."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Maagd Der Armen; FARO/AIESH/REW still YE2024; next every-10 2140"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_maagd_der_armen_jr2025_cw",
        "title": "Companyweb NL OLV Maagd Der Armen YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl JUMP {PNL} ({PNL_YOY}) equity JUMP {EQUITY} ({EQUITY_YOY}) FTE {FTE}; "
            f"neerlegging 03.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2132/maagd_cw_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN OLV Maagd Der Armen YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/onze-lieve-vrouw-maagd-der-armen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 03-07-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; FTE {FTE}; Principal activity nursing homes (M.R.P.A.); "
            f"raw docs/doge/data/raw/tick2132/maagd_cw_en.html"
        ),
    },
    {
        "source_id": "src_maagd_der_armen_jr2025_cw_fr",
        "title": "Companyweb FR OLV Maagd Der Armen YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2132/maagd_cw_fr.html",
    },
    {
        "source_id": f"src_maagd_der_armen_kbo_{TICK}",
        "title": f"KBO OLV Maagd Der Armen {KBO} Actief Aalst Ten Rozen",
        "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Actief VZW; Rozendreef 190 9300 Aalst; 1 VE; RSZ NACE 87.301 ROB; "
            "commercial name Beheerder van Rusthuis O.L.V. Ten Rozen; dagelijks bestuur Bruyland Nathalie / "
            "Vanderbeken Marc"
        ),
    },
    {
        "source_id": f"src_maagd_der_armen_site_{TICK}",
        "title": "WZC OLV Ten Rozen site FOI contact info@wzctenrozen.be",
        "url": "https://www.wzctenrozen.be/",
        "publisher": "WZC OLV Ten Rozen / Maagd Der Armen VZW",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": f"tick{TICK}; WZC OLV Ten Rozen Aalst; FOI info@wzctenrozen.be / zorgdirecteur@wzctenrozen.be",
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Onze-Lieve-Vrouw Maagd Der Armen (Aalst / WZC OLV Ten Rozen)",
        "name_fr": "Notre-Dame Vierge des Pauvres ASBL (Alost / MRS Ten Rozen)",
        "name_en": "OLV Maagd Der Armen VZW (Aalst; WZC Ten Rozen nursing home)",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.wzctenrozen.be/",
        "foi_email": "info@wzctenrozen.be",
        "foi_postal": "Rozendreef 190, 9300 Aalst",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW 1 VE NACE 87.301; "
            f"omzet JUMP 6.91m ({OMZET_YOY}) bruto JUMP 7.12m ({BRUTO_YOY}) pnl JUMP 0.86m ({PNL_YOY}) "
            f"equity JUMP 5.62m ({EQUITY_YOY}) FTE {FTE}; assets/debt Unknown; filed 03.07.2026; FOI {GAP}; "
            "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT L'Orchidée / Care-Support / Restel Flats"
        ),
    },
)

for bid, amt, basis in [
    ("bud_maagd_der_armen_omzet_jr2025_statutory", OMZET, "CW YE2025 Omzet / Turnover"),
    ("bud_maagd_der_armen_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin"),
    ("bud_maagd_der_armen_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss"),
    ("bud_maagd_der_armen_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
    ("bud_maagd_der_armen_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
        "title": "OLV Maagd Der Armen / Ten Rozen YE2025 leftover dual (omzet JUMP 6.91m / pnl JUMP)",
        "entity_id": ENTITY,
        "beneficiary": "WZC residents Aalst (OLV Ten Rozen; ~108 beds + kortverblijf)",
        "legal_basis": f"VZW WZC/ROB (KBO {KBO}; NACE 87.301; 1 VE)",
        "decision_date": "2026-07-03",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET_PRIOR},'
            f'"2024_bruto":{BRUTO_PRIOR},"2024_pnl":{PNL_PRIOR}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/onze-lieve-vrouw-maagd-der-armen",
        "stated_goal": "Elderly residential care (ROB/WZC Ten Rozen Aalst)",
        "cut_option": (
            "Publish NBB PDF assets/debt; disclose RIZIV/VL care vs resident fee split on omzet JUMP"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Aalst>MaagdDerArmen>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT L'Orchidée / Care-Support / Restel Flats / De Fakkel"
        ),
    },
)

# pi ≈ 0.55*5.8 + 0.35*4.2 + 0.10*(11-3.5) ≈ 3.19+1.47+0.75 = 5.41 → 5.4
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "OLV Maagd Der Armen / Ten Rozen omzet JUMP 6.91m / pnl JUMP 0.86m (YE2025)",
        "level": "L5",
        "type": "wzc_vzw",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Aalst>MaagdDerArmen>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY}; bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} JUMP {PNL_YOY}; equity {EQUITY} JUMP {EQUITY_YOY}; FTE {FTE}; "
            "assets/debt Unknown pending NBB PDF; WZC/ROB NACE 87.301"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "WZC residents Aalst (OLV Ten Rozen)",
        "stated_goal": "Elderly residential care (ROB/WZC)",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl JUMP {PNL_YOY}; "
            f"equity JUMP {EQUITY_YOY}; FTE {FTE_PRIOR}→{FTE}"
        ),
        "absurdity_score": "5.8",
        "cost_score": "4.2",
        "difficulty": "3.5",
        "priority_index": "5.4",
        "cut_proposal": (
            "FOI NBB PDF + care-subsidy vs resident-fee split; explain pnl JUMP +41pct path"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
            "DISTINCT L'Orchidée / Care-Support / Restel Flats"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Aalst>MaagdDerArmen>NBB_PDF_assets_debt_omzet_pnl_jump",
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); RIZIV/VL care vs resident fee split; "
            "pnl JUMP 0.86m / equity JUMP path; 1 VE activity matrix"
        ),
        "why_it_matters": (
            "Medium CW shows WZC VZW with omzet JUMP 6.91m and pnl JUMP 0.86m while assets/debt and "
            "public-care vs private-fee mix opaque — subsidy transparency gap"
        ),
        "priority": "8",
        "recipient_body": "VZW Onze-Lieve-Vrouw Maagd Der Armen / WZC OLV Ten Rozen",
        "recipient_email": "info@wzctenrozen.be",
        "recipient_postal": "Rozendreef 190, 9300 Aalst",
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
                f"tick{TICK} leftover OLV Maagd Der Armen Aalst {KBO} Medium CW (omzet JUMP 6.91m bruto JUMP 7.12m "
                f"pnl JUMP 0.86m equity JUMP 5.62m FTE 92.1; assets/debt Unknown; 1 VE NACE 87.301 Ten Rozen); "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2140; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} OLV Maagd Der Armen / Ten Rozen Aalst (omzet JUMP 6.91m / pnl JUMP 0.86m / Medium)

- Unit: **{RQ}** leftover dual after **rq_2131 L'Orchidée Ittre**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Onze-Lieve-Vrouw Maagd Der Armen VZW** YE2025 (KBO **{KBO}**; Rozendreef 190 Aalst; **VZW** NACE **87.301** / **1 VE**; commercial name Beheerder van Rusthuis O.L.V. Ten Rozen). Do not redo L'Orchidée/Care-Support/Restel Flats/De Fakkel/SLG Wallonie/Famifamenne/MPC Sint-Franciscus/Armonea holding.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY} vs YE2024 EUR{OMZET_PRIOR}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** JUMP {PNL_YOY}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}** vs {FTE_PRIOR}; neerlegging **03.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info@wzctenrozen.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.4); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2132/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2130**; next **2140**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "omzet", OMZET)
