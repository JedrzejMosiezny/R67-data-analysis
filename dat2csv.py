import pandas as pd
import os
path = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/data/'
os.chdir(path)
df = pd.read_csv('asdp_data-0001.dat', sep='\s+', header=0, usecols=["pressure"], dtype=str, skiprows=None, decimal='.')

print(df)