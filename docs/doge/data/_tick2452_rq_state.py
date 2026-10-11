from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2452_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2452,")!=1: raise SystemExit("bad 2452 count")
if b"rq_2453," in rq_raw: raise SystemExit("2453 exists")
idx=rq_raw.rfind(b"rq_2452,")
if idx<0: raise SystemExit("rq_2452 not found")
new_2452=Path("/tmp/rq2452_done.txt").read_text(encoding="utf-8")
new_2453=Path("/tmp/rq2453_open.txt").read_text(encoding="utf-8")
if not new_2452.endswith("\n") or not new_2453.endswith("\n"): raise SystemExit("rows missing LF")
if new_2452.count("\n")!=1 or new_2453.count("\n")!=1: raise SystemExit("bad newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2452.encode("utf-8"))
    f.write(new_2453.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2452", chk.count(b"rq_2452,"), "n2453", chk.count(b"rq_2453,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")
state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2452,2452,no,tick2452 leftover dual KINDEROPVANG De Harlekijntjes 0407.700.403 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A JUMP 1700; bruto9900 JUMP 1896924 envelope; pnl DROP 144205; 9901 DROP 136158; equity JUMP 1405811; assets JUMP 1693592; debt DROP 287780; FTE 27 DROP; kapitaalsubsidies DROP 203433; destin691 JUMP 661844; 791 empty; cash DROP 141324; geldbeleggingen JUMP 847580; 1 VE leftover city_tielt CIK); leftover mined city_tielt CIK; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT De Wissel remine; NOT t Sloeberke YE2024; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; next every-10 is 2460; next rq_2453 leftover dual\n",
encoding="utf-8")
print("loop_state ok")
