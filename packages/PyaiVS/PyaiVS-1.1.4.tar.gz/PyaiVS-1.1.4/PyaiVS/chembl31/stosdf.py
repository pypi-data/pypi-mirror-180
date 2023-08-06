import pandas as pd
import rdkit
from rdkit.Chem import  AllChem
def digit_check(x):
    digits = '0123456789.'
    if len(set(str(x))-set(digits))!=0:
        if '>' in str(x):
            return 0
        elif "<1" in str(x):
            return 1
        elif "1-10" in str(x) or 'n.t.' in str(x):
            return 2
        else:
            if float(str(x)[1:]) >10:
                return 0
            else:
                return  2

    else:
        if float(x)>=10:
            return 0
        elif float(x)<=1:
            return 1
        else:
            return 2

df = pd.read_excel('/data/jianping/bokey/OCAICM/dataset/I1049.xlsx')
df=df[['SMILES','IC50 ABCG2 [uM]']]
df = df.dropna()
df.columns = ['Smiles','activity']
di = df[df['activity']=='inactive']
di['label'] = 0
dd = df[~df['activity'].isin(['inactive'])]
dd['label'] = dd['activity'].apply(digit_check)
df = dd[dd['label'].isin([1,0])]
df = pd.concat([df,di])
df['value'] = df['activity']

ref = pd.read_csv('/data/jianping/web-ocaicm/bokey/PyaiVS/chembl31/ABCG2_1.csv')
ref =ref[['Smiles','Activity','Standard Value']]
ref.columns = ['Smiles','label','value']
df = pd.concat([df,ref],ignore_index=True)
df['cano'] = df['Smiles'].apply(lambda x:AllChem.MolToSmiles(AllChem.MolFromSmiles(x)))
dinact = df[df['label']==0]
dact = df[df['label']==1]

dinact = dinact.drop_duplicates(subset=['cano'],keep='first')
dact = dact.drop_duplicates(subset=['cano'],keep='first')
df = pd.concat([dinact,dact])
print(df['label'].value_counts())
df =df[['Smiles','label','value']]
df = df.sample(frac=1)
df.to_csv('/data/jianping/bokey/abcg2.csv',index=False)
# print(pd.read_csv('/data/jianping/bokey/OCAICM/dataset/ABCG2/ABCG2.csv')['Activity'].value_counts())