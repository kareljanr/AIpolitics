# tick 2255 — Corelap Mouscron YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2255
UTC = "2026-08-27T05:55:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_corelap_mouscron"
KBO = "0442.541.516"
KBO_BARE = "0442541516"
SRC_EN = "src_corelap_jr2025_cw_en"
GAP = "gap_corelap_nbb_pdf_assets_debt_bruto_gt_omzet_2_01x_pnl_drop_eta_matrix_l5"
COMM = "comm_corelap_jr2025_statutory_eta_bruto_gt_omzet_pnl_drop"
LB = "lb_corelap_bruto_5_21m_2_01x_pnl_drop_jr2025"
RQ = "rq_2255"
RQ_NEXT = "rq_2256"

OMZET = 2594128
OMZET24 = 2705695
BRUTO = 5208599
BRUTO24 = 5195286
PNL = 571199
PNL24 = 663710
EQUITY = 3905323
EQUITY24 = 3343291
FTE = 130.0
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
                "leftover dual — Corelap YE2025 Medium "
                f"(bruto 5.21m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE:g})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Corelap ASBL Mouscron {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet DROP {OMZET} ({OMZET_PCT}%); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE:g}; 1 VE; NACE 88.993; neerlegging 18.06.2026; assets/debt Unknown; "
                f"FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
                f"Relais Haute Sambre YE2024; after Cambier@2254; next EVERY-10 2260"
            )
            r["instructions"] = (
                "leftover dual Corelap YE2025 FREE Walloon ETA after Cambier; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Corelap — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Corelap YE2025 Medium "
                    f"(bruto 5.21m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE:g}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. Belair / Nekto / Val du Geer / Les Erables "
                    "if YE2025 FREE; skip Corelap/Cambier/Gaillettes/Hunelle/Dauphins Gembloux/Saupont/"
                    "Serviplast/Jean Del'Cour/TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/"
                    "Le Perron/L'Atelier/Axedis/ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/"
                    "Ateliers de Tertre/Le Rucher/Het Rekreatief/Travie/SDB/De Vleugels/Kiemkracht/De Oever/"
                    "ViTeS*/Kringwinkel*/Manus*/Reset/Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; "
                    "Relais Haute Sambre/Sipres/APN still YE2024). "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2260."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Corelap; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Relais Haute Sambre YE2024; next every-10 2260"
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
                f"tick{TICK} leftover Corelap {KBO} Medium (bruto JUMP {BRUTO} ~{RATIO}x; "
                f"omzet DROP {OMZET}; pnl DROP {PNL} {PNL_PCT}%; equity JUMP {EQUITY}; FTE {FTE:g}; 1 VE Mouscron ETA); "
                f"after Cambier@2254; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024; "
                f"next {RQ_NEXT}; next EVERY-10 2260; continuous hole_fill"
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
        f"""# FOI draft — Corelap (NBB PDF / bruto≫omzet ~{RATIO}x / pnl DROP {PNL_PCT}%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Corelap ASBL — KBO **{KBO}** (Actief; Bergstraat 103, 7700 Mouscron; **1 VE**; FTE {FTE:g} CW; NACE **88.993**; Walloon ETA Mouscron)  
**recipient:** eta@corelap.be · Bergstraat 103, 7700 Mouscron  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.corelap.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL Corelap; **1 VE**; zetel Mouscron; NACE **88.993** (+88.995).
- CW YE2025: omzet **EUR{OMZET:,}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE:g}**; filed **18.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024. After Cambier@2254.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Corelap ASBL
via eta@corelap.be
Bergstraat 103, 7700 Mouscron
Objet: Publicité des comptes annuels 2025 Corelap (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OMZET} / marge brute EUR{BRUTO} (~{RATIO}x).
3. PnL DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}) — réconciliation avec FTE {FTE:g} et equity JUMP +{EQUITY_PCT}%.
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition coûts activités Mouscron (copy/packaging/industrial).

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

## Tick {TICK} - {UTC} - rq_2255 Corelap Mouscron (bruto 5.21m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE:g} / Medium)

- Unit: **rq_2255** leftover dual after **rq_2254 Cambier**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre still **YE2024**. Took named FREE Walloon ETA **Corelap ASBL** YE2025 (KBO **{KBO}**; Bergstraat 103 Mouscron; **Actief** **1 VE**; NACE **88.993** AViQ) — deferred from Cambier@2254. Do not redo Cambier/Gaillettes/Hunelle/Dauphins stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE:g}**; neerlegging **18.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via eta@corelap.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.00); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2255=done + rq_2256 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2255/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2250**; next **2260**). Next: rq_2256 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
        )
    print("loop_log appended")


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_corelap_jr2025_cw_nl",
                "title": "Companyweb NL Corelap YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet DROP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} "
                    f"bruto {BRUTO} FTE {FTE:g}; neerlegging 18.06.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2255/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Corelap YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 18-06-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} FTE {FTE:g}"
                ),
            },
            {
                "source_id": "src_corelap_jr2025_cw_fr",
                "title": "Companyweb FR Corelap YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Bénéfice {PNL}",
            },
            {
                "source_id": f"src_corelap_kbo_{TICK}",
                "title": f"KBO Corelap {KBO} Actief Mouscron 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW/ASBL Corelap; zetel Bergstraat 103 7700 Mouscron; "
                    f"1 VE; NACE 88.993/88.995; begindatum 18.10.1990; KBO email empty"
                ),
            },
            {
                "source_id": f"src_corelap_site_contact_{TICK}",
                "title": "Corelap FOI channel eta@corelap.be",
                "url": "https://www.corelap.be/",
                "publisher": "Corelap ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; eta@corelap.be / commercial@corelap.be / copy@corelap.be; "
                    "Bergstraat 103 7700 Mouscron; also leseta.be annuaire"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_corelap_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +{BRUTO_PCT}%; bruto≫omzet ~{RATIO}x (primary envelope)",
            },
            {
                "budget_id": "bud_corelap_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW statutory omzet YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet DROP {OMZET_PCT}% vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_corelap_pnl_jr2025_statutory",
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
                "budget_id": "bud_corelap_equity_jr2025_statutory",
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
                "budget_id": "bud_corelap_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": f"CW social-balance FTE {FTE:g}",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; FTE {FTE:g}; YE2024 FTE Unknown on CW page; assets/debt Unknown",
            },
            {
                "budget_id": "bud_corelap_omzet_jr2024_statutory_cmp",
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
                    "Corelap YE2025 leftover dual "
                    f"(bruto 5.21m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE:g} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Mouscron / AVIQ adapted-work public path",
                "legal_basis": f"ASBL ETA Corelap (KBO {KBO}; Actief; 1 VE; NACE 88.993; Mouscron)",
                "decision_date": "2026-06-18",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(BRUTO),
                "cash_by_year": (
                    f'{{"2025_bruto":{BRUTO},"2025_omzet":{OMZET},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_bruto":{BRUTO24},'
                    f'"2024_omzet":{OMZET24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "stated_goal": "Walloon ETA copy / packaging / industrial Mouscron",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; reconcile pnl DROP vs AVIQ ETA subsidy matrix; "
                    f"explain bruto≫omzet ~{RATIO}x"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Hainaut>Mouscron>Corelap>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} ~{RATIO}x; pnl DROP {PNL}; "
                    f"FTE {FTE:g}; 1 VE; after Cambier@2254; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
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
                    f"Corelap bruto 5.21m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE:g} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Hainaut>Mouscron>Corelap>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW bruto {BRUTO} (~{RATIO}x omzet {OMZET}) / pnl DROP {PNL} ({PNL_PCT}%) / "
                    f"equity JUMP {EQUITY} / FTE {FTE:g} / 1 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Mouscron / AVIQ adapted-work public path",
                "stated_goal": "Walloon ETA copy / packaging / industrial",
                "measured_outcome": (
                    f"bruto JUMP +{BRUTO_PCT}%; omzet DROP {OMZET_PCT}%; pnl DROP {PNL_PCT}%; "
                    f"equity JUMP +{EQUITY_PCT}%; FTE {FTE:g}; filed 18.06.2026"
                ),
                "absurdity_score": "7.0",
                "cost_score": "4.8",
                "difficulty": "3.0",
                "priority_index": "6.00",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
                    "reconcile pnl DROP + bruto≫omzet"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Cambier@2254"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Corelap VZW (Moeskroen / ETA maatwerk Henegouwen)",
                "name_fr": "Corelap ASBL (Mouscron / entreprise de travail adapté Hainaut)",
                "name_en": "Corelap adapted-work ASBL (Mouscron Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.corelap.be/",
                "foi_email": "eta@corelap.be",
                "foi_postal": "Bergstraat 103, 7700 Mouscron",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet DROP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} ({PNL_PCT}%) "
                    f"equity JUMP {EQUITY} FTE {FTE:g}; neerlegging 18.06.2026; assets/debt Unknown; FOI {GAP}; "
                    "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; after Cambier@2254; "
                    "not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Wallonie>Hainaut>Mouscron>Corelap>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OMZET} / "
                    f"bruto EUR{BRUTO} (~{RATIO}x); pnl DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}); "
                    f"FTE {FTE:g}; AVIQ ETA subsidy matrix"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (bruto 5.21m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE:g}) "
                    "under AVIQ path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Corelap ASBL",
                "recipient_email": "eta@corelap.be",
                "recipient_postal": "Bergstraat 103, 7700 Mouscron",
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
                    "AGB Bornem JR2024; after Cambier@2254; next EVERY-10 2260"
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
