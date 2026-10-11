from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2503_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2503,")!=1: raise SystemExit(f"bad 2503 count {rq_raw.count(b'rq_2503,')}")
if b"rq_2504," in rq_raw: raise SystemExit("2504 exists")
idx=rq_raw.rfind(b"rq_2503,")
if idx<0: raise SystemExit("rq_2503 not found")
new_2503=(
"rq_2503,leftover dual Avalon YE2025,hole_fill,8,done,L5,vzw_avalon_buggenhout,"
"Took unused leftover public VAPH Avalon 0464.778.666 leftover mined city_buggenhout. Official NBB VKT-VZW YE2025 2026-00195078 native statutory 13p 49.0kB. Envelope 70/76A JUMP 3558067 (VZW because omzet commercial-only 451254 vs large 73 JUMP 3100234; 76A JUMP 6579; bruto9900 JUMP 3392631); pnl IMPROVED LOSS -32618; 9901 IMPROVED LOSS -36635; destin empty; cash JUMP 1086798; FTE JUMP 37.7. FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_buggenhout still zero leftover children; leftover city_niel VZW census sports/culture only; leftover city_mol/denderleeuw still zero leftover children; leftover city_wetteren CIK taken@2502). NOT every-10. NOT De Heymeulen YE2024. NOT Hunnegem YE2024. NOT Kinderdagverblijf Sint-Jozef remine. NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial.,"
f",{STAMP},{STAMP},tick2503 leftover mined city_buggenhout VAPH; Strong native PDF; 1 VE; prior-year identical; next rq_2504 leftover dual; next every-10 2510\n"
)
new_2504=(
"rq_2504,leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025,hole_fill,8,open,L5,,"
"Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. NOW leftover city_buggenhout VAPH taken (Avalon@2503; leftover WZC De Heymeulen 0420.669.303 still YE2024). leftover city_wetteren CIK taken (Kinderdagverblijf Sint-Jozef@2502; leftover WZC = Zorg-Saam remine; leftover VAPH/CAR/maatwerk still open/empty). leftover city_tielt WZC taken (SAMEN@2501 + De Zonnewende@2487; VAPH De Luifel + CIK Harlekijntjes already taken; leftover city_tielt CAR/maatwerk still open/empty). leftover city_niel still unused (2845 VZW census sports/culture only). leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open (De Ster no JR; WZC Sint-Vincentius YE2024). leftover city_mol/denderleeuw still zero leftover children (Wonen met Zorg no JR). leftover city_herzele leftover WZC Hunnegem YE2024. leftover city_lede WZC Prieelshof Korian skip. leftover city_bornem/puurs/ninove WZC/VAPH still unused. leftover city_zoersel WZC still open but Joostens/Halmolen/Ter Dorpe commercial. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / t Sas / Molleke / OpWeg / Aurora / Het Witte Huis / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 last-balansjaar 2025 but SCAN/CDN 403 / broker HTML stub. Jessa leftover city_hasselt hospital special schema CDN 403 / broker HTML stub. city_kapellen missing. NOT Avalon remine. NOT Kinderdagverblijf Sint-Jozef remine. NOT SAMEN remine. NOT leftover-via-VE. NOT KEERPUNT leftover-via-VE Gent. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2503 leftover city_buggenhout VAPH; Avalon taken leftover mined city_buggenhout VAPH; leftover city_niel still unused; leftover city_mol/denderleeuw still zero leftover children; leftover city_buggenhout WZC De Heymeulen still YE2024; next every-10 2510\n"
)
if new_2503.count("\n")!=1 or new_2504.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2503",new_2503),("2504",new_2504)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2503.encode("utf-8"))
    f.write(new_2504.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2503", chk.count(b"rq_2503,"), "n2504", chk.count(b"rq_2504,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2503,2503,no,tick2503 leftover dual Avalon 0464.778.666 Strong native PDF (omzet70 JUMP 451254 commercial-only vs large 73; 73 JUMP 3100234; 76A JUMP 6579; envelope 70/76A JUMP 3558067; bruto9900 JUMP 3392631; pnl IMPROVED LOSS -32618; 9901 IMPROVED LOSS -36635; equity DROP 4344137; assets DROP 6039963; debt DROP 1573776; FTE JUMP 37.7; kapitaalsubsidies DROP 1831111; destin691 empty; cash JUMP 1086798; geldbeleggingen 250000 FLAT; capex 119601; 1 VE leftover city_buggenhout VAPH); leftover mined city_buggenhout VAPH; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_buggenhout still zero leftover children; leftover city_niel VZW census sports/culture only; leftover city_mol/denderleeuw still zero leftover children); NOT De Heymeulen YE2024; NOT Hunnegem YE2024; NOT Kinderdagverblijf Sint-Jozef remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; next rq_2504 leftover dual; next every-10 2510\n",
encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
