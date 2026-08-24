# tick 2272 — leftover dual De Enter YE2025 Medium (bruto JUMP 4.09m / empty omzet / pnl DROP -64% / FTE 92.7)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2272
UTC = "2026-08-27T10:10:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_de_enter_brecht"
KBO = "0472.926.270"
KBO_BARE = "0472926270"
SRC_EN = "src_enter_jr2025_cw_en"
GAP = "gap_enter_nbb_pdf_assets_debt_empty_omzet_bruto_4_09m_pnl_drop_64pct_matrix_l5"
COMM = "comm_enter_jr2025_statutory_maatwerk_empty_omzet_bruto_4_09m_pnl_drop"
LB = "lb_enter_bruto_4_09m_empty_omzet_pnl_drop_64pct_jr2025"
RQ = "rq_2272"
RQ_NEXT = "rq_2273"

BRUTO = 4090845
BRUTO24 = 3504061
PNL = 92802
PNL24 = 260336
EQUITY = 1981961
EQUITY24 = 1889159
FTE = 92.7
FTE24 = 79.3
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / abs(PNL24) * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
PI = "5.85"


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
                "leftover dual — De Enter YE2025 Medium "
                f"(bruto JUMP 4.09m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; De Enter VZW Brecht {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet unpublished; bruto JUMP {BRUTO} (+{BRUTO_PCT}%); "
                f"pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE} (+{FTE_PCT}% vs {FTE24}); 7 VE; NACE 88.993/47.792; neerlegging 01.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH YE2024; "
                f"Citeco/Foes YE2024; after Serre-Outil@2271; next EVERY-10 2280"
            )
            r["instructions"] = (
                "leftover dual De Enter YE2025 FREE Flemish maatwerk Kringwinkel De Cirkel after Serre-Outil; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after De Enter — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after De Enter YE2025 Medium "
                    f"(bruto JUMP 4.09m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. TWERK/Waardenmakerij if YE2025). "
                    "Skip De Enter/La Serre-Outil/Amis des Aveugles/Hautes Ardennes/Village n°1/"
                    "Le Trait d'Union/L'Ouvroir/APRE/Brochage Renaitre/Stallbois/Sipres/La Lorraine/"
                    "BW Eupen/AJR/Alteria/Wase/ACG/Werkmmaat/Kringwinkel*/Manus*/ViTeS*/Reset/"
                    "Den Azalee/Kemphaan/Mirto/Blankedale; Relais Haute Sambre/APN/Citeco/Groupe Foes YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/"
                    "Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/"
                    "RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Senes. Next EVERY-10: 2280."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} De Enter; FARO/AIESH YE2024; AGB Bornem JR2024; "
                    "Citeco/Foes YE2024; next every-10 2280"
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
                f"tick{TICK} leftover dual De Enter {KBO} Medium (bruto JUMP {BRUTO} +{BRUTO_PCT}%; "
                f"empty omzet; pnl DROP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; "
                f"7 VE Brecht Flemish maatwerk Kringwinkel De Cirkel); after Serre-Outil@2271; "
                f"AGB Bornem JR2024; FARO/AIESH YE2024; next {RQ_NEXT}; next EVERY-10 2280; continuous hole_fill"
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
        f"""# FOI draft — De Enter (NBB PDF / empty omzet / bruto 4.09m / pnl DROP {PNL_PCT}% / Kringwinkel maatwerk)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** VZW De Enter — KBO **{KBO}** (Actief; Bethaniënlei 5, 2960 Brecht; **7 VE**; FTE {FTE} CW; NACE **88.993** / **47.792**; Flemish maatwerk / Kringwinkel De Cirkel)  
**recipient:** de.cirkel@de-cirkel.net · Bethaniënlei 5 / Klein Veerle 34, 2960 Brecht (+32 3 313 49 66)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.kringwinkel.be/centra/de-cirkel-brecht)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown; omzet unpublished)

## Context
- KBO Strong: Actief VZW DE ENTER; **7 VE**; zetel Bethaniënlei 5, 2960 Brecht; RSZ NACE **88.993**; BTW **47.792**; begindatum 22.05.2000.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% vs YE2024 EUR{BRUTO24:,}; pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); filed **01.07.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; Citeco/Groupe Foes YE2024. After Serre-Outil@2271.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: VZW De Enter
via de.cirkel@de-cirkel.net
Bethaniënlei 5, 2960 Brecht
Betreft: Openbaarheid jaarrekening 2025 De Enter (KBO {KBO})

Geachte,

Op basis van de Vlaamse regelgeving inzake openbaarheid van bestuur / sociale economie
verzoek ik om mededeling van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Omzetcijfer YE2025 (niet gepubliceerd op Companyweb) en toelichting brutomarge EUR{BRUTO}
   (+{BRUTO_PCT}%) en winstdaling EUR{PNL} ({PNL_PCT}% vs EUR{PNL24}).
3. Matrix van VDAB/maatwerk-subsidies achter personeelskosten (FTE {FTE}).
4. Opsplitsing activiteiten (Kringwinkel De Cirkel winkels / hergebruik / webshops).
5. Schulden LT/KT en liquiditeiten YE2025 (niet op Companyweb).

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


### 2026-08-27T10:10:00Z - tick 2272 - rq_2272 De Enter Brecht (bruto JUMP 4.09m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2272** leftover dual after **rq_2271 La Serre-Outil**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**. Took FREE Flemish maatwerk **De Enter VZW** YE2025 (KBO **{KBO}**; Bethaniënlei 5 Brecht; **Actief** **7 VE**; NACE **88.993** / Kringwinkel De Cirkel). Do not redo Serre-Outil/Amis/Hautes/Village n1/Trait/Ouvroir/APRE/Wase/ACG/Werkmmaat stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); neerlegging **01.07.2026**. Strong KBO Actief 7 VE VZW. Assets/debt Unknown. Medium. FOI via de.cirkel@de-cirkel.net.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2272=done + rq_2273 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2272/ + data/raw/tick2272/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2270**; next **2280**). Next: rq_2273 (AGB/FARO-if-YE2025 / AIESH-REW / unused ETA-VAPH-WZC-maatwerk).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2272"
    dst_raw = DATA / "raw" / "tick2272"
    dst_raw.mkdir(parents=True, exist_ok=True)
    src_raw.mkdir(parents=True, exist_ok=True)
    for f in dst_raw.glob("*.html"):
        shutil.copy2(f, src_raw / f.name)
    shutil.copy2(Path(__file__), src_raw / Path(__file__).name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_enter_jr2025_cw_nl",
                "title": "Companyweb NL De Enter YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet unpublished bruto JUMP {BRUTO} pnl DROP {PNL} "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 01.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2272/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN De Enter YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 01-07-2026; Last balance sheet year 2025; "
                    f"Turnover unpublished Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_enter_jr2025_cw_fr",
                "title": "Companyweb FR De Enter YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA unpublished; Marge brute {BRUTO}; Benefice {PNL}",
            },
            {
                "source_id": f"src_enter_kbo_{TICK}",
                "title": f"KBO De Enter {KBO} Actief Brecht 7 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW DE ENTER; zetel Bethaniënlei 5 2960 Brecht; "
                    f"7 VE; RSZ NACE 88.993; BTW 47.792; begindatum 22.05.2000"
                ),
            },
            {
                "source_id": f"src_enter_site_contact_{TICK}",
                "title": "De Enter FOI channel de.cirkel@de-cirkel.net",
                "url": "https://www.kringwinkel.be/centra/de-cirkel-brecht",
                "publisher": "De Enter / Kringwinkel De Cirkel",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; de.cirkel@de-cirkel.net; +32 3 313 49 66; "
                    "Bethaniënlei 5 / Klein Veerle 34 Brecht; Flemish maatwerk Kringwinkel De Cirkel"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_enter_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025 (primary; omzet unpublished)",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +{BRUTO_PCT}% vs YE2024 {BRUTO24}; empty omzet",
            },
            {
                "budget_id": "bud_enter_pnl_jr2025_statutory",
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
                "budget_id": "bud_enter_equity_jr2025_statutory",
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
                "budget_id": "bud_enter_fte_jr2025_statutory",
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
                "budget_id": "bud_enter_pnl_jr2024_statutory_cmp",
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
                    "De Enter YE2025 leftover dual "
                    f"(bruto 4.09m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "Maatwerk workers Brecht region / Kringwinkel De Cirkel public path",
                "legal_basis": f"VZW De Enter (KBO {KBO}; Actief; 7 VE; NACE 88.993; Brecht)",
                "decision_date": "2026-07-01",
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
                "stated_goal": "Flemish maatwerk / Kringwinkel De Cirkel (reuse retail Brecht-Essen-Malle-Schilde-Wuustwezel-Zandhoven)",
                "cut_option": (
                    "Publish NBB PDF assets/debt + omzet; reconcile bruto JUMP + FTE JUMP vs VDAB maatwerk matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>Antwerpen>Brecht>DeEnter>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (omzet unpublished); "
                    f"pnl DROP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 7 VE; after Serre-Outil@2271; "
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
                    f"De Enter bruto 4.09m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} "
                    "(YE2025 Flemish maatwerk Kringwinkel)"
                ),
                "level": "L5",
                "type": "maatwerk_asbl_statutory",
                "hierarchy_path": "Vlaanderen>Antwerpen>Brecht>DeEnter>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW bruto {BRUTO} (+{BRUTO_PCT}%) / omzet unpublished / pnl DROP {PNL} ({PNL_PCT}%) / "
                    f"equity JUMP {EQUITY} (+{EQUITY_PCT}%) / FTE {FTE} (vs {FTE24}) / 7 VE Kringwinkel De Cirkel"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "Maatwerk workers Brecht region / Kringwinkel De Cirkel public path",
                "stated_goal": "Flemish maatwerk / Kringwinkel De Cirkel reuse retail",
                "measured_outcome": (
                    f"bruto JUMP +{BRUTO_PCT}%; omzet unpublished; pnl DROP {PNL_PCT}%; "
                    f"equity JUMP +{EQUITY_PCT}%; FTE {FTE} (+{FTE_PCT}%); filed 01.07.2026"
                ),
                "absurdity_score": "6.5",
                "cost_score": "4.5",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/omzet FOI; disclose VDAB maatwerk matrix behind empty omzet + FTE JUMP +16.9%"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH YE2024; after Serre-Outil@2271"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "De Enter VZW (Brecht / Kringwinkel De Cirkel maatwerk)",
                "name_fr": "De Enter ASBL (Brecht / entreprise d'économie sociale / Kringwinkel)",
                "name_en": "De Enter adapted-work VZW (Brecht / Kringwinkel De Cirkel maatwerk)",
                "level": "parastatal",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.kringwinkel.be/centra/de-cirkel-brecht",
                "foi_email": "de.cirkel@de-cirkel.net",
                "foi_postal": "Bethaniënlei 5, 2960 Brecht",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 7 VE NACE 88.993; "
                    f"omzet unpublished bruto JUMP {BRUTO} (+{BRUTO_PCT}%) pnl DROP {PNL} ({PNL_PCT}%) "
                    f"equity JUMP {EQUITY} (+{EQUITY_PCT}%) FTE {FTE}; neerlegging 01.07.2026; "
                    f"assets/debt Unknown; FOI {GAP}; after Serre-Outil@2271; AGB Bornem JR2024; "
                    "FARO/AIESH YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>Antwerpen>Brecht>DeEnter>NBB_PDF_assets_debt_empty_omzet_bruto_4_09m",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet unpublished on CW; "
                    f"bruto EUR{BRUTO}; pnl DROP EUR{PNL} vs EUR{PNL24}; "
                    f"VDAB maatwerk subsidy matrix; FTE {FTE}; activity split Kringwinkel De Cirkel shops"
                ),
                "why_it_matters": (
                    f"Medium CW shows Flemish maatwerk VZW (bruto 4.09m / empty omzet / pnl DROP {PNL_PCT}% / "
                    f"FTE {FTE} JUMP) under Kringwinkel De Cirkel path; assets/debt/omzet unpublished"
                ),
                "priority": "8",
                "recipient_body": "VZW De Enter",
                "recipient_email": "de.cirkel@de-cirkel.net",
                "recipient_postal": "Bethaniënlei 5, 2960 Brecht",
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
                    "AGB Bornem JR2024; after Serre-Outil@2271; next EVERY-10 2280"
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
