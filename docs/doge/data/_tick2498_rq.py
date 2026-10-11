from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2498_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2498,")!=1: raise SystemExit(f"bad 2498 count {rq_raw.count(b'rq_2498,')}")
if b"rq_2499," in rq_raw: raise SystemExit("2499 exists")
idx=rq_raw.rfind(b"rq_2498,")
if idx<0: raise SystemExit("rq_2498 not found")
new_2498=(
"rq_2498,leftover dual Meredal YE2025,hole_fill,8,done,L5,vzw_meredal_erpe_mere,"
"Took unused leftover public WZC Meredal 0419.333.671 leftover mined city_erpe_mere. Official NBB VOL-VZW YE2025 2026-00108199 native statutory 44p 1.68MB. Envelope omzet70 JUMP 8224110 (material not commercial-only; 73 DROP 1091421; 76A DROP 10); pnl DROP 185241; cash DROP 1316785; FTE 92.4. FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_niel WZC Maria Boodschap absorbed SKIP; leftover unused WZC of mined city_erpe_mere). NOT Avondzon remine. NOT WZC Sint-Vincentius YE2024. NOT Maria Boodschap absorbed. NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2498 leftover mined city_erpe_mere WZC; Strong native PDF; 1 VE; prior-year identical; next rq_2499 NOT every-10 (next every-10 is 2500)\n"
)
new_2499=(
"rq_2499,leftover dual hunt after Meredal,hole_fill,8,open,L5,,"
"NOT every-10 (next every-10 is 2500). Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde / geel / herentals (Sint-Anna OCMW skip) / eeklo (Kinderlach YE2024; leftover VAPH Ascendere already taken; De Vierklaver is Deinze-seated not leftover city_eeklo) / halle (CIK+CAR taken; leftover WZC exhausted; leftover VAPH still open — De Poel leftover-via-VE SKIP; KEERPUNT 0461.049.710 zetel Gent leftover-via-VE SKIP if Halle VE) / kalmthout / bornem (CAR taken; leftover WZC/VAPH commercials/remines) / puurs (maatwerk taken; leftover WZC/VAPH remine/commercial) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde (Zorgbedrijf Vilvoorde OCMW skip) / mol / zoersel (Doppa VAPH taken — leftover WZC commercials Joostens/Halmolen/Ter Dorpe BV) / schilde (Pegode is leftover city_kontich not leftover city_schilde; Oude Melkerij BV skip) / denderleeuw (WZC Ter Bake/Rodenbach Armonea commercial) / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken) / schoten (VAPH taken; MAXIMUS BV commercial; Oude Melkerij BV commercial) / lokeren (VAPH Hagewinde+Alderande taken; maatwerk De Sperwer taken — leftover WZC/CAR remine; ZENITH BV commercial SKIP) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK+WZC taken) / ninove (CIK taken; leftover WZC/VAPH still open) / asse (CIK+VAPH+maatwerk taken; leftover WZC/CAR remine-heavy) / erpe_mere (WZC Avondzon + Meredal taken — leftover VAPH/CAR/maatwerk/CIK still open; WZC Sint-Vincentius YE2024 SKIP) / zele (leftover WZC still open — De Vliet is Hamme-seated Trento VE not leftover city_zele) / hamme (WZC Trento taken) / deinze (VAPH Vierklaver taken) / niel (Maria Boodschap 0415.653.116 absorbed 01.01.2025 into De Medemens 0428.692.191 Antwerp-seated leftover-via-VE SKIP; leftover city_niel still unused) / kontich (VAPH Pegode taken). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT Meredal remine. NOT Avondzon remine. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT Maria Boodschap absorbed. NOT De Medemens leftover-via-VE. NOT leftover city_niel via Maria Boodschap. NOT Pegode remine. NOT leftover city_niel via Pegode VE. NOT leftover city_schilde via Pegode VE. NOT Iris remine. NOT De Dageraad remine. NOT Vierklaver remine. NOT leftover city_eeklo via Vierklaver VE. NOT Leieborg remine. NOT Demival remine. NOT Ascendere remine. NOT Trento remine. NOT Doppa remine. NOT 3Wplus Werk remine. NOT Hopperank remine. NOT De Sperwer remine. NOT Alderande remine. NOT De Hagewinde remine. NOT leftover city_zele via Trento VE. NOT De Vlietoever BV. NOT Woonzorg Samen Ouder remine. NOT MAXIMUS BV. NOT EigenWijzer OCMW. NOT Inspiration Fields OCMW. NOT Ter Dorpe BV. NOT Oude Melkerij BV. NOT De Poel leftover-via-VE. NOT ASTOR bankrupt. NOT Aralea YE2024. NOT CAR Kapelhof Drongen OFF. NOT AMAB remine. NOT leftover-via-VE. NOT MILLE LUCI CVBA no JR. NOT Huis Coppens commercial. NOT GROEP 3WPLUS. NOT ACROPOLYS NV. NOT Foyer De Lork remine. NOT Corazon no JR. NOT Al-arm no JR. NOT ZENITH BV. NOT An for All CommV. NOT Studijo Bos CV. NOT Sint-Anna OCMW. NOT Zorgbedrijf Vilvoorde OCMW. NOT KEERPUNT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2498 leftover city_erpe_mere WZC; Meredal taken leftover mined city_erpe_mere WZC; Avondzon already taken leftover mined city_erpe_mere WZC; leftover city_niel still unused; NOT every-10 (next 2500)\n"
)
if new_2498.count("\n")!=1 or new_2499.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2498",new_2498),("2499",new_2499)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2498.encode("utf-8"))
    f.write(new_2499.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2498", chk.count(b"rq_2498,"), "n2499", chk.count(b"rq_2499,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2498,2498,no,tick2498 leftover dual Meredal 0419.333.671 Strong native PDF (omzet70 JUMP 8224110 material not commercial-only; 73 DROP 1091421; 76A DROP 10; envelope omzet70 JUMP 8224110; 70/76A JUMP 9464409; pnl DROP 185241; 9901 DROP 374227; equity JUMP 10586696; assets DROP 20590835; debt DROP 9571459; FTE JUMP 92.4; kapitaalsubsidies DROP 0; destin691 DROP 185241; cash DROP 1316785; geldbeleggingen JUMP 4081030; capex 63438; 1 VE leftover city_erpe_mere WZC); leftover mined city_erpe_mere WZC; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_niel WZC Maria Boodschap absorbed SKIP); NOT Avondzon remine; NOT WZC Sint-Vincentius YE2024; NOT Maria Boodschap absorbed; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2499 NOT every-10 (next every-10 is 2500)\n",
encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
