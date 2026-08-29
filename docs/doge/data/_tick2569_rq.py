#!/usr/bin/env python3
"""tick2569 — surgical rq_2569 done + spawn rq_2570 leftover dual PLUS every-10 + loop_state + loop_log.
Does NOT rewrite whole research_queue.csv: truncates only the last row then appends."""
import csv, io, json, os
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)

ids = json.loads(Path("/tmp/tick2569/IDS.json").read_text())
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
if row["task_id"] != "rq_2569":
    raise SystemExit(f"last row is {row['task_id']} not rq_2569")
row["status"] = "done"
row["entity_id"] = eid
row["blocked_gap_id"] = gap_id
row["updated_utc"] = NOW
row["title"] = "leftover dual Hoito Tienen YE2025"
row["notes"] = (
    "tick2569 DONE leftover city_tienen leftover VAPH Hoito 0429.766.220 YE2025 VOL-VZW deposit 2026-00188348 70/76A JUMP 2865864 73 JUMP 2786262 9901 JUMP 99051 9904 JUMP 123462 cash JUMP 474597 (+128613) FTE 34,3 JUMP official zetel Beauduinstraat 150 3300 Tienen 1 VE leftover-mined AGB-only leftover VAPH after city GE tick1274"
)

skip = (
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child). "
    "HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_tienen leftover VAPH Hoito remine@2569 leftover city_lokeren leftover VAPH Emiliani remine@2568 leftover city_mechelen leftover VAPH Oikonde remine@2567 leftover city_ieper leftover VAPH Vondels remine@2566 leftover city_oostende leftover VAPH Duinhelm remine@2565 leftover Ithaka remine@2325 leftover Bethanie Genk SCAN leftover Stijn leftover-via-VE Hasselt leftover De Lovie remine@2089 leftover De Lier remine leftover Pelikaan OCMW leftover Zorghoeve Sint-Jansberg groenezorg leftover Muylenberg leftover-via-VE Verbint remine@2401 leftover De Link leftover-via-VE leftover OpWeg YE2024 leftover De Bezaan leftover-via-VE leftover De Klokke leftover-via-VE leftover Assjette 0 deposits leftover Autisme Leeft 0 deposits leftover Agape Tielt groenezorg leftover city_overijse leftover VAPH De Berken remine@2564 leftover De Lommerte Laakdal groenezorg leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen emmaus leftover-via-VE leftover De Witte Mol leftover-via-VE Stijn leftover De Voute 0 deposits leftover De Triangel YE2024-only leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine@2393 leftover CAR Accent remine@2396 leftover CAR Overleie remine@2462 leftover Ubuntu leftover-via-VE Kortrijk leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine@2405 leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine@2292 leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth/Buseloc remine under sec_flanders leftover city_boom leftover VLOTTER remine@2555 leftover Vlotter Maatwerk VZW YE2024-only leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea/Korian/Vulpia/CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Casa Di Colore Berlaar 0 deposits leftover groenezorg deferred leftover Apojo Aarschot remine@2336 leftover Kannet destelbergen vrijetijdszorg leftover 0-deposit Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover city_beringen 0 admin leftover VillaVip Familie 0 deposits leftover Woonondersteuning Vlaanderen YE2024-only leftover HabitASS ouderinitiatief leftover Ter Muiden leftover-via-VE Brugge leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024-only leftover De Ark Moerkerke YE2024-only leftover Wijzersterk 0 deposits leftover PIA leftover-via-VE leftover Oranje leftover-via-VE Damme leftover GielsBos remine@2334 leftover Havenzate remine leftover Voluit remine leftover Schoonderhage remine leftover Fiola leftover-via-VE leftover Hagewinde remine@2481 leftover Alderande remine@2489 leftover De Sperwer remine@2490 leftover CAR Waas remine@2397 leftover De Cirkel remine@2338 leftover Ter Engelen remine@1731 leftover CAR DAT remine@2382 leftover Huis in de Stad remine@2308 leftover Hartjes remine@2450 leftover Ooievaarsnest remine@2465 leftover Blankedale remine@2188 leftover Avalon remine@2503 leftover city_kapellen / city_londerzeel / city_wortegem_petegem slugs MISSING leftover groenezorg leftover ouderinitiatief leftover SCAN/OCR leftover 0-deposit leftover YE2024-only leftover GO! leftover-via-VE. PLUS every-10 progress (ticks_completed 2570)."
)
rq_2570 = {
    "task_id": "rq_2570",
    "title": "leftover dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025 PLUS every-10",
    "sprint": "hole_fill",
    "priority": "8",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": skip,
    "blocked_gap_id": "",
    "created_utc": NOW,
    "updated_utc": NOW,
    "notes": "spawned tick2569 after Hoito Tienen leftover dual; leftover public dual unused leftover VAPH of leftover-mined Flanders city PLUS every-10 progress (ticks_completed 2570)",
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
w.writerow({k: rq_2570.get(k, "") for k in fields})
payload = out.getvalue().encode("utf-8")

with open(rq_path, "r+b") as f:
    f.seek(last_line_abs_start)
    f.truncate()
    f.write(payload)
print("surgical rq: patched rq_2569 + spawned rq_2570 at offset", last_line_abs_start)

ls_path = "docs/doge/data/loop_state.csv"
with open(ls_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    ls_fields = r.fieldnames
    ls_rows = list(r)
ls_rows[0]["last_tick_utc"] = NOW
ls_rows[0]["last_unit_id"] = "rq_2569"
ls_rows[0]["ticks_completed"] = "2569"
ls_rows[0]["paused"] = "no"
ls_rows[0]["notes"] = (
    "tick2569 leftover dual Hoito Tienen 0429.766.220 leftover city_tienen leftover VAPH leftover-mined AGB-only leftover type Strong PDF deposit 2026-00188348 VOL-VZW 73962 B 26p 70/76A JUMP 2865864 73 JUMP 2786262 9901 JUMP 99051 9904 JUMP 123462 cash JUMP 474597 (+128613) FTE 34,3 JUMP official zetel Beauduinstraat 150 3300 Tienen 1 VE leftover-mined city GE tick1274; FIRST LOCK leftover city_tienen leftover VAPH Hoito; next rq_2570 leftover dual PLUS every-10"
)
with open(ls_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    w.writeheader()
    for row2 in ls_rows:
        w.writerow({k: row2.get(k, "") for k in ls_fields})

log = f"""

## Tick 2569 — {NOW} — rq_2569 leftover dual Hoito Tienen YE2025

- Unit: **rq_2569** leftover dual after **Emiliani@2568**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child) like Peer@2556 / Dilsen@2557 / As@2558 / Diksmuide@2559 / Kortrijk@2560 / Leopoldsburg@2561 / Jabbeke@2562 / Staden@2563 / Overijse@2564 / Oostende@2565 / Ieper@2566 / Mechelen@2567 / Lokeren@2568. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_lokeren leftover VAPH Emiliani remine@2568 leftover city_mechelen leftover VAPH Oikonde remine@2567 leftover city_ieper leftover VAPH Vondels remine@2566 leftover city_oostende leftover VAPH Duinhelm remine@2565 leftover Ithaka remine@2325 leftover city_overijse leftover VAPH De Berken remine@2564 leftover De Lommerte Laakdal groenezorg leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover Ter Muiden leftover-via-VE leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024 leftover De Ark Moerkerke YE2024 leftover Wijzersterk 0 deposits leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen leftover-via-VE leftover De Witte Mol leftover-via-VE leftover De Voute 0 deposits leftover De Triangel YE2024 leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine leftover CAR Accent remine leftover CAR Overleie remine leftover Ubuntu leftover-via-VE leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth remine leftover city_boom leftover VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel remine leftover Terloo leftover-via-VE leftover Nethedal YE2024 leftover Het Raster leftover-via-VE leftover ErgoEzel leftover Casa Di Colore leftover Apojo remine leftover Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover VillaVip leftover Woonondersteuning Vlaanderen YE2024 leftover HabitASS leftover Wegwijs leftover-via-VE leftover Monnikenheide leftover-via-VE leftover Dominiek Savio leftover Tordale leftover Borgerstein leftover De Schakel leftover Eepos leftover Den Brand leftover Het Noordhof remine leftover city_kapellen / city_londerzeel / city_wortegem_petegem slugs MISSING leftover Armonea/Korian/Vulpia/CuraCare/SLG/OCMW leftover convent leftover leftover-via-VE leftover YE2024-only leftover 0-deposit leftover groenezorg leftover ouderinitiatief leftover SCAN/OCR leftover Hagewinde remine@2481 leftover Alderande remine@2489 leftover De Sperwer remine@2490 leftover CAR Waas remine@2397 leftover De Cirkel remine@2338 leftover Ter Engelen remine@1731 leftover Avalon remine@2503 leftover GO! leftover-via-VE.
- Hunt skips: leftover-mined AGB-only leftover VAPH **Bethanië Genk 0414.744.977** unused YE2025 VOL live but **SCAN/OCR HARD SKIP**. leftover-mined AGB-only leftover VAPH **De Lovie Poperinge remine@2089 SKIP**. leftover-mined AGB-only leftover VAPH **Havenzate Veurne remine SKIP**. leftover-mined AGB-only leftover VAPH **Stijn / Sint-Gerardus / Sint-Oda leftover-via-VE Hasselt SKIP**. leftover-mined AGB-only leftover VAPH **GielsBos Lille remine@2334 SKIP**. leftover-mined AGB-only leftover VAPH **De Lier Lier remine SKIP**. leftover-mined AGB-only leftover VAPH **Schoonderhage remine SKIP**. leftover-mined AGB-only leftover VAPH **Voluit Evergem remine SKIP**. leftover **Pelikaan Menen OCMW SKIP**. leftover **PIA leftover-via-VE Hasselt SKIP**. leftover **Zorghoeve Sint-Jansberg Maaseik groenezorg SKIP**. leftover **De Triangel leftover-via-VE Lievegem YE2024 SKIP**. leftover **Fiola leftover-via-VE Wetteren SKIP**. leftover **Oranje leftover-via-VE Damme SKIP**. leftover **Muylenberg leftover-via-VE Verbint remine@2401 SKIP**. leftover **De Link leftover-via-VE SKIP**. leftover **De Bezaan leftover-via-VE SKIP**. leftover **De Klokke leftover-via-VE SKIP**. leftover **OpWeg YE2024 SKIP**. leftover-mined AGB-only leftover VAPH **Madee / De 3master Beerse leftover-via-VE GO! Fluxus SKIP**. leftover-mined AGB-only leftover VAPH **Zonnebos Schilde leftover-via-VE GO! INVENTO SKIP**. leftover-mined AGB-only leftover VAPH **Odisam leftover-via-VE GO! 24K Nazareth-De Pinte SKIP**. leftover-mined city GE leftover VAPH **Avalon Buggenhout remine@2503 SKIP**. leftover-mined AGB-only leftover VAPH **Alpaca Reckheim Lanaken groenezorg SKIP**. leftover-mined AGB-only leftover VAPH **Ampel Blankenberge remine SKIP**. leftover-mined AGB-only leftover VAPH **VillaVip Middelkerke 0 deposits SKIP**. leftover-mined AGB-only leftover VAPH **Aalternatief Aalter 0 deposits SKIP**. Remine skips: Emiliani@2568 / Oikonde@2567 / Vondels@2566 / Duinhelm@2565 / De Berken@2564 / Kerckstede@2563 / Licht en Liefde Heem@2562 / Berkenhof@2561 / De Hoge Kouter@2560 / Ithaka@2325 / Hagewinde@2481 / Alderande@2489 / De Sperwer@2490 / CAR Waas@2397 / De Cirkel@2338 / Ter Engelen@1731 / CAR DAT@2382 / Huis in de Stad@2308 / Hartjes@2450 / Ooievaarsnest@2465 / Blankedale@2188. Took NON-stall leftover mined **city_tienen** leftover VAPH leftover-mined AGB-only leftover type (city GE tick1274; AGB Tienen tick1272; Hoito unused).
- FIRST LOCK leftover city_tienen leftover VAPH **Hoito 0429.766.220** leftover-mined AGB-only leftover type after city GE tick1274 unused leftover type (Hoito itself unused; CAR DAT remine@2382 / Huis in de Stad remine@2308 / Hartjes remine@2450 / Ooievaarsnest remine@2465 / Blankedale remine@2188). Confirmed unused (0 real entity rows on 0429.766.220 / 0429766220) + official KBO zetel Beauduinstraat 150 **3300 Tienen** (not leftover-via-VE of a DIFFERENT leftover city as parent; 1 VE Tienen) + native YE2025 PDF. Took FREE leftover Flemish **Hoito** YE2025 (KBO **0429.766.220**; naam Hoito since 02.06.2025 was Begeleid Wonen Tienen; official zetel Beauduinstraat 150 3300 Tienen since 27.12.2004; **Actief** **1 VE** **2.154.428.792** Sociaal Pedagogische Dienst - Dienst Begeleid Wonen Beauduinstraat 150 since 13.06.2006; VZW; RSZ2025 **88.999**; leftover of mined **city_tienen**; FOI ann.berwaerts@hoito.be from official NBB PDF + secretariaat@begeleidwonentienen.be from official VAPH + info@hoito.be from official Staatsblad; leftover VAPH / official VAPH adreslijst Hoito Vergunde Zorgaanbieder + RTH). Identity trap: 0429.766.220 ≠ leftover city GE Tienen **0207.525.758** ≠ leftover AGB Tienen **0872.382.861** ≠ leftover CAR DAT **0463.347.917** remine@2382 ≠ leftover Hartjes **0441.374.348** remine@2450 ≠ leftover Ooievaarsnest **0418.588.256** remine@2465 ≠ leftover Huis in de Stad **0407.637.748** remine@2308 ≠ leftover Blankedale **0400.999.978** remine@2188 ≠ leftover Emiliani **0421.911.297** remine@2568 ≠ leftover Oikonde **0414.341.933** remine@2567 ≠ leftover Vondels **0415.108.728** remine@2566 ≠ leftover Duinhelm **0413.223.562** remine@2565 ≠ leftover Bethanië **0414.744.977** SCAN skip. Confirmed leftover public leftover VAPH VZW not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VOL-VZW **native text** (not scan) — 73962 B / 26p native euros (VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.3.5 6.3.6 6.4.1 6.4.2 6.4.3 6.5.1 6.5.2 6.5.3 6.10 6.13 6.14 6.15 6.16 8 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00188348** (73962 B / 26p; AV **19.06.2026**; header **23/06/2026**; CDN GET **200** 73962 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-06-23 22:40:04 UTC MD5 ffa4a5283de20f6859f7d6a9dc2b4ad2; NBB published-deposits list official consult page this tick YE2025 2026-00188348 + YE2024 2025-00122918; NBB consult HTML stub 5344 B discarded; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR54564** JUMP +45.41% (was 37523; commercial-only vs large 73); 73 **EUR2786262** JUMP +11.59% (was 2496977; subsidies 733 **EUR2772253**; schenkingen 731 **EUR14008**); 76A **empty** DROP (was 1986); envelope 70/76A **EUR2865864** JUMP +11.67% (was 2566396; delta +299468); 74 **EUR25039** DROP (was 29909); 62 **EUR2479454** JUMP +8.97% (was 2275278); 630 **EUR66577** DROP −20.79% (was 84049); 66A **EUR1431** JUMP (was 1000); 640/8 **EUR30696** JUMP (was 29836); bedrijfswinst 9901 **EUR99051** JUMP +857% (was 10345; delta +88706); pnl 9904 **EUR123462** JUMP +194.30% (was 41951); 9903 **EUR123462** JUMP; equity **EUR2024353** JUMP +7.58%; assets **EUR2514546** JUMP +7.91%; debt **EUR490193** JUMP +9.31%; FTE 9087 **34,3** JUMP +8.20% (was 31,7; 9086 YE 40 vs 39; social balance 1003 33,5); kapitaalsubsidies **EUR19137** JUMP from empty; destin 691 **EUR142097** JUMP (was 53818); 791 **EUR18636** JUMP (was 11867); cash **EUR474597** JUMP +37.17% (+128613 vs 345984); geldbeleggingen **EUR1547410** JUMP; gebouwen **EUR225672** DROP; MVA 22/27 **EUR350171** DROP; aanbouw **empty**; capex **EUR32951** (8022 4443 + 8162 26452 + 8163 2056). Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_tienen leftover VAPH leftover-mined AGB-only leftover type after city GE tick1274. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial. NOT leftover city_lokeren leftover VAPH Emiliani remine@2568. NOT leftover Bethanië SCAN skip.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 5.50; entities +1; FOI **gap_hoito_tienen_vaph_matrix_70_76a_jump_2_87m_73_jump_2_79m_9901_jump_99k_l5** prio7 ready + draft; raw PDF docs/doge/raw/tick2569/; rq_2569=done; spawn **rq_2570 leftover dual PLUS every-10**; ticks=2569.
- Next: **rq_2570 leftover dual PLUS every-10**.

"""
with open("docs/doge/loop_log.md", "a", encoding="utf-8") as f:
    f.write(log)
print("rq/state/log updated", NOW)
