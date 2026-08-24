import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-28T03:50:00Z"
ROOT = Path("docs/doge/data")
Path("docs/doge/data/raw/tick2346").mkdir(parents=True, exist_ok=True)
Path("docs/doge/foi/drafts").mkdir(parents=True, exist_ok=True)

GAP = "gap_korenbloem_nbb_pdf_assets_debt_pnl_loss_flip_wzc_matrix_l5"
LB = "lb_korenbloem_omzet_12_56m_pnl_loss_flip_equity_drop_fte_176_jr2025"
COMM = "comm_korenbloem_jr2025_statutory_wzc_omzet_12_56m_pnl_loss_flip"
ENTITY = "vzw_de_korenbloem_kortrijk"
RQ = "rq_2347"
RQ_NEXT = "rq_2348"
TICK = "2346"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def has_id(path, key, val):
    with open(path, encoding="utf-8", newline="") as f:
        return any(row.get(key) == val for row in csv.DictReader(f))


path_rq = ROOT / "research_queue.csv"
with open(path_rq, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
if len(rq_rows) < 2000:
    raise SystemExit(f"research_queue too small ({len(rq_rows)}); abort rewrite")
rq = next((row for row in rq_rows if row["task_id"] == RQ), None)
if not rq or rq.get("status") not in ("open", "in_progress"):
    raise SystemExit(f"{RQ} not claimable: " + repr(rq and rq.get("status")))
if has_id(ROOT / "entities.csv", "entity_id", ENTITY):
    raise SystemExit("De Korenbloem already present")
for row in rq_rows:
    if row["task_id"] == RQ:
        row["status"] = "in_progress"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
with open(path_rq, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rq_rows)

if not has_id(ROOT / "sources.csv", "source_id", "src_korenbloem_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        (
            "src_korenbloem_jr2025_cw_nl",
            "Companyweb NL De Korenbloem YE2025 statutory",
            "https://www.companyweb.be/nl/0418825412/de-korenbloem",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick{TICK}; YE2025 omzet JUMP 12564145 bruto JUMP 12311379 pnl LOSS FLIP -360537 equity DROP 8688763 FTE JUMP 175.9; filed 03-06-2026",
        ),
        (
            "src_korenbloem_jr2025_cw_en",
            "Companyweb EN De Korenbloem YE2025 statutory",
            "https://www.companyweb.be/en/0418825412/de-korenbloem",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick{TICK}; EN Medium; Turnover 12564145 Gross 12311379 P/L -360537 Equity 8688763 FTE 175.9; filed 03-06-2026",
        ),
        (
            "src_korenbloem_jr2025_cw_fr",
            "Companyweb FR De Korenbloem YE2025 statutory",
            "https://www.companyweb.be/fr/0418825412/de-korenbloem",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick{TICK}; FR mirror YE2025 CA 12564145 marge 12311379 perte -360537 equity 8688763 FTE 175.9",
        ),
        (
            f"src_korenbloem_kbo_{TICK}",
            "KBO De Korenbloem 0418.825.412",
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418825412",
            "KBO FOD Economie",
            "official_register",
            f"tick{TICK}; Actief VZW 1 VE Kortrijk Aanbestedende; RSZ 87.101 RVT; zetel Pieter de Conincklaan 12 8500 Kortrijk",
        ),
        (
            f"src_korenbloem_site_contact_{TICK}",
            "De Korenbloem FOI info@dekorenbloem.net",
            "https://www.dekorenbloem.net/",
            "De Korenbloem VZW",
            "foi_contact",
            f"tick{TICK}; info@dekorenbloem.net; Pieter de Conincklaan 12, 8500 Kortrijk; T 056 26 01 01",
        ),
    ]:
        append_csv(
            ROOT / "sources.csv",
            dict(
                source_id=sid,
                title=title,
                url=url,
                publisher=pub,
                accessed_date="2026-08-28",
                source_class=klass,
                notes=notes,
            ),
        )

append_csv(
    ROOT / "entities.csv",
    dict(
        entity_id=ENTITY,
        name_nl="De Korenbloem VZW (Kortrijk / WZC RVT)",
        name_fr="De Korenbloem ASBL (Courtrai / MRS)",
        name_en="De Korenbloem VZW (Kortrijk / nursing home RVT)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://www.dekorenbloem.net/",
        foi_email="info@dekorenbloem.net",
        foi_postal="Pieter de Conincklaan 12, 8500 Kortrijk",
        notes=f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0418.825.412 Actief VZW 1 VE Aanbestedende RSZ 87.101; omzet JUMP 12564145 (+2.22%); bruto JUMP 12311379 (+0.17%); pnl LOSS FLIP -360537; equity DROP 8688763 (-4.9%); FTE JUMP 175.9; neerlegging 03.06.2026; assets/debt Unknown; FOI gap_korenbloem_*; after Staf@2345; AGB/FARO YE2024; Gandae/Aralea/Manupal/Vlotter YE2024; not TE-additive of 348bn",
    ),
)

for bid, amt, basis, notes in [
    ("bud_korenbloem_omzet_jr2025_statutory", 12564145, "CW statutory omzet YE2025 JUMP", f"tick{TICK}; Medium CW; omzet +2.22% vs 12291695"),
    ("bud_korenbloem_bruto_jr2025_statutory", 12311379, "CW statutory bruto_marge YE2025", f"tick{TICK}; Medium CW; bruto +0.17% vs 12290405"),
    ("bud_korenbloem_pnl_jr2025_statutory", -360537, "CW statutory winst/verlies YE2025 LOSS FLIP", f"tick{TICK}; Medium CW; pnl LOSS FLIP from +73799 YE2024"),
    ("bud_korenbloem_equity_jr2025_statutory", 8688763, "CW statutory eigen_vermogen YE2025 DROP", f"tick{TICK}; Medium CW; equity -4.9% vs 9136438"),
    ("bud_korenbloem_fte_jr2025_statutory", 175.9, "CW social-balance FTE 175.9", f"tick{TICK}; Medium CW; FTE 175.9 vs 172.7"),
]:
    append_csv(
        ROOT / "budgets.csv",
        dict(
            budget_id=bid,
            entity_id=ENTITY,
            year="2025",
            amount_eur=str(amt),
            amount_min_eur=str(amt),
            amount_max_eur=str(amt),
            basis=basis,
            source_id="src_korenbloem_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        ),
    )

# assert budgets not truncated
with open(ROOT / "budgets.csv", encoding="utf-8", newline="") as _f:
    _n = sum(1 for _ in _f) - 1
if _n < 50000:
    raise SystemExit(f"budgets truncated ({_n}); abort")

append_csv(
    ROOT / "commitments.csv",
    dict(
        commitment_id=COMM,
        title="De Korenbloem YE2025 leftover dual (omzet 12.56m / pnl LOSS FLIP / equity DROP / FTE 175.9 / Medium)",
        entity_id=ENTITY,
        beneficiary="ouderen Kortrijk / WZC RVT publiek pad",
        legal_basis="VZW De Korenbloem (KBO 0418.825.412; Actief; 1 VE; Aanbestedende; RSZ NACE 87.101 RVT)",
        decision_date="2026-06-03",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="12564145",
        cash_by_year='{"2025_omzet":12564145,"2025_bruto":12311379,"2025_pnl":-360537,"2025_equity":8688763,"2025_fte":175.9,"2024_omzet":12291695,"2024_bruto":12290405,"2024_pnl":73799,"2024_equity":9136438,"2024_fte":172.7}',
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0418825412/de-korenbloem",
        stated_goal="WZC/RVT De Korenbloem Kortrijk",
        cut_option="Publish NBB PDF assets/debt FOI; explain pnl LOSS FLIP + equity DROP",
        source_id="src_korenbloem_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Vlaanderen>WestVlaanderen>Kortrijk>DeKorenbloem_WZC>JR2025_statutory_L5",
        notes=f"tick{TICK}; Medium CW; after Staf@2345; not TE-additive",
    ),
)

append_csv(
    ROOT / "leaderboard.csv",
    dict(
        item_id=LB,
        name="De Korenbloem omzet 12.56m / pnl LOSS FLIP -0.36m / equity DROP / FTE 175.9 (YE2025 WZC Kortrijk)",
        level="L5",
        type="wzc_vzw_statutory",
        hierarchy_path="Vlaanderen>WestVlaanderen>Kortrijk>DeKorenbloem_WZC>JR2025",
        annual_cost_eur="12564145",
        total_cost_eur="12564145",
        tco_notes="CW omzet 12564145 / bruto 12311379 / pnl LOSS FLIP -360537 / equity DROP 8688763 / FTE 175.9",
        confidence="medium",
        source_id="src_korenbloem_jr2025_cw_en",
        beneficiaries="ouderen Kortrijk WZC",
        stated_goal="WZC RVT care",
        measured_outcome="pnl LOSS FLIP from +73799 to -360537; equity DROP -4.9%; FTE 175.9; filed 03.06.2026",
        absurdity_score="6.5",
        cost_score="5.5",
        difficulty="3.0",
        priority_index="6.00",
        cut_proposal="Publish NBB PDF assets/debt FOI; WZC RIZIV/Vlaams subsidy matrix; explain loss flip",
        status="open",
        struck_reason="",
        notes=f"tick{TICK}; Medium CW; FOI gap_korenbloem_*; after Staf@2345",
    ),
)

append_csv(
    ROOT / "foi_queue.csv",
    dict(
        gap_id=GAP,
        hierarchy_path="Vlaanderen>WestVlaanderen>Kortrijk>DeKorenbloem_WZC>NBB_PDF",
        entity_id=ENTITY,
        what_is_missing="NBB PDF YE2025 assets/debt; pnl LOSS FLIP -360537 vs YE2024 +73799; equity DROP; WZC RIZIV/Vlaams subsidy matrix; FTE 175.9",
        why_it_matters="Medium CW WZC Kortrijk pnl LOSS FLIP with rising omzet; Aanbestedende; assets/debt unknown",
        priority="8",
        recipient_body="De Korenbloem VZW",
        recipient_email="info@dekorenbloem.net",
        recipient_postal="Pieter de Conincklaan 12, 8500 Kortrijk",
        draft_letter_path=f"docs/doge/foi/drafts/{GAP}.md",
        status="ready",
        date_ready="2026-08-28",
        date_sent="",
        date_due="",
        date_answered="",
        response_summary="",
        linked_commitment_id=COMM,
        linked_leaderboard_id=LB,
        created_utc=UTC,
        updated_utc=UTC,
        notes=f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Staf@2345",
    ),
)

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft ΓÇö De Korenbloem Kortrijk (NBB PDF / pnl LOSS FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** De Korenbloem VZW ΓÇö KBO **0418.825.412** (Actief; Pieter de Conincklaan 12, 8500 Kortrijk; FTE 175.9; 1 VE; Aanbestedende; RSZ **87.101** RVT)  
**recipient:** info@dekorenbloem.net ┬╖ Pieter de Conincklaan 12, 8500 Kortrijk (T 056 26 01 01)  
**sources:** [CW EN](https://www.companyweb.be/en/0418825412/de-korenbloem) ┬╖ [CW NL](https://www.companyweb.be/nl/0418825412/de-korenbloem) ┬╖ [CW FR](https://www.companyweb.be/fr/0418825412/de-korenbloem) ┬╖ [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418825412) ┬╖ [site](https://www.dekorenbloem.net/)  
**tick:** {TICK}  
**confidence:** Medium

## Context
- CW YE2025: omzet **EUR12,564,145** JUMP +2.22%; bruto **EUR12,311,379** JUMP +0.17%; pnl **EUR-360,537** LOSS FLIP (from +73,799); equity **EUR8,688,763** DROP -4.9%; FTE **175.9**; filed **03.06.2026**.
- After Staf@2345. Stalls: AGB Bornem JR2024; FARO/AIESH/Gandae/Aralea/Manupal/Vlotter YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: De Korenbloem VZW
via info@dekorenbloem.net
Pieter de Conincklaan 12, 8500 Kortrijk
Betreft: Openbaarmaking jaarrekening 2025 De Korenbloem (KBO 0418.825.412)

Geachte,
Op grond van openbaarheid van bestuur / Bestuursdecreet vraag ik:
1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting pnl LOSS FLIP EUR-360537 (vs YE2024 +73799) bij omzet JUMP.
3. Toelichting equity DROP EUR8688763 (-4.9%).
4. Overzicht publieke toelagen YE2025 (+ YE2024) ΓÇö RIZIV/Vlaams WZC-matrix.
5. Schulden LT/KT en liquide middelen YE2025.
Ref: {GAP}
Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

with open(path_rq, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

for row in rows:
    if row["task_id"] == RQ:
        row["status"] = "done"
        row["title"] = "leftover dual ΓÇö De Korenbloem YE2025 Medium (omzet JUMP 12.56m / pnl LOSS FLIP / equity DROP / FTE 175.9)"
        row["entity_id"] = ENTITY
        row["hierarchy_target"] = "L5"
        row["priority"] = "8"
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = (
            f"tick{TICK} De Korenbloem 0418.825.412 YE2025 Medium; omzet 12564145; bruto 12311379; "
            "pnl LOSS FLIP -360537; equity DROP 8688763; FTE 175.9; FOI ready NOT sent; after Staf@2345; next EVERY-10 2350"
        )
        row["instructions"] = (
            "After Staf@2345. Prefer AGB/FARO YE2025 else unused. Do NOT redo De Korenbloem/Staf/De Lier/Blijdorp/De Ark stack."
        )

if not any(row["task_id"] == RQ_NEXT for row in rows):
    rows.append(
        {
            "task_id": RQ_NEXT,
            "title": "leftover dual after De Korenbloem ΓÇö prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"After De Korenbloem YE2025 Medium@{TICK}. Prefer AGB/FARO YE2025 else FREE "
                "(Gandae/Aralea/Manupal/Vlotter if YE2025 / unused ETA-VAPH-WZC). "
                "Do NOT redo De Korenbloem/Staf/De Lier/Blijdorp/De Ark/Aurelia stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK} De Korenbloem; next EVERY-10 2350",
        }
    )

if len(rows) < 2000:
    raise SystemExit(f"research_queue rewrite too small ({len(rows)}); abort")
with open(path_rq, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with open(ROOT / "loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        dict(
            state_id="main",
            mode="continuous",
            current_sprint="hole_fill",
            last_tick_utc=UTC,
            last_unit_id=RQ,
            ticks_completed=TICK,
            paused="no",
            notes=(
                f"tick{TICK} leftover dual De Korenbloem 0418.825.412 Medium "
                "(omzet JUMP 12564145; bruto JUMP 12311379; pnl LOSS FLIP -360537; equity DROP 8688763; FTE JUMP 175.9; "
                f"1 VE Kortrijk WZC RVT Aanbestedende); after Staf@2345; AGB/FARO YE2024; next {RQ_NEXT}; next EVERY-10 2350"
            ),
        )
    )

with open("docs/doge/loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} ΓÇö tick {TICK} ΓÇö {RQ} De Korenbloem Kortrijk (omzet JUMP 12.56m / pnl LOSS FLIP / equity DROP / FTE 175.9 / Medium)

- Unit: **{RQ}** leftover dual after Staf@2345. Stalls AGB Bornem / FARO / AIESH / Gandae / Aralea / Manupal / Vlotter still **YE2024**. Took FREE Flemish WZC **De Korenbloem VZW** YE2025 (KBO **0418.825.412**; Pieter de Conincklaan 12, 8500 Kortrijk; **Actief** **1 VE**; Aanbestedende; RSZ **87.101** RVT; info@dekorenbloem.net).
- Found (CW NL+EN+FR YE2025): omzet **EUR12564145** JUMP +2.22%; bruto **EUR12311379** JUMP +0.17%; pnl **EUR-360537** LOSS FLIP; equity **EUR8688763** DROP -4.9%; FTE **175.9**; neerlegging **03.06.2026**. Strong KBO. Assets/debt Unknown. Medium.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.00); entities (+1 {ENTITY}); foi + draft `{GAP}`; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}.
- FOI: **ready not sent**. NOT every-10 (next **2350**). Next: {RQ_NEXT}.
"""
    )

print(f"OK tick{TICK} De Korenbloem")
print("pnl", -360537, "omzet", 12564145)
