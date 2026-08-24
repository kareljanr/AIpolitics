# -*- coding: utf-8 -*-
"""Tick 2310 EVERY-10 + leftover dual: Domino Gent WZC YE2025."""
from __future__ import annotations

import csv
import os
from datetime import datetime, timezone

csv.field_size_limit(10**7)

ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2310")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TICK = "2310"
RQ = "rq_2310"
ENTITY = "vzw_domino_gent"
KBO = "0407.693.770"
GAP = "gap_domino_nbb_pdf_assets_debt_omzet_21_26m_pnl_drop_49pct_wzc_matrix_l5"
LB = "lb_domino_omzet_jump_21_26m_pnl_drop_49pct_equity_11_32m_jr2025"
COMM = "comm_domino_jr2025_statutory_wzc_omzet_pnl_drop"

OMZET = 21255348
OMZET24 = 20783221
BRUTO = 16636876
BRUTO24 = 16147984
PNL = 484409
PNL24 = 948500
EQUITY = 11317845
EQUITY24 = 11310247
FTE = 230.4
FTE24 = 229.7
FILED = "24.06.2026"
EMAIL = "info@dominovzw.be"
RATIO = round(BRUTO / OMZET, 2)  # ~0.78

# cost 5.5 (~21.3m) · abs 6.2 (pnl DROP -49% while omzet JUMP + WZC public path) · diff 3
# pi = 0.55*5.5 + 0.35*6.2 + 0.1*7 = 5.895 → 5.9
ABS, COST, DIFF, PI = 6.2, 5.5, 3.0, 5.9


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
        f"Domino Gent YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl DROP {PNL} "
        f"equity {EQUITY} FTE {FTE} filed {FILED}\n"
        "https://www.companyweb.be/en/0407693770/domino\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407693770\n"
        "https://dominovzw.be/contact\n"
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
        "source_id": "src_domino_jr2025_cw_en",
        "title": "Domino Gent YE2025 CW EN (omzet JUMP 21.26m / pnl DROP -49%)",
        "url": "https://www.companyweb.be/en/0407693770/domino",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW EN; omzet JUMP {OMZET} (+2.27%); bruto JUMP {BRUTO} "
            f"(~{RATIO}x / +3.03%); pnl DROP {PNL} (-48.93%); equity JUMP {EQUITY}; "
            f"FTE JUMP {FTE}; filed {FILED}"
        ),
    },
    {
        "source_id": "src_domino_jr2025_cw_nl",
        "title": "Domino Gent YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0407693770/domino",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": f"tick{TICK}; Medium CW NL; Laatste balansjaar 2025; neerlegging {FILED}; same euros",
    },
    {
        "source_id": "src_domino_jr2025_cw_fr",
        "title": "Domino Gent YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0407693770/domino",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-24",
        "source_class": "companyweb",
        "notes": (
            f"tick{TICK}; Medium CW FR; CA {OMZET}; marge brute {BRUTO}; résultat {PNL}; "
            f"capitaux {EQUITY}; personnel {FTE}"
        ),
    },
    {
        "source_id": "src_domino_kbo_0407693770",
        "title": "KBO Domino 0407.693.770 Actief VZW 6 VE NACE 87.301 Gent",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407693770",
        "publisher": "KBO / BCE",
        "accessed_date": "2026-08-24",
        "source_class": "kbo",
        "notes": (
            f"tick{TICK}; Strong KBO Actief; VZW sinds 19.06.1937; 6 VE; Tichelrei 3 9000 Gent; "
            f"RSZ/BTW 87.301 ROB; email {EMAIL}; www.dominovzw.be"
        ),
    },
    {
        "source_id": "src_domino_site_contact_2310",
        "title": "Domino FOI channel info@dominovzw.be",
        "url": "https://dominovzw.be/contact",
        "publisher": "Domino VZW",
        "accessed_date": "2026-08-24",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; {EMAIL}; Tichelrei 3 9000 Gent; T 09 235 42 95; WZC+assistentiewoningen",
    },
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(spath, sfields, srows)

epath = os.path.join(DATA, "entities.csv")
efields, erows = read_csv(epath)
ent = {
    "entity_id": ENTITY,
    "name_nl": "Domino VZW (Gent / WZC + assistentiewoningen)",
    "name_fr": "Domino ASBL (Gand / MRS + logements assistés)",
    "name_en": "Domino VZW (Ghent / nursing homes + assisted living)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://dominovzw.be/",
    "foi_email": EMAIL,
    "foi_postal": "Tichelrei 3, 9000 Gent",
    "notes": (
        f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 6 VE VZW "
        f"NACE 87.301; omzet JUMP {OMZET} (+2.27%) bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} "
        f"(-48.93%) equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging {FILED}; assets/debt Unknown; "
        f"FOI {GAP}; after Zewopa@2309; AGB/FARO YE2024; not TE-additive of 348bn"
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
        "budget_id": "bud_domino_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW statutory omzet YE2025 primary envelope (WZC)",
        "source_id": "src_domino_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; omzet {OMZET} JUMP +2.27% vs {OMZET24}",
    },
    {
        "budget_id": "bud_domino_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": f"CW statutory bruto YE2025 (~{RATIO}x omzet)",
        "source_id": "src_domino_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; bruto {BRUTO} JUMP +3.03% vs {BRUTO24}",
    },
    {
        "budget_id": "bud_domino_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW statutory pnl YE2025 DROP",
        "source_id": "src_domino_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; pnl {PNL} DROP -48.93% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_domino_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW statutory equity YE2025",
        "source_id": "src_domino_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick{TICK}; equity {EQUITY} JUMP +0.07% vs {EQUITY24}",
    },
    {
        "budget_id": "bud_domino_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW FTE YE2025",
        "source_id": "src_domino_jr2025_cw_en",
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
    "title": "Domino Gent YE2025 EVERY-10 dual (omzet JUMP 21.26m / pnl DROP -49% / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "WZC residents / assisted-living Gent Domino campuses",
    "legal_basis": f"VZW Domino (KBO {KBO}; Actief; 6 VE; NACE 87.301 ROB)",
    "decision_date": "2026-06-24",
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
    "evaluation_url": "https://www.companyweb.be/en/0407693770/domino",
    "stated_goal": "Elderly residential care / WZC + assisted living Gent",
    "cut_option": (
        "Publish NBB PDF assets/debt; disclose RIZIV/Vlaamse zorgkas/resident fee split; "
        "reconcile pnl DROP -49% vs omzet JUMP"
    ),
    "source_id": "src_domino_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>Domino>JR2025_statutory_L5",
    "notes": f"tick{TICK} EVERY-10; Medium CW; omzet primary {OMZET}; after Zewopa@2309",
}
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append(comm)
write_csv(cpath, cfields, crows)

lpath = os.path.join(DATA, "leaderboard.csv")
lfields, lrows = read_csv(lpath)
lb = {
    "item_id": LB,
    "name": "Domino omzet JUMP 21.26m / pnl DROP -49% / equity 11.32m (YE2025)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>Domino>JR2025",
    "annual_cost_eur": str(OMZET),
    "total_cost_eur": str(OMZET),
    "tco_notes": (
        f"CW omzet JUMP {OMZET} (+2.27%) / bruto JUMP {BRUTO} (~{RATIO}x) / "
        f"pnl DROP {PNL} (-48.93%) / equity {EQUITY} / FTE {FTE} / filed {FILED}"
    ),
    "confidence": "medium",
    "source_id": "src_domino_jr2025_cw_en",
    "beneficiaries": "WZC/assisted-living residents Gent",
    "stated_goal": "Elderly nursing-home and assisted living",
    "measured_outcome": f"omzet JUMP +2.27%; pnl DROP -49%; FTE {FTE}; public WZC fee opacity",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": (
        "Publish NBB PDF assets/debt FOI; disclose RIZIV/zorgkas/resident fee split; "
        "reconcile pnl DROP -49%"
    ),
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK} EVERY-10; Medium CW; FOI {GAP}; after Zewopa@2309; AGB/FARO YE2024",
}
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append(lb)
write_csv(lpath, lfields, lrows)

fpath = os.path.join(DATA, "foi_queue.csv")
ffields, frows = read_csv(fpath)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>Domino>NBB_PDF_assets_debt_omzet_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); RIZIV/Vlaamse zorgkas/resident fee split "
        f"inside omzet EUR{OMZET}; pnl DROP EUR{PNL} (-48.93%) vs YE2024 EUR{PNL24} recon"
    ),
    "why_it_matters": (
        f"Medium CW shows Gent WZC VZW (omzet 21.26m / pnl DROP -49% / FTE 230.4) "
        f"under public elderly-care path; assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Domino VZW",
    "recipient_email": EMAIL,
    "recipient_postal": "Tichelrei 3, 9000 Gent",
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
    "notes": f"tick{TICK} EVERY-10; ready NOT sent; Medium CW + Strong KBO; after Zewopa@2309",
}
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(foi)
write_csv(fpath, ffields, frows)

draft = f"""# FOI draft — Domino Gent (NBB PDF / omzet 21.26m / pnl DROP -49%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Domino VZW — KBO **{KBO}** (Actief; Tichelrei 3, 9000 Gent; **6 VE**; FTE {FTE}; NACE **87.301**)  
**recipient:** {EMAIL} · Tichelrei 3, 9000 Gent (T 09 235 42 95)  
**sources:** [CW EN](https://www.companyweb.be/en/0407693770/domino) · [CW NL](https://www.companyweb.be/nl/0407693770/domino) · [CW FR](https://www.companyweb.be/fr/0407693770/domino) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407693770) · [contact](https://dominovzw.be/contact) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0407693770)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **Domino** sinds **19.06.1937**; **6 VE**; zetel Tichelrei 3, 9000 Gent; RSZ NACE **87.301**; email {EMAIL}.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +2.27%; bruto **EUR{BRUTO:,}** JUMP +3.03%; pnl **EUR{PNL:,}** DROP −48.93%; equity **EUR{EQUITY:,}**; FTE **{FTE}**; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024. After Zewopa@2309. Do NOT redo Zewopa/Willekom/Huis in de Stad/Katrinahof stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Domino VZW
via {EMAIL}
Tichelrei 3, 9000 Gent
Betreft: Openbaarmaking jaarrekening 2025 Domino (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Uitsplitsing omzet EUR{OMZET}: RIZIV / Vlaamse zorgkas / residentiebijdragen / overig.
3. Toelichting pnl DROP EUR{PNL} (−48.93% vs YE2024 EUR{PNL24}).
4. Per-WZC / assistentiewoning split YE2025.
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
            "EVERY-10 + leftover dual — Domino Gent YE2025 Medium "
            "(omzet JUMP 21.26m / pnl DROP -49% / FTE 230.4)"
        )
        r["notes"] = (
            f"tick{TICK} EVERY-10 + Domino {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl DROP {PNL}; equity JUMP {EQUITY}; "
            f"FTE JUMP {FTE}; 6 VE NACE 87.301 Gent WZC; neerlegging {FILED}; "
            f"FOI ready NOT sent; progress+waste top10 refreshed; after Zewopa@2309; "
            f"next EVERY-10 2320"
        )
        break
# ensure next open exists (rq_2312 may already exist from Willekom race)
if not any(r.get("task_id") == "rq_2312" for r in rqrows):
    rqrows.append(
        {
            "task_id": "rq_2312",
            "title": (
                "leftover dual after Domino — prefer AGB/FARO-YE2025/"
                "AIESH/or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "leftover dual after Domino YE2025 Medium (omzet JUMP 21.26m / pnl DROP -49%). "
                "Prefer AGB/FARO if YE2025 else FREE ETA-VAPH-WZC-maatwerk "
                "(Hejmen/De Max if YE2025 unused). "
                "Do NOT redo Domino/Willekom/Zewopa/Huis in de Stad/Katrinahof stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK} Domino EVERY-10; next EVERY-10 2320",
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
        # keep higher if race advanced past 2310
        try:
            cur = int(r.get("ticks_completed") or 0)
        except ValueError:
            cur = 0
        r["ticks_completed"] = str(max(cur, int(TICK)))
        r["paused"] = "no"
        r["notes"] = (
            f"tick{TICK} EVERY-10 + leftover dual Domino {KBO} Medium "
            f"(omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl DROP {PNL} -48.93%; "
            f"equity JUMP {EQUITY}; FTE JUMP {FTE}; 6 VE Gent WZC); after Zewopa@2309; "
            f"AGB/FARO YE2024; next rq_2312; next EVERY-10 2320; continuous hole_fill"
        )
write_csv(lspath, lsfields, lsrows)

# EVERY-10 progress + waste top10
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
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2301-2310 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **Domino Gent unlocked YE2025@{TICK}** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2301-2310 is residual dual L5 (not near-complete of 348bn):** Havinet · TMMA · Voluit · BC Sint-Elisabeth · TM Kempen · Alvinnenberg · Katrinahof · Huis in de Stad · Zewopa · EVERY-10 primary **Domino omzet 21.26m / pnl DROP -49% / FTE 230.4** (Medium CW) |
| **E. FOI-ready gaps** | **~1988** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~2040** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk shells** (**NEW 2301-2310** Havinet · TMMA · Voluit · BC Sint-Elisabeth · TM Kempen · Alvinnenberg · Katrinahof · Huis in de Stad · Zewopa · **Domino**) · Metro3 · OWV snowball · Hedera · LUWA PPP · private gambling market.

### Inventory (tick {TICK})

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 53927+ |
| commitments.csv | 6039+ |
| leaderboard.csv | 8159+ |
| entities.csv | 2062+ |
| sources.csv | 6741+ |
| FOI ready | ~1988 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | ~2040 |
| research_queue open | rq_2312 after Domino EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2300

- **Residual dual (tick2301-2310):** **Havinet** · **TMMA** · **Voluit** · **BC Sint-Elisabeth** · **TM Kempen** · **Alvinnenberg** · **Katrinahof** · **Huis in de Stad** · **Zewopa** (NEG equity) · EVERY-10 primary **Domino** (omzet **21.26m** / pnl DROP **-49%** / FTE **230.4**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 · AIESH YE2024 · Citeco/Groupe Foes YE2024 · Gandae YE2024.
"""
with open(os.path.join(DATA, "progress_every_10_ticks.md"), "w", encoding="utf-8") as f:
    f.write(progress)

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **{TICK}** ({UTC[:10]}) · **8159+** leaderboard rows  
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

**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2301-2310:** **Domino omzet 21.26m / pnl DROP -49%** (EVERY-10@{TICK}) · Zewopa NEG equity · Katrinahof · Alvinnenberg · BC Sint-Elisabeth · Huis in de Stad · Voluit · TMMA/TM Kempen · Havinet · Willekom.

**Change vs tick 2300:** pure annual top10 **stable**. **Major NEW residual 2301-2310:** Domino EVERY-10 primary + Zewopa NEG equity + Katrinahof/Alvinnenberg/BC Sint-Elisabeth/Huis in de Stad/Voluit/Havinet/TMMA stack. Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Domino** EVERY-10 primary omzet **EUR21.26m** / pnl DROP **-49%** / FTE **230.4** — Gent WZC opacity.
- **Zewopa** NEG equity **−EUR1.21m** / pnl FLIP / omzet **1.49m**.
- **Katrinahof** bruto **EUR11.18m** / ~**10.5x** omzet / pnl DROP **-93%**.
- **BC Sint-Elisabeth** bruto **EUR26.44m** / ~**11.8x** omzet / pnl DROP **-70%**.
- **Alvinnenberg** bruto **EUR9.38m** / ~**8.4x** / pnl DROP **-97%**.
- **Huis in de Stad** bruto **EUR10.65m** / ~**7.8x** / pnl JUMP **+85%**.
"""
with open(os.path.join(DATA, "doge_waste_top10_current.md"), "w", encoding="utf-8") as f:
    f.write(waste)

with open(LOG, "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} EVERY-10 + Domino Gent (omzet JUMP 21.26m / pnl DROP -49% / Medium)

- **EVERY-10:** refreshed `progress_every_10_ticks.md` + `doge_waste_top10_current.md`. Inventory budgets 53927+ / commitments 6039+ / leaderboard 8159+ / entities 2062+ / sources 6741+ / FOI ready ~1988.
- Unit: **{RQ}** finish **in_progress** EVERY-10 claim (Domino Gent). Prefer NON-stall: AGB Bornem still **JR2024**; FARO still **YE2024**. Took claimed FREE Flemish WZC **Domino VZW** YE2025 (KBO **{KBO}**; Tichelrei 3 Gent; **Actief** **6 VE**; NACE **87.301**). Do not redo Zewopa/Willekom/Huis in de Stad/Katrinahof stack.
- Found: Companyweb NL+EN YE2025 - omzet **EUR{OMZET}** JUMP +2.27%; bruto **EUR{BRUTO}** JUMP +3.03%; pnl **EUR{PNL}** DROP -48.93%; equity **EUR{EQUITY}**; FTE **{FTE}**; neerlegging **{FILED}**. Strong KBO Actief 6 VE. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done; loop_state; raw docs/doge/data/raw/tick{TICK}/; EVERY-10 progress+waste.
- FOI: **ready not sent** (human-gated).
- **EVERY-10 @ {TICK}** (last was 2300; next **2320**). Next: rq_2312.
"""
    )

print(
    f"OK tick{TICK} EVERY-10 {ENTITY} omzet={OMZET} pnl={PNL} pi={PI} next=rq_2312"
)
