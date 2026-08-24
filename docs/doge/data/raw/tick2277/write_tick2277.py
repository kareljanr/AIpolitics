# tick 2277 — leftover dual AMAB YE2025 Medium (omzet JUMP 14.18m / bruto~1.53x / pnl LOSS FLIP / FTE 645.1)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2277
UTC = "2026-08-27T11:30:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_amab_asse"
KBO = "0411.635.039"
KBO_BARE = "0411635039"
SRC_EN = "src_amab_jr2025_cw_en"
GAP = "gap_amab_nbb_pdf_assets_debt_bruto_gt_omzet_1_53x_pnl_loss_flip_matrix_l5"
COMM = "comm_amab_jr2025_statutory_maatwerk_omzet_14_18m_pnl_loss_flip"
LB = "lb_amab_omzet_14_18m_bruto_1_53x_pnl_loss_flip_jr2025"
RQ = "rq_2277"
RQ_NEXT = "rq_2278"

OMZET = 14179340
OMZET24 = 12869693
BRUTO = 21690724
BRUTO24 = 20926423
PNL = -447493
PNL24 = 559019
EQUITY = 17950369
EQUITY24 = 18491679
FTE = 645.1
FTE24 = 642.2
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / abs(PNL24) * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
RATIO = round(BRUTO / OMZET, 2)
PI = "6.80"


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
                "leftover dual — AMAB YE2025 Medium "
                f"(omzet JUMP 14.18m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; AMAB VZW Asse {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}%); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl LOSS FLIP {PNL} ({PNL_PCT}% vs {PNL24}); equity DROP {EQUITY} ({EQUITY_PCT}%); "
                f"FTE {FTE} (+{FTE_PCT}% vs {FTE24}); 3 VE; NACE 88.993; neerlegging 10.06.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / "
                f"FARO/AIESH/Citeco/Groupe Foes YE2024; after CARP@2276 (+ASV race); next EVERY-10 2280"
            )
            r["instructions"] = (
                "leftover dual AMAB YE2025 FREE Flemish maatwerk Asse/Beersel/Zaventem after C.A.R.P./ASV; "
                "preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after AMAB — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after AMAB YE2025 Medium "
                    f"(omzet JUMP 14.18m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                    "else unused ETA-VAPH-WZC-maatwerk with live sourced euros. "
                    "Skip AMAB/C.A.R.P./Atelier Saint-Vincent/A.P.A.C./Adapta/Atelier 85/La Gaume/"
                    "Fournipac/De Enter/Serre-Outil/Amis/Hautes/Village n1/Trait/Ouvroir/APRE stack; "
                    "Relais Haute Sambre/APN/Manupal YE2024; Citeco/Groupe Foes YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/"
                    "Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/"
                    "RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Senes/Forena/Waak/OptimaT. Next EVERY-10: 2280."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} AMAB; FARO/AIESH/Citeco/Groupe Foes YE2024; "
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
                f"tick{TICK} leftover dual AMAB {KBO} Medium (omzet JUMP {OMZET} +{OMZET_PCT}%; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE {FTE}; "
                f"3 VE Asse/Beersel/Zaventem Flemish maatwerk); after CARP@2276; "
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
        f"""# FOI draft — AMAB (NBB PDF / bruto~{RATIO}x omzet / pnl LOSS FLIP / Flemish maatwerk)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** AMAB VZW — KBO **{KBO}** (Actief; Z. 5 Mollem 90, 1730 Asse; **3 VE**; FTE {FTE} CW; NACE **88.993**; Flemish maatwerk Asse/Beersel/Zaventem)  
**recipient:** info@amab.be · Z. 5 Mollem 90, 1730 Asse (+32 2 356 66 97)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}/amab) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}/amab) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}/amab) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_BARE}) · [site](https://www.amab.be/) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/{KBO_BARE})  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW AMAB; **3 VE**; zetel Z. 5 Mollem 90, 1730 Asse; email info@amab.be; RSZ/BTW NACE **88.993**; begindatum 28.10.1971; sites Asse/Beersel/Zaventem.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (~{RATIO}x omzet); pnl **EUR{PNL:,}** LOSS FLIP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP {EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); filed **10.06.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; Citeco YE2024; Groupe Foes YE2024; Manupal YE2024. After C.A.R.P.@2276 (+Atelier Saint-Vincent race).

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: AMAB VZW
via info@amab.be
Z. 5 Mollem 90, 1730 Asse
Betreft: Openbaarmaking jaarrekening 2025 AMAB (KBO {KBO})

Geachte,

Op basis van de regels inzake openbaarheid van bestuur (Vlaamse Codex / Vlaamse
regelgeving sociale economie / maatwerkdecreet) vraag ik mededeling van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij de overgang naar verlies EUR{PNL} (vs winst EUR{PNL24}, {PNL_PCT}%)
   ondanks omzet EUR{OMZET} (+{OMZET_PCT}%) en brutomarge EUR{BRUTO} (~{RATIO}x omzet).
3. Matrix van loonkostensubsidies / maatwerk-tussenkomsten achter FTE {FTE}.
4. Opsplitsing handelsomzet vs publieke steun YE2024–YE2025 (co-packing / elektro / groen / circulaire).
5. Schulden LT/KT en liquiditeiten YE2025 (niet gepubliceerd op Companyweb).

Periode YE2025 (+ vergelijking YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
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


### 2026-08-27T11:30:00Z - tick 2277 - rq_2277 AMAB Asse (omzet JUMP 14.18m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE} / Medium)

- Unit: **rq_2277** leftover dual after **rq_2276 C.A.R.P.** (+Atelier Saint-Vincent race). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**; Manupal YE2024. Took FREE Flemish maatwerk **AMAB VZW** YE2025 (KBO **{KBO}**; Z. 5 Mollem 90 Asse; **Actief** **3 VE**; NACE **88.993** Asse/Beersel/Zaventem). Do not redo CARP/ASV/APAC/Adapta/Atelier85/Forena/Waak/OptimaT stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (~{RATIO}x); pnl **EUR{PNL}** LOSS FLIP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); neerlegging **10.06.2026**. Strong KBO Actief 3 VE VZW info@amab.be. Assets/debt Unknown. Medium.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2277=done + rq_2278 open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2277/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2270**; next **2280**). Next: rq_2278 (AGB/FARO-if-YE2025 / AIESH-REW / Citeco-Foes-if-YE2025 / unused ETA).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2277"
    dst_raw = DATA / "raw" / "tick2277"
    dst_raw.mkdir(parents=True, exist_ok=True)
    src_raw.mkdir(parents=True, exist_ok=True)
    for f in dst_raw.glob("*.html"):
        shutil.copy2(f, src_raw / f.name)
    shutil.copy2(Path(__file__), src_raw / Path(__file__).name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_amab_jr2025_cw_nl",
                "title": "Companyweb NL AMAB YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}/amab",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl LOSS FLIP {PNL} "
                    f"equity DROP {EQUITY} FTE {FTE}; neerlegging 10.06.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2277/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN AMAB YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}/amab",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 10-06-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_amab_jr2025_cw_fr",
                "title": "Companyweb FR AMAB YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}/amab",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Benefice {PNL}",
            },
            {
                "source_id": f"src_amab_kbo_{TICK}",
                "title": f"KBO AMAB {KBO} Actief Asse 3 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW AMAB; zetel Z. 5 Mollem 90 1730 Asse; "
                    f"3 VE; NACE 88.993; info@amab.be; begindatum 28.10.1971"
                ),
            },
            {
                "source_id": f"src_amab_site_contact_{TICK}",
                "title": "AMAB FOI channel info@amab.be",
                "url": "https://www.amab.be/",
                "publisher": "AMAB VZW",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@amab.be; +32 2 356 66 97; "
                    "Z. 5 Mollem 90 Asse; Flemish maatwerk Asse/Beersel/Zaventem"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_amab_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW statutory omzet YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet JUMP +{OMZET_PCT}% vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_amab_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": f"CW statutory bruto_marge YE2025 (~{RATIO}x omzet)",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +{BRUTO_PCT}% vs YE2024 {BRUTO24}; ~{RATIO}x omzet",
            },
            {
                "budget_id": "bud_amab_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025 LOSS FLIP",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl LOSS FLIP {PNL_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_amab_equity_jr2025_statutory",
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
                "budget_id": "bud_amab_fte_jr2025_statutory",
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
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "AMAB YE2025 leftover dual "
                    f"(omzet 14.18m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "maatwerk workers Asse/Beersel/Zaventem / Flemish collectief maatwerk",
                "legal_basis": f"VZW maatwerk AMAB (KBO {KBO}; Actief; 3 VE; NACE 88.993; Asse)",
                "decision_date": "2026-06-10",
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
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}/amab",
                "stated_goal": "Flemish maatwerk Asse/Beersel/Zaventem (co-packing / electro / green / circular)",
                "cut_option": (
                    "Publish NBB PDF assets/debt; reconcile LOSS FLIP + bruto>~1.5x omzet vs maatwerk wage-subsidy matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Asse>AMAB>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (omzet {OMZET} ~{RATIO}x); "
                    f"pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE {FTE}; 3 VE; after CARP@2276; "
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
                    f"AMAB omzet 14.18m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE} "
                    "(YE2025 Flemish maatwerk Asse)"
                ),
                "level": "L5",
                "type": "maatwerk_vzw_statutory",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Asse>AMAB>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW omzet {OMZET} (+{OMZET_PCT}%) / bruto {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%) / "
                    f"pnl LOSS FLIP {PNL} ({PNL_PCT}%) / equity DROP {EQUITY} ({EQUITY_PCT}%) / "
                    f"FTE {FTE} (vs {FTE24}) / 3 VE Flemish maatwerk"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "maatwerk workers Asse/Beersel/Zaventem / Flemish collectief maatwerk",
                "stated_goal": "Flemish maatwerk Asse/Beersel/Zaventem (co-packing/electro/green)",
                "measured_outcome": (
                    f"omzet JUMP +{OMZET_PCT}%; bruto JUMP +{BRUTO_PCT}% (~{RATIO}x); "
                    f"pnl LOSS FLIP {PNL_PCT}%; equity DROP {EQUITY_PCT}%; FTE {FTE}; filed 10.06.2026"
                ),
                "absurdity_score": "7.6",
                "cost_score": "7.0",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt FOI; disclose maatwerk wage-subsidy matrix behind LOSS FLIP despite omzet JUMP"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/Citeco/Groupe Foes YE2024; after CARP@2276"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "AMAB VZW (Asse / Flemish maatwerk)",
                "name_fr": "AMAB ASBL (Asse / entreprise de travail adapté flamande)",
                "name_en": "AMAB adapted-work VZW (Asse Flemish maatwerk)",
                "level": "parastatal",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.amab.be/",
                "foi_email": "info@amab.be",
                "foi_postal": "Z. 5 Mollem 90, 1730 Asse",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 3 VE NACE 88.993; "
                    f"omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%) "
                    f"pnl LOSS FLIP {PNL} ({PNL_PCT}%) equity DROP {EQUITY} ({EQUITY_PCT}%) FTE {FTE}; "
                    f"neerlegging 10.06.2026; assets/debt Unknown; FOI {GAP}; after CARP@2276; "
                    "AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Asse>AMAB>NBB_PDF_assets_debt_bruto_gt_omzet_1_53x_pnl_loss_flip",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); "
                    f"omzet EUR{OMZET}; bruto EUR{BRUTO} (~{RATIO}x); pnl LOSS FLIP EUR{PNL} vs EUR{PNL24}; "
                    f"maatwerk wage-subsidy matrix; FTE {FTE}; activity split co-packing/electro/green/circular"
                ),
                "why_it_matters": (
                    f"Medium CW shows Flemish maatwerk VZW (omzet 14.18m / bruto~{RATIO}x / pnl LOSS FLIP / "
                    f"FTE {FTE}) under collectief maatwerk path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "AMAB VZW",
                "recipient_email": "info@amab.be",
                "recipient_postal": "Z. 5 Mollem 90, 1730 Asse",
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
                    "AGB Bornem JR2024; after CARP@2276; next EVERY-10 2280"
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
