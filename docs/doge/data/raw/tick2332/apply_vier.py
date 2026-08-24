# -*- coding: utf-8 -*-
"""tick 2332 — De Vier Notelaars YE2025; atomic CSV apply + claim."""
from __future__ import annotations

import csv
import sys
import time
from pathlib import Path

csv.field_size_limit(sys.maxsize)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs/doge/data"
FOI = ROOT / "docs/doge/foi/drafts"
LOG = ROOT / "docs/doge/loop_log.md"

TICK = "2332"
RQ = "rq_2332"
RQ_NEXT = "rq_2333"
EID = "vzw_de_vier_notelaars_schoten"
KBO = "0424.064.895"
KBO_NUM = "0424064895"
OMZET = 500791
BRUTO = 2864452
PNL = -40024
EQUITY = 4060369
FTE = 32.9
OMZET24 = 480298
BRUTO24 = 2780033
PNL24 = 183071
EQUITY24 = 4145049
FTE24 = 32.9
RATIO = round(BRUTO / OMZET, 2)
FILED = "01.07.2026"
ADDR = "Wijtschotbaan 12, 2900 Schoten"
EMAIL = "onthaal@viernotelaars.be"
SITE = "https://www.viernotelaars.be"
GAP = "gap_vier_notelaars_nbb_pdf_assets_debt_bruto_gt_omzet_5_72x_pnl_loss_flip_vaph_matrix_l5"
UTC = "2026-08-24T13:45:00Z"
COST = 3.5
ABS = 6.5
DIFF = 3.0
PI = round(0.55 * COST + 0.35 * ABS + 0.10 * (10 - DIFF), 2)
SRC_EN = "src_vier_notelaars_jr2025_cw_en"
COMM = "comm_vier_notelaars_jr2025_statutory_bruto_gt_omzet_5_72x_pnl_loss_flip_vaph"
LB = "lb_vier_notelaars_bruto_2_86m_omzet_0_50m_5_72x_pnl_loss_flip_jr2025"


def read_csv(path: Path):
    for _ in range(40):
        try:
            with path.open(encoding="utf-8", newline="") as f:
                r = csv.DictReader(f)
                return list(r.fieldnames or []), list(r)
        except PermissionError:
            time.sleep(0.3)
    raise RuntimeError(f"read fail {path}")


def atomic_write(path: Path, fields, rows):
    tmp = path.with_suffix(path.suffix + ".__new__")
    bak = path.with_suffix(path.suffix + ".__bak__")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})
    for _ in range(50):
        try:
            if bak.exists():
                try:
                    bak.unlink()
                except OSError:
                    pass
            if path.exists():
                path.replace(bak)
            tmp.replace(path)
            try:
                if bak.exists():
                    bak.unlink()
            except OSError:
                pass
            return
        except PermissionError:
            time.sleep(0.4)
    raise RuntimeError(f"atomic fail {path}")


def upsert(path: Path, new_rows, id_key: str):
    fields, rows = read_csv(path)
    existing = {r.get(id_key) for r in rows}
    added = 0
    for nr in new_rows:
        if nr.get(id_key) in existing:
            # replace
            rows = [nr if r.get(id_key) == nr.get(id_key) else r for r in rows]
        else:
            rows.append(nr)
            added += 1
    atomic_write(path, fields, rows)
    return added


# claim rq_2332
fields, rq = read_csv(DATA / "research_queue.csv")
claimed = False
for r in rq:
    if r.get("task_id") == RQ:
        if r.get("status") == "done" and EID in (r.get("entity_id") or ""):
            print("ALREADY_DONE")
            sys.exit(0)
        if r.get("status") == "in_progress" and "Vier Notelaars" not in (r.get("notes") or "") and "vier" not in (
            r.get("notes") or ""
        ).lower():
            # another unit claimed — abort
            if "giels" in (r.get("notes") or "").lower() or "alma" in (r.get("notes") or "").lower():
                print("BLOCKED_OTHER_CLAIM", r.get("notes"))
                sys.exit(2)
        r["status"] = "in_progress"
        r["updated_utc"] = UTC
        r["notes"] = (r.get("notes") or "") + f"; CLAIM tick{TICK} Vier Notelaars {KBO}"
        claimed = True
        break
if not claimed:
    print("NO_RQ")
    sys.exit(3)
atomic_write(DATA / "research_queue.csv", fields, rq)
print("CLAIMED")

# sources
upsert(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_vier_notelaars_jr2025_cw_nl",
            "title": "Companyweb NL De Vier Notelaars YE2025",
            "url": f"https://www.companyweb.be/nl/{KBO_NUM}/de-vier-notelaars",
            "publisher": "Companyweb",
            "accessed_date": "2026-08-24",
            "source_class": "commercial_registry_mirror",
            "notes": f"tick{TICK}; Medium CW NL; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE} filed {FILED}",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN De Vier Notelaars YE2025",
            "url": f"https://www.companyweb.be/en/{KBO_NUM}/de-vier-notelaars",
            "publisher": "Companyweb",
            "accessed_date": "2026-08-24",
            "source_class": "commercial_registry_mirror",
            "notes": f"tick{TICK}; Medium CW EN; bruto~{RATIO}x omzet; pnl LOSS FLIP",
        },
        {
            "source_id": "src_vier_notelaars_jr2025_cw_fr",
            "title": "Companyweb FR De Vier Notelaars YE2025",
            "url": f"https://www.companyweb.be/fr/{KBO_NUM}/de-vier-notelaars",
            "publisher": "Companyweb",
            "accessed_date": "2026-08-24",
            "source_class": "commercial_registry_mirror",
            "notes": f"tick{TICK}; Medium CW FR cross-check",
        },
        {
            "source_id": "src_vier_notelaars_kbo",
            "title": f"KBO De Vier Notelaars {KBO}",
            "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_NUM}",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-24",
            "source_class": "official_register",
            "notes": f"tick{TICK}; Strong KBO Actief VZW; 1 VE; RSZ 87.202; {ADDR}; {EMAIL}",
        },
        {
            "source_id": "src_vier_notelaars_site_contact",
            "title": f"De Vier Notelaars FOI {EMAIL}",
            "url": SITE,
            "publisher": "De Vier Notelaars VZW",
            "accessed_date": "2026-08-24",
            "source_class": "foi_contact",
            "notes": f"tick{TICK}; {EMAIL}; {ADDR}",
        },
    ],
    "source_id",
)

upsert(
    DATA / "entities.csv",
    [
        {
            "entity_id": EID,
            "name_nl": "De Vier Notelaars VZW (Schoten / VAPH woonondersteuning)",
            "name_fr": "De Vier Notelaars ASBL (Schoten / hébergement VAPH)",
            "name_en": "De Vier Notelaars VZW (Schoten / VAPH residential care)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": SITE,
            "foi_email": EMAIL,
            "foi_postal": ADDR,
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE RSZ 87.202; omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE {FTE}; neerlegging {FILED}; FOI {GAP}; after DenBrand/Mivalti@2330; AGB/FARO YE2024; not TE-additive of 348bn",
        }
    ],
    "entity_id",
)

upsert(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_vier_notelaars_omzet_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet YE2025 JUMP +4.27%",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_vier_notelaars_bruto_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": f"CW statutory bruto YE2025 JUMP ~{RATIO}x omzet",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; primary L5 envelope; vs YE2024 {BRUTO24}",
        },
        {
            "budget_id": "bud_vier_notelaars_pnl_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory pnl YE2025 LOSS FLIP",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; vs YE2024 PROFIT {PNL24}",
        },
        {
            "budget_id": "bud_vier_notelaars_equity_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen YE2025 DROP",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity -2.04% vs {EQUITY24}",
        },
        {
            "budget_id": "bud_vier_notelaars_fte_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": "CW social-balance FTE 32.9 flat",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; FTE flat vs {FTE24}",
        },
    ],
    "budget_id",
)

upsert(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": f"Vier Notelaars YE2025 leftover dual (omzet 0.50m / bruto 2.86m ~{RATIO}x / pnl LOSS FLIP / Medium)",
            "entity_id": EID,
            "beneficiary": "volwassenen mentale handicap Schoten / VAPH",
            "legal_basis": f"VZW De Vier Notelaars (KBO {KBO}; Actief; 1 VE; RSZ 87.202; VAPH woon/dag)",
            "decision_date": "2026-07-01",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(BRUTO),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},'
                f'"2024_omzet":{OMZET24},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": f"https://www.companyweb.be/en/{KBO_NUM}/de-vier-notelaars",
            "stated_goal": "VAPH residential and day support mental disability Schoten",
            "cut_option": f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x + LOSS FLIP + VAPH/PVF matrix",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Schoten>Vier_Notelaars>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO} (~{RATIO}x); after DenBrand/Mivalti@2330; not TE-additive of 348bn",
        }
    ],
    "commitment_id",
)

upsert(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": f"Vier Notelaars bruto 2.86m / omzet 0.50m ~{RATIO}x / pnl LOSS FLIP (YE2025)",
            "level": "L5",
            "type": "vaph_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>Schoten>Vier_Notelaars>JR2025",
            "annual_cost_eur": str(BRUTO),
            "total_cost_eur": str(BRUTO),
            "tco_notes": f"CW omzet JUMP {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x) / pnl LOSS FLIP {PNL} / equity DROP {EQUITY} / FTE {FTE} / filed {FILED}",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "VAPH adults Schoten",
            "stated_goal": "VAPH woon- & dagondersteuning",
            "measured_outcome": f"bruto÷omzet ~{RATIO}x; pnl LOSS FLIP from PROFIT; FTE {FTE} flat",
            "absurdity_score": str(ABS),
            "cost_score": str(COST),
            "difficulty": str(DIFF),
            "priority_index": str(PI),
            "cut_proposal": f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x vs VAPH/PVF + LOSS FLIP",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after DenBrand/Mivalti@2330; AGB/FARO YE2024",
        }
    ],
    "item_id",
)

upsert(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Schoten>Vier_Notelaars>NBB_PDF_assets_debt_bruto_gt_omzet",
            "entity_id": EID,
            "what_is_missing": f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x); pnl LOSS FLIP EUR{PNL} vs PROFIT EUR{PNL24} — VAPH/PVF matrix",
            "why_it_matters": f"Medium CW shows VAPH care VZW Schoten (bruto 2.86m / omzet 0.50m ~{RATIO}x / pnl LOSS FLIP / FTE {FTE}) under public care path; assets/debt unpublished",
            "priority": "8",
            "recipient_body": "De Vier Notelaars VZW",
            "recipient_email": EMAIL,
            "recipient_postal": ADDR,
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
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after DenBrand/Mivalti@2330",
        }
    ],
    "gap_id",
)

# close RQ + spawn next
fields, rq = read_csv(DATA / "research_queue.csv")
for r in rq:
    if r.get("task_id") == RQ:
        r["status"] = "done"
        r["title"] = (
            f"leftover dual — Vier Notelaars YE2025 Medium (bruto JUMP 2.86m / ~{RATIO}x omzet / pnl LOSS FLIP / FTE {FTE})"
        )
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["notes"] = (
            f"tick{TICK}; CW Medium bruto {BRUTO} ~{RATIO}x; pnl LOSS FLIP {PNL}; FOI ready NOT sent; after DenBrand/Mivalti@2330"
        )
if not any(r.get("task_id") == RQ_NEXT for r in rq):
    rq.append(
        {
            "task_id": RQ_NEXT,
            "title": "leftover dual after Vier Notelaars — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "Prefer AGB Bornem/APB → FARO/AIESH if YE2025 → FREE ETA-VAPH-WZC-maatwerk (Gandae/Aralea/Manupal/Vlotter still YE2024). Do NOT redo Vier Notelaars/Mivalti/Den Brand/Pleegzorg/Tandem/Het Eepos/Zonnebeke stack. Next EVERY-10@2340.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK} Vier Notelaars; next EVERY-10 2340",
        }
    )
else:
    for r in rq:
        if r.get("task_id") == RQ_NEXT and r.get("status") == "open":
            r["updated_utc"] = UTC
            r["notes"] = (r.get("notes") or "") + f"; after Vier Notelaars@{TICK}"
atomic_write(DATA / "research_queue.csv", fields, rq)

# loop_state
atomic_write(
    DATA / "loop_state.csv",
    [
        "state_id",
        "mode",
        "current_sprint",
        "last_tick_utc",
        "last_unit_id",
        "ticks_completed",
        "paused",
        "notes",
    ],
    [
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": RQ,
            "ticks_completed": TICK,
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual Vier Notelaars {KBO} Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; "
                f"pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE {FTE}); after DenBrand/Mivalti@2330; AGB/FARO YE2024; "
                f"next {RQ_NEXT}; next EVERY-10 2340; continuous hole_fill"
            ),
        }
    ],
)

# FOI draft
FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — De Vier Notelaars Schoten (NBB PDF / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** De Vier Notelaars VZW — KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; 1 VE; RSZ **87.202**; VAPH woon/dag)  
**recipient:** {EMAIL} · {ADDR} (T 03 658 33 73)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_NUM}/de-vier-notelaars) · [CW NL](https://www.companyweb.be/nl/{KBO_NUM}/de-vier-notelaars) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_NUM}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium

## Context
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +4.27%; bruto **EUR{BRUTO:,}** JUMP +3.04% (~**{RATIO}x**); pnl **EUR{PNL:,}** LOSS FLIP (vs PROFIT EUR{PNL24:,}); equity **EUR{EQUITY:,}** DROP −2.04%; FTE **{FTE}**; filed **{FILED}**.
- After Den Brand/Mivalti@2330. Stalls AGB Bornem/FARO/AIESH still YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: De Vier Notelaars VZW
via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 De Vier Notelaars (KBO {KBO})

Geachte,
Op grond van openbaarheid van bestuur vraag ik:
1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — VAPH/PVF-matrix.
3. Toelichting pnl LOSS FLIP EUR{PNL} (vs winst YE2024 EUR{PNL24}).
4. Overzicht publieke toelagen YE2025.
5. Schulden LT/KT en liquide middelen YE2025.
Ref: {GAP}
Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent
""",
    encoding="utf-8",
)

entry = f"""
### {UTC} - tick {TICK} - {RQ} De Vier Notelaars Schoten (bruto JUMP 2.86m / ~{RATIO}x omzet / pnl LOSS FLIP / Medium)

- Unit: **{RQ}** leftover dual after **DenBrand/Mivalti@2330**. Prefer NON-stall: AGB Bornem still **JR2024**; FARO/AIESH still **YE2024**. Took unused FREE Flemish VAPH **De Vier Notelaars VZW** YE2025 (KBO **{KBO}**; {ADDR}; **Actief** **1 VE**; RSZ **87.202**; {EMAIL}). Do not redo Mivalti/Den Brand/Pleegzorg/Tandem/Het Eepos stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +4.27%; bruto **EUR{BRUTO}** JUMP +3.04% (~**{RATIO}x**); pnl **EUR{PNL}** LOSS FLIP (vs PROFIT {PNL24}); equity **EUR{EQUITY}** DROP -2.04%; FTE **{FTE}** flat; neerlegging **{FILED}**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}.
- FOI: **ready not sent**. NOT every-10 (last **2330**; next **2340**). Next: {RQ_NEXT}.
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(entry)

(DATA / "raw" / "tick2332" / "SUMMARY.txt").write_text(
    f"tick{TICK} Vier Notelaars {KBO} bruto {BRUTO} ~{RATIO}x omzet {OMZET} pnl LOSS FLIP {PNL} Medium PI {PI}\n",
    encoding="utf-8",
)

print(f"DONE {RQ} Vier Notelaars bruto {BRUTO} ~{RATIO}x PI {PI}")
