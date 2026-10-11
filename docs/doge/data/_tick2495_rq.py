from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2495_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2495,")!=1: raise SystemExit(f"bad 2495 count {rq_raw.count(b'rq_2495,')}")
if b"rq_2496," in rq_raw: raise SystemExit("2496 exists")
idx=rq_raw.rfind(b"rq_2495,")
if idx<0: raise SystemExit("rq_2495 not found")
new_2495=(
"rq_2495,leftover dual Zorgnetwerk Trento YE2025,hole_fill,8,done,L5,vzw_zorgnetwerk_trento_hamme,"
"Took unused leftover public WZC Zorgnetwerk Trento 0455.449.048 leftover mined city_hamme. Official NBB VOL-VZW YE2025 2026-00304248 native statutory 45p 1.14MB. Envelope omzet 70 JUMP 13434174 (material not commercial-only; 73 JUMP 3051871; 76A empty); pnl JUMP 362341; destin JUMP 2300000; cash DROP 1921671; FTE 186.5. FIRST leftover unused + live official YE2025 after leftover-type hunt (cached KBO activity NACE 87301 Zele VE led to Hamme-seated parent; unused leftover mined city_hamme; MAXIMUS BV SKIP; EigenWijzer OCMW SKIP; Inspiration Fields OCMW SKIP; Ter Dorpe BV SKIP; Oude Melkerij BV SKIP). NOT leftover city_zele. NOT De Vlietoever BV. NOT Woonzorg Samen Ouder remine. NOT Avondzon remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2495 leftover mined city_hamme WZC; Strong native PDF; 2 VE; prior-year identical; next rq_2496 NOT every-10 (next every-10 is 2500)\n"
)
new_2496=(
"rq_2496,leftover dual hunt after Trento,hole_fill,8,open,L5,,"
"NOT every-10 (next every-10 is 2500). Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde / geel / herentals (Sint-Anna OCMW skip) / eeklo (Kinderlach YE2024; De Vierklaver 0436.015.889 unused leftover VAPH YE2025 still open) / halle (CIK+CAR taken; leftover WZC exhausted; leftover VAPH still open — De Poel leftover-via-VE SKIP; KEERPUNT 0461.049.710 unused YE2025 still open) / kalmthout / bornem (CAR taken; leftover WZC/VAPH commercials/remines) / puurs (maatwerk taken; leftover WZC/VAPH remine/commercial) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde (Zorgbedrijf Vilvoorde OCMW skip) / mol / zoersel (Doppa VAPH taken — leftover WZC commercials Joostens/Halmolen/Ter Dorpe BV) / schilde (Pegode 0420.281.501 unused leftover VAPH YE2025 still open) / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken; ACROPOLYS NV commercial) / schoten (VAPH taken; MAXIMUS BV commercial; Oude Melkerij BV commercial) / lokeren (VAPH Hagewinde+Alderande taken; maatwerk De Sperwer taken — leftover WZC/CAR remine; ZENITH BV commercial SKIP) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK+WZC taken) / ninove (CIK taken; leftover WZC/VAPH still open) / asse (CIK+VAPH+maatwerk taken; leftover WZC/CAR remine-heavy) / erpe_mere (WZC Avondzon taken — leftover VAPH/CAR/maatwerk/CIK still open; WZC Sint-Vincentius YE2024 SKIP) / zele (leftover WZC still open — De Vliet is Hamme-seated Trento VE not leftover city_zele) / hamme (WZC Trento taken). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT Trento remine. NOT Avondzon remine. NOT Doppa remine. NOT 3Wplus Werk remine. NOT Hopperank remine. NOT De Sperwer remine. NOT Alderande remine. NOT De Hagewinde remine. NOT leftover city_zele via Trento VE. NOT De Vlietoever BV. NOT Woonzorg Samen Ouder remine. NOT MAXIMUS BV. NOT EigenWijzer OCMW. NOT Inspiration Fields OCMW. NOT Ter Dorpe BV. NOT Oude Melkerij BV. NOT De Poel leftover-via-VE. NOT ASTOR bankrupt. NOT Aralea YE2024. NOT CAR Kapelhof Drongen OFF. NOT AMAB remine. NOT Hof ter Waarbeek remine. NOT Walfergem remine. NOT 3Wplus Kinderopvang remine. NOT Vijverbeek remine. NOT leftover-via-VE. NOT MILLE LUCI CVBA no JR. NOT Huis Coppens commercial. NOT GROEP 3WPLUS. NOT ACROPOLYS NV. NOT Foyer De Lork remine. NOT Corazon no JR. NOT Al-arm no JR. NOT ZENITH BV. NOT An for All CommV. NOT Studijo Bos CV. NOT Sint-Anna OCMW. NOT Zorgbedrijf Vilvoorde OCMW. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2495 leftover city_hamme WZC; Trento taken leftover mined city_hamme WZC; Avondzon taken leftover mined city_erpe_mere WZC; Doppa taken leftover mined city_zoersel VAPH; NOT every-10 (next 2500)\n"
)
if new_2495.count("\n")!=1 or new_2496.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2495",new_2495),("2496",new_2496)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2495.encode("utf-8"))
    f.write(new_2496.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2495", chk.count(b"rq_2495,"), "n2496", chk.count(b"rq_2496,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2495,2495,no,tick2495 leftover dual Zorgnetwerk Trento 0455.449.048 Strong native PDF (omzet70 JUMP 13434174 material not commercial-only; 73 JUMP 3051871; 76A empty; envelope omzet70 JUMP 13434174; pnl JUMP 362341; 9901 JUMP 331288; equity JUMP 13774142; assets DROP 19824343; debt DROP 6050201; FTE DROP 186.5; kapitaalsubsidies DROP 534830; destin691 JUMP 2300000; 791 empty; cash DROP 1921671; geldbeleggingen JUMP 5290614; capex 328573; 2 VE leftover city_hamme WZC); leftover mined city_hamme WZC; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (cached KBO activity NACE 87301 Zele VE; Hamme-seated parent; MAXIMUS BV SKIP; EigenWijzer OCMW SKIP); NOT leftover city_zele; NOT De Vlietoever BV; NOT Woonzorg Samen Ouder remine; NOT Avondzon remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2496 NOT every-10 (next every-10 is 2500)\n",
encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
