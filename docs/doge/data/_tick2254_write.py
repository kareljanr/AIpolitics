# tick 2254 — Atelier Cambier Charleroi/Jumet YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2254
UTC = "2026-08-27T05:40:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_atelier_cambier_charleroi"
KBO = "0401.571.189"
KBO_BARE = "0401571189"
SRC_EN = "src_cambier_jr2025_cw_en"
GAP = "gap_cambier_nbb_pdf_assets_debt_omzet_drop_18pct_equity_jump_47pct_eta_matrix_l5"
COMM = "comm_cambier_jr2025_statutory_eta_omzet_drop_equity_jump"
LB = "lb_cambier_omzet_8_84m_drop_18pct_equity_jump_47pct_jr2025"
RQ = "rq_2254"
RQ_NEXT = "rq_2255"

OMZET = 8842156
OMZET24 = 10773196
BRUTO = 7841647
BRUTO24 = 8270293
PNL = 287015
PNL24 = 297724
EQUITY = 803999
EQUITY24 = 547703
FTE = 213.1
RATIO = round(BRUTO / OMZET, 2)
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / PNL24 * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)


def append_csv(path: Path, rows: list[dict]):
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        existing = list(reader)
    id_key = fieldnames[0]
    ids = {r[id_key] for r in existing}
    new = [r for r in rows if r[id_key] not in ids]
    if not new:
        print(f"skip {path.name}")
        return
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        for r in new:
            w.writerow({k: r.get(k, "") for k in fieldnames})
    print(f"appended {len(new)} -> {path.name}")


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            found = True
            r["status"] = "done"
            r["title"] = (
                "leftover dual — Atelier Cambier YE2025 Medium "
                f"(omzet DROP 8.84m / {OMZET_PCT}% / equity JUMP +{EQUITY_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Cambier ASBL Jumet/Charleroi {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet DROP {OMZET} ({OMZET_PCT}% vs {OMZET24}); bruto DROP {BRUTO} ({BRUTO_PCT}%; bruto/omzet ~{RATIO}x); "
                f"pnl DROP {PNL} ({PNL_PCT}%); equity JUMP {EQUITY} (+{EQUITY_PCT}%); FTE {FTE}; 1 VE; NACE 88.993; "
                f"neerlegging 16.06.2026; assets/debt Unknown; FOI {GAP} ready NOT sent; "
                f"stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024; "
                f"after Gaillettes@2253; deferred FREE Corelap YE2025; next EVERY-10 2260"
            )
            r["instructions"] = (
                "leftover dual Atelier Cambier YE2025 FREE Walloon ETA after Gaillettes; "
                "preferred AGB/FARO/AIESH/REW still YE2024; Relais Haute Sambre still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Cambier — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Atelier Cambier YE2025 Medium "
                    f"(omzet DROP 8.84m / {OMZET_PCT}% / equity JUMP +{EQUITY_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. Corelap YE2025 FREE deferred; "
                    "skip Cambier/Gaillettes/Hunelle/Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/"
                    "TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/"
                    "ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers de Tertre/Le Rucher/"
                    "Het Rekreatief/Travie/SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/"
                    "Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; Relais Haute Sambre/Sipres/APN still YE2024). "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2260."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Cambier; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Relais Haute Sambre YE2024; deferred FREE Corelap; next every-10 2260"
                ),
            }
        )
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("research_queue updated")


def write_loop_state():
    path = DATA / "loop_state.csv"
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    rows[0].update(
        {
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": RQ,
            "ticks_completed": str(TICK),
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover Cambier {KBO} Medium (omzet DROP {OMZET} {OMZET_PCT}%; "
                f"equity JUMP {EQUITY} +{EQUITY_PCT}%; bruto {BRUTO} ~{RATIO}x; pnl {PNL}; FTE {FTE}; 1 VE Jumet ETA); "
                f"after Gaillettes@2253; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024; "
                f"deferred FREE Corelap; next {RQ_NEXT}; next EVERY-10 2260; continuous hole_fill"
            ),
        }
    )
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("loop_state updated")


def write_foi_draft():
    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — Atelier Cambier (NBB PDF / omzet DROP {OMZET_PCT}% / equity JUMP +{EQUITY_PCT}%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Atelier Cambier ASBL — KBO **{KBO}** (Actief; Zoning Industriel-1ère rue SN, 6040 Charleroi/Jumet; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Charleroi)  
**recipient:** courrier@ateliercambier.be · Zoning Industriel-1ère rue SN, 6040 Charleroi  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.ateliercambier.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL Atelier Cambier; **1 VE**; zetel Jumet/Charleroi; NACE **88.993** (+88.995); replaces 0407.792.750.
- CW YE2025: omzet **EUR{OMZET:,}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** DROP {BRUTO_PCT}% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP {PNL_PCT}%; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}% vs YE2024 EUR{EQUITY24:,}; FTE **{FTE}**; filed **16.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024. After Gaillettes@2253. Deferred FREE Corelap.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Atelier Cambier ASBL
via courrier@ateliercambier.be
Zoning Industriel-1ère rue SN, 6040 Charleroi
Objet: Publicité des comptes annuels 2025 Atelier Cambier (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OMZET} / marge brute EUR{BRUTO} (~{RATIO}x).
3. Omzet DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24} — réconciliation avec equity JUMP +{EQUITY_PCT}% et FTE {FTE}.
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition coûts activités Jumet / Parc d'activités économiques.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )
    print("foi draft written")


def append_log():
    with LOG.open("a", encoding="utf-8") as f:
        f.write(
            f"""

## Tick {TICK} - {UTC} - rq_2254 Atelier Cambier Charleroi (omzet DROP 8.84m / {OMZET_PCT}% / equity JUMP +{EQUITY_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2254** leftover dual after **rq_2253 Gaillettes**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre still **YE2024**; Sipres/APN still **YE2024**. Took named FREE Walloon ETA **Atelier Cambier ASBL** YE2025 (KBO **{KBO}**; Zoning Industriel Jumet/Charleroi; **Actief** **1 VE**; NACE **88.993** AViQ). Deferred FREE Corelap YE2025. Do not redo Gaillettes/Hunelle/Dauphins/Saupont stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** DROP {BRUTO_PCT}% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL}** DROP {PNL_PCT}%; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}% vs YE2024 EUR{EQUITY24}; FTE **{FTE}**; neerlegging **16.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via courrier@ateliercambier.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.30); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2254=done + rq_2255 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2254/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2250**; next **2260**). Next: rq_2255 (AGB/FARO-if-YE2025 / AIESH-REW / unused Corelap).
"""
        )
    print("loop_log appended")


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_cambier_jr2025_cw_nl",
                "title": "Companyweb NL Atelier Cambier YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet DROP {OMZET} pnl {PNL} equity JUMP {EQUITY} "
                    f"bruto {BRUTO} FTE {FTE}; neerlegging 16.06.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2254/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Atelier Cambier YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 16-06-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_cambier_jr2025_cw_fr",
                "title": "Companyweb FR Atelier Cambier YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Bénéfice {PNL}",
            },
            {
                "source_id": f"src_cambier_kbo_{TICK}",
                "title": f"KBO Atelier Cambier {KBO} Actief Charleroi/Jumet 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW/ASBL Atelier Cambier; zetel Zoning Industriel-1ère rue SN 6040 Charleroi "
                    f"(Parc Jumet); 1 VE; NACE 88.993/88.995; begindatum 25.11.1964; replaces 0407.792.750; KBO email empty"
                ),
            },
            {
                "source_id": f"src_cambier_site_contact_{TICK}",
                "title": "Atelier Cambier FOI channel courrier@ateliercambier.be",
                "url": "https://www.ateliercambier.be/",
                "publisher": "Atelier Cambier ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; courrier@ateliercambier.be / c.garbo@ateliercambier.be; "
                    "Zoning Industriel Jumet 6040 Charleroi; also leseta.be annuaire"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_cambier_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW statutory omzet YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet DROP {OMZET_PCT}% vs YE2024 {OMZET24} (primary envelope)",
            },
            {
                "budget_id": "bud_cambier_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto DROP {BRUTO_PCT}%; bruto/omzet ~{RATIO}x (bruto < omzet)",
            },
            {
                "budget_id": "bud_cambier_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl DROP {PNL_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_cambier_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW statutory eigen_vermogen YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; equity JUMP +{EQUITY_PCT}% vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_cambier_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": f"CW social-balance FTE {FTE}",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; FTE {FTE}; YE2024 FTE Unknown on CW page; assets/debt Unknown",
            },
            {
                "budget_id": "bud_cambier_omzet_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(OMZET24),
                "amount_min_eur": str(OMZET24),
                "amount_max_eur": str(OMZET24),
                "basis": "CW statutory omzet YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 omzet {OMZET24} comparative (pre DROP -18%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Atelier Cambier YE2025 leftover dual "
                    f"(omzet DROP 8.84m / {OMZET_PCT}% / equity JUMP +{EQUITY_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Charleroi-Jumet / AVIQ adapted-work public path",
                "legal_basis": f"ASBL ETA Atelier Cambier (KBO {KBO}; Actief; 1 VE; NACE 88.993; Charleroi/Jumet)",
                "decision_date": "2026-06-16",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET24},'
                    f'"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "stated_goal": "Walloon ETA industrial subcontracting Jumet",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; reconcile omzet DROP -18% vs equity JUMP +47%; "
                    "disclose AVIQ ETA subsidy matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Hainaut>Charleroi>Cambier>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; equity JUMP {EQUITY}; "
                    f"FTE {FTE}; 1 VE; after Gaillettes@2253; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": (
                    f"Atelier Cambier omzet DROP 8.84m / {OMZET_PCT}% / equity JUMP +{EQUITY_PCT}% / "
                    f"FTE {FTE} (YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Hainaut>Charleroi>Cambier>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW omzet DROP {OMZET} ({OMZET_PCT}%) / bruto {BRUTO} (~{RATIO}x) / pnl {PNL} / "
                    f"equity JUMP {EQUITY} (+{EQUITY_PCT}%) / FTE {FTE} / 1 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Charleroi-Jumet / AVIQ adapted-work public path",
                "stated_goal": "Walloon ETA industrial subcontracting Jumet",
                "measured_outcome": (
                    f"omzet DROP {OMZET_PCT}%; bruto DROP {BRUTO_PCT}%; pnl DROP {PNL_PCT}%; "
                    f"equity JUMP +{EQUITY_PCT}%; FTE {FTE}; filed 16.06.2026"
                ),
                "absurdity_score": "7.5",
                "cost_score": "5.2",
                "difficulty": "3.0",
                "priority_index": "6.30",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
                    "reconcile omzet DROP -18% vs equity JUMP +47%"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Gaillettes@2253; deferred FREE Corelap"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Atelier Cambier VZW (Charleroi-Jumet / ETA maatwerk Henegouwen)",
                "name_fr": "Atelier Cambier ASBL (Charleroi-Jumet / entreprise de travail adapté Hainaut)",
                "name_en": "Atelier Cambier adapted-work ASBL (Charleroi Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.ateliercambier.be/",
                "foi_email": "courrier@ateliercambier.be",
                "foi_postal": "Zoning Industriel-1ère rue SN, 6040 Charleroi",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet DROP {OMZET} ({OMZET_PCT}%) bruto {BRUTO} (~{RATIO}x) pnl {PNL} equity JUMP {EQUITY} "
                    f"(+{EQUITY_PCT}%) FTE {FTE}; neerlegging 16.06.2026; assets/debt Unknown; FOI {GAP}; "
                    "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024; "
                    "after Gaillettes@2253; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Wallonie>Hainaut>Charleroi>Cambier>NBB_PDF_assets_debt_omzet_drop_equity_jump",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OMZET} "
                    f"DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto EUR{BRUTO} (~{RATIO}x); "
                    f"equity JUMP EUR{EQUITY} (+{EQUITY_PCT}%); FTE {FTE}; AVIQ ETA subsidy matrix"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (omzet DROP 8.84m / {OMZET_PCT}% / equity JUMP +{EQUITY_PCT}% / "
                    f"FTE {FTE}) under AVIQ path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Atelier Cambier ASBL",
                "recipient_email": "courrier@ateliercambier.be",
                "recipient_postal": "Zoning Industriel-1ère rue SN, 6040 Charleroi",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": DATE,
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/REW YE2024; "
                    "AGB Bornem JR2024; Relais Haute Sambre YE2024; after Gaillettes@2253; next EVERY-10 2260"
                ),
            }
        ],
    )

    write_foi_draft()
    update_research_queue()
    write_loop_state()
    append_log()
    print("DONE tick", TICK)


if __name__ == "__main__":
    main()
