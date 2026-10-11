from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2450_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2450,")!=1: raise SystemExit("bad 2450 count")
if b"rq_2451," in rq_raw: raise SystemExit("2451 exists")
idx=rq_raw.rfind(b"rq_2450,")
if idx<0: raise SystemExit("rq_2450 not found")
new_2450=Path("/tmp/rq2450_done.txt").read_text(encoding="utf-8")
new_2451=Path("/tmp/rq2451_open.txt").read_text(encoding="utf-8")
if not new_2450.endswith("\n") or not new_2451.endswith("\n"): raise SystemExit("rows missing LF")
if new_2450.count("\n")!=1 or new_2451.count("\n")!=1: raise SystemExit("bad newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2450.encode("utf-8"))
    f.write(new_2451.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2450", chk.count(b"rq_2450,"), "n2451", chk.count(b"rq_2451,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")
state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2450,2450,no,tick2450 leftover dual Groepsopvang De Hartjes 0441.374.348 Strong native PDF EVERY-10 (omzet70 DROP 251750 commercial-only; 73 JUMP 1342084; 76A empty DROP; opbr70/76A JUMP 1593834 envelope; bruto JUMP 1447874; pnl JUMP 154432; 9901 JUMP 147753; equity JUMP 511958; assets JUMP 695457; debt DROP 183499; FTE 20.6 FLAT; kapitaalsubsidies empty DROP; destin691 JUMP 154432 destin=pnl; 791 empty; cash JUMP 174846; geldbeleggingen FLAT 250000; 1 VE leftover city_tienen CIK); leftover mined city_tienen CIK; NOT De Hartjes Ninove remine; NOT Familia remine; NOT De Wissel remine; NOT t Sloeberke YE2024; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; next every-10 is 2460; next rq_2451 leftover dual\n",
encoding="utf-8")
print("loop_state ok")
