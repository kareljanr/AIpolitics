from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2499_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2499,")!=1: raise SystemExit(f"bad 2499 count {rq_raw.count(b'rq_2499,')}")
if b"rq_2500," in rq_raw: raise SystemExit("2500 exists")
idx=rq_raw.rfind(b"rq_2499,")
if idx<0: raise SystemExit("rq_2499 not found")
new_2499=(
"rq_2499,leftover dual Ten Dries YE2025,hole_fill,8,done,L5,vzw_ten_dries_deinze,"
"Took unused leftover public VAPH/MFC Ten Dries 0410.571.207 leftover mined city_deinze. Official NBB VOL-VZW YE2025 2026-00212085 native statutory 47p 0.60MB. Envelope 70/76A JUMP 9392001 (omzet commercial-only vs large 73 JUMP 8648576; 76A DROP 1666); pnl DROP 106116; cash DROP 386799; FTE 104. SECOND leftover unused + live official YE2025 after leftover-type hunt (leftover city_niel VZW census no leftover public care; leftover city_erpe_mere unused VAPH/CAR/maatwerk/CIK name-search empty; leftover city_deinze VAPH Vierklaver already taken). NOT Vierklaver remine. NOT leftover city_eeklo via Vierklaver VE. NOT Leieborg remine. NOT Demival remine. NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2499 leftover mined city_deinze VAPH/MFC; Strong native PDF; 1 VE; prior-year identical; next rq_2500 EVERY-10\n"
)
new_2500=(
"rq_2500,every-10 progress coverage + waste top10 after Ten Dries,hole_fill,9,open,L5,,"
"EVERY-10 (ticks_completed will be 2500). Refresh docs/doge/data/progress_every_10_ticks.md (coverage % layers A-E of 347.956 bn TE) and docs/doge/data/doge_waste_top10_current.md (top 10 by priority_index + short high-absurdity list). Append 5-10 lines to loop_log.md. Do NOT hunt a leftover dual this tick. After every-10: next leftover hunt still unused leftover public WZC/VAPH/CAR/hospital/maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city with official YE2025 native PDF. leftover city_deinze VAPH now Vierklaver + Ten Dries. leftover city_niel still unused (VZW census no leftover public care). leftover VAPH/CAR/maatwerk/CIK of city_erpe_mere still open. leftover city_bornem WZC/VAPH unused. leftover city_puurs WZC/VAPH unused. leftover city_ninove leftover WZC/VAPH open. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / t Sas / Molleke / OpWeg / Aurora / Het Witte Huis / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 last-balansjaar 2025 but prior SCAN/CDN 403 — re-HEAD only if native PDF. Jessa hospital special schema. city_kapellen missing. NOT Ten Dries remine. NOT Vierklaver remine. NOT leftover city_eeklo via Vierklaver VE. NOT leftover city_niel via Pegode VE. NOT leftover city_schilde via Pegode VE. NOT leftover-via-VE. NOT KEERPUNT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2499 leftover city_deinze VAPH/MFC; Ten Dries taken leftover mined city_deinze VAPH/MFC; Vierklaver already taken leftover mined city_deinze VAPH; leftover city_niel still unused; EVERY-10\n"
)
if new_2499.count("\n")!=1 or new_2500.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2499",new_2499),("2500",new_2500)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2499.encode("utf-8"))
    f.write(new_2500.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2499", chk.count(b"rq_2499,"), "n2500", chk.count(b"rq_2500,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2499,2499,no,tick2499 leftover dual Ten Dries 0410.571.207 Strong native PDF (omzet70 JUMP 357127 commercial-only vs large 73; 73 JUMP 8648576; 76A DROP 1666; envelope 70/76A JUMP 9392001; pnl DROP 106116; 9901 DROP 129620; equity JUMP 8249399; assets JUMP 12364030; debt JUMP 4114631; FTE DROP 104; kapitaalsubsidies JUMP 3272755; destin691 empty; cash DROP 386799; geldbeleggingen DROP 2773494; capex 5258768; 1 VE leftover city_deinze VAPH/MFC); leftover mined city_deinze VAPH/MFC; prior-year identical; SECOND leftover unused + live official YE2025 after leftover-type hunt (leftover city_niel VZW census no leftover public care; leftover city_erpe_mere unused VAPH/CAR/maatwerk/CIK name-search empty); NOT Vierklaver remine; NOT leftover city_eeklo via Vierklaver VE; NOT Leieborg remine; NOT Demival remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2500 EVERY-10\n",
encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
