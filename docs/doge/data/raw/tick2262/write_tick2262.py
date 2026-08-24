# tick 2262 — leftover dual BW Eupen YE2025 Medium
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2262
UTC = "2026-08-27T07:40:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_bw_eupen"
KBO = "0412.778.847"
KBO_BARE = "0412778847"
SRC_EN = "src_bw_eupen_jr2025_cw_en"
GAP = "gap_bw_eupen_nbb_pdf_assets_debt_bruto_gt_omzet_2_05x_pnl_loss_narrow_eta_matrix_l5"
COMM = "comm_bw_eupen_jr2025_statutory_eta_bruto_gt_omzet_2_05x_pnl_loss_narrow"
LB = "lb_bw_eupen_omzet_2_17m_bruto_2_05x_pnl_loss_narrow_jr2025"
RQ = "rq_2262"
RQ_NEXT = "rq_2263"

OMZET = 2165804
OMZET24 = 1843209
BRUTO = 4442051
BRUTO24 = 3938247
PNL = -22080
PNL24 = -49473
EQUITY = 3599551
EQUITY24 = 3752647
FTE = 128
FTE24 = 121.4
RATIO = round(BRUTO / OMZET, 2)
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_NARROW_PCT = round((abs(PNL24) - abs(PNL)) / abs(PNL24) * 100, 2)
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
                "leftover dual — BW Eupen YE2025 Medium "
                f"(omzet JUMP 2.17m / +{OMZET_PCT}% / bruto~{RATIO}x / pnl LOSS NARROW / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; BW Eupen / Beschutzende Werkstatte Eupen Und Umgebung ASBL {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}% vs {OMZET24}); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl LOSS NARROW {PNL} ({PNL_NARROW_PCT}% vs {PNL24}); equity DROP {EQUITY} ({EQUITY_PCT}%); "
                f"FTE {FTE} (+{FTE_PCT}% vs {FTE24}); 1 VE; NACE 88.993; neerlegging 23.06.2026; assets/debt Unknown; "
                f"FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
                f"La Lorraine Services YE2025 FREE deferred; Relais Haute Sambre/Sipres/APN/Stallbois YE2024; "
                f"after AJR@2261; next EVERY-10 2270"
            )
            r["instructions"] = (
                "leftover dual BW Eupen YE2025 FREE DG ETA after AJR; "
                "preferred AGB/FARO/AIESH/REW still YE2024; La Lorraine YE2025 deferred"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after BW Eupen — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused La Lorraine-YE2025-or-ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after BW Eupen YE2025 Medium "
                    f"(omzet JUMP 2.17m / +{OMZET_PCT}% / bruto~{RATIO}x / pnl LOSS NARROW / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused La Lorraine Services YE2025 FREE (KBO 0412.131.719; deferred this tick), "
                    "else unused ETA/VAPH/WZC/maatwerk. "
                    "Skip BW Eupen/AJR/Alteria/Les Erables/Val du Geer/Nekto/Belair/Corelap/Cambier/"
                    "Gaillettes/Hunelle/Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/TRAVCO/Pilifs/"
                    "Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/"
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
                    f"spawned after tick{TICK} BW Eupen; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "La Lorraine YE2025 FREE deferred; Relais Haute Sambre/Sipres/APN/Stallbois YE2024; next every-10 2270"
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
                f"tick{TICK} leftover dual BW Eupen {KBO} Medium (omzet JUMP {OMZET} +{OMZET_PCT}%; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl LOSS NARROW {PNL}; equity DROP {EQUITY}; FTE {FTE}; 1 VE Eupen DG ETA); "
                f"after AJR@2261; AGB Bornem JR2024; FARO/AIESH/REW YE2024; La Lorraine YE2025 deferred; "
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
        f"""# FOI draft — BW Eupen (NBB PDF / bruto≫omzet ~{RATIO}x / pnl LOSS NARROW)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** BW Eupen ASBL (Beschützende Werkstätte Eupen und Umgebung) — KBO **{KBO}** (Actief; Gewerbestrasse 13, 4700 Eupen; **1 VE**; FTE {FTE} CW; NACE **88.993**; DG ETA Eupen)  
**recipient:** info@bweupen.be · Gewerbestrasse 13, 4700 Eupen  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.bweupen.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL BESCHUTZENDE WERKSTATTE EUPEN UND UMGEBUNG; **1 VE**; zetel Eupen; BTW+RSZ NACE **88.993**; begindatum 20.11.1972.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS NARROW {PNL_NARROW_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP {EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); filed **23.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; La Lorraine Services YE2025 FREE deferred; Relais Haute Sambre/Sipres/APN/Stallbois YE2024. After AJR@2261.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: BW Eupen ASBL — Beschützende Werkstätte Eupen und Umgebung
via info@bweupen.be
Gewerbestrasse 13, 4700 Eupen
Objet: Publicité des comptes annuels 2025 BW Eupen (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Communauté germanophone / Wallonie), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OMZET} JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24} / marge brute EUR{BRUTO} (~{RATIO}x CA).
3. PnL LOSS NARROW EUR{PNL} ({PNL_NARROW_PCT}% vs YE2024 EUR{PNL24}) — réconciliation avec FTE {FTE} (vs {FTE24}).
4. Matrice des subsides DG / ETA derrière les charges de personnel.
5. Répartition CA par activité (sous-traitance / services).

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


### 2026-08-27T07:40:00Z - tick 2262 - rq_2262 BW Eupen (omzet JUMP 2.17m / +{OMZET_PCT}% / bruto~{RATIO}x / pnl LOSS NARROW / FTE {FTE} / Medium)

- Unit: **rq_2262** leftover dual after **rq_2261 AJR**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre/Sipres/APN/Stallbois still **YE2024**. Took named FREE DG ETA **BW Eupen / Beschützende Werkstätte Eupen und Umgebung ASBL** YE2025 (KBO **{KBO}**; Gewerbestrasse 13 Eupen; **Actief** **1 VE**; NACE **88.993**). Deferred FREE **La Lorraine Services** YE2025 (KBO 0412.131.719). Do not redo AJR/Alteria/Les Erables/Val du Geer/Nekto/Belair/Corelap stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL}** LOSS NARROW {PNL_NARROW_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); neerlegging **23.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@bweupen.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.05); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2262=done + rq_2263 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2262/ + data/raw/tick2262/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2260**; next **2270**). Next: rq_2263 (AGB/FARO-if-YE2025 / AIESH-REW / unused La Lorraine YE2025).
"""
        )
    print("loop_log appended")


def main():
    # keep data/raw mirror
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2262"
    dst_raw = DATA / "raw" / "tick2262"
    dst_raw.mkdir(parents=True, exist_ok=True)
    for f in src_raw.glob("*"):
        if f.is_file():
            shutil.copy2(f, dst_raw / f.name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_bw_eupen_jr2025_cw_nl",
                "title": "Companyweb NL BW Eupen YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} pnl LOSS NARROW {PNL} equity DROP {EQUITY} "
                    f"bruto {BRUTO} FTE {FTE}; neerlegging 23.06.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2262/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN BW Eupen YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 23-06-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_bw_eupen_jr2025_cw_fr",
                "title": "Companyweb FR BW Eupen YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Perte {PNL}",
            },
            {
                "source_id": f"src_bw_eupen_kbo_{TICK}",
                "title": f"KBO BW Eupen {KBO} Actief Eupen 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW/ASBL BESCHUTZENDE WERKSTATTE EUPEN UND UMGEBUNG; "
                    f"zetel Gewerbestrasse 13 4700 Eupen; 1 VE; BTW+RSZ NACE 88.993; begindatum 20.11.1972; KBO email/web empty"
                ),
            },
            {
                "source_id": f"src_bw_eupen_site_contact_{TICK}",
                "title": "BW Eupen FOI channel info@bweupen.be",
                "url": "https://www.bweupen.be/kontakt/",
                "publisher": "BW Eupen ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@bweupen.be; Tel +32 (0)87/56 01 83; "
                    "Gewerbestrasse 13 4700 Eupen; also leseta.be annuaire"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_bw_eupen_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW statutory omzet YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet JUMP +{OMZET_PCT}% vs YE2024 {OMZET24} (primary envelope)",
            },
            {
                "budget_id": "bud_bw_eupen_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +{BRUTO_PCT}%; bruto/omzet ~{RATIO}x",
            },
            {
                "budget_id": "bud_bw_eupen_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl LOSS NARROW {PNL_NARROW_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_bw_eupen_equity_jr2025_statutory",
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
                "budget_id": "bud_bw_eupen_fte_jr2025_statutory",
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
                "budget_id": "bud_bw_eupen_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory winst YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre LOSS NARROW)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "BW Eupen YE2025 leftover dual "
                    f"(omzet JUMP 2.17m / +{OMZET_PCT}% / bruto~{RATIO}x / pnl LOSS NARROW / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Eupen / DG adapted-work public path",
                "legal_basis": f"ASBL ETA BW Eupen Beschutzende Werkstatte (KBO {KBO}; Actief; 1 VE; NACE 88.993; Eupen)",
                "decision_date": "2026-06-23",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    "{"
                    f'"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET24},'
                    f'"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}'
                    "}"
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "stated_goal": "DG ETA sheltered workshop Eupen und Umgebung services/subcontracting",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; reconcile bruto≫omzet ~2.05x + ongoing loss vs DG ETA subsidy matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "DG>Eupen>BW_Eupen>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; pnl LOSS NARROW {PNL}; "
                    f"FTE {FTE}; 1 VE; after AJR@2261; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "La Lorraine YE2025 deferred; not TE-additive of 348bn"
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
                    f"BW Eupen omzet JUMP 2.17m / bruto~{RATIO}x / pnl LOSS NARROW / FTE {FTE} "
                    "(YE2025 DG ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "DG>Eupen>BW_Eupen>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW omzet JUMP {OMZET} (+{OMZET_PCT}%) / bruto {BRUTO} (~{RATIO}x) / pnl LOSS NARROW {PNL} / "
                    f"equity DROP {EQUITY} / FTE {FTE} (vs {FTE24}) / 1 VE DG ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Eupen / DG adapted-work public path",
                "stated_goal": "DG ETA sheltered workshop Eupen und Umgebung",
                "measured_outcome": (
                    f"omzet JUMP +{OMZET_PCT}%; bruto JUMP +{BRUTO_PCT}% (~{RATIO}x); pnl LOSS NARROW {PNL_NARROW_PCT}%; "
                    f"equity DROP {EQUITY_PCT}%; FTE {FTE} (+{FTE_PCT}%); filed 23.06.2026"
                ),
                "absurdity_score": "7.6",
                "cost_score": "5.5",
                "difficulty": "3.0",
                "priority_index": "6.05",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose DG ETA matrix; "
                    "reconcile bruto≫omzet ~2.05x + ongoing loss despite omzet JUMP"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; La Lorraine YE2025 deferred; after AJR@2261"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "BW Eupen VZW / Beschutzende Werkstatte Eupen und Umgebung (DG ETA Eupen)",
                "name_fr": "BW Eupen ASBL / Atelier protégé Eupen et environs (ETA CG Eupen)",
                "name_en": "BW Eupen / Beschützende Werkstätte Eupen und Umgebung adapted-work ASBL (DG ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "de",
                "website": "https://www.bweupen.be/",
                "foi_email": "info@bweupen.be",
                "foi_postal": "Gewerbestrasse 13, 4700 Eupen",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto JUMP {BRUTO} (~{RATIO}x) pnl LOSS NARROW {PNL} equity DROP {EQUITY} "
                    f"FTE {FTE}; neerlegging 23.06.2026; assets/debt Unknown; FOI {GAP}; "
                    "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; La Lorraine YE2025 deferred; after AJR@2261; "
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
                "hierarchy_path": "DG>Eupen>BW_Eupen>NBB_PDF_assets_debt_bruto_gt_omzet_2_05x_pnl_loss_narrow",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OMZET} JUMP +{OMZET_PCT}% / "
                    f"bruto EUR{BRUTO} (~{RATIO}x); pnl LOSS NARROW EUR{PNL} ({PNL_NARROW_PCT}% vs YE2024 EUR{PNL24}); "
                    f"FTE {FTE}; DG ETA subsidy matrix"
                ),
                "why_it_matters": (
                    f"Medium CW shows DG ETA ASBL (omzet JUMP 2.17m / bruto~{RATIO}x / pnl LOSS NARROW / FTE {FTE}) "
                    "under DG adapted-work path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "BW Eupen ASBL — Beschützende Werkstätte Eupen und Umgebung",
                "recipient_email": "info@bweupen.be",
                "recipient_postal": "Gewerbestrasse 13, 4700 Eupen",
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
                    "AGB Bornem JR2024; La Lorraine YE2025 deferred; after AJR@2261; next EVERY-10 2270"
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
