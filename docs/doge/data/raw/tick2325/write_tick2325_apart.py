# tick 2325: leftover dual aPart Gent YE2025 after Ritmica@2324 (SWITCH from Het Eepos claim)
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
FOI = Path("docs/doge/foi/drafts")
LOG = Path("docs/doge/loop_log.md")
UTC = "2026-08-24T16:20:00Z"
TICK = "2325"
RQ = "rq_2325"
NEXT_RQ = "rq_2326"
ENTITY = "vzw_apart_gent"
KBO = "0567.657.460"
GAP = "gap_apart_nbb_pdf_assets_debt_bruto_gt_omzet_419_67x_pnl_drop_99pct_jeugdhulp_matrix_l5"
LB = "lb_apart_bruto_8_79m_omzet_20_9k_419_67x_pnl_drop_99pct_jr2025"
COMM = "comm_apart_jr2025_statutory_jeugdhulp_bruto_gt_omzet_419_67x"
OMZET, BRUTO, PNL, EQUITY, FTE = 20940, 8787800, 3607, 4025991, 115.7
OMZET24, BRUTO24, PNL24, EQUITY24, FTE24 = 26679, 8354144, 856164, 4037002, 110.8
RATIO = round(BRUTO / OMZET, 2)
ABS, COST, DIFF, PI = 9.0, 5.2, 3.0, 6.71
EMAIL = "info.vzwapart@vzwapart.be"
ADDR = "Brandstraat 3, 9000 Gent"


def append_csv(path, row):
    p = Path(path)
    with p.open(newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    data = p.read_bytes()
    if data and not data.endswith(b"\n"):
        p.write_bytes(data + b"\n")
    out = {k: row.get(k, "") for k in fields}
    with p.open("a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def has_id(path, key, val):
    with open(path, encoding="utf-8", newline="") as f:
        return any(row.get(key) == val for row in csv.DictReader(f))


rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

for row in rows:
    if row["task_id"] == RQ:
        if row["status"] == "done" and row.get("entity_id") not in ("", ENTITY, "vzw_het_eepos_laakdal"):
            raise SystemExit("rq_2325 already done by other: " + (row.get("entity_id") or ""))
        if (
            row["status"] == "in_progress"
            and (row.get("entity_id") or "").strip()
            not in ("", ENTITY, "vzw_het_eepos_laakdal")
        ):
            raise SystemExit("rq_2325 claimed by other: " + (row.get("entity_id") or ""))

if not has_id(ROOT / "sources.csv", "source_id", "src_apart_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        (
            "src_apart_jr2025_cw_nl",
            "Companyweb NL aPart YE2025 statutory",
            "https://www.companyweb.be/nl/0567657460/apart",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick{TICK}; YE2025 omzet DROP {OMZET} bruto JUMP {BRUTO} ~{RATIO}x pnl DROP {PNL} equity {EQUITY} FTE JUMP {FTE}; filed 24.06.2026",
        ),
        (
            "src_apart_jr2025_cw_en",
            "Companyweb EN aPart YE2025 statutory",
            "https://www.companyweb.be/en/0567657460/apart",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick{TICK}; EN Medium; Last balance 2025; Turnover {OMZET} Gross {BRUTO} P/L {PNL} Equity {EQUITY} FTE {FTE}",
        ),
        (
            "src_apart_jr2025_cw_fr",
            "Companyweb FR aPart YE2025 statutory",
            "https://www.companyweb.be/fr/0567657460/apart",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick{TICK}; FR mirror YE2025; CA {OMZET}; marge brute {BRUTO}",
        ),
        (
            f"src_apart_kbo_{TICK}",
            f"KBO aPart {KBO} Actief 12 VE Gent RSZ 87.991",
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0567657460",
            "KBO FOD Economie",
            "official_register",
            f"tick{TICK}; Strong KBO Actief VZW sinds 14.10.2014; Brandstraat 3 9000 Gent; 12 VE; RSZ 87.991 integrale jeugdhulp met huisvesting",
        ),
        (
            f"src_apart_site_contact_{TICK}",
            "aPart FOI info.vzwapart@vzwapart.be",
            "https://vzwapart.be/contacteer-ons",
            "aPart VZW",
            "foi_contact",
            f"tick{TICK}; {EMAIL}; {ADDR}; T 09 225 01 59",
        ),
    ]:
        append_csv(
            ROOT / "sources.csv",
            dict(
                source_id=sid,
                title=title,
                url=url,
                publisher=pub,
                accessed_date="2026-08-24",
                source_class=klass,
                notes=notes,
            ),
        )

if not has_id(ROOT / "entities.csv", "entity_id", ENTITY):
    append_csv(
        ROOT / "entities.csv",
        dict(
            entity_id=ENTITY,
            name_nl="aPart VZW (Gent / integrale jeugdhulp)",
            name_fr="aPart ASBL (Gand / aide à la jeunesse avec hébergement)",
            name_en="aPart VZW (Ghent / residential youth care)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://vzwapart.be/",
            foi_email=EMAIL,
            foi_postal=ADDR,
            notes=(
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 12 VE RSZ 87.991; "
                f"omzet DROP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} (-99.58%); equity {EQUITY}; "
                f"FTE JUMP {FTE}; neerlegging 24.06.2026; FOI {GAP}; after Ritmica@2324; SWITCH from Het Eepos claim; "
                "AGB/FARO YE2024; not TE-additive"
            ),
        ),
    )

if not has_id(ROOT / "budgets.csv", "budget_id", "bud_apart_omzet_jr2025_statutory"):
    for bid, amt, basis, notes in [
        (
            "bud_apart_omzet_jr2025_statutory",
            OMZET,
            "CW statutory omzet YE2025 DROP",
            f"tick{TICK}; Medium CW; omzet -21.51% vs {OMZET24}",
        ),
        (
            "bud_apart_bruto_jr2025_statutory",
            BRUTO,
            f"CW statutory bruto_marge YE2025 ~{RATIO}x omzet",
            f"tick{TICK}; Medium CW; bruto +5.19% vs {BRUTO24}",
        ),
        (
            "bud_apart_pnl_jr2025_statutory",
            PNL,
            "CW statutory winst/verlies YE2025 DROP -99.58%",
            f"tick{TICK}; Medium CW; pnl DROP vs {PNL24}",
        ),
        (
            "bud_apart_equity_jr2025_statutory",
            EQUITY,
            "CW statutory eigen_vermogen YE2025",
            f"tick{TICK}; Medium CW; equity -0.27% vs {EQUITY24}",
        ),
        (
            "bud_apart_fte_jr2025_statutory",
            FTE,
            "CW social-balance FTE 115.7",
            f"tick{TICK}; Medium CW; FTE JUMP vs {FTE24}",
        ),
    ]:
        append_csv(
            ROOT / "budgets.csv",
            dict(
                budget_id=bid,
                entity_id=ENTITY,
                year="2025",
                amount_eur=amt,
                amount_min_eur=amt,
                amount_max_eur=amt,
                basis=basis,
                source_id="src_apart_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            ),
        )

if not has_id(ROOT / "commitments.csv", "commitment_id", COMM):
    cash = json.dumps(
        {
            "2025_omzet": OMZET,
            "2025_bruto": BRUTO,
            "2025_pnl": PNL,
            "2025_equity": EQUITY,
            "2025_fte": FTE,
            "2024_omzet": OMZET24,
            "2024_bruto": BRUTO24,
            "2024_pnl": PNL24,
            "2024_equity": EQUITY24,
            "2024_fte": FTE24,
            "ratio_bruto_omzet": RATIO,
        },
        separators=(",", ":"),
    )
    append_csv(
        ROOT / "commitments.csv",
        dict(
            commitment_id=COMM,
            title=(
                f"aPart YE2025 leftover dual (omzet {OMZET} / bruto {BRUTO} ~{RATIO}x / "
                f"pnl DROP -99.58% / FTE {FTE} / Medium)"
            ),
            entity_id=ENTITY,
            beneficiary="kinderen/jongeren/jongvolwassenen kwetsbare positie Gent / VL jeugdhulp",
            legal_basis=f"VZW aPart (KBO {KBO}; Actief; 12 VE; RSZ 87.991)",
            decision_date="2026-06-24",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=BRUTO,
            cash_by_year=cash,
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0567657460/apart",
            stated_goal="Integrale jeugdhulp met huisvesting (aPart Gent)",
            cut_option=f"Publish NBB PDF assets/debt FOI; explain bruto~{RATIO}x omzet + pnl DROP -99.58%",
            source_id="src_apart_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>OostVlaanderen>Gent>aPart_jeugdhulp>JR2025_statutory_L5",
            notes=f"tick{TICK}; Medium CW; after Ritmica@2324; not TE-additive",
        ),
    )

if not has_id(ROOT / "leaderboard.csv", "item_id", LB):
    append_csv(
        ROOT / "leaderboard.csv",
        dict(
            item_id=LB,
            name=f"aPart bruto 8.79m / omzet 20.9k ~{RATIO}x / pnl DROP -99.58% (YE2025)",
            level="L5",
            type="jeugdhulp_vzw_statutory",
            hierarchy_path="Vlaanderen>OostVlaanderen>Gent>aPart>JR2025",
            annual_cost_eur=BRUTO,
            total_cost_eur=BRUTO,
            tco_notes=(
                f"CW omzet DROP {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x) / pnl DROP {PNL} from {PNL24} / "
                f"equity {EQUITY} / FTE JUMP {FTE} / filed 24.06.2026"
            ),
            confidence="medium",
            source_id="src_apart_jr2025_cw_en",
            beneficiaries="VL jeugdhulp Gent minors/youth",
            stated_goal="Integrale jeugdhulp met huisvesting",
            measured_outcome=f"bruto÷omzet ~{RATIO}x; pnl DROP -99.58%; FTE JUMP {FTE24}→{FTE}",
            absurdity_score=str(ABS),
            cost_score=str(COST),
            difficulty=str(DIFF),
            priority_index=str(PI),
            cut_proposal=f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x + pnl crash",
            status="open",
            struck_reason="",
            notes=f"tick{TICK}; Medium CW; FOI {GAP}; after Ritmica@2324; AGB/FARO YE2024",
        ),
    )

if not has_id(ROOT / "foi_queue.csv", "gap_id", GAP):
    append_csv(
        ROOT / "foi_queue.csv",
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>OostVlaanderen>Gent>aPart>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop",
            entity_id=ENTITY,
            what_is_missing=(
                f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — "
                f"OJW/Opgroeien subsidy matrix; pnl DROP EUR{PNL} vs YE2024 EUR{PNL24} (-99.58%); FTE JUMP"
            ),
            why_it_matters=(
                f"Medium CW shows Gent jeugdhulp VZW (bruto 8.79m / omzet 20.9k ~{RATIO}x / pnl DROP -99.58% / FTE 115.7) "
                "under public youth-care path; assets/debt unpublished"
            ),
            priority="8",
            recipient_body="aPart VZW",
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
            notes=f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Ritmica@2324",
        ),
    )

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — aPart Gent (NBB PDF / bruto≫omzet ~{RATIO}x / pnl DROP -99.58%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** aPart VZW — KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; RSZ **87.991**; 12 VE)  
**recipient:** {EMAIL} · {ADDR} (T 09 225 01 59)  
**sources:** [CW EN](https://www.companyweb.be/en/0567657460/apart) · [CW NL](https://www.companyweb.be/nl/0567657460/apart) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0567657460) · [site](https://vzwapart.be/contacteer-ons)  
**tick:** {TICK}  
**confidence:** Medium

## Context
- CW YE2025: omzet **EUR{OMZET:,}** DROP −21.51%; bruto **EUR{BRUTO:,}** JUMP +5.19% (~**{RATIO}x**); pnl **EUR{PNL:,}** DROP −99.58%; equity **EUR{EQUITY:,}**; FTE **{FTE}** JUMP; filed **24.06.2026**.
- After Ritmica@2324. Stalls AGB Bornem/FARO/AIESH still YE2024. SWITCH from Het Eepos claim (unused).

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: aPart VZW
via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 aPart (KBO {KBO})

Geachte,
Op grond van openbaarheid van bestuur vraag ik:
1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — OJW/Opgroeien-matrix.
3. Toelichting pnl DROP EUR{PNL} vs YE2024 EUR{PNL24} (−99.58%) bij FTE JUMP tot {FTE}.
4. Overzicht publieke toelagen YE2025 (Opgroeien / lokale besturen).
5. Schulden LT/KT en liquide middelen YE2025.
Ref: {GAP}
Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent
""",
    encoding="utf-8",
)

out_rows = []
has_next = False
for row in rows:
    if row["task_id"] == RQ:
        row["title"] = (
            f"leftover dual — aPart YE2025 Medium (bruto JUMP 8.79m / ~{RATIO}x omzet / "
            f"pnl DROP -99.58% / FTE JUMP 115.7)"
        )
        row["status"] = "done"
        row["hierarchy_target"] = "L5"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "After Ritmica. Prefer AGB/FARO YE2025 else unused. Do NOT redo Ritmica/Dominiek Savio/Merlijn/Humival stack."
        )
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = (
            f"tick{TICK}; aPart {KBO} Medium CW; omzet DROP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; "
            f"pnl DROP {PNL}; equity {EQUITY}; FTE JUMP {FTE}; 12 VE RSZ 87.991; FOI {GAP} ready NOT sent; "
            f"after Ritmica@2324; SWITCH from Het Eepos; next EVERY-10 2330"
        )
    if row["task_id"] == NEXT_RQ:
        has_next = True
    out_rows.append(row)

if not has_next:
    out_rows.append(
        {
            "task_id": NEXT_RQ,
            "title": "leftover dual after aPart — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "After aPart. Prefer AGB/FARO YE2025 else FREE ETA-VAPH-WZC-maatwerk "
                "(Manupal/Aralea/Vlotter/Gandae/De Ploeg/Het Eepos if YE2025). "
                "Do NOT redo aPart/Ritmica/Dominiek Savio/Merlijn/Humival/Heder/Kindervriend/Homevil/Maaat stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK} aPart; next EVERY-10 2330",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(out_rows)

with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
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
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": RQ,
            "ticks_completed": TICK,
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual aPart {KBO} Medium (omzet DROP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; "
                f"pnl DROP {PNL}; equity {EQUITY}; FTE JUMP {FTE}; 12 VE Gent jeugdhulp RSZ 87.991); "
                f"after Ritmica@2324; AGB Bornem JR2024; FARO/AIESH YE2024; next {NEXT_RQ}; next EVERY-10 2330; "
                "continuous hole_fill"
            ),
        }
    )

raw = ROOT / "raw" / f"tick{TICK}"
raw.mkdir(parents=True, exist_ok=True)
(raw / "summary.json").write_text(
    json.dumps(
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
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)
(raw / "cw_en_excerpt.txt").write_text(
    (
        f"aPart YE2025 CW EN verified 2026-08-24: omzet {OMZET} (-21.51%) bruto {BRUTO} (+5.19% ~{RATIO}x) "
        f"pnl {PNL} (-99.58%) equity {EQUITY} FTE {FTE} filed 24.06.2026\n"
        "https://www.companyweb.be/en/0567657460/apart\n"
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0567657460\n"
        "https://vzwapart.be/contacteer-ons\n"
    ),
    encoding="utf-8",
)

log_block = f"""
### 2026-08-24T16:20:00Z - tick {TICK} - {RQ} aPart Gent (bruto JUMP 8.79m / ~{RATIO}x omzet / pnl DROP -99.58% / Medium)

- Unit: **{RQ}** finish **in_progress** (SWITCH Het Eepos → **aPart**). Prefer NON-stall: AGB Bornem still **JR2024**; FARO/AIESH still **YE2024**. Took FREE Flemish jeugdhulp **aPart VZW** YE2025 (KBO **{KBO}**; Brandstraat 3 Gent; **Actief** **12 VE**; RSZ **87.991**). Do not redo Ritmica/Dominiek Savio/Merlijn/Humival/Heder stack. Also backfilled missing Ritmica CSV rows from incomplete tick2324 commit.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP -21.51%; bruto **EUR{BRUTO}** JUMP +5.19% (~**{RATIO}x**); pnl **EUR{PNL}** DROP -99.58%; equity **EUR{EQUITY}**; FTE **{FTE}**; neerlegging **24.06.2026**. Strong KBO Actief 12 VE. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/; ritmica CSV backfill.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next EVERY-10 2330**). Next: {NEXT_RQ}.
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("OK tick2325 aPart", RATIO, "x", PI)
