import pandas as pd
from rdkit.Chem.Scaffolds.MurckoScaffold import MurckoScaffoldSmiles
from rdkit import Chem
from rdkit.Chem import Draw
def generate_scaffolds(dataset):
    scaffolds = {}
    for i, ind in enumerate(list(dataset.index)):
        smiles = dataset.iloc[i]
        scaffold = generate_scaffold(smiles)
        if scaffold not in scaffolds:
            scaffolds[scaffold] = [(ind,smiles)]
        else:
            scaffolds[scaffold].append((ind,smiles))

    # Sort from largest to smallest scaffold sets
    scaffolds = {key: sorted(value) for key, value in scaffolds.items()}
    content = list(scaffolds.items())
    content = sorted(content,key=lambda x:len(x[1]),reverse=True)
    return content


def generate_scaffold(smiles):
    mol = Chem.MolFromSmiles(smiles)
    scaffold = MurckoScaffoldSmiles(mol=mol)
    return scaffold
df =pd.read_csv('/data/jianping/web-ocaicm/bokey/PyaiVS/chembl31/abcg2_info.csv')
df =df[df['label']==1]
a = generate_scaffolds(df['Smiles'])
data=pd.DataFrame()
for j,i in enumerate(a[:20]):
    info = [ele[1] for ele in i[1]]
    info = df[df['Smiles'].isin(info)]
    info = info.sort_values('value',ascending=True)

    info=info.reset_index()
    info = info.iloc[:2,:]
    info = info[['Smiles', 'value', 'Molecule']]
    data = pd.concat([data,info],ignore_index=True)
data.to_csv('scaffold_40.csv',index=False)
# f = 0
# b = []
# c = []
# for i in range(len(a)):
#     # print(len(a[i][1]))
#     f+=len(a[i][1])
#     if i%10 ==0:
#         b.append(i)
#         c.append(f)
#         print(f,i)
# b.append(len(a))
# c.append(f)
# print(f,len(a))
# import matplotlib.pyplot as plt
# plt.scatter(b,c)
# plt.xlabel('scaffold num')
# plt.ylabel('active compounds')
# # plt.savefig('./scaffold.png',dpi=300)
# plt.show()