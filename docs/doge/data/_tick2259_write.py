# tick 2259 — Les Erables (C.A.V.A.) Tournai YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2259
UTC = "2026-08-27T06:55:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_les_erables_tournai"
KBO = "0445.138.245"
KBO_BARE = "0445138245"
SRC_EN = "src_erables_jr2025_cw_en"
GAP = "gap_erables_nbb_pdf_assets_debt_pnl_drop_89pct_fte_drop_eta_matrix_l5"
COMM = "comm_erables_jr2025_statutory_eta_omzet_pnl_drop_89pct"
LB = "lb_erables_omzet_4_63m_pnl_drop_89pct_fte_180_jr2025"
RQ = "rq_2259"
RQ_NEXT = "rq_2260"

OMZET = 4627233
OMZET24 = 5073655
BRUTO = 6698079
BRUTO24 = 7093412
PNL = 50897
PNL24 = 480586
EQUITY = 12024460
EQUITY24 = 12038760
FTE = 180.1
FTE24 = 196.5
RATIO = round(BRUTO / OMZET, 2)
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / PNL24 * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)


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
                "leftover dual — Les Erables YE2025 Medium "
                f"(omzet 4.63m / pnl DROP {PNL_PCT}% / FTE DROP {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Les Erables / C.A.V.A. ASBL Tournai {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet DROP {OMZET} ({OMZET_PCT}%); bruto DROP {BRUTO} (~{RATIO}x / {BRUTO_PCT}%); "
                f"pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); equity DROP {EQUITY} ({EQUITY_PCT}%); "
                f"FTE DROP {FTE} vs {FTE24} ({FTE_PCT}%); 1 VE; NACE 88.993; neerlegging 09.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
                f"Relais Haute Sambre/Stallbois YE2024; after Val du Geer@2258; deferred FREE Alteria YE2025 live; "
                f"next EVERY-10 2260 MUST refresh progress+top10"
            )
            r["instructions"] = (
                "leftover dual Les Erables YE2025 FREE Walloon ETA after Val du Geer; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "EVERY-10 + leftover dual after Les Erables — prefer AGB/FARO-YE2025/"
                    "AIESH-REW/Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "EVERY-10 MANDATORY first: refresh docs/doge/data/progress_every_10_ticks.md "
                    "(layers A-E vs €347.956 bn TE) and docs/doge/data/doge_waste_top10_current.md "
                    "(top 10 by priority_index). Then ONE hole-fill unit. "
                    f"After Les Erables YE2025 Medium (omzet 4.63m / pnl DROP {PNL_PCT}% / FTE DROP {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. Alteria Colfontaine YE2025 FREE live deferred; "
                    "skip Les Erables/Val du Geer/Nekto/Belair/Corelap/Cambier/Gaillettes/Hunelle/"
                    "Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/TRAVCO/Pilifs/Jeunes Jardiniers/"
                    "La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA 123 Beauraing/Manufast/"
                    "Metalgroup/EntrAnam/Enghien/Entra/Ateliers de Tertre/Le Rucher/Het Rekreatief/Travie/"
                    "SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/Den Azalee/"
                    "Kemphaan/Mirto/Blankedale/Werkmmaat; Relais Haute Sambre/Sipres/APN/Stallbois still YE2024). "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Les Erables; EVERY-10@2260 MUST refresh progress+top10; "
                    "FARO/AIESH/REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; "
                    "Relais Haute Sambre/Stallbois YE2024; deferred FREE Alteria YE2025 live"
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
                f"tick{TICK} leftover Les Erables {KBO} Medium (omzet DROP {OMZET}; "
                f"pnl DROP {PNL} {PNL_PCT}%; bruto DROP {BRUTO}; equity DROP {EQUITY}; "
                f"FTE DROP {FTE} vs {FTE24}; 1 VE Tournai ETA); after Val du Geer@2258; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre/Stallbois YE2024; "
                f"deferred FREE Alteria YE2025; next {RQ_NEXT} EVERY-10 MUST refresh progress+top10; "
                "continuous hole_fill"
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
        f"""# FOI draft — Les Erables (NBB PDF / pnl DROP {PNL_PCT}% / FTE DROP {FTE})

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Les Erables / C.A.V.A. ASBL — KBO **{KBO}** (Actief; Rue Du Bois Des Hospices 5, 7522 Tournai/Blandain; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Tournai)  
**recipient:** info@leserables.be · oh@leserables.be · Rue Du Bois Des Hospices 5, 7522 Tournai  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}/les-erables) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}/les-erables) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}/les-erables) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_BARE}) · [site](https://www.leserables.be/) · [leseta](https://leseta.be/annuaire-eta/les-erables/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief ASBL/VZW **Les Erables** (also C.A.V.A.); **1 VE**; zetel Tournai; NACE **88.993**; begindatum 24.06.1991.
- CW YE2025: omzet **EUR{OMZET:,}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** DROP {BRUTO_PCT}% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP {EQUITY_PCT}%; FTE **{FTE}** DROP vs {FTE24}; filed **09.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre/Stallbois YE2024. After Val du Geer@2258. Deferred FREE Alteria YE2025 live.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Les Erables ASBL (C.A.V.A.)
via info@leserables.be / oh@leserables.be
Rue Du Bois Des Hospices 5, 7522 Tournai
Objet: Publicité des comptes annuels 2025 Les Erables (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OMZET} / marge brute EUR{BRUTO} (~{RATIO}x).
3. PnL DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}) — réconciliation avec FTE DROP {FTE} (vs {FTE24}).
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition coûts confection / conditionnement / garnissage / contrats d'entreprise.

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

## Tick {TICK} - {UTC} - rq_2259 Les Erables Tournai (omzet 4.63m / pnl DROP {PNL_PCT}% / FTE DROP {FTE} / Medium)

- Unit: **rq_2259** leftover dual after **rq_2258 Val du Geer**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre/Stallbois still **YE2024**. Took deferred FREE Walloon ETA **Les Erables / C.A.V.A. ASBL** YE2025 (KBO **{KBO}**; Rue Du Bois Des Hospices 5 Tournai/Blandain; **Actief** **1 VE**; NACE **88.993** AViQ). Deferred FREE Alteria Colfontaine YE2025 live. Do not redo Val du Geer/Nekto/Belair/Corelap/Cambier/Gaillettes/Hunelle/Dauphins/Saupont stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** DROP {BRUTO_PCT}% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_PCT}%; FTE **{FTE}** DROP vs {FTE24}; neerlegging **09.07.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@leserables.be / oh@leserables.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.25); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2259=done + rq_2260 open (EVERY-10); loop_state ticks={TICK}; raw docs/doge/data/raw/tick2259/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2250**; next **2260** MUST refresh progress + waste top10 then hole-fill). Next: rq_2260.
"""
        )
    print("loop_log appended")


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_erables_jr2025_cw_nl",
                "title": "Companyweb NL Les Erables / C.A.V.A. YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}/les-erables",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet DROP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} "
                    f"bruto {BRUTO} FTE DROP {FTE}; neerlegging 09.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2259/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Les Erables / C.A.V.A. YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}/les-erables",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 09-07-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_erables_jr2025_cw_fr",
                "title": "Companyweb FR Les Erables / C.A.V.A. YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}/les-erables",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Bénéfice {PNL}",
            },
            {
                "source_id": f"src_erables_kbo_{TICK}",
                "title": f"KBO Les Erables {KBO} Actief Tournai 1 VE",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
                    f"lang=nl&ondernemingsnummer={KBO_BARE}"
                ),
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief ASBL/VZW Les Erables (C.A.V.A. on CW); zetel Rue Du Bois Des Hospices 5 "
                    f"7522 Tournai; 1 VE; NACE 88.993; begindatum 24.06.1991; KBO email empty"
                ),
            },
            {
                "source_id": f"src_erables_site_contact_{TICK}",
                "title": "Les Erables FOI channel info@ / oh@leserables.be",
                "url": "https://leseta.be/annuaire-eta/les-erables/",
                "publisher": "leseta.be / Les Erables ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; oh@leserables.be (leseta) + info@leserables.be (FB/LinkedIn); "
                    "site https://www.leserables.be/; tel 069/88.08.00; Rue Du Bois Des Hospices 5 7522 Tournai"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_erables_omzet_jr2025_statutory",
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
                "budget_id": "bud_erables_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto DROP {BRUTO_PCT}%; bruto/omzet ~{RATIO}x",
            },
            {
                "budget_id": "bud_erables_pnl_jr2025_statutory",
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
                "budget_id": "bud_erables_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW statutory eigen_vermogen YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; equity DROP {EQUITY_PCT}% vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_erables_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": f"CW social-balance FTE {FTE}",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; FTE DROP {FTE} vs YE2024 {FTE24}; assets/debt Unknown",
            },
            {
                "budget_id": "bud_erables_omzet_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(OMZET24),
                "amount_min_eur": str(OMZET24),
                "amount_max_eur": str(OMZET24),
                "basis": "CW statutory omzet YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 omzet {OMZET24} comparative (pre DROP)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Les Erables YE2025 leftover dual "
                    f"(omzet 4.63m / pnl DROP {PNL_PCT}% / FTE DROP {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Tournai / AVIQ adapted-work public path",
                "legal_basis": f"ASBL ETA Les Erables / C.A.V.A. (KBO {KBO}; Actief; 1 VE; NACE 88.993; Tournai)",
                "decision_date": "2026-07-09",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET24},'
                    f'"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},'
                    f'"2024_fte":{FTE24}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}/les-erables",
                "stated_goal": "Walloon ETA confection / packaging / upholstery Tournai",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; reconcile pnl DROP -89% + FTE DROP vs AVIQ ETA "
                    "subsidy matrix; disclose atelier cost allocation"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Hainaut>Tournai>LesErables>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; pnl DROP {PNL}; "
                    f"FTE DROP {FTE}; 1 VE; after Val du Geer@2258; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
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
                    f"Les Erables omzet 4.63m / pnl DROP {PNL_PCT}% / FTE DROP {FTE} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Hainaut>Tournai>LesErables>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW omzet {OMZET} / bruto {BRUTO} (~{RATIO}x) / pnl DROP {PNL} ({PNL_PCT}%) / "
                    f"equity DROP {EQUITY} / FTE DROP {FTE} vs {FTE24} / 1 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Tournai / AVIQ adapted-work public path",
                "stated_goal": "Walloon ETA confection / packaging / upholstery",
                "measured_outcome": (
                    f"omzet DROP {OMZET_PCT}%; bruto DROP {BRUTO_PCT}%; pnl DROP {PNL_PCT}%; "
                    f"equity DROP {EQUITY_PCT}%; FTE DROP {FTE_PCT}%; filed 09.07.2026"
                ),
                "absurdity_score": "7.5",
                "cost_score": "4.6",
                "difficulty": "3.0",
                "priority_index": "6.25",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
                    "reconcile pnl DROP -89% + FTE DROP + atelier allocation"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Val du Geer@2258; deferred FREE Alteria YE2025"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Les Erables / C.A.V.A. VZW (Tournai / ETA maatwerk Henegouwen)",
                "name_fr": "Les Erables / C.A.V.A. ASBL (Tournai / entreprise de travail adapté Hainaut)",
                "name_en": "Les Erables / C.A.V.A. adapted-work ASBL (Tournai Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.leserables.be/",
                "foi_email": "info@leserables.be",
                "foi_postal": "Rue Du Bois Des Hospices 5, 7522 Tournai",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet DROP {OMZET} bruto DROP {BRUTO} (~{RATIO}x) pnl DROP {PNL} ({PNL_PCT}%) "
                    f"equity DROP {EQUITY} FTE DROP {FTE} vs {FTE24}; neerlegging 09.07.2026; "
                    f"assets/debt Unknown; FOI {GAP}; also oh@leserables.be; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Val du Geer@2258; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Wallonie>Hainaut>Tournai>LesErables>NBB_PDF_assets_debt_pnl_drop_fte",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OMZET} / "
                    f"bruto EUR{BRUTO} (~{RATIO}x); pnl DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}); "
                    f"FTE DROP {FTE} vs {FTE24}; AVIQ ETA subsidy matrix; atelier cost allocation"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (omzet 4.63m / pnl DROP {PNL_PCT}% / FTE DROP {FTE}) "
                    "under AVIQ path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Les Erables ASBL (C.A.V.A.)",
                "recipient_email": "info@leserables.be",
                "recipient_postal": "Rue Du Bois Des Hospices 5, 7522 Tournai",
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
                    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; also oh@leserables.be; "
                    "preferred stall FARO/AIESH/REW YE2024; AGB Bornem JR2024; after Val du Geer@2258; "
                    "next EVERY-10 2260"
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
