# tick 2257 — Nekto Soignies/Neufvilles YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2257
UTC = "2026-08-27T06:25:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_nekto_soignies"
KBO = "0407.695.453"
KBO_BARE = "0407695453"
SRC_EN = "src_nekto_jr2025_cw_en"
GAP = "gap_nekto_nbb_pdf_assets_debt_bruto_gt_omzet_1_67x_pnl_loss_deepen_eta_matrix_l5"
COMM = "comm_nekto_jr2025_statutory_eta_bruto_gt_omzet_pnl_loss_deepen"
LB = "lb_nekto_bruto_12_59m_1_67x_pnl_loss_deepen_jr2025"
RQ = "rq_2257"
RQ_NEXT = "rq_2258"

OMZET = 7545708
OMZET24 = 7468888
BRUTO = 12592290
BRUTO24 = 11665244
PNL = -172066
PNL24 = -118224
EQUITY = 5269578
EQUITY24 = 5449324
FTE = 310.6
RATIO = round(BRUTO / OMZET, 2)
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
PNL_DEEPEN = PNL - PNL24


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
                "leftover dual — Nekto YE2025 Medium "
                f"(bruto 12.59m / ~{RATIO}x / pnl LOSS DEEPEN / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Nekto ASBL Soignies/Neufvilles {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}%); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl LOSS DEEPEN {PNL} vs YE2024 {PNL24}; equity DROP {EQUITY} ({EQUITY_PCT}%); "
                f"FTE {FTE}; 2 VE; NACE 88.993; neerlegging 12.06.2026; assets/debt Unknown; "
                f"FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
                f"Relais Haute Sambre YE2024; after Belair@2256; deferred FREE Val du Geer/Erables; next EVERY-10 2260"
            )
            r["instructions"] = (
                "leftover dual Nekto YE2025 FREE Walloon ETA after Belair; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Nekto — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Nekto YE2025 Medium "
                    f"(bruto 12.59m / ~{RATIO}x / pnl LOSS DEEPEN / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. Val du Geer / Les Erables if YE2025 FREE; "
                    "skip Nekto/Belair/Corelap/Cambier/Gaillettes/Hunelle/Dauphins Gembloux/Saupont/"
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
                    f"spawned after tick{TICK} Nekto; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Relais Haute Sambre YE2024; deferred FREE Val du Geer/Erables; "
                    "next every-10 2260"
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
                f"tick{TICK} leftover Nekto {KBO} Medium (bruto JUMP {BRUTO} ~{RATIO}x; "
                f"omzet JUMP {OMZET}; pnl LOSS DEEPEN {PNL}; equity DROP {EQUITY}; FTE {FTE}; 2 VE Soignies ETA); "
                f"after Belair@2256; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024; "
                f"deferred FREE Val du Geer/Erables; next {RQ_NEXT}; next EVERY-10 2260; continuous hole_fill"
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
        f"""# FOI draft — Nekto (NBB PDF / bruto≫omzet ~{RATIO}x / pnl LOSS DEEPEN)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Nekto ASBL — KBO **{KBO}** (Actief; Chemin du Clypot 3, 7063 Soignies; **2 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Neufvilles/Soignies)  
**recipient:** contact@nekto.be · Chemin du Clypot 3, 7063 Soignies  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}/nekto) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}/nekto) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}/nekto) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.nekto.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL NEKTO; **2 VE**; zetel Soignies/Neufvilles; NACE **88.993** (+88.995); contact@nekto.be in KBO.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS DEEPEN vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP {EQUITY_PCT}%; FTE **{FTE}**; filed **12.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024. After Belair@2256.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Nekto ASBL
via contact@nekto.be
Chemin du Clypot 3, 7063 Soignies
Objet: Publicité des comptes annuels 2025 Nekto (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OMZET} / marge brute EUR{BRUTO} (~{RATIO}x).
3. PnL LOSS DEEPEN EUR{PNL} vs YE2024 EUR{PNL24} — réconciliation avec FTE {FTE} et equity DROP.
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition coûts bois/palettes / conditionnement / espaces verts / peinture / sites Neufvilles-Braine.

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

## Tick {TICK} - {UTC} - rq_2257 Nekto Soignies (bruto 12.59m / ~{RATIO}x / pnl LOSS DEEPEN / FTE {FTE} / Medium)

- Unit: **rq_2257** leftover dual after **rq_2256 Belair**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre still **YE2024**. Took named FREE Walloon ETA **Nekto ASBL** YE2025 (KBO **{KBO}**; Chemin du Clypot 3 Soignies/Neufvilles; **Actief** **2 VE**; NACE **88.993** AViQ). Deferred FREE Val du Geer/Les Erables. Do not redo Belair/Corelap/Cambier/Gaillettes stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL}** LOSS DEEPEN vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_PCT}%; FTE **{FTE}**; neerlegging **12.06.2026**. Strong KBO Actief 2 VE. Assets/debt Unknown. Medium. FOI via contact@nekto.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.40); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2257=done + rq_2258 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2257/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2250**; next **2260**). Next: rq_2258 (AGB/FARO-if-YE2025 / AIESH-REW / unused Val du Geer).
"""
        )
    print("loop_log appended")


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_nekto_jr2025_cw_nl",
                "title": "Companyweb NL Nekto YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}/nekto",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} pnl LOSS DEEPEN {PNL} equity DROP {EQUITY} "
                    f"bruto {BRUTO} FTE {FTE}; neerlegging 12.06.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2257/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Nekto YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}/nekto",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 12-06-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_nekto_jr2025_cw_fr",
                "title": "Companyweb FR Nekto YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}/nekto",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Perte {PNL}",
            },
            {
                "source_id": f"src_nekto_kbo_{TICK}",
                "title": f"KBO Nekto {KBO} Actief Soignies 2 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW/ASBL NEKTO; zetel Chemin du Clypot 3 7063 Soignies; "
                    f"2 VE; NACE 88.993/88.995; begindatum 01.08.1963; KBO email contact@nekto.be; tel 067/332272"
                ),
            },
            {
                "source_id": f"src_nekto_site_contact_{TICK}",
                "title": "Nekto FOI channel contact@nekto.be",
                "url": "https://www.nekto.be/",
                "publisher": "Nekto ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; contact@nekto.be / job@nekto.be; Chemin du Clypot 3 7063 Soignies; "
                    "also Braine-le-Comte site; leseta.be annuaire"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_nekto_bruto_jr2025_statutory",
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
                "budget_id": "bud_nekto_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW statutory omzet YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet JUMP +{OMZET_PCT}% vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_nekto_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl LOSS DEEPEN vs YE2024 {PNL24} (delta {PNL_DEEPEN})",
            },
            {
                "budget_id": "bud_nekto_equity_jr2025_statutory",
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
                "budget_id": "bud_nekto_fte_jr2025_statutory",
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
                "budget_id": "bud_nekto_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory winst YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre LOSS DEEPEN)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Nekto YE2025 leftover dual "
                    f"(bruto 12.59m / ~{RATIO}x / pnl LOSS DEEPEN / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Soignies-Neufvilles / AVIQ adapted-work public path",
                "legal_basis": f"ASBL ETA Nekto (KBO {KBO}; Actief; 2 VE; NACE 88.993; Soignies)",
                "decision_date": "2026-06-12",
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
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}/nekto",
                "stated_goal": "Walloon ETA wood/pallets / packaging / green spaces / painting",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; reconcile pnl LOSS DEEPEN vs AVIQ ETA subsidy matrix; "
                    f"explain bruto≫omzet ~{RATIO}x"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Hainaut>Soignies>Nekto>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} ~{RATIO}x; pnl LOSS DEEPEN {PNL}; "
                    f"FTE {FTE}; 2 VE; after Belair@2256; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
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
                    f"Nekto bruto 12.59m / ~{RATIO}x / pnl LOSS DEEPEN / FTE {FTE} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Hainaut>Soignies>Nekto>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW bruto {BRUTO} (~{RATIO}x omzet {OMZET}) / pnl LOSS DEEPEN {PNL} / "
                    f"equity DROP {EQUITY} / FTE {FTE} / 2 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Soignies-Neufvilles / AVIQ adapted-work public path",
                "stated_goal": "Walloon ETA wood/pallets / packaging / green spaces / painting",
                "measured_outcome": (
                    f"bruto JUMP +{BRUTO_PCT}%; omzet JUMP +{OMZET_PCT}%; pnl LOSS DEEPEN {PNL}; "
                    f"equity DROP {EQUITY_PCT}%; FTE {FTE}; filed 12.06.2026"
                ),
                "absurdity_score": "7.6",
                "cost_score": "5.5",
                "difficulty": "3.0",
                "priority_index": "6.40",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
                    "reconcile pnl LOSS DEEPEN + bruto≫omzet"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Belair@2256; deferred FREE Val du Geer"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Nekto VZW (Zinnik-Neufvilles / ETA maatwerk Henegouwen)",
                "name_fr": "Nekto ASBL (Soignies-Neufvilles / entreprise de travail adapté Hainaut)",
                "name_en": "Nekto adapted-work ASBL (Soignies Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.nekto.be/",
                "foi_email": "contact@nekto.be",
                "foi_postal": "Chemin du Clypot 3, 7063 Soignies",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE NACE 88.993; "
                    f"omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl LOSS DEEPEN {PNL} equity DROP {EQUITY} "
                    f"FTE {FTE}; neerlegging 12.06.2026; assets/debt Unknown; FOI {GAP}; "
                    "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; after Belair@2256; "
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
                "hierarchy_path": "Wallonie>Hainaut>Soignies>Nekto>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_loss_deepen",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OMZET} / "
                    f"bruto EUR{BRUTO} (~{RATIO}x); pnl LOSS DEEPEN EUR{PNL} vs YE2024 EUR{PNL24}; "
                    f"FTE {FTE}; AVIQ ETA subsidy matrix"
                ),
                "why_it_matters": (
                    f"Medium CW shows large Walloon ETA ASBL (bruto 12.59m / ~{RATIO}x / pnl LOSS DEEPEN / FTE {FTE}) "
                    "under AVIQ path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Nekto ASBL",
                "recipient_email": "contact@nekto.be",
                "recipient_postal": "Chemin du Clypot 3, 7063 Soignies",
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
                    "AGB Bornem JR2024; after Belair@2256; next EVERY-10 2260"
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
