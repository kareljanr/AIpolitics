#!/usr/bin/env python3
"""tick2575 — surgical rq_2575 done + spawn rq_2576 + loop_state + loop_log."""
import csv, io, json, os
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = Path(__file__).resolve().parents[3]
os.chdir(ROOT)

ids = json.loads(Path("/tmp/tick2575/IDS.json").read_text())
NOW = ids["NOW"]
eid = ids["eid"]
gap_id = ids["gap_id"]

rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, "rb") as f:
    f.seek(0, 2)
    size = f.tell()
    f.seek(max(0, size - 400000))
    tail = f.read()
if tail.endswith(b"\n"):
    tail_body = tail[:-1]
    end_nl = True
else:
    tail_body = tail
    end_nl = False
last_nl = tail_body.rfind(b"\n")
if last_nl < 0:
    raise SystemExit("cannot find last row start")
last_line = tail_body[last_nl + 1 :]
if end_nl:
    last_line_abs_start = size - 1 - len(last_line)
else:
    last_line_abs_start = size - len(last_line)
header = "task_id,title,sprint,priority,status,hierarchy_target,entity_id,instructions,blocked_gap_id,created_utc,updated_utc,notes"
buf = io.StringIO(header + "\n" + last_line.decode("utf-8"))
r = csv.DictReader(buf)
row = next(r)
if row["task_id"] != "rq_2575":
    raise SystemExit(f"last row is {row['task_id']} not rq_2575")
row["status"] = "done"
row["entity_id"] = eid
row["blocked_gap_id"] = gap_id
row["updated_utc"] = NOW
row["title"] = "leftover dual Mekanders Turnhout YE2025"
row["notes"] = (
    "tick2575 DONE leftover city_turnhout leftover VAPH Mekanders 0431.176.975 YE2025 VOL-VZW deposit 2026-00263425 70/76A JUMP 13896468 733 11456564 9901 DROP 232982 cash JUMP 6135757 FTE 146,8 FLAT official zetel Steenweg op Oosthoven 25 2300 Turnhout 11 VE leftover-mined AGB leftover VAPH after city GE tick844"
)

skip = (
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child). "
    "HARD SKIP leftover city_turnhout leftover VAPH Mekanders remine@2575 leftover city_machelen leftover VAPH Klim remine@2574 leftover city_damme leftover VAPH De Ark Moerkerke-Brugge remine@2573 leftover Oranje Damme leftover-via-VE leftover city_lennik leftover VAPH Levenslust remine@2572 leftover city_heist_op_den_berg leftover VAPH Nethedal remine@2571 leftover city_tielt_winge leftover VAPH Het Balanske remine@2570 leftover Eyckenborgh Gooik WZC/Gravenkasteel not VAPH leftover Zwart Goor Merksplas Klavier=Emmaus leftover OC Cirkant Zedelgem leftover-via-VE Evara/Broeders van Liefde Gent leftover Clara Fey Brecht leftover-via-VE Evara leftover De Witte Mol leftover-via-VE Stijn leftover DPA Zonhoven leftover-via-VE Stijn leftover Muylenberg leftover-via-VE Verbint remine@2401 leftover Mok Lochristi 0 deposits leftover Woonondersteuning Vlaanderen YE2024 leftover De Triangel YE2024 leftover Nektari remine leftover Nido Brussels leftover Ebergiste/Sint-Ferdinand leftover-via-VE Evara leftover city_kapellen / city_londerzeel / city_wortegem_petegem slugs MISSING leftover Bethanie SCAN leftover Voluit remine leftover VillaVip 0 leftover Armonea/Korian/Vulpia leftover OCMW leftover convent leftover leftover-via-VE of a DIFFERENT leftover city as parent leftover groenezorg leftover ouderinitiatief leftover YE2024-only leftover 0-deposit leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda leftover city_oud_heverlee leftover WZC De Kouter Korian. Continue VAPH list scan (2575 scanned pages 5,6,12-14,20-22; pages 8,10,11,15-19 still thin). NOT every-10 (next every-10 2580)."
)
rq_2576 = {
    "task_id": "rq_2576",
    "title": "leftover dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "sprint": "hole_fill",
    "priority": "8",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": skip,
    "blocked_gap_id": "",
    "created_utc": NOW,
    "updated_utc": NOW,
    "notes": "spawned tick2575 after Mekanders Turnhout leftover dual; leftover public dual unused leftover VAPH of leftover-mined Flanders city; continue VAPH list scan; NOT every-10 (next every-10 2580)",
}

fields = [
    "task_id",
    "title",
    "sprint",
    "priority",
    "status",
    "hierarchy_target",
    "entity_id",
    "instructions",
    "blocked_gap_id",
    "created_utc",
    "updated_utc",
    "notes",
]
out = io.StringIO()
w = csv.DictWriter(out, fieldnames=fields, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
w.writerow({k: row.get(k, "") for k in fields})
w.writerow({k: rq_2576.get(k, "") for k in fields})
payload = out.getvalue().encode("utf-8")

with open(rq_path, "r+b") as f:
    f.seek(last_line_abs_start)
    f.truncate()
    f.write(payload)
print("surgical rq: patched rq_2575 + spawned rq_2576 at offset", last_line_abs_start)

ls_path = "docs/doge/data/loop_state.csv"
with open(ls_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    ls_fields = r.fieldnames
    ls_rows = list(r)
ls_rows[0]["last_tick_utc"] = NOW
ls_rows[0]["last_unit_id"] = "rq_2575"
ls_rows[0]["ticks_completed"] = "2575"
ls_rows[0]["paused"] = "no"
ls_rows[0]["notes"] = (
    "tick2575 leftover dual FRESH HUNT Mekanders Turnhout 0431.176.975 Strong PDF deposit 2026-00263425 VOL-VZW 241491 B 42p 70/76A JUMP 13896468 733 11456564 62 JUMP 11181965 9901 DROP 232982 9904 JUMP 609540 cash JUMP 6135757 termijnrekeningen DROP 0 from 5364549; next rq_2576 continue VAPH list scan"
)
with open(ls_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    w.writeheader()
    for row2 in ls_rows:
        w.writerow({k: row2.get(k, "") for k in ls_fields})

log = f"""

## Tick 2575 — {NOW} — rq_2575 leftover dual Mekanders Turnhout YE2025 (fresh hunt)

- Hunt: continued VAPH address list (Vergunde Zorgaanbieder filter; unscanned pages 5,6,12-14,20-22 live 200) against leftover-mined AGB/OCMW-only and GE-empty Flanders cities → **Mekanders, Steenweg op Oosthoven 25 2300 Turnhout**; city_turnhout had AGB tick1133 + Verbint CAR remine@2401 + Orion + Kinderopvang, no VAPH VZA child; KBO **0431.176.975** had 0 prior repo rows. AGB-only stalls this tick: OC Cirkant Zedelgem leftover-via-VE Evara/Broeders van Liefde Gent; Clara Fey Brecht leftover-via-VE Evara; DPA Zonhoven leftover-via-VE Stijn; Muylenberg leftover-via-VE Verbint remine@2401; Nektari already child of city_puurs_sint_amands; Nido Brussels. GE stalls: De Witte Mol leftover-via-VE Stijn; Mok Lochristi 0 deposits; Woonondersteuning Vlaanderen YE2024; De Triangel YE2024; Ebergiste/Sint-Ferdinand leftover-via-VE Evara.
- KBO: Actief since 24.06.1985; VZW; zetel Steenweg op Oosthoven 25 2300 Turnhout since 15.06.2021; 11 VE (Turnhout ×3 + Arendonk ×3 + Merksplas + Ravels + Dessel + Hoogstraten + Oud-Turnhout); RSZ2025 88.999 andere maatschappelijke dienstverlening zonder huisvesting. Site mekanders.be: kleinschalige woonhuizen/dagcentra Noorderkempen; VAPH Vergunde Zorgaanbieder + RTH + MFC.
- Found: official NBB VOL-VZW native PDF **2026-00263425** (241491 B / 42p; AV 16-06-2026; neergelegd 01/07/2026; MD5 f9feae6b23d06974c0dda22cea45b71b; OpenPDF 1.3.26 CreationDate 2026-07-07 23:18:41 UTC; prior-year RESTATED; broker PDF). 70/76A **EUR13896468** JUMP +2.93% (was restated 13501189); 733 subsidies **EUR11456564** (was restated 793415; jaarverslag: VAPH-afrekeningen 2024-2025 now in result); 73 11682593; omzet70 DROP 1779637 (was restated 11840608); 62 **EUR11181965** JUMP +5.91%; 9901 **EUR232982** DROP −34.29% (was 354568); 9904 **EUR609540** JUMP +17.47% (fin 75/76B 401900); equity 11208352 (kapitaalsubsidies 3640041); assets 14493444; debt DROP 2881949; cash **EUR6135757** JUMP +610.19% after termijnrekeningen 53 DROP 0 from 5364549; capex 930409 (aanbouw 738750 Goriën Dessel + Beukenhof Turnhout); FTE 146,8 FLAT (was 146,6).
- Wrote: sources +4; budgets +12; commitments +1; leaderboard +1 pi 5.50; entities +1 (parent city_turnhout); FOI **gap_mekanders_turnhout_vaph_matrix_70_76a_13_90m_733_11_46m_cash_jump_6_14m_l5** prio6 ready (NOT sent) + draft; raw PDF+txt+KBO+VE+deposits+VAPH+site docs/doge/raw/tick2575/; rq_2575=done; spawn **rq_2576**; ticks=2575.
- Next: **rq_2576 leftover dual** — continue VAPH list scan (NOT every-10; next every-10 2580).
"""
with open("docs/doge/loop_log.md", "a", encoding="utf-8") as f:
    f.write(log)
print("rq/state/log updated", NOW)
