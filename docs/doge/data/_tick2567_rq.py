#!/usr/bin/env python3
"""tick2567 — surgical rq_2567 done + spawn rq_2568 + loop_state + loop_log.
Does NOT rewrite whole research_queue.csv: truncates only the last row then appends."""
import csv, io, json, os
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)

ids = json.loads(Path("/tmp/tick2567/IDS.json").read_text())
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
if row["task_id"] != "rq_2567":
    raise SystemExit(f"last row is {row['task_id']} not rq_2567")
row["status"] = "done"
row["entity_id"] = eid
row["blocked_gap_id"] = gap_id
row["updated_utc"] = NOW
row["title"] = "leftover dual Oikonde Mechelen YE2025"
row["notes"] = (
    "tick2567 DONE leftover city_mechelen leftover VAPH Oikonde 0414.341.933 YE2025 VKT-VZW deposit 2026-00134362 bruto JUMP 2839493 73 JUMP 2931036 9901 JUMP 61595 cash JUMP 580801 (+131019) FTE 32,4 JUMP official zetel Colomastraat 36-38 2800 Mechelen 1 VE leftover-mined AGB-only leftover VAPH after city GE tick829"
)

skip = (
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child). "
    "HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_mechelen leftover VAPH Oikonde remine@2567 leftover city_ieper leftover VAPH Vondels remine@2566 leftover city_oostende leftover VAPH Duinhelm remine@2565 leftover Ithaka remine@2325 leftover Bethanie Genk SCAN leftover Stijn leftover-via-VE Hasselt leftover De Lovie remine@2089 leftover De Lier remine leftover Pelikaan OCMW leftover Zorghoeve Sint-Jansberg groenezorg leftover Muylenberg leftover-via-VE Verbint remine@2401 leftover De Link leftover-via-VE leftover OpWeg YE2024 leftover De Bezaan leftover-via-VE leftover De Klokke leftover-via-VE leftover Assjette 0 deposits leftover Autisme Leeft 0 deposits leftover Agape Tielt groenezorg leftover city_overijse leftover VAPH De Berken remine@2564 leftover De Lommerte Laakdal groenezorg leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen emmaus leftover-via-VE leftover De Witte Mol leftover-via-VE Stijn leftover De Voute 0 deposits leftover De Triangel YE2024-only leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine@2393 leftover CAR Accent remine@2396 leftover CAR Overleie remine@2462 leftover Ubuntu leftover-via-VE Kortrijk leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine@2405 leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine@2292 leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth/Buseloc remine under sec_flanders leftover city_boom leftover VLOTTER remine@2555 leftover Vlotter Maatwerk VZW YE2024-only leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea/Korian/Vulpia/CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Casa Di Colore Berlaar 0 deposits leftover groenezorg deferred leftover Apojo Aarschot remine@2336 leftover Kannet destelbergen vrijetijdszorg leftover 0-deposit Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover city_beringen 0 admin leftover VillaVip Familie 0 deposits leftover Woonondersteuning Vlaanderen YE2024-only leftover HabitASS ouderinitiatief leftover Ter Muiden leftover-via-VE Brugge leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024-only leftover De Ark Moerkerke YE2024-only leftover Wijzersterk 0 deposits leftover PIA leftover-via-VE leftover Oranje leftover-via-VE Damme leftover GielsBos remine@2334 leftover Havenzate remine leftover Voluit remine leftover Schoonderhage remine leftover Fiola leftover-via-VE. NOT every-10 (next every-10 2570)."
)
rq_2568 = {
    "task_id": "rq_2568",
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
    "notes": "spawned tick2567 after Oikonde Mechelen leftover dual; leftover public dual unused leftover VAPH of leftover-mined Flanders city; NOT every-10 (next every-10 2570)",
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
w.writerow({k: rq_2568.get(k, "") for k in fields})
payload = out.getvalue().encode("utf-8")

with open(rq_path, "r+b") as f:
    f.seek(last_line_abs_start)
    f.truncate()
    f.write(payload)
print("surgical rq: patched rq_2567 + spawned rq_2568 at offset", last_line_abs_start)

ls_path = "docs/doge/data/loop_state.csv"
with open(ls_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    ls_fields = r.fieldnames
    ls_rows = list(r)
ls_rows[0]["last_tick_utc"] = NOW
ls_rows[0]["last_unit_id"] = "rq_2567"
ls_rows[0]["ticks_completed"] = "2567"
ls_rows[0]["paused"] = "no"
ls_rows[0]["notes"] = (
    "tick2567 leftover dual Oikonde Mechelen 0414.341.933 leftover city_mechelen leftover VAPH leftover-mined AGB-only leftover type Strong PDF deposit 2026-00134362 VKT-VZW 55019 B 16p bruto JUMP 2839493 73 JUMP 2931036 9901 JUMP 61595 cash JUMP 580801 (+131019) FTE 32,4 JUMP official zetel Colomastraat 36-38 2800 Mechelen 1 VE leftover-mined city GE tick829; FIRST LOCK leftover city_mechelen leftover VAPH Oikonde; next rq_2568 leftover dual (NOT every-10; next every-10 2570)"
)
with open(ls_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    w.writeheader()
    for row2 in ls_rows:
        w.writerow({k: row2.get(k, "") for k in ls_fields})

log = f"""

## Tick 2567 — {NOW} — rq_2567 leftover dual Oikonde Mechelen YE2025

- Unit: **rq_2567** leftover dual after **Vondels@2566**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child) like Peer@2556 / Dilsen@2557 / As@2558 / Diksmuide@2559 / Kortrijk@2560 / Leopoldsburg@2561 / Jabbeke@2562 / Staden@2563 / Overijse@2564 / Oostende@2565 / Ieper@2566. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_ieper leftover VAPH Vondels remine@2566 leftover city_oostende leftover VAPH Duinhelm remine@2565 leftover Ithaka remine@2325 leftover city_overijse leftover VAPH De Berken remine@2564 leftover De Lommerte Laakdal groenezorg leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover Ter Muiden leftover-via-VE leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024 leftover De Ark Moerkerke YE2024 leftover Wijzersterk 0 deposits leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen leftover-via-VE leftover De Witte Mol leftover-via-VE leftover De Voute 0 deposits leftover De Triangel YE2024 leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine leftover CAR Accent remine leftover CAR Overleie remine leftover Ubuntu leftover-via-VE leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth remine leftover city_boom leftover VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel remine leftover Terloo leftover-via-VE leftover Nethedal YE2024 leftover Het Raster leftover-via-VE leftover ErgoEzel leftover Casa Di Colore leftover Apojo remine leftover Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover VillaVip leftover Woonondersteuning Vlaanderen YE2024 leftover HabitASS leftover Wegwijs leftover-via-VE leftover Monnikenheide leftover-via-VE leftover Dominiek Savio leftover Tordale leftover Borgerstein leftover De Schakel leftover Eepos leftover Den Brand leftover Het Noordhof remine leftover city_kapellen / city_londerzeel / city_wortegem_petegem slugs MISSING leftover Armonea/Korian/Vulpia/CuraCare/SLG/OCMW leftover convent leftover leftover-via-VE leftover YE2024-only leftover 0-deposit leftover groenezorg leftover ouderinitiatief.
- Hunt skips: leftover-mined AGB-only leftover VAPH **Bethanië Genk 0414.744.977** unused YE2025 VOL live but **SCAN/OCR HARD SKIP**. leftover-mined AGB-only leftover VAPH **De Lovie Poperinge remine@2089 SKIP**. leftover-mined AGB-only leftover VAPH **Havenzate Veurne remine SKIP**. leftover-mined AGB-only leftover VAPH **Stijn / Sint-Gerardus / Sint-Oda leftover-via-VE Hasselt SKIP**. leftover-mined AGB-only leftover VAPH **GielsBos Lille remine@2334 SKIP**. leftover-mined AGB-only leftover VAPH **De Lier Lier remine SKIP**. leftover-mined AGB-only leftover VAPH **Schoonderhage remine SKIP**. leftover-mined AGB-only leftover VAPH **Voluit Evergem remine SKIP**. leftover **Pelikaan Menen OCMW SKIP**. leftover **PIA leftover-via-VE Hasselt SKIP**. leftover **Zorghoeve Sint-Jansberg Maaseik groenezorg SKIP**. leftover **De Triangel leftover-via-VE Lievegem YE2024 SKIP**. leftover **Fiola leftover-via-VE Wetteren SKIP**. leftover **Oranje leftover-via-VE Damme SKIP**. leftover **Muylenberg leftover-via-VE Verbint remine@2401 SKIP**. leftover **De Link leftover-via-VE SKIP**. leftover **De Bezaan leftover-via-VE SKIP**. leftover **De Klokke leftover-via-VE SKIP**. leftover **OpWeg YE2024 SKIP**. Remine skips: Vondels@2566 / Duinhelm@2565 / De Berken@2564 / Kerckstede@2563 / Licht en Liefde Heem@2562 / Berkenhof@2561 / De Hoge Kouter@2560 / Ithaka@2325. Took NON-stall leftover mined **city_mechelen** leftover VAPH leftover-mined AGB-only leftover type (city GE tick829; AGB Energiepunt tick1162 + AGB SAM tick1173 + AGB MAC tick1270; Oikonde unused).
- FIRST LOCK leftover city_mechelen leftover VAPH **Oikonde 0414.341.933** leftover-mined AGB-only leftover type after city GE tick829 unused leftover type (Oikonde itself unused; Pardoes remine@2473). Confirmed unused (0 real entity rows on 0414.341.933 / 0414341933) + official KBO zetel Colomastraat 36-38 **2800 Mechelen** (not leftover-via-VE of a DIFFERENT leftover city as parent) + native YE2025 PDF. Took FREE leftover Flemish **Oikonde** YE2025 (KBO **0414.341.933**; official zetel Colomastraat 36-38 2800 Mechelen since 13.09.1996; **Actief** **1 VE** **2.200.731.149** oikonde mechelen vzw Colomastraat 36-38 since 26.07.2011; VZW; RSZ2025 **88.999**; leftover of mined **city_mechelen**; FOI info@oikonde.org from official VAPH + official KBO VE; leftover VAPH / official VAPH adreslijst Oikonde Vergunde Zorgaanbieder + RTH). Identity trap: 0414.341.933 ≠ leftover city GE Mechelen **0207.499.430** ≠ leftover AGB Energiepunt **0843.922.170** ≠ leftover AGB SAM **0871.106.718** ≠ leftover AGB MAC **0546.688.337** ≠ leftover Pardoes **0417.400.205** remine@2473 ≠ leftover Vondels **0415.108.728** remine@2566 ≠ leftover Duinhelm **0413.223.562** remine@2565 ≠ leftover Bethanië **0414.744.977** SCAN skip. Confirmed leftover public leftover VAPH VZW not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VKT-VZW **native text** (not scan) — 55019 B / 16p native euros (VKT-VZW 6.5 6.6 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00134362** (55019 B / 16p; AV **26.05.2026**; header **03/06/2026**; CDN GET **200** 55019 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-06-03 10:53:27 UTC MD5 0a132501c77691057c48fb022d854d57; NBB consult HTML stub 5344 B discarded; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR17651** JUMP +42.93% (was 12349; commercial-only vs large 73); 73 **EUR2931036** JUMP +9.32% (was 2681181); 76A **empty**; envelope bruto 9900 **EUR2839493** JUMP +9.53% (VKT envelope because 73 is the subsidy envelope and bruto >> omzet; was 2592486; delta +247007); 74 **not on VKT form**; 62 **EUR2696720** JUMP +8.46% (was 2486379); 630 **EUR59417** JUMP (was 58170); 66A **empty**; 640/8 **EUR21761** JUMP (was 19226); bedrijfswinst 9901 **EUR61595** JUMP +114.53% (was 28712; delta +32883); pnl 9904 **EUR64061** JUMP +150.89% (was 25534); 9903 **EUR64061** JUMP; equity **EUR1080752** JUMP +5.74%; assets **EUR1816621** JUMP +6.25%; debt **EUR735869** JUMP +7.01%; FTE 9087 **32,4** JUMP +2.86% (was 31,5; 100 YE 32,4 vs 31,5; 105 YE 33,3); kapitaalsubsidies **EUR20983** DROP (was 26411); destin 691 **EUR60857** JUMP (was 25534); 791 **empty**; cash **EUR580801** JUMP +29.13% (+131019 vs 449782); geldbeleggingen **empty** DROP (was 250000); gebouwen **EUR583308** DROP; MVA 22/27 **EUR1082251** JUMP; aanbouw **EUR473087** JUMP (was 136056); capex **EUR371907** (8169). Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_mechelen leftover VAPH leftover-mined AGB-only leftover type after city GE tick829. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial. NOT leftover city_ieper leftover VAPH Vondels remine@2566. NOT leftover Bethanië SCAN skip.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 5.50; entities +1; FOI **gap_oikonde_mechelen_vaph_matrix_bruto_jump_2_84m_73_jump_2_93m_9901_jump_62k_cash_jump_131k_l5** prio7 ready + draft; raw PDF docs/doge/raw/tick2567/; rq_2567=done; spawn **rq_2568 leftover dual (NOT every-10; next every-10 2570)**; ticks=2567.
- Next: **rq_2568 leftover dual** (NOT every-10; next every-10 **2570**).

"""
with open("docs/doge/loop_log.md", "a", encoding="utf-8") as f:
    f.write(log)
print("rq/state/log updated", NOW)
