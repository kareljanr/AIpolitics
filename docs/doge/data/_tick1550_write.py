#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1550 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_crbr"
SRC = "src_crbr_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00178051.pdf"
GAP = "gap_crbr_omzet_4_53m_pers_2_58m_expl_loss_l5"
LB = "lb_crbr_omzet_4_53m_pers_2_58m_expl_loss"
COMM = "comm_crbr_jr2025_omzet"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    fields = next(csv.reader(io.StringIO(row)))
    got = len(fields)
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:180]}")
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")

def part_sources():
    rows = [
        f"{SRC},CREMABRU official NBB C-cap JR2025 deposit 2026-00178051,{PDF},Nationale Bank van Belgie / CREMABRU S.C.I.C.,2026-08-20,budget,tick1550; official NBB WVV C-cap PDF 49p / 1261272 bytes; deposit 2026-00178051 Initial; model C-cap 25.0.13 m02-f; AV 26.05.2026; header 17.06.2026; year-end 31.12.2025; pdfinfo created 20.06.2026 02:31:33 UTC OpenPDF 1.3.26; euros PDF only; envelope omzet 70 4531359 (present; not Erfpunt bruto / not INTRADURA bedrijfsopbrengsten)",
        "src_crbr_kbo_0203389204,KBO CREMABRU / Societe Cooperative Intercommunale de Cremation 0203.389.204,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0203389204,FPS Economy KBO,2026-08-20,official_register,tick1550; leftover IGS crematorium of mined Brussel + leftover of other BHG municipalities; zetel Stillelaan 61 1180 Ukkel; KBO 0203.389.204 Actief; naam Societe Cooperative Intercommunale de Cremation; afkorting Cremabu sinds 14.11.2023; commerciële naam Intercommunale cooperative vennootschap voor Crematie; rechtsvorm Cooperative vennootschap sinds 14.11.2023; 1 VE; prefix crbr unused; official register resolved",
        "src_crbr_nbb_consult,NBB consult CREMABRU 0203389204 published deposit 2026-00178051,https://consult.cbso.nbb.be/consult-enterprise/0203389204,Nationale Bank van Belgie,2026-08-20,official_register,tick1550; leftover IGS of mined Brussel; official NBB consult lists JR2025 deposit 2026-00178051; official CDN same 1261272 bytes as public broker URL used for deposit-id confirm only",
        "src_crbr_foi_contact,CREMABRU FOI channel (directeur@cremabru.be),https://www.cremabru.be/,CREMABRU / Crematorium d Uccle S.C.I.C.,2026-08-20,official_web,tick1550; leftover IGS of mined Brussel; FOI ready not sent; Stillelaan 61 1180 Ukkel; official e-mail directeur@cremabru.be (KBO); NOT leftover Haviland crematorium / leftover Westlede / leftover Hofheide / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_crbr," in raw or raw.startswith(b"igs_crbr,"):
        raise SystemExit("igs_crbr already present")
    if b"0203.389.204" in raw or b"0203389204" in raw:
        raise SystemExit("CREMABRU KBO already present as entity")
    row = (
        "igs_crbr,CREMABRU / Crematorium d Uccle S.C.I.C. / Societe Cooperative Intercommunale de Cremation (leftover IGS crematorium of mined Brussel + leftover of other BHG municipalities Ukkel/Elsene and remaining founders; NOT leftover Haviland crematorium / leftover Westlede / leftover Hofheide / leftover Pontus / leftover OVCO / leftover PSLN / leftover CRHS / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548),"
        "Crematorium d Uccle S.C.I.C. (IGS residuel / crematorium intercommunal BHG),"
        "CREMABRU leftover intercommunal crematorium IGS of mined Brussels + remaining BHG founder municipalities (not leftover Haviland crematorium / leftover Westlede / leftover Hofheide / leftover INTRADURA / leftover Brandweerzone Oost OVL),"
        "other,city_brussel,nl,https://www.cremabru.be/,directeur@cremabru.be,Stillelaan 61 1180 Ukkel,"
        "tick1550 leftover residual IGS crematorium of mined Brussel after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover IGS with live official NBB JR2025 euros taken; KBO 0203.389.204 Actief official kbo-bce.fgov.be; zetel Ukkel 1180; live official NBB C-cap deposit 2026-00178051 49p 1261272; sourced euros assets 12679309 omzet 4531359 opbr 4645123 pers 2583529 vte 31.8 expl -270295 LOSS pnl -216386 LOSS cash 258846 UP beleg 888671 JUMP kapsubs 3023908 JUMP; FOI ready not sent; parent city_brussel; prefix crbr; NOT leftover Haviland crematorium / leftover Westlede / leftover Hofheide / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524"
    )
    check(row, 11, "entities")
    pth.write_bytes(raw + (row + "\n").encode("utf-8"))
    print("entities +1 igs_crbr")

def part_budgets():
    rows = [
        f"bud_crbr_omzet_2025,{ENT},2025,4531359,,,executed,{SRC},strong,2025 omzet 70 4531359 envelope (present; hunt IGS omzet-70-if-present); tick1550; primary official NBB C-cap AV 26.05.2026",
        f"bud_crbr_opbr_2025,{ENT},2025,4645123,,,executed,{SRC},strong,2025 ventes et prestations 70/76A 4645123 (70 4531359 + 74 113764; 76A empty); tick1550; primary official NBB C-cap",
        f"bud_crbr_74_2025,{ENT},2025,113764,,,executed,{SRC},strong,2025 autres produits exploitation 74 113764; tick1550; primary official NBB C-cap",
        f"bud_crbr_assets_2025,{ENT},2025,12679309,,,executed,{SRC},strong,2025 balanstotaal 20/58 12679309 UP was 12388987; VA+vlottend holds; tick1550; primary official NBB C-cap",
        f"bud_crbr_va_2025,{ENT},2025,11309645,,,executed,{SRC},strong,2025 actifs immobilises 21/28 11309645 DROP was 11610870; tick1550; primary official NBB C-cap",
        f"bud_crbr_iva_2025,{ENT},2025,7514,,,executed,{SRC},strong,2025 immobilisations incorporelles 21 7514 DROP was 8587; tick1550; primary official NBB C-cap",
        f"bud_crbr_mva_2025,{ENT},2025,11300236,,,executed,{SRC},strong,2025 immobilisations corporelles 22/27 11300236 DROP was 11600388; tick1550; primary official NBB C-cap",
        f"bud_crbr_gebouwen_2025,{ENT},2025,9686766,,,executed,{SRC},strong,2025 terrains et constructions 22 9686766 DROP was 9861535; tick1550; primary official NBB C-cap",
        f"bud_crbr_install_2025,{ENT},2025,1363422,,,executed,{SRC},strong,2025 installations machines outillage 23 1363422 DROP was 1480672; tick1550; primary official NBB C-cap",
        f"bud_crbr_meubilair_2025,{ENT},2025,228044,,,executed,{SRC},strong,2025 mobilier et materiel roulant 24 228044 DROP was 258181; tick1550; primary official NBB C-cap",
        f"bud_crbr_inaanbouw_2025,{ENT},2025,22005,,,executed,{SRC},strong,2025 immobilisations en cours 27 22005 JUMP was empty; tick1550; primary official NBB C-cap",
        f"bud_crbr_vlottend_2025,{ENT},2025,1369664,,,executed,{SRC},strong,2025 actifs circulants 29/58 1369664 JUMP was 778117; tick1550; primary official NBB C-cap",
        f"bud_crbr_stocks_2025,{ENT},2025,60237,,,executed,{SRC},strong,2025 stocks 3 60237 UP was 49708; tick1550; primary official NBB C-cap",
        f"bud_crbr_handelsrecv_2025,{ENT},2025,79825,,,executed,{SRC},strong,2025 creances commerciales 40 79825 DROP was 94805; tick1550; primary official NBB C-cap",
        f"bud_crbr_otherrecv_2025,{ENT},2025,458,,,executed,{SRC},strong,2025 autres creances 41 458 DROP was 167730; tick1550; primary official NBB C-cap",
        f"bud_crbr_beleg_2025,{ENT},2025,888671,,,executed,{SRC},strong,2025 placements de tresorerie 50/53 888671 JUMP was 209094; tick1550; primary official NBB C-cap",
        f"bud_crbr_cash_2025,{ENT},2025,258846,,,executed,{SRC},strong,2025 valeurs disponibles 54/58 258846 UP was 194216; tick1550; primary official NBB C-cap",
        f"bud_crbr_prepaid_2025,{ENT},2025,81628,,,executed,{SRC},strong,2025 comptes de regularisation actif 490/1 81628 UP was 62564; tick1550; primary official NBB C-cap",
        f"bud_crbr_equity_2025,{ENT},2025,7991093,,,executed,{SRC},strong,2025 capitaux propres 10/15 7991093 UP was 7785466; tick1550; primary official NBB C-cap",
        f"bud_crbr_apport_2025,{ENT},2025,455200,,,executed,{SRC},strong,2025 apport 10/11 455200 (primes emission 455200); tick1550; primary official NBB C-cap",
        f"bud_crbr_herwaard_2025,{ENT},2025,1729368,,,executed,{SRC},strong,2025 plus-values de reevaluation 12 1729368 (toelichting 1729367.53); tick1550; primary official NBB C-cap",
        f"bud_crbr_reserves_2025,{ENT},2025,2782617,,,executed,{SRC},strong,2025 reserves 13 2782617 DROP was 3337977; available 133 2660492 DROP; tick1550; primary official NBB C-cap",
        f"bud_crbr_kapsubs_2025,{ENT},2025,3023908,,,executed,{SRC},strong,2025 subsides en capital 15 3023908 JUMP was 2601896; tick1550; primary official NBB C-cap",
        f"bud_crbr_debt_2025,{ENT},2025,4688216,,,executed,{SRC},strong,2025 dettes 17/49 4688216 UP was 4603521; equity+debt holds 12679309; tick1550; primary official NBB C-cap",
        f"bud_crbr_lt_2025,{ENT},2025,3663163,,,executed,{SRC},strong,2025 dettes a plus d un an 17 3663163; bank 173 3662479; tick1550; primary official NBB C-cap",
        f"bud_crbr_st_2025,{ENT},2025,1003903,,,executed,{SRC},strong,2025 dettes a un an au plus 42/48 1003903 UP was 933287; tick1550; primary official NBB C-cap",
        f"bud_crbr_lev_2025,{ENT},2025,235696,,,executed,{SRC},strong,2025 dettes commerciales 44 235696; fournisseurs 233873; tick1550; primary official NBB C-cap",
        f"bud_crbr_taxsoc_2025,{ENT},2025,501125,,,executed,{SRC},strong,2025 dettes fiscales salariales sociales 45 501125; remunerations 373654; tick1550; primary official NBB C-cap",
        f"bud_crbr_costs_2025,{ENT},2025,4915418,,,executed,{SRC},strong,2025 cout des ventes 60/66A 4915418; tick1550; primary official NBB C-cap",
        f"bud_crbr_60_2025,{ENT},2025,499825,,,executed,{SRC},strong,2025 approvisionnements 60 499825 (achats 510355 stock -10529); tick1550; primary official NBB C-cap",
        f"bud_crbr_61_2025,{ENT},2025,1226879,,,executed,{SRC},strong,2025 services et biens divers 61 1226879 DROP was 1376005; tick1550; primary official NBB C-cap",
        f"bud_crbr_pers_2025,{ENT},2025,2583529,,,executed,{SRC},strong,2025 remunerations 62 2583529 / 31.8 VTE UP was 2495565 / 30.4; YE 37; hours 55694; tick1550; primary official NBB C-cap",
        f"bud_crbr_afschr_2025,{ENT},2025,601524,,,executed,{SRC},strong,2025 amortissements 630 601524 JUMP was 438136; tick1550; primary official NBB C-cap",
        f"bud_crbr_expl_2025,{ENT},2025,-270295,,,executed,{SRC},strong,2025 resultat exploitation 9901 -270295 LOSS was -318273; opbr-costs holds; tick1550; primary official NBB C-cap",
        f"bud_crbr_fin_2025,{ENT},2025,140132,,,executed,{SRC},strong,2025 produits financiers 75/76B 140132 (75 124172 + 76B 15960); tick1550; primary official NBB C-cap",
        f"bud_crbr_fincost_2025,{ENT},2025,86222,,,executed,{SRC},strong,2025 charges financieres 65/66B 86222 (65 86021 + 66B 201); tick1550; primary official NBB C-cap",
        f"bud_crbr_pnl_2025,{ENT},2025,-216386,,,executed,{SRC},strong,2025 resultat 9904 -216386 LOSS was -338975; 9903/9905 same; tax 67/77 empty; official 1-euro vs expl+fin -216385; tick1550; primary official NBB C-cap",
        f"bud_crbr_commissaris_2025,{ENT},2025,8376,,,executed,{SRC},strong,2025 emoluments commissaire 9505 8376 (Stas de Richelle Amaury); extra missions 95063 14083; tick1550; primary official NBB C-cap",
        f"bud_crbr_capex_2025,{ENT},2025,219018,,,executed,{SRC},strong,2025 MVA acquisitions 8161 158445 + 8162 60573 = 219018; tick1550; primary official NBB C-cap",
    ]
    for r in rows:
        check(r, 10, "budgets")
    append_lf(DATA / "budgets.csv", rows)
    print(f"budgets +{len(rows)}")

def part_rest():
    comm = (
        f"{COMM},CREMABRU JR2025 leftover IGS dual (omzet 4.53m / opbr 4.65m / pers 2.58m 31.8 VTE / expl LOSS 0.27m / PnL LOSS 0.22m / assets 12.68m),{ENT},CREMABRU / dual mined Brussel + remaining BHG founder municipalities / municipal crematorium,CSA WVV; ordonnantie 30.03.1995 openbaarheid BHG; Bestuursdecreet analog,2026-05-26,2025,2025,4531359,,,active,{PDF},Local leftover IGS crematorium map BHG Brussel CREMABRU — omzet 4.53m / pers 2.58m / expl LOSS 0.27m / beleg JUMP 0.89m / kapsubs JUMP 3.02m,Publish full AV notulen 26.05.2026 + per-gemeente split + toelichting beleg JUMP / kapsubs JUMP / expl LOSS / commissaris extra 14k; do not keep leftover CREMABRU unpublished,{SRC},strong,Brussel>Gemeenten>Brussel>IGS>CREMABRU>JR2025_L5,tick1550; omzet 4531359 opbr 4645123 pers 2583529 vte 31.8 expl -270295 pnl -216386 assets 12679309 beleg 888671 JUMP kapsubs 3023908 JUMP commissaris 8376 extra 14083; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
    )
    check(comm, 19, "commitments")
    append_lf(DATA / "commitments.csv", [comm])
    print("commitments +1")

    lb = (
        f"{LB},CREMABRU JR2025 leftover IGS: omzet 4.53m / pers 2.58m 31.8 VTE / expl LOSS 0.27m / PnL LOSS 0.22m / assets 12.68m,L5,local_budget_line,Brussel>Gemeenten>Brussel>IGS>CREMABRU>JR2025_L5,4531359,12679309,Leftover dual IGS crematorium shell: omzet 4.53m / opbr 4.65m / pers 2.58m 31.8 VTE / expl LOSS 0.27m / PnL LOSS 0.22m / assets 12.68m / beleg JUMP 0.89m / kapsubs JUMP 3.02m / cash UP 0.26m / commissaris 8376 + extra 14083 / dividend 0,strong,{SRC},CREMABRU / dual mined Brussel + remaining BHG founder municipalities / municipal crematorium,Local leftover IGS crematorium map BHG Brussel CREMABRU — official NBB C-cap JR2025 live; per-gemeente split FOI,Official NBB 2026-08-20: omzet 4.53m / pers 2.58m / expl LOSS 0.27m / assets 12.68m,6.8,3.5,3.0,5.0,Publish full AV notulen 26.05.2026 + per-gemeente split + toelichting beleg JUMP / kapsubs JUMP / expl LOSS / commissaris extra 14k; do not keep leftover CREMABRU unpublished,active,,tick1550; leftover IGS crematorium of mined Brussel after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover Haviland crematorium / leftover Westlede / leftover Hofheide / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524"
    )
    check(lb, 21, "leaderboard")
    append_lf(DATA / "leaderboard.csv", [lb])
    print("leaderboard +1")

    foi = (
        f"{GAP},Brussel>Gemeenten>Brussel>IGS>CREMABRU>JR2025_L5,{ENT},Official NBB C-cap publishes omzet 4531359 / opbr 4645123 / pers 2583529 31.8 VTE / expl LOSS 270295 / PnL LOSS 216386 / assets 12679309 / beleg JUMP 888671 / kapsubs JUMP 3023908; per-gemeente municipal split unpublished; toelichting beleg JUMP / kapsubs JUMP / expl LOSS unpublished; commissaris extra missions 14083 unpublished detail; AV notulen 26.05.2026 unpublished,Leftover IGS crematorium of mined Brussel with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; omzet 4.53m / pers 2.58m / expl LOSS 0.27m,8,CREMABRU / dienst openbaarheid,directeur@cremabru.be,Stillelaan 61 1180 Ukkel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1550 leftover IGS crematorium after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover IGS with live official NBB JR2025 euros taken; official CDN PDF. FOI ready not sent. NOT leftover Haviland crematorium / leftover Westlede / leftover Hofheide / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524"
    )
    check(foi, 21, "foi_queue")
    foi_path = DATA / "foi_queue.csv"
    before = foi_path.stat().st_size
    append_lf(foi_path, [foi])
    after = foi_path.stat().st_size
    if after < before:
        raise SystemExit(f"foi_queue shrank {before} -> {after}")
    print("foi_queue +1 append-only", before, "->", after)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    elif part == "budgets":
        part_budgets()
    elif part == "rest":
        part_rest()
    else:
        raise SystemExit("use sources|entities|budgets|rest")
