# tick 2268 — leftover dual Le Trait d'Union YE2025 Medium (omzet 5.37m / bruto~2.19x / pnl DROP -54.5% / FTE 328.2)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]  # .../data/raw/tick2268 -> repo root
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2268
UTC = "2026-08-27T09:10:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_le_trait_dunion_mouscron"
KBO = "0407.638.243"
KBO_BARE = "0407638243"
SRC_EN = "src_trait_jr2025_cw_en"
GAP = "gap_trait_nbb_pdf_assets_debt_bruto_gt_omzet_2_19x_pnl_drop_55pct_eta_matrix_l5"
COMM = "comm_trait_jr2025_statutory_eta_bruto_gt_omzet_2_19x_pnl_drop_55pct"
LB = "lb_trait_bruto_11_74m_omzet_5_37m_bruto_gt_omzet_2_19x_pnl_drop_55pct_jr2025"
RQ = "rq_2268"
RQ_NEXT = "rq_2269"

OMZET = 5369612
OMZET24 = 5341617
BRUTO = 11743773
BRUTO24 = 12029513
PNL = 272985
PNL24 = 599933
EQUITY = 9700116
EQUITY24 = 9465185
FTE = 328.2
FTE24 = 316.8
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / abs(PNL24) * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
RATIO = round(BRUTO / OMZET, 2)
PI = "6.55"


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
                "leftover dual — Le Trait d'Union YE2025 Medium "
                f"(omzet JUMP 5.37m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Le Trait d'Union ASBL Mouscron {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}%); bruto DROP {BRUTO} (~{RATIO}x / {BRUTO_PCT}%); "
                f"pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE} (+{FTE_PCT}% vs {FTE24}); 3 VE; NACE 88.999/88.993; neerlegging 24.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / "
                f"FARO/AIESH YE2024; REW stall opaque; Relais Haute Sambre/APN YE2024; Heropbeuring CW opaque; "
                f"after APRE@2267; next EVERY-10 2270"
            )
            r["instructions"] = (
                "leftover dual Le Trait d'Union YE2025 FREE Walloon ETA Mouscron after APRE; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Trait d'Union — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Le Trait d'Union YE2025 Medium "
                    f"(omzet JUMP 5.37m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else named FREE Village n1 Entreprises / Les Amis des Aveugles / "
                    "Les Hautes Ardennes if YE2025 unused, else unused ETA/VAPH/WZC/maatwerk. "
                    "Skip Le Trait d'Union/APRE/Brochage Renaitre/Stallbois/Sipres/La Lorraine/"
                    "BW Eupen/AJR/Alteria/Les Erables/Val du Geer/Nekto/Belair/Corelap/Cambier/"
                    "Gaillettes/Hunelle/Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/"
                    "TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/"
                    "L'Atelier/Axedis/ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/"
                    "Entra/Ateliers de Tertre/Le Rucher/Het Rekreatief/Travie/SDB/De Vleugels/"
                    "Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/Den Azalee/Kemphaan/"
                    "Mirto/Blankedale/Werkmmaat; Relais Haute Sambre/APN YE2024; Citeco YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/"
                    "Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/"
                    "RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Senes. Next EVERY-10: 2270."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Le Trait d'Union; FARO/AIESH YE2024; AGB Bornem JR2024; "
                    "REW stall opaque; Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024; "
                    "Village n1/Amis Aveugles/Hautes Ardennes YE2025 FREE deferred; next every-10 2270"
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
                f"tick{TICK} leftover dual Le Trait d'Union {KBO} Medium (omzet JUMP {OMZET} +{OMZET_PCT}%; "
                f"bruto DROP {BRUTO} ~{RATIO}x; pnl DROP {PNL} {PNL_PCT}%; equity JUMP {EQUITY}; FTE {FTE}; "
                f"3 VE Mouscron Walloon ETA AViQ); after APRE@2267; AGB Bornem JR2024; "
                f"FARO/AIESH YE2024; REW stall opaque; Relais Haute Sambre/APN YE2024; "
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
        f"""# FOI draft — Le Trait d'Union (NBB PDF / bruto÷omzet ~{RATIO}x / pnl DROP {PNL_PCT}% / Walloon ETA matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Le Trait d'Union ASBL — KBO **{KBO}** (Actief; Boulevard de l'Eurozone / Eurozonelaan 3, 7700 Mouscron; **3 VE**; FTE {FTE} CW; NACE **88.999** / **88.993**; Walloon ETA AViQ)  
**recipient:** info@traitunion.be · Boulevard de l'Eurozone 3, 7700 Mouscron  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.traitunion.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW Le Trait d'Union; **3 VE**; zetel Eurozonelaan 3, 7700 Mouscron; BTW NACE **88.999** / **88.993**; begindatum 13.11.1969.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** DROP {BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); filed **24.07.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024 (0201.712.587); REW stall opaque; Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024. After APRE@2267. Deferred FREE Village n°1 / Amis des Aveugles / Hautes Ardennes YE2025.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Le Trait d'Union ASBL
via info@traitunion.be
Boulevard de l'Eurozone 3, 7700 Mouscron
Objet: Publicité des comptes annuels 2025 Le Trait d'Union (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région wallonne / AViQ / Code de la démocratie locale), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Explication de la baisse du bénéfice EUR{PNL} vs EUR{PNL24} ({PNL_PCT}%) et du ratio
   marge brute/CA ~{RATIO}x (bruto EUR{BRUTO} / omzet EUR{OMZET}).
3. Matrice des subsides AViQ / ETA / AWIPH derrière les charges de personnel (FTE {FTE}).
4. Répartition CA/activités (conditionnement / assemblage / textile / espaces verts / sous-traitance)
   et sites Mouscron-Eurozone / Comines.
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


### 2026-08-27T09:10:00Z - tick 2268 - rq_2268 Le Trait d'Union Mouscron (omzet JUMP 5.37m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2268** leftover dual after **rq_2267 APRE**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024** (0201.712.587); REW stall **opaque**; Heropbeuring still **CW opaque**; Relais Haute Sambre/APN still **YE2024**. Took FREE Walloon ETA **Le Trait d'Union ASBL** YE2025 (KBO **{KBO}**; Boulevard de l'Eurozone 3 Mouscron; **Actief** **3 VE**; NACE **88.999**/88.993 AViQ). Deferred FREE **Village n°1** / **Les Amis des Aveugles** / **Les Hautes Ardennes** (YE2025 live). Do not redo APRE/Renaitre/Stallbois/Sipres/La Lorraine/BW Eupen/AJR/Alteria stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** DROP {BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); neerlegging **24.07.2026**. Strong KBO Actief 3 VE ASBL. Assets/debt Unknown. Medium. FOI via info@traitunion.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2268=done + rq_2269 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2268/ + data/raw/tick2268/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2260**; next **2270**). Next: rq_2269 (AGB/FARO-if-YE2025 / AIESH-REW / Village n1-Amis Aveugles-Hautes Ardennes YE2025).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2268"
    dst_raw = DATA / "raw" / "tick2268"
    dst_raw.mkdir(parents=True, exist_ok=True)
    src_raw.mkdir(parents=True, exist_ok=True)
    for f in dst_raw.glob("*.html"):
        shutil.copy2(f, src_raw / f.name)
    shutil.copy2(Path(__file__), src_raw / Path(__file__).name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_trait_jr2025_cw_nl",
                "title": "Companyweb NL Le Trait d'Union YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto DROP {BRUTO} (~{RATIO}x) pnl DROP {PNL} "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 24.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2268/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Le Trait d'Union YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 24-07-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_trait_jr2025_cw_fr",
                "title": "Companyweb FR Le Trait d'Union YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Benefice {PNL}",
            },
            {
                "source_id": f"src_trait_kbo_{TICK}",
                "title": f"KBO Le Trait d'Union {KBO} Actief Mouscron 3 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW Le Trait d'Union; zetel Eurozonelaan 3 7700 Mouscron; "
                    f"3 VE; BTW NACE 88.999/88.993; begindatum 13.11.1969; KBO email/web empty"
                ),
            },
            {
                "source_id": f"src_trait_site_contact_{TICK}",
                "title": "Le Trait d'Union FOI channel info@traitunion.be",
                "url": "https://www.traitunion.be/",
                "publisher": "Le Trait d'Union ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@traitunion.be; Boulevard de l'Eurozone 3 Mouscron; "
                    "Walloon ETA AViQ (conditionnement/assemblage/textile/espaces verts); sites Mouscron+Comines"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_trait_omzet_jr2025_statutory",
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
                "budget_id": "bud_trait_bruto_jr2025_statutory",
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
                "budget_id": "bud_trait_pnl_jr2025_statutory",
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
                "budget_id": "bud_trait_equity_jr2025_statutory",
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
                "budget_id": "bud_trait_fte_jr2025_statutory",
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
                "budget_id": "bud_trait_pnl_jr2024_statutory_cmp",
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
                    "Le Trait d'Union YE2025 leftover dual "
                    f"(bruto 11.74m / omzet 5.37m / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Mouscron-Comines / Walloon adapted-work public path AViQ",
                "legal_basis": f"ASBL ETA Le Trait d'Union (KBO {KBO}; Actief; 3 VE; NACE 88.999; Mouscron)",
                "decision_date": "2026-07-24",
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
                "stated_goal": "Walloon ETA sheltered workshop Mouscron (packaging/assembly/textile/green spaces)",
                "cut_option": (
                    "Publish NBB PDF assets/debt; reconcile bruto÷omzet ~2.19x + pnl DROP vs AViQ ETA matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Hainaut>Mouscron>TraitDUnion>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (~{RATIO}x omzet {OMZET}); "
                    f"pnl DROP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 3 VE; after APRE@2267; "
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
                    f"Le Trait d'Union bruto 11.74m / omzet 5.37m / bruto÷omzet ~{RATIO}x / "
                    f"pnl DROP {PNL_PCT}% / FTE {FTE} (YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Hainaut>Mouscron>TraitDUnion>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW omzet {OMZET} (+{OMZET_PCT}%) / bruto {BRUTO} ({BRUTO_PCT}%) / bruto÷omzet ~{RATIO}x / "
                    f"pnl DROP {PNL} ({PNL_PCT}%) / equity JUMP {EQUITY} (+{EQUITY_PCT}%) / FTE {FTE} (vs {FTE24}) / "
                    "3 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Mouscron-Comines / Walloon adapted-work public path AViQ",
                "stated_goal": "Walloon ETA sheltered workshop Mouscron (packaging/assembly/textile)",
                "measured_outcome": (
                    f"omzet JUMP +{OMZET_PCT}%; bruto DROP {BRUTO_PCT}%; "
                    f"pnl DROP {PNL_PCT}%; equity JUMP +{EQUITY_PCT}%; FTE {FTE} (+{FTE_PCT}%); filed 24.07.2026"
                ),
                "absurdity_score": "7.2",
                "cost_score": "7.0",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AViQ ETA matrix behind bruto÷omzet ~2.19x + pnl DROP 55%"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH YE2024; after APRE@2267"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Le Trait d'Union VZW (Mouscron / Walloon ETA maatwerk)",
                "name_fr": "Le Trait d'Union ASBL (Mouscron / entreprise de travail adapté wallonne)",
                "name_en": "Le Trait d'Union adapted-work ASBL (Mouscron Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.traitunion.be/",
                "foi_email": "info@traitunion.be",
                "foi_postal": "Boulevard de l'Eurozone 3, 7700 Mouscron",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 3 VE NACE 88.999; "
                    f"omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto DROP {BRUTO} (~{RATIO}x / {BRUTO_PCT}%) "
                    f"pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} (+{EQUITY_PCT}%) FTE {FTE}; "
                    f"neerlegging 24.07.2026; assets/debt Unknown; FOI {GAP}; after APRE@2267; "
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
                "hierarchy_path": "Wallonie>Hainaut>Mouscron>TraitDUnion>NBB_PDF_assets_debt_bruto_gt_omzet_2_19x_pnl_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); "
                    f"bruto EUR{BRUTO} (~{RATIO}x omzet EUR{OMZET}); pnl DROP EUR{PNL} vs EUR{PNL24}; "
                    f"AViQ ETA subsidy matrix; FTE {FTE}; activity/site split Mouscron-Comines"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (bruto 11.74m / omzet 5.37m / bruto~{RATIO}x / "
                    f"pnl DROP {PNL_PCT}% / FTE {FTE}) under AViQ path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Le Trait d'Union ASBL",
                "recipient_email": "info@traitunion.be",
                "recipient_postal": "Boulevard de l'Eurozone 3, 7700 Mouscron",
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
