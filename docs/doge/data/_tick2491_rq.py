from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2491_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2491,")!=1: raise SystemExit(f"bad 2491 count {rq_raw.count(b'rq_2491,')}")
if b"rq_2492," in rq_raw: raise SystemExit("2492 exists")
idx=rq_raw.rfind(b"rq_2491,")
if idx<0: raise SystemExit("rq_2491 not found")
new_2491=(
"rq_2491,leftover dual Hopperank YE2025,hole_fill,8,done,L5,vzw_hopperank_asse,"
"Took unused leftover public VAPH Hopperank 0434.363.921 leftover mined city_asse. Official NBB MIC-VZW YE2025 2026-00126399 native statutory 10p 41.9kB. Envelope bruto 9900 DROP 1384983 (omzet empty MIC; 73 DROP 1462680); pnl DROP 44365; destin empty; FTE 16.7. FIRST leftover unused + live official YE2025 after leftover-type hunt (KBO activity NACE 88106 + leftover-open cities; leftover-via-VE ViTeS/INTRO/Mirto/Mivas SKIP; MILLE LUCI CVBA no JR SKIP; Huis Coppens SENIORS CARE-ION BV commercial SKIP). NOT De Sperwer remine. NOT Alderande remine. NOT De Hagewinde remine. NOT AMAB remine. NOT Hof ter Waarbeek remine. NOT Walfergem remine. NOT 3Wplus Kinderopvang remine. NOT Vijverbeek remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2491 leftover mined city_asse VAPH; Strong native PDF; 1 VE; prior-year identical; next rq_2492 NOT every-10 (next every-10 is 2500)\n"
)
new_2492=(
"rq_2492,leftover dual hunt after Hopperank,hole_fill,8,open,L5,,"
"NOT every-10 (next every-10 is 2500). Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde (Zonneschijn CIK taken) / geel (Augustientjes CIK taken; leftover VAPH/CAR/WZC/maatwerk) / herentals (Bremdael WZC taken; leftover VAPH/CAR; OpWeg YE2024) / eeklo (Kinderlach YE2024) / halle (CAR + CIK taken; leftover WZC exhausted; leftover VAPH still open — De Poel leftover-via-VE SKIP) / kalmthout (MILLE LUCI CVBA no JR) / bornem (CAR taken; leftover WZC/VAPH commercials/remines) / puurs (maatwerk taken; leftover WZC/VAPH remine/commercial) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde / mol / zoersel / schilde / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken) / schoten (VAPH taken) / lokeren (VAPH Hagewinde + Alderande taken; maatwerk De Sperwer taken — leftover WZC/CAR remine) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK + WZC taken) / ninove (CIK taken; leftover WZC/VAPH still open) / asse (CIK + VAPH Hopperank taken — leftover maatwerk 3WPLUS WERK unused YE2025). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT Hopperank remine. NOT De Sperwer remine. NOT Alderande remine. NOT De Hagewinde remine. NOT De Cirkel remine. NOT De Kapoentjes remine. NOT De Zonnewende remine. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT Huize De Veuster remine. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Nektari remine. NOT Reva Ter Linde remine. NOT BWP remine. NOT De Poel leftover-via-VE. NOT ASTOR bankrupt. NOT Aralea YE2024. NOT CAR Kapelhof Drongen OFF. NOT AMAB remine. NOT Hof ter Waarbeek remine. NOT Walfergem remine. NOT ViTeS leftover-via-VE. NOT Groep INTRO leftover-via-VE. NOT Mirto leftover-via-VE. NOT Mivas leftover-via-VE. NOT MILLE LUCI CVBA no JR. NOT Huis Coppens commercial. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2491 leftover city_asse VAPH; Hopperank taken leftover mined city_asse VAPH; 3Wplus+Vijverbeek taken leftover mined city_asse CIK; NOT every-10 (next 2500)\n"
)
if new_2491.count("\n")!=1 or new_2492.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2491",new_2491),("2492",new_2492)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2491.encode("utf-8"))
    f.write(new_2492.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2491", chk.count(b"rq_2491,"), "n2492", chk.count(b"rq_2492,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2491,2491,no,tick2491 leftover dual Hopperank 0434.363.921 Strong native PDF (omzet70 empty MIC; 73 DROP 1462680; 76A empty; envelope bruto9900 DROP 1384983; pnl DROP 44365; 9901 DROP 29074; equity JUMP 1304516; assets JUMP 1515048; debt JUMP 210532; FTE JUMP 16.7; kapitaalsubsidies empty; destin691 empty; 791 empty; cash DROP 456741; geldbeleggingen JUMP 1028808; capex 4090; 1 VE leftover city_asse VAPH); leftover mined city_asse VAPH; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (KBO activity NACE 88106; leftover-via-VE SKIP; MILLE LUCI CVBA no JR; Huis Coppens BV commercial); NOT De Sperwer remine; NOT Alderande remine; NOT De Hagewinde remine; NOT AMAB remine; NOT Hof ter Waarbeek remine; NOT Walfergem remine; NOT 3Wplus Kinderopvang remine; NOT Vijverbeek remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2492 NOT every-10 (next every-10 is 2500)\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2491 - rq_2491 Hopperank Asse (bruto DROP 1.38m / omzet empty MIC / 73 DROP 1.46m / pnl DROP 44k / Strong PDF)

- Unit: **rq_2491** leftover dual after **De Sperwer@2490**. NOT every-10 (next **2500**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of a mined Flanders city with official YE2025 native PDF. STOP leftover-note loop. Official KBO activity NACE **88106** + leftover-open city postcodes + NBB YE2025 (session + all entity-type checkboxes). FIRST leftover unused + live official YE2025 native euros after leftover-type hunt: leftover-via-VE ViTeS **0431.067.802** / Groep INTRO **0472.098.703** / Mirto **0407.656.257** / Mivas **0407.597.958** / Wase Werkplaats **0406.769.993** SKIP; MILLE LUCI **0680.594.461** CVBA Kalmthout no JR SKIP; Huis Coppens **0422.923.859** SENIORS CARE-ION BV commercial SKIP; Wij Blij zetel Zaventem leftover-via-VE SKIP; Re-HEAD YE2024 leftovers still YE2024. Confirmed `city_asse` exists (mined; leftover CIK 3Wplus + Vijverbeek taken — leftover unused VAPH). Took FREE leftover Flemish **HOPPERANK VZW** YE2025 (KBO **0434.363.921**; zetel Gasthuisstraat 7 bus 7 1730 Asse; **Actief** **1 VE** **2.159.420.037** since 12.02.2007; RSZ2025 **88.106**; leftover of mined **city_asse**; info@hopperank.be; VAPH ambulante+mobiele ondersteuning PVB+RTH). Identity trap: 0434.363.921 ≠ 3Wplus Kinderopvang remine ≠ Vijverbeek **0448.164.744** remine ≠ AMAB **0411.635.039** remine ≠ Hof ter Waarbeek **0478.728.256** remine ≠ Walfergem **0633.687.439** remine ≠ De Sperwer **0415.344.892** remine. 1 VE leftover of mined city_asse (zetel + VE Gasthuisstraat 7 bus 7). Confirmed leftover public VAPH not convent / not private / not CIK / not WZC / not commercial NV. MIC-VZW **native text** (not scan) — 41918 B / 10p all native euros (MIC-VZW 6.1.1 6.1.3 6.2 6.3 7 8 niet dienstig).
- Found: official NBB MIC-VZW native PDF deposit **2026-00126399** (41918 B / 10p; AV **19.05.2026**; header **29.05.2026**; official NBB UUID 7c4d8446-5b42-11f1-9d66-df103d3064ff; CDN GET **200** 41918 official NBB-generated OpenPDF 1.3.26 CreationDate 29.05.2026 Last-Modified 10.06.2026 MD5 66694bdfbf5284f43cd866a1ababc3fd; all 10p native; prior-year identical not restated) — omzet 70 **empty** MIC; 73 **EUR1462680** DROP −4.94% (was 1538735); 76A **empty**; envelope bruto 9900 **EUR1384983** DROP −4.57% (MIC because omzet empty; was 1451341); 62 **EUR1348508** JUMP +2.13%; 630 **EUR7401** JUMP +9.56%; 66A **empty**; 640/8 **empty**; 635/9 **empty**; 631/4 **empty**; bedrijfswinst 9901 **EUR29074** DROP −76.58% (was 124166); pnl 9904 **EUR44365** DROP −67.83% (was 137918); equity **EUR1304516** JUMP +3.52%; assets **EUR1515048** JUMP +4.84%; debt **EUR210532** JUMP +13.85%; FTE **16.7** JUMP +2.45% (was 16.3; 100 16.7; 105 18.1); kapitaalsubsidies **empty**; destin 691 **empty**; 791 **empty**; cash **EUR456741** DROP −15.60%; geldbeleggingen **EUR1028808** JUMP +18.63%; gebouwen **empty**; MVA 22/27 **EUR29416** DROP; aanbouw **empty**; capex **EUR4090**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_asse VAPH. NOT De Sperwer remine. NOT AMAB remine. NOT Hof ter Waarbeek remine. NOT Walfergem remine. NOT 3Wplus Kinderopvang remine. NOT Vijverbeek remine. NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.23); entities (+1 vzw_hopperank_asse); foi + draft `gap_hopperank_asse_vaph_matrix_bruto_1_38m_omzet_empty_73_drop_1_46m_pnl_drop_44k_l5`; rq_2491=done + rq_2492 open; loop_state ticks=2491; raw tick2491/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2500**). Next: rq_2492 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Hopperank remine / NOT De Sperwer remine / NOT Alderande remine / NOT De Hagewinde remine / NOT AMAB remine / NOT Hof ter Waarbeek remine / NOT Walfergem remine / NOT 3Wplus Kinderopvang remine / NOT Vijverbeek remine / NOT leftover-via-VE / NOT MILLE LUCI CVBA no JR / NOT Huis Coppens commercial / NOT Armonea commercial / NOT Vulpia commercial / NOT Korian commercial / NOT Evara remine / NOT Zorg-Saam remine). NOW leftover city_asse VAPH taken (CIK already taken). Leftover maatwerk of city_asse (3WPLUS WERK) still open.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("RQ STATE LOG DONE")
