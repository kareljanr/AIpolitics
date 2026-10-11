from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2518_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_schommel_scherpenheuvel"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2518,") != 1:
    raise SystemExit(f"bad 2518 count {rq_raw.count(b'rq_2518,')}")
if b"rq_2519," in rq_raw:
    raise SystemExit("2519 exists")
idx = rq_raw.rfind(b"rq_2518,")
if idx < 0:
    raise SystemExit("rq_2518 not found")

notes_2518 = (
    "Took unused leftover public leftover CIK De Schommel 0462.203.119 leftover mined city_scherpenheuvel_zichem. "
    "Official NBB VOL-VZW YE2025 2026-00270709 native statutory 31p. Envelope 70/76A JUMP 6341052 "
    "(VZW because omzet commercial-only vs large 73; 70 JUMP 47971; 73 JUMP 6186326; 76A JUMP 9000); "
    "cash JUMP 1022183; pnl DROP 265345; 9901 DROP 269556; equity JUMP 4000132; debt JUMP 1260751; FTE JUMP 63. "
    "FIRST leftover unused + live official YE2025 after leftover-type hunt "
    "(lock first valid hit leftover city_scherpenheuvel_zichem leftover CIK after leftover VAPH Huize Levensruimte@2517 + leftover WZC Huyze Honighsdries@2516 + leftover maatwerk De Vlaspit@2515; "
    "leftover WZC Voortberg Armonea 0889.421.308 SKIP; leftover WZC OLV Ster der Zee still unused-looking likely OCMW; leftover CAR none local). "
    "NOT Huize Levensruimte 0407.731.976 remine leftover VAPH@2517. NOT Huyze Honighsdries 0891.481.666 remine leftover WZC@2516. NOT De Vlaspit 0461.019.224 remine leftover maatwerk@2515. NOT leftover-via-VE. "
    "NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Zorg-Saam remine. NOT Wonozo leftover jeugdhulp."
)
extra_2518 = (
    "tick2518 leftover mined city_scherpenheuvel_zichem leftover CIK; Strong native PDF; 2 VE; 1 VE Tienen is VE of SZ-seated parent; site Leuven not a KBO VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2519 leftover dual"
)
notes_2519 = (
    "Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_scherpenheuvel_zichem leftover CIK taken (De Schommel@2518; 2 VE official zetel SZ; 1 VE Tienen is VE of SZ-seated parent; site Leuven not a KBO VE). leftover city_scherpenheuvel_zichem leftover VAPH taken (Huize Levensruimte@2517; 2 VE official zetel SZ; 1 VE Perron Z Aarschot is VE of SZ-seated parent). leftover city_scherpenheuvel_zichem leftover WZC taken (Huyze Honighsdries@2516; leftover WZC Voortberg Armonea SKIP; leftover WZC OLV Ster der Zee still unused-looking likely OCMW). leftover city_scherpenheuvel_zichem leftover maatwerk taken (De Vlaspit@2515). leftover CAR none local. "
    "NOW leftover city_zottegem leftover WZC taken (De Bron@2512). leftover city_zottegem leftover VAPH taken (De Hoop@2513). leftover city_zottegem leftover CIK taken (Sint-Elisabeth@2514; Piet Konijn = Sint-Elisabeth brand). leftover city_zottegem leftover CAR Wegwijs 0408.203.021 remine parent sec_flanders. leftover maatwerk BWZ 0407.657.148 remine@2196 parent sec_flanders. leftover hospital AZ Zottegem remine tick2009/2018. "
    "NOW leftover city_grimbergen leftover WZC taken (Den Bogaet@2511; leftover WZC Heilig Hart remine@2074 parent sec_flanders; leftover VAPH Havinet remine@2301; leftover maatwerk Den Diepen Boomgaard@2510; leftover CAR none local; leftover CIK Kribbekrabbel BV + FERM leftover-via-VE Leuven). "
    "NOW leftover city_asse leftover CIK taken (Kribbe Kinderpret@2509; 3Wplus Kinderopvang@2407; Vijverbeek@2469; leftover VAPH Hopperank@2491; leftover maatwerk 3Wplus Werk@2492). "
    "NOW leftover city_geraardsbergen leftover maatwerk taken (De Dagmoed@2508; leftover CAR Horizon@2395; leftover WZC OCMW/commercial/YE2023; leftover jeugdhulp Wonozo skip; leftover CIK no local leftover VZW). "
    "NOW leftover city_buggenhout leftover VAPH taken (Avalon@2503 + Capelderij@2507; leftover WZC De Heymeulen 0420.669.303 still YE2024 HARD SKIP). leftover city_buggenhout leftover CAR Buggenhout leftover-via-VE Gent SKIP. "
    "NOW leftover city_wetteren leftover CIK taken (Sint-Jozef@2502 + Fiola@2506; leftover VAPH Sint-Lodewijk@2505; leftover WZC Zorg-Saam remine leftover-via-VE Gent; leftover CAR/maatwerk Trianval remine). "
    "NOW leftover city_herzele leftover WZC taken (Hunnegem@2504; leftover VAPH De Kanteling/VillaVip no JR; leftover CAR none local Kapelhof leftover-via-VE Drongen SKIP; leftover maatwerk no local VZW Kringwinkel ZOV leftover-via-VE). leftover CIK Bengeltjes/Klettekes BV skip. "
    "leftover city_bornem leftover WZC remine (OLV remine@2065; De Vlietoever BV skip; Eyckerheyde remine@2341; leftover CAR Ter Linde taken@2482). leftover VAPH still unused-looking maybe (Pegode leftover-via-VE; Weerklank 1022.178.377 founded 09.04.2025 no JR). "
    "leftover city_puurs leftover WZC/VAPH exhausted (Sint-Pieter OCMW remine; Anemoon SLG/Korian remine; Sauvegarde CuraCare; Gravenkasteel Armonea; maatwerk Nektari taken). "
    "leftover city_waregem leftover maatwerk remine (Werkplus@2204); leftover VAPH Ten Anker taken; leftover CIK Kindercentrum + t Zonnetje taken; AZ Waregem SCAN HARD SKIP. "
    "leftover city_niel still unused (2845 VZW census sports/culture only; Lief & Leef BV skip — only take a real leftover care dual). "
    "leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open/empty (WZC Avondzon + Meredal taken; Pamperbroekje leftover CIK BV unused not locked). "
    "leftover city_mol leftover WZC remine/commercial/OCMW; leftover CIK Molleke 0448.186.520 YE2024 SKIP. leftover city_denderleeuw leftover WZC Armonea commercial; leftover CIK t Sas YE2024 SKIP. leftover city_mol/denderleeuw still zero leftover children parented under city_*. "
    "leftover city_tielt leftover CAR/maatwerk empty. leftover city_lokeren leftover VAPH Hagewinde+Alderande + maatwerk De Sperwer taken; leftover CIK EVA remine@1253; leftover CIK Junior 0 NBB. "
    "leftover city_schilde leftover WZC Sint-Lodewijk 0410.127.084 remine@2168 parent sec_flanders. leftover city_herselt leftover WZC Sint-Barbara remine@2019. leftover city_haacht leftover WZC Langerheide remine@2173. leftover city_merchtem leftover WZC Ter Stelten OCMW + Armonea Martinas commercial. leftover city_willebroek leftover WZC Ten Weldebrouc OCMW. leftover city_oosterzele leftover WZC empty leftover VAPH empty. leftover city_evergem leftover WZC Zusters Franciscanessen convent-class + YE2024 / Belscope YE2025 conflict SKIP. leftover city_dendermonde leftover WZC OCMW/Evara/Korian/Zorg-Saam leftover-via-VE Gent; leftover VAPH Blijdorp remine / Hippocare commercial. leftover city_zele leftover WZC De Vliet leftover-via-VE Hamme; leftover VAPH VillaVip no JR; leftover maatwerk Wase Werkplaats leftover-via-VE Temse. leftover city_ronse leftover WZC Hogerlucht = Werken Glorieux remine; leftover maatwerk Grijkoort taken. leftover city_pelt leftover maatwerk Noord-Limburgs Open Atelier 0451.320.313 YE2024 only. leftover city_zoersel leftover WZC Joostens leftover-via-VE Zorgbedrijf Antwerpen. "
    "HARD SKIP: Het Dak 0863.329.989 0 NBB; De Lindeboom remine 2159; MILLE LUCI no JR; GPN SZ ML 0471.795.132 unless leftover city_sint_niklaas actually mined unused leftover type + native YE2025 under 5 min. "
    "AZ Waregem 0405.460.592 unused leftover hospital YE2025 SCAN/OCR HARD SKIP do not invent euros. De Heymeulen leftover city_buggenhout WZC HARD SKIP. "
    "Jules/i-mens 0416.603.716 zetel Gent leftover-via-VE / large chain SKIP. "
    "De Bolster 0861.680.989 zetel Zwalm leftover-via-VE SKIP. "
    "Stay OFF Kloosterstraat 6 Drongen. CAR Kapelhof / Ter Kouter / Buggenhout leftover-via-VE Gent SKIP. city_kapellen slug MISSING. KEERPUNT leftover-via-VE SKIP. VBJK leftover Gent training skip. "
    "NOT De Schommel remine. NOT Huize Levensruimte remine. NOT Huyze Honighsdries remine. NOT De Vlaspit remine. NOT Kinderdagverblijf Sint-Elisabeth remine. NOT De Hoop remine. NOT De Bron remine. NOT Den Bogaet remine. NOT Den Diepen Boomgaard remine. NOT Kribbe Kinderpret remine. "
    "NOT leftover-via-VE. NOT KEERPUNT leftover-via-VE Gent. NOT CAR Buggenhout leftover-via-VE Gent. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2519 = (
    "spawned after tick2518 leftover city_scherpenheuvel_zichem leftover CIK; De Schommel taken leftover mined city_scherpenheuvel_zichem leftover CIK; leftover VAPH Huize Levensruimte taken@2517; leftover WZC Huyze Honighsdries taken@2516; leftover maatwerk De Vlaspit taken@2515; leftover WZC OLV Ster der Zee still unused-looking likely OCMW; leftover WZC Voortberg Armonea SKIP; leftover CAR none local; leftover city_zottegem leftover WZC+VAPH+CIK taken; leftover city_zottegem leftover CAR Wegwijs remine; leftover maatwerk BWZ remine; leftover city_grimbergen leftover WZC+maatwerk taken; leftover city_asse leftover CIK taken; leftover city_geraardsbergen leftover maatwerk taken; leftover city_buggenhout leftover VAPH taken; leftover city_buggenhout WZC De Heymeulen still YE2024; leftover city_wetteren leftover CIK+VAPH taken leftover WZC/CAR/maatwerk remine; leftover city_niel still unused; leftover city_mol leftover CIK Molleke YE2024; leftover city_denderleeuw leftover CIK t Sas YE2024; leftover city_herzele leftover VAPH De Kanteling/VillaVip no JR leftover maatwerk leftover-via-VE; leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open; leftover city_bornem leftover WZC remine leftover VAPH maybe unused; leftover city_puurs leftover WZC exhausted; leftover city_waregem leftover maatwerk remine; leftover city_schilde leftover WZC remine; leftover city_herselt leftover WZC remine; leftover city_haacht leftover WZC remine; leftover city_pelt leftover maatwerk YE2024; AZ Waregem SCAN HARD SKIP; Jules/i-mens leftover-via-VE SKIP; De Bolster leftover-via-VE SKIP; Het Dak 0 NBB SKIP; this tick is NOT every-10 (next every-10 2520)"
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

new_2518 = rq_line([
    "rq_2518",
    "leftover dual De Schommel YE2025",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2518,
    "",
    STAMP,
    STAMP,
    extra_2518,
])
new_2519 = rq_line([
    "rq_2519",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2519,
    "",
    STAMP,
    STAMP,
    extra_2519,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2518)
    f.write(new_2519)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2518", chk.count(b"rq_2518,"), "n2519", chk.count(b"rq_2519,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2518,2518,no,"
    "tick2518 leftover dual De Schommel 0462.203.119 Strong native PDF (omzet70 JUMP 47971 commercial-only; 73 JUMP 6186326; 76A JUMP 9000; envelope 70/76A JUMP 6341052; pnl DROP 265345; 9901 DROP 269556; equity JUMP 4000132; assets JUMP 5526522; debt JUMP 1260751; FTE JUMP 63; kapitaalsubsidies DROP 40622; destin691 DROP 66337; cash JUMP 1022183; 2 VE leftover city_scherpenheuvel_zichem leftover CIK); leftover mined city_scherpenheuvel_zichem leftover CIK; 1 VE Tienen is VE of SZ-seated parent; site Leuven not a KBO VE; prior-year identical; NOT every-10 (next every-10 2520); FIRST leftover unused + live official YE2025 after leftover-type hunt (lock De Schommel first valid hit leftover city_scherpenheuvel_zichem leftover CIK after leftover VAPH Huize Levensruimte@2517 + leftover WZC Huyze Honighsdries@2516 + leftover maatwerk De Vlaspit@2515; leftover WZC Voortberg Armonea SKIP; leftover WZC OLV Ster der Zee still unused-looking likely OCMW; leftover CAR none local); NOT Huize Levensruimte remine leftover VAPH@2517; NOT Huyze Honighsdries remine leftover WZC@2516; NOT De Vlaspit remine leftover maatwerk@2515; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; next rq_2519 leftover dual\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
