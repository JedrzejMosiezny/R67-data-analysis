import os, sys
import pandas as pd
import numpy as np
import csv

path_gen = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/' #ścieżka do katalogu z interesującymi nas plikami
path_post = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/post/' #ścieżka do katalogu z interesującymi nas plikami

os.chdir(path_post)

acupress = pd.read_csv('exp_acupress.csv', sep=',', skiprows=0, index_col=0) #wczytaj pierwszą kolumnę
acupress = pd.DataFrame(data = acupress)
#print(acupress)

mean_p = []
for index, row in acupress.iterrows():
    row = acupress.iloc[index]
    mean = np.mean(row)
    mean_p.append(mean)

dev_p = []
for column in acupress:
    acu_col = acupress.loc[:, column]
    dev = acu_col.sub(mean_p,fill_value=0)
    dev_p.append(dev)