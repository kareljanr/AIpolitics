from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2502_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2502,")!=1: raise SystemExit(f"bad 2502 count {rq_raw.count(b'rq_2502,')}")
if b"rq_2503," in rq_raw: raise SystemExit("2503 exists")
idx=rq_raw.rfind(b"rq_2502,")
if idx<0: raise SystemExit("rq_2502 not found")
new_2502=(
"rq_2502,leftover dual Kinderdagverblijf Sint-Jozef YE2025,hole_fill,8,done,L5,vzw_kdv_sint_jozef_wetteren,"
"Took unused leftover public CIK Kinderdagverblijf Sint-Jozef 0408.475.314 leftover mined city_wetteren. Official NBB VKT-VZW YE2025 2026-00174836 native statutory 13p 51.7kB. Envelope bruto 9900 JUMP 2133695 (VKT because 73 empty and bruto much larger than omzet DROP 540560; 76A JUMP 447; 70/76A 541007); pnl JUMP 230508; 9901 JUMP 249335; destin JUMP 150000; cash DROP 205430 (geldbeleggingen JUMP 813476); FTE JUMP 29.6. FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_wetteren WZC = Zorg-Saam remine; leftover city_niel VZW census sports/culture only; leftover city_mol/denderleeuw/buggenhout still zero leftover children). NOT every-10. NOT AGB Wetteren remine. NOT Trianval remine. NOT Zorg-Saam leftover-via-VE. NOT SAMEN remine. NOT leftover city_buggenhout. NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial.,"
f",{STAMP},{STAMP},tick2502 leftover mined city_wetteren CIK; Strong native PDF; 2 VE; prior-year identical; next rq_2503 leftover dual; next every-10 2510\n"
)
new_2503=(
"rq_2503,leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025,hole_fill,8,open,L5,,"
"Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. NOW leftover city_wetteren CIK taken (Kinderdagverblijf Sint-Jozef@2502; leftover WZC = Zorg-Saam remine; leftover VAPH/CAR/maatwerk still open/empty). leftover city_tielt WZC taken (SAMEN@2501 + De Zonnewende@2487; VAPH De Luifel + CIK Harlekijntjes already taken; leftover city_tielt CAR/maatwerk still open/empty). leftover city_niel still unused (2845 VZW census sports/culture only; Pegode is leftover city_kontich; Maria Boodschap absorbed leftover-via-VE SKIP). leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open (name-search empty; De Ster no JR). leftover city_mol/denderleeuw/buggenhout still zero leftover children (Wonen met Zorg no JR). leftover city_bornem/puurs/ninove WZC/VAPH still unused. leftover city_zoersel WZC still open but Joostens/Halmolen/Ter Dorpe commercial. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / t Sas / Molleke / OpWeg / Aurora / Het Witte Huis / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 last-balansjaar 2025 but SCAN/CDN 403 / broker HTML stub. Jessa leftover city_hasselt hospital special schema CDN 403 / broker HTML stub. city_kapellen missing. NOT Kinderdagverblijf Sint-Jozef remine. NOT SAMEN remine. NOT De Zonnewende remine. NOT De Luifel remine. NOT leftover city_dentergem. NOT leftover-via-VE. NOT KEERPUNT leftover-via-VE Gent. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2502 leftover city_wetteren CIK; Kinderdagverblijf Sint-Jozef taken leftover mined city_wetteren CIK; leftover city_niel still unused; leftover city_mol/denderleeuw/buggenhout still zero leftover children; next every-10 2510\n"
)
if new_2502.count("\n")!=1 or new_2503.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2502",new_2502),("2503",new_2503)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2502.encode("utf-8"))
    f.write(new_2503.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2502", chk.count(b"rq_2502,"), "n2503", chk.count(b"rq_2503,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2502,2502,no,tick2502 leftover dual Kinderdagverblijf Sint-Jozef 0408.475.314 Strong native PDF (omzet70 DROP 540560 ouder-fee slice; 73 empty VKT; 76A JUMP 447; envelope bruto9900 JUMP 2133695; 70/76A 541007; pnl JUMP 230508; 9901 JUMP 249335; equity JUMP 2847914; assets JUMP 3855305; debt JUMP 912391; FTE JUMP 29.6; kapitaalsubsidies DROP 1776246; destin691 JUMP 150000; cash DROP 205430; geldbeleggingen JUMP 813476; capex 31803; 2 VE leftover city_wetteren CIK); leftover mined city_wetteren CIK; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_wetteren WZC = Zorg-Saam remine; leftover city_niel VZW census sports/culture only; leftover city_mol/denderleeuw/buggenhout still zero leftover children); NOT AGB Wetteren remine; NOT Trianval remine; NOT Zorg-Saam leftover-via-VE; NOT leftover city_buggenhout; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; next rq_2503 leftover dual; next every-10 2510\n",
encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
