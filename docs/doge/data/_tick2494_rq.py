from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2494_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2494,")!=1: raise SystemExit(f"bad 2494 count {rq_raw.count(b'rq_2494,')}")
if b"rq_2495," in rq_raw: raise SystemExit("2495 exists")
idx=rq_raw.rfind(b"rq_2494,")
if idx<0: raise SystemExit("rq_2494 not found")
new_2494=(
"rq_2494,leftover dual Avondzon Erpe YE2025,hole_fill,8,done,L5,vzw_avondzon_erpe_mere,"
"Took unused leftover public WZC Avondzon Erpe 0419.044.057 leftover mined city_erpe_mere. Official NBB VOL-VZW YE2025 2026-00283016 native statutory 44p 3.09MB. Envelope omzet 70 JUMP 11741711 (material not commercial-only; 73 DROP 2192121; 76A DROP 76278); pnl FLIP LOSS 54204; destin empty; FTE 141.3. FIRST leftover unused + live official YE2025 after leftover-type hunt (KBO activity NACE 87101 + leftover-open postcode 9420; ZENITH BV commercial SKIP; An for All CommV SKIP; Studijo Bos CV no YE2025 SKIP; Sint-Anna OCMW SKIP; Zorgbedrijf Vilvoorde OCMW SKIP). NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT De Zonnewende remine. NOT Doppa remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2494 leftover mined city_erpe_mere WZC; Strong native PDF; 1 VE; prior-year identical; next rq_2495 NOT every-10 (next every-10 is 2500)\n"
)
new_2495=(
"rq_2495,leftover dual hunt after Avondzon,hole_fill,8,open,L5,,"
"NOT every-10 (next every-10 is 2500). Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde (Zonneschijn CIK taken) / geel (Augustientjes CIK taken; leftover VAPH/CAR/WZC/maatwerk but Foyer De Lork remine / Corazon no JR / Al-arm no JR) / herentals (Bremdael WZC taken; leftover VAPH/CAR; OpWeg YE2024; Sint-Anna OCMW SKIP; An for All CommV SKIP) / eeklo (Kinderlach YE2024) / halle (CAR + CIK taken; leftover WZC exhausted; leftover VAPH still open — De Poel leftover-via-VE SKIP) / kalmthout (MILLE LUCI CVBA no JR) / bornem (CAR taken; leftover WZC/VAPH commercials/remines) / puurs (maatwerk taken; leftover WZC/VAPH remine/commercial) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde (Zorgbedrijf Vilvoorde OCMW skip) / mol / zoersel (Doppa VAPH taken — leftover WZC commercials Joostens/Halmolen) / schilde / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken; ACROPOLYS NV commercial) / schoten (VAPH taken; Studijo Bos CV no YE2025) / lokeren (VAPH Hagewinde + Alderande taken; maatwerk De Sperwer taken — leftover WZC/CAR remine; ZENITH BV commercial SKIP) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK + WZC taken) / ninove (CIK taken; leftover WZC/VAPH still open) / asse (CIK + VAPH Hopperank + maatwerk 3WPLUS WERK taken — leftover WZC/CAR remine-heavy) / erpe_mere (WZC Avondzon taken — leftover VAPH/CAR/maatwerk/CIK still open; WZC Sint-Vincentius YE2024 SKIP). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT Avondzon remine. NOT Doppa remine. NOT 3Wplus Werk remine. NOT Hopperank remine. NOT De Sperwer remine. NOT Alderande remine. NOT De Hagewinde remine. NOT De Cirkel remine. NOT De Kapoentjes remine. NOT De Zonnewende remine. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT Huize De Veuster remine. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Nektari remine. NOT Reva Ter Linde remine. NOT BWP remine. NOT De Poel leftover-via-VE. NOT ASTOR bankrupt. NOT Aralea YE2024. NOT CAR Kapelhof Drongen OFF. NOT AMAB remine. NOT Hof ter Waarbeek remine. NOT Walfergem remine. NOT 3Wplus Kinderopvang remine. NOT Vijverbeek remine. NOT ViTeS leftover-via-VE. NOT Groep INTRO leftover-via-VE. NOT Mirto leftover-via-VE. NOT Mivas leftover-via-VE. NOT MILLE LUCI CVBA no JR. NOT Huis Coppens commercial. NOT GROEP 3WPLUS. NOT ACROPOLYS NV. NOT Foyer De Lork remine. NOT Corazon no JR. NOT Al-arm no JR. NOT ZENITH BV. NOT An for All CommV. NOT Studijo Bos CV. NOT Sint-Anna OCMW. NOT Zorgbedrijf Vilvoorde OCMW. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2494 leftover city_erpe_mere WZC; Avondzon taken leftover mined city_erpe_mere WZC; Doppa taken leftover mined city_zoersel VAPH; 3WPLUS WERK taken leftover mined city_asse maatwerk; Hopperank taken leftover mined city_asse VAPH; NOT every-10 (next 2500)\n"
)
if new_2494.count("\n")!=1 or new_2495.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2494",new_2494),("2495",new_2495)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2494.encode("utf-8"))
    f.write(new_2495.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2494", chk.count(b"rq_2494,"), "n2495", chk.count(b"rq_2495,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2494,2494,no,tick2494 leftover dual Avondzon Erpe 0419.044.057 Strong native PDF (omzet70 JUMP 11741711 material not commercial-only; 73 DROP 2192121; 76A DROP 76278; envelope omzet70 JUMP 11741711; pnl FLIP LOSS 54204; 9901 DROP 127652; equity DROP 9411942; assets DROP 24696447; debt DROP 15284505; FTE DROP 141.3; kapitaalsubsidies DROP 50886; destin691 empty; 791 empty; cash DROP 547038; geldbeleggingen JUMP 941385; capex 360865; 1 VE leftover city_erpe_mere WZC); leftover mined city_erpe_mere WZC; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (KBO activity NACE 87101; ZENITH BV SKIP; An for All CommV SKIP; Studijo Bos CV SKIP; Sint-Anna OCMW SKIP); NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT De Zonnewende remine; NOT Doppa remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2495 NOT every-10 (next every-10 is 2500)\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2494 - rq_2494 Avondzon Erpe-Mere (omzet JUMP 11.74m / 73 DROP 2.19m / pnl FLIP LOSS 54k / Strong PDF)

- Unit: **rq_2494** leftover dual after **Doppa@2493**. NOT every-10 (next **2500**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of a mined Flanders city with official YE2025 native PDF. STOP leftover-note loop. Official KBO activity NACE **88106 / 87101 / 88993 / 87201** + leftover-open city postcodes + NBB YE2025 (session). FIRST leftover unused + live official YE2025 native euros after leftover-type hunt: ZENITH **0886.521.701** BV Lokeren commercial SKIP; An for All **1016.303.444** CommV Herentals commercial SKIP; Studijo Bos **1029.452.783** CV Schoten no YE2025 SKIP; Welzijnsvereniging Sint-Anna **1011.411.080** Herentals OCMW SKIP; Zorgbedrijf Vilvoorde **0697.787.118** OCMW SKIP; PARTNERS IN MAATWERK **0657.969.410** no legal personality SKIP; ACROPOLYS **0440.345.653** NV commercial SKIP; RUBO BTW-eenheid SKIP; Re-HEAD YE2024 leftovers still YE2024. Confirmed `city_erpe_mere` exists (mined; leftover WZC unused — WZC Sint-Vincentius **0422.620.585** YE2024 SKIP). Took FREE leftover Flemish **AVONDZON ERPE VZW** YE2025 (KBO **0419.044.057**; zetel Botermelkstraat 12 9420 Erpe-Mere; **Actief** **1 VE** since 28.10.1978; RSZ2025 **87.101**; leftover of mined **city_erpe_mere**; info@avondzon.be; WZC/RVT + assistentiewoningen). Identity trap: 0419.044.057 ≠ WZC Sint-Vincentius Erpe-Mere **0422.620.585** YE2024 ≠ De Zonnewende **0735.627.214** remine ≠ Doppa remine ≠ Zorgbedrijf Vilvoorde OCMW ≠ Sint-Anna OCMW. 1 VE leftover of mined city_erpe_mere (zetel Botermelkstraat 12). Confirmed leftover public WZC not convent / not private / not CIK / not VAPH / not commercial NV. VOL-VZW **native text** (not scan) — 3089772 B / 44p native statutory euros (VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.4.1-3 6.5.1-3 6.14 6.16 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00283016** (3089772 B / 44p; AV **24.06.2026**; header **10.07.2026**; official NBB UUID b1f510be-7c58-11f1-80db-a734674e7150; CDN GET **200** 3089772 official NBB-generated OpenPDF 1.3.26 CreationDate 13.07.2026 Last-Modified 30.07.2026 MD5 dcc85424deb07dcadc5364b2a186b781; statutory pages native; prior-year identical not restated; commissaris NV Callens Vandelanotte / Roef Mathias) — omzet 70 **EUR11741711** JUMP +0.69% (material not commercial-only; was 11661740; 6.9 WZC+DVC 9171930 / AW 2569780); 73 **EUR2192121** DROP −1.49% (was 2229265; 733 2192121); 76A **EUR76278** DROP −27.19% (was 104759); envelope omzet 70 **EUR11741711** JUMP +0.69% (VZW because omzet material not commercial-only); 70/76A **EUR14259492** JUMP +0.49%; 74 **EUR249382** JUMP; 62 **EUR8783930** JUMP +3.23%; 630 **EUR1606910** JUMP +1.11%; 66A **EUR38009** JUMP; 640/8 **EUR107368** DROP −40.58%; 635/9 **empty**; 631/4 **EUR10815** DROP; bedrijfswinst 9901 **EUR127652** DROP −83.10% (was 755117); pnl 9904 **EUR-54204** FLIP LOSS (was +540121); equity **EUR9411942** DROP −0.72%; assets **EUR24696447** DROP −4.67%; debt **EUR15284505** DROP −6.95%; FTE **141.3** DROP −0.42% (was 141.9; 1003 141.3; 9087 141.3; 9086 174; 105 139.8); kapitaalsubsidies **EUR50886** DROP −22.03%; destin 691 **empty**; 791 **empty**; cash **EUR547038** DROP −19.92%; geldbeleggingen **EUR941385** JUMP +1.31%; gebouwen **EUR12848600** DROP; MVA 22/27 **EUR21519498** DROP; aanbouw **EUR6542** JUMP; capex **EUR360865**. Strong KBO + Strong PDF (native statutory; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_erpe_mere WZC. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT De Zonnewende remine. NOT Doppa remine. NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.54); entities (+1 vzw_avondzon_erpe_mere); foi + draft `gap_avondzon_erpe_mere_wzc_matrix_omzet_11_74m_73_drop_2_19m_pnl_flip_loss_54k_l5`; rq_2494=done + rq_2495 open; loop_state ticks=2494; raw tick2494/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2500**). Next: rq_2495 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Avondzon remine / NOT Doppa remine / NOT 3Wplus Werk remine / NOT Hopperank remine / NOT De Sperwer remine / NOT Alderande remine / NOT De Hagewinde remine / NOT AMAB remine / NOT Hof ter Waarbeek remine / NOT Walfergem remine / NOT 3Wplus Kinderopvang remine / NOT Vijverbeek remine / NOT GROEP 3WPLUS / NOT leftover-via-VE / NOT MILLE LUCI CVBA no JR / NOT Huis Coppens commercial / NOT ACROPOLYS NV / NOT Foyer De Lork remine / NOT Corazon no JR / NOT Al-arm no JR / NOT ZENITH BV / NOT An for All CommV / NOT Studijo Bos CV / NOT Sint-Anna OCMW / NOT Zorgbedrijf Vilvoorde OCMW / NOT WZC Sint-Vincentius Erpe-Mere YE2024 / NOT Armonea commercial / NOT Vulpia commercial / NOT Korian commercial / NOT Evara remine / NOT Zorg-Saam remine). NOW leftover city_erpe_mere WZC taken. Leftover VAPH/CAR/maatwerk/CIK of city_erpe_mere still open.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("RQ STATE LOG DONE")
