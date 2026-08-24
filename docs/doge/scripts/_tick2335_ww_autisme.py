# -*- coding: utf-8 -*-
from __future__ import annotations
import csv, json, sys, time
from pathlib import Path
csv.field_size_limit(sys.maxsize)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs/doge/data"
FOI = ROOT / "docs/doge/foi/drafts"
LOG = ROOT / "docs/doge/loop_log.md"
TICK = "2335"
RQ = "rq_2335"
RQ_NEXT = "rq_2336"
EID = "vzw_wonen_werken_autisme_pajottegem"
KBO = "0443.397.688"
KBO_NUM = "0443397688"
OMZET = 2488539
BRUTO = 13441120
PNL = 2326835
EQUITY = 14663706
FTE = 143.3
OMZET24 = 1881671
BRUTO24 = 10497948
PNL24 = 1088580
EQUITY24 = 12427489
FTE24 = 126.5
RATIO = round(BRUTO / OMZET, 2)
FILED = "09.07.2026"
ADDR = "Repingestraat 12, 1570 Pajottegem"
EMAIL = ""  # KBO email empty; postal FOI
SITE = "https://consult.cbso.nbb.be/consult-enterprise/0443397688"
GAP = "gap_ww_autisme_nbb_pdf_assets_debt_bruto_gt_omzet_5_40x_pnl_jump_vaph_matrix_l5"
UTC = "2026-08-24T18:05:00Z"
COST = 5.8
ABS = 7.2
DIFF = 6
PI = round(0.55 * COST + 0.35 * ABS + 0.10 * (10 - DIFF), 2)


def read_csv(path):
    for _ in range(25):
        try:
            with path.open(encoding="utf-8", newline="") as f:
                r = csv.DictReader(f)
                return list(r.fieldnames or []), list(r)
        except PermissionError:
            time.sleep(0.4)
    raise RuntimeError("read")


def atomic_write(path, fields, rows):
    tmp = path.with_suffix(".csv.__new__")
    bak = path.with_suffix(".csv.__bak__")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})
    for _ in range(40):
        try:
            if bak.exists():
                try:
                    bak.unlink()
                except Exception:
                    pass
            if path.exists():
                path.replace(bak)
            tmp.replace(path)
            try:
                if bak.exists():
                    bak.unlink()
            except Exception:
                pass
            return
        except PermissionError:
            time.sleep(0.5)
    raise RuntimeError("atomic")


def append_rows(path, new_rows, id_key=None):
    fields, rows = read_csv(path)
    have = {r.get(id_key) for r in rows} if id_key else set()
    for nr in new_rows:
        if id_key and nr.get(id_key) in have:
            continue
        rows.append(nr)
    atomic_write(path, fields, rows)


# claim
fields, rq = read_csv(DATA / "research_queue.csv")
for r in rq:
    if r.get("task_id") == RQ:
        eid = r.get("entity_id") or ""
        st = r.get("status")
        if st == "done" and eid and eid != EID:
            print("RACE done", eid)
            sys.exit(2)
        if st == "in_progress" and eid and eid != EID:
            print("RACE ip", eid)
            sys.exit(3)
        if st == "done" and eid == EID:
            print("already done self")
            sys.exit(0)
        r["status"] = "in_progress"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["notes"] = (r.get("notes") or "") + f"; tick{TICK} CLAIM WonenWerkenAutisme"
        atomic_write(DATA / "research_queue.csv", fields, rq)
        print("CLAIMED")
        break
else:
    print("missing")
    sys.exit(4)

src = "src_ww_autisme_jr2025_cw_en"
append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_ww_autisme_jr2025_cw_nl",
            "title": "Companyweb NL Wonen en Werken Autisme YE2025",
            "url": f"https://www.companyweb.be/nl/{KBO_NUM}/wonen-en-werken-voor-personen-met-autisme",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-24",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; omzet {OMZET} bruto {BRUTO} ~{RATIO}x pnl {PNL} equity {EQUITY} FTE {FTE}; filed {FILED}",
        },
        {
            "source_id": src,
            "title": "Companyweb EN Wonen en Werken Autisme YE2025",
            "url": f"https://www.companyweb.be/en/{KBO_NUM}/wonen-en-werken-voor-personen-met-autisme",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-24",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN Medium",
        },
        {
            "source_id": "src_ww_autisme_jr2025_cw_fr",
            "title": "Companyweb FR Wonen en Werken Autisme YE2025",
            "url": f"https://www.companyweb.be/fr/{KBO_NUM}/wonen-en-werken-voor-personen-met-autisme",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-24",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror",
        },
        {
            "source_id": f"src_ww_autisme_kbo_{TICK}",
            "title": f"KBO Wonen en Werken Autisme {KBO}",
            "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_NUM}",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-24",
            "source_class": "official_register",
            "notes": f"tick{TICK}; Strong KBO Actief 1 VE Aanbestedende; RSZ 87.202; BTW 87.201+87.202; email empty",
        },
        {
            "source_id": f"src_ww_autisme_nbb_{TICK}",
            "title": "NBB consult Wonen en Werken Autisme FOI path",
            "url": SITE,
            "publisher": "NBB CBSO",
            "accessed_date": "2026-08-24",
            "source_class": "foi_contact",
            "notes": f"tick{TICK}; postal {ADDR}; KBO email empty",
        },
    ],
    "source_id",
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_ww_autisme_omzet_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet YE2025 JUMP",
            "source_id": src,
            "confidence": "medium",
            "notes": f"tick{TICK}; +32.25% vs {OMZET24}",
        },
        {
            "budget_id": "bud_ww_autisme_bruto_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": f"CW statutory bruto_marge YE2025 ~{RATIO}x",
            "source_id": src,
            "confidence": "medium",
            "notes": f"tick{TICK}; +28.04% vs {BRUTO24}",
        },
        {
            "budget_id": "bud_ww_autisme_pnl_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst/verlies YE2025 JUMP",
            "source_id": src,
            "confidence": "medium",
            "notes": f"tick{TICK}; +113.75% vs {PNL24}",
        },
        {
            "budget_id": "bud_ww_autisme_equity_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen YE2025 JUMP",
            "source_id": src,
            "confidence": "medium",
            "notes": f"tick{TICK}; +17.99% vs {EQUITY24}",
        },
        {
            "budget_id": "bud_ww_autisme_fte_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW FTE {FTE}",
            "source_id": src,
            "confidence": "medium",
            "notes": f"tick{TICK}; FTE JUMP vs {FTE24}",
        },
    ],
    "budget_id",
)

cash = {
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
}
append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "comm_ww_autisme_jr2025_statutory_bruto_gt_omzet_5_40x_pnl_jump_vaph",
            "title": f"WonenWerken Autisme YE2025 leftover dual (omzet 2.49m / bruto 13.44m ~{RATIO}x / pnl JUMP / FTE 143.3 / Medium)",
            "entity_id": EID,
            "beneficiary": "personen met autisme Pajottegem / VAPH",
            "legal_basis": f"VZW Wonen en Werken voor personen met Autisme (KBO {KBO}; Actief; Aanbestedende; RSZ 87.202; 1 VE)",
            "decision_date": "2026-07-09",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(BRUTO),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": f"https://www.companyweb.be/en/{KBO_NUM}/wonen-en-werken-voor-personen-met-autisme",
            "stated_goal": "Residential care + work support autism VAPH",
            "cut_option": "Publish NBB PDF assets/debt; explain bruto~5.40x + pnl JUMP +113%",
            "source_id": src,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Pajottegem>WonenWerkenAutisme_VAPH>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; after GielsBos@2334; not TE-additive",
        }
    ],
    "commitment_id",
)

append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": "lb_ww_autisme_bruto_13_44m_omzet_2_49m_5_40x_pnl_jump_jr2025",
            "name": f"WonenWerken Autisme bruto 13.44m / omzet 2.49m ~{RATIO}x / pnl JUMP (YE2025 VAPH Pajottegem)",
            "level": "L5",
            "type": "vaph_residential_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Pajottegem>WonenWerkenAutisme>JR2025",
            "annual_cost_eur": str(BRUTO),
            "total_cost_eur": str(BRUTO),
            "tco_notes": f"CW omzet JUMP {OMZET}; bruto JUMP {BRUTO} (~{RATIO}x); pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; filed {FILED}",
            "confidence": "medium",
            "source_id": src,
            "beneficiaries": "persons with autism Pajottegem VAPH",
            "stated_goal": "Residential care + work autism",
            "measured_outcome": "Unknown assets/debt",
            "absurdity_score": str(ABS),
            "cost_score": str(COST),
            "difficulty": str(DIFF),
            "priority_index": str(PI),
            "cut_proposal": "FOI NBB PDF + bruto/omzet + VAPH matrix",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW + Strong KBO; AGB/FARO YE2024",
        }
    ],
    "item_id",
)

append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": EID,
            "name_nl": "Wonen en Werken voor personen met Autisme VZW (Pajottegem / VAPH)",
            "name_fr": "Wonen en Werken pour personnes avec autisme ASBL (Pajottegem / VAPH)",
            "name_en": "Living and Working for persons with Autism VZW (Pajottegem / VAPH)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": SITE,
            "foi_email": EMAIL,
            "foi_postal": ADDR,
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE Aanbestedende RSZ 87.202; omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; neerlegging {FILED}; FOI {GAP}; after GielsBos@2334; AGB/FARO YE2024; not TE-additive of 348bn",
        }
    ],
    "entity_id",
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Pajottegem>WonenWerkenAutisme>NBB_PDF",
            "entity_id": EID,
            "what_is_missing": f"NBB PDF YE2025 assets/debt/cash; why bruto EUR{BRUTO} ~{RATIO}x omzet EUR{OMZET}; pnl JUMP EUR{PNL} (+113.75%); VAPH matrix",
            "why_it_matters": f"Medium CW VAPH autism Pajottegem bruto~{RATIO}x omzet with pnl JUMP +113%; assets/debt unknown; KBO email empty",
            "priority": "8",
            "recipient_body": "Wonen en Werken voor personen met Autisme VZW",
            "recipient_email": EMAIL,
            "recipient_postal": ADDR,
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-24",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_ww_autisme_jr2025_statutory_bruto_gt_omzet_5_40x_pnl_jump_vaph",
            "linked_leaderboard_id": "lb_ww_autisme_bruto_13_44m_omzet_2_49m_5_40x_pnl_jump_jr2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; postal FOI",
        }
    ],
    "gap_id",
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Wonen en Werken Autisme (bruto~{RATIO}x / pnl JUMP)

**gap_id:** `{GAP}` · **status:** ready NOT sent · **tick:** {TICK}  
**entity:** Wonen en Werken voor personen met Autisme VZW — KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; RSZ **87.202**; 1 VE Aanbestedende)  
**recipient:** postal {ADDR} (KBO email empty)

## Brief
```text
Aan: Wonen en Werken voor personen met Autisme VZW
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 (KBO {KBO})

1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR{BRUTO} vs omzet EUR{OMZET} (~{RATIO}x).
3. Toelichting pnl JUMP EUR{PNL} (+113.75% vs YE2024 EUR{PNL24}).
4. VAPH-subsidy / PVB matrix vs FTE {FTE}.
5. Schulden LT/KT en liquiditeiten YE2025.

Ref: {GAP}
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

fields, rq = read_csv(DATA / "research_queue.csv")
for r in rq:
    if r.get("task_id") == RQ:
        if (r.get("entity_id") or "") not in ("", EID):
            print("RACE close", r.get("entity_id"))
            sys.exit(6)
        r["status"] = "done"
        r["entity_id"] = EID
        r["title"] = f"leftover dual — WonenWerken Autisme YE2025 Medium (bruto JUMP 13.44m / ~{RATIO}x omzet / pnl JUMP / FTE {FTE})"
        r["updated_utc"] = UTC
        r["notes"] = (
            f"tick{TICK}: WonenWerken Autisme {KBO} YE2025 Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; "
            f"pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; 1 VE Aanbestedende RSZ 87.202); "
            f"FOI {GAP} ready not sent; after GielsBos@2334; next EVERY-10 2340"
        )
if not any(r.get("task_id") == RQ_NEXT for r in rq):
    rq.append(
        {
            "task_id": RQ_NEXT,
            "title": "leftover dual after WonenWerken Autisme — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "After WonenWerken Autisme YE2025. Prefer AGB/FARO/AIESH/REW if YE2025 else FREE unused ETA-VAPH-WZC-maatwerk. Do NOT redo WonenWerken Autisme/GielsBos/Vier Notelaars/Mivalti/Den Brand/Tandem/Pleegzorg/Zonnelied stack.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK}; next EVERY-10 2340",
        }
    )
atomic_write(DATA / "research_queue.csv", fields, rq)

lsf, ls = read_csv(DATA / "loop_state.csv")
for r in ls:
    if r.get("state_id") == "main":
        r.update(
            {
                "last_tick_utc": UTC,
                "last_unit_id": RQ,
                "ticks_completed": TICK,
                "paused": "no",
                "mode": "continuous",
                "current_sprint": "hole_fill",
                "notes": (
                    f"tick{TICK} leftover dual WonenWerken Autisme {KBO} Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; "
                    f"pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; 1 VE Aanbestedende); after GielsBos@2334; "
                    f"AGB/FARO YE2024; next {RQ_NEXT}; next EVERY-10 2340"
                ),
            }
        )
atomic_write(DATA / "loop_state.csv", lsf, ls)

raw = DATA / "raw" / f"tick{TICK}"
raw.mkdir(parents=True, exist_ok=True)
(raw / "summary.json").write_text(
    json.dumps(
        {
            "tick": TICK,
            "unit": RQ,
            "entity": EID,
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
    ),
    encoding="utf-8",
)

with LOG.open("a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick {TICK} - {RQ} Wonen en Werken Autisme Pajottegem (bruto JUMP 13.44m / ~{RATIO}x omzet / pnl JUMP +113.75% / FTE JUMP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **GielsBos@2334**. Prefer NON-stall: AGB Bornem / FARO / AIESH / REW still **YE2024**. Took FREE Flemish VAPH **Wonen en Werken voor personen met Autisme VZW** YE2025 (KBO **{KBO}**; {ADDR}; **Actief** **1 VE** Aanbestedende; RSZ **87.202**). Do NOT redo GielsBos/Vier Notelaars/Mivalti/Den Brand/Tandem/Zonnelied.
- Found: CW NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +32.25%; bruto **EUR{BRUTO}** JUMP +28.04% (~**{RATIO}x**); pnl **EUR{PNL}** JUMP +113.75%; equity **EUR{EQUITY}** JUMP +17.99%; FTE **{FTE}** JUMP; neerlegging **{FILED}**. Strong KBO. Assets/debt Unknown. Medium. KBO email empty → postal FOI.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}; raw tick{TICK}/.
- FOI: **ready not sent**. NOT every-10 (next **2340**). Next: {RQ_NEXT}.
"""
    )
print(f"DONE {RQ} WonenWerkenAutisme bruto {BRUTO} ~{RATIO}x PI {PI}")
