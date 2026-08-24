# -*- coding: utf-8 -*-
"""Tick 2320 EVERY-10 + leftover dual: Heder Ekeren YE2025 VAPH."""
from __future__ import annotations

import csv
import json
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2320")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TICK = "2320"
RQ = "rq_2320"
NEXT_RQ = "rq_2321"
ENTITY = "vzw_heder_ekeren"
KBO = "0538.767.692"
GAP = "gap_heder_nbb_pdf_assets_debt_bruto_gt_omzet_17_59x_pnl_flip_fte_drop_vaph_matrix_l5"
LB = "lb_heder_bruto_32_69m_omzet_1_86m_17_59x_pnl_flip_jr2025"
COMM = "comm_heder_jr2025_statutory_bruto_gt_omzet_17_59x_pnl_flip_vaph"

OMZET = 1858609
OMZET24 = 1537768
BRUTO = 32694121
BRUTO24 = 31777356
PNL = 719053
PNL24 = -128406
EQUITY = 4170158
EQUITY24 = 3397072
FTE = 421.0
FTE24 = 439.1
FILED = "10.07.2026"
EMAIL = "info@heder.be"
RATIO = round(BRUTO / OMZET, 2)  # ~17.59
ABS, COST, DIFF, PI = 8.2, 5.5, 3.0, 6.6


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
        f"Heder YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl FLIP {PNL} "
        f"equity JUMP {EQUITY} FTE DROP {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0538767692/heder\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0538767692\n"
        "https://heder.be/contact/\n"
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
        "source_id": "src_heder_jr2025_cw_en",
        "title": f"Heder YE2025 CW EN (bruto 32.69m / omzet 1.86m ~{RATIO}x / pnl FLIP)",
        "url": "https://www.companyweb.be/en/0538767692/heder",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW EN; omzet JUMP {OMZET} (+20.86%); bruto JUMP {BRUTO} "
            f"(~{RATIO}x / +2.88%); pnl FLIP {PNL} vs YE2024 LOSS {PNL24}; equity JUMP {EQUITY} "
            f"(+22.76%); FTE DROP {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_heder_jr2025_cw_nl",
        "title": "Heder YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0538767692/heder",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}",
    },
    {
        "source_id": "src_heder_jr2025_cw_fr",
        "title": "Heder YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0538767692/heder",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; "
            f"capitaux {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_heder_kbo_0538767692",
        "title": "KBO Heder 0538.767.692 Actief VZW Ekeren NACE 87.201",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0538767692",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-24",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 17.09.2013; Herman Vosstraat 14 2180 Antwerpen; "
            f"VAPH residential minors mental disability"
        ),
    },
    {
        "source_id": "src_heder_site_contact_2320",
        "title": "Heder FOI channel info@heder.be",
        "url": "https://heder.be/contact/",
        "publisher": "Heder VZW",
        "accessed_date": "2026-08-24",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Herman Vosstraat 14 2180 Ekeren; T 03 541 33 80",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Heder VZW (Ekeren / VAPH)",
    "name_fr": "Heder ASBL (Ekeren / VAPH)",
    "name_en": "Heder VZW (Ekeren / VAPH residential care minors mental disability)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://heder.be/",
    "foi_email": EMAIL,
    "foi_postal": "Herman Vosstraat 14, 2180 Ekeren",
    "notes": (
        f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; omzet JUMP {OMZET} "
        f"bruto JUMP {BRUTO} (~{RATIO}x) pnl FLIP {PNL} equity JUMP {EQUITY} FTE DROP {FTE}; "
        f"neerlegging {FILED}; assets/debt Unknown; FOI {GAP}; after Kindervriend@2319; "
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
        "budget_id": "bud_heder_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 primary (~{RATIO}x omzet)",
        "source_id": "src_heder_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +2.88% vs {BRUTO24}",
    },
    {
        "budget_id": "bud_heder_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025",
        "source_id": "src_heder_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET} JUMP +20.86% vs {OMZET24}",
    },
    {
        "budget_id": "bud_heder_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 FLIP from LOSS",
        "source_id": "src_heder_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl FLIP {PNL} vs YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_heder_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025 JUMP",
        "source_id": "src_heder_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +22.76% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_heder_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025 DROP",
        "source_id": "src_heder_jr2025_cw_en",
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
        f"Heder YE2025 EVERY-10 dual (bruto 32.69m / omzet 1.86m ~{RATIO}x / pnl FLIP / Medium)"
    ),
    "entity_id": ENTITY,
    "beneficiary": "VAPH minors/youth mental disability Antwerpen-Ekeren campuses",
    "legal_basis": f"VZW Heder (KBO {KBO}; Actief; NACE 87.201; VAPH)",
    "decision_date": "2026-07-10",
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
    "evaluation_url": "https://www.companyweb.be/en/0538767692/heder",
    "stated_goal": "VAPH residential care minors with mental disability",
    "cut_option": (
        f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x + pnl FLIP vs FTE DROP"
    ),
    "source_id": "src_heder_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Ekeren>Heder>JR2025_statutory_L5",
    "notes": f"tick{TICK} EVERY-10; Medium CW; bruto primary {BRUTO} (~{RATIO}x); after Kindervriend@2319",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": f"Heder bruto 32.69m / omzet 1.86m ~{RATIO}x / pnl FLIP (YE2025)",
    "level": "L5",
    "type": "vaph_mpi_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Ekeren>Heder>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet JUMP {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x) / pnl FLIP {PNL} from LOSS "
        f"{PNL24} / equity JUMP {EQUITY} / FTE DROP {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_heder_jr2025_cw_en",
    "beneficiaries": "VAPH minors/youth Antwerpen-Ekeren",
    "stated_goal": "VAPH residential care",
    "measured_outcome": f"bruto÷omzet ~{RATIO}x; pnl FLIP; FTE DROP {FTE24}→{FTE}",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": (
        f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x + pnl FLIP vs FTE DROP"
    ),
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK} EVERY-10; Medium CW; FOI {GAP}; after Kindervriend@2319; AGB/FARO YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Ekeren>Heder>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_flip",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} "
        f"(~{RATIO}x) — VAPH/PVF matrix; pnl FLIP EUR{PNL} vs YE2024 LOSS EUR{PNL24}; FTE DROP"
    ),
    "why_it_matters": (
        f"Medium CW shows Antwerp VAPH VZW (bruto 32.69m / omzet 1.86m ~{RATIO}x / pnl FLIP / "
        f"FTE 421) under public care path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Heder VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Herman Vosstraat 14, 2180 Ekeren",
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
    "notes": f"tick{TICK} EVERY-10; ready NOT sent; Medium CW + Strong KBO; after Kindervriend@2319",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Heder (NBB PDF / bruto≫omzet ~{RATIO}x / pnl FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Heder VZW — KBO **{KBO}** (Actief; Herman Vosstraat 14, 2180 Ekeren; FTE {FTE}; NACE **87.201**; VAPH)  
**recipient:** {EMAIL} · Herman Vosstraat 14, 2180 Ekeren (T 03 541 33 80)  
**sources:** [CW EN](https://www.companyweb.be/en/0538767692/heder) · [CW NL](https://www.companyweb.be/nl/0538767692/heder) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0538767692) · [contact](https://heder.be/contact/)  
**tick:** {TICK}  
**confidence:** Medium

## Context
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +20.86%; bruto **EUR{BRUTO:,}** JUMP +2.88% (~**{RATIO}x**); pnl **EUR{PNL:,}** FLIP vs YE2024 LOSS; equity **EUR{EQUITY:,}** JUMP +22.76%; FTE **{FTE}** DROP; filed **{FILED}**.
- After Kindervriend@2319. Stalls AGB/FARO YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Heder VZW
via {EMAIL}
Herman Vosstraat 14, 2180 Ekeren
Betreft: Openbaarmaking jaarrekening 2025 Heder (KBO {KBO})

Geachte,
Op grond van openbaarheid van bestuur vraag ik:
1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — VAPH/PVF-matrix.
3. Toelichting pnl FLIP EUR{PNL} vs YE2024 verlies EUR{PNL24} en FTE DROP.
4. Overzicht publieke toelagen YE2025.
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
            f"EVERY-10 + leftover dual — Heder YE2025 Medium "
            f"(bruto JUMP 32.69m / ~{RATIO}x omzet / pnl FLIP / FTE DROP 421)"
        )
        r["notes"] = (
            f"tick{TICK} EVERY-10 + Heder {KBO} YE2025 Medium; omzet {OMZET}; bruto {BRUTO} ~{RATIO}x; "
            f"pnl FLIP {PNL}; equity JUMP {EQUITY}; FTE DROP {FTE}; FOI ready NOT sent; "
            f"progress+waste refreshed; after Kindervriend@2319; next EVERY-10 2330"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after Heder — prefer AGB/FARO-YE2025/"
                "AIESH/or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Heder YE2025 Medium "
                f"(bruto 32.69m / omzet 1.86m ~{RATIO}x / pnl FLIP). Prefer AGB/FARO if YE2025 "
                f"else FREE (Start West-Vlaanderen / De Plek / Manupal if YE2025). "
                f"Do NOT redo Heder/Kindervriend/Olo-Rotonde/Havenzate/Iris/Domino stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK} Heder EVERY-10; next EVERY-10 2330",
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
        try:
            cur = int(r.get("ticks_completed") or 0)
        except ValueError:
            cur = 0
        r["ticks_completed"] = str(max(cur, int(TICK)))
        r["paused"] = "no"
        r["notes"] = (
            f"tick{TICK} EVERY-10 + leftover dual Heder {KBO} Medium "
            f"(omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl FLIP {PNL}; "
            f"equity JUMP {EQUITY}; FTE DROP {FTE}); after Kindervriend@2319; AGB/FARO YE2024; "
            f"next {NEXT_RQ}; next EVERY-10 2330; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** refresh this file **and** append to `loop_log.md`.  
**Anchor:** ESA S.13 TE **€347.956 bn (2025)** = 100% public spend pie.  
**Rule:** no invented euros; never sum all `budgets.csv` rows.

---

## Snapshot at **tick {TICK}** ({UTC[:10]})

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2311-2320; AGB/FARO/AIESH YE2024 stalls; **Heder unlocked YE2025@{TICK}** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2311-2320 residual dual L5:** Willekom · M HKA · Hejmen · Iris · Havenzate · Olo-Rotonde · Schoonderhage · Homevil · Kindervriend · EVERY-10 **Heder bruto 32.69m / ~{RATIO}x / pnl FLIP / FTE 421** |
| **E. FOI-ready gaps** | **~1998** drafts ready | Human send only; answered ~11; partial ~28; total FOI ~2050 |

**Off-TE:** taxex · company cars · **VAPH/WZC/maatwerk dual shells NEW 2311-2320** (Heder · Kindervriend · Olo-Rotonde · Havenzate · …) · Metro3 · OWV snowball · Hedera CAP.

### Inventory (tick {TICK})

| File | Rows |
|------|-----:|
| budgets.csv | 53981+ |
| commitments.csv | 6049+ |
| leaderboard.csv | 8169+ |
| entities.csv | 2072+ |
| sources.csv | 6793+ |
| FOI ready | ~1998 |
| research_queue open | {NEXT_RQ} after Heder EVERY-10 |

### What improved since tick 2310

- Residual dual continuum through Kindervriend / Olo-Rotonde / Havenzate / Iris + EVERY-10 **Heder** (bruto **32.69m** / ~**{RATIO}x** / pnl FLIP / FTE **421**).
- Blocked still: AGB Bornem JR2025 · FARO/AIESH/Citeco/Groupe Foes/Gandae YE2024.
"""
with open(os.path.join(DATA, "progress_every_10_ticks.md"), "w", encoding="utf-8") as f:
    f.write(progress)

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **{TICK}** ({UTC[:10]}) · **8169+** leaderboard rows  
**Sort:** `priority_index` desc; stocks/corrupt pi>10 filtered off pure top10.  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`

---

## Top 10 (annual flow / TE-adjacent)

| # | ID | Name | Annual € | Abs | Cost | Diff | **Priority** |
|---|-----|------|--------:|----:|-----:|-----:|-------------:|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct 13.3bn | **13.27 bn** | 8 | 9.5 | 7 | **8.55** |
| 3 | `lb_fed_fossil_accises_10_5bn` | Fossil accise gaps 10.5bn | **10.54 bn** | 8 | 9.5 | 6 | **8.5** |
| 4 | `lb_company_cars_fpb` | Company cars TE FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** |
| 5 | `lb_exc_heatoil` | Heating gas oil excise preference | **1.84 bn** | 8 | 9.5 | 6 | **8.43** |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 SSC gap | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** |
| 8 | `lb_oaa_consol_reporte_300_6m` | OAA reporté solde +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** |
| 9 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** |
| 10 | `lb_dual_cars_ssc_taxex` | Dual company car SSC under-collection | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** |

**Stock filter off top10:** Metro3 · OWV snowball · **NEW residual 2311-2320:** **Heder bruto 32.69m ~{RATIO}x / pnl FLIP** (EVERY-10) · Kindervriend ~19.9x · Olo-Rotonde ~9.5x · Havenzate · Iris · Domino · Zewopa NEG equity.

### High-absurdity residual

- **Heder** EVERY-10 bruto **EUR32.69m** / ~**{RATIO}x** / pnl FLIP / FTE **421**.
- **Kindervriend** bruto **EUR8.08m** / ~**19.9x** / pnl LOSS.
- **Olo-Rotonde** bruto **EUR66.85m** / ~**9.5x** / FTE **855**.
"""
with open(os.path.join(DATA, "doge_waste_top10_current.md"), "w", encoding="utf-8") as f:
    f.write(waste)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} EVERY-10 + Heder Ekeren (bruto JUMP 32.69m / ~{RATIO}x omzet / pnl FLIP / Medium)

- **EVERY-10:** refreshed progress + waste top10.
- Unit: **{RQ}** finish **in_progress** claim Heder. Prefer NON-stall AGB/FARO **YE2024**. Took FREE VAPH **Heder VZW** YE2025 (KBO **{KBO}**; Herman Vosstraat 14 Ekeren; NACE **87.201**; FTE **421**). Do not redo Kindervriend/Olo-Rotonde/Havenzate/Iris/Domino stack.
- Found: CW NL+EN YE2025 - omzet **EUR{OMZET}** JUMP +20.86%; bruto **EUR{BRUTO}** JUMP +2.88% (~**{RATIO}x**); pnl **EUR{PNL}** FLIP vs YE2024 LOSS; equity **EUR{EQUITY}** JUMP +22.76%; FTE **{FTE}** DROP; neerlegging **{FILED}**. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1); foi + draft; {RQ}=done + {NEXT_RQ} open; EVERY-10 files.
- FOI: **ready not sent**. **EVERY-10 @{TICK}** (next **2330**). Next: {NEXT_RQ}.
"""
    )

print(f"OK tick{TICK} EVERY-10 {ENTITY} bruto={BRUTO} ratio={RATIO}x pnl={PNL} pi={PI} next={NEXT_RQ}")
