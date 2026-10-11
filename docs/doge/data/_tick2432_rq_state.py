from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2432_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2432,")!=1: raise SystemExit("bad 2432 count")
if b"rq_2433," in rq_raw: raise SystemExit("2433 exists")
idx=rq_raw.rfind(b"rq_2432,")
if idx<0: raise SystemExit("rq_2432 not found")
new_2432=Path("/tmp/rq2432_done.txt").read_text(encoding="utf-8")
new_2433=Path("/tmp/rq2433_open.txt").read_text(encoding="utf-8")
if not new_2432.endswith("\n") or not new_2433.endswith("\n"): raise SystemExit("rows missing LF")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2432.encode("utf-8"))
    f.write(new_2433.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2432", chk.count(b"rq_2432,"), "n2433", chk.count(b"rq_2433,"))
print("endswith LF", chk.endswith(b"\n"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed — abort")
print("prefix intact")
state_path=DATA/"loop_state.csv"
state_hdr="state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row=(
"main,continuous,hole_fill,"
f"{STAMP},rq_2432,2432,no,"
"tick2432 leftover dual Home Emmaus 0451.749.190 Strong native PDF (omzet70 JUMP 279413 commercial-only vs large 73; 73 JUMP 1951139; 76A 0; opbr 70+73+76A JUMP 2230552 envelope; bruto9900 JUMP 2086695; pnl JUMP 270624; 9901 JUMP 193689; equity JUMP 2562446; assets JUMP 2911569; debt JUMP 349123; FTE 26.6 DROP; kapitaalsubsidies JUMP 27614; destin691 empty; cash DROP 736197; geldbeleggingen JUMP 1841875; gebouwen empty; aanbouw empty; 1 VE Van den Heckestraat 41-43 Gent-Ledeberg); leftover mined city_gent after Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; NOT every-10 (next 2440); OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ; AGB/FARO/Gandae YE2024; next rq_2433 leftover dual; next every-10 is 2440\n"
)
cur=state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr): raise SystemExit("loop_state header mismatch")
if ",rq_2431,2431," not in cur: raise SystemExit("loop_state not at 2431; abort")
state_path.write_text(state_hdr+state_row, encoding="utf-8")
print("wrote loop_state")
