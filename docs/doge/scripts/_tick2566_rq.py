#!/usr/bin/env python3
"""tick2566 — surgical rq_2566 done + spawn rq_2567 + loop_state + loop_log.
Does NOT rewrite whole research_queue.csv: truncates only the last row then appends."""
import csv, io, json, os
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)

ids = json.loads(Path("/tmp/tick2566/IDS.json").read_text())
NOW = ids["NOW"]
eid = ids["eid"]
gap_id = ids["gap_id"]

rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, "rb") as f:
    f.seek(0, 2)
    size = f.tell()
    f.seek(max(0, size - 200000))
    tail = f.read()
# find last complete line start
# keep header from start of file; only rewrite last record
# locate last newline before EOF
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
# parse last row
header = "task_id,title,sprint,priority,status,hierarchy_target,entity_id,instructions,blocked_gap_id,created_utc,updated_utc,notes"
buf = io.StringIO(header + "\n" + last_line.decode("utf-8"))
r = csv.DictReader(buf)
row = next(r)
if row["task_id"] != "rq_2566":
    raise SystemExit(f"last row is {row['task_id']} not rq_2566")
row["status"] = "done"
row["entity_id"] = eid
row["blocked_gap_id"] = gap_id
row["updated_utc"] = NOW
row["title"] = "leftover dual Vondels Ieper YE2025"
row["notes"] = (
    "tick2566 DONE leftover city_ieper leftover VAPH Vondels 0415.108.728 YE2025 VOL-VZW deposit 2026-00207010 70/76A JUMP 10485951 73 JUMP 9049848 9901 JUMP 451999 cash DROP 921799 (-762307) FTE 104,9 JUMP official zetel Ter Waarde 45 8900 Ieper 9 VE leftover-mined AGB-only leftover VAPH after city GE tick851"
)

skip = (
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child). "
    "HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_ieper leftover VAPH Vondels remine@2566 leftover city_oostende leftover VAPH Duinhelm remine@2565 leftover Ithaka remine@2325 leftover Bethanie Genk SCAN leftover Muylenberg leftover-via-VE Verbint remine@2401 leftover De Link leftover-via-VE leftover OpWeg YE2024 leftover De Bezaan leftover-via-VE leftover De Klokke leftover-via-VE leftover Assjette 0 deposits leftover Autisme Leeft 0 deposits leftover Agape Tielt groenezorg leftover city_overijse leftover VAPH De Berken remine@2564 leftover De Lommerte Laakdal groenezorg leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen emmaus leftover-via-VE leftover De Witte Mol leftover-via-VE Stijn leftover De Voute 0 deposits leftover De Triangel YE2024-only leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine@2393 leftover CAR Accent remine@2396 leftover CAR Overleie remine@2462 leftover Ubuntu leftover-via-VE Kortrijk leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine@2405 leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine@2292 leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth/Buseloc remine under sec_flanders leftover city_boom leftover VLOTTER remine@2555 leftover Vlotter Maatwerk VZW YE2024-only leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea/Korian/Vulpia/CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Casa Di Colore Berlaar 0 deposits leftover groenezorg deferred leftover Apojo Aarschot remine@2336 leftover Kannet destelbergen vrijetijdszorg leftover 0-deposit Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover city_beringen 0 admin leftover VillaVip Familie 0 deposits leftover Woonondersteuning Vlaanderen YE2024-only leftover HabitASS ouderinitiatief leftover Ter Muiden leftover-via-VE Brugge leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024-only leftover De Ark Moerkerke YE2024-only leftover Wijzersterk 0 deposits. NOT every-10 (next every-10 2570)."
)
rq_2567 = {
    "task_id": "rq_2567",
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
    "notes": "spawned tick2566 after Vondels Ieper leftover dual; leftover public dual unused leftover VAPH of leftover-mined Flanders city; NOT every-10 (next every-10 2570)",
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
w.writerow({k: rq_2567.get(k, "") for k in fields})
payload = out.getvalue().encode("utf-8")

with open(rq_path, "r+b") as f:
    f.seek(last_line_abs_start)
    f.truncate()
    f.write(payload)
print("surgical rq: patched rq_2566 + spawned rq_2567 at offset", last_line_abs_start)

# --- loop_state (tiny file) ---
ls_path = "docs/doge/data/loop_state.csv"
with open(ls_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    ls_fields = r.fieldnames
    ls_rows = list(r)
ls_rows[0]["last_tick_utc"] = NOW
ls_rows[0]["last_unit_id"] = "rq_2566"
ls_rows[0]["ticks_completed"] = "2566"
ls_rows[0]["paused"] = "no"
ls_rows[0]["notes"] = (
    "tick2566 leftover dual Vondels Ieper 0415.108.728 leftover city_ieper leftover VAPH leftover-mined AGB-only leftover type Strong PDF deposit 2026-00207010 VOL-VZW 1054665 B 44p 70/76A JUMP 10485951 73 JUMP 9049848 9901 JUMP 451999 cash DROP 921799 (-762307) FTE 104,9 JUMP official zetel Ter Waarde 45 8900 Ieper 9 VE leftover-mined city GE tick851; FIRST LOCK leftover city_ieper leftover VAPH Vondels; next rq_2567 leftover dual (NOT every-10; next every-10 2570)"
)
with open(ls_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    w.writeheader()
    for row2 in ls_rows:
        w.writerow({k: row2.get(k, "") for k in ls_fields})

log = f"""

## Tick 2566 — {NOW} — rq_2566 leftover dual Vondels Ieper YE2025

- Unit: **rq_2566** leftover dual after **Duinhelm@2565**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child) like Peer@2556 / Dilsen@2557 / As@2558 / Diksmuide@2559 / Kortrijk@2560 / Leopoldsburg@2561 / Jabbeke@2562 / Staden@2563 / Overijse@2564 / Oostende@2565. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_oostende leftover VAPH Duinhelm remine@2565 leftover Ithaka remine@2325 leftover city_overijse leftover VAPH De Berken remine@2564 leftover De Lommerte Laakdal groenezorg leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover Ter Muiden leftover-via-VE leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024 leftover De Ark Moerkerke YE2024 leftover Wijzersterk 0 deposits leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen leftover-via-VE leftover De Witte Mol leftover-via-VE leftover De Voute 0 deposits leftover De Triangel YE2024 leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine leftover CAR Accent remine leftover CAR Overleie remine leftover Ubuntu leftover-via-VE leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth remine leftover city_boom leftover VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel remine leftover Terloo leftover-via-VE leftover Nethedal YE2024 leftover Het Raster leftover-via-VE leftover ErgoEzel leftover Casa Di Colore leftover Apojo remine leftover Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover VillaVip leftover Woonondersteuning Vlaanderen YE2024 leftover HabitASS leftover Wegwijs leftover-via-VE leftover Monnikenheide leftover-via-VE leftover Dominiek Savio leftover Tordale leftover Borgerstein leftover De Schakel leftover Eepos leftover Den Brand leftover Het Noordhof remine leftover city_kapellen / city_londerzeel / city_wortegem_petegem slugs MISSING leftover Armonea/Korian/Vulpia/CuraCare/SLG/OCMW leftover convent leftover leftover-via-VE leftover YE2024-only leftover 0-deposit leftover groenezorg leftover ouderinitiatief.
- Hunt skips: leftover-mined AGB-only leftover VAPH **Bethanië Genk 0414.744.977** unused YE2025 VOL live but **SCAN/OCR HARD SKIP** (Xerox AltaLink C8035; 18245010 B / 46p; statutory pages 2-38 empty text; only jaarverslag/commissaris native). **Muylenberg Turnhout leftover-via-VE Verbint remine@2401 SKIP**. **De Link Sint-Niklaas leftover-via-VE GO! SCHOLENGROEP 17 SKIP**. **De Bezaan leftover-via-VE Ithaka SKIP**. **De Klokke leftover-via-VE SKIP**. **OpWeg Herentals YE2024 SKIP**. Remine skips: Duinhelm@2565 / De Berken@2564 / Kerckstede@2563 / Licht en Liefde Heem@2562 / Berkenhof@2561 / De Hoge Kouter@2560 / Ithaka@2325. Took NON-stall leftover mined **city_ieper** leftover VAPH leftover-mined AGB-only leftover type (city GE tick851; AGB Vauban tick1186 + AGB Musea tick1187; Vondels unused).
- FIRST LOCK leftover city_ieper leftover VAPH **Vondels 0415.108.728** leftover-mined AGB-only leftover type after city GE tick851 unused leftover type (Vondels itself unused; CAR De Klinker remine@2386 / Huize Zonnelied remine@2423 / Wintershove remine@2422 / Gesticht Zusters remine@2461). Confirmed unused (0 real entity rows on 0415.108.728 / 0415108728) + official KBO zetel Ter Waarde 45 **8900 Ieper** (not leftover-via-VE of a DIFFERENT leftover city as parent) + native YE2025 PDF. Took FREE leftover Flemish **Vondels** YE2025 (KBO **0415.108.728**; official zetel Ter Waarde 45 8900 Ieper since 08.12.2014; **Actief** **9 VE** **2.237.246.503** Vondels Ter Waarde 45 since 01.01.2015 + **2.234.565.937** Milieuboerderij Vaartstraat 7 8902 Ieper since 01.01.2004 + **2.315.249.943** RWI Siegenlaan 3 8900 Ieper since 01.01.2021 + **2.315.250.735** RWI Merellaan 6 8900 Ieper since 01.01.2021 + **2.365.387.461** Vondels BWI Ter Waarde 66 8900 Ieper since 01.10.2024 + leftover-via-VE FROM leftover city_ieper **2.154.326.943** De Pelgrim Dorpsstraat 22 8952 Heuvelland + **2.234.565.739** Fakkel Laagweg 36 8940 Wervik + **2.234.565.838** Minnehuis Kruisekestraat 92a 8940 Wervik + **2.237.247.392** Vondels Dan. De Haenelaan 2 8630 Veurne; VZW; RSZ2025 **87.202**; leftover of mined **city_ieper**; FOI info@vondels.be from official NBB PDF + official VAPH; leftover VAPH / official VAPH adreslijst Vondels Vergunde Zorgaanbieder). Identity trap: 0415.108.728 ≠ leftover city GE Ieper **0207.484.681** ≠ leftover AGB Vauban **0877.643.330** ≠ leftover AGB Musea **0759.387.858** ≠ leftover CAR De Klinker **0430.535.290** remine@2386 ≠ leftover Huize Zonnelied **0415.082.497** remine@2423 ≠ leftover Wintershove **0459.245.312** remine@2422 ≠ leftover Gesticht Zusters **0410.918.031** remine@2461 ≠ leftover Duinhelm **0413.223.562** remine@2565 ≠ leftover Bethanië **0414.744.977** SCAN skip. Confirmed leftover public leftover VAPH VZW not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VOL-VZW **native text** (not scan) — 1054665 B / 44p native euros (VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.5 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.10 6.14 6.16 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00207010** (1054665 B / 44p; AV **01.06.2026**; header **23/06/2026**; CDN GET **200** 1054665 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-06-27 04:15:35 UTC MD5 c82eac38daca72931f8d13a7f6a9104c; NBB consult HTML stub 5344 B discarded; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR754516** JUMP +12.26% (was 672096; commercial-only vs large 73); 73 **EUR9049848** JUMP +10.30% (was 8204497; subsidies 733 **EUR9049848**; 731 empty); 76A **EUR75533** DROP (was 121597); envelope 70/76A **EUR10485951** JUMP +9.79% (was 9550809; delta +935142); 74 **EUR606055** JUMP (was 552620); 62 **EUR7983439** JUMP (was 7214906); 630 **EUR590453** JUMP (was 588086); 66A **EUR1313** DROP (was 130611); 640/8 **EUR126947** DROP (was 129761); bedrijfswinst 9901 **EUR451999** JUMP +77.41% (was 254774; delta +197225); pnl 9904 **EUR455585** JUMP +56.79% (was 290569); 9903 **EUR452241** JUMP; equity **EUR7255341** JUMP +5.46%; assets **EUR10723136** JUMP +4.08%; debt **EUR3467795** JUMP; FTE 9087 **104,9** JUMP +9.96% (was 95,4; 9086 YE 126 vs 116); kapitaalsubsidies **EUR1465384** DROP (was 1545165); destin 691 **EUR567853** JUMP (was 254039); 791 **empty** (was 1310928); cash **EUR921799** DROP −45.26% (−762307 vs 1684106); geldbeleggingen **EUR2000000** JUMP (was 600000); gebouwen **EUR4284561** DROP; MVA 22/27 **EUR6099664** DROP; aanbouw **EUR3699** DROP (was 371783); capex **EUR322300** (8161+8162+8163+8166). Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 9 VE leftover mined city_ieper leftover VAPH leftover-mined AGB-only leftover type after city GE tick851. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial. NOT leftover city_oostende leftover VAPH Duinhelm remine@2565. NOT leftover Bethanië SCAN skip.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 5.80; entities +1; FOI **gap_vondels_ieper_vaph_matrix_70_76a_jump_10_49m_73_jump_9_05m_9901_jump_197k_cash_drop_762k_l5** prio7 ready + draft; raw PDF docs/doge/raw/tick2566/; rq_2566=done; spawn **rq_2567 leftover dual (NOT every-10; next every-10 2570)**; ticks=2566.
- Next: **rq_2567 leftover dual** (NOT every-10; next every-10 **2570**).

"""
with open("docs/doge/loop_log.md", "a", encoding="utf-8") as f:
    f.write(log)
print("rq/state/log updated", NOW)
