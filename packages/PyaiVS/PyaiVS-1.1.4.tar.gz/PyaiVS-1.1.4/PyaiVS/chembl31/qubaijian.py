import pandas as pd
df = pd.read_csv('/data/jianping/bokey/OCAICM/dataset/AURORAB/screen/record.txt',sep = '\t',header=None,names=['file','scale','screen','total'])
compounds = sum(df['total'])/5
info = df.groupby(['scale'])['screen'].sum()/compounds
info = info.reset_index()
info['info'] =['xgb_cluster_ECFP4_57','rf_random_ecfp4_abcg2','xgb_cluster_ECFP4_56','SVM_random_MACCS_56','rf_random_ecfp4_56','SVM_random_MACCS_57']
print(info)
sp = df[df['file']=='/data/jianping/enamine/tenbillion/D001-1.csv']
sp['info'] = ['xgb_cluster_ECFP4_57','rf_random_ecfp4_abcg2','xgb_cluster_ECFP4_56','SVM_random_MACCS_56','rf_random_ecfp4_56','SVM_random_MACCS_57']
sp.loc[6,:] = [sp.iloc[0,0],6,14457,sp.iloc[0,3],'gcn_random_56']
sp['precent'] = sp['screen']/sp['total']
print(sp[['scale','screen','total','precent','info']])





