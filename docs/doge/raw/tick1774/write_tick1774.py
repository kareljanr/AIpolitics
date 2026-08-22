import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1774'; utc='2026-08-24T18:15:00Z'
eid='nv_centenaire'; sid='src_centenaire_jr2025_nbb'
gap='gap_centenaire_marge_2_62m_nrec_fin_1_18m_dividend_1_42m_l5'
lb='lb_centenaire_marge_2_62m_nrec_fin_1_18m_dividend_1_42m_l5'
comm='comm_centenaire_jr2025_marge_2_62m'
hier='Wallonie>Provinces>Hainaut>Communes>Chatelet>MRPA>LeCentenaire>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,'LE CENTENAIRE SA NBB A-cap YE2025 deposit 2026-00136834','http://cdn.staatsbladmonitor.be/2026pdf/2026-00136834.pdf','Nationale Bank van België / LE CENTENAIRE SA','2026-08-24','primary_official','tick1774; AV 07.05.2026; A-cap abbrev; Vivalto Home Belgium admin; opinion sans reserve; Chatelet Rue Gendebien 186; nrec fin 1.18m; dividend 1.42m; related recv 3.20m'])
    w.writerow(['src_centenaire_site','Vivalto Home — Le Centenaire maisons','https://www.vivaltohome.com/maisons/le-centenaire/','Vivalto Home','2026-08-24','primary_official','tick1774; Rue Gendebien 186 6200 Chatelet; centenaire@vivaltohome.com'])
    w.writerow(['src_centenaire_kbo','KBO LE CENTENAIRE SA 0426.101.796','https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0426101796','KBO','2026-08-24','primary_official','tick1774; SA/NV; Rue Gendebien 186 6200 Chatelet; RPR Charleroi'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,'Le Centenaire NV (leftover Vivalto WZC dual / Châtelet)','LE CENTENAIRE SA (WZC Vivalto résiduel / Châtelet)','LE CENTENAIRE SA leftover Vivalto nursing-home dual Chatelet','other','nv_vivalto_home_be','fr','https://www.vivaltohome.com/maisons/le-centenaire/','centenaire@vivaltohome.com','Rue Gendebien 186 6200 Châtelet','tick1774 leftover Vivalto WZC dual after Seniorie Braine; KBO 0426.101.796 Actief; SA; official NBB A-cap YE2025 deposit 2026-00136834 CDN 200; AV 07.05.2026; mère Vivalto Home Belgium; opinion sans réserve; nrec fin 1183905; dividend apport 1418042; related recv controllers 3201947; autres dettes ST 1534082 (=distribuer); sourced euros assets 5615640 equity 1263600 debt 4038898 FVA 1800000 leasing LT 1683983 marge 2624466 staff 2200823 VTE 37.3 expl 181524 pnl 1277118; FOI ready RIZIV/nrec fin/related recv/dividend'])

buds=[
 ('bud_centenaire_assets_2025',5615640,'stock','Assets YE2025 5615640; tick1774'),
 ('bud_centenaire_equity_2025',1263600,'stock','Equity 1263600 DROP vs 1520563; tick1774'),
 ('bud_centenaire_debt_2025',4038898,'stock','Debt 4038898; tick1774'),
 ('bud_centenaire_leasing_lt_2025',1683983,'stock','LT credit/leasing 1683983; tick1774'),
 ('bud_centenaire_fva_2025',1800000,'stock','Immobilisations financieres 1800000 DROP vs 3199340; tick1774'),
 ('bud_centenaire_autres_creances_2025',1532393,'stock','Autres creances ST 1532393 JUMP vs 144166; tick1774'),
 ('bud_centenaire_related_recv_2025',3201947,'stock','Creances sur administrateurs/controleurs 9500=3201947; tick1774'),
 ('bud_centenaire_marge_2025',2624466,'realized','Marge bruto 2624466 (A-cap; CA undisclosed); tick1774'),
 ('bud_centenaire_staff_2025',2200823,'realized','Staff 2200823 / VTE 37.3; tick1774'),
 ('bud_centenaire_expl_2025',181524,'realized','Benefice exploitation 181524; tick1774'),
 ('bud_centenaire_nrec_fin_2025',1183905,'realized','Produits financiers non recurrents 1183905 drives PnL; tick1774'),
 ('bud_centenaire_pnl_2025',1277118,'realized','PnL 1277118; dividend apport 1418042 + admin 116039; autres dettes ST=distribuer 1534082; tick1774'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,'LE CENTENAIRE SA JR2025 leftover Vivalto dual (marge 2.62m / nrec fin 1.18m / dividend 1.42m)',eid,'LE CENTENAIRE SA / Vivalto Home Belgium / residents Chatelet','CSA SA; decret wallon openbaarheid analog for dual care euros','2026-05-07',2025,2025,2624466,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00136834.pdf','Local leftover Vivalto WZC map WAL Chatelet — marge 2.62m / nrec fin + dividend extraction twin Braine/Meridienne','Publish CA/RIZIV split + nrec fin nature + related recv 3.20m + dividend 1.42m rationale; unit-cost',sid,'strong',hier,'tick1774; assets 5.62m equity 1.26m debt 4.04m FVA 1.80m leasing LT 1.68m marge 2.62m staff 2.20m VTE 37.3 expl 0.18m nrec fin 1.18m pnl 1.28m dividend 1.42m related recv 3.20m; FOI ready not sent; not TE-additive; A-cap CA undisclosed'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,'LE CENTENAIRE SA 2025: marge 2.62m / staff 2.20m (nrec fin 1.18m + dividend 1.42m + related recv 3.20m)','L5','nursing_home_private_dual',hier.replace('>JR2025_L5',''),2624466,3201947,'Envelope=marge 2624466 (A-cap; CA undisclosed); staff 2.20m VTE 37.3; nrec fin 1.18m drives PnL 1.28m; dividend apport 1.42m; related recv controllers 3.20m; FVA DROP 1.80m; autres dettes ST=distribuer 1.53m','strong',sid,'MRPA/WZC residents Chatelet / Vivalto group','Nursing-home care (MRPA/MRS)','Same Vivalto extraction pattern as Meridienne/Braine: nrec fin + large controller receivables + dividend while equity DROPs',6.2,5.5,5,6.4,'Publish CA/RIZIV; disclose nrec fin + related recv/dividend map; unit-cost','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB A-cap YE2025 live marge 2624466 but CA undisclosed; nrec fin 1183905 nature; related recv controllers 3201947; dividend apport 1418042 (autres dettes ST 1534082=distribuer); FVA DROP 1800000 vs 3199340; autres creances JUMP 1532393; leasing LT 1683983 + option achat 93000; admin 116039; equity DROP','Vivalto Chatelet WZC with abbreviated schema + nrec-fin-driven PnL + dividend extraction twin Braine/Meridienne — opacity on public RIZIV share and group cash extraction',8,'LE CENTENAIRE SA / Vivalto Home Belgium SA','centenaire@vivaltohome.com','Rue Gendebien 186 6200 Châtelet',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1774; human-send only; Brembloem still no JR2025; AGB Bornem JR2024; CDN live ClosRoses/Etrier/VertBocage/Tonnelle/AgeDor; NOT Braine/Meridienne continuum'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1774':
        row['status']='done'
        row['title']='LE CENTENAIRE SA JR2025 leftover Vivalto dual residual'
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=('Completed: LE CENTENAIRE SA leftover Vivalto WZC dual Chatelet after Seniorie Braine; '
            'KBO 0426.101.796 Actief; live JR2025 official NBB A-cap PDF (206493 bytes 28p deposit 2026-00136834; AV 07.05.2026; '
            'Vivalto Home Belgium; opinion sans réserve); '
            'sourced euros assets 5615640 equity 1263600 debt 4038898 marge 2624466 staff 2200823 VTE 37.3 '
            'nrec fin 1183905 pnl 1277118 dividend 1418042 related recv 3201947; FOI ready not sent; NOT Braine continuum')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']='tick1774 LE CENTENAIRE leftover Vivalto residual; KBO 0426.101.796; live JR2025 NBB A-cap PDF; sourced euros; FOI ready not sent; next rq_1775 residual dual L5'
        print('updated rq_1774'); break
else:
    raise SystemExit('missing')
if not any(r.get('task_id')=='rq_1775' for r in rows):
    rows.append({
        'task_id':'rq_1775','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':('Tick 1775 after 1774 LE CENTENAIRE. Next every-10 is 1780. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), '
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200 '
                 '(LE CLOS DES ROSES 2026-00176179 / L ETRIER D ARGENT 2026-00176181 / AU VERT BOCAGE 2026-00176184 / '
                 'LA TONNELLE 2026-00176186 / L AGE D OR 2026-00176187 live), '
                 'other IOED/HVZ/IGS. Do NOT redo Centenaire/Braine/Meridienne continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':'spawned after tick1774 LE CENTENAIRE; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/ClosRoses/Etrier/VertBocage/Tonnelle/AgeDor; next every-10 1780'
    })
    print('spawned rq_1775')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
print('OK')
