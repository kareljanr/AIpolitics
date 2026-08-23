# -*- coding: utf-8 -*-
"""Apply tick 2115 — Les Sittelles Chastre (Korian) YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
FOI_DRAFT = ROOT / "foi" / "drafts"
csv.field_size_limit(10**7)

UTC = "2026-08-25T09:10:00Z"
TICK = 2115
RQ = "rq_2115"
NEXT_RQ = "rq_2116"
ENTITY = "nv_les_sittelles_chastre"
GAP = "gap_les_sittelles_nbb_pdf_assets_debt_pnl_flip_loss_matrix_l5"
KBO = "0451.031.489"
KBO_DIGITS = "0451031489"
OMZET = 3020109
BRUTO = 2618231
PNL = -44666
EQUITY = 2486382
FTE = 38.7
OMZET_PRIOR = 3023930
PNL_PRIOR = 75980
BRUTO_PRIOR = 2572622
EQUITY_PRIOR = 2531047
EMAIL = "info@lessittelles.be"
ADDR = "Route Provinciale 121, 1450 Chastre"
WEBSITE = (
    "https://www.korian.be/fr/maisons-de-repos/les-sittelles/"
    "maison-de-repos-les-sittelles/"
)
LB = "lb_les_sittelles_omzet_3_02m_pnl_flip_loss_jr2025"
COMM = "comm_les_sittelles_jr2025_statutory_mrs"
SLUG = "les-sittelles"

DO_NOT_REDO = (
    "Do NOT redo Les Sittelles Chastre, Les Buissons / Château Sous Bois Spa, "
    "Résidence 3 / Saphir, Elisabeth Aan Zee Oostende, Maison de Repos du "
    "XXe Août / PLIMCO, Rusthuis Sint Jozef Ninove, WZC Zilverlinde Olen, "
    "Woonzorgcentrum Sint-Camillus Wevelgem, IDELUX Développement, IDELUX "
    "Projets Publics, IDELUX Eau, IDELUX Finances, IDELUX Environnement, "
    "INTRADEL, Korian Belgium, Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, "
    "Always Home, SLG Operaties, SLG Wallonie, AREWAL, HYGEA, BEP Environnement, "
    "AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, "
    "IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, Aquafin, "
    "AGB Bornem, Armonea, Colisée Belgium, Familiezorg Gent, emeis, IRE*, "
    "FANC, SCK CEN, Veilige Have, Molenheide, WZC Sint-Jozef Rumst, Cassiers, "
    "OLV Roosdaal, De Verlosser Dilbeek, WZC De Foyer Gent."
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
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief NV/SA "
        f"1 VE NACE 87.101/87.301 RVT+ROB (Chastre); omzet DROP {OMZET/1e6:.2f}m "
        f"(−0.13%) bruto JUMP {BRUTO/1e6:.2f}m (+1.77%) pnl FLIP LOSS "
        f"{PNL/1e6:.2f}m (−158.79% vs YE2024 PROFIT {PNL_PRIOR}) equity DROP "
        f"{EQUITY/1e6:.2f}m (−1.76%) FTE {FTE} (YoY Unknown); assets/debt "
        f"Unknown; neerlegging 28.07.2026; FOI {GAP}; Korian Belgium "
        f"bestuurder/gedelegeerd 0869.769.702 path; preferred AGB Bornem "
        f"JR2024; FARO/AIESH/REW YE2024; DISTINCT Les Buissons/Résidence 3/"
        f"Elisabeth Aan Zee/XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/"
        f"INTRADEL; Charmilles Sambreville/La Charmille deferred"
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
                "name_nl": "Les Sittelles (Chastre)",
                "name_fr": "Les Sittelles SA (Chastre)",
                "name_en": (
                    "Les Sittelles nursing home Chastre (NV/SA; Korian path)"
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
            r["title"] = "leftover dual — Les Sittelles Chastre YE2025 Medium"
            r["instructions"] = (
                f"Completed leftover Les Sittelles Chastre YE2025 Medium CW; "
                f"KBO {KBO}; omzet DROP {OMZET} bruto JUMP {BRUTO} pnl FLIP "
                f"LOSS {PNL} equity DROP {EQUITY} FTE {FTE}; FOI {GAP}; 1 VE "
                f"NACE 87.101/87.301 Korian path; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Les Sittelles Medium omzet DROP {OMZET/1e6:.2f}m "
                f"bruto JUMP {BRUTO/1e6:.2f}m pnl FLIP LOSS {PNL/1e6:.2f}m "
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
                    "leftover dual hole-fill after Les Sittelles — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/Charmilles-LaCharmille/unused "
                    "IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Les Sittelles Chastre YE2025 Medium. "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if "
                    "TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "Residence Les Charmilles Sambreville (0457.649.265) / "
                    "La Charmille Pont-à-Celles (0416.116.637) / other "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Les Sittelles; "
                    "FARO/AIESH/REW still YE2024; Charmilles/La Charmille "
                    "YE2025 deferred; next every-10 2120"
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
                    f"tick{TICK} leftover Les Sittelles Chastre {KBO} Medium CW "
                    f"(omzet DROP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                    f"pnl FLIP LOSS {PNL/1e6:.2f}m equity DROP "
                    f"{EQUITY/1e6:.2f}m FTE {FTE}; assets/debt Unknown; 1 VE "
                    f"NACE 87.101/87.301 Korian path); AGB Bornem JR2024; "
                    f"FARO/AIESH/REW YE2024; Les Buissons/Résidence 3/Elisabeth "
                    f"Aan Zee/XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/"
                    f"INTRADEL/ORES SC taken; Charmilles/La Charmille deferred; "
                    f"next {NEXT_RQ}; next every-10 2120; continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} Les Sittelles Chastre (omzet DROP 3.02m / pnl FLIP LOSS -45k / Medium)

- Unit: **{RQ}** leftover dual after **rq_2114 Les Buissons Spa**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Les Sittelles Chastre** YE2025 (KBO **{KBO}**; Route Provinciale 121 Chastre; **NV/SA** NACE **87.101/87.301** / **1 VE**; **Korian Belgium** bestuurder/gedelegeerd **0869.769.702** path). Do not redo Les Buissons/Résidence 3/Elisabeth Aan Zee/XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL/ORES SC/Korian holding/Comnexio/SLG*/Always Home/AGB Bornem. Charmilles Sambreville / La Charmille Pont-à-Celles YE2025 deferred.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** DROP −0.13%; bruto **EUR{BRUTO}** JUMP +1.77%; pnl **LOSS EUR{PNL}** FLIP −158.79% vs YE2024 PROFIT EUR{PNL_PRIOR}; equity **EUR{EQUITY}** DROP −1.76% vs YE2024 EUR{EQUITY_PRIOR}; FTE **{FTE}** (YoY Unknown); neerlegging **28.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL} (alt info@korian.be).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.3); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2115/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2110**; next **2120**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Charmilles-LaCharmille / unused IGS-DSO-WZC-MRS).
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
                "source_id": "src_les_sittelles_jr2025_cw_nl",
                "title": "Companyweb NL — Les Sittelles Chastre YE2025",
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
                "source_id": "src_les_sittelles_jr2025_cw_en",
                "title": "Companyweb EN — Les Sittelles Chastre YE2025",
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
                "source_id": "src_les_sittelles_jr2025_cw_fr",
                "title": "Companyweb FR — Les Sittelles Chastre YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_les_sittelles_kbo_{TICK}",
                "title": f"KBO — Les Sittelles {KBO}",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
                    f"?ondernemingsnummer={KBO_DIGITS}"
                ),
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief NV 1 VE; NACE 87.101/87.301; zetel {ADDR}; "
                    f"bestuurder/gedelegeerd Korian Belgium 0869.769.702; "
                    f"FOI {EMAIL}; Strong"
                ),
            },
            {
                "source_id": f"src_les_sittelles_contact_{TICK}",
                "title": "Les Sittelles / Korian FOI contact",
                "url": WEBSITE,
                "publisher": "Korian Belgium / Les Sittelles",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; {EMAIL}; alt info@korian.be; KBO email empty; "
                    f"postal {ADDR}; site {WEBSITE}"
                ),
            },
        ],
    )
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_les_sittelles_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope MRS NV)",
                "source_id": "src_les_sittelles_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP −0.13% vs YE2024 {OMZET_PRIOR}",
            },
            {
                "budget_id": "bud_les_sittelles_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_les_sittelles_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +1.77% vs YE2024 {BRUTO_PRIOR}",
            },
            {
                "budget_id": "bud_les_sittelles_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_les_sittelles_jr2025_cw_en",
                "confidence": "medium",
                "notes": (
                    f"tick{TICK}; FLIP LOSS −158.79% vs YE2024 PROFIT {PNL_PRIOR}"
                ),
            },
            {
                "budget_id": "bud_les_sittelles_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_les_sittelles_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP −1.76% vs YE2024 {EQUITY_PRIOR}",
            },
            {
                "budget_id": "bud_les_sittelles_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_les_sittelles_jr2025_cw_en",
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
                    "Les Sittelles Chastre YE2025 leftover dual "
                    "(omzet 3.02m / pnl FLIP LOSS)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "MRS residents / care users Chastre (1 VE)",
                "legal_basis": (
                    f"NV/SA maison de repos RVT/ROB (KBO {KBO}; NACE "
                    "87.101/87.301; 1 VE; Korian Belgium bestuurder/gedelegeerd)"
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
                    "Public-interest nursing-home care (Les Sittelles / "
                    "Korian path; AVIQ-adjacent)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain pnl FLIP LOSS vs "
                    "flat omzet; map AVIQ/INAMI vs omzet split; dual Korian "
                    "holding"
                ),
                "source_id": "src_les_sittelles_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Wallonie>Chastre>Les_Sittelles>JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt "
                    "Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not "
                    "TE-additive of 348bn; DISTINCT Les Buissons/Résidence 3/"
                    "Elisabeth Aan Zee/XXe Août; dual Korian Belgium"
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
                    "Les Sittelles Chastre omzet 3.02m / pnl FLIP LOSS −45k "
                    "(YE2025)"
                ),
                "level": "L5",
                "type": "mrs_statutory_nv_korian_path",
                "hierarchy_path": "Wallonie>Chastre>Les_Sittelles>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} DROP −0.13% (primary); bruto {BRUTO} "
                    f"JUMP +1.77%; pnl LOSS {PNL} FLIP −158.79% vs PROFIT "
                    f"{PNL_PRIOR}; equity {EQUITY} DROP −1.76%; FTE {FTE}; "
                    "assets/debt Unknown pending NBB PDF; Korian path"
                ),
                "confidence": "medium",
                "source_id": "src_les_sittelles_jr2025_cw_en",
                "beneficiaries": "MRS residents / care users Chastre (1 VE)",
                "stated_goal": (
                    "Public-interest nursing-home care (Korian / Les Sittelles "
                    "path)"
                ),
                "measured_outcome": (
                    "omzet DROP −0.13%; bruto JUMP +1.77%; pnl FLIP LOSS "
                    f"−158.79%; equity DROP −1.76%; FTE {FTE}"
                ),
                "absurdity_score": "7.0",
                "cost_score": "4.0",
                "difficulty": "3.5",
                "priority_index": "5.3",
                "cut_proposal": (
                    "FOI NBB PDF + AVIQ/INAMI split + explain pnl FLIP LOSS at "
                    "near-flat omzet; dual Korian holding"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW "
                    "still YE2024; DISTINCT Les Buissons/Résidence 3; dual Korian"
                ),
            }
        ],
    )
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Chastre>Les_Sittelles>"
            "NBB_PDF_assets_debt_pnl_flip_loss"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl FLIP "
            "LOSS path; AVIQ/INAMI vs omzet split; dual Korian holding"
        ),
        "why_it_matters": (
            "Medium CW shows 3.02m omzet Chastre MRS NV with pnl FLIP to −45k "
            "(−159% vs YE2024 profit) at near-flat omzet — care-margin "
            "transparency gap on AVIQ-adjacent Korian path"
        ),
        "priority": "8",
        "recipient_body": "Les Sittelles NV / Korian Belgium",
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
        "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2120",
    }
    append_rows(DATA / "foi_queue.csv", [foi_row])
    close_queue()
    write_loop_state()
    append_log()


if __name__ == "__main__":
    main()
