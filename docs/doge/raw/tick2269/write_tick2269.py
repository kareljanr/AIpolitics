# tick 2269 — leftover dual Village n°1 Entreprises YE2025 Medium (omzet DROP 12.15m / bruto~1.49x / pnl LOSS FLIP / FTE 609.1)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2269
UTC = "2026-08-27T09:25:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_village_n1_entreprises_braine"
KBO = "0411.648.501"
KBO_BARE = "0411648501"
SRC_EN = "src_village_n1_jr2025_cw_en"
GAP = "gap_village_n1_nbb_pdf_assets_debt_bruto_gt_omzet_1_49x_pnl_loss_flip_eta_matrix_l5"
COMM = "comm_village_n1_jr2025_statutory_eta_bruto_gt_omzet_1_49x_pnl_loss_flip"
LB = "lb_village_n1_bruto_18_11m_omzet_12_15m_bruto_gt_omzet_1_49x_pnl_loss_flip_jr2025"
RQ = "rq_2269"
RQ_NEXT = "rq_2270"

OMZET = 12147204
OMZET24 = 13390903
BRUTO = 18111184
BRUTO24 = 18776685
PNL = -255560
PNL24 = 38226
EQUITY = 9034193
EQUITY24 = 9388987
FTE = 609.1
FTE24 = 618.4
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_FLIP_PCT = round((PNL - PNL24) / abs(PNL24) * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
RATIO = round(BRUTO / OMZET, 2)
PI = "6.85"


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
                "leftover dual — Village n°1 Entreprises YE2025 Medium "
                f"(omzet DROP 12.15m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Village n°1 Entreprises ASBL Braine-le-Château {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet DROP {OMZET} ({OMZET_PCT}%); bruto DROP {BRUTO} (~{RATIO}x / {BRUTO_PCT}%); "
                f"pnl LOSS FLIP {PNL} ({PNL_FLIP_PCT}% vs {PNL24}); equity DROP {EQUITY} ({EQUITY_PCT}%); "
                f"FTE {FTE} ({FTE_PCT}% vs {FTE24}); 1 VE; NACE 88.999; neerlegging 17.06.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / "
                f"FARO/AIESH YE2024; after Trait@2268+Ouvroir race; next EVERY-10 2270 MUST"
            )
            r["instructions"] = (
                "leftover dual Village n°1 YE2025 FREE Walloon ETA Braine-le-Château after Trait/Ouvroir; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "EVERY-10 + leftover dual after Village n°1 — prefer AGB/FARO-YE2025/"
                    "AIESH-REW/Amis Aveugles-Hautes Ardennes-or-unused ETA"
                ),
                "sprint": "hole_fill",
                "priority": "10",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "EVERY-10 MANDATORY first: refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
                    "Then leftover dual after Village n°1 YE2025 Medium "
                    f"(omzet DROP 12.15m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else named FREE Les Amis des Aveugles (0406.579.854) / Les Hautes Ardennes "
                    "(0407.574.994) if YE2025 unused, else unused ETA/VAPH/WZC/maatwerk. "
                    "Skip Village n°1/Le Trait d'Union/L'Ouvroir/APRE/Brochage Renaitre/Stallbois/"
                    "Sipres/La Lorraine/BW Eupen/AJR/Alteria/Les Erables/Val du Geer/Nekto/Belair/"
                    "Corelap/Cambier/Gaillettes/Hunelle/Dauphins/Saupont/Serviplast/Jean Del'Cour/"
                    "TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/"
                    "L'Atelier/Axedis/Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers de Tertre/"
                    "Le Rucher/Het Rekreatief/Travie/SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/"
                    "Kringwinkel*/Manus*/Reset/Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; "
                    "Relais Haute Sambre/APN YE2024; Citeco YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/"
                    "Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/"
                    "RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Senes. Next EVERY-10 after this: 2280."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Village n°1; MUST every-10 at 2270; "
                    "FARO/AIESH YE2024; AGB Bornem JR2024; Amis Aveugles/Hautes Ardennes YE2025 FREE deferred"
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
                f"tick{TICK} leftover dual Village n°1 {KBO} Medium (omzet DROP {OMZET} {OMZET_PCT}%; "
                f"bruto DROP {BRUTO} ~{RATIO}x; pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE {FTE}; "
                f"1 VE Braine-le-Château Walloon ETA AViQ); after Trait+Ouvroir@2268 race; AGB Bornem JR2024; "
                f"FARO/AIESH YE2024; next {RQ_NEXT} EVERY-10 MUST; next EVERY-10 2270; continuous hole_fill"
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
        f"""# FOI draft — Village n°1 Entreprises (NBB PDF / bruto÷omzet ~{RATIO}x / pnl LOSS FLIP / Walloon ETA matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Village n°1 Entreprises ASBL — KBO **{KBO}** (Actief; Avenue Reine Astrid 1, 1440 Braine-le-Château / Wauthier-Braine; **1 VE**; FTE {FTE} CW; NACE **88.999**; Walloon ETA AViQ)  
**recipient:** entreprises@levillage1.be · Avenue Reine Astrid 1, 1440 Wauthier-Braine (+32 2 386 06 11)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.levillage1.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW Village n°1 Entreprises; **1 VE**; zetel Avenue Reine Astrid(W-B) 1, 1440 Braine-le-Château; BTW NACE **88.999** (+ construction codes); begindatum 24.11.1971; tel 02-386-06-11.
- CW YE2025: omzet **EUR{OMZET:,}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** DROP {BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS FLIP {PNL_FLIP_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP {EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); filed **17.06.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024 (0201.712.587); Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024. After Trait d'Union + L'Ouvroir @2268 race. Deferred FREE Amis des Aveugles / Hautes Ardennes YE2025.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Village n°1 Entreprises ASBL
via entreprises@levillage1.be
Avenue Reine Astrid 1, 1440 Wauthier-Braine
Objet: Publicité des comptes annuels 2025 Village n°1 Entreprises (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région wallonne / AViQ / Code de la démocratie locale), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Explication de la perte EUR{PNL} (FLIP vs bénéfice EUR{PNL24}, {PNL_FLIP_PCT}%) et de la
   baisse du CA EUR{OMZET} ({OMZET_PCT}%) / marge brute EUR{BRUTO} (bruto÷omzet ~{RATIO}x).
3. Matrice des subsides AViQ / ETA derrière les charges de personnel (FTE {FTE}).
4. Répartition CA/activités (conditionnement / numérisation / call center / nettoyage / espaces verts).
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


### 2026-08-27T09:25:00Z - tick 2269 - rq_2269 Village n°1 Entreprises Braine-le-Château (omzet DROP 12.15m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE} / Medium)

- Unit: **rq_2269** leftover dual after **rq_2268 Trait d'Union + L'Ouvroir race**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024** (0201.712.587); Heropbeuring still **CW opaque**; Relais Haute Sambre/APN still **YE2024**. Took named FREE Walloon ETA **Village n°1 Entreprises ASBL** YE2025 (KBO **{KBO}**; Avenue Reine Astrid 1 Braine-le-Château; **Actief** **1 VE**; NACE **88.999** AViQ). Deferred FREE **Les Amis des Aveugles** / **Les Hautes Ardennes** (YE2025 live). Do not redo Trait/Ouvroir/APRE/Renaitre/Stallbois stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** DROP {BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** LOSS FLIP {PNL_FLIP_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); neerlegging **17.06.2026**. Strong KBO Actief 1 VE ASBL. Assets/debt Unknown. Medium. FOI via entreprises@levillage1.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2269=done + rq_2270 open EVERY-10; loop_state ticks={TICK}; raw docs/doge/raw/tick2269/ + data/raw/tick2269/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2260**; next **2270 MUST**). Next: rq_2270 EVERY-10 + Amis Aveugles/Hautes Ardennes YE2025.
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2269"
    dst_raw = DATA / "raw" / "tick2269"
    dst_raw.mkdir(parents=True, exist_ok=True)
    src_raw.mkdir(parents=True, exist_ok=True)
    for f in dst_raw.glob("*.html"):
        shutil.copy2(f, src_raw / f.name)
    shutil.copy2(Path(__file__), src_raw / Path(__file__).name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_village_n1_jr2025_cw_nl",
                "title": "Companyweb NL Village n°1 Entreprises YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet DROP {OMZET} bruto DROP {BRUTO} (~{RATIO}x) pnl LOSS FLIP {PNL} "
                    f"equity DROP {EQUITY} FTE {FTE}; neerlegging 17.06.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2269/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Village n°1 Entreprises YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 17-06-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_village_n1_jr2025_cw_fr",
                "title": "Companyweb FR Village n°1 Entreprises YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Perte {PNL}",
            },
            {
                "source_id": f"src_village_n1_kbo_{TICK}",
                "title": f"KBO Village n°1 Entreprises {KBO} Actief Braine-le-Château 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW Village n°1 Entreprises; zetel Avenue Reine Astrid(W-B) 1 "
                    f"1440 Braine-le-Château; 1 VE; BTW NACE 88.999; begindatum 24.11.1971; tel 02-386-06-11"
                ),
            },
            {
                "source_id": f"src_village_n1_site_contact_{TICK}",
                "title": "Village n°1 FOI channel entreprises@levillage1.be",
                "url": "https://www.levillage1.be/",
                "publisher": "Village n°1 Entreprises ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; entreprises@levillage1.be; +32 2 386 06 11; "
                    "Avenue Reine Astrid 1 Wauthier-Braine; Walloon ETA AViQ"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_village_n1_omzet_jr2025_statutory",
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
                "budget_id": "bud_village_n1_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": f"CW statutory bruto_marge YE2025 (~{RATIO}x omzet)",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto DROP {BRUTO_PCT}% vs YE2024 {BRUTO24}; bruto÷omzet ~{RATIO}x",
            },
            {
                "budget_id": "bud_village_n1_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025 LOSS FLIP",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl LOSS FLIP {PNL_FLIP_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_village_n1_equity_jr2025_statutory",
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
                "budget_id": "bud_village_n1_fte_jr2025_statutory",
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
                "budget_id": "bud_village_n1_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory pnl YE2024 comparative (pre LOSS FLIP)",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl PROFIT {PNL24} comparative (pre LOSS FLIP {PNL_FLIP_PCT}%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Village n°1 Entreprises YE2025 leftover dual "
                    f"(bruto 18.11m / omzet 12.15m / pnl LOSS FLIP / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Braine-le-Château / Walloon adapted-work public path AViQ",
                "legal_basis": f"ASBL ETA Village n°1 Entreprises (KBO {KBO}; Actief; 1 VE; NACE 88.999; Braine-le-Château)",
                "decision_date": "2026-06-17",
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
                "stated_goal": "Walloon ETA sheltered workshop Braine-le-Château (packaging/digitisation/call center/green spaces)",
                "cut_option": (
                    "Publish NBB PDF assets/debt; reconcile bruto÷omzet ~1.49x + LOSS FLIP vs AViQ ETA matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>BrabantWallon>BraineLeChateau>VillageN1>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (~{RATIO}x omzet {OMZET}); "
                    f"pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE {FTE}; 1 VE; after Trait+Ouvroir@2268; "
                    "AGB Bornem JR2024; FARO/AIESH YE2024; not TE-additive of 348bn"
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
                    f"Village n°1 bruto 18.11m / omzet 12.15m / bruto÷omzet ~{RATIO}x / "
                    f"pnl LOSS FLIP / FTE {FTE} (YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>BrabantWallon>BraineLeChateau>VillageN1>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW omzet {OMZET} ({OMZET_PCT}%) / bruto {BRUTO} ({BRUTO_PCT}%) / bruto÷omzet ~{RATIO}x / "
                    f"pnl LOSS FLIP {PNL} / equity DROP {EQUITY} ({EQUITY_PCT}%) / FTE {FTE} (vs {FTE24}) / "
                    "1 VE Walloon ETA large"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Braine-le-Château / Walloon adapted-work public path AViQ",
                "stated_goal": "Walloon ETA sheltered workshop Braine-le-Château",
                "measured_outcome": (
                    f"omzet DROP {OMZET_PCT}%; bruto DROP {BRUTO_PCT}%; "
                    f"pnl LOSS FLIP {PNL_FLIP_PCT}%; equity DROP {EQUITY_PCT}%; FTE {FTE} ({FTE_PCT}%); filed 17.06.2026"
                ),
                "absurdity_score": "7.5",
                "cost_score": "8.0",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AViQ ETA matrix behind bruto÷omzet ~1.49x + LOSS FLIP + omzet DROP 9%"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH YE2024; after Trait+Ouvroir@2268 race"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Village n°1 Entreprises VZW (Braine-le-Château / Walloon ETA maatwerk)",
                "name_fr": "Village n°1 Entreprises ASBL (Braine-le-Château / entreprise de travail adapté wallonne)",
                "name_en": "Village n°1 Entreprises adapted-work ASBL (Braine-le-Château Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.levillage1.be/",
                "foi_email": "entreprises@levillage1.be",
                "foi_postal": "Avenue Reine Astrid 1, 1440 Wauthier-Braine",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.999; "
                    f"omzet DROP {OMZET} ({OMZET_PCT}%) bruto DROP {BRUTO} (~{RATIO}x / {BRUTO_PCT}%) "
                    f"pnl LOSS FLIP {PNL} equity DROP {EQUITY} ({EQUITY_PCT}%) FTE {FTE}; "
                    f"neerlegging 17.06.2026; assets/debt Unknown; FOI {GAP}; after Trait+Ouvroir@2268; "
                    "AGB Bornem JR2024; FARO/AIESH YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Wallonie>BrabantWallon>BraineLeChateau>VillageN1>NBB_PDF_assets_debt_bruto_gt_omzet_1_49x_pnl_loss_flip",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); "
                    f"bruto EUR{BRUTO} (~{RATIO}x omzet EUR{OMZET}); pnl LOSS FLIP EUR{PNL} vs EUR{PNL24}; "
                    f"AViQ ETA subsidy matrix; FTE {FTE}; activity split packaging/call center/green spaces"
                ),
                "why_it_matters": (
                    f"Medium CW shows large Walloon ETA ASBL (bruto 18.11m / omzet 12.15m / bruto~{RATIO}x / "
                    f"pnl LOSS FLIP / FTE {FTE}) under AViQ path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Village n°1 Entreprises ASBL",
                "recipient_email": "entreprises@levillage1.be",
                "recipient_postal": "Avenue Reine Astrid 1, 1440 Wauthier-Braine",
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
                    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH YE2024; "
                    "AGB Bornem JR2024; after Trait+Ouvroir@2268; next EVERY-10 2270 MUST"
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
