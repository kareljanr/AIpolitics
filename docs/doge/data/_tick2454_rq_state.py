from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2454_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2454,")!=1: raise SystemExit("bad 2454 count")
if b"rq_2455," in rq_raw: raise SystemExit("2455 exists")
idx=rq_raw.rfind(b"rq_2454,")
if idx<0: raise SystemExit("rq_2454 not found")
new_2454=Path("/tmp/rq2454_done.txt").read_text(encoding="utf-8")
new_2455=Path("/tmp/rq2455_open.txt").read_text(encoding="utf-8")
if not new_2454.endswith("\n") or not new_2455.endswith("\n"): raise SystemExit("rows missing LF")
if new_2454.count("\n")!=1 or new_2455.count("\n")!=1: raise SystemExit("bad newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2454.encode("utf-8"))
    f.write(new_2455.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2454", chk.count(b"rq_2454,"), "n2455", chk.count(b"rq_2455,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")
state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2454,2454,no,tick2454 leftover dual De Medemens Kinderdagverblijven 0893.678.915 Strong native PDF (omzet70 JUMP 1762950 commercial-only; 73 JUMP 7571818; 76A JUMP 100810; envelope 70/76A JUMP 9548863; bruto9900 empty VOL; pnl DROP 500404; 9901 DROP 501545; equity JUMP 14533752; assets JUMP 16808555; debt JUMP 2186496; FTE 123.7 JUMP; kapitaalsubsidies DROP 3503975; destin691 JUMP 5672853; 791 empty; cash JUMP 3019243; geldbeleggingen FLAT 500000; 9 VE leftover city_antwerpen CIK); leftover mined city_antwerpen CIK; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT De Wissel remine; NOT t Sloeberke YE2024; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; next every-10 is 2460; next rq_2455 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")
