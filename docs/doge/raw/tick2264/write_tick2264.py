# tick 2264 — leftover dual Sipres YE2025 Medium (bruto~1.67x / omzet 2.54m)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2264
UTC = "2026-08-27T08:10:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_sipres_ghlin"
KBO = "0423.643.540"
KBO_BARE = "0423643540"
SRC_EN = "src_sipres_jr2025_cw_en"
GAP = "gap_sipres_nbb_pdf_assets_debt_bruto_gt_omzet_1_67x_eta_matrix_l5"
COMM = "comm_sipres_jr2025_statutory_eta_bruto_gt_omzet_1_67x"
LB = "lb_sipres_bruto_4_23m_omzet_2_54m_bruto_gt_omzet_1_67x_jr2025"
RQ = "rq_2264"
RQ_NEXT = "rq_2265"

OMZET = 2541600
OMZET24 = 2389568
BRUTO = 4232586
BRUTO24 = 3550360
PNL = 145855
PNL24 = 142768
EQUITY = 1562064
EQUITY24 = 1416208
FTE = 114.4
FTE24 = 113.0
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / PNL24 * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
RATIO = round(BRUTO / OMZET, 2)
PI = "6.05"


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
                "leftover dual — Sipres YE2025 Medium "
                f"(omzet 2.54m / bruto~{RATIO}x / pnl JUMP +{PNL_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Sipres ASBL Ghlin/Mons {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}%); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl JUMP {PNL} (+{PNL_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE} (+{FTE_PCT}% vs {FTE24}); 2 VE; NACE 88.993; neerlegging 17.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / "
                f"FARO/AIESH/REW YE2024; Relais Haute Sambre/APN YE2024; Stallbois/APRE/Renaitre YE2025 FREE deferred; "
                f"after La Lorraine@2263; next EVERY-10 2270"
            )
            r["instructions"] = (
                "leftover dual Sipres YE2025 FREE Walloon ETA (unlocked from YE2024 stall) after La Lorraine; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Sipres — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Stallbois-APRE-Renaitre-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Sipres YE2025 Medium "
                    f"(omzet 2.54m / bruto~{RATIO}x / pnl JUMP +{PNL_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else named FREE Stallbois YE2025 (0407.149.877) / Brochage Renaitre YE2025 "
                    "(0407.851.148) / APRE YE2025 (0407.598.354), else unused ETA/VAPH/WZC/maatwerk. "
                    "Skip Sipres/La Lorraine/BW Eupen/AJR/Alteria/Les Erables/Val du Geer/Nekto/Belair/"
                    "Corelap/Cambier/Gaillettes/Hunelle/Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/"
                    "TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/"
                    "ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers de Tertre/"
                    "Le Rucher/Het Rekreatief/Travie/SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/"
                    "Kringwinkel*/Manus*/Reset/Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; "
                    "Relais Haute Sambre/APN YE2024; Citeco YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2270."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Sipres; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024; "
                    "Stallbois/APRE/Renaitre YE2025 FREE deferred; next every-10 2270"
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
                f"tick{TICK} leftover dual Sipres {KBO} Medium (omzet JUMP {OMZET} +{OMZET_PCT}%; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; "
                f"2 VE Ghlin Walloon ETA unlocked YE2025); after La Lorraine@2263; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; Relais Haute Sambre/APN YE2024; Stallbois/APRE/Renaitre YE2025 FREE; "
                f"next {RQ_NEXT}; next EVERY-10 2270; continuous hole_fill"
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
        f"""# FOI draft — Sipres (NBB PDF / bruto~{RATIO}x omzet / AViQ ETA matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Sipres ASBL — KBO **{KBO}** (Actief; Rue Eva Dupont (G.) 11, 7011 Mons/Ghlin; **2 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Hainaut provincial)  
**recipient:** info@sipres-services.be · Rue Eva Dupont 11, 7011 Ghlin (+ site Elouges)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.sipres-services.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL SIPRES; **2 VE**; zetel Rue Eva Dupont (G.) 11, 7011 Mons; RSZ NACE **88.993**; begindatum 03.02.1983.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** JUMP +{PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); filed **17.07.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024. Sipres unlocked YE2025 (was YE2024 stall). After La Lorraine@2263.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Sipres ASBL
via info@sipres-services.be
Rue Eva Dupont 11, 7011 Ghlin
Objet: Publicité des comptes annuels 2025 Sipres (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Wallonie / AViQ / Province de Hainaut), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Réconciliation marge brute EUR{BRUTO} vs chiffre d'affaires EUR{OMZET} (~{RATIO}x) — part subsidies / titres-services.
3. Matrice des subsides AViQ / ETA / Province de Hainaut derrière les charges de personnel (FTE {FTE}).
4. Répartition CA/activités (blanchisserie / nettoyage à sec / couture / horticulture / peinture / titres-services) sites Ghlin + Elouges.
5. Dettes LT/CT et trésorerie YE2025 (non publiées sur Companyweb).

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


### 2026-08-27T08:10:00Z - tick 2264 - rq_2264 Sipres Ghlin (omzet 2.54m / bruto~{RATIO}x / pnl JUMP +{PNL_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2264** leftover dual after **rq_2263 La Lorraine**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre/APN still **YE2024**. **Sipres unlocked YE2025** (was YE2024 stall) — took Walloon ETA **Sipres ASBL** YE2025 (KBO **{KBO}**; Rue Eva Dupont 11 Ghlin/Mons; **Actief** **2 VE**; NACE **88.993** AViQ / Province Hainaut). Deferred FREE **Stallbois** / **Brochage Renaitre** / **APRE** (all YE2025 live this tick). Do not redo La Lorraine/BW Eupen/AJR/Alteria stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** JUMP +{PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); neerlegging **17.07.2026**. Strong KBO Actief 2 VE ASBL. Assets/debt Unknown. Medium. FOI via info@sipres-services.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2264=done + rq_2265 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2264/ + data/raw/tick2264/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2260**; next **2270**). Next: rq_2265 (AGB/FARO-if-YE2025 / AIESH-REW / Stallbois-APRE-Renaitre YE2025).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2264"
    dst_raw = DATA / "raw" / "tick2264"
    dst_raw.mkdir(parents=True, exist_ok=True)
    for f in src_raw.glob("*"):
        if f.is_file():
            shutil.copy2(f, dst_raw / f.name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_sipres_jr2025_cw_nl",
                "title": "Companyweb NL Sipres YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl JUMP {PNL} "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 17.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2264/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Sipres YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 17-07-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_sipres_jr2025_cw_fr",
                "title": "Companyweb FR Sipres YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Bénéfice {PNL}",
            },
            {
                "source_id": f"src_sipres_kbo_{TICK}",
                "title": f"KBO Sipres {KBO} Actief Ghlin 2 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW/ASBL SIPRES; zetel Rue Eva Dupont (G.) 11 7011 Mons; "
                    f"2 VE; RSZ NACE 88.993; begindatum 03.02.1983; KBO email/web empty"
                ),
            },
            {
                "source_id": f"src_sipres_site_contact_{TICK}",
                "title": "Sipres FOI channel info@sipres-services.be",
                "url": "https://www.sipres-services.be/",
                "publisher": "Sipres ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@sipres-services.be; Rue Eva Dupont 11 Ghlin + Elouges site; "
                    "provincial Hainaut ETA (laundry/horticulture/painting/titres-services)"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_sipres_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW statutory omzet/turnover YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet JUMP +{OMZET_PCT}% vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_sipres_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": f"CW statutory bruto_marge YE2025 (~{RATIO}x omzet)",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +{BRUTO_PCT}% vs YE2024 {BRUTO24}; bruto÷omzet ~{RATIO}x",
            },
            {
                "budget_id": "bud_sipres_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl JUMP +{PNL_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_sipres_equity_jr2025_statutory",
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
                "budget_id": "bud_sipres_fte_jr2025_statutory",
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
                "budget_id": "bud_sipres_bruto_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(BRUTO24),
                "amount_min_eur": str(BRUTO24),
                "amount_max_eur": str(BRUTO24),
                "basis": "CW statutory bruto YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 bruto {BRUTO24} comparative (pre JUMP +{BRUTO_PCT}%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Sipres YE2025 leftover dual "
                    f"(omzet 2.54m / bruto~{RATIO}x / pnl JUMP +{PNL_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Ghlin-Elouges / Walloon adapted-work public path",
                "legal_basis": f"ASBL ETA Sipres (KBO {KBO}; Actief; 2 VE; NACE 88.993; Ghlin)",
                "decision_date": "2026-07-17",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(BRUTO),
                "cash_by_year": (
                    "{"
                    f'"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},'
                    f'"2024_omzet":{OMZET24},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}'
                    "}"
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "stated_goal": "Walloon ETA sheltered workshop Ghlin (laundry/horticulture/painting/titres-services)",
                "cut_option": (
                    f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x vs AViQ/Province ETA matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Hainaut>Sipres>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (~{RATIO}x omzet {OMZET}); pnl JUMP {PNL}; "
                    f"FTE {FTE}; 2 VE; unlocked YE2025 after YE2024 stall; after La Lorraine@2263; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
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
                    f"Sipres bruto 4.23m / omzet 2.54m / bruto~{RATIO}x / FTE {FTE} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Hainaut>Sipres>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW bruto {BRUTO} (+{BRUTO_PCT}%) / omzet {OMZET} (+{OMZET_PCT}%) / bruto÷omzet ~{RATIO}x / "
                    f"pnl JUMP {PNL} / equity JUMP {EQUITY} / FTE {FTE} (vs {FTE24}) / 2 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Ghlin-Elouges / Walloon adapted-work public path",
                "stated_goal": "Walloon ETA sheltered workshop Ghlin (Hainaut provincial)",
                "measured_outcome": (
                    f"bruto JUMP +{BRUTO_PCT}% (~{RATIO}x omzet); omzet JUMP +{OMZET_PCT}%; "
                    f"pnl JUMP +{PNL_PCT}%; equity JUMP +{EQUITY_PCT}%; FTE {FTE} (+{FTE_PCT}%); filed 17.07.2026"
                ),
                "absurdity_score": "7.3",
                "cost_score": "5.6",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    f"Publish NBB PDF assets/debt/cash FOI; disclose AViQ/Province ETA matrix behind bruto÷omzet ~{RATIO}x"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; Sipres unlocked YE2025; after La Lorraine@2263"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Sipres VZW (Ghlin / ETA maatwerk Henegouwen)",
                "name_fr": "Sipres ASBL (Ghlin / entreprise de travail adapté Hainaut)",
                "name_en": "Sipres adapted-work ASBL (Ghlin Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.sipres-services.be/",
                "foi_email": "info@sipres-services.be",
                "foi_postal": "Rue Eva Dupont 11, 7011 Ghlin",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE NACE 88.993; "
                    f"omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%) "
                    f"pnl JUMP {PNL} (+{PNL_PCT}%) equity JUMP {EQUITY} FTE {FTE}; neerlegging 17.07.2026; "
                    f"assets/debt Unknown; FOI {GAP}; unlocked YE2025 (was YE2024 stall); "
                    "after La Lorraine@2263; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Wallonie>Hainaut>Sipres>NBB_PDF_assets_debt_bruto_gt_omzet_1_67x",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); "
                    f"bruto EUR{BRUTO} (~{RATIO}x omzet EUR{OMZET}); AViQ/Province ETA subsidy matrix; "
                    f"FTE {FTE}; activity split Ghlin+Elouges"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (bruto 4.23m / omzet 2.54m / bruto~{RATIO}x / FTE {FTE}) "
                    "under AViQ/Province Hainaut path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Sipres ASBL",
                "recipient_email": "info@sipres-services.be",
                "recipient_postal": "Rue Eva Dupont 11, 7011 Ghlin",
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
                    "AGB Bornem JR2024; Sipres unlocked YE2025; after La Lorraine@2263; next EVERY-10 2270"
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
