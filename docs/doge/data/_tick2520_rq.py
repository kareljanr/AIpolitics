from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2520_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_reva_tersig_lebbeke"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2520,") != 1:
    raise SystemExit(f"bad 2520 count {rq_raw.count(b'rq_2520,')}")
if b"rq_2521," in rq_raw:
    raise SystemExit("2521 exists")
idx = rq_raw.rfind(b"rq_2520,")
if idx < 0:
    raise SystemExit("rq_2520 not found")

notes_2520 = (
    "Took unused leftover public leftover WZC Reva Tersig 0860.679.020 leftover mined city_lebbeke. "
    "Official NBB VKT-VZW YE2025 2026-00307029 native statutory 13p. Envelope bruto9900 DROP 3117153 "
    "(VKT because omzet70+73 empty; 76A JUMP 66043); cash DROP 162617; pnl FLIP -454073; 9901 FLIP -453340; "
    "equity DROP 958018; assets DROP 2483710; debt JUMP 1525692; FTE JUMP 50.8. "
    "FIRST leftover unused + live official YE2025 after leftover-type hunt "
    "(lock first valid hit leftover city_lebbeke leftover WZC after leftover city_meerhout leftover WZC Ter Kempen@2519; leftover city_lennik leftover maatwerk Maatwerkbedrijf Pajottenland 0413.313.535 remine@2201 already entity vzw_mwp_pajottenland; leftover city_scherpenheuvel_zichem leftover types exhausted De Vlaspit@2515 / Honighsdries@2516 / Levensruimte@2517 / De Schommel@2518). "
    "NOT leftover WZC Hof ter Veldeken OCMW Lebbeke 0212.192.151. NOT leftover WZC Seniorie Ter Minne BV 0444.150.330 commercial. NOT leftover WZC Seniorie Minneveld BV 0840.544.095 commercial. "
    "NOT Pajottenland remine@2201. NOT Ter Kempen remine@2519. NOT leftover-via-VE. "
    "NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Zorg-Saam remine."
)
extra_2520 = (
    "tick2520 leftover mined city_lebbeke leftover WZC; Strong native PDF; 1 VE; prior-year identical; EVERY-10 (next every-10 2530); next rq_2521 leftover dual"
)
notes_2521 = (
    "Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "NOT every-10 (next every-10 is 2530). "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_lebbeke leftover WZC taken (Reva Tersig@2520; leftover WZC Hof ter Veldeken OCMW 0212.192.151 SKIP; leftover WZC Seniorie Ter Minne BV 0444.150.330 commercial SKIP; leftover WZC Seniorie Minneveld BV 0840.544.095 commercial SKIP). leftover city_lebbeke leftover VAPH/CAR/CIK/maatwerk still unused-looking. "
    "NOW leftover city_lennik leftover maatwerk Maatwerkbedrijf Pajottenland 0413.313.535 remine@2201 already entity vzw_mwp_pajottenland SKIP. leftover city_londerzeel slug MISSING. leftover city_wortegem_petegem slug MISSING. leftover city_wichelen leftover WZC Den Anker 0812.060.838 still unused-looking (skip if leftover-via-VE / remine). "
    "NOW leftover city_meerhout leftover WZC taken (Ter Kempen@2519; leftover WZC De Berk OCMW 0212.196.705 SKIP; leftover maatwerk De Sprong remine@2286 parent sec_flanders). leftover city_meerhout leftover VAPH/CAR/CIK still unused-looking. "
    "NOW leftover city_oosterzele leftover WZC Groep Sint-Franciscus 0412.763.704 remine@2142 zetel Brakel SKIP. leftover city_herselt leftover WZC Sint-Barbara remine@2019. "
    "NOW leftover city_scherpenheuvel_zichem leftover types exhausted (De Vlaspit@2515 / Honighsdries@2516 / Levensruimte@2517 / De Schommel@2518). leftover WZC OLV Ster der Zee still unused-looking likely OCMW. leftover WZC Voortberg Armonea SKIP. leftover CAR none local. "
    "NOW leftover city_zottegem leftover WZC taken (De Bron@2512). leftover city_zottegem leftover VAPH taken (De Hoop@2513). leftover city_zottegem leftover CIK taken (Sint-Elisabeth@2514). leftover city_zottegem leftover CAR Wegwijs remine. leftover maatwerk BWZ remine@2196. leftover hospital AZ Zottegem remine. "
    "NOW leftover city_grimbergen leftover WZC taken (Den Bogaet@2511). leftover maatwerk Den Diepen Boomgaard@2510. leftover VAPH Havinet remine@2301. leftover WZC Heilig Hart remine@2074. leftover CAR none local. leftover CIK Kribbekrabbel BV + FERM leftover-via-VE Leuven. "
    "NOW leftover city_asse leftover CIK taken (Kribbe Kinderpret@2509). leftover city_geraardsbergen leftover maatwerk taken (De Dagmoed@2508). leftover city_buggenhout leftover VAPH taken (Avalon@2503 + Capelderij@2507; leftover WZC De Heymeulen HARD SKIP). leftover city_wetteren leftover CIK+VAPH taken leftover WZC/CAR/maatwerk remine. leftover city_herzele leftover WZC taken (Hunnegem@2504). "
    "leftover city_niel still unused (2845 VZW census sports/culture only). leftover city_mol leftover CIK Molleke YE2024 SKIP. leftover city_denderleeuw leftover CIK t Sas YE2024 SKIP. leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open. leftover city_steenokkerzeel leftover WZC Floordam remine. leftover city_bornem leftover WZC remine leftover VAPH maybe unused. leftover city_puurs leftover WZC exhausted. leftover city_waregem leftover maatwerk remine. "
    "HARD SKIP: Gravenkasteel group 0874.863.091. All OCMW / Armonea / Korian / Vulpia / CuraCare / Emeis / Zorgbedrijf. AZ Waregem SCAN HARD SKIP. De Heymeulen HARD SKIP. Jules/i-mens leftover-via-VE SKIP. Stay OFF Kloosterstraat 6 Drongen. city_kapellen slug MISSING. "
    "NOT Reva Tersig remine. NOT Ter Kempen remine. NOT De Schommel remine. NOT Huize Levensruimte remine. NOT Huyze Honighsdries remine. NOT De Vlaspit remine. NOT Sint-Elisabeth remine. NOT De Hoop remine. NOT De Bron remine. NOT Den Bogaet remine. NOT Den Diepen Boomgaard remine. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2521 = (
    "spawned after tick2520 leftover city_lebbeke leftover WZC EVERY-10; Reva Tersig taken leftover mined city_lebbeke leftover WZC; leftover WZC Hof ter Veldeken OCMW SKIP; leftover WZC Seniorie Ter Minne/Minneveld BV commercial SKIP; leftover city_lennik leftover maatwerk Pajottenland remine@2201; leftover city_wichelen leftover WZC Den Anker unused-looking; leftover city_meerhout leftover WZC taken leftover VAPH/CAR/CIK unused-looking; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; leftover city_zottegem leftover WZC+VAPH+CIK taken; leftover city_grimbergen leftover WZC+maatwerk taken; leftover city_londerzeel slug MISSING; leftover city_wortegem_petegem slug MISSING; leftover city_niel still unused; leftover city_mol leftover CIK Molleke YE2024; leftover city_denderleeuw leftover CIK t Sas YE2024; leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open; AZ Waregem SCAN HARD SKIP; Jules/i-mens leftover-via-VE SKIP; NOT every-10 (next every-10 2530)"
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

new_2520 = rq_line([
    "rq_2520",
    "leftover dual Reva Tersig YE2025 EVERY-10",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2520,
    "",
    STAMP,
    STAMP,
    extra_2520,
])
new_2521 = rq_line([
    "rq_2521",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2521,
    "",
    STAMP,
    STAMP,
    extra_2521,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2520)
    f.write(new_2521)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2520", chk.count(b"rq_2520,"), "n2521", chk.count(b"rq_2521,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2520,2520,no,"
    "tick2520 leftover dual Reva Tersig 0860.679.020 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A JUMP 66043; envelope bruto9900 DROP 3117153; pnl FLIP -454073; 9901 FLIP -453340; equity DROP 958018; assets DROP 2483710; debt JUMP 1525692; FTE JUMP 50.8; kapitaalsubsidies empty; destin691 empty; cash DROP 162617; 1 VE leftover city_lebbeke leftover WZC); leftover mined city_lebbeke leftover WZC; prior-year identical; EVERY-10 (next every-10 2530); FIRST leftover unused + live official YE2025 after leftover-type hunt (lock Reva Tersig first valid hit leftover city_lebbeke leftover WZC after leftover city_meerhout leftover WZC Ter Kempen@2519 + leftover city_lennik leftover maatwerk Pajottenland remine@2201 already entity; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; leftover WZC Hof ter Veldeken OCMW SKIP; leftover WZC Seniorie Ter Minne/Minneveld BV commercial SKIP); NOT Pajottenland remine@2201; NOT Ter Kempen remine@2519; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; next rq_2521 leftover dual\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
