from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2439_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2439,")!=1: raise SystemExit(f"bad 2439 count {rq_raw.count(b'rq_2439,')}")
if b"rq_2440," in rq_raw: raise SystemExit("2440 exists")
idx=rq_raw.rfind(b"rq_2439,")
if idx<0: raise SystemExit("rq_2439 not found")
new_2439=Path("/tmp/rq2439_done.txt").read_text(encoding="utf-8")
new_2440=Path("/tmp/rq2440_open.txt").read_text(encoding="utf-8")
if not new_2439.endswith("\n") or not new_2440.endswith("\n"): raise SystemExit("rows missing LF")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2439.encode("utf-8"))
    f.write(new_2440.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2439", chk.count(b"rq_2439,"), "n2440", chk.count(b"rq_2440,"))
print("endswith LF", chk.endswith(b"\n"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed — abort")
print("prefix intact")
state_path=DATA/"loop_state.csv"
state_hdr="state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row=(
"main,continuous,hole_fill,"
f"{STAMP},rq_2439,2439,no,"
"tick2439 leftover dual De Slabbertjes 0411.972.064 Strong native PDF (omzet70 empty; 73 empty; 76A DROP 2808; bruto9900 DROP 519885 envelope; pnl DROP 48280; 9901 DROP 47360; equity JUMP 599876; assets JUMP 662430; debt DROP 62554; FTE 10.6 JUMP; kapitaalsubsidies DROP 71963; destin691 JUMP 375400 destin>>pnl; cash DROP 138351; geldbeleggingen JUMP 257760; gebouwen DROP 208808; aanbouw empty; 1 VE zetel Mechelsevest 4 3000 Leuven); leftover mined city_leuven CIK; NOT De Wissel; NOT Monte Rosa; NOT Ferm; NOT IZW; NOT t Eekhoorntje; NOT Grauwzusters convent; NOT every-10 (next 2440 MUST refresh); OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Villa Boempatat YE2024 OFF De Regenboog BV OFF Ter Engelen OFF Annuntiaten OFF Konekt OFF MFC Combo OFF Grauwzusters convent; AGB/FARO/Gandae YE2024; De Ukkies leftover city_hasselt CIK still YE2024; Jessa leftover city_hasselt hospital special schema; next rq_2440 leftover dual + EVERY-10; next every-10 is 2440\n"
)
cur=state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr): raise SystemExit("loop_state header mismatch")
if ",rq_2438,2438," not in cur: raise SystemExit("loop_state not at 2438; abort")
state_path.write_text(state_hdr+state_row, encoding="utf-8")
print("wrote loop_state")
