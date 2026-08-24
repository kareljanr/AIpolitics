# -*- coding: utf-8 -*-
"""Tick 2325: leftover dual Ithaka Oostende YE2025 VAPH after Ritmica."""
from __future__ import annotations

import csv
import json
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2325")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TICK = "2325"
RQ = "rq_2325"
NEXT_RQ = "rq_2326"
ENTITY = "vzw_ithaka_oostende"
KBO = "0448.387.646"
GAP = "gap_ithaka_nbb_pdf_assets_debt_empty_omzet_bruto_1_68m_pnl_loss_flip_vaph_matrix_l5"
LB = "lb_ithaka_empty_omzet_bruto_1_68m_pnl_loss_flip_jr2025"
COMM = "comm_ithaka_jr2025_statutory_empty_omzet_bruto_1_68m_vaph"

OMZET = None  # unpublished / empty
BRUTO = 1680736
BRUTO24 = 1598151
PNL = -29736
PNL24 = 116416
EQUITY = 1029376
EQUITY24 = 1071386
FTE = 20.8
FTE24 = 20.2
FILED = "18.06.2026"
EMAIL = "info@vzw-ithaka.be"

# cost 3.5 (~1.68m) · abs 6.5 (empty omzet + pnl LOSS FLIP) · diff 3
# pi = 0.55*3.5 + 0.35*6.5 + 0.1*7 = 4.9
ABS, COST, DIFF, PI = 6.5, 3.5, 3.0, 4.9


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
        f"Ithaka YE2025 empty omzet bruto {BRUTO} pnl LOSS FLIP {PNL} "
        f"equity DROP {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0448387646/ithaka\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0448387646\n"
        "https://vzw-ithaka.be/nl/\n"
    )
with open(os.path.join(RAW, "summary.json"), "w", encoding="utf-8") as f:
    json.dump(
        {
            "tick": TICK,
            "unit": RQ,
            "entity": ENTITY,
            "kbo": KBO,
            "omzet": None,
            "bruto": BRUTO,
            "pnl": PNL,
            "equity": EQUITY,
            "fte": FTE,
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
        "source_id": "src_ithaka_jr2025_cw_en",
        "title": "Ithaka Oostende YE2025 CW EN (empty omzet / bruto 1.68m / pnl LOSS FLIP)",
        "url": "https://www.companyweb.be/en/0448387646/ithaka",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW EN; omzet empty/unpublished; bruto JUMP {BRUTO} (+5.17%); "
            f"pnl LOSS FLIP {PNL} (-125.54% vs {PNL24}); equity DROP {EQUITY} (-3.92%); "
            f"FTE {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_ithaka_jr2025_cw_nl",
        "title": "Ithaka Oostende YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0448387646/ithaka",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}; geen omzet",
    },
    {
        "source_id": "src_ithaka_jr2025_cw_fr",
        "title": "Ithaka Oostende YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0448387646/ithaka",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW FR; CA non publié; marge brute {BRUTO}; résultat {PNL}; "
            f"capitaux {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_ithaka_kbo_0448387646",
        "title": "KBO Ithaka 0448.387.646 Actief VZW Oostende NACE day centres disability",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0448387646",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-24",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 13.07.1992; Kaaistraat 35 8400 Oostende; "
            f"dagcentra volwassenen mentale handicap"
        ),
    },
    {
        "source_id": "src_ithaka_site_contact_2325",
        "title": "Ithaka FOI channel info@vzw-ithaka.be",
        "url": "https://vzw-ithaka.be/nl/",
        "publisher": "Ithaka VZW",
        "accessed_date": "2026-08-24",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Kaaistraat 35 8400 Oostende; T 059 51 48 10",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Ithaka VZW (Oostende / VAPH coaching & dagcentrum)",
    "name_fr": "Ithaka ASBL (Ostende / VAPH)",
    "name_en": "Ithaka VZW (Ostend / VAPH disability coaching centre)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://vzw-ithaka.be/nl/",
    "foi_email": EMAIL,
    "foi_postal": "Kaaistraat 35, 8400 Oostende",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; omzet empty; "
        f"bruto JUMP {BRUTO}; pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE {FTE}; "
        f"neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; after Ritmica@2324; "
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
        "budget_id": "bud_ithaka_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW statutory bruto YE2025 primary (omzet unpublished)",
        "source_id": "src_ithaka_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +5.17% vs {BRUTO24}",
    },
    {
        "budget_id": "bud_ithaka_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 LOSS FLIP",
        "source_id": "src_ithaka_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} LOSS FLIP vs profit {PNL24}",
    },
    {
        "budget_id": "bud_ithaka_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025 DROP",
        "source_id": "src_ithaka_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} DROP -3.92% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_ithaka_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_ithaka_jr2025_cw_en",
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
    "title": "Ithaka YE2025 leftover dual (empty omzet / bruto 1.68m / pnl LOSS FLIP / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "VAPH adults disability coaching / day / housing Oostende-Gistel",
    "legal_basis": f"VZW Ithaka (KBO {KBO}; Actief; NACE day centres mental disability)",
    "decision_date": "2026-06-18",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": (
        f'{{"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},'
        f'"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0448387646/ithaka",
    "stated_goal": "VAPH inclusive coaching work leisure housing",
    "cut_option": "Publish NBB PDF assets/debt; publish omzet; reconcile VAPH/PVF matrix vs bruto",
    "source_id": "src_ithaka_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Oostende>Ithaka>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; empty omzet; after Ritmica@2324",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": "Ithaka empty omzet / bruto 1.68m / pnl LOSS FLIP (YE2025)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Oostende>Ithaka>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet empty / bruto JUMP {BRUTO} / pnl LOSS FLIP {PNL} / "
        f"equity DROP {EQUITY} / FTE {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_ithaka_jr2025_cw_en",
    "beneficiaries": "VAPH adults Oostende coast",
    "stated_goal": "VAPH coaching / day / housing",
    "measured_outcome": f"empty omzet; pnl LOSS FLIP; bruto {BRUTO}; FTE {FTE}",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": "Publish NBB PDF assets/debt FOI; publish omzet; reconcile VAPH subsidy path",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after Ritmica@2324; AGB/FARO YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Oostende>Ithaka>NBB_PDF_assets_debt_empty_omzet",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why omzet unpublished while bruto EUR{BRUTO}; "
        f"pnl LOSS FLIP EUR{PNL}; VAPH/PVF matrix"
    ),
    "why_it_matters": (
        "Medium CW shows VAPH coaching centre Oostende (empty omzet / bruto 1.68m / pnl LOSS FLIP / "
        "FTE 20.8) under public care path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Ithaka VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Kaaistraat 35, 8400 Oostende",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Ritmica@2324",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Ithaka Oostende (NBB PDF / empty omzet / pnl LOSS FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Ithaka VZW — KBO **{KBO}** (Actief; Kaaistraat 35, 8400 Oostende; FTE {FTE}; VAPH coaching/dagcentrum)  
**recipient:** {EMAIL} · Kaaistraat 35, 8400 Oostende (T 059 51 48 10)  
**sources:** [CW EN](https://www.companyweb.be/en/0448387646/ithaka) · [CW NL](https://www.companyweb.be/nl/0448387646/ithaka) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0448387646) · [site](https://vzw-ithaka.be/nl/)  
**tick:** {TICK}  
**confidence:** Medium

## Context
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** JUMP +5.17%; pnl **EUR{PNL:,}** LOSS FLIP; equity **EUR{EQUITY:,}** DROP −3.92%; FTE **{FTE}**; filed **{FILED}**.
- After Ritmica@2324. Stalls AGB Bornem/FARO/AIESH still YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Ithaka VZW
via {EMAIL}
Kaaistraat 35, 8400 Oostende
Betreft: Openbaarmaking jaarrekening 2025 Ithaka (KBO {KBO})

Geachte,
Op grond van openbaarheid van bestuur vraag ik:
1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Omzetcijfer YE2025 (CW toont leeg) en toelichting vs bruto EUR{BRUTO}.
3. Toelichting pnl LOSS FLIP EUR{PNL} — VAPH/PVF-matrix.
4. Overzicht publieke toelagen YE2025.
5. Schulden LT/KT en liquide middelen YE2025.
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
            "leftover dual — Ithaka YE2025 Medium "
            "(empty omzet / bruto JUMP 1.68m / pnl LOSS FLIP / FTE 20.8)"
        )
        r["notes"] = (
            f"tick{TICK} Ithaka {KBO} YE2025 Medium; omzet empty; bruto {BRUTO}; "
            f"pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE {FTE}; FOI ready NOT sent; "
            f"after Ritmica@2324; next EVERY-10 2330"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after Ithaka — prefer AGB/FARO-YE2025/"
                "AIESH/or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "After Ithaka YE2025 Medium (empty omzet / bruto 1.68m / pnl LOSS FLIP). "
                "Prefer AGB Bornem/APB → FARO/AIESH/REW if YE2025 → unused DSO/water/nuclear/"
                "IGS/HVZ (optional FREE: De Plek/Gandae/Aralea/Manupal/Vlotter/Het Eepos/"
                "Pleegzorg if YE2025 unfilled). Do NOT redo Ithaka/Ritmica/Dominiek Savio/"
                "Merlijn/Humival/Heder/Kindervriend/Schoonderhage stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK}; next EVERY-10 2330",
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
            f"tick{TICK} leftover dual Ithaka {KBO} Medium "
            f"(omzet empty; bruto JUMP {BRUTO}; pnl LOSS FLIP {PNL}; "
            f"equity DROP {EQUITY}; FTE {FTE}); after Ritmica@2324; AGB/FARO YE2024; "
            f"next {NEXT_RQ}; next EVERY-10 2330; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Ithaka Oostende (empty omzet / bruto JUMP 1.68m / pnl LOSS FLIP / Medium)

- Unit: **{RQ}** leftover dual after **Ritmica@2324**. Prefer NON-stall: AGB Bornem still **JR2024**; FARO/AIESH still **YE2024**. Took unused FREE Flemish VAPH **Ithaka VZW** YE2025 (KBO **{KBO}**; Kaaistraat 35 Oostende; **Actief**; dagcentra mentale handicap; info@vzw-ithaka.be). Do not redo Ritmica/Dominiek Savio/Merlijn/Humival/Heder/Kindervriend stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **empty**; bruto **EUR{BRUTO}** JUMP +5.17%; pnl **EUR{PNL}** LOSS FLIP; equity **EUR{EQUITY}** DROP -3.92%; FTE **{FTE}**; neerlegging **{FILED}**. Strong KBO Actief. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+4); commitments (+1); leaderboard (+1 pi {PI}); entities (+1); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}.
- FOI: **ready not sent**. NOT every-10 (next **2330**). Next: {NEXT_RQ}.
"""
    )

print(f"OK tick{TICK} {ENTITY} bruto={BRUTO} pnl={PNL} pi={PI} next={NEXT_RQ}")
