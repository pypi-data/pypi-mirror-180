from PyaiVS import model_bulid
import os


os.environ['PYTHONHASHSEED'] = str(42)  # 为了禁止hash随机化，使得实验可复现['KNN','SVM','RF','XGB']
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"
os.environ['PYTHONHASHSEED']='0'
model_bulid.running('/data/jianping/bokey/OCAICM/dataset/abcg2/abcg2.csv',out_dir='/data/jianping/bokey/OCAICM/dataset/',
                    split='all',model='all',FP='all', run_type='param',cpus=8)



#   model  des   split   auc_roc  f1_score       acc       mcc
# 1   gcn  gcn  random  0.921182  0.900331  0.864833  0.705656
#   model  des   split   auc_roc  f1_score       acc       mcc
# 1   gcn  gcn  random  0.920603  0.903845  0.868257  0.712589
#   model  des   split   auc_roc  f1_score       acc       mcc
# 1   gcn  gcn  random  0.921034  0.899969  0.864347  0.704808

