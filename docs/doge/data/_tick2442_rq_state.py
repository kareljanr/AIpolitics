from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2442_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2442,")!=1: raise SystemExit(f"bad 2442 count {rq_raw.count(b'rq_2442,')}")
if b"rq_2443," in rq_raw: raise SystemExit("2443 exists")
idx=rq_raw.rfind(b"rq_2442,")
if idx<0: raise SystemExit("rq_2442 not found")
new_2442=Path("/tmp/rq2442_done.txt").read_text(encoding="utf-8")
new_2443=Path("/tmp/rq2443_open.txt").read_text(encoding="utf-8")
if not new_2442.endswith("\n") or not new_2443.endswith("\n"): raise SystemExit("rows missing LF")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2442.encode("utf-8"))
    f.write(new_2443.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2442", chk.count(b"rq_2442,"), "n2443", chk.count(b"rq_2443,"))
print("endswith LF", chk.endswith(b"\n"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed — abort")
print("prefix intact")
# loop_state
state_path=DATA/"loop_state.csv"
state_hdr="state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row=(
"main,continuous,hole_fill,"
f"{STAMP},rq_2442,2442,no,"
"tick2442 leftover dual t Anemoontje 0413.354.612 Strong native PDF (omzet70 JUMP 136595 commercial-only; 73 JUMP 698331; 76A empty; 70+73 JUMP 834926 envelope; bruto9900 JUMP 759661; pnl JUMP 105278; 9901 JUMP 109330; equity JUMP 1329241; assets JUMP 1575233; debt DROP 245992; FTE 8.1 DROP; kapitaalsubsidies DROP 515543; destin691 JUMP 598014 destin>>pnl; cash JUMP 332675; geldbeleggingen FLAT 250000; gebouwen DROP 898992; 1 VE 2.150.886.809 Bosstraat 30 3012 Leuven); leftover mined city_leuven CIK; NOT Duinhuisjes VE t Anemoontje; NOT De Slabbertjes; NOT Ferm Kinderopvang; NOT De Hummeltjes; NOT De Ukkies; next every-10 is 2450; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF De Slabbertjes OFF De Ukkies OFF De Hummeltjes OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Villa Boempatat YE2024 OFF De Regenboog BV OFF Ter Engelen OFF Annuntiaten OFF Konekt OFF MFC Combo OFF Grauwzusters convent OFF Jessa hospital special schema OFF Klein Hemelrijk remine OFF Pinnochio remine OFF Duinhuisjes VE t Anemoontje; AGB/FARO/Gandae YE2024; next rq_2443 leftover dual; next every-10 is 2450\n"
)
cur=state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr): raise SystemExit("loop_state header mismatch")
if ",rq_2441,2441," not in cur: raise SystemExit("loop_state not at 2441; abort")
state_path.write_text(state_hdr+state_row, encoding="utf-8")
print("wrote loop_state")
