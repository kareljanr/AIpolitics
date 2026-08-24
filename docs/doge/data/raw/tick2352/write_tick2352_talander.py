# -*- coding: utf-8 -*-
"""Tick 2351: Talander Arendonk YE2025 leftover dual — APPEND-ONLY."""
from __future__ import annotations

import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC = "2026-08-28T04:25:00Z"
TICK = "2352"
RQ, NEXT = "rq_2352", "rq_2353"
ENTITY = "vzw_talander_arendonk"
KBO = "0433.306.225"
KD = "0433306225"
GAP = "gap_talander_nbb_pdf_assets_debt_empty_omzet_bruto_1_60m_pnl_jump_vaph_matrix_l5"
LB = "lb_talander_empty_omzet_bruto_1_60m_pnl_jump_fte_19_jr2025"
COMM = "comm_talander_jr2025_statutory_empty_omzet_bruto_1_60m_vaph"
BRUTO, BRUTO24 = 1603209, 1437845
PNL, PNL24 = 142992, 118277
EQUITY, EQUITY24 = 1662056, 1534181
FTE, FTE24 = 18.8, 17.6
FILED = "24.06.2026"
EMAIL = "info@talander.be"
ADDR = "De Lusthoven 88, 2370 Arendonk"
SITE = "https://www.talander.be"
PNL_PCT = round((PNL - PNL24) / PNL24 * 100, 2)
PI = "4.75"


def read(p: Path):
    with p.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames), list(r)


def write(p: Path, fields, rows):
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


def append_only(p: Path, key: str, news):
    fields, rows = read(p)
    have = {r.get(key) for r in rows}
    data = p.read_bytes()
    if data and not data.endswith(b"\n"):
        p.write_bytes(data + b"\n")
    added = 0
    with p.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        for n in news:
            if n.get(key) in have:
                continue
            w.writerow({k: n.get(k, "") for k in fields})
            have.add(n.get(key))
            added += 1
    return added


fields, rq = read(DATA / "research_queue.csv")
rqrow = next((r for r in rq if r.get("task_id") == RQ), None)
if not rqrow:
    raise SystemExit("rq_2352 missing")
if rqrow.get("status") == "done":
    raise SystemExit("already done: " + (rqrow.get("title") or "")[:80])
eid = (rqrow.get("entity_id") or "").strip()
if rqrow.get("status") == "in_progress" and eid not in ("", ENTITY, "CLAIM_PENDING"):
    raise SystemExit("claimed by " + eid)

_, ents = read(DATA / "entities.csv")
if any(r.get("entity_id") == ENTITY for r in ents):
    raise SystemExit("Talander already mined")

for r in rq:
    if r["task_id"] == RQ:
        r["status"] = "in_progress"
        r["entity_id"] = ENTITY
        r["title"] = (
            "leftover dual — Talander YE2025 Medium "
            "(empty omzet / bruto JUMP 1.60m / pnl JUMP +21% / FTE 18.8)"
        )
        r["hierarchy_path"] = "L5"
        r["updated_utc"] = UTC
        r["notes"] = f"tick2352 CLAIM Talander {KBO}; next EVERY-10 2360"
write(DATA / "research_queue.csv", fields, rq)

ns = append_only(
    DATA / "sources.csv",
    "source_id",
    [
        dict(
            source_id="src_talander_jr2025_cw_en",
            title="Companyweb EN Talander YE2025 statutory",
            url=f"https://www.companyweb.be/en/{KD}/talander",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-24",
            source_class="secondary_aggregator",
            notes=f"tick2352; EN Medium; filed {FILED}; Turnover unpublished; Gross {BRUTO}; P/L {PNL}; Equity {EQUITY}; FTE {FTE}",
        ),
        dict(
            source_id="src_talander_jr2025_cw_nl",
            title="Companyweb NL Talander YE2025 statutory",
            url=f"https://www.companyweb.be/nl/{KD}/talander",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-24",
            source_class="secondary_aggregator",
            notes=f"tick2352; empty omzet; bruto {BRUTO}; pnl JUMP {PNL}; equity {EQUITY}; FTE {FTE}",
        ),
        dict(
            source_id="src_talander_jr2025_cw_fr",
            title="Companyweb FR Talander YE2025 statutory",
            url=f"https://www.companyweb.be/fr/{KD}/talander",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-24",
            source_class="secondary_aggregator",
            notes="tick2352; FR mirror; CA non publie",
        ),
        dict(
            source_id="src_talander_kbo_2352",
            title=f"KBO Talander {KBO}",
            url=f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KD}",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-24",
            source_class="official_register",
            notes=f"tick2352; Strong KBO Actief VZW; VAPH residential mental disability; {ADDR}",
        ),
        dict(
            source_id="src_talander_site_contact_2352",
            title="Talander FOI info@talander.be",
            url=SITE,
            publisher="Talander VZW",
            accessed_date="2026-08-24",
            source_class="foi_contact",
            notes=f"tick2352; {EMAIL}; T 014 67 00 69; {ADDR}",
        ),
    ],
)

nb = append_only(
    DATA / "budgets.csv",
    "budget_id",
    [
        dict(
            budget_id="bud_talander_bruto_jr2025_statutory",
            entity_id=ENTITY,
            year="2025",
            amount_eur=str(BRUTO),
            amount_min_eur=str(BRUTO),
            amount_max_eur=str(BRUTO),
            basis="CW statutory bruto_marge YE2025 JUMP empty-omzet",
            source_id="src_talander_jr2025_cw_en",
            confidence="medium",
            notes=f"tick2352; bruto +11.5% vs {BRUTO24}; omzet empty",
        ),
        dict(
            budget_id="bud_talander_pnl_jr2025_statutory",
            entity_id=ENTITY,
            year="2025",
            amount_eur=str(PNL),
            amount_min_eur=str(PNL),
            amount_max_eur=str(PNL),
            basis="CW statutory winst/verlies YE2025 JUMP",
            source_id="src_talander_jr2025_cw_en",
            confidence="medium",
            notes=f"tick2352; pnl +{PNL_PCT}% vs {PNL24}",
        ),
        dict(
            budget_id="bud_talander_equity_jr2025_statutory",
            entity_id=ENTITY,
            year="2025",
            amount_eur=str(EQUITY),
            amount_min_eur=str(EQUITY),
            amount_max_eur=str(EQUITY),
            basis="CW statutory eigen_vermogen YE2025 JUMP",
            source_id="src_talander_jr2025_cw_en",
            confidence="medium",
            notes=f"tick2352; equity +8.34% vs {EQUITY24}",
        ),
        dict(
            budget_id="bud_talander_fte_jr2025_statutory",
            entity_id=ENTITY,
            year="2025",
            amount_eur=str(FTE),
            amount_min_eur=str(FTE),
            amount_max_eur=str(FTE),
            basis="CW social-balance FTE 18.8",
            source_id="src_talander_jr2025_cw_en",
            confidence="medium",
            notes=f"tick2352; FTE JUMP vs {FTE24}",
        ),
    ],
)

ne = append_only(
    DATA / "entities.csv",
    "entity_id",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Talander VZW (Arendonk / VAPH woonondersteuning mentale handicap)",
            name_fr="Talander ASBL (Arendonk / hebergement VAPH)",
            name_en="Talander VZW (Arendonk / VAPH residential mental disability)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website=SITE,
            foi_email=EMAIL,
            foi_postal=ADDR,
            notes=(
                f"tick2352 YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; omzet empty; bruto JUMP {BRUTO}; "
                f"pnl JUMP {PNL} (+{PNL_PCT}%); equity JUMP {EQUITY}; FTE JUMP {FTE}; neerlegging {FILED}; "
                f"FOI {GAP}; after De Korenbloem@2351; AGB/FARO YE2024; not TE-additive"
            ),
        )
    ],
)

nc = append_only(
    DATA / "commitments.csv",
    "commitment_id",
    [
        dict(
            commitment_id=COMM,
            title="Talander YE2025 statutory empty omzet / bruto 1.60m VAPH",
            entity_id=ENTITY,
            beneficiary="VAPH adults mental disability Arendonk",
            legal_basis="VZW jaarrekening + VL VAPH residential path",
            decision_date=FILED,
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(BRUTO),
            cash_by_year=f"2025:{BRUTO}",
            remaining_eur="",
            status="active_statutory",
            evaluation_url=f"https://www.companyweb.be/en/{KD}/talander",
            stated_goal="residential care adults mental disability (heilpedagogie)",
            cut_option="FOI NBB PDF assets/debt; publish omzet; VAPH subsidy matrix",
            source_id="src_talander_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Arendonk>Talander>JR2025",
            notes=f"tick2352; Medium CW; empty omzet; bruto JUMP; pnl JUMP +{PNL_PCT}%",
        )
    ],
)

nlb = append_only(
    DATA / "leaderboard.csv",
    "item_id",
    [
        dict(
            item_id=LB,
            name="Talander empty omzet / bruto 1.60m / pnl JUMP +21% / FTE 18.8 (YE2025)",
            level="L5",
            type="vaph_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Arendonk>Talander>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes=(
                f"CW empty omzet; bruto JUMP {BRUTO}; pnl JUMP {PNL} (+{PNL_PCT}%); "
                f"equity JUMP {EQUITY}; FTE JUMP {FTE}; filed {FILED}"
            ),
            confidence="medium",
            source_id="src_talander_jr2025_cw_en",
            beneficiaries="VAPH adults mental disability Arendonk",
            stated_goal="VAPH residential care / heilpedagogie",
            measured_outcome="empty omzet; bruto 1.60m; pnl JUMP +21%; FTE 18.8",
            absurdity_score="6.5",
            cost_score="3.0",
            difficulty="3.0",
            priority_index=PI,
            cut_proposal="Publish NBB PDF assets/debt FOI; publish omzet; reconcile VAPH subsidy path",
            status="open",
            struck_reason="",
            notes=f"tick2352; Medium CW; FOI {GAP}; after De Korenbloem@2351; AGB/FARO YE2024",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Talander (empty omzet / bruto 1.60m / pnl JUMP)

**gap_id:** `{GAP}` · **status:** ready NOT sent · **tick:** {TICK}  
**entity:** Talander VZW — KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; VAPH residential mental disability)  
**recipient:** {EMAIL}

## Brief
```text
Aan: Talander VZW via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 Talander (KBO {KBO})

1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting waarom omzet unpublished terwijl bruto EUR{BRUTO}.
3. Toelichting pnl JUMP EUR{PNL} (+{PNL_PCT}% vs YE2024 EUR{PNL24}).
4. VAPH/PVF-subsidy matrix vs FTE {FTE}.
5. Schulden LT/KT en liquiditeiten YE2025.

Ref: {GAP}
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

nf = append_only(
    DATA / "foi_queue.csv",
    "gap_id",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>Antwerpen>Arendonk>Talander>NBB_PDF_assets_debt_empty_omzet",
            entity_id=ENTITY,
            what_is_missing=(
                f"NBB PDF YE2025 full (assets/debt/cash); why omzet unpublished while bruto EUR{BRUTO}; "
                f"pnl JUMP EUR{PNL}; VAPH/PVF matrix"
            ),
            why_it_matters=(
                "Medium CW shows Arendonk VAPH residential VZW (empty omzet / bruto 1.60m / "
                "pnl JUMP +21% / FTE 18.8) under public care path; assets/debt unpublished"
            ),
            priority="8",
            recipient_body="Talander VZW",
            recipient_email=EMAIL,
            recipient_postal=ADDR,
            draft_letter_path=f"docs/doge/foi/drafts/{GAP}.md",
            status="ready",
            date_ready="2026-08-24",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id=COMM,
            linked_leaderboard_id=LB,
            created_utc=UTC,
            updated_utc=UTC,
            notes="tick2352; ready NOT sent; Medium CW + Strong KBO; after De Korenbloem@2351",
        )
    ],
)

fields, rq = read(DATA / "research_queue.csv")
have_next = any(r.get("task_id") == NEXT for r in rq)
for r in rq:
    if r["task_id"] == RQ:
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["gap_id"] = GAP
        r["title"] = (
            "leftover dual — Talander YE2025 Medium "
            "(empty omzet / bruto JUMP 1.60m / pnl JUMP +21% / FTE 18.8)"
        )
        r["hierarchy_path"] = "L5"
        r["completed_utc"] = UTC
        r["updated_utc"] = UTC
        r["notes"] = (
            f"tick2352; Talander {KBO} Medium CW; omzet empty; bruto {BRUTO}; pnl JUMP {PNL}; "
            f"equity JUMP {EQUITY}; FTE JUMP {FTE}; FOI {GAP} ready NOT sent; after De Korenbloem@2351; "
            f"next EVERY-10 2360"
        )
if not have_next:
    blank = {k: "" for k in fields}
    blank.update(
        task_id=NEXT,
        title="leftover dual after Talander — prefer AGB/FARO-YE2025/or-unused ETA-VAPH-WZC-maatwerk",
        sprint="hole_fill",
        priority="8",
        status="open",
        hierarchy_path="leftover_dual",
        blocker_notes=(
            "After Talander YE2025. Prefer AGB/FARO if YE2025 else FREE. "
            "Do NOT redo Talander/Korenbloem/Leieborg/Helan/Korenbloem/Oostrem/Staf stack."
        ),
        created_utc=UTC,
        updated_utc=UTC,
        notes="spawned after tick2352 Talander; next EVERY-10 2360",
    )
    rq.append(blank)
write(DATA / "research_queue.csv", fields, rq)

fields, ls = read(DATA / "loop_state.csv")
for r in ls:
    if r.get("state_id") == "main":
        r.update(
            mode="continuous",
            current_sprint="hole_fill",
            last_tick_utc=UTC,
            last_unit_id=RQ,
            ticks_completed=TICK,
            paused="no",
            notes=(
                f"tick2352 leftover dual Talander {KBO} Medium (omzet empty; bruto JUMP {BRUTO}; "
                f"pnl JUMP {PNL} +{PNL_PCT}%; equity JUMP {EQUITY}; FTE JUMP {FTE}); "
                f"after De Korenbloem@2351; AGB/FARO YE2024; next {NEXT}; next EVERY-10 2360; continuous hole_fill"
            ),
        )
write(DATA / "loop_state.csv", fields, ls)

raw = DATA / "raw" / f"tick{TICK}"
raw.mkdir(parents=True, exist_ok=True)
(raw / "summary.json").write_text(
    json.dumps(
        dict(
            tick=TICK,
            entity_id=ENTITY,
            kbo=KBO,
            omzet=None,
            bruto=BRUTO,
            pnl=PNL,
            equity=EQUITY,
            fte=FTE,
            confidence="medium",
            gap_id=GAP,
        ),
        indent=2,
    ),
    encoding="utf-8",
)

with LOG.open("a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Talander Arendonk (empty omzet / bruto JUMP 1.60m / pnl JUMP +{PNL_PCT}% / FTE 18.8 / Medium)

- Unit: **{RQ}** after **Leieborg@2350**. Stalls AGB/FARO YE2024. Took FREE Flemish VAPH **Talander VZW** YE2025 (KBO **{KBO}**; {ADDR}; Actief; {EMAIL}). Do not redo Korenbloem/Leieborg/Helan/Korenbloem/Oostrem/Staf stack.
- Found: CW NL+EN+FR — omzet **empty**; bruto **EUR{BRUTO}** JUMP +11.5%; pnl **EUR{PNL}** JUMP +{PNL_PCT}%; equity **EUR{EQUITY}**; FTE **{FTE}**; neerlegging **{FILED}**. Medium.
- Wrote: sources(+{ns}) budgets(+{nb}) ents(+{ne}) comm(+{nc}) lb(+{nlb} pi {PI}) foi(+{nf}); {RQ}=done + {NEXT} open; ticks={TICK}.
- FOI ready NOT sent. NOT every-10 (Leieborg used rq_2350 id; next **2360**). Next: {NEXT}.
"""
    )

print(f"OK {RQ} src={ns} bud={nb} ent={ne} foi={nf}")
