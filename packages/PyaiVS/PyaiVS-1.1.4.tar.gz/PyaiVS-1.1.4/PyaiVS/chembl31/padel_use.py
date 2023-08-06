from padelpy import padeldescriptor
from padelpy import from_smiles
import pandas as pd
file = '/data/jianping/bokey/OCAICM/dataset/HIV/HIV_pro.csv'
data = pd.DataFrame()
f = open('res_smiles.csv','w')
for line in open(file,'r').readlines()[1:]:
    smiles = line.split(',')[0]
    try:
        a =pd.DataFrame(from_smiles(smiles, fingerprints=True, descriptors=False,timeout=1),index=[0])
        data=pd.concat([data,a],ignore_index=True)
    except:
        f.write(smiles+'\n')
f.close()
data.to_csv('timeout_1.csv',index=False)

