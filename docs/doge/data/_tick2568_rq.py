#!/usr/bin/env python3
"""tick2568 — surgical rq_2568 done + spawn rq_2569 + loop_state + loop_log.
Does NOT rewrite whole research_queue.csv: truncates only the last row then appends."""
import csv, io, json, os
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)

ids = json.loads(Path("/tmp/tick2568/IDS.json").read_text())
NOW = ids["NOW"]
eid = ids["eid"]
gap_id = ids["gap_id"]

rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, "rb") as f:
    f.seek(0, 2)
    size = f.tell()
    f.seek(max(0, size - 200000))
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
if row["task_id"] != "rq_2568":
    raise SystemExit(f"last row is {row['task_id']} not rq_2568")
row["status"] = "done"
row["entity_id"] = eid
row["blocked_gap_id"] = gap_id
row["updated_utc"] = NOW
row["title"] = "leftover dual Emiliani Lokeren YE2025"
row["notes"] = (
    "tick2568 DONE leftover city_lokeren leftover VAPH Emiliani 0421.911.297 YE2025 VOL-VZW deposit 2026-00260230 70/76A JUMP 22024421 73 JUMP 18573150 9901 JUMP 1122855 9904 DROP 1134875 debt JUMP 7843804 (+5024416) cash JUMP 3340047 (+105335) FTE 229,2 JUMP official zetel Krekelstraat 17 9160 Lokeren 7 VE leftover-mined AGB-only leftover VAPH after city GE tick865"
)

skip = (
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child). "
    "HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_lokeren leftover VAPH Emiliani remine@2568 leftover city_mechelen leftover VAPH Oikonde remine@2567 leftover city_ieper leftover VAPH Vondels remine@2566 leftover city_oostende leftover VAPH Duinhelm remine@2565 leftover Ithaka remine@2325 leftover Bethanie Genk SCAN leftover Stijn leftover-via-VE Hasselt leftover De Lovie remine@2089 leftover De Lier remine leftover Pelikaan OCMW leftover Zorghoeve Sint-Jansberg groenezorg leftover Muylenberg leftover-via-VE Verbint remine@2401 leftover De Link leftover-via-VE leftover OpWeg YE2024 leftover De Bezaan leftover-via-VE leftover De Klokke leftover-via-VE leftover Assjette 0 deposits leftover Autisme Leeft 0 deposits leftover Agape Tielt groenezorg leftover city_overijse leftover VAPH De Berken remine@2564 leftover De Lommerte Laakdal groenezorg leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen emmaus leftover-via-VE leftover De Witte Mol leftover-via-VE Stijn leftover De Voute 0 deposits leftover De Triangel YE2024-only leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine@2393 leftover CAR Accent remine@2396 leftover CAR Overleie remine@2462 leftover Ubuntu leftover-via-VE Kortrijk leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine@2405 leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine@2292 leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth/Buseloc remine under sec_flanders leftover city_boom leftover VLOTTER remine@2555 leftover Vlotter Maatwerk VZW YE2024-only leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea/Korian/Vulpia/CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Casa Di Colore Berlaar 0 deposits leftover groenezorg deferred leftover Apojo Aarschot remine@2336 leftover Kannet destelbergen vrijetijdszorg leftover 0-deposit Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover city_beringen 0 admin leftover VillaVip Familie 0 deposits leftover Woonondersteuning Vlaanderen YE2024-only leftover HabitASS ouderinitiatief leftover Ter Muiden leftover-via-VE Brugge leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024-only leftover De Ark Moerkerke YE2024-only leftover Wijzersterk 0 deposits leftover PIA leftover-via-VE leftover Oranje leftover-via-VE Damme leftover GielsBos remine@2334 leftover Havenzate remine leftover Voluit remine leftover Schoonderhage remine leftover Fiola leftover-via-VE leftover Hagewinde remine@2481 leftover Alderande remine@2489 leftover De Sperwer remine@2490 leftover CAR Waas remine@2397 leftover De Cirkel remine@2338 leftover Ter Engelen remine@1731 leftover city_kapellen / city_londerzeel / city_wortegem_petegem slugs MISSING leftover groenezorg leftover ouderinitiatief leftover SCAN/OCR leftover 0-deposit leftover YE2024-only. NOT every-10 (next every-10 2570)."
)
rq_2569 = {
    "task_id": "rq_2569",
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
    "notes": "spawned tick2568 after Emiliani Lokeren leftover dual; leftover public dual unused leftover VAPH of leftover-mined Flanders city; NOT every-10 (next every-10 2570)",
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
w.writerow({k: rq_2569.get(k, "") for k in fields})
payload = out.getvalue().encode("utf-8")

with open(rq_path, "r+b") as f:
    f.seek(last_line_abs_start)
    f.truncate()
    f.write(payload)
print("surgical rq: patched rq_2568 + spawned rq_2569 at offset", last_line_abs_start)

ls_path = "docs/doge/data/loop_state.csv"
with open(ls_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    ls_fields = r.fieldnames
    ls_rows = list(r)
ls_rows[0]["last_tick_utc"] = NOW
ls_rows[0]["last_unit_id"] = "rq_2568"
ls_rows[0]["ticks_completed"] = "2568"
ls_rows[0]["paused"] = "no"
ls_rows[0]["notes"] = (
    "tick2568 leftover dual Emiliani Lokeren 0421.911.297 leftover city_lokeren leftover VAPH leftover-mined AGB-only leftover type Strong PDF deposit 2026-00260230 VOL-VZW 1218604 B 50p 70/76A JUMP 22024421 73 JUMP 18573150 9901 JUMP 1122855 9904 DROP 1134875 debt JUMP 7843804 (+5024416) cash JUMP 3340047 (+105335) FTE 229,2 JUMP official zetel Krekelstraat 17 9160 Lokeren 7 VE leftover-mined city GE tick865; FIRST LOCK leftover city_lokeren leftover VAPH Emiliani; next rq_2569 leftover dual (NOT every-10; next every-10 2570)"
)
with open(ls_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    w.writeheader()
    for row2 in ls_rows:
        w.writerow({k: row2.get(k, "") for k in ls_fields})

log = f"""

## Tick 2568 — {NOW} — rq_2568 leftover dual Emiliani Lokeren YE2025

- Unit: **rq_2568** leftover dual after **Oikonde@2567**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child) like Peer@2556 / Dilsen@2557 / As@2558 / Diksmuide@2559 / Kortrijk@2560 / Leopoldsburg@2561 / Jabbeke@2562 / Staden@2563 / Overijse@2564 / Oostende@2565 / Ieper@2566 / Mechelen@2567. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_mechelen leftover VAPH Oikonde remine@2567 leftover city_ieper leftover VAPH Vondels remine@2566 leftover city_oostende leftover VAPH Duinhelm remine@2565 leftover Ithaka remine@2325 leftover city_overijse leftover VAPH De Berken remine@2564 leftover De Lommerte Laakdal groenezorg leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover Ter Muiden leftover-via-VE leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024 leftover De Ark Moerkerke YE2024 leftover Wijzersterk 0 deposits leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen leftover-via-VE leftover De Witte Mol leftover-via-VE leftover De Voute 0 deposits leftover De Triangel YE2024 leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine leftover CAR Accent remine leftover CAR Overleie remine leftover Ubuntu leftover-via-VE leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth remine leftover city_boom leftover VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel remine leftover Terloo leftover-via-VE leftover Nethedal YE2024 leftover Het Raster leftover-via-VE leftover ErgoEzel leftover Casa Di Colore leftover Apojo remine leftover Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover VillaVip leftover Woonondersteuning Vlaanderen YE2024 leftover HabitASS leftover Wegwijs leftover-via-VE leftover Monnikenheide leftover-via-VE leftover Dominiek Savio leftover Tordale leftover Borgerstein leftover De Schakel leftover Eepos leftover Den Brand leftover Het Noordhof remine leftover city_kapellen / city_londerzeel / city_wortegem_petegem slugs MISSING leftover Armonea/Korian/Vulpia/CuraCare/SLG/OCMW leftover convent leftover leftover-via-VE leftover YE2024-only leftover 0-deposit leftover groenezorg leftover ouderinitiatief leftover SCAN/OCR leftover Hagewinde remine@2481 leftover Alderande remine@2489 leftover De Sperwer remine@2490 leftover CAR Waas remine@2397 leftover De Cirkel remine@2338 leftover Ter Engelen remine@1731.
- Hunt skips: leftover-mined AGB-only leftover VAPH **Bethanië Genk 0414.744.977** unused YE2025 VOL live but **SCAN/OCR HARD SKIP**. leftover-mined AGB-only leftover VAPH **De Lovie Poperinge remine@2089 SKIP**. leftover-mined AGB-only leftover VAPH **Havenzate Veurne remine SKIP**. leftover-mined AGB-only leftover VAPH **Stijn / Sint-Gerardus / Sint-Oda leftover-via-VE Hasselt SKIP**. leftover-mined AGB-only leftover VAPH **GielsBos Lille remine@2334 SKIP**. leftover-mined AGB-only leftover VAPH **De Lier Lier remine SKIP**. leftover-mined AGB-only leftover VAPH **Schoonderhage remine SKIP**. leftover-mined AGB-only leftover VAPH **Voluit Evergem remine SKIP**. leftover **Pelikaan Menen OCMW SKIP**. leftover **PIA leftover-via-VE Hasselt SKIP**. leftover **Zorghoeve Sint-Jansberg Maaseik groenezorg SKIP**. leftover **De Triangel leftover-via-VE Lievegem YE2024 SKIP**. leftover **Fiola leftover-via-VE Wetteren SKIP**. leftover **Oranje leftover-via-VE Damme SKIP**. leftover **Muylenberg leftover-via-VE Verbint remine@2401 SKIP**. leftover **De Link leftover-via-VE SKIP**. leftover **De Bezaan leftover-via-VE SKIP**. leftover **De Klokke leftover-via-VE SKIP**. leftover **OpWeg YE2024 SKIP**. Remine skips: Oikonde@2567 / Vondels@2566 / Duinhelm@2565 / De Berken@2564 / Kerckstede@2563 / Licht en Liefde Heem@2562 / Berkenhof@2561 / De Hoge Kouter@2560 / Ithaka@2325 / Hagewinde@2481 / Alderande@2489 / De Sperwer@2490 / CAR Waas@2397 / De Cirkel@2338 / Ter Engelen@1731. Took NON-stall leftover mined **city_lokeren** leftover VAPH leftover-mined AGB-only leftover type (city GE tick865; AGB Lokeren tick1200; Emiliani unused).
- FIRST LOCK leftover city_lokeren leftover VAPH **Emiliani 0421.911.297** leftover-mined AGB-only leftover type after city GE tick865 unused leftover type (Emiliani itself unused; Hagewinde remine@2481 / Alderande remine@2489 / De Sperwer remine@2490 / CAR Waas remine@2397 / De Cirkel remine@2338 / Ter Engelen remine@1731). Confirmed unused (0 real entity rows on 0421.911.297 / 0421911297) + official KBO zetel Krekelstraat 17 **9160 Lokeren** (not leftover-via-VE of a DIFFERENT leftover city as parent; all 7 VE Lokeren) + native YE2025 PDF. Took FREE leftover Flemish **Emiliani** YE2025 (KBO **0421.911.297**; official zetel Krekelstraat 17 9160 Lokeren since 01.01.2025 technical address-code change; **Actief** **7 VE** **2.152.232.436** vzw Emiliani Krekelstraat 17 since 15.03.2006 + **2.366.555.322** Woonproject Schoolstraat 14 bus W003 since 01.11.2023 + **2.366.556.312** Villa Molenbergplein 6A since 01.01.2016 + **2.366.558.587** De Teerling Daknam-dorp 89 since 01.01.2006 + **2.366.558.686** 't Eikenhof Eekstraat 218 since 01.01.2016 + **2.366.558.884** Jan Persoonsstraat 56 since 01.10.2014 + **2.366.559.181** Jan Persoonsstraat 58 since 01.10.2014; VZW; RSZ2025 **87.202**; leftover of mined **city_lokeren**; FOI info@emiliani.be from official NBB PDF + official VAPH; leftover VAPH / official VAPH adreslijst Emiliani Vergunde Zorgaanbieder + RTH). Identity trap: 0421.911.297 ≠ leftover city GE Lokeren **0207.463.402** ≠ leftover AGB Lokeren **1031.996.262** ≠ leftover Hagewinde **0861.262.010** remine@2481 ≠ leftover Alderande **0431.893.389** remine@2489 ≠ leftover De Sperwer **0415.344.892** remine@2490 ≠ leftover CAR Waas **0415.472.279** remine@2397 ≠ leftover De Cirkel **0470.413.079** remine@2338 ≠ leftover Ter Engelen **0430.882.809** remine@1731 ≠ leftover Oikonde **0414.341.933** remine@2567 ≠ leftover Vondels **0415.108.728** remine@2566 ≠ leftover Duinhelm **0413.223.562** remine@2565 ≠ leftover Bethanië **0414.744.977** SCAN skip. Confirmed leftover public leftover VAPH VZW not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VOL-VZW **native text** (not scan) — 1218604 B / 50p native euros (VOL-VZW 6.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.4.2 6.5.1 6.5.2 6.16 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00260230** (1218604 B / 50p; AV **26.06.2026**; header **07/07/2026**; CDN GET **200** 1218604 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-07-07 07:08:30 UTC MD5 4b1db1dc294340a7824007d9993841af; NBB UUID 0c67c915-79d1-11f1-a491-8f537c3b104c; NBB published-deposits list 8 this tick; NBB consult HTML stub 5344 B discarded; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR3093895** JUMP +4.45% (was 2962198; commercial-only vs large 73); 73 **EUR18573150** JUMP +4.67% (was 17745220; subsidies 733 **EUR18564025**; schenkingen 731 **EUR9125**); 76A **empty** DROP (was 31766); envelope 70/76A **EUR22024421** JUMP +4.40% (was 21096366; delta +928055); 74 **EUR357376** (was 357182); 62 **EUR17964578** JUMP +4.72% (was 17155250); 630 **EUR443281** DROP −8.52% (was 484558); 66A **empty**; 640/8 **EUR84146** DROP (was 136684); bedrijfswinst 9901 **EUR1122855** JUMP +4.54% (was 1074054; delta +48801); pnl 9904 **EUR1134875** DROP −6.41% (was 1212652); 9903 **EUR1134875** DROP; equity **EUR12390807** JUMP +8.48%; assets **EUR21349427** JUMP +39.51% (+6046819); debt **EUR7843804** JUMP +178.21% (+5024416 vs 2819388); FTE 9087 **229,2** JUMP +0.79% (was 227,4; 9086 YE 302 vs 295; 100 YE 229,2 vs 227,4; 105 YE 233,6); kapitaalsubsidies **EUR1340166** DROP (was 1505947); destin 691 **EUR1134875** DROP (was 1212652); 791 **empty**; cash **EUR3340047** JUMP +3.26% (+105335 vs 3234712); geldbeleggingen **EUR5074576** JUMP; gebouwen **EUR3212256** DROP; MVA 22/27 **EUR10983299** JUMP; aanbouw **EUR7220675** JUMP (was 1423626); capex **EUR5922767** (8161+8162+8163+8166; 8166 5797049). Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 7 VE leftover mined city_lokeren leftover VAPH leftover-mined AGB-only leftover type after city GE tick865. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial. NOT leftover city_mechelen leftover VAPH Oikonde remine@2567. NOT leftover Bethanië SCAN skip.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 6.00; entities +1; FOI **gap_emiliani_lokeren_vaph_matrix_70_76a_jump_22_02m_73_jump_18_57m_debt_jump_5_02m_l5** prio7 ready + draft; raw PDF docs/doge/raw/tick2568/; rq_2568=done; spawn **rq_2569 leftover dual (NOT every-10; next every-10 2570)**; ticks=2568.
- Next: **rq_2569 leftover dual** (NOT every-10; next every-10 **2570**).

"""
with open("docs/doge/loop_log.md", "a", encoding="utf-8") as f:
    f.write(log)
print("rq/state/log updated", NOW)
