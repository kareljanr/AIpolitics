from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2443_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2443,")!=1: raise SystemExit(f"bad 2443 count {rq_raw.count(b'rq_2443,')}")
if b"rq_2444," in rq_raw: raise SystemExit("2444 exists")
idx=rq_raw.rfind(b"rq_2443,")
if idx<0: raise SystemExit("rq_2443 not found")
new_2443=Path("/tmp/rq2443_done.txt").read_text(encoding="utf-8")
new_2444=Path("/tmp/rq2444_open.txt").read_text(encoding="utf-8")
if not new_2443.endswith("\n") or not new_2444.endswith("\n"): raise SystemExit("rows missing LF")
# ensure single trailing newline
if new_2443.count("\n")!=1: raise SystemExit(f"2443 newlines {new_2443.count(chr(10))}")
if new_2444.count("\n")!=1: raise SystemExit(f"2444 newlines {new_2444.count(chr(10))}")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2443.encode("utf-8"))
    f.write(new_2444.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2443", chk.count(b"rq_2443,"), "n2444", chk.count(b"rq_2444,"))
print("endswith LF", chk.endswith(b"\n"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed — abort")
print("prefix intact")
# loop_state
state_path=DATA/"loop_state.csv"
state_hdr="state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row=(
"main,continuous,hole_fill,"
f"{STAMP},rq_2443,2443,no,"
"tick2443 leftover dual Jeugdhulp Don Bosco Vlaanderen 0408.666.344 Strong native PDF (omzet70 JUMP 207924 commercial-only; 73 JUMP 27785881; 76A JUMP 671098 Mortsel sale; 70/76A JUMP 29159144 envelope; bruto9900 empty VOL; pnl DROP 830135; 9901 DROP 821772; equity JUMP 24731057; assets JUMP 33372760; debt JUMP 8641703; FTE 342 JUMP; kapitaalsubsidies DROP 7796340; destin691 DROP 830135 destin=pnl; cash JUMP 3303716; geldbeleggingen JUMP 12671844; gebouwen DROP 7430623; commissaris voorbehoud 2017-inbreng MVA; 17 VE 2/17 Eeklo Waaistraat 6); leftover mined city_eeklo jeugdhulp; NOT VIA Don Bosco; NOT Kinderlach; NOT t Anemoontje; next every-10 is 2450; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF De Slabbertjes OFF De Ukkies OFF De Hummeltjes OFF t Anemoontje OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Villa Boempatat YE2024 OFF De Regenboog BV OFF Ter Engelen OFF Annuntiaten OFF Konekt OFF MFC Combo OFF Grauwzusters convent OFF Jessa hospital special schema OFF Klein Hemelrijk remine OFF Pinnochio remine OFF Duinhuisjes VE t Anemoontje OFF VIA Don Bosco; AGB/FARO/Gandae YE2024; next rq_2444 leftover dual; next every-10 is 2450\n"
)
cur=state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr): raise SystemExit("loop_state header mismatch")
if ",rq_2442,2442," not in cur: raise SystemExit("loop_state not at 2442; abort")
state_path.write_text(state_hdr+state_row, encoding="utf-8")
print("wrote loop_state")
