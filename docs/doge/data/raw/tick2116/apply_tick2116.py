# -*- coding: utf-8 -*-
"""Apply tick 2116 — Residence Les Charmilles Sambreville (Korian) YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
FOI_DRAFT = ROOT / "foi" / "drafts"
csv.field_size_limit(10**7)

UTC = "2026-08-25T09:25:00Z"
TICK = 2116
RQ = "rq_2116"
NEXT_RQ = "rq_2117"
ENTITY = "nv_residence_les_charmilles_sambreville"
GAP = "gap_charmilles_sambreville_nbb_pdf_assets_debt_pnl_drop_near_zero_matrix_l5"
KBO = "0457.649.265"
KBO_DIGITS = "0457649265"
OMZET = 4947053
BRUTO = 4339210
PNL = 951
EQUITY = 2426790
FTE = 66.2
OMZET_PRIOR = 4779552
PNL_PRIOR = 49117
BRUTO_PRIOR = 4196807
EQUITY_PRIOR = 2425839
EMAIL = "info@lescharmilles.be"
ADDR = "Rue d'Eghezée(AUV) 54, 5060 Sambreville"
WEBSITE = (
    "https://www.korian.be/fr/maisons-de-repos/les-charmilles/"
    "maison-de-repos-les-charmilles/"
)
LB = "lb_charmilles_omzet_4_95m_pnl_drop_near_zero_jr2025"
COMM = "comm_charmilles_jr2025_statutory_mrs"
SLUG = "residence-les-charmilles"

DO_NOT_REDO = (
    "Do NOT redo Residence Les Charmilles Sambreville, Les Sittelles Chastre, "
    "Les Buissons / Château Sous Bois Spa, Résidence 3 / Saphir, Elisabeth Aan "
    "Zee Oostende, Maison de Repos du XXe Août / PLIMCO, Rusthuis Sint Jozef "
    "Ninove, WZC Zilverlinde Olen, Woonzorgcentrum Sint-Camillus Wevelgem, "
    "IDELUX Développement, IDELUX Projets Publics, IDELUX Eau, IDELUX Finances, "
    "IDELUX Environnement, INTRADEL, Korian Belgium, Comnexio, ORES SC, ORES "
    "Assets, SLG Vlaanderen, Always Home, SLG Operaties, SLG Wallonie, AREWAL, "
    "HYGEA, BEP Environnement, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, "
    "Synergrid, Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, "
    "CILE, SWDE, Aquafin, AGB Bornem, Armonea, Colisée Belgium, Familiezorg "
    "Gent, emeis, IRE*, FANC, SCK CEN, Veilige Have, Molenheide, WZC Sint-Jozef "
    "Rumst, Cassiers, OLV Roosdaal, De Verlosser Dilbeek, WZC De Foyer Gent."
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
        f"1 VE NACE 87.101/87.301 RVT+ROB (Sambreville/Auvelais); omzet JUMP "
        f"{OMZET/1e6:.2f}m (+3.5%) bruto JUMP {BRUTO/1e6:.2f}m (+3.39%) pnl "
        f"DROP {PNL} (−98.06% vs YE2024 {PNL_PRIOR} near-zero) equity JUMP "
        f"{EQUITY/1e6:.2f}m (+0.04%) FTE {FTE} (YoY Unknown); assets/debt "
        f"Unknown; neerlegging 28.07.2026; FOI {GAP}; Korian Belgium "
        f"bestuurder/gedelegeerd 0869.769.702 path; preferred AGB Bornem "
        f"JR2024; FARO/AIESH/REW YE2024; DISTINCT Les Sittelles/Les Buissons/"
        f"Résidence 3/Elisabeth Aan Zee/XXe Août/Ninove/Zilverlinde/"
        f"Sint-Camillus/IDELUX*/INTRADEL; La Charmille deferred"
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
                "name_nl": "Residence Les Charmilles (Sambreville)",
                "name_fr": "Résidence Les Charmilles SA (Sambreville/Auvelais)",
                "name_en": (
                    "Residence Les Charmilles nursing home Sambreville "
                    "(NV/SA; Korian path)"
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
                "leftover dual — Residence Les Charmilles Sambreville "
                "YE2025 Medium"
            )
            r["instructions"] = (
                f"Completed leftover Residence Les Charmilles Sambreville "
                f"YE2025 Medium CW; KBO {KBO}; omzet JUMP {OMZET} bruto JUMP "
                f"{BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} FTE {FTE}; FOI "
                f"{GAP}; 1 VE NACE 87.101/87.301 Korian path; AGB Bornem "
                f"JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Charmilles Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"bruto JUMP {BRUTO/1e6:.2f}m pnl DROP {PNL} (−98%) equity "
                f"JUMP {EQUITY/1e6:.2f}m FTE {FTE}; FOI ready; AGB Bornem "
                f"JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 "
                f"2120"
            )
            found = True
    if not found:
        raise SystemExit(f"{RQ} missing")
    if not any(r["task_id"] == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after Charmilles — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/LaCharmille/unused "
                    "IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Residence Les Charmilles "
                    "Sambreville YE2025 Medium. Prefer leftover AGB/APB if "
                    "JR2025 PDF live, else FARO if TRUE NBB YE2025, else "
                    "AIESH/REW if YE2025, else unused La Charmille "
                    "Pont-à-Celles (0416.116.637) / other "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Charmilles; "
                    "FARO/AIESH/REW still YE2024; La Charmille YE2025 "
                    "deferred; next every-10 2120"
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
                    f"tick{TICK} leftover Residence Les Charmilles Sambreville "
                    f"{KBO} Medium CW (omzet JUMP {OMZET/1e6:.2f}m bruto JUMP "
                    f"{BRUTO/1e6:.2f}m pnl DROP {PNL} near-zero equity JUMP "
                    f"{EQUITY/1e6:.2f}m FTE {FTE}; assets/debt Unknown; 1 VE "
                    f"NACE 87.101/87.301 Korian path); AGB Bornem JR2024; "
                    f"FARO/AIESH/REW YE2024; Les Sittelles/Les Buissons/"
                    f"Résidence 3/Elisabeth Aan Zee/XXe Août/Ninove/"
                    f"Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL/ORES SC/"
                    f"Charmilles taken; La Charmille deferred; next {NEXT_RQ}; "
                    f"next every-10 2120; continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} Residence Les Charmilles Sambreville (omzet JUMP 4.95m / pnl DROP 951 near-zero −98% / Medium)

- Unit: **{RQ}** leftover dual after **rq_2115 Les Sittelles Chastre**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred unused **Residence Les Charmilles Sambreville** YE2025 (KBO **{KBO}**; Rue d'Eghezée(AUV) 54 Sambreville/Auvelais; **NV/SA** NACE **87.101/87.301** / **1 VE**; **Korian Belgium** bestuurder/gedelegeerd **0869.769.702** path). Do not redo Les Sittelles/Les Buissons/Résidence 3/Elisabeth Aan Zee/XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL/ORES SC/Korian holding/Comnexio/SLG*/Always Home/AGB Bornem. La Charmille Pont-à-Celles YE2025 deferred.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +3.5%; bruto **EUR{BRUTO}** JUMP +3.39%; pnl **EUR{PNL}** DROP −98.06% vs YE2024 EUR{PNL_PRIOR} (near-zero); equity **EUR{EQUITY}** JUMP +0.04% vs YE2024 EUR{EQUITY_PRIOR}; FTE **{FTE}** (YoY Unknown); neerlegging **28.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL} (alt direction@lescharmilles.be / info@korian.be).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.7); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2116/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2110**; next **2120**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / La Charmille / unused IGS-DSO-WZC-MRS).
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
                "source_id": "src_charmilles_jr2025_cw_nl",
                "title": "Companyweb NL — Residence Les Charmilles YE2025",
                "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl "
                    f"{PNL} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_charmilles_jr2025_cw_en",
                "title": "Companyweb EN — Residence Les Charmilles YE2025",
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
                "source_id": "src_charmilles_jr2025_cw_fr",
                "title": "Companyweb FR — Residence Les Charmilles YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_charmilles_kbo_{TICK}",
                "title": f"KBO — Residence Les Charmilles {KBO}",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
                    f"?ondernemingsnummer={KBO_DIGITS}"
                ),
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief NV 1 VE; NACE 87.101/87.301; zetel "
                    f"{ADDR}; bestuurder/gedelegeerd Korian Belgium "
                    f"0869.769.702; FOI {EMAIL}; Strong"
                ),
            },
            {
                "source_id": f"src_charmilles_contact_{TICK}",
                "title": "Les Charmilles / Korian FOI contact",
                "url": WEBSITE,
                "publisher": "Korian Belgium / Les Charmilles",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; {EMAIL}; alt direction@lescharmilles.be / "
                    f"info@korian.be; KBO email empty; postal {ADDR}; site "
                    f"{WEBSITE}"
                ),
            },
        ],
    )
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_charmilles_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope MRS NV)",
                "source_id": "src_charmilles_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +3.5% vs YE2024 {OMZET_PRIOR}",
            },
            {
                "budget_id": "bud_charmilles_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_charmilles_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +3.39% vs YE2024 {BRUTO_PRIOR}",
            },
            {
                "budget_id": "bud_charmilles_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_charmilles_jr2025_cw_en",
                "confidence": "medium",
                "notes": (
                    f"tick{TICK}; DROP −98.06% vs YE2024 {PNL_PRIOR} (near-zero)"
                ),
            },
            {
                "budget_id": "bud_charmilles_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_charmilles_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +0.04% vs YE2024 {EQUITY_PRIOR}",
            },
            {
                "budget_id": "bud_charmilles_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_charmilles_jr2025_cw_en",
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
                    "Residence Les Charmilles Sambreville YE2025 leftover dual "
                    "(omzet 4.95m / pnl DROP near-zero)"
                ),
                "entity_id": ENTITY,
                "beneficiary": (
                    "MRS residents / care users Sambreville-Auvelais (1 VE)"
                ),
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
                    "Public-interest nursing-home care (Les Charmilles / "
                    "Korian path; AVIQ-adjacent)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain pnl DROP −98% "
                    "near-zero vs rising omzet; map AVIQ/INAMI vs omzet split; "
                    "dual Korian holding"
                ),
                "source_id": "src_charmilles_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Wallonie>Sambreville>Les_Charmilles>JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt "
                    "Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not "
                    "TE-additive of 348bn; DISTINCT Les Sittelles/Les Buissons/"
                    "Résidence 3; dual Korian Belgium"
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
                    "Les Charmilles Sambreville omzet 4.95m / pnl DROP 951 "
                    "near-zero −98% (YE2025)"
                ),
                "level": "L5",
                "type": "mrs_statutory_nv_korian_path",
                "hierarchy_path": "Wallonie>Sambreville>Les_Charmilles>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} JUMP +3.5% (primary); bruto {BRUTO} "
                    f"JUMP +3.39%; pnl {PNL} DROP −98.06% vs {PNL_PRIOR} "
                    f"(near-zero); equity {EQUITY} JUMP +0.04%; FTE {FTE}; "
                    "assets/debt Unknown pending NBB PDF; Korian path"
                ),
                "confidence": "medium",
                "source_id": "src_charmilles_jr2025_cw_en",
                "beneficiaries": (
                    "MRS residents / care users Sambreville-Auvelais (1 VE)"
                ),
                "stated_goal": (
                    "Public-interest nursing-home care (Korian / Les Charmilles "
                    "path)"
                ),
                "measured_outcome": (
                    "omzet JUMP +3.5%; bruto JUMP +3.39%; pnl DROP −98.06% "
                    f"near-zero; equity JUMP +0.04%; FTE {FTE}"
                ),
                "absurdity_score": "7.3",
                "cost_score": "4.5",
                "difficulty": "3.5",
                "priority_index": "5.7",
                "cut_proposal": (
                    "FOI NBB PDF + AVIQ/INAMI split + explain pnl DROP −98% "
                    "near-zero at rising omzet; dual Korian holding"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW "
                    "still YE2024; DISTINCT Les Sittelles; dual Korian"
                ),
            }
        ],
    )
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Sambreville>Les_Charmilles>"
            "NBB_PDF_assets_debt_pnl_drop_near_zero"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DROP "
            "−98% near-zero path; AVIQ/INAMI vs omzet split; dual Korian holding"
        ),
        "why_it_matters": (
            "Medium CW shows 4.95m omzet Sambreville MRS NV with pnl DROP to "
            "EUR951 (−98% vs YE2024 49k) at rising omzet — care-margin "
            "transparency gap on AVIQ-adjacent Korian path"
        ),
        "priority": "8",
        "recipient_body": "Residence Les Charmilles NV / Korian Belgium",
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
