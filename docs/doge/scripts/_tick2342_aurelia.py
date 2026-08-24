# -*- coding: utf-8 -*-
from __future__ import annotations
import csv, json, sys, time
from pathlib import Path
csv.field_size_limit(sys.maxsize)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs/doge/data"
FOI = ROOT / "docs/doge/foi/drafts"
LOG = ROOT / "docs/doge/loop_log.md"
TICK = "2342"
RQ = "rq_2342"
RQ_NEXT = "rq_2342"
EID = "vzw_aurelia_kortrijk"
KBO = "0878.745.863"
KBO_NUM = "0878745863"
OMZET = 6280971
BRUTO = 6339122
PNL = 142185
EQUITY = 1291057
FTE = 81.6
OMZET24 = 5966375
BRUTO24 = 6066864
PNL24 = 72650
EQUITY24 = 1148872
FTE24 = 82.4
RATIO = round(BRUTO / OMZET, 2)
FILED = "16.07.2026"
ADDR = "Budastraat 30, 8500 Kortrijk"
EMAIL = "receptie@h-hart.be"
SITE = "https://www.h-hart.be/hulpaanhuis"
GAP = "gap_aurelia_nbb_pdf_assets_debt_omzet_6_28m_pnl_jump_95pct_thuiszorg_matrix_l5"
UTC = "2026-08-24T19:00:00Z"
COST = 5.5
ABS = 4.5
DIFF = 5
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
            print("ALREADY done same")
            sys.exit(0)
        r["status"] = "in_progress"
        r["entity_id"] = EID
        r["hierarchy_target"] = "L5"
        r["updated_utc"] = UTC
        r["notes"] = (r.get("notes") or "") + f"; tick{TICK} CLAIM Aurelia"
        atomic_write(DATA / "research_queue.csv", fields, rq)
        print("CLAIMED", EID)
        break
else:
    print("missing", RQ)
    sys.exit(4)

_, ents = read_csv(DATA / "entities.csv")
if any(e.get("entity_id") == EID for e in ents):
    print("ALREADY mined", EID)
    sys.exit(5)

src = "src_aurelia_jr2025_cw_en"
append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_aurelia_jr2025_cw_nl",
            "title": "Companyweb NL Aurelia YE2025",
            "url": f"https://www.companyweb.be/nl/{KBO_NUM}/aurelia",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-24",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed {FILED}",
        },
        {
            "source_id": src,
            "title": "Companyweb EN Aurelia YE2025",
            "url": f"https://www.companyweb.be/en/{KBO_NUM}/aurelia",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-24",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN Medium",
        },
        {
            "source_id": "src_aurelia_jr2025_cw_fr",
            "title": "Companyweb FR Aurelia YE2025",
            "url": f"https://www.companyweb.be/fr/{KBO_NUM}/aurelia",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-24",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror",
        },
        {
            "source_id": f"src_aurelia_kbo_{TICK}",
            "title": f"KBO Aurelia {KBO}",
            "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_NUM}",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-24",
            "source_class": "official_register",
            "notes": f"tick{TICK}; Strong KBO Actief 2 VE RSZ 88.101; BTW 87.101 RVT + 56.112; seat Budastraat 30 + VE Waregem",
        },
        {
            "source_id": f"src_aurelia_site_{TICK}",
            "title": "Zorggroep Heilig Hart Thuiszorg Aurelia FOI",
            "url": SITE,
            "publisher": "Zorggroep Heilig Hart / Aurelia VZW",
            "accessed_date": "2026-08-24",
            "source_class": "foi_contact",
            "notes": f"tick{TICK}; {EMAIL}; also directie@h-hart.be / gezinszorg@h-hart.be; {ADDR}",
        },
    ],
    "source_id",
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_aurelia_omzet_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet YE2025 JUMP",
            "source_id": src,
            "confidence": "medium",
            "notes": f"tick{TICK}; +5.27% vs {OMZET24}",
        },
        {
            "budget_id": "bud_aurelia_bruto_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge YE2025 JUMP",
            "source_id": src,
            "confidence": "medium",
            "notes": f"tick{TICK}; +4.49% vs {BRUTO24}; bruto/omzet ~{RATIO}",
        },
        {
            "budget_id": "bud_aurelia_pnl_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst/verlies YE2025 JUMP +95.71%",
            "source_id": src,
            "confidence": "medium",
            "notes": f"tick{TICK}; JUMP vs {PNL24}",
        },
        {
            "budget_id": "bud_aurelia_equity_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen YE2025 JUMP",
            "source_id": src,
            "confidence": "medium",
            "notes": f"tick{TICK}; +12.38% vs {EQUITY24}",
        },
        {
            "budget_id": "bud_aurelia_fte_jr2025_statutory",
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW FTE {FTE} slight DROP",
            "source_id": src,
            "confidence": "medium",
            "notes": f"tick{TICK}; vs {FTE24}",
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
            "commitment_id": "comm_aurelia_jr2025_statutory_omzet_6_28m_pnl_jump_thuiszorg",
            "title": "Aurelia YE2025 leftover dual (omzet JUMP 6.28m / bruto 6.34m / pnl JUMP +95.71% / FTE 81.6 / Medium)",
            "entity_id": EID,
            "beneficiary": "Thuiszorg / bejaardenzorg clients Kortrijk-Waregem (Zorggroep Heilig Hart path)",
            "legal_basis": f"VZW Aurelia (KBO {KBO}; Actief; RSZ 88.101; BTW 87.101; 2 VE)",
            "decision_date": "2026-07-16",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": f"https://www.companyweb.be/en/{KBO_NUM}/aurelia",
            "stated_goal": "Home elderly care / thuiszorg (excl. nursing) + related services",
            "cut_option": "Publish NBB PDF assets/debt; explain pnl JUMP +95.71% at omzet 6.28m; Zorgkas/public subsidy matrix",
            "source_id": src,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Kortrijk>Aurelia_thuiszorg>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; after Eyckerheyde@2341; not TE-additive",
        }
    ],
    "commitment_id",
)

append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": "lb_aurelia_omzet_6_28m_pnl_jump_95pct_fte_81_jr2025",
            "name": "Aurelia omzet JUMP 6.28m / pnl JUMP +95.71% / FTE 81.6 (YE2025 thuiszorg Kortrijk)",
            "level": "L5",
            "type": "thuiszorg_vzw_statutory",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Kortrijk>Aurelia>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": f"CW omzet JUMP {OMZET}; bruto JUMP {BRUTO} (~{RATIO}x); pnl JUMP {PNL} (+95.71%); equity JUMP {EQUITY}; FTE {FTE}; filed {FILED}",
            "confidence": "medium",
            "source_id": src,
            "beneficiaries": "Home-care elderly clients Kortrijk/Waregem",
            "stated_goal": "Thuiszorg bejaardenzorg (Zorggroep Heilig Hart Aurelia)",
            "measured_outcome": "Unknown assets/debt",
            "absurdity_score": str(ABS),
            "cost_score": str(COST),
            "difficulty": str(DIFF),
            "priority_index": str(PI),
            "cut_proposal": "FOI NBB PDF + pnl JUMP path + Zorgkas/public subsidy matrix",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW + Strong KBO; AGB/FARO YE2024; after Eyckerheyde@2341",
        }
    ],
    "item_id",
)

append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": EID,
            "name_nl": "Aurelia VZW (Kortrijk / Zorggroep Heilig Hart thuiszorg)",
            "name_fr": "Aurelia ASBL (Courtrai / soins a domicile Heilig Hart)",
            "name_en": "Aurelia VZW (Kortrijk / Heilig Hart home elderly care)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": SITE,
            "foi_email": EMAIL,
            "foi_postal": ADDR,
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE RSZ 88.101; omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl JUMP {PNL} (+95.71%); equity JUMP {EQUITY}; FTE {FTE}; neerlegging {FILED}; FOI {GAP}; after Eyckerheyde@2341; AGB/FARO/Gandae/Aralea/Manupal/Vlotter YE2024",
        }
    ],
    "entity_id",
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Kortrijk>Aurelia>NBB_PDF",
            "entity_id": EID,
            "what_is_missing": f"NBB PDF YE2025 assets/debt/cash; why pnl JUMP EUR{PNL} (+95.71%) at omzet EUR{OMZET}; Zorgkas/public subsidy vs omzet split; FTE {FTE} vs YE2024 {FTE24}",
            "why_it_matters": "Medium CW Heilig Hart thuiszorg Aurelia omzet 6.28m with pnl nearly doubling; assets/debt unknown",
            "priority": "8",
            "recipient_body": "Aurelia VZW / Zorggroep Heilig Hart",
            "recipient_email": EMAIL,
            "recipient_postal": ADDR,
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-24",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_aurelia_jr2025_statutory_omzet_6_28m_pnl_jump_thuiszorg",
            "linked_leaderboard_id": "lb_aurelia_omzet_6_28m_pnl_jump_95pct_fte_81_jr2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready NOT sent; also directie@h-hart.be / gezinszorg@h-hart.be; Medium CW + Strong KBO",
        }
    ],
    "gap_id",
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft â€” Aurelia Kortrijk (omzet 6.28m / pnl JUMP +95.71%)

**gap_id:** `{GAP}` Â· **status:** ready NOT sent Â· **tick:** {TICK}  
**entity:** Aurelia VZW â€” KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; RSZ **88.101**; 2 VE; Zorggroep Heilig Hart thuiszorg)  
**recipient:** {EMAIL} Â· also directie@h-hart.be / gezinszorg@h-hart.be

## Brief
```text
Aan: Aurelia VZW / Zorggroep Heilig Hart via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 Aurelia (KBO {KBO})

1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting pnl JUMP EUR{PNL} (+95.71%) vs YE2024 EUR{PNL24} bij omzet EUR{OMZET}.
3. Zorgkas / publieke toelagen vs omzet YE2025.
4. FTE {FTE} vs YE2024 {FTE24}; split Kortrijk/Waregem.
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
        r["hierarchy_target"] = "L5"
        r["blocked_gap_id"] = GAP
        r["title"] = f"leftover dual â€” Aurelia YE2025 Medium (omzet JUMP 6.28m / pnl JUMP +95.71% / FTE {FTE})"
        r["updated_utc"] = UTC
        r["notes"] = (
            f"tick{TICK}: Aurelia {KBO} YE2025 Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO}; "
            f"pnl JUMP {PNL} +95.71%; equity JUMP {EQUITY}; FTE {FTE}; 2 VE RSZ 88.101); "
            f"FOI {GAP} ready not sent; after Eyckerheyde@2341; next EVERY-10 2350"
        )
if not any(r.get("task_id") == RQ_NEXT for r in rq):
    rq.append(
        {
            "task_id": RQ_NEXT,
            "title": "leftover dual after Aurelia â€” prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "After Aurelia YE2025. Prefer AGB Bornem/FARO/AIESH/REW/Citeco if YE2025 "
                "else FREE ETA-VAPH-WZC-maatwerk (Gandae/Aralea/Manupal/Vlotter if YE2025). "
                "Do NOT redo Aurelia/Eyckerheyde/Konekt/OZC Sint-Vincentius/De Cirkel/Wieltjesgracht/Apojo/"
                "WW Autisme/GielsBos/Vier Notelaars/Okkernoot stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK}; next EVERY-10 2350",
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
                    f"tick{TICK} leftover dual Aurelia {KBO} Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO}; "
                    f"pnl JUMP {PNL} +95.71%; equity JUMP {EQUITY}; FTE {FTE}; 2 VE RSZ 88.101); "
                    f"after Eyckerheyde@2341; AGB/FARO/Gandae/Aralea YE2024; next {RQ_NEXT}; next EVERY-10 2350"
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
### {UTC} â€” tick {TICK} â€” {RQ} Aurelia Kortrijk (omzet JUMP 6.28m / pnl JUMP +95.71% / FTE {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **Huize Eyckerheyde@2341**. Prefer NON-stall AGB/FARO/Gandae/Aralea/Manupal/Vlotter **YE2024**. Took preferred FREE Flemish thuiszorg **Aurelia VZW** YE2025 (KBO **{KBO}**; {ADDR}; **Actief** **2 VE**; RSZ **88.101**; Zorggroep Heilig Hart; {EMAIL}). Do NOT redo Eyckerheyde/Konekt/OZC/De Cirkel/Wieltjesgracht/Apojo stack.
- Found: CW NL+EN+FR YE2025 â€” omzet **EUR{OMZET}** JUMP +5.27%; bruto **EUR{BRUTO}** JUMP +4.49% (~**{RATIO}x**); pnl **EUR{PNL}** JUMP +95.71%; equity **EUR{EQUITY}** JUMP +12.38%; FTE **{FTE}** slight DROP; neerlegging **{FILED}**. Strong KBO. Assets/debt Unknown. Medium.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}; raw tick{TICK}/.
- FOI: **ready not sent**. NOT every-10 (last **2340**; next **2350**). Next: {RQ_NEXT}.
"""
    )
print(f"SUCCESS {RQ} Aurelia omzet {OMZET} pnl JUMP PI {PI}")

