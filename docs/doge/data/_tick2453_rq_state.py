from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2453_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2453,")!=1: raise SystemExit("bad 2453 count")
if b"rq_2454," in rq_raw: raise SystemExit("2454 exists")
idx=rq_raw.rfind(b"rq_2453,")
if idx<0: raise SystemExit("rq_2453 not found")
new_2453=Path("/tmp/rq2453_done.txt").read_text(encoding="utf-8")
new_2454=Path("/tmp/rq2454_open.txt").read_text(encoding="utf-8")
if not new_2453.endswith("\n") or not new_2454.endswith("\n"): raise SystemExit("rows missing LF")
if new_2453.count("\n")!=1 or new_2454.count("\n")!=1: raise SystemExit("bad newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2453.encode("utf-8"))
    f.write(new_2454.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2453", chk.count(b"rq_2453,"), "n2454", chk.count(b"rq_2454,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")
state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2453,2453,no,tick2453 leftover dual OKO & ZO 0862.154.608 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; bruto9900 DROP 914033 envelope; pnl FLIP LOSS -15184; 9901 FLIP LOSS -20522; equity DROP 668157; assets DROP 858840; debt DROP 190683; FTE 14.2 DROP; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 419271; geldbeleggingen DROP 0; 2 VE leftover city_zele CIK); leftover mined city_zele CIK; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT De Wissel remine; NOT t Sloeberke YE2024; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; next every-10 is 2460; next rq_2454 leftover dual\n",
encoding="utf-8")
print("loop_state ok")
