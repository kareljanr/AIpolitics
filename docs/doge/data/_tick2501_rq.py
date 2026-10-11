from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2501_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2501,")!=1: raise SystemExit(f"bad 2501 count {rq_raw.count(b'rq_2501,')}")
if b"rq_2502," in rq_raw: raise SystemExit("2502 exists")
idx=rq_raw.rfind(b"rq_2501,")
if idx<0: raise SystemExit("rq_2501 not found")
new_2501=(
"rq_2501,leftover dual SAMEN YE2025,hole_fill,8,done,L5,vzw_samen_tielt,"
"Took unused leftover public WZC SAMEN 0728.627.079 leftover mined city_tielt. Official NBB VOL-VZW YE2025 2026-00229914 native statutory 50p 1.87MB. Envelope omzet 70 JUMP 14791167 (material not commercial-only vs 73 JUMP 2813573; 76A DROP 72928; 70/76A JUMP 18017846); pnl IMPROVED LOSS -305249; 9901 FLIP 247706; cash DROP 2242270; FTE JUMP 177.6. FIRST leftover unused + live official YE2025 after leftover-type hunt (Mivalti remine; M-accent remine; De Ster no JR; Wonen met Zorg no JR; leftover city_niel VZW census sports/culture only; leftover city_mol/denderleeuw still zero leftover children; leftover city_tielt WZC already had De Zonnewende@2487 — second leftover WZC like Avondzon+Meredal). NOT every-10. NOT De Zonnewende remine. NOT De Luifel remine. NOT Mivalti remine. NOT leftover city_dentergem (VE only). NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2501 leftover mined city_tielt WZC; Strong native PDF; 3 VE; prior-year identical; next rq_2502 leftover dual; next every-10 2510\n"
)
new_2502=(
"rq_2502,leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025,hole_fill,8,open,L5,,"
"Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. NOW leftover city_tielt WZC taken (SAMEN@2501 + De Zonnewende@2487; VAPH De Luifel + CIK Harlekijntjes already taken; leftover city_tielt CAR/maatwerk still open/empty). leftover city_niel still unused (2845 VZW census sports/culture only; Pegode is leftover city_kontich; Maria Boodschap absorbed leftover-via-VE SKIP). leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open (name-search empty; De Ster no JR). leftover city_mol/denderleeuw still zero leftover children (Wonen met Zorg no JR). leftover city_bornem/puurs/ninove WZC/VAPH still unused. leftover city_zoersel WZC still open but Joostens/Halmolen/Ter Dorpe commercial. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / t Sas / Molleke / OpWeg / Aurora / Het Witte Huis / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 last-balansjaar 2025 but SCAN/CDN 403 / broker HTML stub. Jessa leftover city_hasselt hospital special schema CDN 403 / broker HTML stub. city_kapellen missing. NOT SAMEN remine. NOT De Zonnewende remine. NOT De Luifel remine. NOT Mivalti remine. NOT M-accent remine. NOT leftover city_dentergem. NOT leftover-via-VE. NOT KEERPUNT leftover-via-VE Gent. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2501 leftover city_tielt WZC; SAMEN taken leftover mined city_tielt WZC; leftover city_niel still unused; leftover city_mol/denderleeuw still zero leftover children; next every-10 2510\n"
)
if new_2501.count("\n")!=1 or new_2502.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2501",new_2501),("2502",new_2502)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2501.encode("utf-8"))
    f.write(new_2502.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2501", chk.count(b"rq_2501,"), "n2502", chk.count(b"rq_2502,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2501,2501,no,tick2501 leftover dual SAMEN 0728.627.079 Strong native PDF (omzet70 JUMP 14791167 material not commercial-only; 73 JUMP 2813573; 76A DROP 72928; envelope omzet70 JUMP 14791167; 70/76A JUMP 18017846; pnl IMPROVED LOSS -305249; 9901 FLIP 247706; equity DROP 6321909; assets DROP 39656390; debt DROP 33334481; FTE JUMP 177.6; kapitaalsubsidies JUMP 527989; destin691 empty; cash DROP 2242270; geldbeleggingen empty; capex 777795; 3 VE leftover city_tielt WZC); leftover mined city_tielt WZC; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (Mivalti remine; M-accent remine; De Ster no JR; Wonen met Zorg no JR; leftover city_niel VZW census sports/culture only; leftover city_mol/denderleeuw still zero leftover children); NOT De Zonnewende remine; NOT De Luifel remine; NOT leftover city_dentergem; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2502 leftover dual; next every-10 2510\n",
encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
