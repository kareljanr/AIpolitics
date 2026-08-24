# -*- coding: utf-8 -*-
"""Tick 2330 EVERY-10 + leftover dual: fill Mivalti Tielt YE2025 (phantom CSV gap)."""
from __future__ import annotations

import csv
import json
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2330")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TICK = "2330"
RQ = "rq_2330"
NEXT_RQ = "rq_2331"
ENTITY = "vzw_mivalti_tielt"
KBO = "0416.406.548"
GAP = "gap_mivalti_nbb_pdf_assets_debt_bruto_gt_omzet_6_82x_pnl_jump_vaph_matrix_l5"
LB = "lb_mivalti_bruto_11_49m_omzet_1_68m_6_82x_pnl_jump_jr2025"
COMM = "comm_mivalti_jr2025_statutory_bruto_gt_omzet_6_82x_vaph"

OMZET = 1683253
OMZET24 = 1609944
BRUTO = 11487628
BRUTO24 = 10636440
PNL = 470626
PNL24 = 370928
EQUITY = 8134690
EQUITY24 = 7660758
FTE = 134.9
FTE24 = 133.1
FILED = "16.06.2026"
EMAIL = "info@mivalti.be"
RATIO = round(BRUTO / OMZET, 2)  # ~6.82

# cost 5.5 (~11.5m) · abs 6.0 (bruto~6.8x VAPH) · diff 3 → pi 5.8
ABS, COST, DIFF, PI = 6.0, 5.5, 3.0, 5.8


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
        f"Mivalti YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl JUMP {PNL} "
        f"equity JUMP {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0416406548/mivalti\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416406548\n"
        "https://mivalti.be/\n"
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
            "every_10": True,
        },
        f,
        indent=2,
    )
    f.write("\n")

spath = os.path.join(DATA, "sources.csv")
sfields, srows = read_csv(spath)
for ns in [
    {
        "source_id": "src_mivalti_jr2025_cw_en",
        "title": f"Mivalti YE2025 CW EN (bruto 11.49m / omzet 1.68m ~{RATIO}x)",
        "url": "https://www.companyweb.be/en/0416406548/mivalti",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW EN; omzet JUMP {OMZET} (+4.55%); bruto JUMP {BRUTO} "
            f"(~{RATIO}x / +8%); pnl JUMP {PNL} (+26.88%); equity JUMP {EQUITY}; "
            f"FTE {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_mivalti_jr2025_cw_nl",
        "title": "Mivalti YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0416406548/mivalti",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}",
    },
    {
        "source_id": "src_mivalti_jr2025_cw_fr",
        "title": "Mivalti YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0416406548/mivalti",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; "
            f"capitaux {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_mivalti_kbo_0416406548",
        "title": "KBO Mivalti 0416.406.548 Actief VZW Tielt 2 VE RSZ 87.202",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416406548",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-24",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 25.05.1976; Gruuthusestraat 36 8700 Tielt; "
            f"2 VE; RSZ 87.202 VAPH residential mental disability"
        ),
    },
    {
        "source_id": "src_mivalti_site_contact_2330",
        "title": "Mivalti FOI channel info@mivalti.be",
        "url": "https://mivalti.be/",
        "publisher": "Mivalti VZW",
        "accessed_date": "2026-08-24",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Gruuthusestraat 36 8700 Tielt; T 051 40 52 52",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Mivalti VZW (Tielt / VAPH woon- & dagondersteuning)",
    "name_fr": "Mivalti ASBL (Tielt / VAPH)",
    "name_en": "Mivalti VZW (Tielt / VAPH residential & day support)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://mivalti.be/",
    "foi_email": EMAIL,
    "foi_postal": "Gruuthusestraat 36, 8700 Tielt",
    "notes": (
        f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; omzet JUMP {OMZET} "
        f"bruto JUMP {BRUTO} (~{RATIO}x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE {FTE}; "
        f"neerlegging {FILED}; 2 VE; assets/debt Unknown on CW; FOI {GAP}; "
        f"fills prior phantom Mivalti commits; AGB/FARO YE2024; not TE-additive of 348bn"
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
        "budget_id": "bud_mivalti_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 primary (~{RATIO}x omzet)",
        "source_id": "src_mivalti_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +8% vs {BRUTO24}",
    },
    {
        "budget_id": "bud_mivalti_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025",
        "source_id": "src_mivalti_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET} JUMP +4.55% vs {OMZET24}",
    },
    {
        "budget_id": "bud_mivalti_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 JUMP",
        "source_id": "src_mivalti_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} JUMP +26.88% vs {PNL24}",
    },
    {
        "budget_id": "bud_mivalti_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025",
        "source_id": "src_mivalti_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +6.19% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_mivalti_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_mivalti_jr2025_cw_en",
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
    "title": f"Mivalti YE2025 EVERY-10 dual (bruto 11.49m / omzet 1.68m ~{RATIO}x / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "VAPH adults mental disability Tielt residential/day",
    "legal_basis": f"VZW Mivalti (KBO {KBO}; Actief; 2 VE; RSZ 87.202)",
    "decision_date": "2026-06-16",
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
    "evaluation_url": "https://www.companyweb.be/en/0416406548/mivalti",
    "stated_goal": "VAPH residential day individual support mental disability",
    "cut_option": f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x + VAPH/PVF matrix",
    "source_id": "src_mivalti_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Tielt>Mivalti>JR2025_statutory_L5",
    "notes": f"tick{TICK}; EVERY-10; Medium CW; bruto primary {BRUTO} (~{RATIO}x)",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": f"Mivalti bruto 11.49m / omzet 1.68m ~{RATIO}x / pnl JUMP (YE2025)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Tielt>Mivalti>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet JUMP {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x) / pnl JUMP {PNL} / "
        f"equity JUMP {EQUITY} / FTE {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_mivalti_jr2025_cw_en",
    "beneficiaries": "VAPH adults Tielt",
    "stated_goal": "VAPH woon- & dagondersteuning",
    "measured_outcome": f"bruto÷omzet ~{RATIO}x; FTE {FTE}; equity 8.13m; VAPH subsidy opacity",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x vs VAPH/PVF",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; EVERY-10; Medium CW; FOI {GAP}; AGB/FARO YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Tielt>Mivalti>NBB_PDF_assets_debt_bruto_gt_omzet",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} "
        f"(~{RATIO}x) — VAPH/PVF matrix; pnl JUMP EUR{PNL}"
    ),
    "why_it_matters": (
        f"Medium CW shows VAPH care VZW Tielt (bruto 11.49m / omzet 1.68m ~{RATIO}x / "
        f"FTE 134.9) under public care path; assets/debt unpublished on CW"
    ),
    "priority": "8",
    "recipient_body": "Mivalti VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Gruuthusestraat 36, 8700 Tielt",
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
    "notes": f"tick{TICK}; EVERY-10; ready NOT sent; Medium CW + Strong KBO",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Mivalti Tielt (NBB PDF / bruto≫omzet ~{RATIO}x)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Mivalti VZW — KBO **{KBO}** (Actief; Gruuthusestraat 36, 8700 Tielt; FTE {FTE}; 2 VE; RSZ **87.202**; VAPH)  
**recipient:** {EMAIL} · Gruuthusestraat 36, 8700 Tielt (T 051 40 52 52)  
**sources:** [CW EN](https://www.companyweb.be/en/0416406548/mivalti) · [CW NL](https://www.companyweb.be/nl/0416406548/mivalti) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416406548) · [site](https://mivalti.be/)  
**tick:** {TICK} (EVERY-10)  
**confidence:** Medium

## Context
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +4.55%; bruto **EUR{BRUTO:,}** JUMP +8% (~**{RATIO}x**); pnl **EUR{PNL:,}** JUMP +26.88%; equity **EUR{EQUITY:,}**; FTE **{FTE}**; filed **{FILED}**.
- EVERY-10@2330. Stalls AGB Bornem/FARO/AIESH still YE2024. Prior Mivalti commits left CSV gap — filled this tick.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Mivalti VZW
via {EMAIL}
Gruuthusestraat 36, 8700 Tielt
Betreft: Openbaarmaking jaarrekening 2025 Mivalti (KBO {KBO})

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
        r["priority"] = "10"
        r["title"] = (
            f"EVERY-10 + leftover dual — Mivalti YE2025 Medium "
            f"(bruto JUMP 11.49m / ~{RATIO}x omzet / pnl JUMP / FTE 134.9)"
        )
        r["notes"] = (
            f"tick{TICK} EVERY-10 Mivalti {KBO} YE2025 Medium; omzet {OMZET}; bruto {BRUTO} "
            f"~{RATIO}x; pnl {PNL}; equity {EQUITY}; FTE {FTE}; FOI ready NOT sent; "
            f"CSV fill after phantom commits; next EVERY-10 2340"
        )
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual after Mivalti EVERY-10 — prefer AGB/FARO-YE2025/"
                "AIESH/or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"After Mivalti YE2025 Medium (bruto 11.49m / omzet 1.68m ~{RATIO}x). "
                "Prefer AGB Bornem/APB → FARO/AIESH/REW if YE2025 → unused DSO/water/nuclear/"
                "IGS/HVZ (optional FREE: Den Brand/Gandae/Aralea/Manupal/Vlotter/De Ploeg "
                "if YE2025). Do NOT redo Mivalti/Tandem/Het Eepos/Pleegzorg/Zonnebeke/"
                "Ithaka/Schoonderhage/Kindervriend stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK} EVERY-10; next EVERY-10 2340",
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
            f"tick{TICK} EVERY-10 leftover dual Mivalti {KBO} Medium "
            f"(omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL}; "
            f"equity JUMP {EQUITY}; FTE {FTE}); AGB/FARO YE2024; "
            f"next {NEXT_RQ}; next EVERY-10 2340; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

inv = {}
for fn, key in [
    ("budgets.csv", "budgets"),
    ("commitments.csv", "commitments"),
    ("leaderboard.csv", "leaderboard"),
    ("entities.csv", "entities"),
    ("sources.csv", "sources"),
    ("foi_queue.csv", "foi"),
]:
    _, rows = read_csv(os.path.join(DATA, fn))
    inv[key] = len(rows)
foi_ready = sum(1 for r in read_csv(os.path.join(DATA, "foi_queue.csv"))[1] if r.get("status") == "ready")

progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick {TICK}** ({UTC[:10]})

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2321-2330 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **Mivalti unlocked YE2025@{TICK}** (CSV fill after phantom commits) |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2321-2330 is residual dual L5 (not near-complete of 348bn):** Heder · Humival · Merlijn · Dominiek Savio · L'entre D'eux · Ritmica · Ithaka · Zonnebeke · Het Eepos · Tandem · Pleegzorg · EVERY-10 primary **Mivalti bruto 11.49m / ~{RATIO}x omzet / FTE 134.9** (Medium CW) |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~{inv['foi']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk shells** (**NEW 2321-2330** Heder · Humival · Merlijn · Savio · Ritmica · Ithaka · Zonnebeke · Eepos · Tandem · Pleegzorg · **Mivalti**) · Metro3 · OWV snowball · Hedera · LUWA PPP · private gambling market.

### Inventory (tick {TICK})

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {inv['budgets']}+ |
| commitments.csv | {inv['commitments']}+ |
| leaderboard.csv | {inv['leaderboard']}+ |
| entities.csv | {inv['entities']}+ |
| sources.csv | {inv['sources']}+ |
| FOI ready | ~{foi_ready} |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | ~{inv['foi']} |
| research_queue open | {NEXT_RQ} after Mivalti EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2320

- **Residual dual (tick2321-2330):** **Heder** · **Humival** · **Merlijn** (~24x) · **Dominiek Savio** · **L'entre D'eux** · **Ritmica** · **Ithaka** · **Zonnebeke** · **Het Eepos** · **Tandem** · **Pleegzorg** · EVERY-10 primary **Mivalti** (bruto **11.49m** / ~**{RATIO}x** / FTE **134.9**; Medium CW; FOI ready; CSV fill).
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 · AIESH YE2024 · REW YE2024 · Gandae/Aralea/Manupal/Vlotter YE2024.
"""
with open(os.path.join(DATA, "progress_every_10_ticks.md"), "w", encoding="utf-8") as f:
    f.write(progress)

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **{TICK}** ({UTC[:10]}) · **{inv['leaderboard']}+** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 4 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 9 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |
| 10 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |

**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2321-2330:** **Mivalti bruto 11.49m / ~{RATIO}x** (EVERY-10@{TICK}) · Merlijn ~24x · Kindervriend · Tandem · Het Eepos · Dominiek Savio · Pleegzorg · Ritmica · Ithaka.

**Change vs tick 2320:** pure annual top10 **stable**. **Major NEW residual 2321-2330:** Mivalti EVERY-10 primary + Merlijn bruto≫omzet ~24x + Tandem/Eepos/Savio/Pleegzorg/Ritmica/Ithaka stack. Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Mivalti** EVERY-10 primary bruto **EUR11.49m** / ~**{RATIO}x** omzet / FTE **134.9** — Tielt VAPH opacity.
- **Merlijn** bruto **EUR3.68m** / ~**23.98x** omzet / FTE JUMP.
- **Kindervriend** bruto **EUR8.08m** / ~**19.86x** / pnl LOSS.
- **Tandem** bruto **EUR3.92m** / ~**6.33x** / pnl PROFIT FLIP.
- **Het Eepos** opbrengsten **EUR6.97m** / subsidies **EUR5.81m** (Strong BBC).
- **Dominiek Savio** bruto **EUR35.19m** / ~**7.08x** / pnl PROFIT FLIP.
"""
with open(os.path.join(DATA, "doge_waste_top10_current.md"), "w", encoding="utf-8") as f:
    f.write(waste)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} EVERY-10 + Mivalti Tielt (bruto JUMP 11.49m / ~{RATIO}x omzet / Medium)

- **EVERY-10:** refreshed `progress_every_10_ticks.md` + `doge_waste_top10_current.md`. Inventory budgets {inv['budgets']}+ / commitments {inv['commitments']}+ / leaderboard {inv['leaderboard']}+ / entities {inv['entities']}+ / sources {inv['sources']}+ / FOI ready ~{foi_ready}.
- Unit: **{RQ}** EVERY-10 + leftover dual. Prefer NON-stall: AGB Bornem still **JR2024**; FARO/AIESH still **YE2024**. Took preferred FREE Flemish VAPH **Mivalti VZW** YE2025 (KBO **{KBO}**; Gruuthusestraat 36 Tielt; **Actief** **2 VE**; RSZ **87.202**; info@mivalti.be) — CSV fill after prior phantom Mivalti commits. Do not redo Tandem/Het Eepos/Pleegzorg/Zonnebeke/Ithaka/Merlijn stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +4.55%; bruto **EUR{BRUTO}** JUMP +8% (~**{RATIO}x**); pnl **EUR{PNL}** JUMP +26.88%; equity **EUR{EQUITY}** JUMP +6.19%; FTE **{FTE}**; neerlegging **{FILED}**. Strong KBO Actief 2 VE. Assets/debt Unknown on CW. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/; EVERY-10 progress+waste.
- FOI: **ready not sent** (human-gated).
- **EVERY-10 @ {TICK}** (last was 2320; next **2340**). Next: {NEXT_RQ}.
"""
    )

print(f"OK tick{TICK} EVERY-10 {ENTITY} bruto={BRUTO} omzet={OMZET} ratio={RATIO}x pi={PI} next={NEXT_RQ}")
