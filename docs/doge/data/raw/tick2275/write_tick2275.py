# tick 2275 — leftover dual A.P.A.C. YE2025 Medium (bruto DROP 3.15m / empty omzet / pnl DROP -66.88% / FTE 89)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2275
UTC = "2026-08-27T10:55:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_apac_manage"
KBO = "0456.685.007"
KBO_BARE = "0456685007"
SRC_EN = "src_apac_jr2025_cw_en"
GAP = "gap_apac_nbb_pdf_assets_debt_empty_omzet_bruto_3_15m_pnl_drop_67pct_eta_matrix_l5"
COMM = "comm_apac_jr2025_statutory_eta_empty_omzet_bruto_3_15m_pnl_drop"
LB = "lb_apac_bruto_3_15m_empty_omzet_pnl_drop_67pct_jr2025"
RQ = "rq_2275"
RQ_NEXT = "rq_2276"

BRUTO = 3145869
BRUTO24 = 3287566
PNL = 43469
PNL24 = 131226
EQUITY = 2254927
EQUITY24 = 2241559
FTE = 89.0
FTE24 = 93.0
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / abs(PNL24) * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
PI = "5.70"


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
                "leftover dual — A.P.A.C. YE2025 Medium "
                f"(bruto DROP 3.15m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; A.P.A.C. ASBL Manage {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet unpublished; bruto DROP {BRUTO} ({BRUTO_PCT}%); "
                f"pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE} ({FTE_PCT}% vs {FTE24}); 1 VE; NACE 88.993; neerlegging 11.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / "
                f"FARO/AIESH/Citeco/Groupe Foes YE2024; after Atelier85@2274; next EVERY-10 2280"
            )
            r["instructions"] = (
                "leftover dual A.P.A.C. YE2025 FREE Walloon ETA Manage after Atelier 85; "
                "preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after A.P.A.C. — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after A.P.A.C. YE2025 Medium "
                    f"(bruto DROP 3.15m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                    "else unused ETA-VAPH-WZC-maatwerk (Adapta/Criquelion/Roseau Vert if YE2025). "
                    "Skip A.P.A.C./Atelier 85/La Gaume/Fournipac/De Enter/La Serre-Outil/"
                    "Amis des Aveugles/Hautes Ardennes/Village n°1/Le Trait d'Union/L'Ouvroir/"
                    "APRE/Brochage Renaitre/Stallbois/Sipres/La Lorraine/BW Eupen/AJR/Alteria; "
                    "Relais Haute Sambre/APN YE2024; Citeco/Groupe Foes YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/"
                    "Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/"
                    "RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Senes. Next EVERY-10: 2280."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} A.P.A.C.; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                    "AGB Bornem JR2024; next every-10 2280"
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
                f"tick{TICK} leftover dual A.P.A.C. {KBO} Medium (bruto DROP {BRUTO} {BRUTO_PCT}%; "
                f"empty omzet; pnl DROP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; "
                f"1 VE Manage Walloon ETA AViQ paper/textile/packaging); after Atelier85@2274; "
                f"AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; next {RQ_NEXT}; "
                f"next EVERY-10 2280; continuous hole_fill"
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
        f"""# FOI draft — A.P.A.C. (NBB PDF / empty omzet / bruto 3.15m / pnl DROP {PNL_PCT}% / Walloon ETA)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** A.P.A.C. ASBL — KBO **{KBO}** (Actief; rue du Chenia 13/A, 7170 Manage; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA AViQ)  
**recipient:** info@apac-belgium.be · rue du Chenia 13/A, 7170 Manage (+32 64 23 87 16)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.apac-belgium.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown; omzet unpublished)

## Context
- KBO Strong: Actief VZW A.P.A.C.; **1 VE**; zetel rue du Chenia 13 bus A, 7170 Manage; BTW/RSZ NACE **88.993**; begindatum 25.04.1995.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** DROP {BRUTO_PCT}% vs YE2024 EUR{BRUTO24:,}; pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); filed **11.07.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024. After Atelier 85@2274.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: A.P.A.C. ASBL
via info@apac-belgium.be
rue du Chenia 13/A, 7170 Manage
Objet: Publicité des comptes annuels 2025 A.P.A.C. (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région wallonne / AViQ / Code de la démocratie locale), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Chiffre d'affaires YE2025 (non publié sur Companyweb) et explication de la baisse de
   marge brute EUR{BRUTO} ({BRUTO_PCT}%) et du bénéfice EUR{PNL} ({PNL_PCT}% vs EUR{PNL24}).
3. Matrice des subsides AViQ / ETA derrière les charges de personnel (FTE {FTE}).
4. Répartition CA/activités (façonnage papier / textile / conditionnement / entreposage).
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


### 2026-08-27T10:55:00Z - tick 2275 - rq_2275 A.P.A.C. Manage (bruto DROP 3.15m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2275** leftover dual after **rq_2274 Atelier 85**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**. Took FREE Walloon ETA **A.P.A.C. ASBL** YE2025 (KBO **{KBO}**; rue du Chenia 13/A Manage; **Actief** **1 VE**; NACE **88.993** AViQ paper/textile/packaging). Do not redo Atelier85/La Gaume/Fournipac/De Enter/Serre-Outil/Amis/Hautes stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** DROP {BRUTO_PCT}% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); neerlegging **11.07.2026**. Strong KBO Actief 1 VE ASBL. Assets/debt Unknown. Medium. FOI via info@apac-belgium.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2275=done + rq_2276 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2275/ + data/raw/tick2275/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2270**; next **2280**). Next: rq_2276 (AGB/FARO-if-YE2025 / AIESH-REW / Citeco-Foes-if-YE2025 / unused ETA).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2275"
    dst_raw = DATA / "raw" / "tick2275"
    dst_raw.mkdir(parents=True, exist_ok=True)
    src_raw.mkdir(parents=True, exist_ok=True)
    for f in dst_raw.glob("*.html"):
        shutil.copy2(f, src_raw / f.name)
    shutil.copy2(Path(__file__), src_raw / Path(__file__).name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_apac_jr2025_cw_nl",
                "title": "Companyweb NL A.P.A.C. YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet unpublished bruto DROP {BRUTO} pnl DROP {PNL} "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 11.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2275/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN A.P.A.C. YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 11-07-2026; Last balance sheet year 2025; "
                    f"Turnover unpublished Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_apac_jr2025_cw_fr",
                "title": "Companyweb FR A.P.A.C. YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA unpublished; Marge brute {BRUTO}; Benefice {PNL}",
            },
            {
                "source_id": f"src_apac_kbo_{TICK}",
                "title": f"KBO A.P.A.C. {KBO} Actief Manage 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW A.P.A.C.; zetel rue du Chenia 13 bus A 7170 Manage; "
                    f"1 VE; NACE 88.993; begindatum 25.04.1995"
                ),
            },
            {
                "source_id": f"src_apac_site_contact_{TICK}",
                "title": "A.P.A.C. FOI channel info@apac-belgium.be",
                "url": "https://www.apac-belgium.be/",
                "publisher": "A.P.A.C. ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@apac-belgium.be; +32 64 23 87 16; "
                    "rue du Chenia 13/A Manage; Walloon ETA AViQ paper/textile/packaging"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_apac_bruto_jr2025_statutory",
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
                "budget_id": "bud_apac_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025 DROP",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl DROP {PNL_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_apac_equity_jr2025_statutory",
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
                "budget_id": "bud_apac_fte_jr2025_statutory",
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
                "budget_id": "bud_apac_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory pnl YE2024 comparative",
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
                    "A.P.A.C. YE2025 leftover dual "
                    f"(bruto 3.15m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Manage / Walloon adapted-work public path AViQ",
                "legal_basis": f"ASBL ETA A.P.A.C. (KBO {KBO}; Actief; 1 VE; NACE 88.993; Manage)",
                "decision_date": "2026-07-11",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(BRUTO),
                "cash_by_year": (
                    "{"
                    f'"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},'
                    f'"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}'
                    "}"
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "stated_goal": "Walloon ETA sheltered workshop Manage (paper finishing/textile/packaging/warehousing)",
                "cut_option": (
                    "Publish NBB PDF assets/debt + omzet; reconcile bruto DROP + pnl DROP vs AViQ ETA matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Hainaut>Manage>APAC>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (omzet unpublished); "
                    f"pnl DROP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 1 VE; after Atelier85@2274; "
                    "AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
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
                    f"A.P.A.C. bruto 3.15m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} "
                    "(YE2025 Walloon ETA Manage)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Hainaut>Manage>APAC>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW bruto {BRUTO} ({BRUTO_PCT}%) / omzet unpublished / pnl DROP {PNL} ({PNL_PCT}%) / "
                    f"equity JUMP {EQUITY} (+{EQUITY_PCT}%) / FTE {FTE} (vs {FTE24}) / 1 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Manage / Walloon adapted-work public path AViQ",
                "stated_goal": "Walloon ETA sheltered workshop Manage (paper/textile/packaging)",
                "measured_outcome": (
                    f"bruto DROP {BRUTO_PCT}%; omzet unpublished; pnl DROP {PNL_PCT}%; "
                    f"equity JUMP +{EQUITY_PCT}%; FTE {FTE} ({FTE_PCT}%); filed 11.07.2026"
                ),
                "absurdity_score": "6.8",
                "cost_score": "4.2",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/omzet FOI; disclose AViQ ETA matrix behind empty omzet + pnl DROP 67%"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/Citeco/Groupe Foes YE2024; after Atelier85@2274"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "A.P.A.C. VZW (Manage / Walloon ETA maatwerk)",
                "name_fr": "A.P.A.C. ASBL (Manage / entreprise de travail adapté wallonne)",
                "name_en": "A.P.A.C. adapted-work ASBL (Manage Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.apac-belgium.be/",
                "foi_email": "info@apac-belgium.be",
                "foi_postal": "rue du Chenia 13/A, 7170 Manage",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet unpublished bruto DROP {BRUTO} ({BRUTO_PCT}%) pnl DROP {PNL} ({PNL_PCT}%) "
                    f"equity JUMP {EQUITY} (+{EQUITY_PCT}%) FTE {FTE}; neerlegging 11.07.2026; "
                    f"assets/debt Unknown; FOI {GAP}; after Atelier85@2274; AGB Bornem JR2024; "
                    "FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Wallonie>Hainaut>Manage>APAC>NBB_PDF_assets_debt_empty_omzet_bruto_3_15m",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet unpublished on CW; "
                    f"bruto EUR{BRUTO}; pnl DROP EUR{PNL} vs EUR{PNL24}; "
                    f"AViQ ETA subsidy matrix; FTE {FTE}; activity split paper/textile/packaging"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (bruto 3.15m / empty omzet / pnl DROP {PNL_PCT}% / "
                    f"FTE {FTE}) under AViQ path; assets/debt/omzet unpublished"
                ),
                "priority": "8",
                "recipient_body": "A.P.A.C. ASBL",
                "recipient_email": "info@apac-belgium.be",
                "recipient_postal": "rue du Chenia 13/A, 7170 Manage",
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
                    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/Citeco/Foes YE2024; "
                    "AGB Bornem JR2024; after Atelier85@2274; next EVERY-10 2280"
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
