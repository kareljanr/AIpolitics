# -*- coding: utf-8 -*-
"""Tick 1398 — leftover IGS IBEG JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1398"
UTC = "2026-08-19T05:05:00Z"
ENT = "igs_ibeg"
HIER = "Vlaanderen>VlaamsBrabant>IGS>IBEG"
GAP = "gap_ibeg_omzet_empty_div_3_50m_fva_96_37m_l5"
SRC = "src_ibeg_jr2025_nbb"
SRC2 = "src_ibeg_site"
SRC3 = "src_kbo_ibeg_0202082078"
SRC4 = "src_ibeg_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00238388.pdf"
SRC2_URL = "https://ibeg.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0202082078"
SRC4_URL = "https://ibeg.be/contact/"
FOI_EMAIL = "info@ibeg.be"
FOI_POSTAL = "Laurent Benoit Dewezplein 6 1800 Vilvoorde"
DRAFT = "docs/doge/foi/drafts/gap_ibeg_omzet_empty_div_3_50m_fva_96_37m_l5.md"
COMM = "comm_ibeg_jr2025_pnl"
LB = "lb_ibeg_omzet_empty_div_3_50m_fva_96_37m"
VENNOTEN = "Grimbergen + Machelen + Meise + Vilvoorde + Wemmel (ibeg.be; leftover IGS energy holding HV)"


def append_rows(path, new_rows):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing_ids = set()
        id_key = fields[0]
        for row in reader:
            existing_ids.add(row.get(id_key))
    added = 0
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        for row in new_rows:
            if row.get(id_key) in existing_ids:
                continue
            w.writerow({k: row.get(k, "") for k in fields})
            added += 1
    return added


def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()


def patch_last_rq_and_spawn(path, target_id, new_target, spawn_row):
    header = path.open(encoding="utf-8").readline()
    fields = next(csv.reader([header.strip("\n").strip("\r")]))
    with path.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        chunk = min(size, 131072)
        f.seek(size - chunk)
        tail = f.read()
    if tail.endswith(b"\n"):
        search = tail[:-1]
    else:
        search = tail
    last_nl = search.rfind(b"\n")
    last_line = search[last_nl + 1 :] if last_nl != -1 else search
    last_text = last_line.decode("utf-8")
    if not last_text.startswith(target_id + ","):
        raise SystemExit("last rq line is not %s: %s" % (target_id, last_text[:160]))
    last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
    spawn_id = spawn_row.get("task_id")
    if spawn_id and spawn_id.encode("utf-8") in tail:
        raise SystemExit("spawn id already in tail")
    payload = (csv_line(fields, new_target) + "\n" + csv_line(fields, spawn_row) + "\n").encode("utf-8")
    with path.open("r+b") as f:
        f.seek(last_start)
        f.truncate()
        f.write(payload)
    return True, True


BUDGETS = [
    ("bud_ibeg_assets_2025", "2025", "100488193", "2025 assets 100488193 VOL-inb 20/58; tick1398; primary official NBB WVV"),
    ("bud_ibeg_assets_2024", "2024", "103058477", "2024 assets 103058477 comparative; tick1398; primary official NBB WVV 20/58"),
    ("bud_ibeg_fixed_2025", "2025", "96372430", "2025 vaste activa 96372430 all FVA; MVA/IVA empty; tick1398; primary official NBB WVV 21/28"),
    ("bud_ibeg_fva_2025", "2025", "96372430", "2025 FVA 96372430 vs 96872430; tick1398; primary official NBB WVV 28"),
    ("bud_ibeg_fva_rel_2025", "2025", "83085538", "2025 verbonden FVA 83085538 vs 83585538; tick1398; primary official NBB WVV 280/1"),
    ("bud_ibeg_fva_part_2025", "2025", "74085538", "2025 verbonden deelnemingen 74085538 (Fluvius HV 64830538 + VENTUM 9255000); tick1398; primary official NBB WVV 280"),
    ("bud_ibeg_fva_loan_2025", "2025", "9000000", "2025 verbonden vorderingen 9000000 vs 9500000 (Fluvius HV credit; facility 30m); tick1398; primary official NBB WVV 281"),
    ("bud_ibeg_fva_oth_2025", "2025", "13286892", "2025 andere aandelen 13286892 (Publigas 423 + Publi-T 20117); tick1398; primary official NBB WVV 284"),
    ("bud_ibeg_fhv_fva_2025", "2025", "64830538", "2025 Fluvius HV 21.48pct valued 64830538.49; tick1398; primary official NBB WVV 6.19"),
    ("bud_ibeg_ventum_fva_2025", "2025", "9255000", "2025 VENTUM&green 92.55pct valued 9255000; tick1398; primary official NBB WVV 6.19"),
    ("bud_ibeg_current_2025", "2025", "4115762", "2025 vlottend 4115762 vs 6186047; tick1398; primary official NBB WVV 29/58"),
    ("bud_ibeg_strecv_2025", "2025", "576007", "2025 ST vorderingen 576007 tax prepaid; tick1398; primary official NBB WVV 40/41"),
    ("bud_ibeg_invest_2025", "2025", "1697144", "2025 geldbeleggingen 1697144 DROP vs 3330349; tick1398; primary official NBB WVV 50/53"),
    ("bud_ibeg_invest_2024", "2024", "3330349", "2024 geldbeleggingen 3330349 comparative; tick1398; primary official NBB WVV 50/53"),
    ("bud_ibeg_bonds_2025", "2025", "1501788", "2025 vastrentende effecten 1501788 vs 3066794; tick1398; primary official NBB WVV 52"),
    ("bud_ibeg_termijn_2025", "2025", "195357", "2025 termijnrekeningen >1y 195357 vs 263555; tick1398; primary official NBB WVV 53"),
    ("bud_ibeg_cash_2025", "2025", "1842610", "2025 liquide middelen 1842610 vs 1638882; tick1398; primary official NBB WVV 54/58"),
    ("bud_ibeg_cash_2024", "2024", "1638882", "2024 liquide middelen 1638882 comparative; tick1398; primary official NBB WVV 54/58"),
    ("bud_ibeg_equity_2025", "2025", "99038008", "2025 EV 99038008 vs 101254697; tick1398; primary official NBB WVV 10/15"),
    ("bud_ibeg_inbreng_2025", "2025", "94803958", "2025 inbreng onbeschikbaar 94803958 / 764918 aandelen; tick1398; primary official NBB WVV 10/11"),
    ("bud_ibeg_reserves_2025", "2025", "3159688", "2025 reserves 3159688 (onbeschikbaar 39527 / beschikbaar 3120162); tick1398; primary official NBB WVV 13"),
    ("bud_ibeg_re_2025", "2025", "1074362", "2025 overgedragen winst 1074362 vs 3371541; tick1398; primary official NBB WVV 14"),
    ("bud_ibeg_debt_2025", "2025", "1450184", "2025 schulden 1450184 vs 1803780; no LT; tick1398; primary official NBB WVV 17/49"),
    ("bud_ibeg_debt_2024", "2024", "1803780", "2024 schulden 1803780 comparative; tick1398; primary official NBB WVV 17/49"),
    ("bud_ibeg_st_2025", "2025", "1450184", "2025 ST schulden 1450184; tick1398; primary official NBB WVV 42/48"),
    ("bud_ibeg_sttrade_2025", "2025", "450184", "2025 leveranciers 450184 vs empty; tick1398; primary official NBB WVV 440/4"),
    ("bud_ibeg_stoth_2025", "2025", "1000000", "2025 overige ST 1000000 vs 1803780 (saldo dividend); tick1398; primary official NBB WVV 47/48"),
    ("bud_ibeg_diensten_2025", "2025", "809703", "2025 diensten 809703 JUMP vs 271411; omzet 70 empty; tick1398; primary official NBB WVV 61"),
    ("bud_ibeg_diensten_2024", "2024", "271411", "2024 diensten 271411 comparative; tick1398; primary official NBB WVV 61"),
    ("bud_ibeg_othcost_2025", "2025", "7012", "2025 andere bedrijfskosten 7012 vs 6093; tick1398; primary official NBB WVV 641/8"),
    ("bud_ibeg_nrec_2025", "2025", "519509", "2025 niet-recurrent 66A 519509 minderwaarde realisatie / onttrekking investeringsreserve; tick1398; primary official NBB WVV 66A"),
    ("bud_ibeg_expl_2025", "2025", "-1336225", "2025 expl -1336225 vs -874818; tick1398; primary official NBB WVV 9901"),
    ("bud_ibeg_expl_2024", "2024", "-874818", "2024 expl -874818 comparative; tick1398; primary official NBB WVV 9901"),
    ("bud_ibeg_fininc_2025", "2025", "2640731", "2025 fin opbr 2640731 vs 3556828; tick1398; primary official NBB WVV 75/76B"),
    ("bud_ibeg_fva_inc_2025", "2025", "2318574", "2025 opbrengsten FVA 2318574 DBI aftrek; tick1398; primary official NBB WVV 750"),
    ("bud_ibeg_fincost_2025", "2025", "21195", "2025 fin kosten 21195 vs 54684; tick1398; primary official NBB WVV 65/66B"),
    ("bud_ibeg_pnl_2025", "2025", "1283311", "2025 PnL +1283311 vs +2627327; tick1398; primary official NBB WVV 9904"),
    ("bud_ibeg_pnl_2024", "2024", "2627327", "2024 PnL +2627327 comparative; tick1398; primary official NBB WVV 9904"),
    ("bud_ibeg_div_2025", "2025", "3500000", "2025 dividend 3500000 DROP vs 5303780; tick1398; primary official NBB WVV 694"),
    ("bud_ibeg_div_2024", "2024", "5303780", "2024 dividend 5303780 comparative; tick1398; primary official NBB WVV 694"),
    ("bud_ibeg_rel_inc_2025", "2025", "458721", "2025 related-party FVA income 458721 vs 926009; tick1398; primary official NBB WVV 9421"),
    ("bud_ibeg_comm_2025", "2025", "8233", "2025 commissaris EY 8233 + extra 1671; tick1398; primary official NBB WVV 9505"),
    ("bud_ibeg_board_2025", "2025", "28314", "2025 bestuurders 28314; tick1398; primary official NBB WVV 9503"),
    ("bud_ibeg_taxprep_2025", "2025", "576007", "2025 geactiveerde VenB 576007; tick1398; primary official NBB WVV 9136"),
    ("bud_ibeg_latent_2025", "2025", "5068258", "2025 actieve latenties 5068258; tick1398; primary official NBB WVV 9141"),
    ("bud_ibeg_loanfac_2025", "2025", "30000000", "2025 Fluvius HV credit facility max 30000000; tick1398; primary official NBB WVV jaarverslag"),
]


def main() -> None:
    step = sys.argv[1] if len(sys.argv) > 1 else "all"

    if step in ("all", "sources"):
        n = append_rows(
            DATA / "sources.csv",
            [
                {
                    "source_id": SRC,
                    "title": "IGS IBEG jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00238388; AV 23.06.2026)",
                    "url": SRC_URL,
                    "publisher": "IGS IBEG / NBB WVV deposit",
                    "accessed_date": "2026-08-19",
                    "source_class": "budget",
                    "notes": (
                        "tick1398; official NBB VOL-inb PDF 1.93MB 40p deposit 2026-00238388 created 02.07.2026 header 30.06.2026; "
                        "leftover IGS energy holding Grimbergen+Machelen+Meise+Vilvoorde+Wemmel; "
                        "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                        "Belscope/Companyweb extracted tables not used; Staatsbladmonitor table euros not used; "
                        "commissaris EY B00160 / 0446.334.711 / Paul Eelen + Line Vyvey; fee 8233 + extra 1671; "
                        "VOL-inb 8 is 6:116 liquidity test only (no statutory audit oordeel); omzet 70 empty; 6.10 empty"
                    ),
                },
                {
                    "source_id": SRC2,
                    "title": "IGS IBEG official site (leftover energy holding IGS 5 HV municipalities)",
                    "url": SRC2_URL,
                    "publisher": "IGS IBEG",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1398; leftover IGS of 5 HV municipalities Grimbergen+Machelen+Meise+Vilvoorde+Wemmel; "
                        "site quote strategische participaties energiesector; statutory 2025 balans is the NBB CDN deposit"
                    ),
                },
                {
                    "source_id": SRC3,
                    "title": "KBO IGS IBEG 0202.082.078",
                    "url": SRC3_URL,
                    "publisher": "KBO Public Search FOD Economie",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1398; KBO 0202.082.078 Actief / normale toestand since 01.01.1968; "
                        "statutaire naam Intercommunale van Brabant voor Electriciteit en Gas since 01.04.2019; "
                        "afkorting I.B.E.G since 01.04.2019; Opdrachthoudende vereniging (Vlaams Gewest) since 01.04.2019; "
                        "zetel Grote Markt z/n 1800 Vilvoorde Stadhuis since 01.01.2019; 0 VE; "
                        "KBO no email/web/tel; official site https://ibeg.be/; kapitaal 619733.82; "
                        "jaarvergadering april; boekjaar 31 december; aanbestedende overheid since 01.01.1968; "
                        "absorbed 0202.082.177 + 0869.581.640 (01.04.2019); 15 bestuurders; KBO stand 18.08.2026"
                    ),
                },
                {
                    "source_id": SRC4,
                    "title": "IGS IBEG FOI channel / secretariaat (info@ibeg.be; Dewezplein 6 Vilvoorde)",
                    "url": SRC4_URL,
                    "publisher": "IGS IBEG",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1398; site contact via e-mail; secretariaat Laurent Benoit Dewezplein 6 1800 Vilvoorde; "
                        "info@ibeg.be; KBO zetel Grote Markt z/n Stadhuis; voorzitter Jean-Pierre De Groef; ondervoorzitter Katrien Vaes"
                    ),
                },
            ],
        )
        print("sources", n)

    if step in ("all", "entities"):
        n = append_rows(
            DATA / "entities.csv",
            [
                {
                    "entity_id": ENT,
                    "name_nl": "IGS IBEG (Intercommunale van Brabant voor Elektriciteit en Gas; leftover IGS energy holding HV)",
                    "name_fr": "IGS IBEG (intercommunale Brabant electricite et gaz; IGS residuel holding energie HV)",
                    "name_en": "IGS IBEG leftover IGS energy holding Halle-Vilvoorde 5 municipalities",
                    "level": "other",
                    "parent_id": "sec_flanders",
                    "community_language": "nl",
                    "website": "https://ibeg.be/",
                    "foi_email": FOI_EMAIL,
                    "foi_postal": FOI_POSTAL,
                    "notes": (
                        "tick1398 leftover residual IGS IBEG energy holding IGS; "
                        "KBO 0202.082.078 Actief since 01.01.1968; official NBB WVV VOL-inb PDF downloads; "
                        "sourced euros assets 100488193 omzet empty diensten 809703 debt 1450184 pnl 1283311 equity 99038008 div 3500000 fva 96372430; "
                        "FOI ready omzet empty / 3.50m dividend / 96.37m FVA / 9.00m Fluvius HV loan; "
                        "distinct from already-mined Fluvius Halle-Vilvoorde 1387 prefix flhv (IBEG is 21.48pct holding) and IGS IVEBICA 1397 / Pontes 1396 / Fluvius stack 1382-1391"
                    ),
                },
            ],
        )
        print("entities", n)

    if step in ("all", "budgets"):
        n = append_rows(
            DATA / "budgets.csv",
            [
                {
                    "budget_id": bid,
                    "entity_id": ENT,
                    "year": year,
                    "amount_eur": amt,
                    "amount_min_eur": "",
                    "amount_max_eur": "",
                    "basis": "executed",
                    "source_id": SRC,
                    "confidence": "strong",
                    "notes": notes,
                }
                for bid, year, amt, notes in BUDGETS
            ],
        )
        print("budgets", n)

    if step in ("all", "commitments"):
        n = append_rows(
            DATA / "commitments.csv",
            [
                {
                    "commitment_id": COMM,
                    "title": "IGS IBEG JR2025 leftover IGS dual (assets 100.49m / omzet empty / FVA 96.37m / dividend 3.50m / PnL +1.28m)",
                    "entity_id": ENT,
                    "beneficiary": "IGS IBEG / " + VENNOTEN,
                    "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
                    "decision_date": "2026-06-23",
                    "start_year": "1968",
                    "end_year": "",
                    "total_envelope_eur": "3500000",
                    "cash_by_year": "",
                    "remaining_eur": "",
                    "status": "active",
                    "evaluation_url": SRC_URL,
                    "stated_goal": "Local leftover IGS map VL energy holding HV 5 gemeenten — omzet unpublished / 3.50m dividend / 96.37m FVA / PnL +1.28m",
                    "cut_option": "Publish omzet + 809k diensten split + 3.50m dividend per vennoot + 96.37m FVA counterparts + 9.00m Fluvius HV loan terms + statutory audit oordeel; do not keep energy holding IGS as dual unpublished vehicle",
                    "source_id": SRC,
                    "confidence": "strong",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "notes": "tick1398; assets 100488193 omzet empty diensten 809703 debt 1450184 pnl 1283311 equity 99038008 div 3500000 fva 96372430; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius HV 1387 possible",
                }
            ],
        )
        print("commitments", n)

    if step in ("all", "leaderboard"):
        n = append_rows(
            DATA / "leaderboard.csv",
            [
                {
                    "item_id": LB,
                    "name": "IGS IBEG JR2025 leftover IGS: assets 100.49m / omzet empty / FVA 96.37m / dividend 3.50m / 0 VTE",
                    "level": "L5",
                    "type": "local_budget_line",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "annual_cost_eur": "3500000",
                    "total_cost_eur": "100488193",
                    "tco_notes": (
                        "Leftover dual IGS energy holding 5 HV municipalities (Grimbergen/Machelen/Meise/Vilvoorde/Wemmel): "
                        "assets 100.49m / equity 99.04m / pnl +1.28m / omzet unpublished / diensten 0.81m JUMP / "
                        "FVA 96.37m (Fluvius HV 64.83m 21.48pct + VENTUM 9.26m 92.55pct + Publigas/Publi-T 13.29m) / "
                        "loan to Fluvius HV 9.00m (facility 30m) / dividend 3.50m / debt 1.45m (no LT) / cash 1.84m / 0 VTE / "
                        "statutory audit oordeel unpublished (6:116 only); "
                        "official NBB WVV live; do not treat 100.49m as TE-additive of 348bn; double_count vs Fluvius HV 1387 possible"
                    ),
                    "confidence": "strong",
                    "source_id": SRC,
                    "beneficiaries": "IGS IBEG / " + VENNOTEN,
                    "stated_goal": "Local leftover IGS map VL energy holding HV 5 gemeenten — JR2025 live; dual omzet/dividend/FVA FOI",
                    "measured_outcome": "Official NBB WVV 2026-08-19: assets 100.49m / omzet empty / FVA 96.37m / dividend 3.50m / pnl +1.28m / 0 VTE",
                    "absurdity_score": "7.0",
                    "cost_score": "7.5",
                    "difficulty": "3.0",
                    "priority_index": "6.4",
                    "cut_proposal": "Publish omzet + 809k diensten split + 3.50m dividend per vennoot + 96.37m FVA counterparts + 9.00m Fluvius HV loan terms + statutory audit oordeel; do not keep energy holding IGS as dual unpublished vehicle",
                    "status": "active",
                    "struck_reason": "",
                    "notes": "tick1398; leftover IGS IBEG energy holding IGS; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius HV 1387 and IGS IVEBICA 1397 / Pontes 1396 / Fluvius stack 1382-1391",
                }
            ],
        )
        print("leaderboard", n)

    if step in ("all", "foi"):
        n = append_rows(
            DATA / "foi_queue.csv",
            [
                {
                    "gap_id": GAP,
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "entity_id": ENT,
                    "what_is_missing": (
                        "omzet WVV 70 empty + 6.10 category/geo empty + 74 empty "
                        "+ diensten 809703 JUMP vs 271411 (WVV 61; no split; I.B.E.G.-fonds / adviseur unpublished) "
                        "+ dividend 3500000 DROP vs 5303780 (694; bijlage 3 verdeelsleutel per vennoot unpublished) "
                        "+ FVA 96372430 (Fluvius HV 64830538 21.48pct / VENTUM 9255000 92.55pct / Publigas+Publi-T 13286892) Publi-T kapitaleverhoging 3672433 unpublished "
                        "+ krediet Fluvius HV 9000000 (facility 30000000; rente/looptijd unpublished) "
                        "+ niet-recurrent 519509 minderwaarde / investeringsreserve per gemeente unpublished "
                        "+ VOL-inb 8 statutory audit oordeel missing (only 6:116 liquidity) + 0 VTE"
                    ),
                    "why_it_matters": (
                        "Leftover IGS energy holding of 5 mined Halle-Vilvoorde municipalities Grimbergen/Machelen/Meise/Vilvoorde/Wemmel "
                        "(distinct from Fluvius Halle-Vilvoorde 1387 DSO and from IGS IVEBICA 1397 / Pontes 1396 / Fluvius 1382-1391): "
                        "100.49m assets / omzet unpublished / 96.37m FVA / 3.50m dividend / 9.00m Fluvius HV loan / 0 VTE / "
                        "holding shell hides omzet and per-vennoot dividend "
                        "is a dual opacity residual, not TE-additive of 348bn."
                    ),
                    "priority": "8",
                    "recipient_body": "IGS IBEG / Raad van Bestuur / Jean-Pierre De Groef / Katrien Vaes / 5 HV vennoten",
                    "recipient_email": FOI_EMAIL,
                    "recipient_postal": FOI_POSTAL,
                    "draft_letter_path": DRAFT,
                    "status": "ready",
                    "date_ready": "2026-08-19",
                    "date_sent": "",
                    "date_due": "",
                    "date_answered": "",
                    "response_summary": "",
                    "linked_commitment_id": COMM,
                    "linked_leaderboard_id": LB,
                    "created_utc": UTC,
                    "updated_utc": UTC,
                    "notes": (
                        "tick1398 leftover IGS energy holding 5 HV gemeenten after honest hunt; "
                        "live JR2025 official NBB WVV VOL-inb PDF now extracted (1.93MB 40p deposit 2026-00238388). "
                        "Leftover AGB first: Duffel/Zoersel/Diepenbeek/Dendermonde/Grimbergen/Tienen/Menen/Herk/sogent already mined — skipped; Zwevegem extract-only — skipped. "
                        "IGS IVEBICA already mined 1397 — skipped. IGS Pontes already mined 1396 — skipped. Fluvius stack already mined 1382-1391 — skipped. "
                        "IVAREM still 2024 — skipped. IGL last JR2024 — skipped. "
                        "Dommelhof leftover next if a JR2025 PDF now downloads. "
                        "Otary RS Nuhma-adjacent fallback not taken. "
                        "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                    ),
                }
            ],
        )
        print("foi", n)

    if step in ("all", "rq"):
        rq_new = {
            "task_id": "rq_1398",
            "title": "IGS IBEG JR2025 leftover dual residual",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "done",
            "hierarchy_target": "L5",
            "entity_id": ENT,
            "instructions": (
                "Completed: IGS IBEG leftover IGS energy holding of Grimbergen+Machelen+Meise+Vilvoorde+Wemmel after honest hunt; "
                "KBO 0202.082.078 Actief; live JR2025 official NBB WVV VOL-inb PDF (1.93MB 40p deposit 2026-00238388; commissaris EY 6:116 only); "
                "sourced euros assets 100488193 / omzet empty / diensten 809703 / debt 1450184 / pnl 1283311 / dividend 3500000 / fva 96372430; "
                "FOI ready omzet empty / 3.50m dividend / 96.37m FVA / 9.00m Fluvius HV loan"
            ),
            "blocked_gap_id": GAP,
            "created_utc": "2026-08-19T05:15:00Z",
            "updated_utc": UTC,
            "notes": (
                "tick1398 IGS IBEG leftover IGS energy holding residual; KBO 0202.082.078; "
                "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1399 residual dual L5 VL"
            ),
        }
        rq_spawn = {
            "task_id": "rq_1399",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
                "(prior 1255-1398 done including IGS IBEG 1398 leftover energy holding IGS live NBB WVV / "
                "IGS IVEBICA 1397 leftover library/culture/academy IGS live NBB WVV / "
                "IGS Pontes 1396 leftover crematorium IGS live NBB WVV / "
                "IGS Hofheide 1395 leftover crematorium IGS live NBB WVV / "
                "IGS Westlede 1394 leftover crematorium IGS live NBB WVV / "
                "HAVICREM 1393 leftover crematorium IGS live NBB WVV / "
                "IVLA 1392 leftover waste IGS live NBB WVV); "
                "leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; "
                "other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; "
                "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
                "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
                "skip already-mined IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / ILvA 1344; "
                "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
                "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick1398 after IGS IBEG leftover energy holding IGS live NBB WVV; next residual dual L5 VL",
        }
        found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1398", rq_new, rq_spawn)
        print("research_queue 1398", found, "spawned_1399", spawned)

    if step in ("all", "state"):
        with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(
                f,
                fieldnames=[
                    "state_id",
                    "mode",
                    "current_sprint",
                    "last_tick_utc",
                    "last_unit_id",
                    "ticks_completed",
                    "paused",
                    "notes",
                ],
                lineterminator="\r\n",
            )
            w.writeheader()
            w.writerow(
                {
                    "state_id": "main",
                    "mode": "continuous",
                    "current_sprint": "hole_fill",
                    "last_tick_utc": UTC,
                    "last_unit_id": "rq_1398",
                    "ticks_completed": "1398",
                    "paused": "no",
                    "notes": (
                        "tick1398 IGS IBEG leftover IGS energy holding residual; KBO 0202.082.078; "
                        "live JR2025 NBB WVV PDF; sourced euros assets 100488193 omzet empty diensten 809703 debt 1450184 pnl 1283311 equity 99038008 div 3500000 fva 96372430; "
                        "FOI ready omzet-empty/3.50m dividend/96.37m FVA/9.00m Fluvius HV loan; next rq_1399 residual dual L5 VL; continuous hole_fill"
                    ),
                }
            )
        print("loop_state ok")

    if step in ("all", "log"):
        log = ROOT / "loop_log.md"
        entry = (
            "### Tick 1398 - 2026-08-19 - rq_1398 IGS IBEG dual residual leftover\n"
            "- Unit: IGS IBEG / Intercommunale van Brabant voor Elektriciteit en Gas (leftover IGS opdrachthoudende vereniging / energy holding of 5 mined Halle-Vilvoorde municipalities Grimbergen + Machelen + Meise + Vilvoorde + Wemmel; 0 VE) after residual dual hunt (KBO **0202.082.078**; official ibeg.be has 5 gemeenten + contact; live NBB WVV VOL-inb deposit **2026-00238388** PDF 1.93MB / 40p; AV **23.06.2026**; created **02.07.2026**; header **30.06.2026**; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / Paul Eelen A02213 + Line Vyvey A02501 fee 8.233 + extra 1.671; VOL-inb 8 is 6:116 liquiditeitstest only for the 3.50m dividend — no statutory audit oordeel filed). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; leftover AGB first: Duffel/Zoersel/Diepenbeek/Dendermonde/Grimbergen/Tienen/Menen/Herk/sogent/Oostkamp/Haacht/Vilvoorde/Herzele/Wingene/Ternat already mined, Zwevegem extract-only, leftover Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403, Halle/Dilbeek/Waregem/Eeklo no live JR2025 this hunt — then leftover IBEG with live CDN this tick). Distinct from already-mined Fluvius Halle-Vilvoorde 1387 (prefix `flhv`; IBEG is a 21,48% vennoot/holding, not the DSO) and from IGS IVEBICA 1397 (prefix `ivbc`) and IGS Pontes 1396 (prefix `pnts`) and from Fluvius stack 1382-1391. First confirmed not already mined: no IBEG / 0202.082.078 JR2025 extract in entities/sources/leaderboard (only leftover-vennoot mentions in Fluvius HV 1387). KBO Actief / normale toestand since **01.01.1968**; statutaire naam Intercommunale van Brabant voor Electriciteit en Gas since 01.04.2019; afkorting I.B.E.G since 01.04.2019; Opdrachthoudende vereniging (Vlaams Gewest) since 01.04.2019; zetel Grote Markt z/n 1800 Vilvoorde Stadhuis since 01.01.2019; **0 VE**; KBO no email/web/tel; official site https://ibeg.be/; kapitaal 619.733,82; jaarvergadering april; boekjaar 31 december; aanbestedende overheid since 01.01.1968. Absorbed Intercommunale van Brabant voor Gas 0202.082.177 + IBE 0869.581.640 (01.04.2019). Voorzitter Jean-Pierre De Groef since 12.03.2019; ondervoorzitter Katrien Vaes since 18.03.2025. Contact info@ibeg.be; secretariaat Laurent Benoit Dewezplein 6 1800 Vilvoorde. Hunt leftover AGB first: already mined / extract-only / 404 — skipped. Leftover IGS IBEG statutory CDN live this tick (HTTP 200 / 1929115 / 40p) — taken. IGS IVEBICA already mined 1397 — skipped. IGS Pontes already mined 1396 — skipped. Fluvius stack already mined 1382-1391 — skipped. IVAREM still JR2024 — skipped. IGL last JR2024 — skipped. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live IBEG extracted. Otary RS Nuhma-adjacent fallback not taken. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used. Not every-10 (next 1400).\n"
            "- EUR strong (primary official WVV VOL-inb; **omzet 70 empty**; 74 empty; 6.10 category/geo empty; pers 62/9087 empty / 0 VTE; VOL-inb 6.1/6.2/6.3/6.8/6.9/6.14/6.17/6.18/6.20/9-15 not filed; 6:116 only): assets **100.488.193** (was 103.058.477); fixed **96.372.430** all FVA (MVA/IVA empty); FVA deelnemingen **74.085.538** (Fluvius Halle-Vilvoorde 21,48% valued **64.830.538** + VENTUM&green 92,55% valued **9.255.000**); verbonden vorderingen **9.000.000** (krediet Fluvius HV; facility **30.000.000**); andere aandelen **13.286.892** (Publigas 423 + Publi-T 20.117); current **4.115.762**; ST recv **576.007** (tax prepaid); geldbeleggingen **1.697.144 DROP** vs 3.330.349; cash **1.842.610**; equity **99.038.008** (inbreng 94.803.958 / 764.918 aandelen; reserves 3.159.688; overgedragen 1.074.362); voorzieningen empty; schulden **1.450.184** (no LT; leveranciers **450.184** + overige **1.000.000**); omzet 70 empty; diensten **809.703 JUMP** vs 271.411; pers empty; niet-recurrent 66A **519.509**; expl **−1.336.225** vs −874.818; fin opbr **2.640.731** (FVA 2.318.574 DBI); fin kosten 21.195; tax 0; PnL **+1.283.311** vs +2.627.327; dividend **3.500.000** DROP vs 5.303.780; commissaris 8.233; bestuurders 28.314. Vennoten: Grimbergen + Machelen + Meise + Vilvoorde + Wemmel (ibeg.be).\n"
            "- CSVs: sources+4/entities+1/budgets+46/commitments+1/leaderboard+1 + FOI ready `gap_ibeg_omzet_empty_div_3_50m_fva_96_37m_l5` (not sent); rq_1398=done; spawn rq_1399; ticks=1398.\n"
            "- Coverage: residual dual L5 (IGS IBEG leftover energy holding IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs Fluvius Halle-Vilvoorde 1387 possible. No progress refresh (not every-10; next 1400).\n"
            "- Next: rq_1399 residual dual L5 VL JR2025 hole_fill (prefer leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / ILvA 1344 / Haviland 1370).\n"
        )
        with log.open("a", encoding="utf-8") as f:
            f.write(entry)
        print("loop_log ok")
    print("tick1398 write", step, "done")


if __name__ == "__main__":
    main()
