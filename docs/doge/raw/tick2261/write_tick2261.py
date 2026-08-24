# tick 2261 — leftover dual AJR Lobbes YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2261
UTC = "2026-08-27T07:25:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_ajr_lobbes"
KBO = "0407.410.391"
KBO_BARE = "0407410391"
SRC_EN = "src_ajr_jr2025_cw_en"
GAP = "gap_ajr_nbb_pdf_assets_debt_omzet_drop_21pct_pnl_drop_87pct_eta_matrix_l5"
COMM = "comm_ajr_jr2025_statutory_eta_omzet_drop_21pct_pnl_drop_87pct"
LB = "lb_ajr_omzet_18_02m_pnl_drop_87pct_jr2025"
RQ = "rq_2261"
RQ_NEXT = "rq_2262"

OMZET = 18015589
OMZET24 = 22884000
BRUTO = 11541367
BRUTO24 = 13412889
PNL = 96680
PNL24 = 743761
EQUITY = 4644312
EQUITY24 = 4587623
FTE = 292
FTE24 = 308.1
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
                "leftover dual - AJR YE2025 Medium "
                f"(omzet DROP 18.02m / {OMZET_PCT}% / pnl DROP {PNL_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; AJR/Atelier Jean Regniers ASBL Lobbes {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet DROP {OMZET} ({OMZET_PCT}% vs {OMZET24}); bruto DROP {BRUTO} (~{RATIO}x / {BRUTO_PCT}%); "
                f"pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE} ({FTE_PCT}% vs {FTE24}); 1 VE; NACE 88.993; neerlegging 08.07.2026; assets/debt Unknown; "
                f"FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
                f"Relais Haute Sambre/Sipres/APN/Stallbois YE2024; La Lorraine/BW Eupen still YE2024; "
                f"after Alteria@2260; next EVERY-10 2270"
            )
            r["instructions"] = (
                "leftover dual AJR YE2025 FREE Walloon ETA after Alteria; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after AJR — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after AJR YE2025 Medium "
                    f"(omzet DROP 18.02m / {OMZET_PCT}% / pnl DROP {PNL_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. La Lorraine / BW Eupen / Adapta "
                    "if YE2025 FREE; skip AJR/Alteria/Les Erables/Val du Geer/Nekto/Belair/Corelap/Cambier/"
                    "Gaillettes/Hunelle/Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/TRAVCO/Pilifs/"
                    "Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/"
                    "ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers de Tertre/"
                    "Le Rucher/Het Rekreatief/Travie/SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/"
                    "Kringwinkel*/Manus*/Reset/Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; "
                    "Relais Haute Sambre/Sipres/APN/Stallbois YE2024; La Lorraine/BW Eupen YE2024 this tick). "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2270."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} AJR; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "La Lorraine/BW Eupen YE2024; Relais Haute Sambre/Sipres/APN/Stallbois YE2024; next every-10 2270"
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
                f"tick{TICK} leftover dual AJR {KBO} Medium (omzet DROP {OMZET} {OMZET_PCT}%; "
                f"pnl DROP {PNL} {PNL_PCT}%; bruto DROP {BRUTO} ~{RATIO}x; equity JUMP {EQUITY}; FTE {FTE}; 1 VE Lobbes ETA); "
                f"after Alteria@2260; AGB Bornem JR2024; FARO/AIESH/REW YE2024; La Lorraine/BW Eupen YE2024; "
                f"Relais Haute Sambre/Sipres/APN/Stallbois YE2024; next {RQ_NEXT}; next EVERY-10 2270; continuous hole_fill"
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
        f"""# FOI draft — AJR / Atelier Jean Regniers (NBB PDF / omzet DROP {OMZET_PCT}% / pnl DROP {PNL_PCT}%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** AJR ASBL (Atelier Jean Regniers) — KBO **{KBO}** (Actief; Rue Evelyn Drory 5, 6543 Lobbes; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Lobbes/Hainaut)  
**recipient:** marketing@ajregniers.be · Rue Evelyn Drory 5, 6543 Lobbes  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.ajregniers.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL Atelier Jean Regniers / AJR; **1 VE**; zetel Lobbes; RSZ NACE **88.993**; BTW sinds 1971; begindatum 25.11.1965.
- CW YE2025: omzet **EUR{OMZET:,}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** DROP {BRUTO_PCT}% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); filed **08.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; La Lorraine/BW Eupen YE2024; Relais Haute Sambre/Sipres/APN/Stallbois YE2024. After Alteria@2260.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: AJR ASBL — Atelier Jean Regniers
via marketing@ajregniers.be
Rue Evelyn Drory 5, 6543 Lobbes
Objet: Publicité des comptes annuels 2025 AJR (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OMZET} DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24} / marge brute EUR{BRUTO}.
3. PnL DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}) — réconciliation avec FTE {FTE} (vs {FTE24}).
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition CA par activité (bois/palettes, détergents, couture, conditionnement, PVC-PP, régie).

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

### 2026-08-27T07:25:00Z - tick 2261 - rq_2261 AJR Lobbes (omzet DROP 18.02m / {OMZET_PCT}% / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2261** leftover dual after **rq_2260 Alteria**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; La Lorraine / BW Eupen still **YE2024**; Relais Haute Sambre/Sipres/APN/Stallbois still **YE2024**. Took named FREE Walloon ETA **AJR / Atelier Jean Regniers ASBL** YE2025 (KBO **{KBO}**; Rue Evelyn Drory 5 Lobbes; **Actief** **1 VE**; NACE **88.993** AViQ). Do not redo Alteria/Les Erables/Val du Geer/Nekto/Belair/Corelap/Cambier stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** DROP {BRUTO_PCT}% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); neerlegging **08.07.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via marketing@ajregniers.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.85); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2261=done + rq_2262 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2261/ + data/raw/tick2261/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2260**; next **2270**). Next: rq_2262 (AGB/FARO-if-YE2025 / AIESH-REW / unused La Lorraine-if-YE2025).
"""
        )
    print("loop_log appended")


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_ajr_jr2025_cw_nl",
                "title": "Companyweb NL AJR / Atelier Jean Regniers YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet DROP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} "
                    f"bruto {BRUTO} FTE {FTE}; neerlegging 08.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2261/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN AJR / Atelier Jean Regniers YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 08-07-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_ajr_jr2025_cw_fr",
                "title": "Companyweb FR AJR / Atelier Jean Regniers YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Bénéfice {PNL}",
            },
            {
                "source_id": f"src_ajr_kbo_{TICK}",
                "title": f"KBO AJR {KBO} Actief Lobbes 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW/ASBL Atelier Jean Regniers / AJR; zetel Rue Evelyn Drory 5 6543 Lobbes; "
                    f"1 VE; RSZ NACE 88.993; BTW 85.322; begindatum 25.11.1965; KBO email/web empty"
                ),
            },
            {
                "source_id": f"src_ajr_site_contact_{TICK}",
                "title": "AJR FOI channel marketing@ajregniers.be",
                "url": "https://www.ajregniers.be/",
                "publisher": "AJR ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; marketing@ajregniers.be / cguyaux@ajregniers.be; "
                    "Rue Evelyn Drory 5 6543 Lobbes; also leseta.be annuaire"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_ajr_omzet_jr2025_statutory",
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
                "budget_id": "bud_ajr_bruto_jr2025_statutory",
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
                "budget_id": "bud_ajr_pnl_jr2025_statutory",
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
                "budget_id": "bud_ajr_equity_jr2025_statutory",
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
                "budget_id": "bud_ajr_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": f"CW social-balance FTE {FTE}",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; FTE {FTE} vs YE2024 {FTE24}; assets/debt Unknown",
            },
            {
                "budget_id": "bud_ajr_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory winst YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre DROP -87%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "AJR YE2025 leftover dual "
                    f"(omzet DROP 18.02m / {OMZET_PCT}% / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Lobbes / AVIQ adapted-work public path",
                "legal_basis": f"ASBL ETA AJR Atelier Jean Regniers (KBO {KBO}; Actief; 1 VE; NACE 88.993; Lobbes)",
                "decision_date": "2026-07-08",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET24},'
                    f'"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "stated_goal": "Walloon ETA wood/pallets detergents sewing packaging PVC-PP régie Lobbes",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; reconcile omzet DROP -21% + pnl DROP -87% vs AVIQ ETA subsidy matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Hainaut>Lobbes>AJR>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; pnl DROP {PNL}; "
                    f"FTE {FTE}; 1 VE; after Alteria@2260; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
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
                    f"AJR omzet DROP 18.02m / {OMZET_PCT}% / pnl DROP {PNL_PCT}% / FTE {FTE} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Hainaut>Lobbes>AJR>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW omzet DROP {OMZET} ({OMZET_PCT}%) / bruto {BRUTO} (~{RATIO}x) / pnl DROP {PNL} ({PNL_PCT}%) / "
                    f"equity JUMP {EQUITY} / FTE {FTE} (vs {FTE24}) / 1 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Lobbes / AVIQ adapted-work public path",
                "stated_goal": "Walloon ETA wood/pallets detergents sewing packaging PVC-PP régie",
                "measured_outcome": (
                    f"omzet DROP {OMZET_PCT}%; bruto DROP {BRUTO_PCT}%; pnl DROP {PNL_PCT}%; "
                    f"equity JUMP +{EQUITY_PCT}%; FTE {FTE} ({FTE_PCT}%); filed 08.07.2026"
                ),
                "absurdity_score": "8.2",
                "cost_score": "6.8",
                "difficulty": "3.0",
                "priority_index": "6.85",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
                    "reconcile omzet DROP -21% + pnl DROP -87%"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; La Lorraine/BW Eupen YE2024; after Alteria@2260"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "AJR VZW / Atelier Jean Regniers (Lobbes / ETA maatwerk Henegouwen)",
                "name_fr": "AJR ASBL / Atelier Jean Regniers (Lobbes / entreprise de travail adapté Hainaut)",
                "name_en": "AJR / Atelier Jean Regniers adapted-work ASBL (Lobbes Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.ajregniers.be/",
                "foi_email": "marketing@ajregniers.be",
                "foi_postal": "Rue Evelyn Drory 5, 6543 Lobbes",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet DROP {OMZET} ({OMZET_PCT}%) bruto DROP {BRUTO} (~{RATIO}x) pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} "
                    f"FTE {FTE}; neerlegging 08.07.2026; assets/debt Unknown; FOI {GAP}; "
                    "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; after Alteria@2260; "
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
                "hierarchy_path": "Wallonie>Hainaut>Lobbes>AJR>NBB_PDF_assets_debt_omzet_drop_21pct_pnl_drop_87pct",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OMZET} DROP {OMZET_PCT}% / "
                    f"bruto EUR{BRUTO}; pnl DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}); "
                    f"FTE {FTE}; AVIQ ETA subsidy matrix"
                ),
                "why_it_matters": (
                    f"Medium CW shows large Walloon ETA ASBL (omzet DROP 18.02m / {OMZET_PCT}% / pnl DROP {PNL_PCT}% / FTE {FTE}) "
                    "under AVIQ path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "AJR ASBL — Atelier Jean Regniers",
                "recipient_email": "marketing@ajregniers.be",
                "recipient_postal": "Rue Evelyn Drory 5, 6543 Lobbes",
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
                    "AGB Bornem JR2024; La Lorraine/BW Eupen YE2024; after Alteria@2260; next EVERY-10 2270"
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
