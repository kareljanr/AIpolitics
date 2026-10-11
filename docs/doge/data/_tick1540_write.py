#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1540 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzm"
SRC = "src_hvzm_jr2025_bbc"
PDF = "https://www.maldegem.be/file/download/80b29791-d19b-4e15-8040-df30f6b2a3de/3GyCecLpP8KnwZad0NCw3WW9QL04GEbFvqjxhQ9RJqI3d.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Hulpverleningszone Meetjesland official zoneraad JR2025 uittreksel,{PDF},HVZ Meetjesland,2026-08-20,budget,tick1540; official zoneraad uittreksel 18.03.2026 Vaststellen jaarrekening 2025; PDF 3p / 740853 bytes; pdfinfo created 02.04.2026 14:03:33 UTC Word/Ascertia; legal basis Wet 15.05.2007 civiele veiligheid + KB 19.04.2014 boekhouding hulpverleningszones (as printed); euros PDF only; full rekening bijlage unpublished",
        "src_hvzm_kbo_0500927596,KBO Hulpverleningszone Meetjesland 0500.927.596,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500927596,FPS Economy KBO,2026-08-20,official_register,tick1540; leftover IGS hulpverleningszone of mined Eeklo + leftover of Aalter/Maldegem/Kaprijke/Sint-Laureins/Deinze-Nevele/Lievegem; zetel Gentsesteenweg 2 9900 Eeklo; KBO 0500.927.596 Actief; prefix hvzm unused",
        "src_hvzm_site,HVZ Meetjesland official site (JR2025 uittreksel published via member-city portal),https://www.zonemeetjesland.be/,HVZ Meetjesland,2026-08-20,official_web,tick1540; leftover IGS of mined Eeklo; official zoneraad 18.03.2026 live on maldegem.be; full rekening bijlage unpublished (inzage / FOI)",
        "src_hvzm_foi_contact,HVZ Meetjesland FOI channel (communicatie@zonemeetjesland.be),https://www.zonemeetjesland.be/contact/admin,HVZ Meetjesland,2026-08-20,official_web,tick1540; leftover IGS of mined Eeklo; FOI ready not sent; Gentsesteenweg 2 9900 Eeklo; official contact communicatie@zonemeetjesland.be / boekhouding@zonemeetjesland.be; NOT leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover WM Meetjesland 1496 / leftover RL Meetjesland 1443",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_hvzm," in raw or raw.startswith(b"igs_hvzm,"):
        raise SystemExit("igs_hvzm already present")
    if b"0500.927.596" in raw or b"0500927596" in raw:
        raise SystemExit("HVZ Meetjesland KBO already present as entity")
    row = (
        "igs_hvzm,Hulpverleningszone Meetjesland / HVZ Meetjesland (leftover IGS hulpverleningszone of mined Eeklo + leftover of Aalter/Maldegem/Kaprijke/Sint-Laureins/Deinze-Nevele/Lievegem-Waarschoot-Zomergem; NOT leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover HVZ Waasland / leftover CAW Oost-Vlaanderen 1532 / leftover CGG Adentro 1511 / leftover Woonmaatschappij Meetjesland 1496 / leftover RL Meetjesland 1443 / leftover IVM / leftover Erfpunt 1536 / leftover IVAREM 1524),"
        "Zone de secours Meetjesland (IGS residuel / zone de secours),"
        "Hulpverleningszone Meetjesland leftover fire-rescue IGS of mined Eeklo + remaining Meetjesland municipalities (not leftover HVZ1 / leftover HVZ Taxandria / leftover HVZ Oost / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover WM Meetjesland / leftover RL Meetjesland / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_eeklo,nl,https://www.zonemeetjesland.be/,communicatie@zonemeetjesland.be,Gentsesteenweg 2 9900 Eeklo,"
        "tick1540 leftover residual IGS hulpverleningszone of mined Eeklo after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official JR2025 uittreksel taken; KBO 0500.927.596 Actief; zetel Eeklo 9900; live JR2025 official zoneraad 18.03.2026; sourced euros assets 4113934 expl 258096 pnl 284889 uitz 26793 equity 3158074 debt 955860 vastgelegd_gewone 6332064; FOI ready not sent; parent city_eeklo; prefix hvzm; NOT leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover CAW Oost-Vlaanderen 1532 / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover WM Meetjesland 1496 / leftover RL Meetjesland 1443"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_hvzm")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
