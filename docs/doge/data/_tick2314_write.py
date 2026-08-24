# -*- coding: utf-8 -*-
"""Tick 2314: leftover dual Iris/Huize Iris Kontich YE2025 VAPH after Hejmen."""
from __future__ import annotations

import csv
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2314")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TICK = "2314"
RQ = "rq_2314"
NEXT_RQ = "rq_2315"
ENTITY = "vzw_iris_kontich"
KBO = "0419.665.154"
GAP = "gap_iris_kontich_nbb_pdf_assets_debt_bruto_gt_omzet_7_70x_pnl_drop_72pct_vaph_matrix_l5"
LB = "lb_iris_kontich_bruto_1_73m_omzet_0_22m_7_70x_pnl_drop_72pct_jr2025"
COMM = "comm_iris_kontich_jr2025_statutory_bruto_gt_omzet_7_70x_pnl_drop_vaph"

OMZET = 224127
OMZET24 = None  # unpublished YE2024 in CW table
BRUTO = 1725182
BRUTO24 = 1664837
PNL = 10077
PNL24 = 36574
EQUITY = 3502266
EQUITY24 = 3492189
FTE = 22.1
FTE24 = 19.0
FILED = "09.06.2026"
EMAIL = "info@huize-iris.be"
RATIO = round(BRUTO / OMZET, 2)  # ~7.70

# cost 3.5 (~1.73m) · abs 7.0 (bruto~7.7x + pnl DROP -72%) · diff 3
# pi = 0.55*3.5 + 0.35*7.0 + 0.1*7 = 5.075 → 5.1
ABS, COST, DIFF, PI = 7.0, 3.5, 3.0, 5.1


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(path, fieldnames, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


os.makedirs(RAW, exist_ok=True)
os.makedirs(FOI_DRAFTS, exist_ok=True)
with open(os.path.join(RAW, "cw_en_excerpt.txt"), "w", encoding="utf-8") as f:
    f.write(
        f"Iris Kontich YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl DROP {PNL} "
        f"equity {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0419665154/iris\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419665154\n"
        "https://huize-iris.be/\n"
    )
with open(os.path.join(RAW, "summary.json"), "w", encoding="utf-8") as f:
    f.write(
        "{\n"
        f'  "tick": "{TICK}",\n'
        f'  "unit": "{RQ}",\n'
        f'  "entity": "{ENTITY}",\n'
        f'  "kbo": "{KBO}",\n'
        f'  "omzet": {OMZET},\n'
        f'  "bruto": {BRUTO},\n'
        f'  "pnl": {PNL},\n'
        f'  "equity": {EQUITY},\n'
        f'  "fte": {FTE},\n'
        f'  "ratio": {RATIO},\n'
        f'  "confidence": "medium",\n'
        f'  "gap": "{GAP}",\n'
        f'  "pi": {PI}\n'
        "}\n"
    )

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
for ns in [
    {
        "source_id": "src_iris_kontich_jr2025_cw_en",
        "title": f"Iris Kontich YE2025 CW EN (bruto 1.73m / omzet 0.22m ~{RATIO}x / pnl DROP -72%)",
        "url": "https://www.companyweb.be/en/0419665154/iris",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW EN; omzet {OMZET} (YE2024 unpublished in CW); bruto JUMP {BRUTO} "
            f"(~{RATIO}x / +3.62%); pnl DROP {PNL} (-72.45%); equity JUMP {EQUITY}; FTE JUMP {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_iris_kontich_jr2025_cw_nl",
        "title": "Iris Kontich YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0419665154/iris",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}; same euros",
    },
    {
        "source_id": "src_iris_kontich_jr2025_cw_fr",
        "title": "Iris Kontich YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0419665154/iris",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; "
            f"capitaux {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_iris_kontich_kbo_0419665154",
        "title": "KBO IRIS 0419.665.154 Actief VZW 1 VE NACE 87.202 Kontich",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419665154",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-24",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 29.06.1979; 1 VE; Reepkenslei 53 2550 Kontich; "
            f"RSZ/BTW 87.202 adults mental disability residential"
        ),
    },
    {
        "source_id": "src_iris_kontich_site_contact_2314",
        "title": "Huize Iris FOI channel info@huize-iris.be",
        "url": "https://huize-iris.be/",
        "publisher": "Iris / Huize Iris VZW",
        "accessed_date": "2026-08-24",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Reepkenslei 53 2550 Kontich; T 03 457 53 57",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Iris / Huize Iris VZW (Kontich / VAPH)",
    "name_fr": "Iris / Huize Iris ASBL (Kontich / VAPH)",
    "name_en": "Iris / Huize Iris VZW (Kontich / VAPH residential care adults mental disability)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://huize-iris.be/",
    "foi_email": EMAIL,
    "foi_postal": "Reepkenslei 53, 2550 Kontich",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE VZW "
        f"NACE 87.202; omzet {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} (-72.45%) "
        f"equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging {FILED}; assets/debt Unknown; "
        f"FOI {GAP}; after Hejmen@2313; AGB/FARO YE2024; not TE-additive of 348bn"
    ),
}
if not any(r.get("entity_id") == ENTITY for r in erows):
    erows.append(ent)
else:
    for i, r in enumerate(erows):
        if r.get("entity_id") == ENTITY:
            erows[i] = ent
            break
write_csv(epath, efields, erows)

bpath = os.path.join(DATA, "budgets.csv")
bfields, brows = read_csv(bpath)
for nb in [
    {
        "budget_id": "bud_iris_kontich_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 primary envelope (~{RATIO}x omzet)",
        "source_id": "src_iris_kontich_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +3.62% vs {BRUTO24}; ~{RATIO}x omzet {OMZET}",
    },
    {
        "budget_id": "bud_iris_kontich_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025",
        "source_id": "src_iris_kontich_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET}; YE2024 omzet unpublished in CW table",
    },
    {
        "budget_id": "bud_iris_kontich_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 DROP",
        "source_id": "src_iris_kontich_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} DROP -72.45% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_iris_kontich_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025",
        "source_id": "src_iris_kontich_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +0.29% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_iris_kontich_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_iris_kontich_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} vs {FTE24}",
    },
]:
    if nb["budget_id"] not in {r["budget_id"] for r in brows}:
        brows.append(nb)
write_csv(bpath, bfields, brows)

cpath = os.path.join(DATA, "commitments.csv")
cfields, crows = read_csv(cpath)
comm = {
    "commitment_id": COMM,
    "title": (
        f"Iris Kontich YE2025 leftover dual (bruto 1.73m / omzet 0.22m ~{RATIO}x / "
        f"pnl DROP -72% / Medium)"
    ),
    "entity_id": ENTITY,
    "beneficiary": "adults with mental disability / Huize Iris Kontich",
    "legal_basis": f"VZW IRIS (KBO {KBO}; Actief; 1 VE; NACE 87.202; VAPH path)",
    "decision_date": "2026-06-09",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": (
        f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},'
        f'"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0419665154/iris",
    "stated_goal": "VAPH residential care adults with mental disability (Kontich)",
    "cut_option": (
        f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -72% vs VAPH/PVF"
    ),
    "source_id": "src_iris_kontich_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Kontich>Iris>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO} (~{RATIO}x); after Hejmen@2313",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": f"Iris Kontich bruto 1.73m / omzet 0.22m ~{RATIO}x / pnl DROP -72% (YE2025)",
    "level": "L5",
    "type": "vaph_residential_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Kontich>Iris>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x / +3.62%) / "
        f"pnl DROP {PNL} (-72.45%) / equity {EQUITY} / FTE JUMP {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_iris_kontich_jr2025_cw_en",
    "beneficiaries": "adults with mental disability Kontich",
    "stated_goal": "VAPH residential care",
    "measured_outcome": f"bruto÷omzet ~{RATIO}x; pnl DROP -72%; FTE {FTE}",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": (
        f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -72%"
    ),
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after Hejmen@2313; AGB/FARO YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Kontich>Iris>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — "
        f"VAPH/PVF matrix; pnl DROP EUR{PNL} (-72.45%) vs YE2024 EUR{PNL24}"
    ),
    "why_it_matters": (
        f"Medium CW shows Kontich VAPH VZW (bruto 1.73m / omzet 0.22m ~{RATIO}x / "
        f"pnl DROP -72% / FTE 22.1) under public care path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Iris / Huize Iris VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Reepkenslei 53, 2550 Kontich",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": COMM,
    "linked_leaderboard_id": LB,
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Hejmen@2313",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Iris Kontich (NBB PDF / bruto≫omzet ~{RATIO}x / pnl DROP -72%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Iris / Huize Iris VZW — KBO **{KBO}** (Actief; Reepkenslei 53, 2550 Kontich; **1 VE**; FTE {FTE}; NACE **87.202**)  
**recipient:** {EMAIL} · Reepkenslei 53, 2550 Kontich (T 03 457 53 57)  
**sources:** [CW EN](https://www.companyweb.be/en/0419665154/iris) · [CW NL](https://www.companyweb.be/nl/0419665154/iris) · [CW FR](https://www.companyweb.be/fr/0419665154/iris) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419665154) · [site](https://huize-iris.be/) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0419665154)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **IRIS** sinds **29.06.1979**; **1 VE**; zetel Reepkenslei 53, 2550 Kontich; RSZ NACE **87.202**.
- CW YE2025: omzet **EUR{OMZET:,}**; bruto **EUR{BRUTO:,}** JUMP +3.62% (~**{RATIO}x**); pnl **EUR{PNL:,}** DROP −72.45%; equity **EUR{EQUITY:,}**; FTE **{FTE}**; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024. After Hejmen@2313. Do NOT redo Hejmen/Willekom/Zewopa/Domino/M HKA stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Iris / Huize Iris VZW
via {EMAIL}
Reepkenslei 53, 2550 Kontich
Betreft: Openbaarmaking jaarrekening 2025 Iris (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting waarom bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — VAPH/PVF-matrix.
3. Toelichting pnl DROP EUR{PNL} (−72.45% vs YE2024 EUR{PNL24}).
4. Overzicht publieke toelagen/PVF/VAPH-stromen YE2025.
5. Schulden LT/KT en liquide middelen YE2025.

Periode YE2025 (+ YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
"""
with open(os.path.join(FOI_DRAFTS, f"{GAP}.md"), "w", encoding="utf-8") as f:
    f.write(draft)

rqpath = os.path.join(DATA, "research_queue.csv")
rqfields, rqrows = read_csv(rqpath)
for r in rqrows:
    if r.get("task_id") == RQ:
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["title"] = (
            f"leftover dual — Iris Kontich YE2025 Medium "
            f"(bruto JUMP 1.73m / ~{RATIO}x omzet / pnl DROP -72% / FTE JUMP 22.1)"
        )
        r["notes"] = (
            f"tick{TICK} Iris {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet {OMZET}; bruto JUMP {BRUTO} (~{RATIO}x); pnl DROP {PNL}; "
            f"equity JUMP {EQUITY}; FTE JUMP {FTE}; 1 VE NACE 87.202 Kontich; "
            f"neerlegging {FILED}; FOI ready NOT sent; after Hejmen@2313; next EVERY-10 2320"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after Iris Kontich — prefer AGB/FARO-YE2025/"
                "AIESH/or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Iris Kontich YE2025 Medium "
                f"(bruto 1.73m / omzet 0.22m ~{RATIO}x / pnl DROP -72%). "
                "Prefer AGB/FARO if YE2025 else FREE ETA-VAPH-WZC-maatwerk "
                "(Manupal/Aralea/Vlotter/Gandae if YE2025; Citeco/Groupe Foes if YE2025). "
                "Do NOT redo Iris/Hejmen/Willekom/Zewopa/Domino/M HKA/Katrinahof stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK} Iris; AGB/FARO YE2024; next EVERY-10 2320",
        }
    )
write_csv(rqpath, rqfields, rqrows)

lspath = os.path.join(DATA, "loop_state.csv")
lsfields, lsrows = read_csv(lspath)
for r in lsrows:
    if r.get("state_id") == "main":
        r["mode"] = "continuous"
        r["current_sprint"] = "hole_fill"
        r["last_tick_utc"] = UTC
        r["last_unit_id"] = RQ
        r["ticks_completed"] = TICK
        r["paused"] = "no"
        r["notes"] = (
            f"tick{TICK} leftover dual Iris Kontich {KBO} Medium "
            f"(omzet {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -72.45%; "
            f"equity JUMP {EQUITY}; FTE JUMP {FTE}; 1 VE VAPH Kontich); after Hejmen@2313; "
            f"AGB/FARO YE2024; next {NEXT_RQ}; next EVERY-10 2320; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Iris Kontich (bruto JUMP 1.73m / ~{RATIO}x omzet / pnl DROP -72% / Medium)

- Unit: **{RQ}** leftover dual after **Hejmen@2313**. Prefer NON-stall: AGB Bornem still **JR2024**; FARO still **YE2024**. Took unused FREE Flemish VAPH **Iris / Huize Iris VZW** YE2025 (KBO **{KBO}**; Reepkenslei 53 Kontich; **Actief** **1 VE**; NACE **87.202**). Do not redo Hejmen/Willekom/Zewopa/Domino/M HKA stack.
- Found: Companyweb NL+EN YE2025 - omzet **EUR{OMZET}**; bruto **EUR{BRUTO}** JUMP +3.62% (~**{RATIO}x**); pnl **EUR{PNL}** DROP -72.45%; equity **EUR{EQUITY}**; FTE **{FTE}**; neerlegging **{FILED}**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next EVERY-10 2320**). Next: {NEXT_RQ}.
"""
    )

print(
    f"OK tick{TICK} {ENTITY} bruto={BRUTO} omzet={OMZET} ratio={RATIO}x "
    f"pnl={PNL} pi={PI} next={NEXT_RQ}"
)
