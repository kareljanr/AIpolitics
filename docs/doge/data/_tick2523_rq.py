from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2523_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_sint_bernardus_bertem"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2523,") != 1:
    raise SystemExit(f"bad 2523 count {rq_raw.count(b'rq_2523,')}")
if b"rq_2524," in rq_raw:
    raise SystemExit("2524 exists")
idx = rq_raw.rfind(b"rq_2523,")
if idx < 0:
    raise SystemExit("rq_2523 not found")

notes_2523 = (
    "Took unused leftover public leftover WZC Sint-Bernardus Bertem 0435.723.406 leftover mined city_bertem leftover-mined AGB-only. "
    "Official NBB VOL-VZW YE2025 2026-00268836 native statutory 36p. Envelope omzet70 DROP 14533086 "
    "(VZW because 70 present and not commercial-only vs 73 DROP 2661412; 76A empty); cash DROP 1258185; geldbeleggingen JUMP 4237589; pnl FLIP LOSS -283512; 9901 FLIP LOSS -254666; "
    "equity DROP 11925827; assets JUMP 17198350; debt JUMP 5272522; FTE DROP 189. "
    "FIRST leftover unused + live official YE2025 after leftover-type hunt "
    "(leftover city_stabroek leftover VAPH/CAR/maatwerk none local after leftover WZC Cuypers@2522 leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover VAPH t Volderke 0432.224.080 YE2025 2026-00271440 SCAN Konica SKIP leftover CAR/CIK unused-looking leftover CIK fallback not taken; lock leftover city_bertem leftover WZC Sint-Bernardus 0435.723.406 leftover-mined AGB-only). "
    "NOT leftover city_stabroek leftover WZC Aalmoezenier Cuypers remine@2522. "
    "NOT leftover WZC Sint-Bernardus Assenede remine. NOT leftover-via-VE. "
    "NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Zorg-Saam remine."
)
extra_2523 = (
    "tick2523 leftover mined city_bertem leftover WZC leftover-mined AGB-only; Strong native PDF; 2 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2524 leftover dual"
)
notes_2524 = (
    "Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "NOT every-10 (next every-10 is 2530). "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_bertem leftover WZC taken (Sint-Bernardus@2523 leftover-mined AGB-only). leftover city_bertem leftover VAPH/CAR/CIK/maatwerk still unused-looking. "
    "NOW leftover city_stabroek leftover WZC taken (Aalmoezenier Cuypers@2522; leftover WZC Villa ter Molen Vulpia 0521.970.559 commercial SKIP). leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking. "
    "NOW leftover city_wichelen leftover WZC taken (Den Anker / Torkenshof@2521; leftover WZC Molenkouter OCMW 0212.183.045 SKIP). leftover city_wichelen leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking. "
    "NOW leftover city_lebbeke leftover WZC taken (Reva Tersig@2520; leftover WZC Hof ter Veldeken OCMW 0212.192.151 SKIP; leftover WZC Seniorie Ter Minne BV 0444.150.330 commercial SKIP; leftover WZC Seniorie Minneveld BV 0840.544.095 commercial SKIP). leftover city_lebbeke leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking. "
    "NOW leftover city_meerhout leftover WZC taken (Ter Kempen@2519; leftover WZC De Berk OCMW 0212.196.705 SKIP; leftover maatwerk De Sprong remine@2286). leftover city_meerhout leftover VAPH t Volderke 0432.224.080 YE2025 2026-00271440 SCAN Konica SKIP leftover CAR/CIK unused-looking. "
    "NOW leftover city_lennik leftover maatwerk Maatwerkbedrijf Pajottenland 0413.313.535 remine@2201 SKIP. leftover city_londerzeel slug MISSING. leftover city_wortegem_petegem slug MISSING. leftover city_kapellen slug MISSING. "
    "NOW leftover city_scherpenheuvel_zichem leftover types exhausted (De Vlaspit@2515 / Honighsdries@2516 / Levensruimte@2517 / De Schommel@2518). leftover WZC OLV Ster der Zee still unused-looking likely OCMW. leftover WZC Voortberg Armonea SKIP. leftover CAR none local. "
    "NOW leftover city_zottegem leftover WZC+VAPH+CIK taken. leftover city_grimbergen leftover WZC+maatwerk taken. leftover city_oosterzele leftover WZC Groep Sint-Franciscus remine@2142 zetel Brakel SKIP. leftover city_herselt leftover WZC Sint-Barbara remine@2019. "
    "leftover city_niel still unused (sports/culture only; leftover WZC De Medemens remine@2086). leftover city_mol leftover CIK Molleke YE2024 SKIP leftover WZC Witte Meren remine. leftover city_denderleeuw leftover CIK t Sas YE2024 SKIP leftover WZC Gravenkasteel SKIP. leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken. "
    "HARD SKIP: Gravenkasteel group 0874.863.091. All OCMW / Armonea / Korian / Vulpia / CuraCare / Emeis / Zorgbedrijf. AZ Waregem SCAN HARD SKIP. De Heymeulen HARD SKIP. Jules/i-mens leftover-via-VE SKIP. Stay OFF Kloosterstraat 6 Drongen. leftover city_meerhout leftover VAPH t Volderke SCAN SKIP. "
    "NOT Sint-Bernardus Bertem remine. NOT Aalmoezenier Cuypers remine. NOT Torkenshof remine. NOT Reva Tersig remine. NOT Ter Kempen remine. NOT De Schommel remine. NOT Huize Levensruimte remine. NOT Huyze Honighsdries remine. NOT De Vlaspit remine. NOT Sint-Elisabeth remine. NOT De Hoop remine. NOT De Bron remine. NOT Den Bogaet remine. NOT Den Diepen Boomgaard remine. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2524 = (
    "spawned after tick2523 leftover city_bertem leftover WZC; Sint-Bernardus Bertem taken leftover mined city_bertem leftover WZC leftover-mined AGB-only; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking; leftover city_meerhout leftover WZC taken leftover VAPH t Volderke SCAN leftover CAR/CIK unused-looking; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; leftover city_zottegem leftover WZC+VAPH+CIK taken; leftover city_grimbergen leftover WZC+maatwerk taken; leftover city_niel still unused leftover WZC De Medemens remine; leftover city_mol leftover CIK Molleke YE2024; leftover city_denderleeuw leftover CIK t Sas YE2024; leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open; AZ Waregem SCAN HARD SKIP; Jules/i-mens leftover-via-VE SKIP; NOT every-10 (next every-10 2530)"
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

new_2523 = rq_line([
    "rq_2523",
    "leftover dual Sint-Bernardus Bertem YE2025",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2523,
    "",
    STAMP,
    STAMP,
    extra_2523,
])
new_2524 = rq_line([
    "rq_2524",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2524,
    "",
    STAMP,
    STAMP,
    extra_2524,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2523)
    f.write(new_2524)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2523", chk.count(b"rq_2523,"), "n2524", chk.count(b"rq_2524,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2523,2523,no,"
    "tick2523 leftover dual Sint-Bernardus Bertem 0435.723.406 Strong native PDF (omzet70 DROP 14533086 not commercial-only; 73 DROP 2661412; 76A empty; envelope omzet70 DROP 14533086; pnl FLIP LOSS -283512; 9901 FLIP LOSS -254666; equity DROP 11925827; assets JUMP 17198350; debt JUMP 5272522; FTE DROP 189; kapitaalsubsidies DROP 31528; destin691 empty; cash DROP 1258185; geldbeleggingen JUMP 4237589; 2 VE leftover city_bertem leftover WZC leftover-mined AGB-only); leftover mined city_bertem leftover WZC; prior-year identical; NOT every-10 (next every-10 2530); FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover VAPH t Volderke 0432.224.080 SCAN SKIP leftover CAR/CIK unused-looking leftover CIK fallback not taken; lock leftover city_bertem leftover WZC Sint-Bernardus); NOT Aalmoezenier Cuypers remine@2522; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; next rq_2524 leftover dual\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
