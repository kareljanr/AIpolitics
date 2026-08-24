# tick 2278 — leftover dual m-accent YE2025 Medium (omzet JUMP 2.75m / bruto~1.63x / pnl JUMP +87% / FTE 91.9)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2278
UTC = "2026-08-27T11:45:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_m_accent_eeklo"
KBO = "0465.841.411"
KBO_BARE = "0465841411"
SRC_EN = "src_maccent_jr2025_cw_en"
GAP = "gap_maccent_nbb_pdf_assets_debt_bruto_gt_omzet_1_63x_pnl_jump_87pct_matrix_l5"
COMM = "comm_maccent_jr2025_statutory_maatwerk_omzet_2_75m_pnl_jump"
LB = "lb_maccent_omzet_2_75m_bruto_1_63x_pnl_jump_87pct_jr2025"
RQ = "rq_2278"
RQ_NEXT = "rq_2279"

OMZET = 2747558
OMZET24 = 2499264
BRUTO = 4486626
BRUTO24 = 3938259
PNL = 774084
PNL24 = 414796
EQUITY = 6353816
EQUITY24 = 5598652
FTE = 91.9
FTE24 = 84.1
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / abs(PNL24) * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
RATIO = round(BRUTO / OMZET, 2)
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
                "leftover dual — m-accent YE2025 Medium "
                f"(omzet JUMP 2.75m / bruto~{RATIO}x / pnl JUMP / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; m-accent VZW Eeklo {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}%); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl JUMP {PNL} ({PNL_PCT}% vs {PNL24}); equity JUMP {EQUITY} ({EQUITY_PCT}%); "
                f"FTE {FTE} (+{FTE_PCT}% vs {FTE24}); 6 VE; NACE 47.792/47.793 (maatwerk/Kringwinkel); neerlegging 14.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / "
                f"FARO/AIESH/Citeco/Groupe Foes YE2024; after AMAB@2277  ; next EVERY-10 2280"
            )
            r["instructions"] = (
                "leftover dual m-accent YE2025 FREE Flemish maatwerk/Kringwinkel Meetjesland after AMAB; "
                "preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after m-accent — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after m-accent YE2025 Medium "
                    f"(omzet JUMP 2.75m / bruto~{RATIO}x / pnl JUMP / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                    "else unused ETA-VAPH-WZC-maatwerk with live sourced euros. "
                    "Skip m-accent/C.A.R.P./Atelier Saint-Vincent/A.P.A.C./Adapta/Atelier 85/La Gaume/"
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
                    f"spawned after tick{TICK} m-accent; FARO/AIESH/Citeco/Groupe Foes YE2024; "
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
                f"tick{TICK} leftover dual m-accent {KBO} Medium (omzet JUMP {OMZET} +{OMZET_PCT}%; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; "
                f"6 VE Eeklo Meetjesland Kringwinkel maatwerk); after AMAB@2277; "
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
        f"""# FOI draft — m-accent (NBB PDF / bruto~{RATIO}x omzet / pnl JUMP / Flemish maatwerk/Kringwinkel)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** m-accent VZW — KBO **{KBO}** (Actief; Slachthuisstraat 2/B, 9900 Eeklo; **6 VE**; FTE {FTE} CW; NACE **47.792/47.793** (Kringwinkel; maatwerk Crevits list); Flemish maatwerk/Kringwinkel Meetjesland)  
**recipient:** info@m-accent.be · Slachthuisstraat 2/B, 9900 Eeklo (+32 9 377 77 74)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}/m-accent) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}/m-accent) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}/m-accent) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_BARE}) · [site](https://www.m-accent.be/) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/{KBO_BARE})  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW m-accent; **6 VE**; zetel Slachthuisstraat 2/B, 9900 Eeklo; email info@m-accent.be; RSZ/BTW NACE **47.792/47.793** (Kringwinkel; maatwerk Crevits list); begindatum 16.10.1998; sites Eeklo/Maldegem Meetjesland Kringwinkel.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (~{RATIO}x omzet); pnl **EUR{PNL:,}** JUMP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); filed **14.07.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; Citeco YE2024; Groupe Foes YE2024; Manupal YE2024. After C.A.R.P.@2276 (+Atelier Saint-Vincent race).

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: m-accent VZW
via info@m-accent.be
Slachthuisstraat 2/B, 9900 Eeklo
Betreft: Openbaarmaking jaarrekening 2025 m-accent (KBO {KBO})

Geachte,

Op basis van de regels inzake openbaarheid van bestuur (Vlaamse Codex / Vlaamse
regelgeving sociale economie / maatwerkdecreet) vraag ik mededeling van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij brutomarge EUR{BRUTO} (~{RATIO}x omzet EUR{OMZET}) en winstsprong
   EUR{PNL} (+{PNL_PCT}% vs EUR{PNL24}) vs publieke maatwerk-loonsubsidies.
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


### 2026-08-27T11:45:00Z - tick 2278 - rq_2278 m-accent Eeklo (omzet JUMP 2.75m / bruto~{RATIO}x / pnl JUMP / FTE {FTE} / Medium)

- Unit: **rq_2278** leftover dual after **rq_2277 AMAB**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**; Manupal YE2024. Took FREE Flemish maatwerk/Kringwinkel **m-accent VZW** YE2025 (KBO **{KBO}**; Slachthuisstraat 2/B Eeklo; **Actief** **6 VE**; NACE **47.792/47.793** (Kringwinkel; maatwerk Crevits list) Eeklo Meetjesland Kringwinkel). Do not redo AMAB/CARP/ASV/APAC/Adapta/Atelier85/Forena/Waak/OptimaT stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (~{RATIO}x); pnl **EUR{PNL}** JUMP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); neerlegging **14.07.2026**. Strong KBO Actief 6 VE VZW info@m-accent.be. Assets/debt Unknown. Medium.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2278=done + rq_2279 open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2278/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2270**; next **2280**). Next: rq_2278 (AGB/FARO-if-YE2025 / AIESH-REW / Citeco-Foes-if-YE2025 / unused ETA).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2278"
    dst_raw = DATA / "raw" / "tick2278"
    dst_raw.mkdir(parents=True, exist_ok=True)
    src_raw.mkdir(parents=True, exist_ok=True)
    for f in dst_raw.glob("*.html"):
        shutil.copy2(f, src_raw / f.name)
    shutil.copy2(Path(__file__), src_raw / Path(__file__).name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_maccent_jr2025_cw_nl",
                "title": "Companyweb NL m-accent YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}/m-accent",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 14.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2278/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN m-accent YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}/m-accent",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 14-07-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_maccent_jr2025_cw_fr",
                "title": "Companyweb FR m-accent YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}/m-accent",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Benefice {PNL}",
            },
            {
                "source_id": f"src_maccent_kbo_{TICK}",
                "title": f"KBO m-accent {KBO} Actief Eeklo 6 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW m-accent; zetel Slachthuisstraat 2/B 9900 Eeklo; "
                    f"6 VE; NACE 47.792/47.793 (maatwerk/Kringwinkel); info@m-accent.be; begindatum 16.10.1998"
                ),
            },
            {
                "source_id": f"src_maccent_site_contact_{TICK}",
                "title": "m-accent FOI channel info@m-accent.be",
                "url": "https://www.m-accent.be/",
                "publisher": "m-accent VZW",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@m-accent.be; +32 9 377 77 74; "
                    "Slachthuisstraat 2/B Eeklo; Flemish maatwerk/Kringwinkel Meetjesland"
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
                "basis": "CW statutory winst/verlies YE2025 JUMP",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl JUMP {PNL_PCT}% vs YE2024 {PNL24}",
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
                "notes": f"tick{TICK}; Medium CW; equity JUMP +{EQUITY_PCT}% vs YE2024 {EQUITY24}",
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
                    "m-accent YE2025 leftover dual "
                    f"(omzet 2.75m / bruto~{RATIO}x / pnl JUMP / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "maatwerk workers Eeklo Meetjesland Kringwinkel / Flemish collectief maatwerk",
                "legal_basis": f"VZW maatwerk m-accent (KBO {KBO}; Actief; 6 VE; NACE 47.792/47.793 (maatwerk/Kringwinkel); Eeklo)",
                "decision_date": "2026-07-14",
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
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}/m-accent",
                "stated_goal": "Flemish maatwerk/Kringwinkel Meetjesland (kringwinkel / secondhand retail / social employment)",
                "cut_option": (
                    "Publish NBB PDF assets/debt; reconcile bruto>~1.6x omzet + pnl JUMP vs maatwerk wage-subsidy matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>OostVlaanderen>Eeklo>m-accent>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (omzet {OMZET} ~{RATIO}x); "
                    f"pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 6 VE; after AMAB@2277; "
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
                    f"m-accent omzet 2.75m / bruto~{RATIO}x / pnl JUMP / FTE {FTE} "
                    "(YE2025 Flemish maatwerk/Kringwinkel Eeklo)"
                ),
                "level": "L5",
                "type": "maatwerk_vzw_statutory",
                "hierarchy_path": "Vlaanderen>OostVlaanderen>Eeklo>m-accent>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW omzet {OMZET} (+{OMZET_PCT}%) / bruto {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%) / "
                    f"pnl JUMP {PNL} ({PNL_PCT}%) / equity JUMP {EQUITY} ({EQUITY_PCT}%) / "
                    f"FTE {FTE} (vs {FTE24}) / 6 VE Flemish maatwerk/Kringwinkel"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "maatwerk workers Eeklo Meetjesland Kringwinkel / Flemish collectief maatwerk",
                "stated_goal": "Flemish maatwerk/Kringwinkel Meetjesland (kringwinkel/secondhand)",
                "measured_outcome": (
                    f"omzet JUMP +{OMZET_PCT}%; bruto JUMP +{BRUTO_PCT}% (~{RATIO}x); "
                    f"pnl JUMP {PNL_PCT}%; equity JUMP +{EQUITY_PCT}%; FTE {FTE}; filed 10.06.2026"
                ),
                "absurdity_score": "5.8",
                "cost_score": "4.5",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt FOI; disclose maatwerk wage-subsidy matrix behind bruto>~1.6x omzet"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/Citeco/Groupe Foes YE2024; after AMAB@2277"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "m-accent VZW (Eeklo / Flemish maatwerk/Kringwinkel)",
                "name_fr": "m-accent ASBL (Eeklo / entreprise de travail adapté flamande)",
                "name_en": "m-accent adapted-work VZW (Eeklo Flemish maatwerk/Kringwinkel)",
                "level": "parastatal",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.m-accent.be/",
                "foi_email": "info@m-accent.be",
                "foi_postal": "Slachthuisstraat 2/B, 9900 Eeklo",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 6 VE NACE 47.792/47.793 (maatwerk/Kringwinkel); "
                    f"omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%) "
                    f"pnl JUMP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} ({EQUITY_PCT}%) FTE {FTE}; "
                    f"neerlegging 14.07.2026; assets/debt Unknown; FOI {GAP}; after AMAB@2277; "
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
                "hierarchy_path": "Vlaanderen>OostVlaanderen>Eeklo>m-accent>NBB_PDF_assets_debt_bruto_gt_omzet_1_63x_pnl_jump",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); "
                    f"omzet EUR{OMZET}; bruto EUR{BRUTO} (~{RATIO}x); pnl JUMP EUR{PNL} vs EUR{PNL24}; "
                    f"maatwerk wage-subsidy matrix; FTE {FTE}; activity split kringwinkel/secondhand/circular"
                ),
                "why_it_matters": (
                    f"Medium CW shows Flemish maatwerk/Kringwinkel VZW (omzet 2.75m / bruto~{RATIO}x / pnl JUMP / "
                    f"FTE {FTE}) under collectief maatwerk / Kringwinkel Meetjesland path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "m-accent VZW",
                "recipient_email": "info@m-accent.be",
                "recipient_postal": "Slachthuisstraat 2/B, 9900 Eeklo",
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
                    "AGB Bornem JR2024; after AMAB@2277; next EVERY-10 2280"
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
