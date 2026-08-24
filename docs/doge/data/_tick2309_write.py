# -*- coding: utf-8 -*-
"""Tick 2309: leftover dual Zewopa Lier YE2025 VAPH after Huis in de Stad."""
from __future__ import annotations

import csv
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2309")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TICK = "2309"
RQ = "rq_2309"
NEXT_RQ = "rq_2310"
ENTITY = "vzw_zewopa_lier"
KBO = "0421.896.748"
GAP = "gap_zewopa_nbb_pdf_assets_debt_neg_equity_1_21m_pnl_flip_bruto_drop_fte_drop_vaph_matrix_l5"
LB = "lb_zewopa_neg_equity_1_21m_pnl_flip_omzet_1_49m_bruto_drop_jr2025"
COMM = "comm_zewopa_jr2025_statutory_neg_equity_pnl_flip_vaph"

OMZET = 1492730
OMZET24 = 1466924
BRUTO = 1602575
BRUTO24 = 1871278
PNL = 67635
PNL24 = -100456
EQUITY = -1211742
EQUITY24 = -1278181
FTE = 21.0
FTE24 = 26.9
FILED = "30.06.2026"
EMAIL = "melding@zewopa.be"
RATIO = round(BRUTO / OMZET, 2)  # ~1.07

# cost 3.5 (~1.6m) · abs 7.8 (NEG equity -1.21m + pnl FLIP + FTE DROP under VAPH) · diff 3
# pi = 0.55*3.5 + 0.35*7.8 + 0.1*7 = 5.355 → 5.35
ABS, COST, DIFF, PI = 7.8, 3.5, 3.0, 5.35


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
        f"Zewopa YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl FLIP {PNL} "
        f"equity NEG {EQUITY} FTE DROP {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0421896748/zewopa\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421896748\n"
        "https://inclusiefwonen.com/\n"
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
        "source_id": "src_zewopa_jr2025_cw_en",
        "title": "Zewopa YE2025 CW EN (NEG equity -1.21m / pnl FLIP / omzet 1.49m)",
        "url": "https://www.companyweb.be/en/0421896748/zewopa",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW EN; omzet JUMP {OMZET} (+1.76%); bruto DROP {BRUTO} "
            f"(~{RATIO}x / -14.36%); pnl FLIP {PNL} vs YE2024 {PNL24}; equity NEG {EQUITY} "
            f"(improving +5.2% vs {EQUITY24}); FTE DROP {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_zewopa_jr2025_cw_nl",
        "title": "Zewopa YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0421896748/zewopa",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}; same euros",
    },
    {
        "source_id": "src_zewopa_jr2025_cw_fr",
        "title": "Zewopa YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0421896748/zewopa",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; "
            f"capitaux NEG {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_zewopa_kbo_0421896748",
        "title": "KBO Zewopa 0421.896.748 Actief VZW 6 VE NACE 87.304 Lier",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421896748",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-24",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 18.05.1981; 6 VE; "
            f"Florent Van Cauwenberghstraat 1 2500 Lier; RSZ 87.304; absorbed René Magritte + "
            f"Zelfstandig Wonen Provincie Antwerpen"
        ),
    },
    {
        "source_id": "src_zewopa_site_contact_2309",
        "title": "Zewopa FOI channel melding@zewopa.be / inclusiefwonen.com",
        "url": "https://inclusiefwonen.com/",
        "publisher": "Zewopa VZW",
        "accessed_date": "2026-08-24",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Florent Van Cauwenberghstraat 1 2500 Lier; T 03 443 20 90",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Zewopa VZW (Lier / VAPH inclusief wonen)",
    "name_fr": "Zewopa ASBL (Lier / habitat inclusif VAPH)",
    "name_en": "Zewopa VZW (Lier / VAPH inclusive housing for adults with motor disability)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://inclusiefwonen.com/",
    "foi_email": EMAIL,
    "foi_postal": "Florent Van Cauwenberghstraat 1, 2500 Lier",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 6 VE VZW "
        f"NACE 87.304; omzet JUMP {OMZET} bruto DROP {BRUTO} (~{RATIO}x) pnl FLIP {PNL} "
        f"equity NEG {EQUITY} FTE DROP {FTE}; neerlegging {FILED}; assets/debt Unknown; "
        f"FOI {GAP}; after Huis in de Stad@2308; AGB/FARO YE2024; not TE-additive of 348bn"
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
        "budget_id": "bud_zewopa_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025 primary envelope",
        "source_id": "src_zewopa_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET} JUMP +1.76% vs {OMZET24}",
    },
    {
        "budget_id": "bud_zewopa_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 (~{RATIO}x omzet)",
        "source_id": "src_zewopa_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} DROP -14.36% vs {BRUTO24}",
    },
    {
        "budget_id": "bud_zewopa_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 FLIP from LOSS",
        "source_id": "src_zewopa_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl FLIP {PNL} vs YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_zewopa_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025 NEGATIVE",
        "source_id": "src_zewopa_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity NEG {EQUITY} improving vs {EQUITY24}",
    },
    {
        "budget_id": "bud_zewopa_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025 DROP",
        "source_id": "src_zewopa_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE {FTE} DROP vs {FTE24}",
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
        "Zewopa YE2025 leftover dual (NEG equity -1.21m / pnl FLIP / omzet 1.49m / Medium)"
    ),
    "entity_id": ENTITY,
    "beneficiary": "adults with motor disability / inclusive housing Lier-Antwerpen",
    "legal_basis": f"VZW Zewopa (KBO {KBO}; Actief; 6 VE; NACE 87.304; VAPH path)",
    "decision_date": "2026-06-30",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(OMZET),
    "cash_by_year": (
        f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_omzet":{OMZET24},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},'
        f'"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
    ),
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0421896748/zewopa",
    "stated_goal": "Inclusive independent living for adults with physical disability (VAPH)",
    "cut_option": (
        "Publish NBB PDF assets/debt; disclose NEG equity -1.21m solvency path + pnl FLIP "
        "vs bruto DROP/FTE DROP under public VAPH funding"
    ),
    "source_id": "src_zewopa_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Lier>Zewopa>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; NEG equity primary absurdity; after Huis in de Stad@2308",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": "Zewopa NEG equity -1.21m / pnl FLIP / omzet 1.49m (YE2025)",
    "level": "L5",
    "type": "vaph_inclusive_housing_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Lier>Zewopa>JR2025",
    "annual_cost_eur": str(OMZET),
    "total_cost_eur": str(OMZET),
    "tco_notes": (
        f"CW omzet JUMP {OMZET} / bruto DROP {BRUTO} (~{RATIO}x) / pnl FLIP {PNL} from LOSS "
        f"{PNL24} / equity NEG {EQUITY} / FTE DROP {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_zewopa_jr2025_cw_en",
    "beneficiaries": "adults with motor disability Lier e.o.",
    "stated_goal": "VAPH inclusive housing / zelfstandig wonen",
    "measured_outcome": (
        f"NEG equity -1.21m multi-year; pnl FLIP; bruto DROP -14%; FTE DROP {FTE24}→{FTE}"
    ),
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": (
        "Publish NBB PDF assets/debt FOI; disclose NEG equity solvency + public funding path"
    ),
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after Huis in de Stad@2308; AGB/FARO YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Lier>Zewopa>NBB_PDF_assets_debt_neg_equity_pnl_flip",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why equity NEG EUR{EQUITY} multi-year under "
        f"VAPH path; pnl FLIP EUR{PNL} vs YE2024 LOSS EUR{PNL24}; bruto DROP vs FTE DROP recon"
    ),
    "why_it_matters": (
        f"Medium CW shows VAPH inclusive-housing VZW Lier with NEG equity -1.21m, pnl FLIP, "
        f"FTE DROP to 21 while omzet 1.49m; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Zewopa VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Florent Van Cauwenberghstraat 1, 2500 Lier",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Huis in de Stad@2308",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Zewopa (NBB PDF / NEG equity -1.21m / pnl FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Zewopa VZW — KBO **{KBO}** (Actief; Florent Van Cauwenberghstraat 1, 2500 Lier; **6 VE**; FTE {FTE}; NACE **87.304**)  
**recipient:** {EMAIL} · Florent Van Cauwenberghstraat 1, 2500 Lier (T 03 443 20 90)  
**sources:** [CW EN](https://www.companyweb.be/en/0421896748/zewopa) · [CW NL](https://www.companyweb.be/nl/0421896748/zewopa) · [CW FR](https://www.companyweb.be/fr/0421896748/zewopa) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421896748) · [site](https://inclusiefwonen.com/) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0421896748)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **Zewopa** sinds **18.05.1981**; **6 VE**; zetel Florent Van Cauwenberghstraat 1, 2500 Lier; RSZ NACE **87.304**.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +1.76%; bruto **EUR{BRUTO:,}** DROP −14.36%; pnl **EUR{PNL:,}** FLIP vs YE2024 LOSS; equity **NEG EUR{EQUITY:,}**; FTE **{FTE}** DROP; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024. After Huis in de Stad@2308. Do NOT redo Huis in de Stad/Katrinahof/Alvinnenberg/TM Kempen stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Zewopa VZW
via {EMAIL}
Florent Van Cauwenberghstraat 1, 2500 Lier
Betreft: Openbaarmaking jaarrekening 2025 Zewopa (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting negatief eigen vermogen EUR{EQUITY} (multi-jaar) onder VAPH-pad.
3. Toelichting pnl FLIP EUR{PNL} vs YE2024 verlies EUR{PNL24}.
4. Toelichting bruto DROP en FTE DROP {FTE24}→{FTE}.
5. Overzicht publieke toelagen/PVF/VAPH-stromen YE2025.

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
            "leftover dual — Zewopa YE2025 Medium "
            "(NEG equity -1.21m / pnl FLIP / omzet 1.49m / FTE DROP 21)"
        )
        r["notes"] = (
            f"tick{TICK} Zewopa {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET}; bruto DROP {BRUTO}; pnl FLIP {PNL}; equity NEG {EQUITY}; "
            f"FTE DROP {FTE}; 6 VE NACE 87.304 Lier; neerlegging {FILED}; FOI ready NOT sent; "
            f"after Huis in de Stad@2308; next EVERY-10 2310"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "EVERY-10 + leftover dual after Zewopa — prefer AGB/FARO-YE2025/"
                "AIESH/or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "EVERY-10 tick 2310 + leftover dual after Zewopa YE2025 Medium "
                "(NEG equity -1.21m / pnl FLIP / omzet 1.49m). "
                "Prefer AGB/FARO if YE2025 else FREE ETA-VAPH-WZC-maatwerk "
                "(Hejmen/Willekom/De Max/Domino WZC/Iris if YE2025 unused). "
                "Do NOT redo Zewopa/Huis in de Stad/Katrinahof/Alvinnenberg/TM Kempen/"
                "BC Sint-Elisabeth/Voluit/Kompas stack. Refresh progress+waste top10."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Zewopa; EVERY-10 due 2310; AGB/FARO YE2024"
            ),
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
            f"tick{TICK} leftover dual Zewopa {KBO} Medium "
            f"(omzet JUMP {OMZET}; bruto DROP {BRUTO}; pnl FLIP {PNL}; equity NEG {EQUITY}; "
            f"FTE DROP {FTE}; 6 VE Lier VAPH); after Huis in de Stad@2308; AGB/FARO YE2024; "
            f"next {NEXT_RQ}; next EVERY-10 2310; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Zewopa Lier (NEG equity -1.21m / pnl FLIP / omzet 1.49m / Medium)

- Unit: **{RQ}** leftover dual after **Huis in de Stad@2308**. Prefer NON-stall: AGB Bornem still **JR2024**; FARO still **YE2024**. Took unused FREE Flemish VAPH inclusive-housing **Zewopa VZW** YE2025 (KBO **{KBO}**; Florent Van Cauwenberghstraat 1 Lier; **Actief** **6 VE**; NACE **87.304**). Do not redo Huis in de Stad/Katrinahof/Alvinnenberg/TM Kempen stack.
- Found: Companyweb NL+EN YE2025 - omzet **EUR{OMZET}** JUMP +1.76%; bruto **EUR{BRUTO}** DROP -14.36%; pnl **EUR{PNL}** FLIP vs YE2024 LOSS EUR{PNL24}; equity **NEG EUR{EQUITY}**; FTE **{FTE}** DROP; neerlegging **{FILED}**. Strong KBO Actief 6 VE. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open (EVERY-10 due); loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next EVERY-10 is 2310** = next open). Next: {NEXT_RQ}.
"""
    )

print(
    f"OK tick{TICK} {ENTITY} omzet={OMZET} equity={EQUITY} pnl={PNL} pi={PI} next={NEXT_RQ}"
)
