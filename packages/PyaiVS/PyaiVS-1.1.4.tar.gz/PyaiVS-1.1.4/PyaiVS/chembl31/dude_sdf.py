from rdkit import Chem

import os
import pandas as pd
from rdkit.Chem import Lipinski, Descriptors, Crippen,rdMolDescriptors
# def sdf_creat(row):
#     smiles =row[1]
#     mol = Chem.MolFromSmiles(smiles)
#     mol = Chem.AddHs(mol)
#     mol.SetProp('name','dude_'+str(row[0]))
#     mol.SetProp('smiles',str(row[1]))
#     mol.SetProp('cindex',  str(row[2]))
#     mol.SetProp('pindex',  str(row[3]))
#     return mol
# dude_dir = '/home/jianping/Downloads/test/dude-decoys/decoys'
# smiles = []
# for file in os.listdir(dude_dir):
#     info = [row.strip().split('	') for row in open(os.path.join(dude_dir,file),'r').readlines()[1:]]
#     print(info)
#     smiles.extend(info)
# df = pd.DataFrame(smiles,columns=['Smiles','Cindex','Pindex'])
# file_name = dude_dir+'/decoys.sdf'
# dd = df[['Smiles']]
# df.to_csv('/data/jianping/bokey/schrodinger/decoys.smi',index=False,header=False)
# # w = Chem.SDWriter(file_name)
# for j,row in enumerate(df.to_records()):
#     if j%100 == 0:
#         print(j,len(df))
#     mol = sdf_creat(row)
#     w.write(mol)