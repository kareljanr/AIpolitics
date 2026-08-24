# -*- coding: utf-8 -*-
"""Atomic tick2352 MFC Combo: write CSVs + EVERY-10 skip + commit/rebase/push."""
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

TICK = 2352
UTC = "2026-08-24T20:15:00Z"
ENTITY = "vzw_mfc_combo_leuven"
GAP = "gap_mfc_combo_nbb_pdf_assets_debt_empty_omzet_bruto_4_46m_pnl_drop_75pct_vaph_mfc_matrix_l5"
COMM = "comm_mfc_combo_jr2025_statutory_empty_omzet_bruto_4_46m_pnl_drop"
LB = "lb_mfc_combo_empty_omzet_bruto_4_46m_pnl_drop_75pct_fte_54_jr2025"
OMZET = ""  # unpublished
BRUTO = 4461186
PNL = 37849
EQUITY = 2597315
FTE = 54.4
BRUTO24 = 4410405
PNL24 = 153514
EQUITY24 = 2599092
FTE24 = 54.6
FILED = "10.06.2026"
KBO = "0839.782.745"
CW_NL = "https://www.companyweb.be/nl/0839782745/mfc-combo"
CW_EN = "https://www.companyweb.be/en/0839782745/combo"
CW_FR = "https://www.companyweb.be/fr/0839782745/combo"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0839782745"
SITE = "https://www.mfccombo.be"
EMAIL = "info@mfccombo.be"
ADDR = "Parkstraat 185, 3000 Leuven"
# empty omzet + bruto 4.46m + pnl DROP 75%
COST, ABS, DIFF = 4.0, 6.5, 3.0
PI = round(0.55 * COST + 0.35 * ABS + 0.10 * (10 - DIFF), 2)


def read_csv(path: Path):
    for _ in range(30):
        try:
            with path.open(encoding="utf-8", newline="") as f:
                r = csv.DictReader(f)
                return list(r.fieldnames or []), list(r)
        except PermissionError:
            time.sleep(0.4)
    raise RuntimeError(f"read fail {path}")


def write_csv(path: Path, fieldnames, rows):
    tmp = path.with_suffix(".csv.__new__")
    bak = path.with_suffix(".csv.__bak__")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    for _ in range(40):
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
            time.sleep(0.5)
    raise RuntimeError(f"write fail {path}")


def sh(args: list[str], retries: int = 10) -> None:
    for i in range(retries):
        print("+", " ".join(args))
        try:
            subprocess.check_call(args, cwd=str(ROOT))
            return
        except subprocess.CalledProcessError as e:
            lock = ROOT / ".git" / "index.lock"
            if lock.exists() and i < retries - 1:
                try:
                    r = subprocess.run(
                        [
                            "powershell",
                            "-NoProfile",
                            "-Command",
                            "Get-Process git -ErrorAction SilentlyContinue",
                        ],
                        cwd=str(ROOT),
                        capture_output=True,
                        text=True,
                    )
                    if not (r.stdout or "").strip():
                        lock.unlink(missing_ok=True)
                        print("removed stale index.lock")
                except OSError:
                    pass
                time.sleep(0.5 * (i + 1))
                continue
            raise e


def write_unit() -> str:
    budgets_txt = (DATA / "budgets.csv").read_text(encoding="utf-8")
    if "bud_mfc_combo_" in budgets_txt or "vzw_mfc_combo_leuven" in budgets_txt:
        raise SystemExit("ABORT: MFC Combo already present")

    q_fields, q_rows = read_csv(DATA / "research_queue.csv")
    target = None
    for r in q_rows:
        if r.get("task_id") == "rq_2352" and r.get("status", "").lower() in (
            "open",
            "in_progress",
        ):
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
                "leftover dual — MFC Combo YE2025 Medium (empty omzet / bruto JUMP 4.46m / "
                "pnl DROP -75% / FTE 54.4)"
            ),
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": UTC,
            "instructions": (
                "After Korenbloem@2351. Prefer AGB/FARO YE2025 else FREE. "
                "Do NOT redo Korenbloem/Leieborg/Helan/Staf/De Lier/De Ark."
            ),
            "notes": (
                f"tick{TICK} MFC Combo {KBO} YE2025 Medium; empty omzet; bruto {BRUTO}; "
                f"pnl DROP {PNL} -75.34%; equity {EQUITY}; FTE {FTE}; filed {FILED}; "
                f"FOI ready NOT sent; after Korenbloem@2351; next EVERY-10 2360"
            ),
        }
    )
    if next_id not in ids:
        q_rows.append(
            {
                "task_id": next_id,
                "title": (
                    "leftover dual after MFC Combo — prefer AGB/FARO-YE2025/AIESH/"
                    "or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"After MFC Combo@{TICK}. Prefer AGB/FARO if YE2025 else FREE. "
                    "Do NOT redo Combo/Korenbloem/Leieborg/Helan/Staf."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"spawned after tick{TICK} MFC Combo; next EVERY-10 2360",
            }
        )
    write_csv(DATA / "research_queue.csv", q_fields, q_rows)

    s_fields, s_rows = read_csv(DATA / "sources.csv")
    s_rows += [
        {
            "source_id": "src_mfc_combo_jr2025_cw_nl",
            "title": "Companyweb NL MFC Combo YE2025",
            "url": CW_NL,
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-24",
            "source_class": "secondary_aggregator",
            "notes": (
                f"tick{TICK}; empty omzet; bruto {BRUTO}; pnl {PNL}; equity {EQUITY}; "
                f"FTE {FTE}; filed {FILED}"
            ),
        },
        {
            "source_id": "src_mfc_combo_jr2025_cw_en",
            "title": "Companyweb EN MFC Combo YE2025",
            "url": CW_EN,
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-24",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN Medium; Turnover unpublished; Gross margin {BRUTO}",
        },
        {
            "source_id": "src_mfc_combo_jr2025_cw_fr",
            "title": "Companyweb FR MFC Combo YE2025",
            "url": CW_FR,
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-24",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror",
        },
        {
            "source_id": f"src_mfc_combo_kbo_{TICK}",
            "title": f"KBO MFC Combo {KBO}",
            "url": KBO_URL,
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-24",
            "source_class": "official_register",
            "notes": (
                f"tick{TICK}; Strong KBO Actief 7 VE RSZ 87.991; {ADDR}; {EMAIL}"
            ),
        },
        {
            "source_id": f"src_mfc_combo_site_{TICK}",
            "title": f"MFC Combo FOI {EMAIL}",
            "url": f"{SITE}/contacteer-ons/",
            "publisher": "MFC Combo VZW",
            "accessed_date": "2026-08-24",
            "source_class": "foi_contact",
            "notes": f"tick{TICK}; {EMAIL}",
        },
    ]
    write_csv(DATA / "sources.csv", s_fields, s_rows)

    b_fields, b_rows = read_csv(DATA / "budgets.csv")
    b_rows += [
        {
            "budget_id": "bud_mfc_combo_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge YE2025 JUMP +1.15% (omzet empty)",
            "source_id": "src_mfc_combo_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; empty omzet; vs YE2024 {BRUTO24}",
        },
        {
            "budget_id": "bud_mfc_combo_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst/verlies YE2025 DROP -75.34%",
            "source_id": "src_mfc_combo_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; DROP vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_mfc_combo_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen YE2025 DROP -0.07%",
            "source_id": "src_mfc_combo_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_mfc_combo_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW FTE {FTE}",
            "source_id": "src_mfc_combo_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; vs YE2024 {FTE24}",
        },
    ]
    write_csv(DATA / "budgets.csv", b_fields, b_rows)

    e_fields, e_rows = read_csv(DATA / "entities.csv")
    e_rows.append(
        {
            "entity_id": ENTITY,
            "name_nl": "MFC Combo VZW (Leuven / multifunctioneel centrum jeugdhulp)",
            "name_fr": "MFC Combo ASBL (Louvain / centre multifonctionnel aide à la jeunesse)",
            "name_en": "MFC Combo VZW (Leuven / multifunctional youth-care centre)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": SITE,
            "foi_email": EMAIL,
            "foi_postal": ADDR,
            "notes": (
                f"tick{TICK} YE2025 Medium CW + Strong KBO {KBO} Actief 7 VE RSZ 87.991; "
                f"empty omzet; bruto {BRUTO}; pnl DROP {PNL}; FTE {FTE}; FOI {GAP}"
            ),
        }
    )
    write_csv(DATA / "entities.csv", e_fields, e_rows)

    c_fields, c_rows = read_csv(DATA / "commitments.csv")
    cash = (
        f'{{"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},'
        f'"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
    )
    c_rows.append(
        {
            "commitment_id": COMM,
            "title": (
                f"MFC Combo YE2025 leftover dual (empty omzet / bruto 4.46m / "
                f"pnl DROP -75% / FTE 54.4 / Medium)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "kinderen/jongeren Leuven MFC / integrale jeugdhulp",
            "legal_basis": f"VZW MFC Combo (KBO {KBO}; Actief; 7 VE; RSZ 87.991)",
            "decision_date": FILED,
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(BRUTO),
            "cash_by_year": cash,
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": CW_EN,
            "stated_goal": "Multifunctional centre / integral youth care with housing",
            "cut_option": (
                "Publish NBB PDF assets/debt; explain empty omzet vs bruto 4.46m; "
                "VAPH/jeugdhulp subsidy matrix; pnl DROP path"
            ),
            "source_id": "src_mfc_combo_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Leuven>MFC_Combo>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; not TE-additive",
        }
    )
    write_csv(DATA / "commitments.csv", c_fields, c_rows)

    lb_fields, lb_rows = read_csv(DATA / "leaderboard.csv")
    lb_rows.append(
        {
            "item_id": LB,
            "name": (
                "MFC Combo empty omzet / bruto 4.46m / pnl DROP -75% / FTE 54.4 (YE2025 Leuven)"
            ),
            "level": "L5",
            "type": "vaph_mfc_vzw_statutory",
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Leuven>MFC_Combo>JR2025",
            "annual_cost_eur": str(BRUTO),
            "total_cost_eur": str(BRUTO),
            "tco_notes": (
                f"CW empty omzet; bruto {BRUTO}; pnl DROP {PNL} (-75.34%); "
                f"equity {EQUITY}; FTE {FTE}; filed {FILED}"
            ),
            "confidence": "medium",
            "source_id": "src_mfc_combo_jr2025_cw_en",
            "beneficiaries": "children/youth Leuven MFC / integral youth care",
            "stated_goal": "VAPH/jeugdhulp multifunctional centre with housing",
            "measured_outcome": "empty omzet; pnl DROP 75%; assets/debt Unknown",
            "absurdity_score": str(ABS),
            "cost_score": str(COST),
            "difficulty": str(int(DIFF)),
            "priority_index": str(PI),
            "cut_proposal": (
                "FOI NBB PDF + empty-omzet path + VAPH/jeugdhulp subsidy matrix + pnl DROP"
            ),
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW + Strong KBO 7 VE RSZ 87.991",
        }
    )
    write_csv(DATA / "leaderboard.csv", lb_fields, lb_rows)

    f_fields, f_rows = read_csv(DATA / "foi_queue.csv")
    f_rows.append(
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Leuven>MFC_Combo>NBB_PDF",
            "entity_id": ENTITY,
            "what_is_missing": (
                f"NBB PDF YE2025 assets/debt/cash; why omzet empty while bruto {BRUTO}; "
                f"pnl DROP {PNL} (-75.34%); VAPH/jeugdhulp subsidy matrix"
            ),
            "why_it_matters": (
                "Medium CW MFC empty omzet + bruto 4.46m + pnl DROP 75%; assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "MFC Combo VZW",
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
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO",
        }
    )
    write_csv(DATA / "foi_queue.csv", f_fields, f_rows)

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    (FOI_DRAFTS / f"{GAP}.md").write_text(
        f"""# FOI draft — MFC Combo Leuven (empty omzet / bruto 4.46m / pnl DROP -75%)

**gap_id:** `{GAP}` · **status:** ready NOT sent · **tick:** {TICK}  
**entity:** MFC Combo VZW — KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; 7 VE; RSZ **87.991**)  
**recipient:** {EMAIL}

## Context
- CW YE2025: omzet **empty**; bruto **EUR{BRUTO}** JUMP +1.15%; pnl **EUR{PNL}** DROP -75.34%; equity **EUR{EQUITY}**; FTE **{FTE}**; filed **{FILED}**.
- After Korenbloem@2351. Stalls AGB Bornem / FARO / AIESH / Gandae / Aralea / Manupal / Vlotter still YE2024.

## Brief
```text
Aan: MFC Combo VZW via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 MFC Combo (KBO {KBO})

1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting ontbrekende omzet terwijl bruto EUR{BRUTO} — VAPH/jeugdhulp-subsidiematrix.
3. Toelichting pnl DROP EUR{PNL} (-75.34% vs YE2024 EUR{PNL24}).
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
            f"tick{TICK} leftover dual MFC Combo {KBO} Medium (empty omzet; bruto {BRUTO}; "
            f"pnl DROP {PNL} -75.34%; equity {EQUITY}; FTE {FTE}; 7 VE RSZ 87.991); "
            f"after Korenbloem@2351; AGB/FARO YE2024; next {next_id}; next EVERY-10 2360"
        ),
    }
    write_csv(DATA / "loop_state.csv", ls_fields, ls_rows)

    with LOG.open("a", encoding="utf-8") as f:
        f.write(
            f"""
### {UTC} - tick {TICK} - {unit_id} MFC Combo Leuven (empty omzet / bruto JUMP 4.46m / pnl DROP -75% / FTE {FTE} / Medium)

- Unit: **{unit_id}** leftover dual after Korenbloem@2351. Prefer NON-stall AGB/FARO YE2024. Took FREE Flemish VAPH/jeugdhulp **MFC Combo VZW** YE2025 (KBO **{KBO}**; {ADDR}; **Actief** **7 VE**; RSZ **87.991**; {EMAIL}). Do not redo Korenbloem/Leieborg/Helan/Staf/De Ark stack.
- Found: CW NL+EN+FR — omzet **empty**; bruto **EUR{BRUTO}** JUMP +1.15%; pnl **EUR{PNL}** DROP -75.34%; equity **EUR{EQUITY}**; FTE **{FTE}**; neerlegging **{FILED}**. Strong KBO. Assets/debt Unknown. Medium.
- Wrote: sources(+5) budgets(+4) commitments(+1) leaderboard(+1 pi {PI}) entities(+1) foi+draft; {unit_id}=done + {next_id} open; ticks={TICK}.
- FOI: **ready not sent**. NOT every-10 (next **2360**). Next: {next_id}.
"""
        )

    raw = DATA / "raw" / f"tick{TICK}"
    raw.mkdir(parents=True, exist_ok=True)
    (raw / "summary.json").write_text(
        (
            f'{{"tick":{TICK},"unit":"MFC_Combo","kbo":"{KBO}","omzet":null,"bruto":{BRUTO},'
            f'"pnl":{PNL},"fte":{FTE},"confidence":"medium","queue":"{unit_id}","pi":{PI}}}\n'
        ),
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
        "docs/doge/scripts/_tick2352_mfc_combo_atomic.py",
    ]
    sh(["git", "add", *paths])
    diff = subprocess.check_output(
        ["git", "diff", "--cached", "--stat"], cwd=str(ROOT), text=True
    )
    if "budgets.csv" not in diff:
        raise SystemExit("ABORT: budgets not staged")
    sh(
        [
            "git",
            "commit",
            "-m",
            f"doge(loop): tick {TICK} — {unit_id} MFC Combo empty omzet bruto 4.46m pnl DROP Medium",
        ]
    )
    try:
        sh(["git", "pull", "--rebase", "origin", "main"])
    except subprocess.CalledProcessError:
        sh(["git", "rebase", "--abort"])
        raise SystemExit("ABORT: rebase failed")
    if "bud_mfc_combo_" not in (DATA / "budgets.csv").read_text(encoding="utf-8"):
        raise SystemExit("ABORT: MFC Combo lost during rebase")
    sh(["git", "push", "origin", "HEAD"])
    sha = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"], cwd=str(ROOT), text=True
    ).strip()
    print(f"PUSHED {sha} unit={unit_id} MFC Combo bruto={BRUTO} empty_omzet pnl_DROP Medium pi={PI}")


if __name__ == "__main__":
    main()
