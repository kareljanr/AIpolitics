# -*- coding: utf-8 -*-
"""Apply tick 2114 — Les Buissons Spa (Château Sous Bois / Korian) YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
FOI_DRAFT = ROOT / "foi" / "drafts"
csv.field_size_limit(10**7)

UTC = "2026-08-25T08:55:00Z"
TICK = 2114
RQ = "rq_2114"
NEXT_RQ = "rq_2115"
ENTITY = "bv_les_buissons_spa"
GAP = "gap_les_buissons_spa_nbb_pdf_assets_debt_pnl_loss_widen_equity_drop_matrix_l5"
KBO = "0466.961.859"
KBO_DIGITS = "0466961859"
OMZET = 4751876
BRUTO = 3660061
PNL = -288584
EQUITY = 165283
FTE = 54.3
OMZET_PRIOR = 4704912
PNL_PRIOR = -39598
BRUTO_PRIOR = 3709951
EQUITY_PRIOR = 453867
EMAIL = "info@korian.be"
ADDR = "Chemin Sous-Bois 22, 4900 Spa"
WEBSITE = (
    "https://www.korian.be/fr/maisons-de-repos/chateau-sous-bois/"
    "maison-de-repos-chateau-sous-bois/"
)
LB = "lb_les_buissons_omzet_4_75m_pnl_loss_widen_equity_drop_jr2025"
COMM = "comm_les_buissons_spa_jr2025_statutory_mrs"
SLUG = "residence-les-buissons"

DO_NOT_REDO = (
    "Do NOT redo Les Buissons / Château Sous Bois Spa, Résidence 3 / Saphir, "
    "Elisabeth Aan Zee Oostende, Maison de Repos du XXe Août / PLIMCO, "
    "Rusthuis Sint Jozef Ninove, WZC Zilverlinde Olen, Woonzorgcentrum "
    "Sint-Camillus Wevelgem, IDELUX Développement, IDELUX Projets Publics, "
    "IDELUX Eau, IDELUX Finances, IDELUX Environnement, INTRADEL, Korian "
    "Belgium, Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, Always Home, "
    "SLG Operaties, AREWAL, HYGEA, BEP Environnement, AIEG, RESA, Enodia, "
    "Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, IGRETEC, "
    "SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, Aquafin, AGB Bornem, "
    "Armonea, Colisée Belgium, Familiezorg Gent, emeis, IRE*, FANC, SCK CEN, "
    "Veilige Have, Molenheide, WZC Sint-Jozef Rumst, Cassiers, OLV Roosdaal, "
    "De Verlosser Dilbeek, WZC De Foyer Gent."
)


def append_rows(path: Path, new_rows: list[dict]):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    ids = {r.get(fieldnames[0]) for r in rows}
    added = 0
    for nr in new_rows:
        if nr.get(fieldnames[0]) in ids:
            print("SKIP exists", path.name, nr.get(fieldnames[0]))
            continue
        clean = {k: nr.get(k, "") for k in fieldnames}
        rows.append(clean)
        added += 1
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(path.name, "appended", added)


def upsert_entity():
    path = DATA / "entities.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    note = (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief BV/SRL "
        f"1 VE NACE 87.301 ROB (Château Sous Bois); omzet JUMP {OMZET/1e6:.2f}m "
        f"(+1.00%) bruto DROP {BRUTO/1e6:.2f}m (−1.34%) pnl LOSS WIDEN "
        f"{PNL/1e6:.2f}m (−628.78% vs YE2024 LOSS {PNL_PRIOR}) equity DROP "
        f"{EQUITY/1e6:.2f}m (−63.58%) FTE {FTE} (YoY Unknown); assets/debt "
        f"Unknown; neerlegging 28.07.2026; FOI {GAP}; Korian Belgium "
        f"bestuurder/gedelegeerd 0869.769.702 path; preferred AGB Bornem "
        f"JR2024; FARO/AIESH/REW YE2024; DISTINCT Résidence 3/Elisabeth Aan "
        f"Zee/XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL"
    )
    found = False
    for r in rows:
        if r.get("entity_id") == ENTITY:
            r["foi_email"] = EMAIL
            r["foi_postal"] = ADDR
            r["website"] = WEBSITE
            r["notes"] = note
            found = True
            break
    if not found:
        rows.append(
            {
                "entity_id": ENTITY,
                "name_nl": "Résidence Les Buissons (Spa / Château Sous Bois)",
                "name_fr": "Résidence Les Buissons SRL (Spa / Château Sous Bois)",
                "name_en": (
                    "Les Buissons nursing home Spa (BV/SRL; Korian / "
                    "Château Sous Bois path)"
                ),
                "level": "other",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": WEBSITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": note,
            }
        )
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("entities", "updated" if found else "created", ENTITY)


def close_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: {RQ} status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = (
                "leftover dual — Les Buissons Spa YE2025 Medium"
            )
            r["instructions"] = (
                f"Completed leftover Les Buissons Spa / Château Sous Bois "
                f"YE2025 Medium CW; KBO {KBO}; omzet JUMP {OMZET} bruto DROP "
                f"{BRUTO} pnl LOSS WIDEN {PNL} equity DROP {EQUITY} FTE {FTE}; "
                f"FOI {GAP}; 1 VE NACE 87.301 Korian path; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Les Buissons Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"bruto DROP {BRUTO/1e6:.2f}m pnl LOSS WIDEN {PNL/1e6:.2f}m "
                f"equity DROP {EQUITY/1e6:.2f}m FTE {FTE}; FOI ready; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; "
                f"next every-10 2120"
            )
            found = True
    if not found:
        raise SystemExit(f"{RQ} missing")
    if not any(r["task_id"] == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after Les Buissons — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Les Buissons Spa YE2025 Medium. "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if "
                    "TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Les Buissons; "
                    "FARO/AIESH/REW still YE2024; next every-10 2120"
                ),
            }
        )
        print("spawned", NEXT_RQ)
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("research_queue closed", RQ)


def write_loop_state():
    with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "state_id",
                "mode",
                "current_sprint",
                "last_tick_utc",
                "last_unit_id",
                "ticks_completed",
                "paused",
                "notes",
            ],
            lineterminator="\n",
        )
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
                    f"tick{TICK} leftover Les Buissons Spa {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m "
                    f"pnl LOSS WIDEN {PNL/1e6:.2f}m equity DROP "
                    f"{EQUITY/1e6:.2f}m FTE {FTE}; assets/debt Unknown; 1 VE "
                    f"NACE 87.301 Korian/Château Sous Bois path); AGB Bornem "
                    f"JR2024; FARO/AIESH/REW YE2024; Résidence 3/Elisabeth Aan "
                    f"Zee/XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/"
                    f"INTRADEL/ORES SC taken; next {NEXT_RQ}; next every-10 "
                    f"2120; continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} Les Buissons Spa (omzet JUMP 4.75m / pnl LOSS WIDEN -0.29m / equity DROP / Medium)

- Unit: **{RQ}** leftover dual after **rq_2113 Résidence 3 Bruxelles**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred unused **Les Buissons / Château Sous Bois Spa** YE2025 (KBO **{KBO}**; Chemin Sous-Bois 22 Spa; **BV/SRL** NACE **87.301** / **1 VE**; **Korian Belgium** bestuurder/gedelegeerd **0869.769.702** path). Do not redo Résidence 3/Elisabeth Aan Zee/XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL/ORES SC/Korian holding/Comnexio/SLG*/Always Home/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +1.00%; bruto **EUR{BRUTO}** DROP −1.34%; pnl **LOSS EUR{PNL}** LOSS WIDEN −628.78% vs YE2024 LOSS EUR{PNL_PRIOR}; equity **EUR{EQUITY}** DROP −63.58% vs YE2024 EUR{EQUITY_PRIOR}; FTE **{FTE}** (YoY Unknown); neerlegging **28.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.8); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2114/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2110**; next **2120**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print("log appended")


def main():
    draft = FOI_DRAFT / f"{GAP}.md"
    if not draft.exists():
        raise SystemExit(f"missing FOI draft {draft}")

    with (DATA / "research_queue.csv").open(encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            if r["task_id"] == RQ and (r.get("status") or "").lower() not in (
                "open",
                "in_progress",
            ):
                raise SystemExit(f"RACE early: {RQ} status={r.get('status')}")

    upsert_entity()
    append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_les_buissons_jr2025_cw_nl",
                "title": "Companyweb NL — Les Buissons Spa YE2025",
                "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL} "
                    f"FTE {FTE}"
                ),
            },
            {
                "source_id": "src_les_buissons_jr2025_cw_en",
                "title": "Companyweb EN — Les Buissons Spa YE2025",
                "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; filed 28.07.2026; equity {EQUITY}; FTE {FTE}; "
                    "last BS year 2025"
                ),
            },
            {
                "source_id": "src_les_buissons_jr2025_cw_fr",
                "title": "Companyweb FR — Les Buissons Spa YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_les_buissons_kbo_{TICK}",
                "title": f"KBO — Les Buissons {KBO}",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
                    f"?ondernemingsnummer={KBO_DIGITS}"
                ),
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief BV 1 VE; NACE 87.301 ROB; zetel {ADDR}; "
                    f"bestuurder/gedelegeerd Korian Belgium 0869.769.702; "
                    f"FOI {EMAIL}; Strong"
                ),
            },
            {
                "source_id": f"src_les_buissons_contact_{TICK}",
                "title": "Les Buissons / Château Sous Bois / Korian FOI contact",
                "url": WEBSITE,
                "publisher": "Korian Belgium / Château Sous Bois",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; {EMAIL}; KBO email empty; postal {ADDR}; "
                    f"site {WEBSITE}"
                ),
            },
        ],
    )
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_les_buissons_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope MRS BV)",
                "source_id": "src_les_buissons_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +1.00% vs YE2024 {OMZET_PRIOR}",
            },
            {
                "budget_id": "bud_les_buissons_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_les_buissons_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP −1.34% vs YE2024 {BRUTO_PRIOR}",
            },
            {
                "budget_id": "bud_les_buissons_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_les_buissons_jr2025_cw_en",
                "confidence": "medium",
                "notes": (
                    f"tick{TICK}; LOSS WIDEN −628.78% vs YE2024 LOSS {PNL_PRIOR}"
                ),
            },
            {
                "budget_id": "bud_les_buissons_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_les_buissons_jr2025_cw_en",
                "confidence": "medium",
                "notes": (
                    f"tick{TICK}; DROP −63.58% vs YE2024 {EQUITY_PRIOR}"
                ),
            },
            {
                "budget_id": "bud_les_buissons_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_les_buissons_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE} (YoY Unknown)",
            },
        ],
    )
    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Les Buissons Spa YE2025 leftover dual "
                    "(omzet 4.75m / pnl LOSS WIDEN / equity DROP)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "MRS residents / care users Spa (1 VE)",
                "legal_basis": (
                    f"BV/SRL maison de repos ROB (KBO {KBO}; NACE 87.301; "
                    "1 VE; Korian Belgium bestuurder/gedelegeerd)"
                ),
                "decision_date": "2026-07-28",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/{SLUG}",
                "stated_goal": (
                    "Public-interest nursing-home care (Les Buissons / "
                    "Château Sous Bois / Korian path; AVIQ-adjacent)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain LOSS WIDEN vs "
                    "equity DROP −63.58% at flat omzet; map AVIQ/INAMI vs "
                    "omzet split; dual Korian holding / Château Sous Bois brand"
                ),
                "source_id": "src_les_buissons_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Wallonie>Spa>Les_Buissons_Chateau_Sous_Bois>"
                    "JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt "
                    "Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not "
                    "TE-additive of 348bn; DISTINCT Résidence 3/Elisabeth Aan "
                    "Zee/XXe Août/Ninove; dual Korian Belgium"
                ),
            }
        ],
    )
    append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": (
                    "Les Buissons Spa omzet 4.75m / pnl LOSS WIDEN −0.29m / "
                    "equity DROP −63.6% (YE2025)"
                ),
                "level": "L5",
                "type": "mrs_statutory_bv_korian_path",
                "hierarchy_path": (
                    "Wallonie>Spa>Les_Buissons_Chateau_Sous_Bois>JR2025"
                ),
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} JUMP +1.00% (primary); bruto {BRUTO} "
                    f"DROP −1.34%; pnl LOSS {PNL} WIDEN −628.78% vs LOSS "
                    f"{PNL_PRIOR}; equity {EQUITY} DROP −63.58%; FTE {FTE}; "
                    "assets/debt Unknown pending NBB PDF; Korian/Château Sous "
                    "Bois path"
                ),
                "confidence": "medium",
                "source_id": "src_les_buissons_jr2025_cw_en",
                "beneficiaries": "MRS residents / care users Spa (1 VE)",
                "stated_goal": (
                    "Public-interest nursing-home care (Korian / Château Sous "
                    "Bois path)"
                ),
                "measured_outcome": (
                    "omzet JUMP +1.00%; bruto DROP −1.34%; pnl LOSS WIDEN "
                    f"−628.78%; equity DROP −63.58%; FTE {FTE}"
                ),
                "absurdity_score": "7.4",
                "cost_score": "4.6",
                "difficulty": "3.5",
                "priority_index": "5.8",
                "cut_proposal": (
                    "FOI NBB PDF + AVIQ/INAMI split + explain equity DROP −63.58% "
                    "and LOSS WIDEN at near-flat omzet; dual Korian holding"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW "
                    "still YE2024; DISTINCT Résidence 3/XXe Août; dual Korian"
                ),
            }
        ],
    )
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Spa>Les_Buissons_Chateau_Sous_Bois>"
            "NBB_PDF_assets_debt_pnl_loss_widen_equity_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); LOSS WIDEN "
            "vs equity DROP path; AVIQ/INAMI vs omzet split; dual Korian holding "
            "/ Château Sous Bois branding"
        ),
        "why_it_matters": (
            "Medium CW shows 4.75m omzet Spa MRS BV with LOSS WIDEN to −0.29m "
            "(−629% vs YE2024) and equity DROP to 0.17m (−64%) at near-flat "
            "omzet — care-margin / solvency transparency gap on AVIQ-adjacent "
            "Korian path"
        ),
        "priority": "8",
        "recipient_body": "Résidence Les Buissons BV / Korian Belgium / Château Sous Bois",
        "recipient_email": EMAIL,
        "recipient_postal": ADDR,
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
        "notes": (
            f"tick{TICK}; human-send only; Medium CW; next every-10 2120"
        ),
    }
    append_rows(DATA / "foi_queue.csv", [foi_row])
    close_queue()
    write_loop_state()
    append_log()
    print("DONE tick", TICK)


if __name__ == "__main__":
    main()
