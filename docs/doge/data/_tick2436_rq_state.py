from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2436_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2436,")!=1: raise SystemExit(f"bad 2436 count {rq_raw.count(b'rq_2436,')}")
if b"rq_2437," in rq_raw: raise SystemExit("2437 exists")
idx=rq_raw.rfind(b"rq_2436,")
if idx<0: raise SystemExit("rq_2436 not found")
new_2436=Path("/tmp/rq2436_done.txt").read_text(encoding="utf-8")
new_2437=Path("/tmp/rq2437_open.txt").read_text(encoding="utf-8")
if not new_2436.endswith("\n") or not new_2437.endswith("\n"): raise SystemExit("rows missing LF")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2436.encode("utf-8"))
    f.write(new_2437.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2436", chk.count(b"rq_2436,"), "n2437", chk.count(b"rq_2437,"))
print("endswith LF", chk.endswith(b"\n"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed — abort")
print("prefix intact")
state_path=DATA/"loop_state.csv"
state_hdr="state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row=(
"main,continuous,hole_fill,"
f"{STAMP},rq_2436,2436,no,"
"tick2436 leftover dual Avida 0438.814.241 Strong native PDF (omzet70 JUMP 42857494 envelope not commercial-only vs 73; 73 JUMP 11552982; 76A 37803; 70/76A JUMP 55138086; bruto9900 empty VOL; pnl DROP -784162; 9901 DROP -484969; equity JUMP 32531263; assets JUMP 67049389; debt JUMP 34448367; FTE 624.2 JUMP; kapitaalsubsidies JUMP 10271770; destin691 empty; cash JUMP 6847926; geldbeleggingen DROP 0; gebouwen JUMP 43981165; aanbouw JUMP 1256730; 7 VE zetel Molenaarsstraat 34 9000 Gent); leftover mined city_gent; Conecto 0433.961.964 absorbed 01.01.2025; NOT WZC Sint-Coleta Gent 0448.294.507; NOT Home Emmaus; NOT De Foyer; NOT IZW; NOT Ferm Kinderopvang; NOT every-10 (next 2440); OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Villa Boempatat YE2024 OFF De Regenboog BV; AGB/FARO/Gandae YE2024; next rq_2437 leftover dual; next every-10 is 2440\n"
)
cur=state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr): raise SystemExit("loop_state header mismatch")
if ",rq_2435,2435," not in cur: raise SystemExit("loop_state not at 2435; abort")
state_path.write_text(state_hdr+state_row, encoding="utf-8")
print("wrote loop_state")
