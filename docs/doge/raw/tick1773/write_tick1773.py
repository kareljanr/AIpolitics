import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1773'; utc='2026-08-24T18:00:00Z'
eid='nv_braine'; sid='src_braine_jr2025_nbb'
gap='gap_braine_ca_6_11m_nrec_fin_2_33m_dividend_2_20m_l5'
lb='lb_braine_ca_6_11m_nrec_fin_2_33m_dividend_2_20m_l5'
comm='comm_braine_jr2025_ca_6_11m'
hier='Wallonie>Provinces>BrabantWallon>Communes>BraineLeChateau>MRPA>SeniorieBraine>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,'Seniorie Braine-Le-Chateau SA NBB C-cap YE2025 deposit 2026-00136833','http://cdn.staatsbladmonitor.be/2026pdf/2026-00136833.pdf','Nationale Bank van België / Seniorie Braine-Le-Chateau SA','2026-08-24','primary_official','tick1773; AV 08.05.2026; C-cap full; Vivalto Home Belgium admin; opinion sans reserve; Braine-le-Chateau Rue Auguste Latour 43k; nrec fin plus-value cession FVA 2.33m; dividend 2.20m'])
    w.writerow(['src_braine_site','Vivalto Home — Seniorie de Braine-le-Château','https://www.vivaltohome.com/maisons/seniorie-de-braine-le-chateau/','Vivalto Home','2026-08-24','primary_official','tick1773; Rue Auguste Latour 43k 1440 Braine-le-Chateau; senioriebrainelechateau.info@vivaltohome.com'])
    w.writerow(['src_braine_kbo','KBO Seniorie Braine-Le-Chateau SA 0448.185.431','https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0448185431','KBO','2026-08-24','primary_official','tick1773; SA/NV; Rue Auguste Latour 43k 1440 Braine-le-Chateau; RPR Brabant wallon'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,'Seniorie Braine-le-Château NV (leftover Vivalto WZC dual / Braine-le-Château)','Seniorie Braine-Le-Chateau SA (WZC Vivalto résiduel / Braine-le-Château)','Seniorie Braine-Le-Chateau SA leftover Vivalto nursing-home dual Braine-le-Chateau','other','nv_vivalto_home_be','fr','https://www.vivaltohome.com/maisons/seniorie-de-braine-le-chateau/','senioriebrainelechateau.info@vivaltohome.com','Rue Auguste Latour 43k 1440 Braine-le-Château','tick1773 leftover Vivalto WZC dual after LA MERIDIENNE; KBO 0448.185.431 Actief; SA; official NBB C-cap YE2025 deposit 2026-00136833 CDN 200; AV 08.05.2026; mère Vivalto Home Belgium; opinion sans réserve; nrec fin 2332732 = plus-value cession FVA; dividend apport 2200000; related recv controllers 7773862; FVA reclass to related autres creances 5600000; sourced euros assets 13693231 equity 4452399 debt 8379027 leasing LT 4641025 omzet 6110005 staff 4046311 VTE 58.9 expl 575104 pnl 2638023; FOI ready RIZIV/cession FVA/related recv/dividend'])

buds=[
 ('bud_braine_assets_2025',13693231,'stock','Assets YE2025 13693231 UP vs 12564982; tick1773'),
 ('bud_braine_equity_2025',4452399,'stock','Equity 4452399; tick1773'),
 ('bud_braine_debt_2025',8379027,'stock','Debt 8379027; tick1773'),
 ('bud_braine_leasing_lt_2025',4641025,'stock','LT leasing debt 4641025; tick1773'),
 ('bud_braine_related_fva_creances_2025',5600000,'stock','Related autres creances FVA 5600000 (participations to 0 after cession); tick1773'),
 ('bud_braine_related_recv_st_2025',2173862,'stock','Creances entreprises liees ST 2173862; tick1773'),
 ('bud_braine_related_recv_controllers_2025',7773862,'stock','Creances sur administrateurs/controleurs 9500=7773862; tick1773'),
 ('bud_braine_omzet_2025',6110005,'realized','Chiffre d affaires 6110005 (C-cap disclosed); tick1773'),
 ('bud_braine_staff_2025',4046311,'realized','Staff 4046311 / VTE 58.9 DROP vs 64.4; tick1773'),
 ('bud_braine_expl_2025',575104,'realized','Benefice exploitation 575104; tick1773'),
 ('bud_braine_nrec_fin_2025',2332732,'realized','Nrec fin 2332732 plus-value cession immobilisations financieres; tick1773'),
 ('bud_braine_pnl_2025',2638023,'realized','PnL 2638023 TURNAROUND; dividend apport 2200000 + admin 224212; tick1773'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,'Seniorie Braine SA JR2025 leftover Vivalto dual (CA 6.11m / nrec fin 2.33m / dividend 2.20m)',eid,'Seniorie Braine-Le-Chateau SA / Vivalto Home Belgium / residents Braine-le-Chateau','CSA SA; decret wallon openbaarheid analog for dual care euros','2026-05-08',2025,2025,6110005,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00136833.pdf','Local leftover Vivalto WZC map WAL Brabant wallon — CA 6.11m / FVA cession gain + dividend extraction','Publish RIZIV split + FVA cession buyer/terms + related recv 7.77m map + dividend 2.20m rationale; unit-cost',sid,'strong',hier,'tick1773; assets 13.69m equity 4.45m debt 8.38m leasing LT 4.64m omzet 6.11m staff 4.05m VTE 58.9 expl 0.58m nrec fin 2.33m pnl 2.64m dividend 2.20m related recv controllers 7.77m; FOI ready not sent; not TE-additive; twin Meridienne pattern'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,'Seniorie Braine SA 2025: CA 6.11m / staff 4.05m (nrec FVA gain 2.33m + dividend 2.20m + related recv 7.77m)','L5','nursing_home_private_dual',hier.replace('>JR2025_L5',''),6110005,7773862,'Envelope=CA 6110005 (C-cap); staff 4.05m VTE 58.9; nrec fin 2.33m = plus-value cession FVA; dividend apport 2.20m; related recv controllers 7.77m; FVA reclass to related creances 5.60m; cash DROP to 5.9k','strong',sid,'MRPA/WZC residents Braine-le-Chateau / Vivalto group','Nursing-home care (MRPA/MRS)','Operating turnaround + FVA disposal gain funds 2.2m dividend while cash collapses and controller receivables balloon — group extraction opacity',6.5,6.5,5,7.0,'Publish RIZIV; disclose FVA cession + related recv/dividend map; unit-cost','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB C-cap YE2025 live CA 6110005 but RIZIV/residentie split unpublished; nrec fin 2332732 plus-value cession FVA — need buyer/terms; related recv controllers 7773862 + related ST 2173862; dividend apport 2200000; FVA participations to 0 reclass autres creances liees 5600000; cash DROP 5910; leasing LT 4641025 + option achat 198000; admin 224212','Vivalto Braine WZC with FVA disposal-driven PnL + 2.2m dividend + mega controller receivables + cash collapse — opacity on public care-euro path and group extraction',8,'Seniorie Braine-Le-Chateau SA / Vivalto Home Belgium SA','senioriebrainelechateau.info@vivaltohome.com','Rue Auguste Latour 43k 1440 Braine-le-Château',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1773; human-send only; Brembloem still no JR2025; AGB Bornem JR2024; CDN live Centenaire/ClosRoses/Etrier/VertBocage/Tonnelle/AgeDor; NOT Meridienne continuum'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1773':
        row['status']='done'
        row['title']='Seniorie Braine-Le-Chateau SA JR2025 leftover Vivalto dual residual'
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=('Completed: Seniorie Braine-Le-Chateau SA leftover Vivalto WZC dual after LA MERIDIENNE; '
            'KBO 0448.185.431 Actief; live JR2025 official NBB C-cap PDF (1204232 bytes 53p deposit 2026-00136833; AV 08.05.2026; '
            'Vivalto Home Belgium; opinion sans réserve); '
            'sourced euros assets 13693231 equity 4452399 debt 8379027 omzet 6110005 staff 4046311 VTE 58.9 '
            'nrec fin 2332732 pnl 2638023 dividend 2200000 related recv controllers 7773862; FOI ready not sent; NOT Meridienne continuum')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']='tick1773 Seniorie Braine leftover Vivalto residual; KBO 0448.185.431; live JR2025 NBB C-cap PDF; sourced euros; FOI ready not sent; next rq_1774 residual dual L5'
        print('updated rq_1773'); break
else:
    raise SystemExit('missing')
if not any(r.get('task_id')=='rq_1774' for r in rows):
    rows.append({
        'task_id':'rq_1774','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':('Tick 1774 after 1773 Seniorie Braine. Next every-10 is 1780. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), '
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200 '
                 '(LE CENTENAIRE 2026-00136834 / LE CLOS DES ROSES 2026-00176179 / L ETRIER D ARGENT 2026-00176181 / '
                 'AU VERT BOCAGE 2026-00176184 / LA TONNELLE 2026-00176186 / L AGE D OR 2026-00176187 live), '
                 'other IOED/HVZ/IGS. Do NOT redo Braine/Meridienne continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':'spawned after tick1773 Seniorie Braine; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/Centenaire/ClosRoses/Etrier/VertBocage/Tonnelle/AgeDor; next every-10 1780'
    })
    print('spawned rq_1774')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
print('OK')
