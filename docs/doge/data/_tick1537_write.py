#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1537 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzo"
SRC = "src_hvzo_jr2025_bbc"
PDF = "https://oost-vlaams-brabant.hulpverleningszone.be/storage/AKwBj1sHddY6KSHKufRCMX9Td2EuKSU8mdaMqknP.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Hulpverleningszone Oost Vlaams-Brabant official zoneraad JR2025 besluit,{PDF},HVZ Oost Vlaams-Brabant,2026-08-20,budget,tick1537; official zoneraad besluit 2026_ZR_00026 Jaarrekening 2025 voorlopige afsluiting Goedkeuring 22.04.2026; PDF 3p / 130439 bytes; pdfinfo created 22.04.2026 14:39:47 UTC ModDate 27.04.2026 10:32:50 UTC; legal basis Wet 15.05.2007 civiele veiligheid + KB 19.04.2014 boekhouding hulpverleningszones Hoofdstuk 4; euros PDF only; Rekening_2025_deel_1/2/3 unpublished (inzage zetel only)",
        "src_hvzo_kbo_0500928982,KBO Hulpverleningszone Oost Vlaams-Brabant 0500.928.982,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500928982,FPS Economy KBO,2026-08-20,official_register,tick1537; leftover IGS hulpverleningszone of mined Herent + leftover of 31 other Oost-VB municipalities; zetel Spoorwegstraat 6 3020 Herent; KBO 0500.928.982 Actief; prefix hvzo unused",
        "src_hvzo_agenda,HVZ Oost Vlaams-Brabant agenda en besluiten (JR2025 published),https://oost-vlaams-brabant.hulpverleningszone.be/pagina/agenda-en-besluiten,HVZ Oost Vlaams-Brabant,2026-08-20,official_web,tick1537; leftover IGS; ZR20260422_3_Jaarrekening 2025.pdf live; Rekening_2025_deel_1/2/3 listed as bijlagen but not published (inzage zetel Herent + gemeentehuizen)",
        "src_hvzo_foi_contact,HVZ Oost Vlaams-Brabant FOI channel (info@hvzoost.be),https://oost-vlaams-brabant.hulpverleningszone.be/pagina/administratieve-diensten,HVZ Oost Vlaams-Brabant,2026-08-20,official_web,tick1537; leftover IGS of mined Herent; FOI ready not sent; Spoorwegstraat 6 3020 Herent; official contact info@hvzoost.be; NOT leftover Brandweerzone Antwerpen / leftover CAW Oost-Brabant 1530 / leftover CGG VBO 1509 / leftover Kanvaz",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_hvzo," in raw or raw.startswith(b"igs_hvzo,"):
        raise SystemExit("igs_hvzo already present")
    if b"0500.928.982" in raw or b"0500928982" in raw:
        raise SystemExit("HVZ Oost VB KBO already present as entity")
    row = (
        "igs_hvzo,Hulpverleningszone Oost Vlaams-Brabant / HVZ Oost (leftover IGS hulpverleningszone of mined Herent + leftover of 31 other Oost-VB municipalities Aarschot/Leuven/Tienen/Diest/Tervuren/Overijse and remaining; NOT leftover Brandweerzone Antwerpen / leftover CAW Oost-Brabant 1530 / leftover CGG VBO 1509 / leftover CGG PassAnt 1520 / leftover Kanvaz / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Zone de secours Est Brabant flamand (IGS residuel / zone de secours),"
        "Hulpverleningszone Oost Vlaams-Brabant leftover fire-rescue IGS of mined Herent + remaining Oost-VB municipalities (not leftover Brandweerzone Antwerpen / leftover CAW Oost-Brabant / leftover CGG VBO / leftover Kanvaz / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_herent,nl,https://oost-vlaams-brabant.hulpverleningszone.be/,info@hvzoost.be,Spoorwegstraat 6 3020 Herent,"
        "tick1537 leftover residual IGS hulpverleningszone of mined Herent after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official JR2025 besluit taken; KBO 0500.928.982 Actief; zetel Herent 3020; live JR2025 official zoneraad besluit 2026_ZR_00026 22.04.2026; sourced euros assets 48137974 expl 4279776 pnl 3557913 uitz_kosten 6887696 uitz_opbr 6165833 begroting_gewone 6378403; FOI ready not sent; parent city_herent; prefix hvzo; NOT leftover Brandweerzone Antwerpen / leftover CAW Oost-Brabant 1530 / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover Erfpunt 1536 / leftover IVAREM 1524"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_hvzo")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
