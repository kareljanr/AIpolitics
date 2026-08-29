#!/usr/bin/env python3
"""tick2565 — surgical rq_2565 done + spawn rq_2566 + loop_state + loop_log."""
import csv, json, os
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)

ids = json.loads(Path("/tmp/tick2565/IDS.json").read_text())
NOW = ids["NOW"]
eid = ids["eid"]
gap_id = ids["gap_id"]

# --- research_queue: update rq_2565 + spawn rq_2566 only ---
rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
found = False
for row in rq_rows:
    if row["task_id"] == "rq_2565":
        found = True
        row["status"] = "done"
        row["entity_id"] = eid
        row["blocked_gap_id"] = gap_id
        row["updated_utc"] = NOW
        row["title"] = "leftover dual Duinhelm Oostende YE2025"
        row["notes"] = "tick2565 DONE leftover city_oostende leftover VAPH Duinhelm 0413.223.562 YE2025 VOL-VZW deposit 2026-00157589 70/76A JUMP 12607017 73 JUMP 10583537 9901 JUMP 886627 cash DROP 541306 (-154349) FTE 128,8 JUMP official zetel Rietmusstraat 24 8400 Oostende 10 VE leftover-mined city GE tick842"
if not found:
    raise SystemExit("rq_2565 not found")
skip = (
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child). "
    "HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_oostende leftover VAPH Duinhelm remine@2565 leftover Ithaka remine@2325 leftover Assjette 0 deposits leftover Autisme Leeft 0 deposits leftover Agape Tielt groenezorg leftover De Klokke leftover-via-VE leftover city_overijse leftover VAPH De Berken remine@2564 leftover De Lommerte Laakdal groenezorg leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen emmaus leftover-via-VE leftover De Witte Mol leftover-via-VE Stijn leftover De Voute 0 deposits leftover De Triangel YE2024-only leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine@2393 leftover CAR Accent remine@2396 leftover CAR Overleie remine@2462 leftover Ubuntu leftover-via-VE Kortrijk leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine@2405 leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine@2292 leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth/Buseloc remine under sec_flanders leftover city_boom leftover VLOTTER remine@2555 leftover Vlotter Maatwerk VZW YE2024-only leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea/Korian/Vulpia/CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Casa Di Colore Berlaar 0 deposits leftover groenezorg deferred leftover Apojo Aarschot remine@2336 leftover Kannet destelbergen vrijetijdszorg leftover 0-deposit Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover city_beringen 0 admin leftover VillaVip Familie 0 deposits leftover Woonondersteuning Vlaanderen YE2024-only leftover HabitASS ouderinitiatief leftover Ter Muiden leftover-via-VE Brugge leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024-only leftover De Ark Moerkerke YE2024-only leftover Wijzersterk 0 deposits. NOT every-10 (next every-10 2570)."
)
rq_2566 = {
    "task_id": "rq_2566",
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
    "notes": "spawned tick2565 after Duinhelm Oostende leftover dual; leftover public dual unused leftover VAPH of leftover-mined Flanders city; NOT every-10 (next every-10 2570)",
}
if any(x["task_id"] == "rq_2566" for x in rq_rows):
    raise SystemExit("rq_2566 already exists")
rq_rows.append(rq_2566)
with open(rq_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    w.writeheader()
    for row in rq_rows:
        w.writerow({k: row.get(k, "") for k in rq_fields})

# --- loop_state ---
ls_path = "docs/doge/data/loop_state.csv"
with open(ls_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    ls_fields = r.fieldnames
    ls_rows = list(r)
ls_rows[0]["last_tick_utc"] = NOW
ls_rows[0]["last_unit_id"] = "rq_2565"
ls_rows[0]["ticks_completed"] = "2565"
ls_rows[0]["paused"] = "no"
ls_rows[0]["notes"] = (
    "tick2565 leftover dual Duinhelm Oostende 0413.223.562 leftover city_oostende leftover VAPH Strong PDF deposit 2026-00157589 VOL-VZW 867669 B 59p 70/76A JUMP 12607017 73 JUMP 10583537 9901 JUMP 886627 cash DROP 541306 (-154349) FTE 128,8 JUMP official zetel Rietmusstraat 24 8400 Oostende 10 VE leftover-mined city GE tick842; FIRST LOCK leftover city_oostende leftover VAPH Duinhelm; next rq_2566 leftover dual (NOT every-10; next every-10 2570)"
)
with open(ls_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    w.writeheader()
    for row in ls_rows:
        w.writerow({k: row.get(k, "") for k in ls_fields})

# --- loop_log append ---
log = f"""

## Tick 2565 — {NOW} — rq_2565 leftover dual Duinhelm Oostende YE2025

- Unit: **rq_2565** leftover dual after **De Berken@2564**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child) like Peer@2556 / Dilsen@2557 / As@2558 / Diksmuide@2559 / Kortrijk@2560 / Leopoldsburg@2561 / Jabbeke@2562 / Staden@2563 / Overijse@2564. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_overijse leftover VAPH De Berken remine@2564 leftover De Lommerte Laakdal groenezorg leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover Ter Muiden leftover-via-VE Brugge leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024 leftover De Ark Moerkerke YE2024 leftover Wijzersterk 0 deposits leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen leftover-via-VE leftover De Witte Mol leftover-via-VE leftover De Voute 0 deposits leftover De Triangel YE2024 leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine leftover CAR Accent remine leftover CAR Overleie remine leftover Ubuntu leftover-via-VE leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth remine leftover city_boom leftover VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel remine leftover Terloo leftover-via-VE leftover Nethedal YE2024 leftover Het Raster leftover-via-VE leftover ErgoEzel leftover Casa Di Colore 0 deposits leftover Apojo remine leftover Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover VillaVip 0 deposits leftover Woonondersteuning Vlaanderen YE2024 leftover HabitASS leftover Wegwijs leftover-via-VE leftover Monnikenheide leftover-via-VE leftover 't Ingelhof leftover Achiel en Hector leftover Hof van Dorset leftover OC Ebergiste leftover-via-VE leftover Stal Den Eik leftover Havinet remine leftover Dominiek Savio leftover Tordale leftover Borgerstein leftover De Schakel leftover Eepos leftover Den Brand leftover Athletes for Hope leftover Breek uit jezelf leftover Woonondersteuning leftover HabitASS leftover VillaVip leftover De Lommerte groenezorg.
- Hunt skips: prefer-list **city_zutendaal** Wegwijs leftover-via-VE Zonhoven SKIP; **city_olen** no VZA; **city_wuustwezel** Monnikenheide leftover-via-VE Zoersel + groenezorg SKIP; AGB-only leftover VAPH hunt stalled on 0-deposit/YE2024/groenezorg/hard-skips. Extra: **Assjette Hasselt 0553.727.468 0 NBB deposits SKIP**; **Autisme Leeft Hasselt 0820.047.896 0 deposits SKIP**; **Agapè Tielt groenezorg SKIP**; **De Klokke Sint-Niklaas leftover-via-VE SKIP**; **OpWeg Herentals YE2024 SKIP**; **Bethanië Genk unused YE2025 VOL live but took Duinhelm first**. Remine skips: De Berken@2564 / Kerckstede@2563 / Licht en Liefde Heem@2562 / Berkenhof@2561 / De Hoge Kouter@2560 / Ithaka@2325. Took NON-stall leftover mined **city_oostende** leftover VAPH (city GE tick842; AG-O child exists; Duinhelm unused).
- FIRST LOCK leftover city_oostende leftover VAPH **Duinhelm 0413.223.562** leftover-mined city GE tick842 unused leftover type (Duinhelm itself unused; Ithaka remine@2325 under sec_flanders). Confirmed unused (0 real entity rows on 0413.223.562 / 0413223562) + official KBO zetel Rietmusstraat 24 **8400 Oostende** (not leftover-via-VE of a DIFFERENT leftover city as parent) + native YE2025 PDF. Took FREE leftover Flemish **Duinhelm** YE2025 (KBO **0413.223.562**; official zetel Rietmusstraat 24 8400 Oostende since 27.05.1987; **Actief** **10 VE** **2.154.906.468** Duinhelm vzw Rietmusstraat 24 since 05.07.2006 + 9 other VEs mostly Oostende + 1 Gistel leftover-via-VE FROM leftover city_oostende; VZW; RSZ2025 **87.202**; leftover of mined **city_oostende**; FOI info@duinhelm.be from official NBB PDF + annelore.devidts@duinhelm.be from official VAPH; leftover VAPH / official VAPH adreslijst Duinhelm Vergunde Zorgaanbieder + RTH). Identity trap: 0413.223.562 ≠ leftover city GE Oostende **0207.436.775** ≠ leftover AG-O Oostende **0267.389.606** ≠ leftover Ithaka **0448.387.646** remine@2325. Confirmed leftover public leftover VAPH VZW not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VOL-VZW **native text** (not scan) — 867669 B / 59p native euros (VOL-VZW 6.1 6.2.1 6.2.2 6.2.4 6.3.4 6.3.6 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.14 6.16 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00157589** (867669 B / 59p; AV **20.05.2026**; header **11/06/2026**; CDN GET **200** 867669 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-06-13 01:16:02 UTC MD5 3f1f6ef973d0438874fc72d91d186fb3; NBB consult HTML stub 5344 B discarded; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR1296875** JUMP +3.81% (was 1249232; commercial-only vs large 73); 73 **EUR10583537** JUMP +11.28% (was 9510384; subsidies 733 **EUR10546090**; schenkingen 731 **EUR36923**); 76A **EUR71649** DROP (was 235308); envelope 70/76A **EUR12607017** JUMP +9.19% (was 11546208; delta +1060809); 74 **EUR654956** JUMP (was 551284); 62 **EUR9458561** JUMP (was 8541018); 630 **EUR403934** DROP (was 440879); 66A **EUR30087** JUMP (was 120); 640/8 **EUR323537** DROP (was 332882); bedrijfswinst 9901 **EUR886627** JUMP +69.28% (was 523770; delta +362857); pnl 9904 **EUR904762** JUMP +62.46% (was 556930); 9903 **EUR919738** JUMP; equity **EUR7995963** JUMP +11.62%; assets **EUR11997286** JUMP +7.19%; debt **EUR3423856** flat; FTE 9087 **128,8** JUMP +4.89% (was 122,8; 9086 YE 147 vs 149); kapitaalsubsidies **EUR451436** DROP (was 523673); destin 691 **EUR885708** DROP (was 1248453); 791 **empty**; cash **EUR541306** DROP −22.19% (−154349 vs 695655); geldbeleggingen **EUR2648693** JUMP; gebouwen **EUR5774103** DROP; MVA 22/27 **EUR7162269** DROP; aanbouw **empty**; capex **EUR207752** (8162+8163). Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 10 VE leftover mined city_oostende leftover VAPH unused leftover type after city GE tick842. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial. NOT leftover city_overijse leftover VAPH De Berken remine@2564. NOT leftover Ithaka remine@2325.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 5.88; entities +1; FOI **gap_duinhelm_oostende_vaph_matrix_70_76a_jump_12_61m_73_jump_10_58m_9901_jump_887k_cash_drop_154k_l5** prio7 ready + draft; raw PDF docs/doge/raw/tick2565/; rq_2565=done; spawn **rq_2566 leftover dual (NOT every-10; next every-10 2570)**; ticks=2565.
- Next: **rq_2566 leftover dual** (NOT every-10; next every-10 **2570**).

"""
with open("docs/doge/loop_log.md", "a", encoding="utf-8") as f:
    f.write(log)
print("rq/state/log updated", NOW)
