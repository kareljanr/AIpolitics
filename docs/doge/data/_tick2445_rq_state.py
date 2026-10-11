from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2445_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2445,")!=1: raise SystemExit(f"bad 2445 count {rq_raw.count(b'rq_2445,')}")
if b"rq_2446," in rq_raw: raise SystemExit("2446 exists")
idx=rq_raw.rfind(b"rq_2445,")
if idx<0: raise SystemExit("rq_2445 not found")
new_2445=Path("/tmp/rq2445_done.txt").read_text(encoding="utf-8")
new_2446=Path("/tmp/rq2446_open.txt").read_text(encoding="utf-8")
if not new_2445.endswith("\n") or not new_2446.endswith("\n"): raise SystemExit("rows missing LF")
if new_2445.count("\n")!=1: raise SystemExit(f"2445 newlines {new_2445.count(chr(10))}")
if new_2446.count("\n")!=1: raise SystemExit(f"2446 newlines {new_2446.count(chr(10))}")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2445.encode("utf-8"))
    f.write(new_2446.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2445", chk.count(b"rq_2445,"), "n2446", chk.count(b"rq_2446,"))
print("endswith LF", chk.endswith(b"\n"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed — abort")
print("prefix intact")
state_path=DATA/"loop_state.csv"
state_hdr="state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row=(
"main,continuous,hole_fill,"
f"{STAMP},rq_2445,2445,no,"
"tick2445 leftover dual t Zonnetje 0443.648.306 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A JUMP 10445; bruto9900 JUMP 2113971 envelope; pnl DROP 175969; 9901 DROP 158114; equity JUMP 1652293; assets JUMP 2101178; debt JUMP 448885; FTE 30.5 JUMP; kapitaalsubsidies DROP 213065; destin691 empty; cash DROP 279435; geldbeleggingen JUMP 900000; 3 VE Waregem+Kruisem+Nazareth-De Pinte); leftover mined city_waregem + leftover mined city_kruisem CIK; NOT Kindercentrum; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT KDV De Regenboog BV; NOT Wigwam; NOT Jeugdhulp Don Bosco; NOT Kinderlach; next every-10 is 2450; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF De Slabbertjes OFF De Ukkies OFF De Hummeltjes OFF t Anemoontje OFF Jeugdhulp Don Bosco OFF Wigwam OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Villa Boempatat YE2024 OFF De Regenboog BV OFF Ter Engelen OFF Annuntiaten OFF Konekt OFF MFC Combo OFF Grauwzusters convent OFF Jessa hospital special schema OFF Klein Hemelrijk remine OFF Pinnochio remine OFF Duinhuisjes VE t Anemoontje OFF VIA Don Bosco; AGB/FARO/Gandae YE2024; next rq_2446 leftover dual; next every-10 is 2450\n"
)
cur=state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr): raise SystemExit("loop_state header mismatch")
if ",rq_2444,2444," not in cur: raise SystemExit("loop_state not at 2444; abort")
state_path.write_text(state_hdr+state_row, encoding="utf-8")
print("wrote loop_state")
