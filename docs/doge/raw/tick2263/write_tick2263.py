# tick 2263 — leftover dual La Lorraine Services YE2025 Medium (empty omzet)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2263
UTC = "2026-08-27T07:55:00Z"
DATE = "2026-08-27"
ENTITY = "sc_la_lorraine_arlon"
KBO = "0412.131.719"
KBO_BARE = "0412131719"
SRC_EN = "src_lorraine_jr2025_cw_en"
GAP = "gap_lorraine_nbb_pdf_assets_debt_empty_omzet_pnl_drop_56pct_eta_matrix_l5"
COMM = "comm_lorraine_jr2025_statutory_eta_empty_omzet_pnl_drop_56pct"
LB = "lb_lorraine_bruto_5_47m_empty_omzet_pnl_drop_56pct_jr2025"
RQ = "rq_2263"
RQ_NEXT = "rq_2264"

BRUTO = 5468069
BRUTO24 = 5481366
PNL = 267299
PNL24 = 607581
EQUITY = 2808835
EQUITY24 = 2553494
FTE = 156.5
FTE24 = 154.4
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / PNL24 * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
PI = "6.00"


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
                "leftover dual — La Lorraine Services YE2025 Medium "
                f"(bruto 5.47m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; La Lorraine Services SC Arlon {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet unpublished; bruto DROP {BRUTO} ({BRUTO_PCT}%); pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); "
                f"equity JUMP {EQUITY} (+{EQUITY_PCT}%); FTE {FTE} (+{FTE_PCT}% vs {FTE24}); 2 VE; NACE 88.993; "
                f"neerlegging 23.07.2026; assets/debt Unknown; FOI {GAP} ready NOT sent; "
                f"stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024; Relais Haute Sambre/Sipres/APN/Stallbois YE2024; "
                f"after BW Eupen@2262; next EVERY-10 2270"
            )
            r["instructions"] = (
                "leftover dual La Lorraine Services YE2025 FREE Walloon ETA after BW Eupen; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after La Lorraine — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after La Lorraine Services YE2025 Medium "
                    f"(bruto 5.47m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk. "
                    "Skip La Lorraine/BW Eupen/AJR/Alteria/Les Erables/Val du Geer/Nekto/Belair/Corelap/"
                    "Cambier/Gaillettes/Hunelle/Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/TRAVCO/"
                    "Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/"
                    "ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers de Tertre/"
                    "Le Rucher/Het Rekreatief/Travie/SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/"
                    "Kringwinkel*/Manus*/Reset/Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; "
                    "Relais Haute Sambre/Sipres/APN/Stallbois YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2270."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} La Lorraine; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Relais Haute Sambre/Sipres/APN/Stallbois YE2024; next every-10 2270"
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
                f"tick{TICK} leftover dual La Lorraine Services {KBO} Medium (bruto DROP {BRUTO} {BRUTO_PCT}%; "
                f"empty omzet; pnl DROP {PNL} {PNL_PCT}%; equity JUMP {EQUITY}; FTE {FTE}; 2 VE Arlon Walloon ETA); "
                f"after BW Eupen@2262; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
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
        f"""# FOI draft — La Lorraine Services (NBB PDF / empty omzet / pnl DROP {PNL_PCT}%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** La Lorraine Services SC — KBO **{KBO}** (Actief; Weyler Zone artisanale 32A, 6700 Arlon; **2 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Arlon)  
**recipient:** commercial@lalorraine.org · Weyler Zone artisanale 32 bus A, 6700 Arlon  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.lalorraine.org/) · [leseta](https://leseta.be/annuaire-eta/la-lorraine/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; omzet/assets/debt Unknown)

## Context
- KBO Strong: Actief SC/CV LA LORRAINE SERVICES; **2 VE**; zetel Arlon Weyler; BTW NACE **88.993** (+ cleaning/placement); begindatum 01.03.1972; rechtsvorm SC sinds 10.07.2024.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** DROP {BRUTO_PCT}% vs YE2024 EUR{BRUTO24:,}; pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); filed **23.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre/Sipres/APN/Stallbois YE2024. After BW Eupen@2262 (this unit was deferred).

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: La Lorraine Services SC
via commercial@lalorraine.org
Weyler, Zone artisanale 32 bus A, 6700 Arlon
Objet: Publicité des comptes annuels 2025 La Lorraine Services (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Wallonie / AViQ), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Chiffre d'affaires YE2025 (non publié sur Companyweb) et composition vs marge brute EUR{BRUTO}.
3. PnL DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}) — réconciliation avec FTE {FTE} (vs {FTE24}).
4. Matrice des subsides AViQ / ETA derrière les charges de personnel.
5. Répartition CA/activités (nettoyage Mitreex / services / mise au travail).

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


### 2026-08-27T07:55:00Z - tick 2263 - rq_2263 La Lorraine Services Arlon (bruto 5.47m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2263** leftover dual after **rq_2262 BW Eupen**. Prefer NON-stall live: AGB Bornem still **JR2024-only** (portal 404 this tick); FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre/Sipres/APN/Stallbois still **YE2024**. Took deferred FREE Walloon ETA **La Lorraine Services SC** YE2025 (KBO **{KBO}**; Weyler Zone artisanale 32A Arlon; **Actief** **2 VE**; NACE **88.993** AViQ). Do not redo BW Eupen/AJR/Alteria/Les Erables/Val du Geer/Nekto/Belair stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** DROP {BRUTO_PCT}% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); neerlegging **23.07.2026**. Strong KBO Actief 2 VE SC. Assets/debt Unknown. Medium. FOI via commercial@lalorraine.org.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2263=done + rq_2264 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2263/ + data/raw/tick2263/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2260**; next **2270**). Next: rq_2264 (AGB/FARO-if-YE2025 / AIESH-REW / unused ETA-VAPH-WZC-maatwerk).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2263"
    dst_raw = DATA / "raw" / "tick2263"
    dst_raw.mkdir(parents=True, exist_ok=True)
    for f in src_raw.glob("*"):
        if f.is_file():
            shutil.copy2(f, dst_raw / f.name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_lorraine_jr2025_cw_nl",
                "title": "Companyweb NL La Lorraine Services YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet unpublished pnl DROP {PNL} equity JUMP {EQUITY} "
                    f"bruto {BRUTO} FTE {FTE}; neerlegging 23.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2263/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN La Lorraine Services YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 23-07-2026; Last balance sheet year 2025; "
                    f"Turnover unpublished Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_lorraine_jr2025_cw_fr",
                "title": "Companyweb FR La Lorraine Services YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA unpublished; Marge brute {BRUTO}; Bénéfice {PNL}",
            },
            {
                "source_id": f"src_lorraine_kbo_{TICK}",
                "title": f"KBO La Lorraine Services {KBO} Actief Arlon 2 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief SC/CV LA LORRAINE SERVICES; zetel Weyler Zone artisanale 32 bus A 6700 Arlon; "
                    f"2 VE; BTW NACE 88.993; begindatum 01.03.1972; rechtsvorm SC sinds 10.07.2024; KBO email/web empty"
                ),
            },
            {
                "source_id": f"src_lorraine_site_contact_{TICK}",
                "title": "La Lorraine FOI channel commercial@lalorraine.org",
                "url": "https://www.lalorraine.org/",
                "publisher": "La Lorraine Services SC",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; commercial@lalorraine.org; Tel +32 63 22 18 73; "
                    "Weyler Zone artisanale Arlon; also leseta.be annuaire ETA"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_lorraine_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025 (primary; omzet unpublished)",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto DROP {BRUTO_PCT}% vs YE2024 {BRUTO24}; empty omzet",
            },
            {
                "budget_id": "bud_lorraine_pnl_jr2025_statutory",
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
                "budget_id": "bud_lorraine_equity_jr2025_statutory",
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
                "budget_id": "bud_lorraine_fte_jr2025_statutory",
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
                "budget_id": "bud_lorraine_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory winst YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre DROP {PNL_PCT}%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "La Lorraine Services YE2025 leftover dual "
                    f"(bruto 5.47m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Arlon / Walloon adapted-work public path",
                "legal_basis": f"SC ETA La Lorraine Services (KBO {KBO}; Actief; 2 VE; NACE 88.993; Arlon)",
                "decision_date": "2026-07-23",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(BRUTO),
                "cash_by_year": (
                    "{"
                    f'"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},'
                    f'"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24},'
                    '"2025_omzet":"unpublished"'
                    "}"
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "stated_goal": "Walloon ETA sheltered workshop Arlon (cleaning Mitreex / services / placement)",
                "cut_option": (
                    "Publish NBB PDF assets/debt + omzet FOI; reconcile pnl DROP -56% vs FTE 156.5 / AViQ ETA matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Arlon>La_Lorraine_Services>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (omzet unpublished); pnl DROP {PNL}; "
                    f"FTE {FTE}; 2 VE; after BW Eupen@2262; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
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
                    f"La Lorraine bruto 5.47m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_sc_statutory",
                "hierarchy_path": "Wallonie>Arlon>La_Lorraine_Services>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW bruto {BRUTO} ({BRUTO_PCT}%) / omzet unpublished / pnl DROP {PNL} ({PNL_PCT}%) / "
                    f"equity JUMP {EQUITY} / FTE {FTE} (vs {FTE24}) / 2 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Arlon / Walloon adapted-work public path",
                "stated_goal": "Walloon ETA sheltered workshop Arlon (Mitreex/services)",
                "measured_outcome": (
                    f"bruto DROP {BRUTO_PCT}%; omzet unpublished; pnl DROP {PNL_PCT}%; "
                    f"equity JUMP +{EQUITY_PCT}%; FTE {FTE} (+{FTE_PCT}%); filed 23.07.2026"
                ),
                "absurdity_score": "7.4",
                "cost_score": "5.8",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash + omzet FOI; disclose AViQ ETA matrix; "
                    "reconcile pnl DROP -56% despite stable bruto/FTE"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after BW Eupen@2262"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "La Lorraine Services CV (Arlon / ETA maatwerk Luxemburg)",
                "name_fr": "La Lorraine Services SC (Arlon / entreprise de travail adapté Luxembourg)",
                "name_en": "La Lorraine Services adapted-work SC (Arlon Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.lalorraine.org/",
                "foi_email": "commercial@lalorraine.org",
                "foi_postal": "Weyler, Zone artisanale 32 bus A, 6700 Arlon",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE NACE 88.993; "
                    f"omzet unpublished bruto DROP {BRUTO} ({BRUTO_PCT}%) pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} "
                    f"FTE {FTE}; neerlegging 23.07.2026; assets/debt Unknown; FOI {GAP}; "
                    "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; after BW Eupen@2262; "
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
                "hierarchy_path": "Wallonie>Arlon>La_Lorraine_Services>NBB_PDF_assets_debt_empty_omzet_pnl_drop_56pct",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet unpublished on CW; "
                    f"bruto EUR{BRUTO} ({BRUTO_PCT}%); pnl DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}); "
                    f"FTE {FTE}; AViQ ETA subsidy matrix"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA SC (bruto 5.47m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE}) "
                    "under AViQ path; omzet/assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "La Lorraine Services SC",
                "recipient_email": "commercial@lalorraine.org",
                "recipient_postal": "Weyler, Zone artisanale 32 bus A, 6700 Arlon",
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
                    "AGB Bornem JR2024; after BW Eupen@2262; next EVERY-10 2270"
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
