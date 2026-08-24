# tick 2260 — EVERY-10 + Alteria Colfontaine YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2260
UTC = "2026-08-27T07:10:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_alteria_colfontaine"
KBO = "0476.855.364"
KBO_BARE = "0476855364"
SRC_EN = "src_alteria_jr2025_cw_en"
GAP = "gap_alteria_nbb_pdf_assets_debt_bruto_gt_omzet_1_72x_pnl_drop_88pct_eta_matrix_l5"
COMM = "comm_alteria_jr2025_statutory_eta_bruto_gt_omzet_pnl_drop_88pct"
LB = "lb_alteria_omzet_3_12m_pnl_drop_88pct_jr2025"
RQ = "rq_2260"
RQ_NEXT = "rq_2261"

OMZET = 3115001
OMZET24 = 3026171
BRUTO = 5351920
BRUTO24 = 4942521
PNL = 72779
PNL24 = 592478
EQUITY = 1966154
EQUITY24 = 1895513
FTE = 212.4
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
                "EVERY-10 + leftover dual — Alteria YE2025 Medium "
                f"(omzet 3.12m / pnl DROP {PNL_PCT}% / bruto~{RATIO}x / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; EVERY-10 refreshed; Alteria ASBL Colfontaine {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}%); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE}; 1 VE; NACE 88.993; neerlegging 08.07.2026; assets/debt Unknown; "
                f"FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
                f"Relais Haute Sambre/Sipres/APN/Stallbois YE2024; after Les Erables@2259; next EVERY-10 2270"
            )
            r["instructions"] = (
                "EVERY-10 progress+top10 then leftover dual Alteria YE2025 FREE Walloon ETA"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Alteria — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Alteria YE2025 Medium "
                    f"(omzet 3.12m / pnl DROP {PNL_PCT}% / bruto~{RATIO}x / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. AJR / La Lorraine / BW Eupen / Adapta "
                    "if YE2025 FREE; skip Alteria/Les Erables/Val du Geer/Nekto/Belair/Corelap/Cambier/"
                    "Gaillettes/Hunelle/Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/TRAVCO/Pilifs/"
                    "Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/"
                    "ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers de Tertre/"
                    "Le Rucher/Het Rekreatief/Travie/SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/"
                    "Kringwinkel*/Manus*/Reset/Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; "
                    "Relais Haute Sambre/Sipres/APN/Stallbois YE2024). "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2270."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} EVERY-10 + Alteria; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Relais Haute Sambre/Sipres/APN/Stallbois YE2024; next every-10 2270"
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
                f"tick{TICK} EVERY-10 + leftover Alteria {KBO} Medium (omzet JUMP {OMZET}; "
                f"pnl DROP {PNL} {PNL_PCT}%; bruto JUMP {BRUTO} ~{RATIO}x; equity JUMP {EQUITY}; FTE {FTE}; 1 VE Colfontaine ETA); "
                f"after Les Erables@2259; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre/Sipres/APN/Stallbois YE2024; "
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
        f"""# FOI draft — Alteria (NBB PDF / pnl DROP {PNL_PCT}% / bruto≫omzet ~{RATIO}x)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Alteria ASBL — KBO **{KBO}** (Actief; Rue Grande 5-7, 7340 Colfontaine; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Colfontaine)  
**recipient:** info@eta-alteria.be · Rue Grande 5-7, 7340 Colfontaine  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://eta-alteria.be/)  
**tick:** {TICK} EVERY-10  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL ALTERIA; **1 VE**; zetel Colfontaine; NACE **88.993** (+88.995); aanbestedende overheid.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}**; filed **08.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre/Sipres/APN/Stallbois YE2024. After Les Erables@2259. EVERY-10@2260 primary.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Alteria ASBL
via info@eta-alteria.be
Rue Grande 5-7, 7340 Colfontaine
Objet: Publicité des comptes annuels 2025 Alteria (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OMZET} / marge brute EUR{BRUTO} (~{RATIO}x).
3. PnL DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}) — réconciliation avec FTE {FTE}.
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition coûts toiture / peinture / menuiserie / reliure / couture / sous-traitance.

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

### 2026-08-27T07:10:00Z - tick 2260 - rq_2260 EVERY-10 + Alteria Colfontaine (omzet 3.12m / pnl DROP {PNL_PCT}% / bruto~{RATIO}x / FTE {FTE} / Medium)

- **EVERY-10:** refreshed `progress_every_10_ticks.md` (A **100%** / B **100%** / C **~99%** / D **~74-88%** generous residual dual / E **~1914** FOI-ready) and `doge_waste_top10_current.md` (GIP #1; fossil/cars/cheque/reporté #2-10 stable; Alteria off pure top10). Next every-10: **2270**.
- Unit: **rq_2260** leftover dual after **rq_2259 Les Erables**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre/Sipres/APN/Stallbois still **YE2024**. Took named FREE Walloon ETA **Alteria ASBL** YE2025 (KBO **{KBO}**; Rue Grande 5-7 Colfontaine; **Actief** **1 VE**; NACE **88.993** AViQ). Do not redo Les Erables/Val du Geer/Nekto/Belair stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}**; neerlegging **08.07.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@eta-alteria.be.
- Wrote: progress+top10; sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.10); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2260=done + rq_2261 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2260/.
- FOI: **ready not sent** (human-gated).
- EVERY-10@**2260** done. Next: rq_2261 (AGB/FARO-if-YE2025 / AIESH-REW / unused). Next every-10 **2270**.
"""
        )
    print("loop_log appended")


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_alteria_jr2025_cw_nl",
                "title": "Companyweb NL Alteria YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} "
                    f"bruto {BRUTO} FTE {FTE}; neerlegging 08.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2260/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Alteria YE2025 statutory",
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
                "source_id": "src_alteria_jr2025_cw_fr",
                "title": "Companyweb FR Alteria YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Bénéfice {PNL}",
            },
            {
                "source_id": f"src_alteria_kbo_{TICK}",
                "title": f"KBO Alteria {KBO} Actief Colfontaine 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW/ASBL ALTERIA; zetel Rue Grande 5-7 7340 Colfontaine; "
                    f"1 VE; NACE 88.993/88.995; begindatum 21.12.2001; aanbestedende overheid; KBO email empty"
                ),
            },
            {
                "source_id": f"src_alteria_site_contact_{TICK}",
                "title": "Alteria FOI channel info@eta-alteria.be",
                "url": "https://eta-alteria.be/",
                "publisher": "Alteria ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@eta-alteria.be / jobs@eta-alteria.be; "
                    "Rue Grande 5-7 7340 Colfontaine; also leseta.be annuaire"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_alteria_omzet_jr2025_statutory",
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
                "budget_id": "bud_alteria_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +{BRUTO_PCT}%; bruto≫omzet ~{RATIO}x",
            },
            {
                "budget_id": "bud_alteria_pnl_jr2025_statutory",
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
                "budget_id": "bud_alteria_equity_jr2025_statutory",
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
                "budget_id": "bud_alteria_fte_jr2025_statutory",
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
                "budget_id": "bud_alteria_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory winst YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre DROP -88%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Alteria YE2025 leftover dual EVERY-10 "
                    f"(omzet 3.12m / pnl DROP {PNL_PCT}% / bruto~{RATIO}x / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Colfontaine / AVIQ adapted-work public path",
                "legal_basis": f"ASBL ETA Alteria (KBO {KBO}; Actief; 1 VE; NACE 88.993; Colfontaine)",
                "decision_date": "2026-07-08",
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
                "stated_goal": "Walloon ETA roofing / painting / joinery / binding / sewing Colfontaine",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; reconcile pnl DROP -88% vs AVIQ ETA subsidy matrix; "
                    f"explain bruto≫omzet ~{RATIO}x"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Hainaut>Colfontaine>Alteria>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; pnl DROP {PNL}; "
                    f"FTE {FTE}; 1 VE; after Les Erables@2259; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
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
                    f"Alteria omzet 3.12m / pnl DROP {PNL_PCT}% / bruto~{RATIO}x / FTE {FTE} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Hainaut>Colfontaine>Alteria>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW omzet {OMZET} / bruto {BRUTO} (~{RATIO}x) / pnl DROP {PNL} ({PNL_PCT}%) / "
                    f"equity JUMP {EQUITY} / FTE {FTE} / 1 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Colfontaine / AVIQ adapted-work public path",
                "stated_goal": "Walloon ETA roofing / painting / joinery / binding / sewing",
                "measured_outcome": (
                    f"omzet JUMP +{OMZET_PCT}%; bruto JUMP +{BRUTO_PCT}%; pnl DROP {PNL_PCT}%; "
                    f"equity JUMP +{EQUITY_PCT}%; FTE {FTE}; filed 08.07.2026"
                ),
                "absurdity_score": "7.7",
                "cost_score": "4.5",
                "difficulty": "3.0",
                "priority_index": "6.10",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
                    "reconcile pnl DROP -88% + bruto≫omzet"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK} EVERY-10 primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Les Erables@2259"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Alteria VZW (Colfontaine / ETA maatwerk Henegouwen)",
                "name_fr": "Alteria ASBL (Colfontaine / entreprise de travail adapté Hainaut)",
                "name_en": "Alteria adapted-work ASBL (Colfontaine Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://eta-alteria.be/",
                "foi_email": "info@eta-alteria.be",
                "foi_postal": "Rue Grande 5-7, 7340 Colfontaine",
                "notes": (
                    f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} "
                    f"FTE {FTE}; neerlegging 08.07.2026; assets/debt Unknown; FOI {GAP}; "
                    "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; after Les Erables@2259; "
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
                "hierarchy_path": "Wallonie>Hainaut>Colfontaine>Alteria>NBB_PDF_assets_debt_pnl_drop_88pct",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OMZET} / "
                    f"bruto EUR{BRUTO} (~{RATIO}x); pnl DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}); "
                    f"FTE {FTE}; AVIQ ETA subsidy matrix"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (omzet 3.12m / pnl DROP {PNL_PCT}% / FTE {FTE}) "
                    "under AVIQ path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Alteria ASBL",
                "recipient_email": "info@eta-alteria.be",
                "recipient_postal": "Rue Grande 5-7, 7340 Colfontaine",
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
                    "AGB Bornem JR2024; after Les Erables@2259; EVERY-10@2260; next EVERY-10 2270"
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
