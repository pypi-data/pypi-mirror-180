import rdkit
from rdkit import Chem
import pandas as pd
from rdkit.Chem import Lipinski, Descriptors, Crippen,rdMolDescriptors
def sdf_creat(row):
    smiles =row[1]
    # label = row[2]
    # value = row[3]
    # name = row[-1]
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    mol.SetProp('name','inactive_'+str(row[0]))
    # mol.SetProp('label', str(label))
    # mol.SetProp('value', str(value))
    return mol
def lp_info(x):
    mol = Chem.MolFromSmiles(x)
    h_acc = Lipinski.NumHAcceptors(mol)
    h_don = Lipinski.NumHDonors(mol)
    rotal = Lipinski.NumRotatableBonds(mol)
    weight = Descriptors.ExactMolWt(mol)
    logp = Crippen.MolLogP(mol)
    count = sum([weight <= 500, h_acc <= 10, h_don <= 5, logp <= 5])
df = pd.read_csv('/data/jianping/web-ocaicm/bokey/PyaiVS/chembl31/abcg2_info.csv')
df = df[df['label']==0]
# act = df
# act['h_acc'] = act['Smiles'].apply(lambda x:Lipinski.NumHAcceptors(Chem.MolFromSmiles(x)))
# act['h_don'] = act['Smiles'].apply(lambda x:Lipinski.NumHDonors(Chem.MolFromSmiles(x)))
# act['weight'] = act['Smiles'].apply(lambda x:Descriptors.ExactMolWt(Chem.MolFromSmiles(x)))
# act['rotal'] = act['Smiles'].apply(lambda x:Lipinski.NumRotatableBonds(Chem.MolFromSmiles(x)))
# act['logp'] = act['Smiles'].apply(lambda x:Crippen.MolLogP(Chem.MolFromSmiles(x)))
# act['aring'] = act['Smiles'].apply(lambda x:rdMolDescriptors.CalcNumAromaticRings(Chem.MolFromSmiles(x)))
# act['ring'] = act['Smiles'].apply(lambda x:rdMolDescriptors.CalcNumRings(Chem.MolFromSmiles(x)))
# act.to_csv('abcg2_info.csv',index=False)
# ref1 = pd.read_csv('/data/jianping/web-ocaicm/bokey/PyaiVS/chembl31/ABCG2_1.csv')[['Molecule ChEMBL ID','Smiles']]
# ref1.columns = ['Molecule','Smiles']
# ref2 = pd.read_excel('/data/jianping/bokey/OCAICM/dataset/I1049.xlsx')[['Compound ', 'SMILES']]
# ref2.columns = ['Molecule','Smiles']
# part1 = pd.merge(act,ref1,on='Smiles')
# part2 = pd.merge(act,ref2,on='Smiles')
# df = pd.concat([part1,part2])
# df.to_csv('abcg2_info.csv',index=False)
w = Chem.SDWriter('inactive.sdf')
for j,row in enumerate(df.to_records()):
    if j%100 == 0:
        print(j,len(df))
    mol = sdf_creat(row)
    w.write(mol)
# df = pd.read_csv('abcg2_info.csv')
# df = df[df['label']==1]
# print(df['value'].apply(lambda x:float(x)))

# import matplotlib.pyplot as plt
# from matplotlib.gridspec import GridSpec
# import seaborn as sns
# from scipy.stats import gaussian_kde
# df = pd.read_csv('abcg2_info.csv')
#
# gs = GridSpec(3,3)
# plt.subplot(gs[0,0])
# data1 = df[df['label']==0]['aring'].value_counts()
# data2= df[df['label']==1]['aring'].value_counts()
# plt.bar(data2.index,data2/len(df[df['label']==1]))
# plt.bar(data1.index,-data1/len(df[df['label']==0]))
# plt.legend(['active','inactive'])
# plt.title('Aromatic Ring')
#
# plt.subplot(gs[0,1])
# data1 = df[df['label']==0]['ring'].value_counts()
# data2= df[df['label']==1]['ring'].value_counts()
# plt.bar(data2.index,data2/len(df[df['label']==1]))
# plt.bar(data1.index,-data1/len(df[df['label']==0]))
# plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11])
# plt.legend(['active','inactive'])
# plt.title('Ring')
#
# plt.subplot(gs[0,2])
# data1 = df[df['label']==0]['weight']
# data2= df[df['label']==1]['weight']
# plt.hist(data2,alpha=0.8,density=True)
# plt.hist(data1,alpha=0.8,density=True)
# plt.xlabel('')
# plt.ylabel('')
# sns.kdeplot(data2)
# sns.kdeplot(data1)
# plt.yticks([0,0.001,0.002,0.003,0.004,0.005],[0,0.1,0.2,0.3,0.4,0.5])
# plt.legend(['active','inactive'])
# plt.title('Weight')
#
# plt.subplot(gs[1,0])
# data1 = df[df['label']==0]['h_acc'].value_counts()
# data2= df[df['label']==1]['h_acc'].value_counts()
# plt.bar(data2.index,data2/len(df[df['label']==1]))
# plt.bar(data1.index,-data1/len(df[df['label']==0]))
#
# plt.legend(['active','inactive'])
# plt.title('h_acc')
#
# plt.subplot(gs[1,1])
# data1 = df[df['label']==0]['h_don'].value_counts()
# data2= df[df['label']==1]['h_don'].value_counts()
# plt.bar(data2.index,data2/len(df[df['label']==1]))
# plt.bar(data1.index,-data1/len(df[df['label']==0]))
# plt.legend(['active','inactive'])
# plt.title('h_don')
#
# plt.subplot(gs[1,2])
# data1 = df[df['label']==0]['rotal'].value_counts()
# data2= df[df['label']==1]['rotal'].value_counts()
# plt.bar(data2.index,data2/len(df[df['label']==1]))
# plt.bar(data1.index,-data1/len(df[df['label']==0]))
# plt.legend(['active','inactive'])
# plt.xlabel('Rotatable')
#
# plt.subplot(gs[2,0])
# data1 = df[df['label']==0]['logp']
# data2= df[df['label']==1]['logp']
# plt.hist(data2,alpha=0.8,density=True)
# plt.hist(data1,alpha=0.8,density=True)
# sns.kdeplot(data2)
# sns.kdeplot(data1)
# plt.legend(['active','inactive'])
# plt.title('logp')
#
#
# plt.show()
# plt.savefig('abcg2_info.png',dpi=300)
#
#
