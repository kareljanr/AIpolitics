from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2522_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_cuypers_stabroek"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2522,") != 1:
    raise SystemExit(f"bad 2522 count {rq_raw.count(b'rq_2522,')}")
if b"rq_2523," in rq_raw:
    raise SystemExit("2523 exists")
idx = rq_raw.rfind(b"rq_2522,")
if idx < 0:
    raise SystemExit("rq_2522 not found")

notes_2522 = (
    "Took unused leftover public leftover WZC Aalmoezenier Cuypers 0408.704.847 leftover mined city_stabroek leftover-mined AGB-only. "
    "Official NBB VOL-VZW YE2025 2026-00325553 native statutory 54p. Envelope omzet70 JUMP 6273758 "
    "(VZW because 70 present and not commercial-only vs 73 DROP 1161030; 76A DROP 8890); cash DROP 49222; geldbeleggingen FLAT 704504; pnl DROP -101734; 9901 DROP 148842; "
    "equity DROP 2629512; assets DROP 9598296; debt DROP 6878783; FTE JUMP 75.9. "
    "FIRST leftover unused + live official YE2025 after leftover-type hunt "
    "(leftover city_wichelen leftover VAPH/CAR/maatwerk none local after leftover WZC Torkenshof@2521; leftover city_lebbeke leftover VAPH/CAR/maatwerk none local after leftover WZC Reva Tersig@2520; leftover city_meerhout leftover VAPH t Volderke 0432.224.080 YE2025 2026-00271440 SCAN Konica SKIP; leftover CIK fallback not taken; lock leftover city_stabroek leftover WZC Aalmoezenier Cuypers 0408.704.847 leftover-mined AGB-only). "
    "NOT leftover WZC Villa ter Molen Vulpia 0521.970.559. "
    "NOT Torkenshof remine@2521. NOT Reva Tersig remine@2520. NOT Ter Kempen remine@2519. NOT leftover-via-VE. "
    "NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Zorg-Saam remine."
)
extra_2522 = (
    "tick2522 leftover mined city_stabroek leftover WZC leftover-mined AGB-only; Strong native PDF; 1 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2523 leftover dual"
)
notes_2523 = (
    "Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "NOT every-10 (next every-10 is 2530). "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_stabroek leftover WZC taken (Aalmoezenier Cuypers@2522; leftover WZC Villa ter Molen Vulpia 0521.970.559 commercial SKIP). leftover city_stabroek leftover VAPH/CAR/CIK/maatwerk still unused-looking. "
    "NOW leftover city_wichelen leftover WZC taken (Den Anker / Torkenshof@2521; leftover WZC Molenkouter OCMW 0212.183.045 SKIP). leftover city_wichelen leftover VAPH/CAR/maatwerk none local. leftover city_wichelen leftover CIK still unused-looking. "
    "NOW leftover city_lebbeke leftover WZC taken (Reva Tersig@2520; leftover WZC Hof ter Veldeken OCMW 0212.192.151 SKIP; leftover WZC Seniorie Ter Minne BV 0444.150.330 commercial SKIP; leftover WZC Seniorie Minneveld BV 0840.544.095 commercial SKIP). leftover city_lebbeke leftover VAPH/CAR/CIK/maatwerk still unused-looking. "
    "NOW leftover city_meerhout leftover WZC taken (Ter Kempen@2519; leftover WZC De Berk OCMW 0212.196.705 SKIP; leftover maatwerk De Sprong remine@2286). leftover city_meerhout leftover VAPH t Volderke 0432.224.080 YE2025 2026-00271440 SCAN Konica SKIP. leftover city_meerhout leftover CAR/CIK still unused-looking. "
    "NOW leftover city_lennik leftover maatwerk Maatwerkbedrijf Pajottenland 0413.313.535 remine@2201 SKIP. leftover city_londerzeel slug MISSING. leftover city_wortegem_petegem slug MISSING. leftover city_kapellen slug MISSING. "
    "NOW leftover city_scherpenheuvel_zichem leftover types exhausted (De Vlaspit@2515 / Honighsdries@2516 / Levensruimte@2517 / De Schommel@2518). leftover WZC OLV Ster der Zee still unused-looking likely OCMW. leftover WZC Voortberg Armonea SKIP. leftover CAR none local. "
    "NOW leftover city_zottegem leftover WZC+VAPH+CIK taken. leftover city_grimbergen leftover WZC+maatwerk taken. leftover city_oosterzele leftover WZC Groep Sint-Franciscus remine@2142 zetel Brakel SKIP. leftover city_herselt leftover WZC Sint-Barbara remine@2019. "
    "leftover city_niel still unused (sports/culture only; leftover WZC De Medemens remine@2086). leftover city_mol leftover CIK Molleke YE2024 SKIP leftover WZC Witte Meren remine. leftover city_denderleeuw leftover CIK t Sas YE2024 SKIP leftover WZC Gravenkasteel SKIP. leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken. "
    "HARD SKIP: Gravenkasteel group 0874.863.091. All OCMW / Armonea / Korian / Vulpia / CuraCare / Emeis / Zorgbedrijf. AZ Waregem SCAN HARD SKIP. De Heymeulen HARD SKIP. Jules/i-mens leftover-via-VE SKIP. Stay OFF Kloosterstraat 6 Drongen. leftover city_meerhout leftover VAPH t Volderke SCAN SKIP. "
    "NOT Aalmoezenier Cuypers remine. NOT Torkenshof remine. NOT Reva Tersig remine. NOT Ter Kempen remine. NOT De Schommel remine. NOT Huize Levensruimte remine. NOT Huyze Honighsdries remine. NOT De Vlaspit remine. NOT Sint-Elisabeth remine. NOT De Hoop remine. NOT De Bron remine. NOT Den Bogaet remine. NOT Den Diepen Boomgaard remine. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2523 = (
    "spawned after tick2522 leftover city_stabroek leftover WZC; Aalmoezenier Cuypers taken leftover mined city_stabroek leftover WZC leftover-mined AGB-only; leftover WZC Villa ter Molen Vulpia SKIP; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/CIK/maatwerk unused-looking; leftover city_meerhout leftover WZC taken leftover VAPH t Volderke SCAN leftover CAR/CIK unused-looking; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; leftover city_zottegem leftover WZC+VAPH+CIK taken; leftover city_grimbergen leftover WZC+maatwerk taken; leftover city_niel still unused leftover WZC De Medemens remine; leftover city_mol leftover CIK Molleke YE2024; leftover city_denderleeuw leftover CIK t Sas YE2024; leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open; AZ Waregem SCAN HARD SKIP; Jules/i-mens leftover-via-VE SKIP; NOT every-10 (next every-10 2530)"
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

new_2522 = rq_line([
    "rq_2522",
    "leftover dual Aalmoezenier Cuypers YE2025",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2522,
    "",
    STAMP,
    STAMP,
    extra_2522,
])
new_2523 = rq_line([
    "rq_2523",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2523,
    "",
    STAMP,
    STAMP,
    extra_2523,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2522)
    f.write(new_2523)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2522", chk.count(b"rq_2522,"), "n2523", chk.count(b"rq_2523,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2522,2522,no,"
    "tick2522 leftover dual Aalmoezenier Cuypers 0408.704.847 Strong native PDF (omzet70 JUMP 6273758 not commercial-only; 73 DROP 1161030; 76A DROP 8890; envelope omzet70 JUMP 6273758; pnl DROP -101734; 9901 DROP 148842; equity DROP 2629512; assets DROP 9598296; debt DROP 6878783; FTE JUMP 75.9; kapitaalsubsidies DROP 1070581; destin691 empty; cash DROP 49222; geldbeleggingen FLAT 704504; 1 VE leftover city_stabroek leftover WZC leftover-mined AGB-only); leftover mined city_stabroek leftover WZC; prior-year identical; NOT every-10 (next every-10 2530); FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_wichelen leftover VAPH/CAR/maatwerk none local after leftover WZC Torkenshof@2521; leftover city_lebbeke leftover VAPH/CAR/maatwerk none local after leftover WZC Reva Tersig@2520; leftover city_meerhout leftover VAPH t Volderke 0432.224.080 SCAN SKIP; leftover CIK fallback not taken; lock leftover city_stabroek leftover WZC Aalmoezenier Cuypers); NOT Torkenshof remine@2521; NOT Reva Tersig remine@2520; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; next rq_2523 leftover dual\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
