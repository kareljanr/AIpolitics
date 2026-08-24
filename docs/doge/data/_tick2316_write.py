# -*- coding: utf-8 -*-
"""Tick 2316: leftover dual Olo-Rotonde Brasschaat YE2025 VAPH after Havenzate."""
from __future__ import annotations

import csv
import json
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2316")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TICK = "2316"
RQ = "rq_2316"
NEXT_RQ = "rq_2317"
ENTITY = "vzw_olo_rotonde_brasschaat"
KBO = "0406.677.745"
GAP = "gap_olo_rotonde_nbb_pdf_assets_debt_bruto_gt_omzet_9_53x_pnl_drop_vaph_matrix_l5"
LB = "lb_olo_rotonde_bruto_66_85m_omzet_7_01m_9_53x_pnl_drop_jr2025"
COMM = "comm_olo_rotonde_jr2025_statutory_bruto_gt_omzet_9_53x_vaph"

OMZET = 7014913
OMZET24 = 6455332
BRUTO = 66852480
BRUTO24 = 64201893
PNL = 1458369
PNL24 = 1610841
EQUITY = 52557823
EQUITY24 = 51805076
FTE = 854.6
FTE24 = 834.0
FILED = "19.06.2026"
EMAIL = "info@olo-rotonde.be"
RATIO = round(BRUTO / OMZET, 2)
ABS, COST, DIFF, PI = 8.0, 5.5, 3.0, 6.55


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
        f"Olo-Rotonde YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl DROP {PNL} "
        f"equity {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0406677745/olo-rotonde\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406677745\n"
        "https://www.olo-rotonde.be/\n"
    )
with open(os.path.join(RAW, "summary.json"), "w", encoding="utf-8") as f:
    json.dump(
        {
            "tick": TICK,
            "unit": RQ,
            "entity": ENTITY,
            "kbo": KBO,
            "omzet": OMZET,
            "bruto": BRUTO,
            "pnl": PNL,
            "equity": EQUITY,
            "fte": FTE,
            "ratio": RATIO,
            "confidence": "medium",
            "gap": GAP,
            "pi": PI,
        },
        f,
        indent=2,
    )
    f.write("\n")

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
for ns in [
    {
        "source_id": "src_olo_rotonde_jr2025_cw_en",
        "title": f"Olo-Rotonde YE2025 CW EN (bruto 66.85m / omzet 7.01m ~{RATIO}x)",
        "url": "https://www.companyweb.be/en/0406677745/olo-rotonde",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW EN; omzet JUMP {OMZET} (+8.67%); bruto JUMP {BRUTO} "
            f"(~{RATIO}x / +4.13%); pnl DROP {PNL} (-9.47%); equity JUMP {EQUITY}; "
            f"FTE JUMP {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_olo_rotonde_jr2025_cw_nl",
        "title": "Olo-Rotonde YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0406677745/olo-rotonde",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}",
    },
    {
        "source_id": "src_olo_rotonde_jr2025_cw_fr",
        "title": "Olo-Rotonde YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0406677745/olo-rotonde",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; "
            f"capitaux {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_olo_rotonde_kbo_0406677745",
        "title": "KBO Olo-Rotonde 0406.677.745 Actief VZW Brasschaat NACE 87.202",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406677745",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-24",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 18.06.1969; Miksebaan 264 B 2930 Brasschaat; "
            f"multi-VE VAPH"
        ),
    },
    {
        "source_id": "src_olo_rotonde_site_contact_2316",
        "title": "Olo-Rotonde FOI channel info@olo-rotonde.be",
        "url": "https://www.olo-rotonde.be/",
        "publisher": "Olo-Rotonde VZW",
        "accessed_date": "2026-08-24",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Miksebaan 264 B 2930 Brasschaat; T 03 633 98 50",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Olo-Rotonde VZW (Brasschaat / VAPH orthopedagogisch)",
    "name_fr": "Olo-Rotonde ASBL (Brasschaat / VAPH)",
    "name_en": "Olo-Rotonde VZW (Brasschaat / VAPH disability care group)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.olo-rotonde.be/",
    "foi_email": EMAIL,
    "foi_postal": "Miksebaan 264 B, 2930 Brasschaat",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; omzet JUMP {OMZET} "
        f"bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; "
        f"neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; after Havenzate@2315; "
        f"AGB/FARO YE2024; not TE-additive of 348bn"
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
        "budget_id": "bud_olo_rotonde_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 primary (~{RATIO}x omzet)",
        "source_id": "src_olo_rotonde_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +4.13% vs {BRUTO24}",
    },
    {
        "budget_id": "bud_olo_rotonde_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025",
        "source_id": "src_olo_rotonde_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET} JUMP +8.67% vs {OMZET24}",
    },
    {
        "budget_id": "bud_olo_rotonde_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 DROP",
        "source_id": "src_olo_rotonde_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} DROP -9.47% vs {PNL24}",
    },
    {
        "budget_id": "bud_olo_rotonde_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025",
        "source_id": "src_olo_rotonde_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +1.45% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_olo_rotonde_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_olo_rotonde_jr2025_cw_en",
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
    "title": f"Olo-Rotonde YE2025 leftover dual (bruto 66.85m / omzet 7.01m ~{RATIO}x / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "VAPH users / children youth adults disability Antwerpen-Gent",
    "legal_basis": f"VZW Olo-Rotonde (KBO {KBO}; Actief; multi-VE; NACE 87.202)",
    "decision_date": "2026-06-19",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": (
        f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_omzet":{OMZET24},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},'
        f'"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0406677745/olo-rotonde",
    "stated_goal": "VAPH orthopedagogical care / education / day / residential",
    "cut_option": f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x + VAPH/PVF matrix",
    "source_id": "src_olo_rotonde_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Brasschaat>OloRotonde>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO} (~{RATIO}x); after Havenzate@2315",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": f"Olo-Rotonde bruto 66.85m / omzet 7.01m ~{RATIO}x / pnl DROP (YE2025)",
    "level": "L5",
    "type": "vaph_group_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Brasschaat>OloRotonde>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet JUMP {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x) / pnl DROP {PNL} / "
        f"equity JUMP {EQUITY} / FTE JUMP {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_olo_rotonde_jr2025_cw_en",
    "beneficiaries": "VAPH users Antwerpen-Gent",
    "stated_goal": "VAPH disability care group",
    "measured_outcome": f"bruto÷omzet ~{RATIO}x; FTE {FTE}; equity 52.6m; VAPH subsidy opacity",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x vs VAPH/PVF",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after Havenzate@2315; AGB/FARO YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Brasschaat>OloRotonde>NBB_PDF_assets_debt_bruto_gt_omzet",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} "
        f"(~{RATIO}x) — VAPH/PVF matrix; pnl DROP EUR{PNL}"
    ),
    "why_it_matters": (
        f"Medium CW shows large VAPH group Brasschaat (bruto 66.85m / omzet 7.01m ~{RATIO}x / "
        f"FTE 854.6) under public care path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Olo-Rotonde VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Miksebaan 264 B, 2930 Brasschaat",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Havenzate@2315",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Olo-Rotonde (NBB PDF / bruto≫omzet ~{RATIO}x)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Olo-Rotonde VZW — KBO **{KBO}** (Actief; Miksebaan 264 B, 2930 Brasschaat; FTE {FTE}; NACE **87.202**; VAPH)  
**recipient:** {EMAIL} · Miksebaan 264 B, 2930 Brasschaat (T 03 633 98 50)  
**sources:** [CW EN](https://www.companyweb.be/en/0406677745/olo-rotonde) · [CW NL](https://www.companyweb.be/nl/0406677745/olo-rotonde) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406677745) · [site](https://www.olo-rotonde.be/)  
**tick:** {TICK}  
**confidence:** Medium

## Context
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +8.67%; bruto **EUR{BRUTO:,}** JUMP +4.13% (~**{RATIO}x**); pnl **EUR{PNL:,}** DROP −9.47%; equity **EUR{EQUITY:,}**; FTE **{FTE}**; filed **{FILED}**.
- After Havenzate@2315. Stalls AGB/FARO YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Olo-Rotonde VZW
via {EMAIL}
Miksebaan 264 B, 2930 Brasschaat
Betreft: Openbaarmaking jaarrekening 2025 Olo-Rotonde (KBO {KBO})

Geachte,
Op grond van openbaarheid van bestuur vraag ik:
1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — VAPH/PVF-matrix.
3. Overzicht publieke toelagen YE2025.
4. Schulden LT/KT en liquide middelen YE2025.
Ref: {GAP}
Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent
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
            f"leftover dual — Olo-Rotonde YE2025 Medium "
            f"(bruto JUMP 66.85m / ~{RATIO}x omzet / FTE JUMP 854.6)"
        )
        r["notes"] = (
            f"tick{TICK} Olo-Rotonde {KBO} YE2025 Medium; omzet {OMZET}; bruto {BRUTO} ~{RATIO}x; "
            f"pnl {PNL}; equity {EQUITY}; FTE {FTE}; FOI ready NOT sent; after Havenzate@2315; "
            f"next EVERY-10 2320"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after Olo-Rotonde — prefer AGB/FARO-YE2025/"
                "AIESH/or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Olo-Rotonde YE2025 Medium "
                f"(bruto 66.85m / omzet 7.01m ~{RATIO}x). Prefer AGB/FARO if YE2025 else FREE "
                f"(Start West-Vlaanderen / De Plek / Manupal if YE2025). "
                f"Do NOT redo Olo-Rotonde/Havenzate/Iris/Hejmen/Domino stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK}; next EVERY-10 2320",
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
            f"tick{TICK} leftover dual Olo-Rotonde {KBO} Medium "
            f"(omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL}; "
            f"equity JUMP {EQUITY}; FTE JUMP {FTE}); after Havenzate@2315; AGB/FARO YE2024; "
            f"next {NEXT_RQ}; next EVERY-10 2320; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Olo-Rotonde Brasschaat (bruto JUMP 66.85m / ~{RATIO}x omzet / FTE JUMP 854.6 / Medium)

- Unit: **{RQ}** leftover dual after **Havenzate@2315**. Prefer NON-stall: AGB/FARO still **YE2024**. Took unused FREE Flemish VAPH mega-group **Olo-Rotonde VZW** YE2025 (KBO **{KBO}**; Miksebaan 264 B Brasschaat; **Actief**; NACE **87.202**; FTE **854.6**). Do not redo Havenzate/Iris/Hejmen/Domino/Willekom/Zewopa stack.
- Found: Companyweb NL+EN YE2025 - omzet **EUR{OMZET}** JUMP +8.67%; bruto **EUR{BRUTO}** JUMP +4.13% (~**{RATIO}x**); pnl **EUR{PNL}** DROP -9.47%; equity **EUR{EQUITY}**; FTE **{FTE}**; neerlegging **{FILED}**. Strong KBO. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}.
- FOI: **ready not sent**. NOT every-10 (next **2320**). Next: {NEXT_RQ}.
"""
    )

print(f"OK tick{TICK} {ENTITY} bruto={BRUTO} omzet={OMZET} ratio={RATIO}x pi={PI} next={NEXT_RQ}")
