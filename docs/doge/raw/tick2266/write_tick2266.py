# tick 2266 — leftover dual Brochage Renaitre YE2025 Medium (omzet 3.16m / bruto~1.78x / pnl LOSS WIDEN / FTE 159.2)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]  # .../data/raw/tick2266 -> repo root
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2266
UTC = "2026-08-27T08:40:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_brochage_renaitre_evere"
KBO = "0407.851.148"
KBO_BARE = "0407851148"
SRC_EN = "src_renaitre_jr2025_cw_en"
GAP = "gap_renaitre_nbb_pdf_assets_debt_bruto_gt_omzet_1_78x_pnl_loss_widen_eta_matrix_l5"
COMM = "comm_renaitre_jr2025_statutory_eta_bruto_gt_omzet_1_78x_pnl_loss_widen"
LB = "lb_renaitre_bruto_5_63m_omzet_3_16m_bruto_gt_omzet_1_78x_pnl_loss_widen_jr2025"
RQ = "rq_2266"
RQ_NEXT = "rq_2267"

OMZET = 3160438
OMZET24 = 2982859
BRUTO = 5629467
BRUTO24 = 4537343
PNL = -575836
PNL24 = -218840
EQUITY = 20384054
EQUITY24 = 21016819
FTE = 159.2
FTE24 = 155.7
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
LOSS_WIDEN_PCT = round((abs(PNL) - abs(PNL24)) / abs(PNL24) * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
RATIO = round(BRUTO / OMZET, 2)
PI = "6.25"


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
                "leftover dual — Brochage Renaitre YE2025 Medium "
                f"(omzet JUMP 3.16m / bruto~{RATIO}x / pnl LOSS WIDEN / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Brochage Renaitre ASBL Evere {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}%); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl LOSS WIDEN {PNL} (+{LOSS_WIDEN_PCT}% vs {PNL24}); equity DROP {EQUITY} ({EQUITY_PCT}%); "
                f"FTE {FTE} (+{FTE_PCT}% vs {FTE24}); 1 VE; NACE 88.993/18.140; neerlegging 03.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / "
                f"FARO/AIESH/REW YE2024; Relais Haute Sambre/APN YE2024; APRE YE2025 FREE deferred; "
                f"after Stallbois@2265; next EVERY-10 2270"
            )
            r["instructions"] = (
                "leftover dual Brochage Renaitre YE2025 FREE Brussels ETA after Stallbois; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Renaitre — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "APRE-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Brochage Renaitre YE2025 Medium "
                    f"(omzet JUMP 3.16m / bruto~{RATIO}x / pnl LOSS WIDEN / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else named FREE APRE YE2025 (0407.598.354), else unused ETA/VAPH/WZC/maatwerk. "
                    "Skip Brochage Renaitre/Stallbois/Sipres/La Lorraine/BW Eupen/AJR/Alteria/Les Erables/"
                    "Val du Geer/Nekto/Belair/Corelap/Cambier/Gaillettes/Hunelle/Dauphins Gembloux/Saupont/"
                    "Serviplast/Jean Del'Cour/TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/"
                    "Jean Gielen/Le Perron/L'Atelier/Axedis/ETA 123 Beauraing/Manufast/Metalgroup/"
                    "EntrAnam/Enghien/Entra/Ateliers de Tertre/Le Rucher/Het Rekreatief/Travie/SDB/"
                    "De Vleugels/Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/Den Azalee/"
                    "Kemphaan/Mirto/Blankedale/Werkmmaat; Relais Haute Sambre/APN YE2024; Citeco YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2270."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Brochage Renaitre; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024; "
                    "APRE YE2025 FREE deferred; next every-10 2270"
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
                f"tick{TICK} leftover dual Brochage Renaitre {KBO} Medium (omzet JUMP {OMZET} +{OMZET_PCT}%; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl LOSS WIDEN {PNL}; equity DROP {EQUITY}; FTE {FTE}; "
                f"1 VE Evere Brussels ETA PHARE/bookbinding); after Stallbois@2265; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; Relais Haute Sambre/APN YE2024; APRE YE2025 FREE; "
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
        f"""# FOI draft — Brochage Renaitre (NBB PDF / bruto÷omzet ~{RATIO}x / pnl LOSS WIDEN / PHARE ETA matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Brochage Renaitre ASBL — KBO **{KBO}** (Actief; Stroobantsstraat 48 bus C/D, 1140 Evere; **1 VE**; FTE {FTE} CW; NACE **88.993** / BTW **18.140**; Brussels ETA PHARE)  
**recipient:** info@brochage-renaitre.be · Rue Stroobants 48 c/d, 1140 Evere (+32 2 216 00 37)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.brochage-renaitre.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW BROCHAGE RENAITRE; **1 VE**; zetel Stroobantsstraat 48 bus C/D, 1140 Evere; RSZ NACE **88.993**; BTW NACE **18.140**; begindatum 08.10.1970.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS WIDEN +{LOSS_WIDEN_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP {EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); filed **03.07.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024. After Stallbois@2265. Deferred FREE APRE YE2025.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Brochage Renaitre ASBL
via info@brochage-renaitre.be
Rue Stroobants 48 c/d, 1140 Evere
Objet: Publicité des comptes annuels 2025 Brochage Renaitre (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région de Bruxelles-Capitale / PHARE / COCOF), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Explication de la perte élargie EUR{PNL} vs EUR{PNL24} (+{LOSS_WIDEN_PCT}%) et de la baisse des fonds propres EUR{EQUITY} ({EQUITY_PCT}%).
3. Matrice des subsides PHARE / ETA / COCOF derrière les charges de personnel (FTE {FTE}) et le ratio marge brute/CA ~{RATIO}x.
4. Répartition CA/activités (brochage / pliage / collage / finition / sous-traitance).
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


### 2026-08-27T08:40:00Z - tick 2266 - rq_2266 Brochage Renaitre Evere (omzet JUMP 3.16m / bruto~{RATIO}x / pnl LOSS WIDEN / FTE {FTE} / Medium)

- Unit: **rq_2266** leftover dual after **rq_2265 Stallbois**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW last balansjaar 2024); AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre/APN still **YE2024**. Took named FREE Brussels ETA **Brochage Renaitre ASBL** YE2025 (KBO **{KBO}**; Stroobantsstraat 48 C/D Evere; **Actief** **1 VE**; NACE **88.993** PHARE / bookbinding). Deferred FREE **APRE** YE2025 (0407.598.354). Do not redo Stallbois/Sipres/La Lorraine/BW Eupen/AJR/Alteria stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** LOSS WIDEN +{LOSS_WIDEN_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); neerlegging **03.07.2026**. Strong KBO Actief 1 VE ASBL. Assets/debt Unknown. Medium. FOI via info@brochage-renaitre.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2266=done + rq_2267 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2266/ + data/raw/tick2266/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2260**; next **2270**). Next: rq_2267 (AGB/FARO-if-YE2025 / AIESH-REW / APRE YE2025).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2266"
    dst_raw = DATA / "raw" / "tick2266"
    dst_raw.mkdir(parents=True, exist_ok=True)
    src_raw.mkdir(parents=True, exist_ok=True)
    for f in (DATA / "raw" / "tick2266").glob("*.html"):
        shutil.copy2(f, src_raw / f.name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_renaitre_jr2025_cw_nl",
                "title": "Companyweb NL Brochage Renaitre YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl LOSS WIDEN {PNL} "
                    f"equity DROP {EQUITY} FTE {FTE}; neerlegging 03.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2266/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Brochage Renaitre YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 03-07-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_renaitre_jr2025_cw_fr",
                "title": "Companyweb FR Brochage Renaitre YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Perte {PNL}",
            },
            {
                "source_id": f"src_renaitre_kbo_{TICK}",
                "title": f"KBO Brochage Renaitre {KBO} Actief Evere 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW BROCHAGE RENAITRE; zetel Stroobantsstraat 48 bus C/D 1140 Evere; "
                    f"1 VE; RSZ NACE 88.993; BTW NACE 18.140; begindatum 08.10.1970; KBO email/web empty"
                ),
            },
            {
                "source_id": f"src_renaitre_site_contact_{TICK}",
                "title": "Brochage Renaitre FOI channel info@brochage-renaitre.be",
                "url": "https://www.brochage-renaitre.be/",
                "publisher": "Brochage Renaitre ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@brochage-renaitre.be / devis@brochage-renaitre.be / jobs@brochage-renaitre.be; "
                    "+32 2 216 00 37; Rue Stroobants 48 c/d Evere; Brussels ETA PHARE (brochage/bookbinding)"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_renaitre_omzet_jr2025_statutory",
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
                "budget_id": "bud_renaitre_bruto_jr2025_statutory",
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
                "budget_id": "bud_renaitre_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025 LOSS WIDEN",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl LOSS WIDEN +{LOSS_WIDEN_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_renaitre_equity_jr2025_statutory",
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
                "budget_id": "bud_renaitre_fte_jr2025_statutory",
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
                "budget_id": "bud_renaitre_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory pnl YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre LOSS WIDEN +{LOSS_WIDEN_PCT}%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Brochage Renaitre YE2025 leftover dual "
                    f"(bruto 5.63m / omzet 3.16m / pnl LOSS WIDEN / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Evere / Brussels adapted-work public path PHARE",
                "legal_basis": f"ASBL ETA Brochage Renaitre (KBO {KBO}; Actief; 1 VE; NACE 88.993; Evere)",
                "decision_date": "2026-07-03",
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
                "stated_goal": "Brussels ETA sheltered workshop Evere (brochage/bookbinding/finishing)",
                "cut_option": (
                    "Publish NBB PDF assets/debt; reconcile bruto÷omzet ~1.78x + LOSS WIDEN vs PHARE/COCOF ETA matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Bruxelles>Evere>BrochageRenaitre>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (~{RATIO}x omzet {OMZET}); "
                    f"pnl LOSS WIDEN {PNL}; equity DROP {EQUITY}; FTE {FTE}; 1 VE; after Stallbois@2265; "
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
                    f"Brochage Renaitre bruto 5.63m / omzet 3.16m / bruto÷omzet ~{RATIO}x / "
                    f"pnl LOSS WIDEN / FTE {FTE} (YE2025 Brussels ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Bruxelles>Evere>BrochageRenaitre>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW omzet {OMZET} (+{OMZET_PCT}%) / bruto {BRUTO} (+{BRUTO_PCT}%) / bruto÷omzet ~{RATIO}x / "
                    f"pnl LOSS WIDEN {PNL} / equity DROP {EQUITY} ({EQUITY_PCT}%) / FTE {FTE} (vs {FTE24}) / 1 VE Brussels ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Evere / Brussels adapted-work public path PHARE",
                "stated_goal": "Brussels ETA sheltered workshop Evere (brochage/bookbinding)",
                "measured_outcome": (
                    f"omzet JUMP +{OMZET_PCT}%; bruto JUMP +{BRUTO_PCT}%; "
                    f"pnl LOSS WIDEN +{LOSS_WIDEN_PCT}%; equity DROP {EQUITY_PCT}%; FTE {FTE} (+{FTE_PCT}%); filed 03.07.2026"
                ),
                "absurdity_score": "7.5",
                "cost_score": "5.6",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose PHARE/COCOF ETA matrix behind bruto÷omzet ~1.78x + LOSS WIDEN"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Stallbois@2265"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Brochage Renaitre VZW (Evere / Brussels ETA maatwerk)",
                "name_fr": "Brochage Renaitre ASBL (Evere / entreprise de travail adapté bruxelloise)",
                "name_en": "Brochage Renaitre adapted-work ASBL (Evere Brussels ETA)",
                "level": "parastatal",
                "parent_id": "sec_brussels",
                "community_language": "fr",
                "website": "https://www.brochage-renaitre.be/",
                "foi_email": "info@brochage-renaitre.be",
                "foi_postal": "Rue Stroobants 48 c/d, 1140 Evere",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%) "
                    f"pnl LOSS WIDEN {PNL} equity DROP {EQUITY} ({EQUITY_PCT}%) FTE {FTE}; neerlegging 03.07.2026; "
                    f"assets/debt Unknown; FOI {GAP}; after Stallbois@2265; AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Bruxelles>Evere>BrochageRenaitre>NBB_PDF_assets_debt_bruto_gt_omzet_1_78x_pnl_loss_widen",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); "
                    f"bruto EUR{BRUTO} (~{RATIO}x omzet EUR{OMZET}); pnl LOSS WIDEN EUR{PNL} vs EUR{PNL24}; "
                    f"PHARE/COCOF ETA subsidy matrix; FTE {FTE}; activity split brochage/binding"
                ),
                "why_it_matters": (
                    f"Medium CW shows Brussels ETA ASBL (bruto 5.63m / omzet 3.16m / bruto~{RATIO}x / "
                    f"pnl LOSS WIDEN / FTE {FTE}) under PHARE path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Brochage Renaitre ASBL",
                "recipient_email": "info@brochage-renaitre.be",
                "recipient_postal": "Rue Stroobants 48 c/d, 1140 Evere",
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
                    "AGB Bornem JR2024; after Stallbois@2265; next EVERY-10 2270"
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
