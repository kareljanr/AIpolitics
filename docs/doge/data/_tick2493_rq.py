from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2493_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2493,")!=1: raise SystemExit(f"bad 2493 count {rq_raw.count(b'rq_2493,')}")
if b"rq_2494," in rq_raw: raise SystemExit("2494 exists")
idx=rq_raw.rfind(b"rq_2493,")
if idx<0: raise SystemExit("rq_2493 not found")
new_2493=(
"rq_2493,leftover dual Doppa YE2025,hole_fill,8,done,L5,vzw_doppa_zoersel,"
"Took unused leftover public VAPH Doppa 0836.745.160 leftover mined city_zoersel. Official NBB VKT-VZW YE2025 2026-00172866 native statutory 13p 50.9kB. Envelope bruto 9900 DROP 2540982 (omzet+73 empty VKT; 76A DROP 3510); pnl FLIP LOSS 106107; destin empty; FTE 32. FIRST leftover unused + live official YE2025 after leftover-type hunt (KBO activity NACE 88106 + leftover-open postcode 2980; Foyer De Lork remine SKIP; Corazon no JR SKIP; Al-arm no JR SKIP; ACROPOLYS NV commercial SKIP). NOT AGB Zoersel remine. NOT Joostens commercial. NOT Halmolen Vulpia commercial. NOT 3Wplus Werk remine. NOT Hopperank remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2493 leftover mined city_zoersel VAPH; Strong native PDF; 1 VE; prior-year identical; next rq_2494 NOT every-10 (next every-10 is 2500)\n"
)
new_2494=(
"rq_2494,leftover dual hunt after Doppa,hole_fill,8,open,L5,,"
"NOT every-10 (next every-10 is 2500). Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde (Zonneschijn CIK taken) / geel (Augustientjes CIK taken; leftover VAPH/CAR/WZC/maatwerk but Foyer De Lork remine / Corazon no JR / Al-arm no JR) / herentals (Bremdael WZC taken; leftover VAPH/CAR; OpWeg YE2024) / eeklo (Kinderlach YE2024) / halle (CAR + CIK taken; leftover WZC exhausted; leftover VAPH still open — De Poel leftover-via-VE SKIP) / kalmthout (MILLE LUCI CVBA no JR) / bornem (CAR taken; leftover WZC/VAPH commercials/remines) / puurs (maatwerk taken; leftover WZC/VAPH remine/commercial) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde / mol / zoersel (Doppa VAPH taken — leftover WZC commercials Joostens/Halmolen) / schilde / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken; ACROPOLYS NV commercial) / schoten (VAPH taken) / lokeren (VAPH Hagewinde + Alderande taken; maatwerk De Sperwer taken — leftover WZC/CAR remine) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK + WZC taken) / ninove (CIK taken; leftover WZC/VAPH still open) / asse (CIK + VAPH Hopperank + maatwerk 3WPLUS WERK taken — leftover WZC/CAR remine-heavy). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT Doppa remine. NOT 3Wplus Werk remine. NOT Hopperank remine. NOT De Sperwer remine. NOT Alderande remine. NOT De Hagewinde remine. NOT De Cirkel remine. NOT De Kapoentjes remine. NOT De Zonnewende remine. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT Huize De Veuster remine. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Nektari remine. NOT Reva Ter Linde remine. NOT BWP remine. NOT De Poel leftover-via-VE. NOT ASTOR bankrupt. NOT Aralea YE2024. NOT CAR Kapelhof Drongen OFF. NOT AMAB remine. NOT Hof ter Waarbeek remine. NOT Walfergem remine. NOT 3Wplus Kinderopvang remine. NOT Vijverbeek remine. NOT ViTeS leftover-via-VE. NOT Groep INTRO leftover-via-VE. NOT Mirto leftover-via-VE. NOT Mivas leftover-via-VE. NOT MILLE LUCI CVBA no JR. NOT Huis Coppens commercial. NOT GROEP 3WPLUS. NOT ACROPOLYS NV. NOT Foyer De Lork remine. NOT Corazon no JR. NOT Al-arm no JR. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2493 leftover city_zoersel VAPH; Doppa taken leftover mined city_zoersel VAPH; 3WPLUS WERK taken leftover mined city_asse maatwerk; Hopperank taken leftover mined city_asse VAPH; NOT every-10 (next 2500)\n"
)
if new_2493.count("\n")!=1 or new_2494.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2493",new_2493),("2494",new_2494)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2493.encode("utf-8"))
    f.write(new_2494.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2493", chk.count(b"rq_2493,"), "n2494", chk.count(b"rq_2494,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2493,2493,no,tick2493 leftover dual Doppa 0836.745.160 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A DROP 3510; envelope bruto9900 DROP 2540982; pnl FLIP LOSS 106107; 9901 FLIP LOSS 123586; equity DROP 1531949; assets DROP 1891357; debt DROP 359408; FTE DROP 32; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 88271; geldbeleggingen DROP 881350; capex 23080; 1 VE leftover city_zoersel VAPH); leftover mined city_zoersel VAPH; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (KBO activity NACE 88106; Foyer De Lork remine SKIP; Corazon no JR SKIP; Al-arm no JR SKIP; ACROPOLYS NV SKIP); NOT AGB Zoersel remine; NOT Joostens commercial; NOT Halmolen Vulpia commercial; NOT 3Wplus Werk remine; NOT Hopperank remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2494 NOT every-10 (next every-10 is 2500)\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2493 - rq_2493 Doppa Zoersel (bruto DROP 2.54m / omzet+73 empty VKT / pnl FLIP LOSS 106k / Strong PDF)

- Unit: **rq_2493** leftover dual after **3Wplus Werk@2492**. NOT every-10 (next **2500**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of a mined Flanders city with official YE2025 native PDF. STOP leftover-note loop. Official KBO activity NACE **88106 / 87101 / 88993 / 87201** + leftover-open city postcodes + NBB YE2025 (session). FIRST leftover unused + live official YE2025 native euros after leftover-type hunt: Foyer De Lork **0446.022.331** remine SKIP; Corazon **0700.553.596** no JR SKIP; Al-arm **0880.359.429** no JR SKIP; ACROPOLYS **0440.345.653** NV commercial SKIP; PARTNERS IN MAATWERK **0657.969.410** no legal personality SKIP; RUBO BTW-eenheid SKIP; Steunfonds Mivalti no JR SKIP; Zorgbedrijf Vilvoorde OCMW SKIP; Re-HEAD YE2024 leftovers still YE2024. Confirmed `city_zoersel` exists (mined; leftover WZC commercials Joostens/Halmolen — leftover unused VAPH). Took FREE leftover Flemish **DOPPA VZW** / Dienst Ondersteuningsplan Provincie Antwerpen YE2025 (KBO **0836.745.160**; zetel Zandstraat 46 2980 Zoersel; **Actief** **1 VE** **2.204.301.838** TRAJECT since 01.12.2011; RSZ2025 **88.106**; leftover of mined **city_zoersel**; info@doppa.be; VAPH ondersteuningsplan / PVF). Identity trap: 0836.745.160 ≠ AGB Zoersel remine ≠ WZC Joostens Zorgbedrijf Antwerpen ≠ Halmolen Vulpia ≠ 3Wplus Werk **0467.004.520** remine ≠ Hopperank **0434.363.921** remine ≠ Foyer De Lork remine ≠ MPI Oosterlo remine. 1 VE leftover of mined city_zoersel (zetel + VE Zandstraat 46). Confirmed leftover public VAPH not convent / not private / not CIK / not WZC / not commercial NV. VKT-VZW **native text** (not scan) — 50888 B / 13p all native euros (VKT-VZW 6.1.1 6.3 6.5 6.6 7 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00172866** (50888 B / 13p; AV **08.06.2026**; header **16.06.2026**; official NBB UUID 54a001b8-6992-11f1-ba33-47adf9e6d406; CDN GET **200** 50888 official NBB-generated OpenPDF 1.3.26 CreationDate 18.06.2026 Last-Modified 22.06.2026 MD5 328f7082865c74385115660898ea66dc; all 13p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **EUR3510** DROP −97.67% (was 150706); envelope bruto 9900 **EUR2540982** DROP −4.30% (VKT because omzet empty; was 2655050); 62 **EUR2608339** JUMP +0.44%; 630 **EUR36698** JUMP +74.92%; 66A **EUR2676** JUMP (was empty); 640/8 **EUR16855** DROP −14.27%; 635/9 **empty**; 631/4 **empty**; bedrijfswinst 9901 **EUR-123586** FLIP LOSS (was +17384); pnl 9904 **EUR-106107** FLIP LOSS (was +40968); equity **EUR1531949** DROP −6.48%; assets **EUR1891357** DROP −7.57%; debt **EUR359408** DROP −11.95%; FTE **32** DROP −4.76% (was 33.6; 100 32; 9087 32; 105 32); kapitaalsubsidies **empty**; destin 691 **empty**; 791 **empty**; cash **EUR88271** JUMP +12.79%; geldbeleggingen **EUR881350** DROP −10.88%; gebouwen **EUR832430** DROP; MVA 22/27 **EUR855294** DROP; aanbouw **empty**; capex **EUR23080**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_zoersel VAPH. NOT AGB Zoersel remine. NOT Joostens commercial. NOT Halmolen Vulpia commercial. NOT 3Wplus Werk remine. NOT Hopperank remine. NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.28); entities (+1 vzw_doppa_zoersel); foi + draft `gap_doppa_zoersel_vaph_matrix_bruto_2_54m_omzet73_empty_pnl_flip_loss_106k_l5`; rq_2493=done + rq_2494 open; loop_state ticks=2493; raw tick2493/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2500**). Next: rq_2494 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Doppa remine / NOT 3Wplus Werk remine / NOT Hopperank remine / NOT De Sperwer remine / NOT Alderande remine / NOT De Hagewinde remine / NOT AMAB remine / NOT Hof ter Waarbeek remine / NOT Walfergem remine / NOT 3Wplus Kinderopvang remine / NOT Vijverbeek remine / NOT GROEP 3WPLUS / NOT leftover-via-VE / NOT MILLE LUCI CVBA no JR / NOT Huis Coppens commercial / NOT ACROPOLYS NV / NOT Foyer De Lork remine / NOT Corazon no JR / NOT Al-arm no JR / NOT Armonea commercial / NOT Vulpia commercial / NOT Korian commercial / NOT Evara remine / NOT Zorg-Saam remine). NOW leftover city_zoersel VAPH taken. Leftover WZC of city_zoersel still open but Joostens/Halmolen commercial.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("RQ STATE LOG DONE")
