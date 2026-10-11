from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2431_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2431,")!=1: raise SystemExit("bad 2431 count")
if b"rq_2432," in rq_raw: raise SystemExit("2432 exists")
idx=rq_raw.rfind(b"rq_2431,")
if idx<0: raise SystemExit("rq_2431 not found")
new_2431=Path("/tmp/rq2431_new2431.txt").read_text(encoding="utf-8")
new_2432=Path("/tmp/rq2431_new2432.txt").read_text(encoding="utf-8")
if not new_2431.endswith("\n") or not new_2432.endswith("\n"): raise SystemExit("rows missing LF")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2431.encode("utf-8"))
    f.write(new_2432.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2431", chk.count(b"rq_2431,"), "n2432", chk.count(b"rq_2432,"))
print("endswith LF", chk.endswith(b"\n"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed — abort")
print("prefix intact")
state_path=DATA/"loop_state.csv"
state_hdr="state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row=(
"main,continuous,hole_fill,"
f"{STAMP},rq_2431,2431,no,"
"tick2431 leftover dual Witje Wiebel 0443.654.937 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; bruto9900 FLAT 1878999 envelope; pnl JUMP 301158; 9901 DROP 304658; equity JUMP 2307857; assets JUMP 2843864; debt DROP 536007; FTE 25.3; kapitaalsubsidies DROP 560470; destin691 300000; cash JUMP 804896; geldbeleggingen FLAT 650000; gebouwen DROP 1134601; aanbouw empty; 2 VE Kortrijksesteenweg 1020 + Smidsestraat 88 Gent); leftover mined city_gent after Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; NOT every-10 (next 2440); OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993; AGB/FARO/Gandae YE2024; next rq_2432 leftover dual; next every-10 is 2440\n"
)
cur=state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr): raise SystemExit("loop_state header mismatch")
if ",rq_2430,2430," not in cur: raise SystemExit("loop_state not at 2430; abort")
state_path.write_text(state_hdr+state_row, encoding="utf-8")
print("wrote loop_state")
