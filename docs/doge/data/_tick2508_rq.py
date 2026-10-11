from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2508_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_dagmoed_geraardsbergen"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2508,") != 1:
    raise SystemExit(f"bad 2508 count {rq_raw.count(b'rq_2508,')}")
if b"rq_2509," in rq_raw:
    raise SystemExit("2509 exists")
idx = rq_raw.rfind(b"rq_2508,")
if idx < 0:
    raise SystemExit("rq_2508 not found")

notes_2508 = (
    "Took unused leftover public leftover maatwerk De Dagmoed 0416.317.070 leftover mined city_geraardsbergen. "
    "Official NBB VKT-VZW YE2025 2026-00131365 native statutory 15p. Envelope bruto9900 JUMP 3928555 "
    "(VKT because omzet70+73 empty; 76A empty); cash DROP 397386; 635/9 JUMP 185300; pnl JUMP 122649; "
    "9901 DROP 118329; destin empty; FTE JUMP 89.3. FIRST leftover unused + live official YE2025 after leftover-type hunt "
    "(leftover city_mol leftover WZC Witte Meren remine tick1732 parent sec_flanders; Hemelrijck Armonea; Ten Hove OCMW; leftover city_denderleeuw leftover WZC Ter Bake/Rodenbach Armonea/Gravenkasteel commercial; leftover city_geraardsbergen leftover WZC OCMW/commercial/YE2023 Baronie last JR YE2023; leftover jeugdhulp Wonozo skip; leftover CAR Horizon already taken — leftover maatwerk unused). "
    "NOT Wonozo skip jeugdhulp. NOT CAR Horizon remine. NOT Kringwinkel remine. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2508 = (
    "tick2508 leftover mined city_geraardsbergen leftover maatwerk; Strong native PDF; 1 VE; prior-year identical; next rq_2509 leftover dual; next every-10 2510"
)
notes_2509 = (
    "Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_geraardsbergen leftover maatwerk taken (De Dagmoed@2508; leftover CAR Horizon@2395; leftover WZC OCMW/commercial/YE2023; leftover jeugdhulp Wonozo skip). "
    "NOW leftover city_buggenhout leftover VAPH taken (Avalon@2503 + Capelderij@2507; leftover WZC De Heymeulen 0420.669.303 still YE2024 / SBM still YE2024 / broker HTML stub HARD SKIP). leftover city_buggenhout leftover CAR Buggenhout 0412.404.903 zetel Kloosterstraat 6 9031 Gent leftover-via-VE SKIP. "
    "NOW leftover city_wetteren leftover CIK taken (Kinderdagverblijf Sint-Jozef@2502 + Fiola@2506; leftover VAPH Sint-Lodewijk@2505; leftover WZC = Zorg-Saam remine; leftover CAR/maatwerk still open/empty). "
    "NOW leftover city_herzele leftover CIK Fie&Ola Herzele is leftover-via-VE of leftover city_wetteren seated Fiola SKIP. leftover city_herzele leftover WZC taken (Hunnegem@2504; leftover WZC exhausted Stuyvenberg/Ter Linden CuraCare commercial; leftover VAPH De Kanteling/VillaVip no JR). leftover city_herzele leftover CAR/maatwerk/CIK may still be open. "
    "leftover city_tielt WZC taken (SAMEN@2501 + De Zonnewende@2487; VAPH De Luifel + CIK Harlekijntjes already taken; leftover city_tielt CAR/maatwerk still open/empty). "
    "leftover city_niel still unused (2845 VZW census sports/culture only). "
    "leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open/empty (WZC Avondzon + Meredal taken). "
    "leftover city_mol leftover WZC remine/commercial/OCMW (Witte Meren remine tick1732 parent sec_flanders; Hemelrijck Armonea; Ten Hove OCMW; leftover hospital Heilig Hart YE2024; leftover maatwerk Lidwina remine). leftover city_denderleeuw leftover WZC Armonea/Gravenkasteel commercial. leftover city_mol/denderleeuw still zero leftover children parented under city_*. "
    "leftover city_bornem leftover WZC/VAPH remine/commercial (De Vlietoever BV; OLV remine; Huize Eyckerheyde remine@2341; CAR taken). "
    "leftover city_puurs leftover WZC commercial/OCMW (Sint-Pieter OCMW remine; Anemoon/SLG 0410.958.712 Korian remine; Sauvegarde CuraCare BV; maatwerk Nektari taken). "
    "leftover city_ninove leftover WZC commercial/OCMW; leftover VAPH remine/commercial; leftover CIK Fie&Ola leftover-via-VE Fiola SKIP. "
    "Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / t Sas / Molleke / OpWeg / Aurora / Het Witte Huis / WZC Sint-Vincentius Erpe-Mere / Aralea / De Heymeulen still YE2024. "
    "NOT De Dagmoed remine. NOT Wonozo skip jeugdhulp. NOT CAR Horizon remine. NOT Capelderij remine. NOT Avalon remine. NOT Fiola remine. "
    "NOT leftover-via-VE. NOT KEERPUNT leftover-via-VE Gent. NOT CAR Buggenhout leftover-via-VE Gent. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2509 = (
    "spawned after tick2508 leftover city_geraardsbergen leftover maatwerk; De Dagmoed taken leftover mined city_geraardsbergen leftover maatwerk; leftover city_geraardsbergen leftover maatwerk now taken; leftover city_geraardsbergen leftover WZC OCMW/commercial/YE2023; leftover city_buggenhout leftover VAPH now Avalon+Capelderij; leftover city_buggenhout WZC De Heymeulen still YE2024; leftover city_wetteren leftover CIK now Sint-Jozef+Fiola; leftover city_wetteren CAR/maatwerk still open/empty; leftover city_niel still unused; leftover city_mol/denderleeuw still zero leftover children; leftover city_herzele leftover VAPH De Kanteling/VillaVip no JR; leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open; Wonozo skip; next every-10 2510"
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

new_2508 = rq_line([
    "rq_2508",
    "leftover dual De Dagmoed YE2025",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2508,
    "",
    STAMP,
    STAMP,
    extra_2508,
])
new_2509 = rq_line([
    "rq_2509",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2509,
    "",
    STAMP,
    STAMP,
    extra_2509,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2508)
    f.write(new_2509)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2508", chk.count(b"rq_2508,"), "n2509", chk.count(b"rq_2509,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2508,2508,no,"
    "tick2508 leftover dual De Dagmoed 0416.317.070 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 JUMP 3928555; pnl JUMP 122649; 9901 DROP 118329; equity JUMP 2137199; assets JUMP 4296270; debt JUMP 1111269; FTE JUMP 89.3; kapitaalsubsidies empty; destin691 empty; 791 empty; cash DROP 397386; geldbeleggingen JUMP 2000000; 635/9 JUMP 185300; capex 324771; 1 VE leftover city_geraardsbergen leftover maatwerk); leftover mined city_geraardsbergen leftover maatwerk; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_geraardsbergen leftover maatwerk unused besides CAR Horizon@2395; leftover WZC OCMW/commercial/YE2023; Wonozo skip jeugdhulp; leftover city_mol leftover WZC Witte Meren remine tick1732; leftover city_denderleeuw leftover WZC Armonea); NOT Wonozo skip jeugdhulp; NOT CAR Horizon remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; next rq_2509 leftover dual; next every-10 2510\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
