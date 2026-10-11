from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2492_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2492,")!=1: raise SystemExit(f"bad 2492 count {rq_raw.count(b'rq_2492,')}")
if b"rq_2493," in rq_raw: raise SystemExit("2493 exists")
idx=rq_raw.rfind(b"rq_2492,")
if idx<0: raise SystemExit("rq_2492 not found")
new_2492=(
"rq_2492,leftover dual 3Wplus Werk YE2025,hole_fill,8,done,L5,vzw_3wplus_werk_asse,"
"Took unused leftover public maatwerk 3WPLUS WERK 0467.004.520 leftover mined city_asse. Official NBB VKT-VZW YE2025 2026-00271890 native statutory 26p 309.8kB. Envelope bruto 9900 JUMP 2631017 (omzet+73 empty VKT; 76A DROP 1000); pnl FLIP 49057; destin empty; FTE 56.8. FIRST leftover unused + live official YE2025 after leftover-type hunt (KBO activity NACE 88993 + postcode 1730; AMAB remine SKIP; GROEP 3WPLUS holding SKIP; ViTeS/INTRO leftover-via-VE SKIP). NOT 3Wplus Kinderopvang remine. NOT AMAB remine. NOT Hopperank remine. NOT Vijverbeek remine. NOT Hof ter Waarbeek remine. NOT Walfergem remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2492 leftover mined city_asse maatwerk; Strong native PDF; 3 VE; prior-year identical; next rq_2493 NOT every-10 (next every-10 is 2500)\n"
)
new_2493=(
"rq_2493,leftover dual hunt after 3Wplus Werk,hole_fill,8,open,L5,,"
"NOT every-10 (next every-10 is 2500). Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde (Zonneschijn CIK taken) / geel (Augustientjes CIK taken; leftover VAPH/CAR/WZC/maatwerk) / herentals (Bremdael WZC taken; leftover VAPH/CAR; OpWeg YE2024) / eeklo (Kinderlach YE2024) / halle (CAR + CIK taken; leftover WZC exhausted; leftover VAPH still open — De Poel leftover-via-VE SKIP) / kalmthout (MILLE LUCI CVBA no JR) / bornem (CAR taken; leftover WZC/VAPH commercials/remines) / puurs (maatwerk taken; leftover WZC/VAPH remine/commercial) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde / mol / zoersel / schilde / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken) / schoten (VAPH taken) / lokeren (VAPH Hagewinde + Alderande taken; maatwerk De Sperwer taken — leftover WZC/CAR remine) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK + WZC taken) / ninove (CIK taken; leftover WZC/VAPH still open) / asse (CIK + VAPH Hopperank + maatwerk 3WPLUS WERK taken — leftover WZC/CAR still open BUT AMAB/Hof ter Waarbeek/Walfergem remine). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT 3Wplus Werk remine. NOT Hopperank remine. NOT De Sperwer remine. NOT Alderande remine. NOT De Hagewinde remine. NOT De Cirkel remine. NOT De Kapoentjes remine. NOT De Zonnewende remine. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT Huize De Veuster remine. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Nektari remine. NOT Reva Ter Linde remine. NOT BWP remine. NOT De Poel leftover-via-VE. NOT ASTOR bankrupt. NOT Aralea YE2024. NOT CAR Kapelhof Drongen OFF. NOT AMAB remine. NOT Hof ter Waarbeek remine. NOT Walfergem remine. NOT 3Wplus Kinderopvang remine. NOT Vijverbeek remine. NOT ViTeS leftover-via-VE. NOT Groep INTRO leftover-via-VE. NOT Mirto leftover-via-VE. NOT Mivas leftover-via-VE. NOT MILLE LUCI CVBA no JR. NOT Huis Coppens commercial. NOT GROEP 3WPLUS. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2492 leftover city_asse maatwerk; 3WPLUS WERK taken leftover mined city_asse maatwerk; Hopperank taken leftover mined city_asse VAPH; 3Wplus+Vijverbeek taken leftover mined city_asse CIK; NOT every-10 (next 2500)\n"
)
if new_2492.count("\n")!=1 or new_2493.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2492",new_2492),("2493",new_2493)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2492.encode("utf-8"))
    f.write(new_2493.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2492", chk.count(b"rq_2492,"), "n2493", chk.count(b"rq_2493,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2492,2492,no,tick2492 leftover dual 3WPLUS WERK 0467.004.520 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A DROP 1000; envelope bruto9900 JUMP 2631017; pnl FLIP 49057; 9901 JUMP 67042; equity JUMP 1625771; assets DROP 3392304; debt DROP 1766533; FTE JUMP 56.8; kapitaalsubsidies DROP 63475; destin691 empty; 791 empty; cash JUMP 494869; geldbeleggingen empty; capex 226984; 3 VE leftover city_asse maatwerk); leftover mined city_asse maatwerk; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (KBO activity NACE 88993; AMAB remine SKIP; GROEP 3WPLUS holding SKIP; ViTeS/INTRO leftover-via-VE SKIP); NOT 3Wplus Kinderopvang remine; NOT AMAB remine; NOT Hopperank remine; NOT Vijverbeek remine; NOT Hof ter Waarbeek remine; NOT Walfergem remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2493 NOT every-10 (next every-10 is 2500)\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2492 - rq_2492 3Wplus Werk Asse (bruto JUMP 2.63m / omzet+73 empty VKT / pnl FLIP 49k / Strong PDF)

- Unit: **rq_2492** leftover dual after **Hopperank@2491**. NOT every-10 (next **2500**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of a mined Flanders city with official YE2025 native PDF. STOP leftover-note loop. Official KBO activity NACE **88993** + leftover-open city postcode 1730 Asse + NBB YE2025 (session). FIRST leftover unused + live official YE2025 native euros after leftover-type hunt: AMAB **0411.635.039** remine SKIP; GROEP 3WPLUS **0674.926.988** holding SKIP; ViTeS **0431.067.802** / Groep INTRO **0472.098.703** leftover-via-VE SKIP; Re-HEAD YE2024 leftovers still YE2024. Confirmed `city_asse` exists (mined; leftover CIK 3Wplus + Vijverbeek taken; leftover VAPH Hopperank taken — leftover unused maatwerk). Took FREE leftover Flemish **3WPLUS WERK VZW** YE2025 (KBO **0467.004.520**; zetel Z. 5 Mollem 250 1730 Asse; **Actief** **3 VE**; RSZ2025 **88.993**; leftover of mined **city_asse**; maatwerk@3wplus.be; beschutte/sociale werkplaatsen PC 32701). Identity trap: 0467.004.520 ≠ 3Wplus Kinderopvang **0893.870.539** remine ≠ AMAB **0411.635.039** remine ≠ GROEP 3WPLUS **0674.926.988** ≠ Hopperank **0434.363.921** remine ≠ Vijverbeek **0448.164.744** remine ≠ Hof ter Waarbeek **0478.728.256** remine ≠ Walfergem **0633.687.439** remine. 3 VE leftover of mined city_asse (Z. 5 Mollem 250 Asse + Solheide 16 Overijse + Marcel Felicestraat 29 Hoeilaart; zetel Mollem 250). Confirmed leftover public maatwerk not convent / not private / not CIK / not WZC / not commercial NV. VKT-VZW **native text** (not scan) — 309825 B / 26p all native euros (VKT-VZW 7 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00271890** (309825 B / 26p; AV **26.06.2026**; header **09.07.2026**; official NBB UUID 2362fb06-7b77-11f1-886f-e597a8377b24; CDN GET **200** 309825 official NBB-generated OpenPDF 1.3.26 CreationDate 09.07.2026 Last-Modified 29.07.2026 MD5 8c29488f1a1fae7afecd118ca9f27390; all 26p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **EUR1000** DROP −93.85% (was 16250); envelope bruto 9900 **EUR2631017** JUMP +5.66% (VKT because omzet empty; was 2490048); 62 **EUR2340946** JUMP +1.03%; 630 **EUR147618** JUMP +2.24%; 66A **empty** DROP (was 2453); 640/8 **EUR75412** JUMP +412.97%; 635/9 **empty**; 631/4 **empty**; bedrijfswinst 9901 **EUR67042** JUMP +487.88% (was 11404); pnl 9904 **EUR49057** FLIP (was LOSS −4970); equity **EUR1625771** JUMP +2.12%; assets **EUR3392304** DROP −0.84%; debt **EUR1766533** DROP −3.39%; FTE **56.8** JUMP +3.27% (was 55; 100 56.8; 105 57.6); kapitaalsubsidies **EUR63475** DROP −19.42%; destin 691 **empty**; 791 **empty**; cash **EUR494869** JUMP +1.36%; geldbeleggingen **empty**; gebouwen **EUR1802320** JUMP; MVA 22/27 **EUR2320375** JUMP; aanbouw **EUR3236** DROP; capex **EUR226984**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 3 VE leftover mined city_asse maatwerk. NOT 3Wplus Kinderopvang remine. NOT AMAB remine. NOT GROEP 3WPLUS. NOT Hopperank remine. NOT Vijverbeek remine. NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.30); entities (+1 vzw_3wplus_werk_asse); foi + draft `gap_3wplus_werk_asse_maatwerk_matrix_bruto_2_63m_omzet73_empty_pnl_flip_49k_l5`; rq_2492=done + rq_2493 open; loop_state ticks=2492; raw tick2492/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2500**). Next: rq_2493 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT 3Wplus Werk remine / NOT Hopperank remine / NOT De Sperwer remine / NOT Alderande remine / NOT De Hagewinde remine / NOT AMAB remine / NOT Hof ter Waarbeek remine / NOT Walfergem remine / NOT 3Wplus Kinderopvang remine / NOT Vijverbeek remine / NOT GROEP 3WPLUS / NOT leftover-via-VE / NOT MILLE LUCI CVBA no JR / NOT Huis Coppens commercial / NOT Armonea commercial / NOT Vulpia commercial / NOT Korian commercial / NOT Evara remine / NOT Zorg-Saam remine). NOW leftover city_asse maatwerk taken (CIK + VAPH already taken). Leftover WZC/CAR of city_asse still open but remine-heavy.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("RQ STATE LOG DONE")
