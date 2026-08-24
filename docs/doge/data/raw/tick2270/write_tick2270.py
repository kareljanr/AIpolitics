# tick 2270 — EVERY-10 + leftover dual Amis des Aveugles YE2025 Medium (omzet 1.88m / bruto~3.40x / pnl LOSS -4.74m / equity 39.2m)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2270
UTC = "2026-08-27T09:40:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_amis_des_aveugles_mons"
KBO = "0406.579.854"
KBO_BARE = "0406579854"
SRC_EN = "src_amis_jr2025_cw_en"
GAP = "gap_amis_nbb_pdf_assets_debt_bruto_gt_omzet_3_40x_pnl_loss_4_74m_eta_matrix_l5"
COMM = "comm_amis_jr2025_statutory_eta_bruto_gt_omzet_3_40x_pnl_loss_4_74m"
LB = "lb_amis_bruto_6_40m_omzet_1_88m_bruto_gt_omzet_3_40x_pnl_loss_4_74m_jr2025"
RQ = "rq_2270"
RQ_NEXT = "rq_2271"

OMZET = 1882853
OMZET24 = 1592187
BRUTO = 6398659
BRUTO24 = 6958732
PNL = -4744990
PNL24 = -4556387
EQUITY = 39171129
EQUITY24 = 37881233
FTE = 172.9
FTE24 = 173.4
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
LOSS_WIDEN_PCT = round((abs(PNL) - abs(PNL24)) / abs(PNL24) * 100, 2)
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
                "EVERY-10 + leftover dual — Amis des Aveugles YE2025 Medium "
                f"(omzet JUMP 1.88m / bruto~{RATIO}x / pnl LOSS -4.74m / equity 39.2m)"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; EVERY-10 refreshed; Amis des Aveugles ASBL Mons {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}%); bruto DROP {BRUTO} (~{RATIO}x / {BRUTO_PCT}%); "
                f"pnl LOSS WIDEN {PNL} (+{LOSS_WIDEN_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE} ({FTE_PCT}% vs {FTE24}); 7 VE; NACE 88.993; neerlegging 29.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH YE2024; "
                f"Hautes Ardennes YE2025 FREE deferred; after Village n1@2269; next EVERY-10 2280"
            )
            r["instructions"] = (
                "EVERY-10 + leftover dual Amis des Aveugles YE2025 FREE Mons ETA after Village n1; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Amis — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Hautes Ardennes-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Amis des Aveugles YE2025 Medium "
                    f"(omzet JUMP 1.88m / bruto~{RATIO}x / pnl LOSS -4.74m / equity 39.2m). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else named FREE Les Hautes Ardennes (0407.574.994) if YE2025 unused, "
                    "else unused ETA/VAPH/WZC/maatwerk. "
                    "Skip Amis des Aveugles/Village n°1/Le Trait d'Union/L'Ouvroir/APRE/"
                    "Brochage Renaitre/Stallbois/Sipres/La Lorraine/BW Eupen/AJR/Alteria/"
                    "Les Erables/Val du Geer/Nekto/Belair/Corelap/Cambier/Gaillettes/Hunelle/"
                    "Dauphins/Saupont/Serviplast/Jean Del'Cour/TRAVCO/Pilifs/Jeunes Jardiniers/"
                    "La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/Manufast/Metalgroup/"
                    "EntrAnam/Enghien/Entra/Ateliers de Tertre/Le Rucher/Het Rekreatief/Travie/"
                    "SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/"
                    "Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; Relais Haute Sambre/APN YE2024; "
                    "Citeco YE2024. Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/"
                    "Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/"
                    "Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL/Orpimmo/"
                    "Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. Next EVERY-10: 2280."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Amis EVERY-10; FARO/AIESH YE2024; AGB Bornem JR2024; "
                    "Hautes Ardennes YE2025 FREE deferred; next every-10 2280"
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
                f"tick{TICK} EVERY-10 + leftover dual Amis des Aveugles {KBO} Medium "
                f"(omzet JUMP {OMZET} +{OMZET_PCT}%; bruto DROP {BRUTO} ~{RATIO}x; "
                f"pnl LOSS WIDEN {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 7 VE Mons federal blind-care ETA); "
                f"after Village n1@2269; AGB Bornem JR2024; FARO/AIESH YE2024; "
                f"Hautes Ardennes YE2025 FREE; next {RQ_NEXT}; next EVERY-10 2280; continuous hole_fill"
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
        f"""# FOI draft — Amis des Aveugles (NBB PDF / bruto÷omzet ~{RATIO}x / pnl LOSS −4.74m / equity 39.2m)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Oeuvre Fédérale Les Amis des Aveugles et Malvoyants ASBL — KBO **{KBO}** (Actief; Rue de la Barrière 37, 7011 Mons/Ghlin; **7 VE**; FTE {FTE} CW; NACE **88.993**; Walloon/federal blind-care + ETA Ateliers de Mons)  
**recipient:** info@amisdesaveugles.org · Rue de la Barrière 37, 7011 Mons (+32 65 40 31 00)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.amisdesaveugles.org/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW Oeuvre Fédérale Les Amis des Aveugles…; **7 VE**; zetel Rue de la Barrière (G.) 37, 7011 Mons; RSZ NACE **88.993**; begindatum 20.09.1928.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** DROP {BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS WIDEN +{LOSS_WIDEN_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); filed **29.07.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024. After Village n°1@2269. Deferred FREE Hautes Ardennes YE2025.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Oeuvre Fédérale Les Amis des Aveugles et Malvoyants ASBL
via info@amisdesaveugles.org
Rue de la Barrière 37, 7011 Mons
Objet: Publicité des comptes annuels 2025 Amis des Aveugles (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région wallonne / AViQ / Code de la démocratie locale), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Explication de la perte structurelle EUR{PNL} (vs EUR{PNL24}, +{LOSS_WIDEN_PCT}%) malgré
   fonds propres EUR{EQUITY} et CA EUR{OMZET}; ratio marge brute/CA ~{RATIO}x (bruto EUR{BRUTO}).
3. Matrice des subsides AViQ / PHARE / fédéral / dons-legs derrière FTE {FTE} et Ateliers de Mons ETA.
4. Répartition CA/activités (ETA ateliers / chiens guides / résidentiel / réadaptation / formations).
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


### 2026-08-27T09:40:00Z - tick 2270 - EVERY-10 + rq_2270 Amis des Aveugles Mons (omzet JUMP 1.88m / bruto~{RATIO}x / pnl LOSS -4.74m / equity 39.2m / Medium)

- **EVERY-10:** refreshed `progress_every_10_ticks.md` (layers A–E @2270) + `doge_waste_top10_current.md` (top10 stable; NEW residual 2261-2270 noted off pure top10).
- Unit: **rq_2270** leftover dual after **rq_2269 Village n°1**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre/APN still **YE2024**. Took named FREE **Amis des Aveugles / Vrienden der Blinden ASBL** YE2025 (KBO **{KBO}**; Rue de la Barrière 37 Mons; **Actief** **7 VE**; NACE **88.993** AViQ/federal blind-care + Ateliers de Mons ETA). Deferred FREE **Les Hautes Ardennes** YE2025. Do not redo Village n1/Trait/Ouvroir/APRE/Renaitre stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** DROP {BRUTO_PCT}% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** LOSS WIDEN +{LOSS_WIDEN_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); neerlegging **29.07.2026**. Strong KBO Actief 7 VE ASBL. Assets/debt Unknown. Medium. FOI via info@amisdesaveugles.org.
- Wrote: progress+top10; sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2270=done + rq_2271 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2270/ + data/raw/tick2270/.
- FOI: **ready not sent** (human-gated).
- **EVERY-10 done** (last was 2260; next **2280**). Next: rq_2271 (AGB/FARO-if-YE2025 / AIESH-REW / Hautes Ardennes YE2025).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2270"
    dst_raw = DATA / "raw" / "tick2270"
    dst_raw.mkdir(parents=True, exist_ok=True)
    src_raw.mkdir(parents=True, exist_ok=True)
    for f in dst_raw.glob("*.html"):
        shutil.copy2(f, src_raw / f.name)
    shutil.copy2(Path(__file__), src_raw / Path(__file__).name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_amis_jr2025_cw_nl",
                "title": "Companyweb NL Amis des Aveugles YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto DROP {BRUTO} (~{RATIO}x) pnl LOSS {PNL} "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 29.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2270/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Amis des Aveugles YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 29-07-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_amis_jr2025_cw_fr",
                "title": "Companyweb FR Amis des Aveugles YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Perte {PNL}",
            },
            {
                "source_id": f"src_amis_kbo_{TICK}",
                "title": f"KBO Amis des Aveugles {KBO} Actief Mons 7 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW Oeuvre Federale Les Amis des Aveugles; zetel Rue de la Barriere 37 "
                    f"7011 Mons; 7 VE; RSZ NACE 88.993; begindatum 20.09.1928"
                ),
            },
            {
                "source_id": f"src_amis_site_contact_{TICK}",
                "title": "Amis des Aveugles FOI channel info@amisdesaveugles.org",
                "url": "https://www.amisdesaveugles.org/",
                "publisher": "Amis des Aveugles ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@amisdesaveugles.org; +32 65 40 31 00; "
                    "Rue de la Barriere 37 Mons; federal blind-care + Ateliers de Mons ETA"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_amis_omzet_jr2025_statutory",
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
                "budget_id": "bud_amis_bruto_jr2025_statutory",
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
                "budget_id": "bud_amis_pnl_jr2025_statutory",
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
                "budget_id": "bud_amis_equity_jr2025_statutory",
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
                "budget_id": "bud_amis_fte_jr2025_statutory",
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
                "budget_id": "bud_amis_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory pnl YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl LOSS {PNL24} comparative (pre WIDEN +{LOSS_WIDEN_PCT}%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Amis des Aveugles YE2025 EVERY-10 leftover dual "
                    f"(bruto 6.40m / omzet 1.88m / pnl LOSS -4.74m / equity 39.2m / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "Blind/visually impaired + ETA workers Mons / federal+Walloon public path",
                "legal_basis": f"ASBL Amis des Aveugles (KBO {KBO}; Actief; 7 VE; NACE 88.993; Mons)",
                "decision_date": "2026-07-29",
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
                "stated_goal": "Federal blind-care ASBL Mons (ETA Ateliers de Mons / guide dogs / residential / rehab)",
                "cut_option": (
                    "Publish NBB PDF assets/debt; reconcile bruto÷omzet ~3.40x + structural LOSS vs AViQ/donation matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Hainaut>Mons>AmisDesAveugles>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (~{RATIO}x omzet {OMZET}); "
                    f"pnl LOSS {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 7 VE; after Village n1@2269; "
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
                    f"Amis des Aveugles bruto 6.40m / omzet 1.88m / bruto÷omzet ~{RATIO}x / "
                    f"pnl LOSS -4.74m / equity 39.2m / FTE {FTE} (YE2025 Mons)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Hainaut>Mons>AmisDesAveugles>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW omzet {OMZET} (+{OMZET_PCT}%) / bruto {BRUTO} ({BRUTO_PCT}%) / bruto÷omzet ~{RATIO}x / "
                    f"pnl LOSS {PNL} / equity JUMP {EQUITY} (+{EQUITY_PCT}%) / FTE {FTE} (vs {FTE24}) / "
                    "7 VE Mons blind-care+ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "Blind/visually impaired + ETA workers Mons / federal+Walloon public path",
                "stated_goal": "Federal blind-care ASBL Mons (ETA Ateliers de Mons / guide dogs / rehab)",
                "measured_outcome": (
                    f"omzet JUMP +{OMZET_PCT}%; bruto DROP {BRUTO_PCT}%; "
                    f"pnl LOSS WIDEN +{LOSS_WIDEN_PCT}%; equity JUMP +{EQUITY_PCT}%; FTE {FTE} ({FTE_PCT}%); filed 29.07.2026"
                ),
                "absurdity_score": "8.0",
                "cost_score": "5.5",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AViQ/donation matrix behind bruto÷omzet ~3.40x + structural LOSS -4.74m vs equity 39m"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; EVERY-10@2270 primary; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH YE2024; after Village n1@2269"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Amis des Aveugles / Vrienden der Blinden VZW (Mons / federal blind-care + ETA)",
                "name_fr": "Amis des Aveugles ASBL (Mons / œuvre fédérale + entreprise de travail adapté)",
                "name_en": "Friends of the Blind ASBL (Mons federal blind-care + adapted work)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.amisdesaveugles.org/",
                "foi_email": "info@amisdesaveugles.org",
                "foi_postal": "Rue de la Barrière 37, 7011 Mons",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 7 VE NACE 88.993; "
                    f"omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto DROP {BRUTO} (~{RATIO}x / {BRUTO_PCT}%) "
                    f"pnl LOSS {PNL} equity JUMP {EQUITY} (+{EQUITY_PCT}%) FTE {FTE}; "
                    f"neerlegging 29.07.2026; assets/debt Unknown; FOI {GAP}; EVERY-10@2270; "
                    "after Village n1@2269; AGB Bornem JR2024; FARO/AIESH YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Wallonie>Hainaut>Mons>AmisDesAveugles>NBB_PDF_assets_debt_bruto_gt_omzet_3_40x_pnl_loss",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); "
                    f"bruto EUR{BRUTO} (~{RATIO}x omzet EUR{OMZET}); pnl LOSS EUR{PNL} vs EUR{PNL24}; "
                    f"AViQ/donation/ETA subsidy matrix; FTE {FTE}; activity split ateliers/guide dogs/residential"
                ),
                "why_it_matters": (
                    f"Medium CW shows Mons federal blind-care ASBL (bruto 6.40m / omzet 1.88m / bruto~{RATIO}x / "
                    f"pnl LOSS -4.74m / equity 39.2m / FTE {FTE}); assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Oeuvre Federale Les Amis des Aveugles et Malvoyants ASBL",
                "recipient_email": "info@amisdesaveugles.org",
                "recipient_postal": "Rue de la Barrière 37, 7011 Mons",
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
                    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; EVERY-10@2270; "
                    "preferred stall FARO/AIESH YE2024; AGB Bornem JR2024; next EVERY-10 2280"
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
