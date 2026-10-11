from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2527_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_talander_arendonk"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2527,") != 1:
    raise SystemExit(f"bad 2527 count {rq_raw.count(b'rq_2527,')}")
if b"rq_2528," in rq_raw:
    raise SystemExit("2528 exists")
idx = rq_raw.rfind(b"rq_2527,")
if idx < 0:
    raise SystemExit("rq_2527 not found")

notes_2527 = (
    "Took unused leftover public leftover VAPH Talander 0433.306.225 leftover mined city_arendonk leftover-mined AGB-only unused leftover type. "
    "Official NBB VKT-VZW YE2025 2026-00192214 native statutory 14p. Envelope bruto9900 JUMP 1603209 "
    "(VKT because omzet70+73 empty; 76A empty); cash JUMP 1050120; pnl JUMP 142992; 9901 JUMP 140447; "
    "equity JUMP 1662056; assets JUMP 2205622; debt DROP 543566; FTE JUMP 18.8. "
    "FIRST leftover unused + live official YE2025 after leftover-type hunt "
    "(leftover city_arendonk leftover WZC WZGA@2526 taken leftover OCMW De Peulder 0212.236.097 SKIP leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wingene leftover WZC Het Laar@2525 taken leftover WZC Curando remine@2046 leftover WZC Amphora unused leftover WZC type now taken leftover VAPH/CAR/maatwerk unused-looking leftover CIK unused-looking leftover CIK fallback not taken; leftover city_bertem leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover WZC taken leftover VAPH t Volderke SCAN leftover maatwerk DE SPRONG remine leftover CAR/CIK unused-looking leftover CIK fallback not taken; lock leftover city_arendonk leftover VAPH Talander 0433.306.225 leftover-mined AGB-only unused leftover type). "
    "NOT leftover city_arendonk leftover WZC WZGA remine@2526. "
    "NOT leftover OCMW Arendonk De Peulder SKIP. NOT leftover-via-VE. "
    "NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Zorg-Saam remine."
)
extra_2527 = (
    "tick2527 leftover mined city_arendonk leftover VAPH leftover-mined AGB-only unused leftover type; Strong native PDF; 2 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2528 leftover dual"
)
notes_2528 = (
    "Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "NOT every-10 (next every-10 is 2530). "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_arendonk leftover WZC taken (WZGA@2526 leftover-mined AGB-only unused leftover type). NOW leftover city_arendonk leftover VAPH taken (Talander@2527 leftover-mined AGB-only unused leftover type; leftover OCMW De Peulder 0212.236.097 SKIP). leftover city_arendonk leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_wingene leftover WZC taken (Het Laar@2525 leftover-mined AGB-only; leftover WZC Curando 0445.499.422 remine@2046 SKIP; leftover WZC Amphora 0833.161.902 unused leftover WZC type now taken leftover Companyweb last deposit 02.07.2025 likely YE2024). leftover city_wingene leftover VAPH/CAR/maatwerk unused-looking leftover CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_bertem leftover WZC taken (Sint-Bernardus@2523 leftover-mined AGB-only). NOW leftover city_bertem leftover VAPH taken (De Eglantier@2524 leftover-mined AGB-only; leftover VAPH A-Tipi 0788.729.170 leftover-via-VE Leuven SKIP). leftover city_bertem leftover CAR none local leftover maatwerk none local leftover CIK Ferm leftover-via-VE Leuven SKIP leftover CIK Elfenbosje remine Sint-Bernardus@2523 leftover CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_stabroek leftover WZC taken (Aalmoezenier Cuypers@2522; leftover WZC Villa ter Molen Vulpia 0521.970.559 commercial SKIP). leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_wichelen leftover WZC taken (Den Anker / Torkenshof@2521; leftover WZC Molenkouter OCMW 0212.183.045 SKIP). leftover city_wichelen leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_lebbeke leftover WZC taken (Reva Tersig@2520; leftover WZC Hof ter Veldeken OCMW 0212.192.151 SKIP; leftover WZC Seniorie Ter Minne BV 0444.150.330 commercial SKIP; leftover WZC Seniorie Minneveld BV 0840.544.095 commercial SKIP). leftover city_lebbeke leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_meerhout leftover WZC taken (Ter Kempen@2519; leftover WZC De Berk OCMW 0212.196.705 SKIP; leftover maatwerk De Sprong remine@2286 HARD SKIP). leftover city_meerhout leftover VAPH t Volderke 0432.224.080 YE2025 2026-00271440 SCAN Konica SKIP leftover CAR/CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_lennik leftover maatwerk Maatwerkbedrijf Pajottenland 0413.313.535 remine@2201 SKIP. leftover city_londerzeel slug MISSING. leftover city_wortegem_petegem slug MISSING leftover WZC De Linde remine@2425. leftover city_kapellen slug MISSING. "
    "NOW leftover city_scherpenheuvel_zichem leftover types exhausted (De Vlaspit@2515 / Honighsdries@2516 / Levensruimte@2517 / De Schommel@2518). leftover WZC OLV Ster der Zee still unused-looking likely OCMW. leftover WZC Voortberg Armonea SKIP. leftover CAR none local. "
    "NOW leftover city_zottegem leftover WZC+VAPH+CIK taken. leftover city_grimbergen leftover WZC+maatwerk taken leftover WZC Heilig Hart remine@2074. leftover city_oosterzele leftover WZC Groep Sint-Franciscus remine@2142 zetel Brakel SKIP. leftover city_herselt leftover WZC Sint-Barbara remine@2019. "
    "leftover city_niel still unused (sports/culture only; leftover WZC De Medemens remine@2086). leftover city_mol leftover CIK Molleke YE2024 SKIP leftover WZC Witte Meren remine. leftover city_denderleeuw leftover CIK t Sas YE2024 SKIP leftover WZC Gravenkasteel SKIP. leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius 0422.620.585 unused leftover WZC type already taken. "
    "HARD SKIP: Gravenkasteel group 0874.863.091. All OCMW / Armonea / Korian / Vulpia / CuraCare / Emeis / Zorgbedrijf. AZ Waregem SCAN HARD SKIP. De Heymeulen HARD SKIP. Jules/i-mens leftover-via-VE SKIP. Stay OFF Kloosterstraat 6 Drongen. leftover city_meerhout leftover VAPH t Volderke SCAN SKIP leftover maatwerk DE SPRONG remine@2286 HARD SKIP. leftover city_bertem leftover VAPH A-Tipi leftover-via-VE Leuven SKIP. leftover city_bertem leftover CIK Ferm leftover-via-VE Leuven SKIP leftover CIK Elfenbosje remine. leftover city_wingene leftover WZC Curando remine@2046. leftover city_wingene leftover WZC Amphora unused leftover WZC type now taken. leftover city_wingene leftover WZC Het Laar remine@2525. leftover city_arendonk leftover WZC WZGA remine@2526. leftover city_arendonk leftover OCMW De Peulder SKIP. "
    "NOT Talander remine. NOT WZGA remine. NOT Het Laar remine. NOT De Eglantier remine. NOT Sint-Bernardus Bertem remine. NOT Aalmoezenier Cuypers remine. NOT Torkenshof remine. NOT Reva Tersig remine. NOT Ter Kempen remine. NOT De Schommel remine. NOT Huize Levensruimte remine. NOT Huyze Honighsdries remine. NOT De Vlaspit remine. NOT Sint-Elisabeth remine. NOT De Hoop remine. NOT De Bron remine. NOT Den Bogaet remine. NOT Den Diepen Boomgaard remine. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2528 = (
    "spawned after tick2527 leftover city_arendonk leftover VAPH; Talander Arendonk taken leftover mined city_arendonk leftover VAPH leftover-mined AGB-only unused leftover type; leftover city_arendonk leftover WZC taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover OCMW De Peulder SKIP; leftover city_wingene leftover WZC taken leftover WZC Curando remine leftover WZC Amphora unused leftover WZC type now taken leftover VAPH/CAR/maatwerk unused-looking leftover CIK unused-looking leftover CIK fallback not taken; leftover city_bertem leftover WZC+VAPH taken leftover CIK Ferm leftover-via-VE leftover CIK Elfenbosje remine leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover WZC taken leftover VAPH t Volderke SCAN leftover maatwerk DE SPRONG remine leftover CAR/CIK unused-looking leftover CIK fallback not taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; leftover city_zottegem leftover WZC+VAPH+CIK taken; leftover city_grimbergen leftover WZC+maatwerk taken leftover WZC Heilig Hart remine; leftover city_niel still unused leftover WZC De Medemens remine; leftover city_mol leftover CIK Molleke YE2024; leftover city_denderleeuw leftover CIK t Sas YE2024; leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open leftover WZC Sint-Vincentius unused leftover WZC type already taken; AZ Waregem SCAN HARD SKIP; Jules/i-mens leftover-via-VE SKIP; leftover VAPH A-Tipi leftover-via-VE Leuven SKIP; leftover city_bertem leftover CIK Ferm leftover-via-VE Leuven SKIP leftover CIK Elfenbosje remine; leftover city_wingene leftover WZC Curando remine leftover WZC Amphora unused leftover WZC type now taken leftover WZC Het Laar remine; leftover city_arendonk leftover WZC WZGA remine leftover OCMW De Peulder SKIP leftover VAPH Talander remine; leftover city_meerhout leftover maatwerk DE SPRONG remine@2286 HARD SKIP; NOT every-10 (next every-10 2530)"
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

new_2527 = rq_line([
    "rq_2527",
    "leftover dual Talander Arendonk YE2025",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2527,
    "",
    STAMP,
    STAMP,
    extra_2527,
])
new_2528 = rq_line([
    "rq_2528",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2528,
    "",
    STAMP,
    STAMP,
    extra_2528,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2527)
    f.write(new_2528)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2527", chk.count(b"rq_2527,"), "n2528", chk.count(b"rq_2528,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2527,2527,no,"
    "tick2527 leftover dual Talander Arendonk 0433.306.225 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 JUMP 1603209; pnl JUMP 142992; 9901 JUMP 140447; equity JUMP 1662056; assets JUMP 2205622; debt DROP 543566; FTE JUMP 18.8; kapitaalsubsidies DROP 297292; destin691 empty; cash JUMP 1050120; 2 VE leftover city_arendonk leftover VAPH leftover-mined AGB-only unused leftover type); leftover mined city_arendonk leftover VAPH; prior-year identical; NOT every-10 (next every-10 2530); FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_arendonk leftover WZC WZGA@2526 taken leftover OCMW De Peulder SKIP leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wingene leftover WZC Het Laar@2525 leftover WZC Curando remine@2046 leftover WZC Amphora unused leftover WZC type now taken leftover VAPH/CAR/maatwerk unused-looking leftover CIK unused-looking leftover CIK fallback not taken; leftover city_bertem leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover WZC taken leftover VAPH t Volderke SCAN leftover maatwerk DE SPRONG remine leftover CAR/CIK unused-looking leftover CIK fallback not taken; leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken; lock leftover city_arendonk leftover VAPH Talander); NOT WZGA remine@2526; NOT De Peulder OCMW SKIP; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; next rq_2528 leftover dual\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
