from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2500_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2500,")!=1: raise SystemExit(f"bad 2500 count {rq_raw.count(b'rq_2500,')}")
if b"rq_2501," in rq_raw: raise SystemExit("2501 exists")
idx=rq_raw.rfind(b"rq_2500,")
if idx<0: raise SystemExit("rq_2500 not found")
new_2500=(
"rq_2500,leftover dual De Luifel YE2025 + every-10,hole_fill,8,done,L5,vzw_luifel_tielt,"
"Took unused leftover public VAPH De Luifel 0434.011.652 leftover mined city_tielt. Official NBB VKT-VZW YE2025 2026-00245078 native statutory 12p 47kB. Envelope 70/76A JUMP 1782588 (omzet commercial-only vs large 73 JUMP 1711321; 76A empty); pnl DROP 19557; cash JUMP 535798; FTE JUMP 21.4. FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_niel VZW census sports/culture only; leftover city_erpe_mere unused VAPH/CAR/maatwerk/CIK name-search empty; leftover city_tielt WZC + CIK already taken). EVERY-10 also refreshed progress_every_10_ticks.md + doge_waste_top10_current.md from live CSVs. NOT De Zonnewende remine. NOT Mivalti remine. NOT De Harlekijntjes remine. NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2500 leftover mined city_tielt VAPH + EVERY-10; Strong native PDF; 2 VE; prior-year identical; next rq_2501 leftover dual; next every-10 2510\n"
)
new_2501=(
"rq_2501,leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025,hole_fill,8,open,L5,,"
"Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. NOW leftover city_tielt VAPH taken (De Luifel@2500; WZC De Zonnewende + CIK Harlekijntjes already taken). leftover city_niel still unused (2845 VZW census sports/culture only; Pegode is leftover city_kontich; Maria Boodschap absorbed leftover-via-VE SKIP). leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open (name-search empty; Molenhof/De Ster no JR). leftover city_bornem/puurs/ninove WZC/VAPH still unused. leftover city_zoersel WZC still open but Joostens/Halmolen/Ter Dorpe commercial. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / t Sas / Molleke / OpWeg / Aurora / Het Witte Huis / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 last-balansjaar 2025 but SCAN/CDN 403 / broker HTML stub. Jessa leftover city_hasselt hospital special schema CDN 403 / broker HTML stub. city_kapellen missing. NOT De Luifel remine. NOT De Zonnewende remine. NOT Mivalti remine. NOT leftover-via-VE. NOT KEERPUNT leftover-via-VE Gent. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2500 leftover city_tielt VAPH + EVERY-10; De Luifel taken leftover mined city_tielt VAPH; leftover city_niel still unused; next every-10 2510\n"
)
if new_2500.count("\n")!=1 or new_2501.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2500",new_2500),("2501",new_2501)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2500.encode("utf-8"))
    f.write(new_2501.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2500", chk.count(b"rq_2500,"), "n2501", chk.count(b"rq_2501,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2500,2500,no,tick2500 leftover dual De Luifel 0434.011.652 Strong native PDF (omzet70 JUMP 71267 commercial-only vs large 73; 73 JUMP 1711321; 76A empty; envelope 70/76A JUMP 1782588; pnl DROP 19557; 9901 DROP 26431; equity JUMP 683911; assets JUMP 1561492; debt DROP 877581; FTE JUMP 21.4; kapitaalsubsidies empty; destin691 empty; cash JUMP 535798; geldbeleggingen empty DROP; capex 44199; 2 VE leftover city_tielt VAPH) + EVERY-10; leftover mined city_tielt VAPH; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_niel VZW census sports/culture only; leftover city_erpe_mere unused VAPH/CAR/maatwerk/CIK name-search empty); NOT De Zonnewende remine; NOT Mivalti remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2501 leftover dual; next every-10 2510\n",
encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
