# tick 2265 — leftover dual Stallbois YE2025 Medium (omzet JUMP 4.00m / pnl LOSS NARROW / FTE 95.7)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2265
UTC = "2026-08-27T08:25:00Z"
DATE = "2026-08-27"
ENTITY = "sc_stallbois_etalle"
KBO = "0407.149.877"
KBO_BARE = "0407149877"
SRC_EN = "src_stallbois_jr2025_cw_en"
GAP = "gap_stallbois_nbb_pdf_assets_debt_pnl_loss_narrow_equity_drop_eta_matrix_l5"
COMM = "comm_stallbois_jr2025_statutory_eta_pnl_loss_narrow_equity_drop"
LB = "lb_stallbois_omzet_4_00m_pnl_loss_narrow_equity_drop_fte_95_7_jr2025"
RQ = "rq_2265"
RQ_NEXT = "rq_2266"

OMZET = 3999436
OMZET24 = 3828140
BRUTO = 1795431
BRUTO24 = 1540732
PNL = -174496
PNL24 = -192014
EQUITY = 3773006
EQUITY24 = 4177465
FTE = 95.7
FTE24 = 96.5
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
LOSS_NARROW_PCT = round((abs(PNL24) - abs(PNL)) / abs(PNL24) * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
RATIO = round(BRUTO / OMZET, 2)
PI = "5.95"


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
                "leftover dual — Stallbois YE2025 Medium "
                f"(omzet JUMP 4.00m / +{OMZET_PCT}% / pnl LOSS NARROW / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Stallbois SC/CV Etalle {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}%); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl LOSS NARROW {PNL} ({LOSS_NARROW_PCT}% vs {PNL24}); equity DROP {EQUITY} ({EQUITY_PCT}%); "
                f"FTE {FTE} ({FTE_PCT}% vs {FTE24}); 1 VE; NACE 88.993; neerlegging 30.06.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / "
                f"FARO/AIESH/REW YE2024; Relais Haute Sambre/APN YE2024; APRE/Renaitre YE2025 FREE deferred; "
                f"after Sipres@2264; next EVERY-10 2270"
            )
            r["instructions"] = (
                "leftover dual Stallbois YE2025 FREE Walloon ETA after Sipres; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Stallbois — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "APRE-Renaitre-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Stallbois YE2025 Medium "
                    f"(omzet JUMP 4.00m / +{OMZET_PCT}% / pnl LOSS NARROW / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else named FREE Brochage Renaitre YE2025 (0407.851.148) / APRE YE2025 "
                    "(0407.598.354), else unused ETA/VAPH/WZC/maatwerk. "
                    "Skip Stallbois/Sipres/La Lorraine/BW Eupen/AJR/Alteria/Les Erables/Val du Geer/"
                    "Nekto/Belair/Corelap/Cambier/Gaillettes/Hunelle/Dauphins Gembloux/Saupont/"
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
                    f"spawned after tick{TICK} Stallbois; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024; "
                    "APRE/Renaitre YE2025 FREE deferred; next every-10 2270"
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
                f"tick{TICK} leftover dual Stallbois {KBO} Medium (omzet JUMP {OMZET} +{OMZET_PCT}%; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl LOSS NARROW {PNL}; equity DROP {EQUITY}; FTE {FTE}; "
                f"1 VE Etalle Walloon ETA Luxembourg province); after Sipres@2264; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; Relais Haute Sambre/APN YE2024; APRE/Renaitre YE2025 FREE; "
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
        f"""# FOI draft — Stallbois (NBB PDF / pnl LOSS NARROW / equity DROP / AViQ ETA matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Stallbois SC/CV — KBO **{KBO}** (Actief; Zoning de Belle-Vue 2, 6740 Etalle; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Luxembourg province)  
**recipient:** info@stallbois.be · Zoning de Belle-Vue 2, 6740 Etalle (+32 63 45 53 19)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://stallbois.eu/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief SC/CV STALLBOIS; **1 VE**; zetel Zoning de Belle-Vue 2, 6740 Etalle; RSZ NACE **88.993**; begindatum 15.02.1968.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS NARROW {LOSS_NARROW_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP {EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); filed **30.06.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024. After Sipres@2264. Deferred FREE APRE/Renaitre YE2025.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Stallbois SC
via info@stallbois.be
Zoning de Belle-Vue 2, 6740 Etalle
Objet: Publicité des comptes annuels 2025 Stallbois (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Wallonie / AViQ / Province de Luxembourg), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Explication de la perte réduite EUR{PNL} vs EUR{PNL24} et de la baisse des fonds propres EUR{EQUITY} ({EQUITY_PCT}%).
3. Matrice des subsides AViQ / ETA / Province de Luxembourg derrière les charges de personnel (FTE {FTE}).
4. Répartition CA/activités (menuiserie / boissellerie / PLV / abris / construction bois).
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


### 2026-08-27T08:25:00Z - tick 2265 - rq_2265 Stallbois Etalle (omzet JUMP 4.00m / +{OMZET_PCT}% / pnl LOSS NARROW / FTE {FTE} / Medium)

- Unit: **rq_2265** leftover dual after **rq_2264 Sipres**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre/APN still **YE2024**. Took named FREE Walloon ETA **Stallbois SC/CV** YE2025 (KBO **{KBO}**; Zoning de Belle-Vue 2 Etalle; **Actief** **1 VE**; NACE **88.993** AViQ / Province Luxembourg). Deferred FREE **Brochage Renaitre** / **APRE** (both YE2025 live this tick). Do not redo Sipres/La Lorraine/BW Eupen/AJR/Alteria stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** LOSS NARROW {LOSS_NARROW_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); neerlegging **30.06.2026**. Strong KBO Actief 1 VE SC/CV. Assets/debt Unknown. Medium. FOI via info@stallbois.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2265=done + rq_2266 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2265/ + data/raw/tick2265/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2260**; next **2270**). Next: rq_2266 (AGB/FARO-if-YE2025 / AIESH-REW / APRE-Renaitre YE2025).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2265"
    dst_raw = DATA / "raw" / "tick2265"
    dst_raw.mkdir(parents=True, exist_ok=True)
    for f in src_raw.glob("*"):
        if f.is_file():
            shutil.copy2(f, dst_raw / f.name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_stallbois_jr2025_cw_nl",
                "title": "Companyweb NL Stallbois YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl LOSS NARROW {PNL} "
                    f"equity DROP {EQUITY} FTE {FTE}; neerlegging 30.06.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2265/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Stallbois YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 30-06-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_stallbois_jr2025_cw_fr",
                "title": "Companyweb FR Stallbois YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Perte {PNL}",
            },
            {
                "source_id": f"src_stallbois_kbo_{TICK}",
                "title": f"KBO Stallbois {KBO} Actief Etalle 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief SC/CV STALLBOIS; zetel Zoning de Belle-Vue 2 6740 Etalle; "
                    f"1 VE; RSZ NACE 88.993; begindatum 15.02.1968; KBO email/web empty"
                ),
            },
            {
                "source_id": f"src_stallbois_site_contact_{TICK}",
                "title": "Stallbois FOI channel info@stallbois.be",
                "url": "https://stallbois.eu/",
                "publisher": "Stallbois SC",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@stallbois.be / rh@stallbois.be; +32 63 45 53 19; "
                    "Zoning Belle-Vue 2 Etalle; Walloon ETA Luxembourg province (menuiserie/boissellerie)"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_stallbois_omzet_jr2025_statutory",
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
                "budget_id": "bud_stallbois_bruto_jr2025_statutory",
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
                "budget_id": "bud_stallbois_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025 LOSS NARROW",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl LOSS NARROW {LOSS_NARROW_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_stallbois_equity_jr2025_statutory",
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
                "budget_id": "bud_stallbois_fte_jr2025_statutory",
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
                "budget_id": "bud_stallbois_equity_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(EQUITY24),
                "amount_min_eur": str(EQUITY24),
                "amount_max_eur": str(EQUITY24),
                "basis": "CW statutory equity YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 equity {EQUITY24} comparative (pre DROP {EQUITY_PCT}%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Stallbois YE2025 leftover dual "
                    f"(omzet JUMP 4.00m / pnl LOSS NARROW / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Etalle / Walloon adapted-work public path Luxembourg province",
                "legal_basis": f"SC/CV ETA Stallbois (KBO {KBO}; Actief; 1 VE; NACE 88.993; Etalle)",
                "decision_date": "2026-06-30",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    "{"
                    f'"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},'
                    f'"2024_omzet":{OMZET24},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}'
                    "}"
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "stated_goal": "Walloon ETA sheltered workshop Etalle (menuiserie/boissellerie/PLV/abris)",
                "cut_option": (
                    "Publish NBB PDF assets/debt; reconcile multi-year LOSS path + equity DROP vs AViQ/Province ETA matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Luxembourg>Stallbois>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; bruto {BRUTO} (~{RATIO}x); "
                    f"pnl LOSS NARROW {PNL}; equity DROP {EQUITY}; FTE {FTE}; 1 VE; after Sipres@2264; "
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
                    f"Stallbois omzet 4.00m / pnl LOSS NARROW / equity DROP / FTE {FTE} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_sc_statutory",
                "hierarchy_path": "Wallonie>Luxembourg>Stallbois>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW omzet {OMZET} (+{OMZET_PCT}%) / bruto {BRUTO} (+{BRUTO_PCT}%) / bruto÷omzet ~{RATIO}x / "
                    f"pnl LOSS NARROW {PNL} / equity DROP {EQUITY} ({EQUITY_PCT}%) / FTE {FTE} (vs {FTE24}) / 1 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Etalle / Walloon adapted-work public path Luxembourg province",
                "stated_goal": "Walloon ETA sheltered workshop Etalle (Luxembourg provincial)",
                "measured_outcome": (
                    f"omzet JUMP +{OMZET_PCT}%; bruto JUMP +{BRUTO_PCT}%; "
                    f"pnl LOSS NARROW {LOSS_NARROW_PCT}%; equity DROP {EQUITY_PCT}%; FTE {FTE} ({FTE_PCT}%); filed 30.06.2026"
                ),
                "absurdity_score": "7.1",
                "cost_score": "5.4",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AViQ/Province ETA matrix behind multi-year LOSS + equity DROP"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Sipres@2264"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Stallbois CV (Etalle / ETA maatwerk Luxemburg)",
                "name_fr": "Stallbois SC (Etalle / entreprise de travail adapté Luxembourg)",
                "name_en": "Stallbois adapted-work SC (Etalle Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://stallbois.eu/",
                "foi_email": "info@stallbois.be",
                "foi_postal": "Zoning de Belle-Vue 2, 6740 Etalle",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%) "
                    f"pnl LOSS NARROW {PNL} equity DROP {EQUITY} ({EQUITY_PCT}%) FTE {FTE}; neerlegging 30.06.2026; "
                    f"assets/debt Unknown; FOI {GAP}; after Sipres@2264; AGB Bornem JR2024; "
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
                "hierarchy_path": "Wallonie>Luxembourg>Stallbois>NBB_PDF_assets_debt_pnl_loss_narrow_equity_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); "
                    f"pnl LOSS NARROW EUR{PNL} vs EUR{PNL24}; equity DROP EUR{EQUITY} ({EQUITY_PCT}%); "
                    f"AViQ/Province ETA subsidy matrix; FTE {FTE}; activity split menuiserie/boissellerie"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA SC (omzet 4.00m / pnl LOSS NARROW / equity DROP / FTE {FTE}) "
                    "under AViQ/Province Luxembourg path; multi-year loss + equity erosion; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Stallbois SC",
                "recipient_email": "info@stallbois.be",
                "recipient_postal": "Zoning de Belle-Vue 2, 6740 Etalle",
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
                    "AGB Bornem JR2024; after Sipres@2264; next EVERY-10 2270"
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
