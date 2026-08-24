# tick 2330 — EVERY-10 + Den Brand Mol YE2025 Medium
import csv
import re
from pathlib import Path

csv.field_size_limit(100 * 1024 * 1024)
UTC = "2026-08-28T01:15:00Z"
RAW = Path("docs/doge/data/raw/tick2330")
RAW.mkdir(parents=True, exist_ok=True)

OMZET = 1270740
BRUTO = 7222348
PNL = 226679
EQUITY = 5729856
FTE = 89.4
RATIO = round(BRUTO / OMZET, 2)  # 5.68


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def has_id(path, key, val):
    with open(path, encoding="utf-8", newline="") as f:
        return any(row.get(key) == val for row in csv.DictReader(f))


# --- sources ---
if not has_id("docs/doge/data/sources.csv", "source_id", "src_den_brand_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        (
            "src_den_brand_jr2025_cw_nl",
            "Companyweb NL Den Brand YE2025 statutory",
            "https://www.companyweb.be/nl/0422073526/den-brand",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick2330; YE2025 omzet {OMZET} bruto {BRUTO} ~{RATIO}x pnl DROP {PNL} equity JUMP {EQUITY} FTE {FTE}",
        ),
        (
            "src_den_brand_jr2025_cw_en",
            "Companyweb EN Den Brand YE2025 statutory",
            "https://www.companyweb.be/en/0422073526/den-brand",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick2330; EN Medium; filed 25-06-2026; Turnover {OMZET} Gross {BRUTO} P/L {PNL} Equity {EQUITY} FTE {FTE}",
        ),
        (
            "src_den_brand_jr2025_cw_fr",
            "Companyweb FR Den Brand YE2025 statutory",
            "https://www.companyweb.be/fr/0422073526/den-brand",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2330; FR mirror",
        ),
        (
            "src_den_brand_kbo_2330",
            "KBO Den Brand 0422.073.526",
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0422073526",
            "KBO FOD Economie",
            "official_register",
            "tick2330; Actief VZW 18 VE Mol RSZ 87.202; info@denbrand.be; T +3214347040",
        ),
        (
            "src_den_brand_site_contact_2330",
            "Den Brand FOI info@denbrand.be",
            "https://www.denbrand.be/",
            "Den Brand VZW",
            "foi_contact",
            "tick2330; info@denbrand.be; Spoorwegstraat 27 Mol; VAPH woon/dag Mol-Herentals-Lier",
        ),
    ]:
        append_csv(
            "docs/doge/data/sources.csv",
            dict(
                source_id=sid,
                title=title,
                url=url,
                publisher=pub,
                accessed_date="2026-08-28",
                source_class=klass,
                notes=notes,
            ),
        )

# --- entity ---
if not has_id("docs/doge/data/entities.csv", "entity_id", "vzw_den_brand_mol"):
    append_csv(
        "docs/doge/data/entities.csv",
        dict(
            entity_id="vzw_den_brand_mol",
            name_nl="Den Brand VZW (Mol / VAPH woonondersteuning)",
            name_fr="Den Brand ASBL (Mol / hébergement VAPH)",
            name_en="Den Brand VZW (Mol / VAPH residential care)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.denbrand.be/",
            foi_email="info@denbrand.be",
            foi_postal="Spoorwegstraat 27, 2400 Mol",
            notes=(
                f"tick2330 YE2025 Medium CW + Strong KBO 0422.073.526 Actief 18 VE RSZ 87.202; "
                f"omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL}; equity JUMP {EQUITY}; "
                f"FTE JUMP {FTE}; FOI gap_den_brand_*; EVERY-10@2330; after Tandem@2329; not TE-additive"
            ),
        ),
    )

# --- budgets ---
if not has_id("docs/doge/data/budgets.csv", "budget_id", "bud_den_brand_omzet_jr2025_statutory"):
    for bid, amt, basis, notes in [
        ("bud_den_brand_omzet_jr2025_statutory", OMZET, "CW statutory omzet YE2025 JUMP", "tick2330; Medium CW; omzet +4.91% vs 1211312"),
        ("bud_den_brand_bruto_jr2025_statutory", BRUTO, f"CW statutory bruto_marge YE2025 ~{RATIO}x omzet", "tick2330; Medium CW; bruto +5.05% vs 6874877"),
        ("bud_den_brand_pnl_jr2025_statutory", PNL, "CW statutory winst/verlies YE2025 DROP", "tick2330; Medium CW; pnl -22.95% vs 294196"),
        ("bud_den_brand_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen YE2025 JUMP", "tick2330; Medium CW; equity +3.01% vs 5562533"),
        ("bud_den_brand_fte_jr2025_statutory", FTE, "CW social-balance FTE 89.4 JUMP", "tick2330; Medium CW; FTE 89.4 vs 84.9"),
    ]:
        append_csv(
            "docs/doge/data/budgets.csv",
            dict(
                budget_id=bid,
                entity_id="vzw_den_brand_mol",
                year="2025",
                amount_eur=str(amt),
                amount_min_eur=str(amt),
                amount_max_eur=str(amt),
                basis=basis,
                source_id="src_den_brand_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            ),
        )

# --- commitment ---
if not has_id(
    "docs/doge/data/commitments.csv",
    "commitment_id",
    "comm_den_brand_jr2025_statutory_vaph_bruto_7_22m_5_68x",
):
    append_csv(
        "docs/doge/data/commitments.csv",
        dict(
            commitment_id="comm_den_brand_jr2025_statutory_vaph_bruto_7_22m_5_68x",
            title=f"Den Brand YE2025 leftover dual (omzet 1.27m / bruto 7.22m ~{RATIO}x / pnl DROP / FTE JUMP / Medium)",
            entity_id="vzw_den_brand_mol",
            beneficiary="volwassenen mentale handicap Mol-Herentals-Lier / VAPH",
            legal_basis="VZW Den Brand (KBO 0422.073.526; Actief; 18 VE; RSZ 87.202; VAPH woon/dag)",
            decision_date="2026-06-25",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(BRUTO),
            cash_by_year=(
                f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                f'"2025_equity":{EQUITY},"2025_fte":{FTE},'
                f'"2024_omzet":1211312,"2024_bruto":6874877,"2024_pnl":294196,'
                f'"2024_equity":5562533,"2024_fte":84.9}}'
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0422073526/den-brand",
            stated_goal="VAPH residential and day support mental disability Mol belt",
            cut_option="Publish NBB PDF assets/debt; reconcile bruto÷omzet ~5.68x + VAPH/PVF matrix",
            source_id="src_den_brand_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Mol>Den_Brand>JR2025_statutory_L5",
            notes=f"tick2330 EVERY-10; Medium CW; bruto primary {BRUTO} (~{RATIO}x); after Tandem@2329",
        ),
    )

# --- leaderboard ---
# pi = 0.55*3.5 + 0.35*6.5 + 0.10*(10-3) = 4.9
if not has_id(
    "docs/doge/data/leaderboard.csv",
    "item_id",
    "lb_den_brand_bruto_7_22m_omzet_1_27m_5_68x_pnl_drop_jr2025",
):
    append_csv(
        "docs/doge/data/leaderboard.csv",
        dict(
            item_id="lb_den_brand_bruto_7_22m_omzet_1_27m_5_68x_pnl_drop_jr2025",
            name=f"Den Brand bruto 7.22m / omzet 1.27m ~{RATIO}x / pnl DROP (YE2025)",
            level="L5",
            type="vaph_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Mol>Den_Brand>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes=(
                f"CW omzet JUMP {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x) / pnl DROP {PNL} / "
                f"equity JUMP {EQUITY} / FTE JUMP {FTE} / filed 25.06.2026"
            ),
            confidence="medium",
            source_id="src_den_brand_jr2025_cw_en",
            beneficiaries="VAPH adults Mol-Herentals-Lier",
            stated_goal="VAPH woon- & dagondersteuning",
            measured_outcome=f"bruto÷omzet ~{RATIO}x; pnl DROP -23%; FTE JUMP {FTE}",
            absurdity_score="6.5",
            cost_score="3.5",
            difficulty="3.0",
            priority_index="4.9",
            cut_proposal="Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~5.68x vs VAPH/PVF",
            status="open",
            struck_reason="",
            notes=(
                "tick2330 EVERY-10; Medium CW; FOI gap_den_brand_nbb_pdf_assets_debt_"
                f"bruto_gt_omzet_{RATIO:.2f}x_pnl_drop_fte_jump_vaph_matrix_l5; after Tandem@2329"
            ),
        ),
    )

GAP = "gap_den_brand_nbb_pdf_assets_debt_bruto_gt_omzet_5_68x_pnl_drop_fte_jump_vaph_matrix_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"

# --- foi ---
if not has_id("docs/doge/data/foi_queue.csv", "gap_id", GAP):
    append_csv(
        "docs/doge/data/foi_queue.csv",
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>Antwerpen>Mol>Den_Brand>NBB_PDF_assets_debt_bruto_gt_omzet",
            entity_id="vzw_den_brand_mol",
            what_is_missing=(
                f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} "
                f"(~{RATIO}x); pnl DROP EUR{PNL} despite omzet/bruto JUMP — VAPH/PVF matrix"
            ),
            why_it_matters=(
                f"Medium CW shows VAPH care VZW Mol (bruto 7.22m / omzet 1.27m ~{RATIO}x / pnl DROP / "
                f"FTE JUMP {FTE}) under public care path; assets/debt unpublished"
            ),
            priority="8",
            recipient_body="Den Brand VZW",
            recipient_email="info@denbrand.be",
            recipient_postal="Spoorwegstraat 27, 2400 Mol",
            draft_letter_path=DRAFT,
            status="ready",
            date_ready="2026-08-28",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_den_brand_jr2025_statutory_vaph_bruto_7_22m_5_68x",
            linked_leaderboard_id="lb_den_brand_bruto_7_22m_omzet_1_27m_5_68x_pnl_drop_jr2025",
            created_utc=UTC,
            updated_utc=UTC,
            notes="tick2330 EVERY-10; ready NOT sent; Medium CW + Strong KBO; after Tandem@2329",
        ),
    )

# --- research_queue line patch (avoid full CSV rewrite of corrupted large fields) ---
rq_path = Path("docs/doge/data/research_queue.csv")
data = rq_path.read_bytes()
# close rq_2330
pat = re.compile(rb"(rq_2330,[^\n]*)")
m = pat.search(data)
if not m:
    raise SystemExit("rq_2330 not found")
old = m.group(1)
# if already done with den brand, skip rewrite of this line
if b"Den Brand" in old and b",done," in old:
    print("rq_2330 already Den Brand done")
else:
    new = (
        f"rq_2330,EVERY-10 + leftover dual — Den Brand YE2025 Medium (bruto JUMP 7.22m / ~{RATIO}x omzet / "
        f"pnl DROP / FTE JUMP 89.4),hole_fill,10,done,L5,vzw_den_brand_mol,"
        f"EVERY-10@2330 + Den Brand after Tandem@2329. Prefer AGB/FARO YE2025 else unused. "
        f"Do NOT redo Tandem/Mivalti/Pleegzorg/Het Eepos/Zonnebeke stack.,{GAP},"
        f"2026-08-28T00:40:00Z,{UTC},"
        f"tick2330 EVERY-10 + Den Brand 0422.073.526 YE2025 Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO} "
        f"~{RATIO}x; pnl DROP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; 18 VE RSZ 87.202); "
        f"FOI {GAP} ready not sent; next rq_2331; next EVERY-10 2340"
    ).encode("utf-8")
    data = data[: m.start(1)] + new + data[m.end(1) :]

# spawn rq_2331 if missing
if b"rq_2331," not in data:
    spawn = (
        "\nrq_2331,leftover dual after Den Brand — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk,"
        "hole_fill,8,open,L5,,After Den Brand YE2025 Medium EVERY-10@2330. Prefer AGB Bornem/FARO/AIESH/REW/Citeco "
        "if YE2025 else FREE (Gandae/Aralea/Manupal/Vlotter/Aurelia if YE2025). Do NOT redo Den Brand/Tandem/"
        "Mivalti/Pleegzorg/Het Eepos/Zonnebeke stack.,,"
        f"{UTC},{UTC},spawned after tick2330 Den Brand EVERY-10; next EVERY-10 2340\n"
    ).encode("utf-8")
    if not data.endswith(b"\n"):
        data += b"\n"
    data += spawn

rq_path.write_bytes(data)

# --- loop_state ---
Path("docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},rq_2330,2330,no,"
    f"tick2330 EVERY-10 + leftover dual Den Brand 0422.073.526 Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO} "
    f"~{RATIO}x; pnl DROP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; 18 VE Mol VAPH); "
    f"after Tandem@2329; AGB/FARO YE2024; next rq_2331; next EVERY-10 2340\n",
    encoding="utf-8",
    newline="\n",
)

# raw summary
(RAW / "cw_summary.json").write_text(
    "{\n"
    '  "kbo": "0422.073.526",\n'
    '  "entity": "vzw_den_brand_mol",\n'
    f'  "omzet": {OMZET},\n'
    f'  "bruto": {BRUTO},\n'
    f'  "ratio": {RATIO},\n'
    f'  "pnl": {PNL},\n'
    f'  "equity": {EQUITY},\n'
    f'  "fte": {FTE},\n'
    '  "filed": "2026-06-25",\n'
    '  "confidence": "medium",\n'
    '  "every10": true\n'
    "}\n",
    encoding="utf-8",
)

print("OK tick2330 Den Brand + state")
print("ratio", RATIO, "pi", 4.9)
