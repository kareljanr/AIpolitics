# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T12:20:00Z"
TICK = 2126
RQ = "rq_2126"
NEXT_RQ = "rq_2127"
ENTITY = "srl_slg_wallonie"
GAP = "gap_slg_wallonie_nbb_pdf_assets_debt_merger_jump_loss_matrix_l5"
COMM = "comm_slg_wallonie_jr2025_statutory_merger_jump"
LB = "lb_slg_wallonie_omzet_jump_44_73m_fte_jump_loss_jr2025"
SRC_EN = "src_slg_wallonie_jr2025_cw_en"
KBO = "0427.821.963"
KBO_DIGITS = "0427821963"
OMZET = "44731152"
OMZET_PRIOR = "6889604"
OMZET_YOY = "+549.26%"
BRUTO = "27100572"
BRUTO_PRIOR = "5038811"
BRUTO_YOY = "+437.84%"
PNL = "-1210267"
PNL_PRIOR = "-21853"
EQUITY = "8741449"
EQUITY_PRIOR = "1290937"
EQUITY_YOY = "+577.14%"
FTE = "545.3"
FTE_PRIOR = "78.1"
ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def update_rq_done():
    path = DATA / "research_queue.csv"
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fields = rows[0].keys() if rows else []
        # re-read fieldnames properly
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r.get("task_id") == RQ and r.get("status") == "open":
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["title"] = "leftover dual — SLG Wallonie YE2025 Medium"
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} SLG Wallonie Medium omzet JUMP 44.73m bruto JUMP 27.10m "
                f"pnl LOSS -1.21m equity JUMP 8.74m FTE JUMP 545.3; FOI ready; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2130"
            )
            r["instructions"] = (
                f"Completed leftover dual SLG Wallonie after Famifamenne; preferred AGB Bornem JR2024 / "
                f"FARO/AIESH/REW YE2024; live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl LOSS {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; "
                f"FOI {GAP}; mid-2025 absorption wave Korian Wallonie MRS"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"{RQ} open row not found")
    # spawn next if missing
    if not any(r.get("task_id") == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after SLG Wallonie — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after SLG Wallonie YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/"
                    "hospital/WZC/psych/MRS/creche. Do NOT redo SLG Wallonie, Famifamenne, Residence Le Castel, "
                    "R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, Le Bosquet, Strebo, Entraide, La Charmille, "
                    "Charmilles, Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, "
                    "Zilverlinde, Sint-Camillus, IDELUX*, INTRADEL, Korian Belgium holding, Comnexio, ORES*, "
                    "SLG Operaties Vlaanderen, Always Home, AREWAL, AGB Bornem, Armonea holding, emeis holding."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} SLG Wallonie fill; FARO/AIESH/REW still YE2024; next every-10 2130"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": "src_slg_wallonie_jr2025_cw",
        "title": "Companyweb NL SLG Wallonie YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl LOSS {PNL} equity JUMP {EQUITY} ({EQUITY_YOY}) FTE JUMP {FTE} (vs {FTE_PRIOR}); "
            f"neerlegging 28.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2126/slgw_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN SLG Wallonie YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 28-07-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; FTE {FTE}; Principal activity nursing homes MRPA; "
            f"raw docs/doge/data/raw/tick2126/slgw_en.html"
        ),
    },
    {
        "source_id": "src_slg_wallonie_jr2025_cw_fr",
        "title": "Companyweb FR SLG Wallonie YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2126/slgw_fr.html",
    },
    {
        "source_id": f"src_slg_wallonie_kbo_{TICK}",
        "title": f"KBO SLG Wallonie {KBO} Actief Namur Korian-path",
        "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Actief BV/SRL SLG WALLONIE; Rue des VII Voyes(VD) 9 5020 Namur since 30.06.2025; "
            f"2 VE; NACE 87.101/87.302; bestuurders 0869.769.702 Beelen Dominiek + 0894.020.690 Danneels Liesbet; "
            "absorbed mid-2025 Seniservices/Passerinette/Cheveux d'Argent/Ry du Chevreuil/Bethanie/Le Progres/"
            "Seigneurie du Val; email/web empty in KBO"
        ),
    },
    {
        "source_id": f"src_slg_wallonie_korian_{TICK}",
        "title": "Korian Belgium FOI contact info@korian.be (SLG Wallonie path)",
        "url": "https://www.korian.be/",
        "publisher": "Korian Belgium / SLG",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Walloon Korian/SLG ops shell after mid-2025 absorption wave; FOI info@korian.be; "
            "DISTINCT SLG Operaties Vlaanderen / Korian Belgium holding / mined Charmilles/Sittelles/Buissons"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "SLG Wallonie (Namur / Korian-path MRS ops)",
        "name_fr": "SLG Wallonie SRL (Namur / ops MRS Korian)",
        "name_en": "SLG Wallonie nursing-home SRL (Namur; Korian path)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.korian.be/",
        "foi_email": "info@korian.be",
        "foi_postal": "Rue des VII Voyes(VD) 9, 5020 Namur",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief BV/SRL 2 VE NACE 87.101/87.302; "
            f"omzet JUMP 44.73m ({OMZET_YOY}) bruto JUMP 27.10m ({BRUTO_YOY}) pnl LOSS -1.21m equity JUMP 8.74m "
            f"({EQUITY_YOY}) FTE JUMP {FTE} (vs {FTE_PRIOR}); assets/debt Unknown; filed 28.07.2026; "
            f"mid-2025 absorption wave 7 MRS; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "DISTINCT SLG Operaties VL / Korian holding / Famifamenne / Charmilles continuum"
        ),
    },
)

for bid, amt, basis in [
    ("bud_slg_wallonie_omzet_jr2025_statutory", OMZET, "CW YE2025 omzet / Turnover (primary envelope)"),
    ("bud_slg_wallonie_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin"),
    ("bud_slg_wallonie_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss (LOSS)"),
    ("bud_slg_wallonie_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
    ("bud_slg_wallonie_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
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
            "notes": f"tick{TICK}; Medium CW; assets/debt Unknown pending NBB PDF; merger JUMP path",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "SLG Wallonie YE2025 leftover dual (omzet JUMP 44.73m / FTE JUMP / LOSS)",
        "entity_id": ENTITY,
        "beneficiary": "Walloon ROB/RVT residents via Korian/SLG (2 VE; 7 absorbed MRS mid-2025)",
        "legal_basis": f"BV/SRL maison de repos RVT/ROB (KBO {KBO}; NACE 87.101/87.302; 2 VE)",
        "decision_date": "2026-07-28",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET_PRIOR},'
            f'"2024_fte":{FTE_PRIOR}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "stated_goal": "Public-interest multi-site nursing-home care (Wallonie AViQ-adjacent / Korian path)",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; map per-absorbed entity contribution to +549% omzet / "
            "+545 FTE JUMP; disclose AViQ/INAMI vs fees; explain LOSS with equity JUMP"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Namur>SLG_Wallonie>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT SLG Operaties VL / Korian holding / Famifamenne"
        ),
    },
)

# priority_index ≈ 0.55*abs + 0.35*cost + 0.10*(10-diff)
# abs 7.8 (merger JUMP + LOSS), cost 6.8 (~45m), diff 3.5 → 0.55*7.8+0.35*6.8+0.10*6.5 ≈ 4.29+2.38+0.65 = 7.32
append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "SLG Wallonie omzet JUMP 44.73m (+549%) / FTE JUMP 78→545 / LOSS -1.21m (YE2025)",
        "level": "L5",
        "type": "mrs_statutory_srl",
        "hierarchy_path": "Wallonie>Namur>SLG_Wallonie>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY} (primary); bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl LOSS {PNL}; equity {EQUITY} JUMP {EQUITY_YOY}; FTE {FTE} JUMP vs {FTE_PRIOR}; "
            "assets/debt Unknown pending NBB PDF; mid-2025 absorption of 7 Walloon MRS"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "Walloon ROB/RVT residents (Korian/SLG multi-site after absorption wave)",
        "stated_goal": "Public-interest nursing-home care (Wallonie)",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl LOSS WIDEN; "
            f"equity JUMP {EQUITY_YOY}; FTE JUMP {FTE_PRIOR}→{FTE}"
        ),
        "absurdity_score": "7.8",
        "cost_score": "6.8",
        "difficulty": "3.5",
        "priority_index": "7.3",
        "cut_proposal": (
            "FOI NBB PDF + per-absorbed MRS contribution matrix + assets/debt; "
            "map AViQ/INAMI vs private operator extraction amid LOSS"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
            "DISTINCT SLG Operaties VL / Korian holding / Famifamenne / Charmilles continuum"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>Namur>SLG_Wallonie>NBB_PDF_assets_debt_merger_jump_loss",
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); per-absorbed entity omzet/FTE "
            "contribution matrix (7 MRS mid-2025); AViQ/INAMI vs fee split; LOSS vs equity JUMP path"
        ),
        "why_it_matters": (
            "Medium CW shows Korian/SLG Wallonie ops SRL with omzet JUMP 44.73m (+549%) and FTE 78→545 "
            "after absorbing 7 MRS while posting LOSS -1.21m and opaque assets/debt — merger / care-margin "
            "transparency gap"
        ),
        "priority": "8",
        "recipient_body": "SLG Wallonie SRL (via Korian Belgium)",
        "recipient_email": "info@korian.be",
        "recipient_postal": "Rue des VII Voyes(VD) 9, 5020 Namur",
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
        "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2130",
    },
)

# loop_state
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
                f"tick{TICK} leftover SLG Wallonie {KBO} Medium CW (omzet JUMP 44.73m +549% bruto JUMP 27.10m "
                f"pnl LOSS -1.21m equity JUMP 8.74m FTE JUMP 545.3 vs 78.1; assets/debt Unknown; 2 VE NACE "
                f"87.101/87.302 Namur Korian-path; mid-2025 absorbed 7 MRS); AGB Bornem JR2024; FARO/AIESH/REW "
                f"YE2024; Famifamenne taken; next {NEXT_RQ}; next every-10 2130; continuous hole_fill"
            ),
        }
    )

update_rq_done()

# loop_log append
log_path = ROOT / "loop_log.md"
entry = f"""
## Tick {TICK} - {UTC} - {RQ} SLG Wallonie Namur (omzet JUMP 44.73m / FTE JUMP 78→545 / LOSS -1.21m / Medium)

- Unit: **{RQ}** leftover dual after **rq_2125 Famifamenne**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **SLG Wallonie SRL** YE2025 (KBO **{KBO}**; Rue des VII Voyes 9 Namur; **BV/SRL** NACE **87.101/87.302** / **2 VE**; Korian path; mid-2025 absorption of 7 Walloon MRS). Do not redo Famifamenne/Le Castel/RSW/Home Sebrechts/Unite/'t Buurthuis/Le Bosquet/Strebo/Entraide/SLG Operaties VL/Korian holding/Armonea holding.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY} vs YE2024 EUR{OMZET_PRIOR}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** LOSS WIDEN vs YE2024 EUR{PNL_PRIOR}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}** JUMP vs {FTE_PRIOR}; neerlegging **28.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info@korian.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 7.3); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2126/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2120**; next **2130**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
with open(log_path, "a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick", TICK, ENTITY, "omzet", OMZET)
