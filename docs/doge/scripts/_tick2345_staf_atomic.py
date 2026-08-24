# -*- coding: utf-8 -*-
"""Atomic tick2345 Staf: write CSVs then commit+rebase+push in-process."""
from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"

TICK = 2345
UTC = "2026-08-24T19:30:00Z"
ENTITY = "vzw_staf_leuven"
GAP = "gap_staf_nbb_pdf_assets_debt_bruto_gt_omzet_68x_pnl_flip_vaph_dagcentrum_matrix_l5"
COMM = "comm_staf_jr2025_statutory_vaph_bruto_5_05m_68x_pnl_flip"
LB = "lb_staf_bruto_5_05m_gt_omzet_68x_pnl_flip_fte_61_jr2025"
OMZET, BRUTO, PNL, EQUITY, FTE = 74103, 5047619, 156705, 2593536, 61.4
RATIO = round(BRUTO / OMZET, 2)
FILED, KBO = "2026-07-14", "0431.333.660"
CW_EN = "https://www.companyweb.be/en/0431333660/staf"
CW_NL = "https://www.companyweb.be/nl/0431333660/staf"
CW_FR = "https://www.companyweb.be/fr/0431333660/staf"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431333660"
SITE, EMAIL = "https://www.wijzijnstaf.be", "info@wijzijnstaf.be"
ADDR = "Prins-Regentplein 13, 3010 Leuven"


def read_csv(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(path: Path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def sh(args: list[str], retries: int = 8) -> None:
    import time

    for i in range(retries):
        print("+", " ".join(args))
        try:
            subprocess.check_call(args, cwd=str(ROOT))
            return
        except subprocess.CalledProcessError as e:
            lock = ROOT / ".git" / "index.lock"
            if lock.exists() and i < retries - 1:
                try:
                    # only remove if no git process
                    r = subprocess.run(
                        ["powershell", "-NoProfile", "-Command", "Get-Process git -ErrorAction SilentlyContinue"],
                        cwd=str(ROOT),
                        capture_output=True,
                        text=True,
                    )
                    if not (r.stdout or "").strip():
                        lock.unlink(missing_ok=True)
                        print("removed stale index.lock")
                except OSError:
                    pass
                time.sleep(0.4 * (i + 1))
                continue
            raise e


def write_unit() -> str:
    budgets_txt = (DATA / "budgets.csv").read_text(encoding="utf-8")
    if "bud_staf_" in budgets_txt or "vzw_staf_leuven" in budgets_txt:
        raise SystemExit("ABORT: Staf already present")

    q_fields, q_rows = read_csv(DATA / "research_queue.csv")
    target = None
    for r in q_rows:
        if r.get("task_id") == "rq_2345" and r.get("status", "").lower() in ("open", "in_progress"):
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
                f"leftover dual — Staf YE2025 Medium (bruto JUMP 5.05m / ~{RATIO}x omzet / "
                "pnl PROFIT FLIP / FTE 61.4)"
            ),
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": UTC,
            "instructions": (
                "After Blijdorp@2344. Prefer AGB/FARO YE2025 else FREE. "
                "Do NOT redo Blijdorp/Perrekes/Aurelia/Eyckerheyde/Konekt/OZC."
            ),
            "notes": (
                f"tick{TICK} Staf {KBO} YE2025 Medium; omzet {OMZET}; bruto {BRUTO} ~{RATIO}x; "
                f"pnl PROFIT FLIP {PNL}; equity {EQUITY}; FTE {FTE}; filed {FILED}; "
                f"FOI ready NOT sent; after Blijdorp@2344; next EVERY-10 2350"
            ),
        }
    )
    if next_id not in ids:
        q_rows.append(
            {
                "task_id": next_id,
                "title": "leftover dual after Staf — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "After Staf@2345. Prefer AGB/FARO if YE2025 else FREE. "
                    "Do NOT redo Staf/Blijdorp/Perrekes/Aurelia/Eyckerheyde/Konekt."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"spawned after tick{TICK} Staf; next EVERY-10 2350",
            }
        )
    write_csv(DATA / "research_queue.csv", q_fields, q_rows)

    s_fields, s_rows = read_csv(DATA / "sources.csv")
    s_rows += [
        {"source_id": "src_staf_jr2025_cw_nl", "title": "Companyweb NL Staf YE2025", "url": CW_NL, "publisher": "Companyweb (NBB-derived)", "accessed_date": "2026-08-24", "source_class": "secondary_aggregator", "notes": f"tick{TICK}; omzet {OMZET}; bruto {BRUTO}; pnl {PNL}; equity {EQUITY}; FTE {FTE}; filed {FILED}"},
        {"source_id": "src_staf_jr2025_cw_en", "title": "Companyweb EN Staf YE2025", "url": CW_EN, "publisher": "Companyweb (NBB-derived)", "accessed_date": "2026-08-24", "source_class": "secondary_aggregator", "notes": f"tick{TICK}; EN Medium"},
        {"source_id": "src_staf_jr2025_cw_fr", "title": "Companyweb FR Staf YE2025", "url": CW_FR, "publisher": "Companyweb (NBB-derived)", "accessed_date": "2026-08-24", "source_class": "secondary_aggregator", "notes": f"tick{TICK}; FR mirror"},
        {"source_id": f"src_staf_kbo_{TICK}", "title": f"KBO Staf {KBO}", "url": KBO_URL, "publisher": "KBO FOD Economie", "accessed_date": "2026-08-24", "source_class": "official_register", "notes": f"tick{TICK}; Strong KBO Actief 4 VE RSZ 88.106; {ADDR}; {EMAIL}"},
        {"source_id": f"src_staf_site_{TICK}", "title": f"Staf FOI {EMAIL}", "url": SITE, "publisher": "Staf VZW", "accessed_date": "2026-08-24", "source_class": "foi_contact", "notes": f"tick{TICK}; {EMAIL}"},
    ]
    write_csv(DATA / "sources.csv", s_fields, s_rows)

    b_fields, b_rows = read_csv(DATA / "budgets.csv")
    b_rows += [
        {"budget_id": "bud_staf_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET), "amount_min_eur": str(OMZET), "amount_max_eur": str(OMZET), "basis": "CW statutory omzet YE2025 JUMP +33.22%", "source_id": "src_staf_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; +33.22% vs 55626"},
        {"budget_id": "bud_staf_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": str(BRUTO), "amount_max_eur": str(BRUTO), "basis": f"CW statutory bruto_marge YE2025 ~{RATIO}x omzet", "source_id": "src_staf_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; ~{RATIO}x omzet"},
        {"budget_id": "bud_staf_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": str(PNL), "amount_max_eur": str(PNL), "basis": "CW statutory winst/verlies YE2025 PROFIT FLIP", "source_id": "src_staf_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; FLIP vs -2708"},
        {"budget_id": "bud_staf_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": str(EQUITY), "amount_max_eur": str(EQUITY), "basis": "CW statutory eigen_vermogen YE2025 JUMP", "source_id": "src_staf_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; +6.43%"},
        {"budget_id": "bud_staf_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": str(FTE), "amount_max_eur": str(FTE), "basis": f"CW FTE {FTE}", "source_id": "src_staf_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; JUMP vs 58.7"},
    ]
    write_csv(DATA / "budgets.csv", b_fields, b_rows)

    e_fields, e_rows = read_csv(DATA / "entities.csv")
    e_rows.append({"entity_id": ENTITY, "name_nl": "Staf VZW (Leuven / VAPH dagcentrum mentale handicap)", "name_fr": "Staf ASBL (Louvain / centre de jour handicap mental)", "name_en": "Staf VZW (Leuven / day centre adults with mental disabilities)", "level": "parastatal", "parent_id": "sec_flanders", "community_language": "nl", "website": SITE, "foi_email": EMAIL, "foi_postal": ADDR, "notes": f"tick{TICK} YE2025 Medium CW + Strong KBO {KBO} Actief 4 VE RSZ 88.106; omzet {OMZET}; bruto {BRUTO} ~{RATIO}x; pnl FLIP {PNL}; FTE {FTE}; FOI {GAP}"})
    write_csv(DATA / "entities.csv", e_fields, e_rows)

    c_fields, c_rows = read_csv(DATA / "commitments.csv")
    cash = f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":55626,"2024_bruto":4595062,"2024_pnl":-2708,"2024_equity":2436832,"2024_fte":58.7}}'
    c_rows.append({"commitment_id": COMM, "title": f"Staf YE2025 leftover dual (omzet {OMZET} / bruto 5.05m ~{RATIO}x / pnl PROFIT FLIP / FTE 61.4 / Medium)", "entity_id": ENTITY, "beneficiary": "volwassenen met mentale handicap Leuven / VAPH dagcentrum", "legal_basis": f"VZW Staf (KBO {KBO}; Actief; 4 VE; RSZ 88.106)", "decision_date": FILED, "start_year": "2025", "end_year": "2025", "total_envelope_eur": str(BRUTO), "cash_by_year": cash, "remaining_eur": "0", "status": "active", "evaluation_url": CW_EN, "stated_goal": "Day centres adults with mental disabilities / outpatient", "cut_option": "Publish NBB PDF assets/debt; explain bruto>>omzet ~68x; VAPH subsidy matrix", "source_id": "src_staf_jr2025_cw_en", "confidence": "medium", "hierarchy_path": "Vlaanderen>VlaamsBrabant>Leuven>Staf_VAPH_dagcentrum>JR2025_statutory_L5", "notes": f"tick{TICK}; Medium CW; not TE-additive"})
    write_csv(DATA / "commitments.csv", c_fields, c_rows)

    lb_fields, lb_rows = read_csv(DATA / "leaderboard.csv")
    lb_rows.append({"item_id": LB, "name": f"Staf bruto 5.05m / ~{RATIO}x omzet {OMZET} / pnl PROFIT FLIP / FTE 61.4 (YE2025 Leuven)", "level": "L5", "type": "vaph_dagcentrum_vzw_statutory", "hierarchy_path": "Vlaanderen>VlaamsBrabant>Leuven>Staf>JR2025", "annual_cost_eur": str(BRUTO), "total_cost_eur": str(BRUTO), "tco_notes": f"CW omzet {OMZET}; bruto {BRUTO} (~{RATIO}x); pnl PROFIT FLIP {PNL}; equity {EQUITY}; FTE {FTE}; filed {FILED}", "confidence": "medium", "source_id": "src_staf_jr2025_cw_en", "beneficiaries": "adults with mental disabilities Leuven day centres", "stated_goal": "VAPH day centres / outpatient mental disability", "measured_outcome": f"~{RATIO}x bruto/omzet; pnl FLIP; assets/debt Unknown", "absurdity_score": "8.5", "cost_score": "5.0", "difficulty": "3", "priority_index": "6.85", "cut_proposal": "FOI NBB PDF + bruto>>omzet path + VAPH/public subsidy matrix", "status": "active", "struck_reason": "", "notes": f"tick{TICK}; Medium CW + Strong KBO 4 VE"})
    write_csv(DATA / "leaderboard.csv", lb_fields, lb_rows)

    f_fields, f_rows = read_csv(DATA / "foi_queue.csv")
    f_rows.append({"gap_id": GAP, "hierarchy_path": "Vlaanderen>VlaamsBrabant>Leuven>Staf>NBB_PDF", "entity_id": ENTITY, "what_is_missing": f"NBB PDF YE2025 assets/debt/cash; why bruto {BRUTO} ~{RATIO}x omzet {OMZET}; pnl PROFIT FLIP {PNL}; VAPH/public subsidy matrix", "why_it_matters": f"Medium CW VAPH dagcentrum bruto~{RATIO}x omzet + profit flip; assets/debt unpublished", "priority": "8", "recipient_body": "Staf VZW", "recipient_email": EMAIL, "recipient_postal": ADDR, "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md", "status": "ready", "date_ready": "2026-08-24", "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "", "linked_commitment_id": COMM, "linked_leaderboard_id": LB, "created_utc": UTC, "updated_utc": UTC, "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO"})
    write_csv(DATA / "foi_queue.csv", f_fields, f_rows)

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    (FOI_DRAFTS / f"{GAP}.md").write_text(
        f"""# FOI draft — Staf Leuven (bruto 5.05m / ~{RATIO}x omzet / pnl PROFIT FLIP)

**gap_id:** `{GAP}` · **status:** ready NOT sent · **tick:** {TICK}  
**entity:** Staf VZW — KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; 4 VE; RSZ **88.106**)  
**recipient:** {EMAIL}

## Context
- CW YE2025: omzet **EUR{OMZET}**; bruto **EUR{BRUTO}** (~**{RATIO}x**); pnl **EUR{PNL}** PROFIT FLIP; equity **EUR{EQUITY}**; FTE **{FTE}**; filed **{FILED}**.
- After Blijdorp@2344. Stalls AGB/FARO YE2024.

## Brief
```text
Aan: Staf VZW via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 Staf (KBO {KBO})

1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — VAPH/PVF-matrix.
3. Toelichting pnl PROFIT FLIP EUR{PNL} (vs verlies YE2024).
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
            f"tick{TICK} leftover dual Staf {KBO} Medium (omzet {OMZET}; bruto {BRUTO} ~{RATIO}x; "
            f"pnl PROFIT FLIP {PNL}; equity {EQUITY}; FTE {FTE}; 4 VE RSZ 88.106); "
            f"after Blijdorp@2344; AGB/FARO YE2024; next {next_id}; next EVERY-10 2350"
        ),
    }
    write_csv(DATA / "loop_state.csv", ls_fields, ls_rows)

    with LOG.open("a", encoding="utf-8") as f:
        f.write(
            f"""
### {UTC} - tick {TICK} - {unit_id} Staf Leuven (bruto JUMP 5.05m / ~{RATIO}x omzet / pnl PROFIT FLIP / FTE {FTE} / Medium)

- Unit: **{unit_id}** leftover dual after Blijdorp@2344. Prefer NON-stall AGB/FARO YE2024. Took FREE VAPH dagcentrum **Staf VZW** YE2025 (KBO **{KBO}**; {ADDR}; 4 VE; RSZ 88.106; {EMAIL}).
- Found: CW NL+EN+FR — omzet **EUR{OMZET}**; bruto **EUR{BRUTO}** (~**{RATIO}x**); pnl **EUR{PNL}** PROFIT FLIP; equity **EUR{EQUITY}**; FTE **{FTE}**; filed **{FILED}**. Medium. Assets/debt Unknown.
- Wrote: sources(+5) budgets(+5) commitments(+1) leaderboard(+1 pi 6.85) entities(+1) foi+draft; {unit_id}=done + {next_id} open; ticks={TICK}.
- FOI: **ready not sent**. NOT every-10 (next **2350**). Next: {next_id}.
"""
        )

    raw = DATA / "raw" / f"tick{TICK}"
    raw.mkdir(parents=True, exist_ok=True)
    (raw / "summary.json").write_text(
        f'{{"tick":{TICK},"unit":"Staf","kbo":"{KBO}","omzet":{OMZET},"bruto":{BRUTO},"ratio":{RATIO},"pnl":{PNL},"fte":{FTE},"confidence":"medium","queue":"{unit_id}"}}\n',
        encoding="utf-8",
    )
    return unit_id


def main() -> None:
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
        "docs/doge/scripts/_tick2345_staf_atomic.py",
    ]
    sh(["git", "add", *paths])
    # verify staged has staf
    diff = subprocess.check_output(["git", "diff", "--cached", "--stat"], cwd=str(ROOT), text=True)
    if "budgets.csv" not in diff:
        raise SystemExit("ABORT: budgets not staged")
    sh(
        [
            "git",
            "commit",
            "-m",
            f"doge(loop): tick {TICK} — {unit_id} Staf bruto 5.05m ~68x omzet pnl PROFIT FLIP Medium",
        ]
    )
    # rebase onto remote then push (retry once)
    try:
        sh(["git", "pull", "--rebase", "origin", "main"])
    except subprocess.CalledProcessError:
        sh(["git", "rebase", "--abort"])
        raise SystemExit("ABORT: rebase failed")
    # re-check staf survived rebase
    if "bud_staf_" not in (DATA / "budgets.csv").read_text(encoding="utf-8"):
        raise SystemExit("ABORT: Staf lost during rebase")
    sh(["git", "push", "origin", "HEAD"])
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=str(ROOT), text=True).strip()
    print(f"PUSHED {sha} unit={unit_id} Staf bruto={BRUTO} ~{RATIO}x Medium")


if __name__ == "__main__":
    main()
