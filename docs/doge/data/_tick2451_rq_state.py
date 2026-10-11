from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2451_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2451,")!=1: raise SystemExit("bad 2451 count")
if b"rq_2452," in rq_raw: raise SystemExit("2452 exists")
idx=rq_raw.rfind(b"rq_2451,")
if idx<0: raise SystemExit("rq_2451 not found")
new_2451=Path("/tmp/rq2451_done.txt").read_text(encoding="utf-8")
new_2452=Path("/tmp/rq2452_open.txt").read_text(encoding="utf-8")
if not new_2451.endswith("\n") or not new_2452.endswith("\n"): raise SystemExit("rows missing LF")
if new_2451.count("\n")!=1 or new_2452.count("\n")!=1: raise SystemExit("bad newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2451.encode("utf-8"))
    f.write(new_2452.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2451", chk.count(b"rq_2451,"), "n2452", chk.count(b"rq_2452,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")
state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2451,2451,no,tick2451 leftover dual Kinderdagverblijf De Hartjes Ninove 0446.391.327 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; bruto9900 JUMP 483796 envelope; pnl JUMP 31142; 9901 FLIP PROFIT 21273; equity JUMP 437479; assets JUMP 478634; debt DROP 41156; FTE 8.2 DROP; kapitaalsubsidies DROP 27420; destin691 empty FLAT; 791 empty; cash JUMP 391809; geldbeleggingen empty; 1 VE leftover city_ninove CIK); leftover mined city_ninove CIK; NOT Groepsopvang De Hartjes Tienen remine; NOT Familia remine; NOT De Wissel remine; NOT t Sloeberke YE2024; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; next every-10 is 2460; next rq_2452 leftover dual\n",
encoding="utf-8")
print("loop_state ok")
