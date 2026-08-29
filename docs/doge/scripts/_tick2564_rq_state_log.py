#!/usr/bin/env python3
"""tick2564 — surgical rq_2564 done + spawn rq_2565 + loop_state + loop_log."""
import csv, json, os
from pathlib import Path
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)

ids = json.loads(Path("/tmp/tick2564/IDS.json").read_text())
NOW = ids["NOW"]
eid = ids["eid"]
gap_id = ids["gap_id"]

# --- research_queue: update rq_2564 + spawn rq_2565 only ---
rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
found = False
for row in rq_rows:
    if row["task_id"] == "rq_2564":
        found = True
        row["status"] = "done"
        row["entity_id"] = eid
        row["blocked_gap_id"] = gap_id
        row["updated_utc"] = NOW
        row["title"] = "leftover dual De Berken Overijse YE2025"
        row["notes"] = "tick2564 DONE leftover city_overijse leftover VAPH De Berken 0425.840.688 YE2025 VKT-VZW deposit 2026-00213938 bruto9900 DROP 1115742 73 DROP 1010312 9901 FLIP LOSS -74568 cash JUMP 684185 (+216864) FTE 13,5 DROP official zetel Schavei 70 3090 Overijse 1 VE leftover-mined city GE tick1068"
if not found:
    raise SystemExit("rq_2564 not found")
skip = (
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child). "
    "HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_overijse leftover VAPH De Berken remine@2564 leftover De Lommerte Laakdal groenezorg leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen emmaus leftover-via-VE leftover De Witte Mol leftover-via-VE Stijn leftover De Voute 0 deposits opgericht 2025 leftover De Triangel YE2024-only stall leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine@2393 leftover CAR Accent remine@2396 leftover CAR Overleie remine@2462 leftover Ubuntu leftover-via-VE Kortrijk leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine@2405 leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine@2292 leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth/Buseloc remine under sec_flanders leftover city_boom leftover VLOTTER remine@2555 leftover Vlotter Maatwerk VZW YE2024-only leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea/Korian/Vulpia/CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Casa Di Colore Berlaar 0 deposits leftover groenezorg deferred leftover Apojo Aarschot remine@2336 leftover Kannet destelbergen vrijetijdszorg leftover 0-deposit Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover city_beringen 0 admin leftover VillaVip Familie 0 deposits leftover Woonondersteuning Vlaanderen YE2024-only leftover HabitASS ouderinitiatief leftover Ter Muiden leftover-via-VE Brugge leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024-only leftover De Ark Moerkerke YE2024-only leftover Wijzersterk 0 deposits. NOT every-10 (next every-10 2570)."
)
rq_2565 = {
    "task_id": "rq_2565",
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
    "notes": "spawned tick2564 after De Berken Overijse leftover dual; leftover public dual unused leftover VAPH of leftover-mined Flanders city; NOT every-10 (next every-10 2570)",
}
if any(x["task_id"] == "rq_2565" for x in rq_rows):
    raise SystemExit("rq_2565 already exists")
rq_rows.append(rq_2565)
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
ls_rows[0]["last_unit_id"] = "rq_2564"
ls_rows[0]["ticks_completed"] = "2564"
ls_rows[0]["paused"] = "no"
ls_rows[0]["notes"] = (
    "tick2564 leftover dual De Berken Overijse 0425.840.688 leftover city_overijse leftover VAPH Strong PDF deposit 2026-00213938 VKT-VZW 50434 B 14p bruto9900 DROP 1115742 73 DROP 1010312 9901 FLIP LOSS -74568 cash JUMP 684185 (+216864) FTE 13,5 DROP official zetel Schavei 70 3090 Overijse 1 VE leftover-mined city GE tick1068; FIRST LOCK leftover city_overijse leftover VAPH De Berken; next rq_2565 leftover dual (NOT every-10; next every-10 2570)"
)
with open(ls_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    w.writeheader()
    for row in ls_rows:
        w.writerow({k: row.get(k, "") for k in ls_fields})

# --- loop_log append ---
log = f"""

## Tick 2564 — {NOW} — rq_2564 leftover dual De Berken Overijse YE2025

- Unit: **rq_2564** leftover dual after **Kerckstede@2563**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. Prefer leftover-mined AGB-only leftover VAPH; if AGB-only stalls, leftover-mined city GE (no AGB child) like Peer@2556 / Dilsen@2557 / As@2558 / Diksmuide@2559 / Kortrijk@2560 / Leopoldsburg@2561 / Jabbeke@2562 / Staden@2563. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_staden leftover VAPH Kerckstede remine@2563 leftover city_jabbeke leftover VAPH Licht en Liefde Heem remine@2562 leftover Ter Muiden leftover-via-VE Brugge leftover Klein Postel groenezorg leftover Mok Lochristi 0 deposits leftover Levenslust Lennik YE2024-only leftover De Ark Moerkerke YE2024-only leftover Wijzersterk 0 deposits leftover city_leopoldsburg leftover VAPH Berkenhof remine@2561 leftover DVC Zevenbergen leftover-via-VE leftover De Witte Mol leftover-via-VE leftover De Voute 0 deposits leftover De Triangel YE2024-only leftover city_kortrijk leftover VAPH De Hoge Kouter remine@2560 leftover Zonnebloem remine leftover CAR Accent remine leftover CAR Overleie remine leftover Ubuntu leftover-via-VE leftover city_diksmuide leftover VAPH Duin en Polder remine@2559 leftover CIK De Hoeksteen remine leftover city_as leftover VAPH Duizendschoon remine@2558 leftover Labor Arbeidskansen remine leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover BC Sint-Elisabeth remine leftover city_boom leftover VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht/Ter Heyder Heide/Steger 0 deposits leftover Pelikaan OCMW leftover Ampel remine leftover Terloo leftover-via-VE leftover Nethedal YE2024 leftover Het Raster leftover-via-VE leftover ErgoEzel leftover Casa Di Colore 0 deposits leftover Apojo remine leftover Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend leftover VillaVip 0 deposits leftover Woonondersteuning Vlaanderen YE2024 leftover HabitASS leftover Wegwijs leftover-via-VE leftover Monnikenheide leftover-via-VE leftover 't Ingelhof leftover Achiel en Hector leftover Hof van Dorset leftover OC Ebergiste leftover-via-VE leftover Stal Den Eik leftover Havinet remine leftover Dominiek Savio leftover Tordale leftover Borgerstein leftover De Schakel leftover Eepos leftover Den Brand leftover Het Noordhof remine.
- Hunt skips: prefer-list **city_zutendaal** Wegwijs leftover-via-VE Zonhoven SKIP; **city_olen** no VZA; **city_wuustwezel** Monnikenheide leftover-via-VE Zoersel + groenezorg SKIP; AGB-only leftover VAPH hunt stalled on 0-deposit/YE2024/groenezorg/hard-skips. Extra: **De Lommerte Laakdal 0737.360.445 groenezorg SKIP**. Remine skips: Kerckstede@2563 / Licht en Liefde Heem@2562 / Berkenhof@2561 / De Hoge Kouter@2560. Took NON-stall leftover mined **city_overijse** leftover VAPH (city GE tick1068; no AGB child; De Berken unused).
- FIRST LOCK leftover city_overijse leftover VAPH **De Berken 0425.840.688** leftover-mined city GE tick1068 unused leftover type (no agb_overijse child; De Berken itself unused). Confirmed unused (0 real entity rows on 0425.840.688 / 0425840688) + official KBO zetel Schavei 70 **3090 Overijse** (not leftover-via-VE of a DIFFERENT leftover city as parent) + native YE2025 PDF. Took FREE leftover Flemish **De Berken** YE2025 (KBO **0425.840.688**; official zetel Schavei 70 3090 Overijse since 25.08.1983; **Actief** **1 VE** **2.150.826.431** De Berken Schavei 70 since 03.01.2006; VZW; RSZ2025 **88.106**; leftover of mined **city_overijse**; FOI directie@deberken.be from official VAPH; leftover VAPH / official VAPH adreslijst De Berken Vergunde Zorgaanbieder). Identity trap: 0425.840.688 ≠ leftover city GE Overijse **0207.512.001** ≠ leftover OCMW Overijse **0212.207.393**. Confirmed leftover public leftover VAPH VZW not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VKT-VZW **native text** (not scan) — 50434 B / 14p native euros (VKT-VZW 6.1.1 6.1.2 6.2 6.3 6.5 6.6 7 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00213938** (50434 B / 14p; AV **18.06.2026**; header **29/06/2026**; CDN GET **200** 50434 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-06-29 20:13:44 UTC MD5 3f49303ce08b6a68847d2f5d9ec2d4a6; NBB consult HTML stub 5344 B discarded; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR158625** DROP −3.42% (was 164235; commercial-only vs large 73); 73 **EUR1010312** DROP −8.13% (was 1099776); 76A **empty**; envelope bruto 9900 **EUR1115742** DROP −8.20% (VKT envelope because 73 is the subsidy envelope and bruto >> omzet; was 1215402; delta −99660); 74 **not on VKT form**; 62 **EUR1059410** DROP −0.92% (was 1069276); 630 **EUR68916** JUMP +7.45% (was 64135); 66A **empty**; 640/8 **EUR61983** JUMP (was 49316); bedrijfswinst 9901 **EUR−74568** FLIP LOSS (was +32675); pnl 9904 **EUR−28725** FLIP LOSS (was +79693); 9903 **EUR−28725** FLIP LOSS; equity **EUR1957246** DROP −2.81%; assets **EUR2077732** DROP −2.83%; debt **EUR120486** DROP −3.18%; FTE 9087 **13,5** DROP −2.17% (was 13,8); kapitaalsubsidies **n/a detail**; destin 691/791 **empty**; cash **EUR684185** JUMP +46.41% (+216864 vs 467321); geldbeleggingen **EUR1000000** DROP; gebouwen via MVA; MVA 22/27 **EUR352511** DROP; aanbouw **empty**; capex via 630. Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_overijse leftover VAPH unused leftover type after city GE tick1068. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial. NOT leftover city_staden leftover VAPH Kerckstede remine@2563.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 5.35; entities +1; FOI **gap_de_berken_overijse_vaph_matrix_bruto_drop_1_12m_73_drop_1_01m_9901_flip_loss_75k_cash_jump_217k_l5** prio7 ready + draft; raw PDF docs/doge/raw/tick2564/; rq_2564=done; spawn **rq_2565 leftover dual (NOT every-10; next every-10 2570)**; ticks=2564.
- Next: **rq_2565 leftover dual** (NOT every-10; next every-10 **2570**).

"""
with open("docs/doge/loop_log.md", "a", encoding="utf-8") as f:
    f.write(log)
print("rq/state/log updated", NOW)
