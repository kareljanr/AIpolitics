# -*- coding: utf-8 -*-
"""tick2347: close stuck Staf rq_2346 + land Leieborg YE2025 leftover dual; commit+push."""
from __future__ import annotations

import csv
import subprocess
import sys
import time
from pathlib import Path

csv.field_size_limit(sys.maxsize)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"

TICK = 2347
UTC = "2026-08-24T19:45:00Z"
ENTITY = "vzw_leieborg_deinze"
GAP = "gap_leieborg_nbb_pdf_assets_debt_bruto_gt_omzet_9_20x_pnl_jump_vaph_matrix_l5"
COMM = "comm_leieborg_jr2025_statutory_vaph_bruto_39_20m_9_20x_pnl_jump"
LB = "lb_leieborg_bruto_39_20m_gt_omzet_9_20x_pnl_jump_fte_469_jr2025"

OMZET, BRUTO, PNL, EQUITY, FTE = 4261838, 39202304, 1955277, 27357675, 468.6
RATIO = round(BRUTO / OMZET, 2)
FILED, KBO = "2026-06-24", "0418.832.835"
CW_EN = "https://www.companyweb.be/en/0418832835/leieborg"
CW_NL = "https://www.companyweb.be/nl/0418832835/leieborg"
CW_FR = "https://www.companyweb.be/fr/0418832835/leieborg"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418832835"
SITE, EMAIL = "https://www.leieborg.be", "info@leieborg.be"
ADDR = "Leernsesteenweg 53, 9800 Deinze"


def read_csv(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(path: Path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def sh(args: list[str], retries: int = 10) -> None:
    for i in range(retries):
        print("+", " ".join(args))
        try:
            subprocess.check_call(args, cwd=str(ROOT))
            return
        except subprocess.CalledProcessError:
            lock = ROOT / ".git" / "index.lock"
            if lock.exists() and i < retries - 1:
                r = subprocess.run(
                    ["powershell", "-NoProfile", "-Command",
                     "if (-not (Get-Process git -ErrorAction SilentlyContinue)) { 'free' } else { 'busy' }"],
                    cwd=str(ROOT), capture_output=True, text=True,
                )
                if "free" in (r.stdout or ""):
                    lock.unlink(missing_ok=True)
                    print("removed stale index.lock")
                time.sleep(0.35 * (i + 1))
                continue
            raise


def write_unit() -> str:
    bud = (DATA / "budgets.csv").read_text(encoding="utf-8")
    if "bud_leieborg_" in bud or "vzw_leieborg_deinze" in bud:
        raise SystemExit("ABORT: Leieborg already present")

    q_fields, q_rows = read_csv(DATA / "research_queue.csv")

    # close stuck Staf in_progress
    for r in q_rows:
        if r.get("task_id") == "rq_2346" and r.get("status", "").lower() == "in_progress":
            r["status"] = "done"
            r["updated_utc"] = UTC
            notes = r.get("notes") or ""
            if "tick2347 close" not in notes:
                r["notes"] = (notes + " | " if notes else "") + "tick2347 close stuck in_progress (CSVs already filled)"

    target = None
    for r in q_rows:
        if r.get("task_id") == "rq_2348" and r.get("status", "").lower() in ("open", "in_progress"):
            target = r
            break
    if target is None:
        for r in q_rows:
            if (
                r.get("status", "").lower() == "open"
                and (r.get("task_id") or "").startswith("rq_")
                and r.get("task_id") != "rq_116"
                and "leftover dual" in (r.get("title") or "").lower()
            ):
                target = r
                break
    if target is None:
        raise SystemExit("ABORT: no open leftover dual")

    unit_id = target["task_id"]
    next_n = int(unit_id.split("_")[1]) + 1
    next_id = f"rq_{next_n}"
    ids = {r.get("task_id") for r in q_rows}

    target.update(
        {
            "status": "done",
            "title": (
                f"leftover dual — Leieborg YE2025 Medium (bruto JUMP 39.20m / ~{RATIO}x omzet / "
                "pnl JUMP +121% / FTE 468.6)"
            ),
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": UTC,
            "instructions": (
                "After De Korenbloem@2346. Prefer AGB/FARO YE2025 else FREE. "
                "Do NOT redo Korenbloem/Staf/De Lier/De Ark/Perrekes."
            ),
            "notes": (
                f"tick{TICK} Leieborg {KBO} YE2025 Medium; omzet {OMZET}; bruto {BRUTO} ~{RATIO}x; "
                f"pnl JUMP {PNL}; equity {EQUITY}; FTE {FTE}; filed {FILED}; "
                f"FOI ready NOT sent; Aanbestedende 8 VE; next EVERY-10 2350"
            ),
        }
    )
    if next_id not in ids:
        q_rows.append(
            {
                "task_id": next_id,
                "title": "leftover dual after Leieborg — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "After Leieborg@2347. Prefer AGB/FARO if YE2025 else FREE. "
                    "Do NOT redo Leieborg/Korenbloem/Staf/De Lier/De Ark."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"spawned after tick{TICK} Leieborg; next EVERY-10 2350",
            }
        )
    write_csv(DATA / "research_queue.csv", q_fields, q_rows)

    s_fields, s_rows = read_csv(DATA / "sources.csv")
    s_rows += [
        {"source_id": "src_leieborg_jr2025_cw_nl", "title": "Companyweb NL Leieborg YE2025", "url": CW_NL, "publisher": "Companyweb (NBB-derived)", "accessed_date": "2026-08-24", "source_class": "secondary_aggregator", "notes": f"tick{TICK}; omzet {OMZET}; bruto {BRUTO}; pnl {PNL}; equity {EQUITY}; FTE {FTE}; filed {FILED}"},
        {"source_id": "src_leieborg_jr2025_cw_en", "title": "Companyweb EN Leieborg YE2025", "url": CW_EN, "publisher": "Companyweb (NBB-derived)", "accessed_date": "2026-08-24", "source_class": "secondary_aggregator", "notes": f"tick{TICK}; EN Medium"},
        {"source_id": "src_leieborg_jr2025_cw_fr", "title": "Companyweb FR Leieborg YE2025", "url": CW_FR, "publisher": "Companyweb (NBB-derived)", "accessed_date": "2026-08-24", "source_class": "secondary_aggregator", "notes": f"tick{TICK}; FR mirror"},
        {"source_id": f"src_leieborg_kbo_{TICK}", "title": f"KBO Leieborg {KBO}", "url": KBO_URL, "publisher": "KBO FOD Economie", "accessed_date": "2026-08-24", "source_class": "official_register", "notes": f"tick{TICK}; Strong KBO Actief 8 VE Aanbestedende RSZ 87.201; {ADDR}; {EMAIL}"},
        {"source_id": f"src_leieborg_site_{TICK}", "title": f"Leieborg FOI {EMAIL}", "url": SITE, "publisher": "Leieborg VZW", "accessed_date": "2026-08-24", "source_class": "foi_contact", "notes": f"tick{TICK}; {EMAIL}"},
    ]
    write_csv(DATA / "sources.csv", s_fields, s_rows)

    b_fields, b_rows = read_csv(DATA / "budgets.csv")
    b_rows += [
        {"budget_id": "bud_leieborg_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET), "amount_min_eur": str(OMZET), "amount_max_eur": str(OMZET), "basis": "CW statutory omzet YE2025 JUMP +10.31%", "source_id": "src_leieborg_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; +10.31% vs 3863394"},
        {"budget_id": "bud_leieborg_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": str(BRUTO), "amount_max_eur": str(BRUTO), "basis": f"CW statutory bruto_marge YE2025 ~{RATIO}x omzet", "source_id": "src_leieborg_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; +8.39% vs 36167501; ~{RATIO}x"},
        {"budget_id": "bud_leieborg_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": str(PNL), "amount_max_eur": str(PNL), "basis": "CW statutory winst/verlies YE2025 JUMP +121%", "source_id": "src_leieborg_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; JUMP vs 884034"},
        {"budget_id": "bud_leieborg_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": str(EQUITY), "amount_max_eur": str(EQUITY), "basis": "CW statutory eigen_vermogen YE2025 JUMP", "source_id": "src_leieborg_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; +6.72% vs 25634305"},
        {"budget_id": "bud_leieborg_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": str(FTE), "amount_max_eur": str(FTE), "basis": f"CW FTE {FTE}", "source_id": "src_leieborg_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; JUMP vs 453.9"},
    ]
    write_csv(DATA / "budgets.csv", b_fields, b_rows)

    e_fields, e_rows = read_csv(DATA / "entities.csv")
    e_rows.append({"entity_id": ENTITY, "name_nl": "Leieborg VZW (Deinze / VAPH woon minderjarigen mentale handicap)", "name_fr": "Leieborg ASBL (Deinze / hébergement mineurs handicap mental)", "name_en": "Leieborg VZW (Deinze / residential care minors with mental disability)", "level": "parastatal", "parent_id": "sec_flanders", "community_language": "nl", "website": SITE, "foi_email": EMAIL, "foi_postal": ADDR, "notes": f"tick{TICK} YE2025 Medium CW + Strong KBO {KBO} Actief 8 VE Aanbestedende RSZ 87.201; omzet {OMZET}; bruto {BRUTO} ~{RATIO}x; pnl JUMP {PNL}; FTE {FTE}; FOI {GAP}"})
    write_csv(DATA / "entities.csv", e_fields, e_rows)

    c_fields, c_rows = read_csv(DATA / "commitments.csv")
    cash = f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":3863394,"2024_bruto":36167501,"2024_pnl":884034,"2024_equity":25634305,"2024_fte":453.9}}'
    c_rows.append({"commitment_id": COMM, "title": f"Leieborg YE2025 leftover dual (omzet 4.26m / bruto 39.20m ~{RATIO}x / pnl JUMP +121% / FTE 468.6 / Medium)", "entity_id": ENTITY, "beneficiary": "minderjarigen met mentale handicap Deinze / VAPH woon", "legal_basis": f"VZW Leieborg (KBO {KBO}; Actief; 8 VE; Aanbestedende; RSZ 87.201)", "decision_date": FILED, "start_year": "2025", "end_year": "2025", "total_envelope_eur": str(BRUTO), "cash_by_year": cash, "remaining_eur": "0", "status": "active", "evaluation_url": CW_EN, "stated_goal": "Residential care minors with mental disability", "cut_option": "Publish NBB PDF assets/debt; explain bruto>>omzet ~9.2x; VAPH subsidy matrix", "source_id": "src_leieborg_jr2025_cw_en", "confidence": "medium", "hierarchy_path": "Vlaanderen>OostVlaanderen>Deinze>Leieborg_VAPH>JR2025_statutory_L5", "notes": f"tick{TICK}; Medium CW; not TE-additive"})
    write_csv(DATA / "commitments.csv", c_fields, c_rows)

    lb_fields, lb_rows = read_csv(DATA / "leaderboard.csv")
    lb_rows.append({"item_id": LB, "name": f"Leieborg bruto 39.20m / ~{RATIO}x omzet 4.26m / pnl JUMP +121% / FTE 468.6 (YE2025 Deinze)", "level": "L5", "type": "vaph_vzw_statutory", "hierarchy_path": "Vlaanderen>OostVlaanderen>Deinze>Leieborg>JR2025", "annual_cost_eur": str(BRUTO), "total_cost_eur": str(BRUTO), "tco_notes": f"CW omzet {OMZET}; bruto {BRUTO} (~{RATIO}x); pnl JUMP {PNL} (+121%); equity {EQUITY}; FTE {FTE}; filed {FILED}", "confidence": "medium", "source_id": "src_leieborg_jr2025_cw_en", "beneficiaries": "minors with mental disability Deinze residential", "stated_goal": "VAPH residential care minors mental disability", "measured_outcome": f"~{RATIO}x bruto/omzet; pnl JUMP; assets/debt Unknown", "absurdity_score": "7.5", "cost_score": "7.0", "difficulty": "3", "priority_index": "6.85", "cut_proposal": "FOI NBB PDF + bruto>>omzet path + VAPH/public subsidy matrix", "status": "active", "struck_reason": "", "notes": f"tick{TICK}; Medium CW + Strong KBO Aanbestedende 8 VE"})
    write_csv(DATA / "leaderboard.csv", lb_fields, lb_rows)

    f_fields, f_rows = read_csv(DATA / "foi_queue.csv")
    f_rows.append({"gap_id": GAP, "hierarchy_path": "Vlaanderen>OostVlaanderen>Deinze>Leieborg>NBB_PDF", "entity_id": ENTITY, "what_is_missing": f"NBB PDF YE2025 assets/debt/cash; why bruto {BRUTO} ~{RATIO}x omzet {OMZET}; pnl JUMP {PNL}; VAPH/public subsidy matrix", "why_it_matters": f"Medium CW VAPH woon bruto~{RATIO}x omzet + pnl JUMP; assets/debt unpublished; Aanbestedende", "priority": "8", "recipient_body": "Leieborg VZW", "recipient_email": EMAIL, "recipient_postal": ADDR, "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md", "status": "ready", "date_ready": "2026-08-24", "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "", "linked_commitment_id": COMM, "linked_leaderboard_id": LB, "created_utc": UTC, "updated_utc": UTC, "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO"})
    write_csv(DATA / "foi_queue.csv", f_fields, f_rows)

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    (FOI_DRAFTS / f"{GAP}.md").write_text(
        f"""# FOI draft — Leieborg Deinze (bruto 39.20m / ~{RATIO}x omzet / pnl JUMP +121%)

**gap_id:** `{GAP}` · **status:** ready NOT sent · **tick:** {TICK}  
**entity:** Leieborg VZW — KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; 8 VE Aanbestedende; RSZ **87.201**)  
**recipient:** {EMAIL}

## Context
- CW YE2025: omzet **EUR{OMZET}** JUMP +10.31%; bruto **EUR{BRUTO}** JUMP +8.39% (~**{RATIO}x**); pnl **EUR{PNL}** JUMP +121%; equity **EUR{EQUITY}**; FTE **{FTE}**; filed **{FILED}**.
- After De Korenbloem@2346. Closed stuck Staf rq_2346. Stalls AGB/FARO YE2024.

## Brief
```text
Aan: Leieborg VZW via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 Leieborg (KBO {KBO})

1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — VAPH/PVF-matrix.
3. Toelichting pnl JUMP EUR{PNL} (+121% vs YE2024).
4. Overzicht publieke toelagen YE2025 (+ YE2024) vs FTE {FTE}.
5. Schulden LT/KT en liquide middelen YE2025.

Ref: {GAP}
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )

    ls_fields, ls_rows = read_csv(DATA / "loop_state.csv")
    ls_rows[-1] = {
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": unit_id,
        "ticks_completed": str(TICK),
        "paused": "no",
        "notes": (
            f"tick{TICK} leftover dual Leieborg {KBO} Medium (omzet {OMZET}; bruto {BRUTO} ~{RATIO}x; "
            f"pnl JUMP {PNL}; equity {EQUITY}; FTE {FTE}; 8 VE Aanbestedende RSZ 87.201); "
            f"closed stuck Staf rq_2346; AGB/FARO YE2024; next {next_id}; next EVERY-10 2350"
        ),
    }
    write_csv(DATA / "loop_state.csv", ls_fields, ls_rows)

    with LOG.open("a", encoding="utf-8") as f:
        f.write(
            f"""
### {UTC} - tick {TICK} - {unit_id} Leieborg Deinze (bruto JUMP 39.20m / ~{RATIO}x omzet / pnl JUMP +121% / FTE {FTE} / Medium)

- Unit: **{unit_id}** leftover dual after De Korenbloem@2346 (also closed stuck **rq_2346 Staf in_progress**). Prefer NON-stall AGB/FARO YE2024. Took FREE VAPH **Leieborg VZW** YE2025 (KBO **{KBO}**; {ADDR}; 8 VE Aanbestedende; RSZ 87.201; {EMAIL}).
- Found: CW NL+EN — omzet **EUR{OMZET}**; bruto **EUR{BRUTO}** (~**{RATIO}x**); pnl **EUR{PNL}** JUMP +121%; equity **EUR{EQUITY}**; FTE **{FTE}**; filed **{FILED}**. Medium. Assets/debt Unknown.
- Wrote: sources(+5) budgets(+5) commitments(+1) leaderboard(+1 pi 6.85) entities(+1) foi+draft; closed rq_2346; {unit_id}=done + {next_id} open; ticks={TICK}.
- FOI: **ready not sent**. NOT every-10 (next **2350**). Next: {next_id}.
"""
        )

    raw = DATA / "raw" / f"tick{TICK}"
    raw.mkdir(parents=True, exist_ok=True)
    (raw / "summary.json").write_text(
        f'{{"tick":{TICK},"unit":"Leieborg","kbo":"{KBO}","omzet":{OMZET},"bruto":{BRUTO},"ratio":{RATIO},"pnl":{PNL},"fte":{FTE},"confidence":"medium","queue":"{unit_id}"}}\n',
        encoding="utf-8",
    )
    return unit_id


def main() -> None:
    sh(["git", "pull", "origin", "main"])
    unit_id = write_unit()
    paths = [
        "docs/doge/data/budgets.csv",
        "docs/doge/data/commitments.csv",
        "docs/doge/data/entities.csv",
        "docs/doge/data/foi_queue.csv",
        "docs/doge/data/leaderboard.csv",
        "docs/doge/data/loop_state.csv",
        "docs/doge/data/research_queue.csv",
        "docs/doge/data/sources.csv",
        "docs/doge/loop_log.md",
        f"docs/doge/foi/drafts/{GAP}.md",
        f"docs/doge/data/raw/tick{TICK}/",
        "docs/doge/scripts/_tick2347_leieborg_atomic.py",
    ]
    sh(["git", "add", *paths])
    sh(["git", "commit", "-m", f"doge(loop): tick {TICK} — {unit_id} Leieborg bruto 39.20m ~9.2x omzet pnl JUMP Medium"])
    try:
        sh(["git", "pull", "--rebase", "origin", "main"])
    except subprocess.CalledProcessError:
        subprocess.call(["git", "rebase", "--abort"], cwd=str(ROOT))
        raise SystemExit("ABORT: rebase failed")
    if "bud_leieborg_" not in (DATA / "budgets.csv").read_text(encoding="utf-8"):
        raise SystemExit("ABORT: Leieborg lost during rebase")
    sh(["git", "push", "origin", "HEAD"])
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=str(ROOT), text=True).strip()
    print(f"PUSHED {sha} unit={unit_id} Leieborg bruto={BRUTO} ~{RATIO}x Medium")


if __name__ == "__main__":
    main()
