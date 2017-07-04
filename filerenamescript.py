import os
path = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/data' 
lista = os.listdir(path)

for filename in lista:
    os.rename(filename, filename + ".dat")
