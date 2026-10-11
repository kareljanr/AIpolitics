from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2496_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2496,")!=1: raise SystemExit(f"bad 2496 count {rq_raw.count(b'rq_2496,')}")
if b"rq_2497," in rq_raw: raise SystemExit("2497 exists")
idx=rq_raw.rfind(b"rq_2496,")
if idx<0: raise SystemExit("rq_2496 not found")
new_2496=(
"rq_2496,leftover dual De Vierklaver YE2025,hole_fill,8,done,L5,vzw_vierklaver_deinze,"
"Took unused leftover public VAPH De Vierklaver 0436.015.889 leftover mined city_deinze. Official NBB VOL-VZW YE2025 2026-00178582 native statutory 49p 771KB. Envelope 70/76A JUMP 13914807 (omzet commercial-only vs large 73 JUMP 11513087; 76A empty); pnl FLIP LOSS 213049; destin JUMP 3500000; cash JUMP 3450957; FTE 138. FIRST leftover unused + live official YE2025 after leftover-type hunt (FIRST spotted unused YE2025 leftover De Vierklaver; official KBO zetel Deinze not Eeklo; leftover mined city_deinze VAPH unused). NOT leftover city_eeklo. NOT Leieborg remine. NOT Demival remine. NOT Ascendere remine. NOT Trento remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2496 leftover mined city_deinze VAPH; Strong native PDF; 6 VE; prior-year identical; next rq_2497 NOT every-10 (next every-10 is 2500)\n"
)
new_2497=(
"rq_2497,leftover dual hunt after Vierklaver,hole_fill,8,open,L5,,"
"NOT every-10 (next every-10 is 2500). Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde / geel / herentals (Sint-Anna OCMW skip) / eeklo (Kinderlach YE2024; leftover VAPH Ascendere already taken; De Vierklaver is Deinze-seated not leftover city_eeklo) / halle (CIK+CAR taken; leftover WZC exhausted; leftover VAPH still open — De Poel leftover-via-VE SKIP; KEERPUNT 0461.049.710 zetel Gent leftover-via-VE SKIP if Halle VE) / kalmthout / bornem (CAR taken; leftover WZC/VAPH commercials/remines) / puurs (maatwerk taken; leftover WZC/VAPH remine/commercial) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde (Zorgbedrijf Vilvoorde OCMW skip) / mol / zoersel (Doppa VAPH taken — leftover WZC commercials Joostens/Halmolen/Ter Dorpe BV) / schilde (Pegode 0420.281.501 zetel Niel leftover city_niel not leftover city_schilde — take ONLY as leftover city_niel if unused + official YE2025 native PDF) / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken) / schoten (VAPH taken; MAXIMUS BV commercial; Oude Melkerij BV commercial) / lokeren (VAPH Hagewinde+Alderande taken; maatwerk De Sperwer taken — leftover WZC/CAR remine; ZENITH BV commercial SKIP) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK+WZC taken) / ninove (CIK taken; leftover WZC/VAPH still open) / asse (CIK+VAPH+maatwerk taken; leftover WZC/CAR remine-heavy) / erpe_mere (WZC Avondzon taken — leftover VAPH/CAR/maatwerk/CIK still open; WZC Sint-Vincentius YE2024 SKIP) / zele (leftover WZC still open — De Vliet is Hamme-seated Trento VE not leftover city_zele) / hamme (WZC Trento taken) / deinze (VAPH Vierklaver taken). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT Vierklaver remine. NOT leftover city_eeklo via Vierklaver VE. NOT Leieborg remine. NOT Demival remine. NOT Ascendere remine. NOT Trento remine. NOT Avondzon remine. NOT Doppa remine. NOT 3Wplus Werk remine. NOT Hopperank remine. NOT De Sperwer remine. NOT Alderande remine. NOT De Hagewinde remine. NOT leftover city_zele via Trento VE. NOT De Vlietoever BV. NOT Woonzorg Samen Ouder remine. NOT MAXIMUS BV. NOT EigenWijzer OCMW. NOT Inspiration Fields OCMW. NOT Ter Dorpe BV. NOT Oude Melkerij BV. NOT De Poel leftover-via-VE. NOT ASTOR bankrupt. NOT Aralea YE2024. NOT CAR Kapelhof Drongen OFF. NOT AMAB remine. NOT leftover-via-VE. NOT MILLE LUCI CVBA no JR. NOT Huis Coppens commercial. NOT GROEP 3WPLUS. NOT ACROPOLYS NV. NOT Foyer De Lork remine. NOT Corazon no JR. NOT Al-arm no JR. NOT ZENITH BV. NOT An for All CommV. NOT Studijo Bos CV. NOT Sint-Anna OCMW. NOT Zorgbedrijf Vilvoorde OCMW. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2496 leftover city_deinze VAPH; Vierklaver taken leftover mined city_deinze VAPH; NOT leftover city_eeklo; Trento taken leftover mined city_hamme WZC; Avondzon taken leftover mined city_erpe_mere WZC; Doppa taken leftover mined city_zoersel VAPH; NOT every-10 (next 2500)\n"
)
if new_2496.count("\n")!=1 or new_2497.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2496",new_2496),("2497",new_2497)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2496.encode("utf-8"))
    f.write(new_2497.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2496", chk.count(b"rq_2496,"), "n2497", chk.count(b"rq_2497,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2496,2496,no,tick2496 leftover dual De Vierklaver 0436.015.889 Strong native PDF (omzet70 JUMP 1746754 commercial-only vs large 73; 73 JUMP 11513087; 76A empty; envelope 70/76A JUMP 13914807; pnl FLIP LOSS 213049; 9901 DEEPER LOSS 234486; equity DROP 6745980; assets JUMP 9723578; debt JUMP 2977598; FTE JUMP 138; kapitaalsubsidies DROP 1894593; destin691 JUMP 3500000; 791 empty; cash JUMP 3450957; geldbeleggingen empty; capex 213405; 6 VE leftover city_deinze VAPH); leftover mined city_deinze VAPH; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (official KBO zetel Deinze not Eeklo); NOT leftover city_eeklo; NOT Leieborg remine; NOT Demival remine; NOT Ascendere remine; NOT Trento remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2497 NOT every-10 (next every-10 is 2500)\n",
encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
