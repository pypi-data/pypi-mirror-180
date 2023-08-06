import pandas as pd
import os
path = '/data/jianping/bokey/OCAICM/dataset/aurorab/screen/'
# total = 0
# for file in os.listdir('/data/jianping/enamine/tenbillion'):
#     if '.csv' in file:
#
#         total+=len(open(os.path.join('/data/jianping/enamine/tenbillion',file),'r').readlines())
# f = open('record_models.csv','w')
# for dir in os.listdir(path):
#     if os.path.isdir(os.path.join(path,dir)):
#         if len(os.listdir(os.path.join(path,dir))) == 16:
#             count = 0
#             for file in os.listdir(os.path.join(path,dir)):
#                 count+=len(open(os.path.join(path,dir,file),'r').readlines())
#             print(dir,count,total)
#             f.write('%s\t%d\t%d\n'%(dir.replace('_','\t'),count,total))
# f.close()

# df = pd.read_csv('record_models.csv',sep='\t',header=None,names=['model','split','des','screen','number'])
# ref = pd.read_csv('/data/jianping/bokey/OCAICM/dataset/aurorab/aurorab_mcc_152.csv')
# data = pd.merge(df,ref,on=['model','split','des'])
# data['number'] = round(data['screen']/data['number'],2)
# data.to_csv('record_mdoels.csv',index=False)

