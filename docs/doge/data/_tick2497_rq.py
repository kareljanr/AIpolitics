from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2497_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2497,")!=1: raise SystemExit(f"bad 2497 count {rq_raw.count(b'rq_2497,')}")
if b"rq_2498," in rq_raw: raise SystemExit("2498 exists")
idx=rq_raw.rfind(b"rq_2497,")
if idx<0: raise SystemExit("rq_2497 not found")
new_2497=(
"rq_2497,leftover dual Pegode YE2025,hole_fill,8,done,L5,vzw_pegode_kontich,"
"Took unused leftover public VAPH Pegode 0420.281.501 leftover mined city_kontich. Official NBB VOL-VZW YE2025 2026-00293740 native statutory 47p 1.88MB. Envelope 70/76A JUMP 18110069 (omzet commercial-only vs large 73 JUMP 15317093; 76A JUMP 741511); pnl JUMP 629938; cash JUMP 1497839; FTE 174.6. FIRST leftover unused + live official YE2025 after leftover-type hunt (FIRST spotted unused YE2025 leftover Pegode; official KBO zetel Kontich not Niel; leftover mined city_kontich VAPH unused). NOT leftover city_niel. NOT leftover city_schilde. NOT Iris remine. NOT De Dageraad remine. NOT Vierklaver remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2497 leftover mined city_kontich VAPH; Strong native PDF; 19 VE; prior-year identical; next rq_2498 NOT every-10 (next every-10 is 2500)\n"
)
new_2498=(
"rq_2498,leftover dual hunt after Pegode,hole_fill,8,open,L5,,"
"NOT every-10 (next every-10 is 2500). Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde / geel / herentals (Sint-Anna OCMW skip) / eeklo (Kinderlach YE2024; leftover VAPH Ascendere already taken; De Vierklaver is Deinze-seated not leftover city_eeklo) / halle (CIK+CAR taken; leftover WZC exhausted; leftover VAPH still open — De Poel leftover-via-VE SKIP; KEERPUNT 0461.049.710 zetel Gent leftover-via-VE SKIP if Halle VE) / kalmthout / bornem (CAR taken; leftover WZC/VAPH commercials/remines) / puurs (maatwerk taken; leftover WZC/VAPH remine/commercial) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde (Zorgbedrijf Vilvoorde OCMW skip) / mol / zoersel (Doppa VAPH taken — leftover WZC commercials Joostens/Halmolen/Ter Dorpe BV) / schilde (Pegode is leftover city_kontich not leftover city_schilde; Oude Melkerij BV skip) / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken) / schoten (VAPH taken; MAXIMUS BV commercial; Oude Melkerij BV commercial) / lokeren (VAPH Hagewinde+Alderande taken; maatwerk De Sperwer taken — leftover WZC/CAR remine; ZENITH BV commercial SKIP) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK+WZC taken) / ninove (CIK taken; leftover WZC/VAPH still open) / asse (CIK+VAPH+maatwerk taken; leftover WZC/CAR remine-heavy) / erpe_mere (WZC Avondzon taken — leftover VAPH/CAR/maatwerk/CIK still open; WZC Sint-Vincentius YE2024 SKIP) / zele (leftover WZC still open — De Vliet is Hamme-seated Trento VE not leftover city_zele) / hamme (WZC Trento taken) / deinze (VAPH Vierklaver taken) / niel (Pegode is leftover city_kontich not leftover city_niel — leftover city_niel still unused) / kontich (VAPH Pegode taken). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT Pegode remine. NOT leftover city_niel via Pegode VE. NOT leftover city_schilde via Pegode VE. NOT Iris remine. NOT De Dageraad remine. NOT Vierklaver remine. NOT leftover city_eeklo via Vierklaver VE. NOT Leieborg remine. NOT Demival remine. NOT Ascendere remine. NOT Trento remine. NOT Avondzon remine. NOT Doppa remine. NOT 3Wplus Werk remine. NOT Hopperank remine. NOT De Sperwer remine. NOT Alderande remine. NOT De Hagewinde remine. NOT leftover city_zele via Trento VE. NOT De Vlietoever BV. NOT Woonzorg Samen Ouder remine. NOT MAXIMUS BV. NOT EigenWijzer OCMW. NOT Inspiration Fields OCMW. NOT Ter Dorpe BV. NOT Oude Melkerij BV. NOT De Poel leftover-via-VE. NOT ASTOR bankrupt. NOT Aralea YE2024. NOT CAR Kapelhof Drongen OFF. NOT AMAB remine. NOT leftover-via-VE. NOT MILLE LUCI CVBA no JR. NOT Huis Coppens commercial. NOT GROEP 3WPLUS. NOT ACROPOLYS NV. NOT Foyer De Lork remine. NOT Corazon no JR. NOT Al-arm no JR. NOT ZENITH BV. NOT An for All CommV. NOT Studijo Bos CV. NOT Sint-Anna OCMW. NOT Zorgbedrijf Vilvoorde OCMW. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT KEERPUNT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2497 leftover city_kontich VAPH; Pegode taken leftover mined city_kontich VAPH; NOT leftover city_niel; NOT leftover city_schilde; Vierklaver taken leftover mined city_deinze VAPH; Trento taken leftover mined city_hamme WZC; NOT every-10 (next 2500)\n"
)
if new_2497.count("\n")!=1 or new_2498.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2497",new_2497),("2498",new_2498)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2497.encode("utf-8"))
    f.write(new_2498.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2497", chk.count(b"rq_2497,"), "n2498", chk.count(b"rq_2498,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2497,2497,no,tick2497 leftover dual Pegode 0420.281.501 Strong native PDF (omzet70 JUMP 1914328 commercial-only vs large 73; 73 JUMP 15317093; 76A JUMP 741511; envelope 70/76A JUMP 18110069; pnl JUMP 629938; 9901 JUMP 610467; equity JUMP 4856573; assets JUMP 8551945; debt DROP 3480999; FTE JUMP 174.6; kapitaalsubsidies JUMP 285334; destin691 JUMP 370649; 791 DROP 92286; cash JUMP 1497839; geldbeleggingen DROP 1240218; capex 739991; 19 VE leftover city_kontich VAPH); leftover mined city_kontich VAPH; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (official KBO zetel Kontich not Niel); NOT leftover city_niel; NOT leftover city_schilde; NOT Iris remine; NOT De Dageraad remine; NOT Vierklaver remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2498 NOT every-10 (next every-10 is 2500)\n",
encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
