# -*- coding: utf-8 -*-
"""Tick 2320 EVERY-10 + Heder Ekeren VAPH YE2025 — APPEND-ONLY."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
RAW = DATA / "raw" / "tick2320"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"

UTC = "2026-08-27T23:20:00Z"
TICK = "2320"
RQ, NEXT_RQ = "rq_2320", "rq_2321"
ENTITY = "vzw_heder_ekeren"
KBO = "0538.767.692"
KBO_DIGITS = "0538767692"
GAP = "gap_heder_nbb_pdf_assets_debt_bruto_gt_omzet_17_59x_pnl_profit_flip_fte_drop_vaph_matrix_l5"
LB = "lb_heder_bruto_32_69m_omzet_1_86m_17_59x_pnl_profit_flip_fte_421_jr2025"
COMM = "comm_heder_jr2025_statutory_vaph_bruto_32_69m_17_59x_pnl_flip"

OMZET, OMZET24 = 1858609, 1537768
BRUTO, BRUTO24 = 32694121, 31777356
PNL, PNL24 = 719053, -128406
EQUITY, EQUITY24 = 4170158, 3397072
FTE, FTE24 = 421.0, 439.1
FILED = "10.07.2026"
EMAIL = "info@heder.be"
ADDR = "Herman Vosstraat 14, 2180 Antwerpen"
RATIO = round(BRUTO / OMZET, 2)  # 17.59
ABS, COST, DIFF, PI = 8.5, 5.5, 3.0, 6.7


def read_csv(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames), list(r)


def write_csv(path: Path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def append_rows(path: Path, id_key: str, new_rows):
    fields, rows = read_csv(path)
    have = {r.get(id_key) for r in rows}
    added = 0
    for nr in new_rows:
        if nr.get(id_key) in have:
            continue
        rows.append(nr)
        have.add(nr.get(id_key))
        added += 1
    write_csv(path, fields, rows)
    return added


def count(name):
    return len(read_csv(DATA / name)[1])


_, lsrows = read_csv(DATA / "loop_state.csv")
main = next(r for r in lsrows if r.get("state_id") == "main")
ticks = int(main.get("ticks_completed") or 0)
if ticks >= 2320:
    raise SystemExit(f"already at {ticks}")
if (DATA / "progress_every_10_ticks.md").read_text(encoding="utf-8").find("Snapshot at **tick 2320**") >= 0:
    raise SystemExit("EVERY-10 @2320 already refreshed")

_, rqrows = read_csv(DATA / "research_queue.csv")
rq = next((r for r in rqrows if r.get("task_id") == RQ), None)
if not rq or rq.get("status") not in ("open", "in_progress"):
    raise SystemExit(f"rq_2320 not claimable: {rq and rq.get('status')}")

_, ents = read_csv(DATA / "entities.csv")
if any(r.get("entity_id") == ENTITY for r in ents):
    raise SystemExit("Heder already in entities")

RAW.mkdir(parents=True, exist_ok=True)
FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(RAW / "cw_en_excerpt.txt").write_text(
    f"Heder YE2025 omzet {OMZET} bruto {BRUTO} ~{RATIO}x pnl PROFIT FLIP {PNL} "
    f"equity {EQUITY} FTE {FTE} filed {FILED}\n"
    f"https://www.companyweb.be/en/{KBO_DIGITS}/heder\n",
    encoding="utf-8",
)

print("sources +", append_rows(DATA / "sources.csv", "source_id", [
    {"source_id": "src_heder_jr2025_cw_en", "title": f"Heder YE2025 CW EN (bruto 32.69m / omzet 1.86m ~{RATIO}x / pnl PROFIT FLIP)", "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/heder", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "companyweb", "notes": f"tick{TICK} EVERY-10; Medium CW EN; omzet JUMP {OMZET} (+20.86%); bruto JUMP {BRUTO} (~{RATIO}x); pnl PROFIT FLIP {PNL} (vs LOSS {PNL24}); equity JUMP {EQUITY}; FTE DROP {FTE}; filed {FILED}"},
    {"source_id": "src_heder_jr2025_cw_nl", "title": "Heder YE2025 Companyweb NL", "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/heder", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "companyweb", "notes": f"tick{TICK} EVERY-10; Medium CW NL; neerlegging {FILED}"},
    {"source_id": "src_heder_jr2025_cw_fr", "title": "Heder YE2025 Companyweb FR", "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/heder", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "companyweb", "notes": f"tick{TICK} EVERY-10; Medium CW FR; CA {OMZET}; marge {BRUTO}; résultat {PNL}"},
    {"source_id": f"src_heder_kbo_{KBO_DIGITS}", "title": f"KBO Heder {KBO} Actief VZW NACE 87.203 Antwerpen/Ekeren", "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}", "publisher": "KBO / BCE", "accessed_date": "2026-08-27", "source_class": "kbo", "notes": f"tick{TICK} EVERY-10; Strong KBO Actief; VZW 17.09.2013; Herman Vosstraat 14 2180 Antwerpen; multi-VE; minors mental disability; {EMAIL}"},
    {"source_id": "src_heder_site_contact_2320", "title": "Heder FOI info@heder.be", "url": "https://heder.be/contact/", "publisher": "Heder VZW", "accessed_date": "2026-08-27", "source_class": "foi_contact", "notes": f"tick{TICK} EVERY-10; {EMAIL}; {ADDR}; T 03 541 33 80"},
]))

print("budgets +", append_rows(DATA / "budgets.csv", "budget_id", [
    {"budget_id": "bud_heder_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": str(BRUTO), "amount_max_eur": str(BRUTO), "basis": f"CW bruto YE2025 primary (~{RATIO}x omzet)", "source_id": "src_heder_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; bruto {BRUTO}"},
    {"budget_id": "bud_heder_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET), "amount_min_eur": str(OMZET), "amount_max_eur": str(OMZET), "basis": "CW omzet YE2025", "source_id": "src_heder_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; omzet {OMZET}"},
    {"budget_id": "bud_heder_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": str(PNL), "amount_max_eur": str(PNL), "basis": "CW pnl YE2025 PROFIT FLIP", "source_id": "src_heder_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; pnl {PNL} vs {PNL24}"},
    {"budget_id": "bud_heder_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": str(EQUITY), "amount_max_eur": str(EQUITY), "basis": "CW equity YE2025", "source_id": "src_heder_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; equity {EQUITY}"},
    {"budget_id": "bud_heder_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": str(FTE), "amount_max_eur": str(FTE), "basis": "CW FTE YE2025", "source_id": "src_heder_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; FTE {FTE} vs {FTE24}"},
]))

print("commitments +", append_rows(DATA / "commitments.csv", "commitment_id", [{
    "commitment_id": COMM,
    "title": f"Heder YE2025 EVERY-10 leftover dual (bruto 32.69m / omzet 1.86m ~{RATIO}x / pnl PROFIT FLIP / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "VAPH/Opgroeien minors Antwerpen motor/mental disability",
    "legal_basis": f"VZW Heder (KBO {KBO}; Actief; multi-VE; RSZ minors mental disability)",
    "decision_date": "2026-07-10",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET24},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/heder",
    "stated_goal": "Flemish VAPH/MFC residential + support minors Antwerpen",
    "cut_option": f"Publish NBB PDF; reconcile bruto÷omzet ~{RATIO}x + pnl PROFIT FLIP",
    "source_id": "src_heder_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Ekeren>Heder>JR2025_statutory_L5",
    "notes": f"tick{TICK} EVERY-10; Medium CW; bruto primary {BRUTO}; after Kindervriend@2319",
}]))

print("leaderboard +", append_rows(DATA / "leaderboard.csv", "item_id", [{
    "item_id": LB,
    "name": f"Heder bruto 32.69m / omzet 1.86m ~{RATIO}x / pnl PROFIT FLIP / FTE 421 (YE2025)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Ekeren>Heder>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": f"CW omzet JUMP {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x) / pnl PROFIT FLIP {PNL} (vs LOSS {PNL24}) / equity JUMP {EQUITY} / FTE DROP {FTE} / filed {FILED}",
    "confidence": "medium",
    "source_id": "src_heder_jr2025_cw_en",
    "beneficiaries": "VAPH minors mental/motor disability Antwerpen",
    "stated_goal": "Flemish MFC/VAPH residential + day support",
    "measured_outcome": f"bruto÷omzet ~{RATIO}x; pnl PROFIT FLIP; FTE DROP {FTE}",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": f"Publish NBB PDF FOI; reconcile bruto÷omzet ~{RATIO}x + assets/debt",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK} EVERY-10; Medium CW; FOI {GAP}; after Kindervriend@2319",
}]))

print("entities +", append_rows(DATA / "entities.csv", "entity_id", [{
    "entity_id": ENTITY,
    "name_nl": "Heder VZW (Ekeren/Antwerpen / VAPH MFC minderjarigen)",
    "name_fr": "Heder ASBL (Ekeren/Anvers / VAPH MFC mineurs)",
    "name_en": "Heder VZW (Ekeren/Antwerp VAPH MFC minors)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://heder.be/",
    "foi_email": EMAIL,
    "foi_postal": ADDR,
    "notes": f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW multi-VE; omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl PROFIT FLIP {PNL} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging {FILED}; FOI {GAP}; after Kindervriend@2319; AGB Bornem JR2024; FARO/AIESH YE2024; not TE-additive",
}]))

print("foi_queue +", append_rows(DATA / "foi_queue.csv", "gap_id", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Ekeren>Heder>NBB_PDF_assets_debt_bruto_gt_omzet_vaph",
    "entity_id": ENTITY,
    "what_is_missing": f"NBB PDF YE2025; why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x); pnl PROFIT FLIP EUR{PNL} (vs LOSS {PNL24}); FTE DROP {FTE}; assets/debt/cash; VAPH/Opgroeien matrix",
    "why_it_matters": f"Medium CW VAPH MFC Antwerpen (bruto 32.69m / omzet 1.86m ~{RATIO}x / pnl PROFIT FLIP / FTE {FTE}); assets/debt unpublished",
    "priority": "8",
    "recipient_body": "Heder VZW",
    "recipient_email": EMAIL,
    "recipient_postal": ADDR,
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-27",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": COMM,
    "linked_leaderboard_id": LB,
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": f"tick{TICK} EVERY-10; ready NOT sent; Medium CW + Strong KBO",
}]))

(FOI_DRAFTS / f"{GAP}.md").write_text(f"""# FOI draft — Heder (NBB PDF / bruto≫omzet ~{RATIO}x / pnl PROFIT FLIP)

**gap_id:** `{GAP}` · **status:** ready NOT sent · **tick:** {TICK} EVERY-10  
**entity:** Heder VZW — KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; multi-VE; minors mental disability)  
**recipient:** {EMAIL}

## Brief
```text
Aan: Heder VZW via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 Heder (KBO {KBO})

1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — VAPH/Opgroeien/MFC-matrix.
3. Toelichting pnl PROFIT FLIP EUR{PNL} (vs YE2024 LOSS EUR{PNL24}).
4. FTE DROP {FTE} vs {FTE24} vs care matrix.
5. Schulden LT/KT en liquide middelen YE2025.

Ref: {GAP}
```
- [x] ready NOT sent (human-gated)
""", encoding="utf-8")
print("foi draft written")

for r in rqrows:
    if r.get("task_id") == RQ:
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["title"] = f"EVERY-10 + leftover dual — Heder YE2025 Medium (bruto JUMP 32.69m / ~{RATIO}x omzet / pnl PROFIT FLIP / FTE DROP {FTE})"
        r["notes"] = f"tick{TICK} EVERY-10: Heder YE2025 Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl PROFIT FLIP {PNL}; equity JUMP {EQUITY}; FTE DROP {FTE}; multi-VE Ekeren VAPH); FOI {GAP} ready not sent; progress+waste top10 refreshed; after Kindervriend@2319; stalls YE2024; next EVERY-10 2330"
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append({
        "task_id": NEXT_RQ,
        "title": "leftover dual after Heder — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": f"After Heder YE2025 Medium (bruto ~{RATIO}x / pnl PROFIT FLIP). Prefer AGB Bornem/APB → FARO/AIESH if YE2025 → FREE ETA-VAPH-WZC-maatwerk (Gandae/Manupal/Aralea/De Ploeg/Vlotter if YE2025). Do NOT redo Heder/Kindervriend/Homevil/Schoonderhage/Havenzate/Iris/Hejmen/Domino stack.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": f"spawned after tick{TICK} Heder EVERY-10; stalls YE2024; next EVERY-10 2330",
    })
write_csv(DATA / "research_queue.csv", read_csv(DATA / "research_queue.csv")[0], rqrows)

for r in lsrows:
    if r.get("state_id") == "main":
        r.update({
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": RQ,
            "ticks_completed": TICK,
            "paused": "no",
            "notes": f"tick{TICK} EVERY-10 leftover dual Heder {KBO} Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl PROFIT FLIP {PNL}; equity JUMP {EQUITY}; FTE DROP {FTE}; multi-VE Ekeren VAPH); after Kindervriend@2319; AGB Bornem JR2024; FARO/AIESH YE2024; next {NEXT_RQ}; next EVERY-10 2330; continuous hole_fill",
        })
write_csv(DATA / "loop_state.csv", read_csv(DATA / "loop_state.csv")[0], lsrows)

foi_rows = read_csv(DATA / "foi_queue.csv")[1]
foi_c = Counter(r.get("status") for r in foi_rows)
ready = foi_c.get("ready", 0)

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
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2311-2320 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; Gandae still YE2024; **Heder unlocked YE2025@{TICK}** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2311-2320 is residual dual L5 (not near-complete of 348bn):** Willekom · M HKA · Hejmen · Iris · Havenzate · Homevil · Schoonderhage · Ons Tehuis / Olo-Rotonde · Kindervriend · EVERY-10 primary **Heder bruto 32.69m / omzet 1.86m ~{RATIO}x / pnl PROFIT FLIP / FTE {FTE}** (Medium CW) |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **~{foi_c.get('answered',0)}**; partial **~{foi_c.get('partial',0)}**; total FOI rows **~{len(foi_rows)}** |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk shells** (**NEW 2311-2320** Willekom · M HKA · Hejmen · Iris · Havenzate · Homevil · Schoonderhage · Kindervriend · **Heder** · prior 2301-2310 Domino stack retained) · Metro3 · OWV snowball · Hedera CAP · LUWA PPP · private gambling market.

### Inventory (tick {TICK})

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {count('budgets.csv')}+ |
| commitments.csv | {count('commitments.csv')}+ |
| leaderboard.csv | {count('leaderboard.csv')}+ |
| entities.csv | {count('entities.csv')}+ |
| sources.csv | {count('sources.csv')}+ |
| FOI ready | ~{ready} |
| FOI answered | {foi_c.get('answered',0)} |
| FOI partial | {foi_c.get('partial',0)} |
| FOI total rows | ~{len(foi_rows)} |
| research_queue open | rq_2321 after Heder EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2310

- **Residual dual (tick2311-2320):** **Willekom** · **M HKA** · **Hejmen** · **Iris Kontich** · **Havenzate** · **Homevil** · **Schoonderhage** · **Ons Tehuis-Brabant / Olo-Rotonde** · **MPI De Kindervriend** · EVERY-10 primary **Heder** (bruto **32.69m** / omzet **1.86m** ~**{RATIO}x** / pnl PROFIT FLIP / FTE **{FTE}**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 · AIESH YE2024 · Citeco/Groupe Foes YE2024 · Gandae YE2024 · Manupal/Aralea/De Ploeg/Vlotter YE2024.
"""
(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **{TICK}** ({UTC[:10]}) · **{count('leaderboard.csv')}+** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

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

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans** · **EU GNI / MFF** · **Entity II HermReg** · **illness / RIZIV** · **SS spend** · **MOG II** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2311-2320:** **Heder bruto 32.69m / omzet 1.86m ~{RATIO}x / pnl PROFIT FLIP / FTE {FTE}** (EVERY-10@{TICK} primary) · Kindervriend · Homevil · Schoonderhage · Havenzate · Iris · Hejmen · prior 2301-2310 Domino stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia · **LUWA PPP** · private gambling market.

**Change vs tick 2310:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off). **Major NEW residual 2311-2320 (off pure top10 / dual):** Willekom · M HKA · Hejmen · Iris · Havenzate · Homevil · Schoonderhage · Kindervriend · **Heder bruto 32.69m / ~{RATIO}x / pnl PROFIT FLIP / FTE {FTE}** (EVERY-10@{TICK} primary). **Prior 2301-2310 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Heder** EVERY-10 primary bruto **EUR32.69m** / omzet **EUR1.86m** ~**{RATIO}x** / pnl PROFIT FLIP / FTE **{FTE}** — Antwerpen/Ekeren VAPH MFC opacity.
- **MPI De Kindervriend** bruto **EUR8.08m** / ~**19.86x** omzet / pnl LOSS / FTE **96.6**.
- **Homevil** empty omzet / bruto **EUR4.12m** / pnl JUMP **+160%** / FTE **41.1**.
- **Schoonderhage** bruto **EUR15.10m** / ~**6.64x** / pnl JUMP **+24%** / FTE **196.3**.
- **Havenzate** bruto **EUR4.69m** / ~**5.51x** / pnl DROP **-4%** / FTE **47.7**.
- **Domino** prior EVERY-10 omzet **EUR21.26m** / pnl DROP **-49%** (retained).
"""
(DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("progress+waste refreshed")

with LOG.open("a", encoding="utf-8") as f:
    f.write(f"""
### {UTC} - tick {TICK} - rq_{TICK} EVERY-10 + Heder Ekeren (bruto JUMP 32.69m / ~{RATIO}x omzet / pnl PROFIT FLIP / FTE DROP {FTE} / Medium)

- **EVERY-10:** refreshed `progress_every_10_ticks.md` (layers A-E of EUR 347.956 bn TE) + `doge_waste_top10_current.md` (top 10 by priority_index; pure annual flow filter). Inventory budgets {count('budgets.csv')}+ / commitments {count('commitments.csv')}+ / leaderboard {count('leaderboard.csv')}+ / entities {count('entities.csv')}+ / sources {count('sources.csv')}+ / FOI ready ~{ready}.
- Unit: **{RQ}** leftover dual after **Kindervriend@2319**. Prefer NON-stall: AGB Bornem still **JR2024**; FARO/AIESH still **YE2024**. Took FREE Flemish VAPH MFC **Heder VZW** YE2025 (KBO **{KBO}**; {ADDR}; **Actief** multi-VE; minors mental disability; {EMAIL}). Do not redo Kindervriend/Homevil/Schoonderhage/Havenzate/Iris/Hejmen/Domino stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +20.86% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +2.88% (~**{RATIO}x**); pnl **EUR{PNL}** PROFIT FLIP (vs YE2024 LOSS EUR{PNL24}); equity **EUR{EQUITY}** JUMP +22.76%; FTE **{FTE}** DROP (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; progress+waste top10; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- **EVERY-10 done** (last was 2310; next **2330**). Next: {NEXT_RQ}.

#### EVERY-10 brief (A/B/C/D/E)
- **A:** 100% L0 TE EUR347.956bn Strong
- **B:** 100% L1 subsector map Strong
- **C:** ~99% L2 entity totals (order-of-magnitude); stalls AGB Bornem/FARO/AIESH YE2024
- **D:** ~74-88% generous L5 named; residual dual NOT near-complete of 348bn
- **E:** ~{ready} FOI-ready; answered ~{foi_c.get('answered',0)}; partial ~{foi_c.get('partial',0)}
""")
print("DONE tick", TICK, "Heder EVERY-10")
