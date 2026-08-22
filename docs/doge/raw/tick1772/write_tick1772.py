import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1772'; utc='2026-08-24T17:45:00Z'
eid='nv_meridienne'; sid='src_meridienne_jr2025_nbb'
gap='gap_meridienne_marge_4_00m_nrec_fin_1_88m_related_recv_6_16m_l5'
lb='lb_meridienne_marge_4_00m_nrec_fin_1_88m_dividend_2_00m_l5'
comm='comm_meridienne_jr2025_marge_4_00m'
hier='Wallonie>Provinces>Namur>Communes>LaBruyere>SaintDenisBovesse>MRPA>LaMeridienne>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,'LA MERIDIENNE SA NBB A-cap YE2025 deposit 2026-00136832','http://cdn.staatsbladmonitor.be/2026pdf/2026-00136832.pdf','Nationale Bank van België / LA MERIDIENNE SA','2026-08-24','primary_official','tick1772; AV 07.05.2026; A-cap abbrev; Vivalto Home Belgium admin; Forvis Mazars opinion sans reserve; Saint-Denis-Bovesse Rue du Village 13; nrec fin 1.88m; related recv controllers 6.16m'])
    w.writerow(['src_meridienne_site','Vivalto Home — La Méridienne maisons','https://www.vivaltohome.com/maisons/la-meridienne/','Vivalto Home','2026-08-24','primary_official','tick1772; Rue du Village 13 5081 Saint-Denis-Bovesse; lameridienne@vivaltohome.com'])
    w.writerow(['src_meridienne_kbo','KBO LA MERIDIENNE SA 0432.683.346','https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0432683346','KBO','2026-08-24','primary_official','tick1772; SA/NV; Rue du Village 13 5081 Saint-Denis-Bovesse; RPR Namur'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,'La Méridienne NV (leftover Vivalto WZC dual / Saint-Denis-Bovesse)','LA MERIDIENNE SA (WZC Vivalto résiduel / Saint-Denis-Bovesse)','LA MERIDIENNE SA leftover Vivalto nursing-home dual Saint-Denis-Bovesse','other','nv_vivalto_home_be','fr','https://www.vivaltohome.com/maisons/la-meridienne/','lameridienne@vivaltohome.com','Rue du Village 13 5081 Saint-Denis-Bovesse','tick1772 leftover Vivalto WZC dual after De Vrienden; KBO 0432.683.346 Actief; SA; official NBB A-cap YE2025 deposit 2026-00136832 CDN 200; AV 07.05.2026; mère Vivalto Home Belgium; opinion sans réserve; nrec fin 1884018; dividend apport 2000000; related recv controllers 6155186; sourced euros assets 10253817 equity 3604150 debt 6243716 FVA 4000000 leasing LT 2568729 marge 4004546 staff 3139951 VTE 50.3 expl 561263 pnl 2232767 admin 173076 autres creances JUMP 2155186; FOI ready RIZIV/nrec fin/related recv/dividend'])

buds=[
 ('bud_meridienne_assets_2025',10253817,'stock','Assets YE2025 10253817 UP vs 9469659; tick1772'),
 ('bud_meridienne_equity_2025',3604150,'stock','Equity 3604150; tick1772'),
 ('bud_meridienne_debt_2025',6243716,'stock','Debt 6243716; tick1772'),
 ('bud_meridienne_leasing_lt_2025',2568729,'stock','LT credit/leasing 2568729; tick1772'),
 ('bud_meridienne_fva_2025',4000000,'stock','Immobilisations financieres 4000000 DROP vs 5091301; tick1772'),
 ('bud_meridienne_autres_creances_2025',2155186,'stock','Autres creances ST 2155186 JUMP vs 258; tick1772'),
 ('bud_meridienne_related_recv_2025',6155186,'stock','Creances sur administrateurs/controleurs 9500=6155186; tick1772'),
 ('bud_meridienne_marge_2025',4004546,'realized','Marge bruto 4004546 (A-cap; CA undisclosed); tick1772'),
 ('bud_meridienne_staff_2025',3139951,'realized','Staff 3139951 / VTE 50.3; tick1772'),
 ('bud_meridienne_expl_2025',561263,'realized','Benefice exploitation 561263; tick1772'),
 ('bud_meridienne_nrec_fin_2025',1884018,'realized','Produits financiers non recurrents 1884018 drives PnL; tick1772'),
 ('bud_meridienne_pnl_2025',2232767,'realized','PnL 2232767; dividend apport 2000000 + admin 173076; tick1772'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,'LA MERIDIENNE SA JR2025 leftover Vivalto dual (marge 4.00m / nrec fin 1.88m / related recv 6.16m)',eid,'LA MERIDIENNE SA / Vivalto Home Belgium / residents Saint-Denis-Bovesse','CSA SA; decret wallon openbaarheid analog for dual care euros','2026-05-07',2025,2025,4004546,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00136832.pdf','Local leftover Vivalto WZC map WAL Namur — marge 4.00m / nrec fin + mega related recv','Publish CA/RIZIV split + nature nrec fin 1.88m + related recv 6.16m counterparties + dividend 2.00m rationale; unit-cost',sid,'strong',hier,'tick1772; assets 10.25m equity 3.60m debt 6.24m FVA 4.00m leasing LT 2.57m marge 4.00m staff 3.14m VTE 50.3 expl 0.56m nrec fin 1.88m pnl 2.23m dividend 2.00m related recv 6.16m; FOI ready not sent; not TE-additive; A-cap CA undisclosed; next live CDN Seniorie Braine/Centenaire/ClosDesRoses/Etrier/VertBocage/Tonnelle/AgeDor'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,'LA MERIDIENNE SA 2025: marge 4.00m / staff 3.14m (nrec fin 1.88m + dividend 2.00m + related recv 6.16m)','L5','nursing_home_private_dual',hier.replace('>JR2025_L5',''),4004546,6155186,'Envelope=marge 4004546 (A-cap; CA undisclosed); staff 3.14m VTE 50.3; nrec fin 1.88m drives PnL 2.23m; dividend apport 2.00m; related recv controllers 6.16m; autres creances JUMP 2.16m; FVA 4.00m','strong',sid,'MRPA/WZC residents Saint-Denis-Bovesse / Vivalto group','Nursing-home care (MRPA/MRS)','Operating expl solid but PnL dominated by non-rec fin + large controller receivables + 2m dividend; CA hidden',6.3,6.0,5,6.7,'Publish CA/RIZIV; disclose nrec fin + related recv map + dividend rationale; unit-cost','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB A-cap YE2025 live marge 4004546 but CA undisclosed; nrec fin products 1884018 nature unexplained; related recv controllers 6155186 counterparties/terms; dividend apport 2000000 vs prior 0; autres creances JUMP 2155186; FVA 4000000 nature; leasing LT 2568729 + option achat 130800; admin remun 173076','Vivalto Namur WZC with abbreviated schema + non-rec fin driven PnL + mega controller receivables + 2m dividend — opacity on public RIZIV share and group cash extraction',8,'LA MERIDIENNE SA / Vivalto Home Belgium SA','lameridienne@vivaltohome.com','Rue du Village 13 5081 Saint-Denis-Bovesse',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1772; human-send only; Brembloem still no JR2025; AGB Bornem JR2024; other Vivalto CDN live for later: Braine 00136833 Centenaire 00136834 ClosRoses 00176179 Etrier 00176181 VertBocage 00176184 Tonnelle 00176186 AgeDor 00176187; NOT DeVrienden continuum'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1772':
        row['status']='done'
        row['title']='LA MERIDIENNE SA JR2025 leftover Vivalto dual residual'
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=('Completed: LA MERIDIENNE SA leftover Vivalto WZC dual Saint-Denis-Bovesse after De Vrienden; '
            'KBO 0432.683.346 Actief; live JR2025 official NBB A-cap PDF (237452 bytes 28p deposit 2026-00136832; AV 07.05.2026; '
            'Vivalto Home Belgium; opinion sans réserve); '
            'sourced euros assets 10253817 equity 3604150 debt 6243716 marge 4004546 staff 3139951 VTE 50.3 '
            'nrec fin 1884018 pnl 2232767 dividend 2000000 related recv 6155186; FOI ready not sent; NOT DeVrienden continuum')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']='tick1772 LA MERIDIENNE leftover Vivalto residual; KBO 0432.683.346; live JR2025 NBB A-cap PDF; sourced euros; FOI ready not sent; next rq_1773 residual dual L5'
        print('updated rq_1772'); break
else:
    raise SystemExit('missing')
if not any(r.get('task_id')=='rq_1773' for r in rows):
    rows.append({
        'task_id':'rq_1773','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':('Tick 1773 after 1772 LA MERIDIENNE. Next every-10 is 1780. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), '
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200 '
                 '(Seniorie Braine 2026-00136833 / LE CENTENAIRE 2026-00136834 / LE CLOS DES ROSES 2026-00176179 / '
                 'L ETRIER D ARGENT 2026-00176181 / AU VERT BOCAGE 2026-00176184 / LA TONNELLE 2026-00176186 / L AGE D OR 2026-00176187 live), '
                 'other IOED/HVZ/IGS. Do NOT redo Meridienne/DeVrienden continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':'spawned after tick1772 LA MERIDIENNE; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/Braine/Centenaire/ClosRoses/Etrier/VertBocage/Tonnelle/AgeDor; next every-10 1780'
    })
    print('spawned rq_1773')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
print('OK')
