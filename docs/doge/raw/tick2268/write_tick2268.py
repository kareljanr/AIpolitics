# tick 2268 — leftover dual L'Ouvroir YE2025 Medium (omzet 0.80m / bruto~1.59x / pnl PROFIT FLIP / FTE 41.3)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2268
UTC = "2026-08-27T09:10:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_louvroir_bruxelles"
KBO = "0407.722.573"
KBO_BARE = "0407722573"
SRC_EN = "src_louvroir_jr2025_cw_en"
GAP = "gap_louvroir_nbb_pdf_assets_debt_bruto_gt_omzet_1_59x_pnl_profit_flip_eta_matrix_l5"
COMM = "comm_louvroir_jr2025_statutory_eta_bruto_gt_omzet_1_59x_pnl_profit_flip"
LB = "lb_louvroir_bruto_1_26m_omzet_0_80m_bruto_gt_omzet_1_59x_pnl_profit_flip_jr2025"
RQ = "rq_2268"
RQ_NEXT = "rq_2269"

OMZET = 796261
OMZET24 = 816763
BRUTO = 1262350
BRUTO24 = 1224804
PNL = 63141
PNL24 = -39784
EQUITY = 2286584
EQUITY24 = 2284761
FTE = 41.3
FTE24 = 44.1
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_FLIP_PCT = round((PNL - PNL24) / abs(PNL24) * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
RATIO = round(BRUTO / OMZET, 2)
PI = "5.55"


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
                "leftover dual — L'Ouvroir YE2025 Medium "
                f"(omzet DROP 0.80m / bruto~{RATIO}x / pnl PROFIT FLIP / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; L'Ouvroir ASBL Bruxelles {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet DROP {OMZET} ({OMZET_PCT}%); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl PROFIT FLIP {PNL} (+{PNL_FLIP_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE} ({FTE_PCT}% vs {FTE24}); 1 VE; NACE 88.993/18.140; neerlegging 03.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / "
                f"FARO/AIESH/REW YE2024; Relais Haute Sambre/APN YE2024; "
                f"after APRE@2267; next EVERY-10 2270"
            )
            r["instructions"] = (
                "leftover dual L'Ouvroir YE2025 FREE Brussels ETA after APRE; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after L'Ouvroir — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after L'Ouvroir YE2025 Medium "
                    f"(omzet DROP 0.80m / bruto~{RATIO}x / pnl PROFIT FLIP / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk with live sourced euros. "
                    "Skip L'Ouvroir/APRE/Brochage Renaitre/Stallbois/Sipres/La Lorraine/BW Eupen/"
                    "AJR/Alteria/Les Erables/Val du Geer/Nekto/Belair/Corelap/Cambier/Gaillettes/"
                    "Hunelle/Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/TRAVCO/Pilifs/"
                    "Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/"
                    "ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/"
                    "Ateliers de Tertre/Le Rucher/Het Rekreatief/Travie/SDB/De Vleugels/"
                    "Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/Den Azalee/"
                    "Kemphaan/Mirto/Blankedale/Werkmmaat/ATE Ensival; Relais Haute Sambre/APN YE2024; "
                    "Citeco YE2024; FOES YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/"
                    "Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/"
                    "Atrias/RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/"
                    "Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2270 (MUST refresh progress + waste top10 then hole-fill)."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} L'Ouvroir; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024; "
                    "next every-10 2270 MUST"
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
                f"tick{TICK} leftover dual L'Ouvroir {KBO} Medium (omzet DROP {OMZET} {OMZET_PCT}%; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl PROFIT FLIP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; "
                f"1 VE Bruxelles ETA PHARE/bookbinding-mailing); after APRE@2267; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; Relais Haute Sambre/APN YE2024; next {RQ_NEXT}; "
                "next EVERY-10 2270; continuous hole_fill"
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
        f"""# FOI draft — L'Ouvroir (NBB PDF / bruto÷omzet ~{RATIO}x / pnl PROFIT FLIP / PHARE ETA matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** L'Ouvroir ASBL — KBO **{KBO}** (Actief; Bodegemstraat 78-82A, 1000 Brussel; **1 VE**; FTE {FTE} CW; NACE **88.993** / BTW **18.140**; Brussels ETA PHARE / bookbinding-mailing)  
**recipient:** louvroir@louvroir.be · Rue Bodeghem 78-82a, 1000 Bruxelles (+32 2 511 04 17)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.louvroir.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW L'OUVROIR; **1 VE**; zetel Bodegemstraat 78-82A, 1000 Brussel; RSZ NACE **88.993**; BTW NACE **18.140**; begindatum 30.06.1927.
- CW YE2025: omzet **EUR{OMZET:,}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** PROFIT FLIP +{PNL_FLIP_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); filed **03.07.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024 (CW last balansjaar 2024; reconfirmed); AIESH/REW YE2024; Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024. After APRE@2267.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: L'Ouvroir ASBL
via louvroir@louvroir.be
Rue Bodeghem 78-82a, 1000 Bruxelles
Objet: Publicité des comptes annuels 2025 L'Ouvroir (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région de Bruxelles-Capitale / PHARE / COCOF), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Explication du retournement de résultat EUR{PNL} vs EUR{PNL24} (+{PNL_FLIP_PCT}%) et du ratio marge brute/CA ~{RATIO}x.
3. Matrice des subsides PHARE / ETA / COCOF derrière les charges de personnel (FTE {FTE}).
4. Répartition CA/activités (reliure / mailing / cartonnage / upcycling / confection).
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


### 2026-08-27T09:10:00Z - tick 2268 - rq_2268 L'Ouvroir Bruxelles (omzet DROP 0.80m / bruto~{RATIO}x / pnl PROFIT FLIP / FTE {FTE} / Medium)

- Unit: **rq_2268** leftover dual after **rq_2267 APRE**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW last balansjaar 2024; reconfirmed this tick); AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre/APN still **YE2024**. Took unused FREE Brussels ETA **L'Ouvroir ASBL** YE2025 (KBO **{KBO}**; Bodegemstraat 78-82A Bruxelles; **Actief** **1 VE**; NACE **88.993** PHARE / bookbinding-mailing). Do not redo APRE/Renaitre/Stallbois/Sipres/La Lorraine stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** PROFIT FLIP +{PNL_FLIP_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); neerlegging **03.07.2026**. Strong KBO Actief 1 VE ASBL. Assets/debt Unknown. Medium. FOI via louvroir@louvroir.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2268=done + rq_2269 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2268/ + data/raw/tick2268/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2260**; next **2270** MUST). Next: rq_2269 (AGB/FARO-if-YE2025 / AIESH-REW / unused ETA-VAPH-WZC-maatwerk).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2268"
    dst_raw = DATA / "raw" / "tick2268"
    dst_raw.mkdir(parents=True, exist_ok=True)
    for f in src_raw.glob("*.html"):
        shutil.copy2(f, dst_raw / f.name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_louvroir_jr2025_cw_nl",
                "title": "Companyweb NL L'Ouvroir YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet DROP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl PROFIT FLIP {PNL} "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 03.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2268/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN L'Ouvroir YE2025 statutory",
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
                "source_id": "src_louvroir_jr2025_cw_fr",
                "title": "Companyweb FR L'Ouvroir YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Benefice {PNL}",
            },
            {
                "source_id": f"src_louvroir_kbo_{TICK}",
                "title": f"KBO L'Ouvroir {KBO} Actief Bruxelles 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW L'OUVROIR; zetel Bodegemstraat 78-82A 1000 Brussel; "
                    f"1 VE; RSZ NACE 88.993; BTW NACE 18.140; begindatum 30.06.1927; KBO email/web empty"
                ),
            },
            {
                "source_id": f"src_louvroir_site_contact_{TICK}",
                "title": "L'Ouvroir FOI channel louvroir@louvroir.be",
                "url": "https://www.louvroir.be/",
                "publisher": "L'Ouvroir ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; louvroir@louvroir.be; +32 2 511 04 17; "
                    "Rue Bodeghem 78-82a Bruxelles; Brussels ETA PHARE (reliure/mailing/cartonnage)"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_louvroir_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW statutory omzet/turnover YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet DROP {OMZET_PCT}% vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_louvroir_bruto_jr2025_statutory",
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
                "budget_id": "bud_louvroir_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025 PROFIT FLIP",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl PROFIT FLIP +{PNL_FLIP_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_louvroir_equity_jr2025_statutory",
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
                "budget_id": "bud_louvroir_fte_jr2025_statutory",
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
                "budget_id": "bud_louvroir_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory pnl YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre PROFIT FLIP +{PNL_FLIP_PCT}%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "L'Ouvroir YE2025 leftover dual "
                    f"(bruto 1.26m / omzet 0.80m / pnl PROFIT FLIP / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Bruxelles / Brussels adapted-work public path PHARE",
                "legal_basis": f"ASBL ETA L'Ouvroir (KBO {KBO}; Actief; 1 VE; NACE 88.993; Bruxelles)",
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
                "stated_goal": "Brussels ETA sheltered workshop (reliure/mailing/cartonnage/upcycling)",
                "cut_option": (
                    "Publish NBB PDF assets/debt; reconcile bruto÷omzet ~1.59x + PROFIT FLIP vs PHARE/COCOF ETA matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Bruxelles>Centre>LOuvroir>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (~{RATIO}x omzet {OMZET}); "
                    f"pnl PROFIT FLIP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 1 VE; after APRE@2267; "
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
                    f"L'Ouvroir bruto 1.26m / omzet 0.80m / bruto÷omzet ~{RATIO}x / "
                    f"pnl PROFIT FLIP / FTE {FTE} (YE2025 Brussels ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Bruxelles>Centre>LOuvroir>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW omzet {OMZET} ({OMZET_PCT}%) / bruto {BRUTO} (+{BRUTO_PCT}%) / bruto÷omzet ~{RATIO}x / "
                    f"pnl PROFIT FLIP {PNL} / equity JUMP {EQUITY} (+{EQUITY_PCT}%) / FTE {FTE} (vs {FTE24}) / 1 VE Brussels ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Bruxelles / Brussels adapted-work public path PHARE",
                "stated_goal": "Brussels ETA sheltered workshop (reliure/mailing/cartonnage)",
                "measured_outcome": (
                    f"omzet DROP {OMZET_PCT}%; bruto JUMP +{BRUTO_PCT}%; "
                    f"pnl PROFIT FLIP +{PNL_FLIP_PCT}%; equity JUMP +{EQUITY_PCT}%; FTE {FTE} ({FTE_PCT}%); filed 03.07.2026"
                ),
                "absurdity_score": "6.6",
                "cost_score": "4.2",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose PHARE/COCOF ETA matrix behind bruto÷omzet ~1.59x + PROFIT FLIP"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after APRE@2267"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "L'Ouvroir VZW (Brussel / Brussels ETA maatwerk)",
                "name_fr": "L'Ouvroir ASBL (Bruxelles / entreprise de travail adapté bruxelloise)",
                "name_en": "L'Ouvroir adapted-work ASBL (Brussels ETA)",
                "level": "parastatal",
                "parent_id": "sec_brussels",
                "community_language": "fr",
                "website": "https://www.louvroir.be/",
                "foi_email": "louvroir@louvroir.be",
                "foi_postal": "Rue Bodeghem 78-82a, 1000 Bruxelles",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet DROP {OMZET} ({OMZET_PCT}%) bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%) "
                    f"pnl PROFIT FLIP {PNL} equity JUMP {EQUITY} (+{EQUITY_PCT}%) FTE {FTE}; "
                    f"neerlegging 03.07.2026; assets/debt Unknown; FOI {GAP}; after APRE@2267; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Bruxelles>Centre>LOuvroir>NBB_PDF_assets_debt_bruto_gt_omzet_1_59x_pnl_profit_flip",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); "
                    f"bruto EUR{BRUTO} (~{RATIO}x omzet EUR{OMZET}); pnl PROFIT FLIP EUR{PNL} vs EUR{PNL24}; "
                    f"PHARE/COCOF ETA subsidy matrix; FTE {FTE}; activity split reliure/mailing"
                ),
                "why_it_matters": (
                    f"Medium CW shows Brussels ETA ASBL (bruto 1.26m / omzet 0.80m / bruto~{RATIO}x / "
                    f"pnl PROFIT FLIP / FTE {FTE}) under PHARE path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "L'Ouvroir ASBL",
                "recipient_email": "louvroir@louvroir.be",
                "recipient_postal": "Rue Bodeghem 78-82a, 1000 Bruxelles",
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
                    "AGB Bornem JR2024; after APRE@2267; next EVERY-10 2270"
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
