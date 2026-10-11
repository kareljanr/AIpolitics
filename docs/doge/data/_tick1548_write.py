#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1548 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import sys
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvoo"
SRC = "src_hvoo_jr2025_bbc"
PDF = "https://oost.hulpverleningszone.be/storage/i3rR7xKSixoE9claxCf2XSYVEfzV1myOsvvwfhGq.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Brandweerzone Oost OVL official zoneraad 22.05.2026 Beknopte lijst Vaststelling rekening 2025,{PDF},Brandweerzone Oost - Oost-Vlaanderen / HVZ Oost OVL,2026-08-20,budget,tick1548; official zoneraad 22.05.2026 Beknopte lijst 7p / 1126629 bytes; pdfinfo ModDate 08.06.2026 06:59:00 UTC Ascertia; signed 08.06.2026; euros PDF only; envelope balanstotaal 13589234 (1537/1538/1540/1541 pattern; uitgaven gewone unpublished)",
        "src_hvoo_kbo_0500927893,KBO Brandweerzone Oost - Oost-Vlaanderen 0500.927.893,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500927893,FPS Economy KBO,2026-08-20,official_register,tick1548; leftover IGS hulpverleningszone of mined Dendermonde + leftover of Berlare/Buggenhout/Hamme/Lebbeke/Lokeren/Moerbeke/Wichelen/Zele; zetel Oude Vest (DEN) 150 9200 Dendermonde; KBO 0500.927.893 Actief; naam Brandweerzone Oost - Oost-Vlaanderen sinds 07.12.2018; rechtsvorm Hulpverleningszone sinds 01.01.2015; 7 VE; prefix hvoo unused; official register resolved",
        "src_hvoo_site,Brandweerzone Oost OVL official zoneraad 2026 page (rekening 2025 besluit published),https://oost.hulpverleningszone.be/pagina/zoneraad-2026,Brandweerzone Oost - Oost-Vlaanderen / HVZ Oost OVL,2026-08-20,official_web,tick1548; leftover IGS of mined Dendermonde; official Beknopte lijst ZR 20260522 live; glossy JV2025 25p 21488675 no spend table; full rekening verslag / uitgaven gewone / pers / werking unpublished",
        "src_hvoo_foi_contact,Brandweerzone Oost OVL FOI channel (administratie@zoneoost.be),https://oost.hulpverleningszone.be/,Brandweerzone Oost - Oost-Vlaanderen / HVZ Oost OVL,2026-08-20,official_web,tick1548; leftover IGS of mined Dendermonde; FOI ready not sent; Oude Vest 150 9200 Dendermonde; official e-mail administratie@zoneoost.be (KBO); NOT leftover HVZ Oost VB 1537 / leftover HVZ Fluvia 1547 / leftover BVLAR 1542 / leftover HVZ Meetjesland 1540 / leftover CAW Oost-Vlaanderen 1532 / leftover CGG Adentro 1511 / leftover HVZ Zuid-Oost / leftover Dijk92",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_hvoo," in raw or raw.startswith(b"igs_hvoo,"):
        raise SystemExit("igs_hvoo already present")
    if b"0500.927.893" in raw or b"0500927893" in raw:
        raise SystemExit("Brandweerzone Oost OVL KBO already present as entity")
    row = (
        "igs_hvoo,Brandweerzone Oost - Oost-Vlaanderen / HVZ Oost OVL / Zone Oost (leftover IGS hulpverleningszone of mined Dendermonde + leftover of Berlare/Buggenhout/Hamme/Lebbeke/Lokeren/Moerbeke/Wichelen/Zele; NOT leftover HVZ Oost VB 1537 / leftover HVZ Fluvia 1547 / leftover BVLAR 1542 / leftover HVZ Meetjesland 1540 / leftover CAW Oost-Vlaanderen 1532 / leftover CGG Adentro 1511 / leftover HVZ Zuid-Oost / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover Dijk92 / leftover Brandweerzone Antwerpen),"
        "Zone de secours Est Flandre orientale (IGS residuel / zone de secours),"
        "HVZ Oost OVL leftover fire-rescue IGS of mined Dendermonde + remaining Oost-Vlaanderen Oost municipalities (not leftover HVZ Oost VB / leftover HVZ Fluvia / leftover BVLAR / leftover HVZ Meetjesland / leftover CAW Oost-Vlaanderen / leftover CGG Adentro / leftover HVZ Zuid-Oost / leftover Dijk92),"
        "other,city_dendermonde,nl,https://oost.hulpverleningszone.be/,administratie@zoneoost.be,Oude Vest 150 9200 Dendermonde,"
        "tick1548 leftover residual IGS hulpverleningszone of mined Dendermonde after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official zoneraad rekening 2025 euros taken; KBO 0500.927.893 Actief official kbo-bce.fgov.be; zetel Dendermonde 9200; live official Beknopte lijst ZR 22.05.2026 7p 1126629; sourced euros balans 13589234 resultaat_gewone_begroting 2011808 resultaat_gewone_boek 2481692 resultaat_buit_begroting -2897489 resultaat_buit_boek 703832 pnl_nadelig 25226; FOI ready not sent; parent city_dendermonde; prefix hvoo; NOT leftover HVZ Oost VB 1537 (do NOT reuse hvzo) / leftover HVZ Fluvia 1547 / leftover HVZ ZWL 1546 / leftover HVZ Noord-Limburg 1545 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover HVZ Zuid-Oost / leftover Dijk92 / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover Erfpunt 1536 / leftover IVAREM 1524"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_hvoo")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
