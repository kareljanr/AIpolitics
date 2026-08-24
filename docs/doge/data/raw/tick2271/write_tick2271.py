# tick 2271 — leftover dual La Serre-Outil YE2025 Medium (omzet JUMP 3.11m / bruto~1.51x / pnl DROP -5.58% / FTE 102.6)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2271
UTC = "2026-08-27T09:55:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_la_serre_outil_woluwe"
KBO = "0420.454.022"
KBO_BARE = "0420454022"
SRC_EN = "src_serre_jr2025_cw_en"
GAP = "gap_serre_nbb_pdf_assets_debt_bruto_gt_omzet_1_51x_eta_matrix_l5"
COMM = "comm_serre_jr2025_statutory_eta_bruto_gt_omzet_1_51x"
LB = "lb_serre_bruto_4_70m_omzet_3_11m_bruto_gt_omzet_1_51x_jr2025"
RQ = "rq_2271"
RQ_NEXT = "rq_2272"

OMZET = 3110087
OMZET24 = 2897300
BRUTO = 4704892
BRUTO24 = 4349539
PNL = 264629
PNL24 = 280272
EQUITY = 5191212
EQUITY24 = 4939756
FTE = 102.6
FTE24 = 99.8
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / abs(PNL24) * 100, 2)
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
                "leftover dual — La Serre-Outil YE2025 Medium "
                f"(omzet JUMP 3.11m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; La Serre-Outil ASBL Woluwe-Saint-Pierre {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}%); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE} (+{FTE_PCT}% vs {FTE24}); 3 VE; NACE 88.993; neerlegging 23.05.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH YE2024; "
                f"Amis+Hautes already mined@2270 race; after Amis@2270; next EVERY-10 2280"
            )
            r["instructions"] = (
                "leftover dual La Serre-Outil YE2025 FREE Brussels ETA gardens after Amis/Hautes race; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Serre-Outil — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after La Serre-Outil YE2025 Medium "
                    f"(omzet JUMP 3.11m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                    "else unused ETA/VAPH/WZC/maatwerk. "
                    "Skip La Serre-Outil/Amis des Aveugles/Hautes Ardennes/Village n°1/"
                    "Le Trait d'Union/L'Ouvroir/APRE/Brochage Renaitre/Stallbois/Sipres/"
                    "La Lorraine/BW Eupen/AJR/Alteria/Les Erables/Val du Geer/Nekto/Belair/"
                    "Corelap/Cambier/Gaillettes/Hunelle/Dauphins/Saupont/Serviplast/"
                    "Jean Del'Cour/TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/"
                    "Jean Gielen/Le Perron/L'Atelier/Axedis/Manufast/Metalgroup/EntrAnam/"
                    "Enghien/Entra/Ateliers de Tertre/Le Rucher/Het Rekreatief/Travie/SDB/"
                    "De Vleugels/Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/"
                    "Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; Relais Haute Sambre/APN YE2024; "
                    "Citeco YE2024; Groupe Foes YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/"
                    "Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/"
                    "RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Senes. Next EVERY-10: 2280."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} La Serre-Outil; FARO/AIESH YE2024; AGB Bornem JR2024; "
                    "Citeco/Groupe Foes YE2024 stalls; next every-10 2280"
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
                f"tick{TICK} leftover dual La Serre-Outil {KBO} Medium (omzet JUMP {OMZET} +{OMZET_PCT}%; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; "
                f"3 VE Woluwe Brussels ETA PHARE gardens); after Amis@2270; AGB Bornem JR2024; "
                f"FARO/AIESH YE2024; next {RQ_NEXT}; next EVERY-10 2280; continuous hole_fill"
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
        f"""# FOI draft — La Serre-Outil (NBB PDF / bruto÷omzet ~{RATIO}x / Brussels ETA gardens matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** La Serre - Outil ASBL — KBO **{KBO}** (Actief; Chaussée de Stockel / Stokkelsesteenweg 377, 1150 Woluwe-Saint-Pierre; **3 VE**; FTE {FTE} CW; NACE **88.993**; Brussels ETA PHARE / jardins)  
**recipient:** info@laserreoutil.be · Chaussée de Stockel 377, 1150 Woluwe-Saint-Pierre (+32 2 762 80 73)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.laserreoutil.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW La Serre - Outil; **3 VE**; zetel Stokkelsesteenweg 377, 1150 Sint-Pieters-Woluwe; BTW NACE **88.993** / 47.761 / 81.300; begindatum 15.02.1980; email info@laserreoutil.be.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); filed **23.05.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; Amis+Hautes already mined@2270 race. After Amis@2270. Deferred Citeco/Groupe Foes YE2024.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: La Serre - Outil ASBL
via info@laserreoutil.be
Chaussée de Stockel 377, 1150 Woluwe-Saint-Pierre
Objet: Publicité des comptes annuels 2025 La Serre-Outil (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région de Bruxelles-Capitale / PHARE / COCOF), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Explication du ratio marge brute/CA ~{RATIO}x (bruto EUR{BRUTO} / omzet EUR{OMZET}) et de la
   baisse du bénéfice EUR{PNL} ({PNL_PCT}% vs EUR{PNL24}).
3. Matrice des subsides PHARE / COCOF / ETA derrière les charges de personnel (FTE {FTE}).
4. Répartition CA/activités (entreprise de jardins / jardinerie / élagage / distribution journaux).
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


### 2026-08-27T09:55:00Z - tick 2271 - rq_2271 La Serre-Outil Woluwe (omzet JUMP 3.11m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2271** leftover dual after **rq_2270 Amis des Aveugles** (Hautes Ardennes also mined@2270 race). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Amis+Hautes **already mined**. Took FREE Brussels ETA **La Serre-Outil ASBL** YE2025 (KBO **{KBO}**; Stokkelsesteenweg 377 Woluwe-Saint-Pierre; **Actief** **3 VE**; NACE **88.993** PHARE / jardins+jardinerie). Deferred Citeco/Groupe Foes still **YE2024**. Do not redo Amis/Hautes/Village n1/Trait/Ouvroir/APRE stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); neerlegging **23.05.2026**. Strong KBO Actief 3 VE ASBL. Assets/debt Unknown. Medium. FOI via info@laserreoutil.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2271=done + rq_2272 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2271/ + data/raw/tick2271/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2270**; next **2280**). Next: rq_2272 (AGB/FARO-if-YE2025 / AIESH-REW / Citeco-Foes-if-YE2025 / unused ETA).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2271"
    dst_raw = DATA / "raw" / "tick2271"
    dst_raw.mkdir(parents=True, exist_ok=True)
    src_raw.mkdir(parents=True, exist_ok=True)
    for f in dst_raw.glob("*.html"):
        shutil.copy2(f, src_raw / f.name)
    shutil.copy2(Path(__file__), src_raw / Path(__file__).name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_serre_jr2025_cw_nl",
                "title": "Companyweb NL La Serre-Outil YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 23.05.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2271/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN La Serre-Outil YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 23-05-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_serre_jr2025_cw_fr",
                "title": "Companyweb FR La Serre-Outil YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Benefice {PNL}",
            },
            {
                "source_id": f"src_serre_kbo_{TICK}",
                "title": f"KBO La Serre-Outil {KBO} Actief Woluwe 3 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW La Serre - Outil; zetel Stokkelsesteenweg 377 1150 Sint-Pieters-Woluwe; "
                    f"3 VE; BTW NACE 88.993; begindatum 15.02.1980; email info@laserreoutil.be"
                ),
            },
            {
                "source_id": f"src_serre_site_contact_{TICK}",
                "title": "La Serre-Outil FOI channel info@laserreoutil.be",
                "url": "https://www.laserreoutil.be/",
                "publisher": "La Serre-Outil ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@laserreoutil.be; +32 2 762 80 73; "
                    "Chaussee de Stockel 377 Woluwe; Brussels ETA PHARE gardens/jardinerie"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_serre_omzet_jr2025_statutory",
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
                "budget_id": "bud_serre_bruto_jr2025_statutory",
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
                "budget_id": "bud_serre_pnl_jr2025_statutory",
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
                "budget_id": "bud_serre_equity_jr2025_statutory",
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
                "budget_id": "bud_serre_fte_jr2025_statutory",
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
                "budget_id": "bud_serre_pnl_jr2024_statutory_cmp",
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
                    "La Serre-Outil YE2025 leftover dual "
                    f"(bruto 4.70m / omzet 3.11m / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Woluwe / Brussels adapted-work public path PHARE gardens",
                "legal_basis": f"ASBL ETA La Serre-Outil (KBO {KBO}; Actief; 3 VE; NACE 88.993; Woluwe)",
                "decision_date": "2026-05-23",
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
                "stated_goal": "Brussels ETA sheltered workshop Woluwe (gardens/jardinerie/pruning/newspaper delivery)",
                "cut_option": (
                    "Publish NBB PDF assets/debt; reconcile bruto÷omzet ~1.51x vs PHARE/COCOF ETA matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Bruxelles>WoluweSaintPierre>LaSerreOutil>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (~{RATIO}x omzet {OMZET}); "
                    f"pnl DROP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 3 VE; after Amis@2270; "
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
                    f"La Serre-Outil bruto 4.70m / omzet 3.11m / bruto÷omzet ~{RATIO}x / "
                    f"pnl DROP {PNL_PCT}% / FTE {FTE} (YE2025 Brussels ETA gardens)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Bruxelles>WoluweSaintPierre>LaSerreOutil>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW omzet {OMZET} (+{OMZET_PCT}%) / bruto {BRUTO} (+{BRUTO_PCT}%) / bruto÷omzet ~{RATIO}x / "
                    f"pnl DROP {PNL} ({PNL_PCT}%) / equity JUMP {EQUITY} (+{EQUITY_PCT}%) / FTE {FTE} (vs {FTE24}) / "
                    "3 VE Brussels ETA gardens"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Woluwe / Brussels adapted-work public path PHARE gardens",
                "stated_goal": "Brussels ETA sheltered workshop Woluwe (gardens/jardinerie)",
                "measured_outcome": (
                    f"omzet JUMP +{OMZET_PCT}%; bruto JUMP +{BRUTO_PCT}%; "
                    f"pnl DROP {PNL_PCT}%; equity JUMP +{EQUITY_PCT}%; FTE {FTE} (+{FTE_PCT}%); filed 23.05.2026"
                ),
                "absurdity_score": "6.2",
                "cost_score": "4.8",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose PHARE/COCOF ETA matrix behind bruto÷omzet ~1.51x"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH YE2024; after Amis@2270"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "La Serre-Outil VZW (Woluwe / Brussels ETA tuinen maatwerk)",
                "name_fr": "La Serre-Outil ASBL (Woluwe / entreprise de travail adapté jardins bruxelloise)",
                "name_en": "La Serre-Outil adapted-work ASBL (Woluwe Brussels ETA gardens)",
                "level": "parastatal",
                "parent_id": "sec_brussels",
                "community_language": "fr",
                "website": "https://www.laserreoutil.be/",
                "foi_email": "info@laserreoutil.be",
                "foi_postal": "Chaussée de Stockel 377, 1150 Woluwe-Saint-Pierre",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 3 VE NACE 88.993; "
                    f"omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%) "
                    f"pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} (+{EQUITY_PCT}%) FTE {FTE}; "
                    f"neerlegging 23.05.2026; assets/debt Unknown; FOI {GAP}; after Amis@2270; "
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
                "hierarchy_path": "Bruxelles>WoluweSaintPierre>LaSerreOutil>NBB_PDF_assets_debt_bruto_gt_omzet_1_51x",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); "
                    f"bruto EUR{BRUTO} (~{RATIO}x omzet EUR{OMZET}); pnl DROP EUR{PNL} vs EUR{PNL24}; "
                    f"PHARE/COCOF ETA subsidy matrix; FTE {FTE}; activity split gardens/jardinerie/pruning"
                ),
                "why_it_matters": (
                    f"Medium CW shows Brussels ETA ASBL (bruto 4.70m / omzet 3.11m / bruto~{RATIO}x / "
                    f"pnl DROP {PNL_PCT}% / FTE {FTE}) under PHARE gardens path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "La Serre - Outil ASBL",
                "recipient_email": "info@laserreoutil.be",
                "recipient_postal": "Chaussée de Stockel 377, 1150 Woluwe-Saint-Pierre",
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
                    "AGB Bornem JR2024; after Amis@2270; next EVERY-10 2280"
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
