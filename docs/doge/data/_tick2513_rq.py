from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2513_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_de_hoop_zottegem"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2513,") != 1:
    raise SystemExit(f"bad 2513 count {rq_raw.count(b'rq_2513,')}")
if b"rq_2514," in rq_raw:
    raise SystemExit("2514 exists")
idx = rq_raw.rfind(b"rq_2513,")
if idx < 0:
    raise SystemExit("rq_2513 not found")

notes_2513 = (
    "Took unused leftover public leftover VAPH De Hoop 0870.779.490 leftover mined city_zottegem. "
    "Official NBB VKT-VZW YE2025 2026-00269926 native statutory 14p. Envelope bruto9900 DROP 145460 "
    "(VKT because omzet empty vs 73 DROP 20846; 76A DROP 3269); "
    "cash DROP 542495; pnl JUMP 80173; 9901 FLIP 45595; equity JUMP 328381; debt DROP 1511877; FTE DROP 0. "
    "FIRST leftover unused + live official YE2025 after leftover-type hunt "
    "(lock first valid hit leftover city_zottegem leftover VAPH De Hoop after leftover WZC De Bron@2512; "
    "leftover city_zottegem leftover CAR Wegwijs 0408.203.021 remine parent sec_flanders; leftover maatwerk BWZ 0407.657.148 remine@2196 parent sec_flanders; leftover hospital AZ Zottegem remine tick2009/2018; leftover CIK still open/empty). "
    "NOT De Bron leftover WZC remine. NOT WZC Egmont OCMW. NOT De Bolster leftover-via-VE Zwalm. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Zorg-Saam remine."
)
extra_2513 = (
    "tick2513 leftover mined city_zottegem leftover VAPH; Strong native PDF; 0 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2514 leftover dual"
)
notes_2514 = (
    "Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_zottegem leftover VAPH taken (De Hoop@2513; leftover WZC De Bron@2512; leftover WZC Egmont OCMW skip; leftover CAR Wegwijs remine parent sec_flanders; leftover maatwerk BWZ remine@2196 parent sec_flanders; leftover hospital AZ Zottegem remine; leftover CIK still open/empty). "
    "NOW leftover city_grimbergen leftover WZC taken (Den Bogaet@2511; leftover WZC Heilig Hart remine@2074 parent sec_flanders; leftover VAPH Havinet remine@2301; leftover maatwerk Den Diepen Boomgaard@2510; leftover CAR none local; leftover CIK Kribbekrabbel BV + FERM leftover-via-VE Leuven). "
    "NOW leftover city_asse leftover CIK taken (Kribbe Kinderpret@2509; 3Wplus Kinderopvang@2407; Vijverbeek@2469; leftover VAPH Hopperank@2491; leftover maatwerk 3Wplus Werk@2492). "
    "NOW leftover city_geraardsbergen leftover maatwerk taken (De Dagmoed@2508; leftover CAR Horizon@2395; leftover WZC OCMW/commercial/YE2023; leftover jeugdhulp Wonozo skip; leftover CIK no local leftover VZW). "
    "NOW leftover city_buggenhout leftover VAPH taken (Avalon@2503 + Capelderij@2507; leftover WZC De Heymeulen 0420.669.303 still YE2024 HARD SKIP). leftover city_buggenhout leftover CAR Buggenhout leftover-via-VE Gent SKIP. "
    "NOW leftover city_wetteren leftover CIK taken (Sint-Jozef@2502 + Fiola@2506; leftover VAPH Sint-Lodewijk@2505; leftover CAR/maatwerk still open/empty). "
    "NOW leftover city_herzele leftover WZC taken (Hunnegem@2504; leftover VAPH De Kanteling/VillaVip no JR; leftover CAR none local; leftover CIK Bengeltjes/Klettekes BV + Fie&Ola leftover-via-VE). leftover city_herzele leftover maatwerk still empty. "
    "leftover city_bornem leftover WZC remine (OLV remine@2065; De Vlietoever BV skip; Eyckerheyde remine@2341; leftover CAR Ter Linde taken). leftover VAPH still unused-looking maybe. "
    "leftover city_puurs leftover WZC/VAPH exhausted (Sint-Pieter OCMW remine; Anemoon SLG/Korian remine; Sauvegarde CuraCare; Gravenkasteel Armonea; maatwerk Nektari taken). "
    "leftover city_waregem leftover maatwerk remine (Werkplus@2204); leftover VAPH Ten Anker taken; leftover CIK Kindercentrum + t Zonnetje taken; AZ Waregem SCAN HARD SKIP. "
    "leftover city_niel still unused (2845 VZW census sports/culture only). "
    "leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open/empty (WZC Avondzon + Meredal taken; Pamperbroekje leftover CIK BV unused not locked; Linde vzw 0 VE arts skip). "
    "leftover city_mol leftover WZC remine/commercial/OCMW; leftover CIK Molleke 0448.186.520 YE2024 SKIP. leftover city_denderleeuw leftover WZC Armonea commercial; leftover CIK t Sas YE2024 SKIP. leftover city_mol/denderleeuw still zero leftover children parented under city_*. "
    "HARD SKIP: Het Dak 0863.329.989 0 NBB; De Lindeboom remine 2159; MILLE LUCI no JR; GPN SZ ML 0471.795.132 unless leftover city_sint_niklaas actually mined unused leftover type + native YE2025 under 5 min. "
    "AZ Waregem 0405.460.592 unused leftover hospital YE2025 SCAN/OCR HARD SKIP do not invent euros. "
    "Jules/i-mens 0416.603.716 zetel Gent leftover-via-VE / large chain SKIP. "
    "De Bolster 0861.680.989 zetel Zwalm leftover-via-VE SKIP. "
    "NOT De Hoop remine. NOT De Bron remine. NOT Den Bogaet remine. NOT Den Diepen Boomgaard remine. NOT Kribbe Kinderpret remine. "
    "NOT leftover-via-VE. NOT KEERPUNT leftover-via-VE Gent. NOT CAR Buggenhout leftover-via-VE Gent. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2514 = (
    "spawned after tick2513 leftover city_zottegem leftover VAPH; De Hoop taken leftover mined city_zottegem leftover VAPH; leftover WZC De Bron taken leftover city_zottegem leftover WZC; leftover city_zottegem leftover CAR Wegwijs remine; leftover maatwerk BWZ remine; leftover city_grimbergen leftover WZC+maatwerk taken; leftover city_asse leftover CIK taken; leftover city_geraardsbergen leftover maatwerk taken; leftover city_buggenhout leftover VAPH taken; leftover city_buggenhout WZC De Heymeulen still YE2024; leftover city_wetteren leftover CIK taken; leftover city_wetteren CAR/maatwerk still open/empty; leftover city_niel still unused; leftover city_mol leftover CIK Molleke YE2024; leftover city_denderleeuw leftover CIK t Sas YE2024; leftover city_herzele leftover VAPH De Kanteling/VillaVip no JR; leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open; leftover city_bornem leftover WZC remine leftover VAPH maybe unused; leftover city_puurs leftover WZC exhausted; leftover city_waregem leftover maatwerk remine; AZ Waregem SCAN HARD SKIP; Jules/i-mens leftover-via-VE SKIP; De Bolster leftover-via-VE SKIP; Het Dak 0 NBB SKIP; this tick is NOT every-10 (next every-10 2520)"
)

def rq_line(fields):
    buf = StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(fields)
    line = buf.getvalue()
    n = len(next(csv.reader(StringIO(line))))
    if n != 12:
        raise SystemExit(f"rq fields {n} != 12 for {fields[0]}")
    if not line.endswith("\n"):
        raise SystemExit("rq line no LF")
    if line.count("\n") != 1:
        raise SystemExit("rq line extra NL")
    return line.encode("utf-8")

new_2513 = rq_line([
    "rq_2513",
    "leftover dual De Hoop YE2025",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2513,
    "",
    STAMP,
    STAMP,
    extra_2513,
])
new_2514 = rq_line([
    "rq_2514",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2514,
    "",
    STAMP,
    STAMP,
    extra_2514,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2513)
    f.write(new_2514)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2513", chk.count(b"rq_2513,"), "n2514", chk.count(b"rq_2514,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2513,2513,no,"
    "tick2513 leftover dual De Hoop 0870.779.490 Strong native PDF (omzet70 empty VKT was 69057 vs 73 DROP 20846; 76A DROP 3269; envelope bruto9900 DROP 145460; 70/76A 3269; pnl JUMP 80173; 9901 FLIP 45595; equity JUMP 328381; assets DROP 1840258; debt DROP 1511877; FTE DROP 0; kapitaalsubsidies DROP 291843; destin691 empty; cash DROP 542495; geldbeleggingen empty DROP; 0 VE leftover city_zottegem leftover VAPH); leftover mined city_zottegem leftover VAPH; prior-year identical; NOT every-10 (next every-10 2520); FIRST leftover unused + live official YE2025 after leftover-type hunt (lock De Hoop first valid hit leftover city_zottegem leftover VAPH after leftover WZC De Bron@2512; leftover city_zottegem leftover CAR Wegwijs remine parent sec_flanders; leftover maatwerk BWZ remine@2196; leftover hospital AZ Zottegem remine); NOT De Bron leftover WZC; NOT WZC Egmont OCMW; NOT De Bolster leftover-via-VE Zwalm; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; next rq_2514 leftover dual\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
