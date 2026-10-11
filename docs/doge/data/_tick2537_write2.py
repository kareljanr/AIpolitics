from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2537_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_leefbaar_wonen_oostkamp"
GAP = "gap_trad_oostkamp_maatwerk_ye2025_nbb_pdf_403_l5"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_rows(path, rows, fieldnames):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} no LF")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="raise", lineterminator="\n")
        for row in rows:
            w.writerow(row)
    print("appended", len(rows), "->", path.name)

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Oostkamp>Leefbaar Wonen-Kringloopcentrum>leftover_maatwerk",
    "entity_id": EID,
    "what_is_missing": "Official NBB YE2025 statutory native PDF + deposit-id (NBB published-deposits 403 this tick; SBM IP-blacklist; no CDN/broker without deposit-id) and WSE/maatwerk / gemeente Oostkamp subsidy matrix behind that filing",
    "why_it_matters": "Leftover public maatwerk VZW of mined leftover-mined AGB-only city_oostkamp after leftover WZC Ter Luchte@2536; official KBO zetel Oostkamp 12 VE; unused leftover type; YE2025 native euros not extracted this tick (NBB 403); no invented euros; FOI-ready last resort",
    "priority": "8",
    "recipient_body": "VZW Leefbaar Wonen-Kringloopcentrum / Voorzitter Raad van Bestuur",
    "recipient_email": "info@trad.be",
    "recipient_postal": "Terluchtestraat 38 8020 Oostkamp",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": DAY,
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "",
    "linked_leaderboard_id": "",
    "created_utc": STAMP,
    "updated_utc": STAMP,
    "notes": "tick2537; ready NOT sent; FOI-ready last resort after NBB published-deposits 403 + SBM IP-blacklist + no deposit-id; leftover mined city_oostkamp leftover maatwerk leftover-mined AGB-only unused leftover type; leftover city_oostkamp leftover WZC taken leftover WZC Sint-Jozef Groep Zorg H. Familie remine@2057 leftover-via-VE leftover CIK HARD SKIP leftover WZC type now taken leftover city_oud_heverlee leftover WZC De Kouter 0848.738.221 Korian PPS SKIP + NBB 403 leftover city_vleteren leftover WZC Benaja YE2024 SKIP leftover city_machelen leftover WZC Woluwedal commercial SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC Den Olm same KBO leftover WZC unused-not-hardskip of leftover-mined AGB-only cities 0 leftover CIK HARD SKIP leftover KBO-activity HARD SKIP; 12 VE; next rq_2538 leftover dual (NOT every-10; next every-10 2540); off leftover-via-VE of a DIFFERENT leftover city; off Armonea; off Korian; off Vulpia; FIRST LOCK leftover city_oostkamp leftover maatwerk",
}], foi_fields)
print("foi ok")
print("CORE1B DONE")
