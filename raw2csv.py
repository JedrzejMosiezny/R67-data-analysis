import os, sys
import pandas as pd
import numpy as np
import csv

path = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/data/' #ścieżka do katalogu z interesującymi nas plikami
path2 = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/' #ścieżka do katalogu, gdzie będzie utworzony plik z wynikiem

filelist = os.listdir(path)            #Tworzy listę z plików w danym katalogu
os.chdir(path)                          #przejdź do katalogu
tsnum = str(os.path.basename(str(path + 'asdp_data-0001.dat')))
tsnum = tsnum[10:-4]

pstatic = pd.read_csv('asdp_data-0001.dat', sep='\s+', header=0, usecols=["pressure"], dtype=str, skiprows=0, decimal='.') #wczytaj pierwszą kolumnę
acupress = pd.DataFrame(data = pstatic) #zamień kolumnę na dataframe
acupress.columns = [tsnum]

for file in filelist[1:]:
    tsnum = str(os.path.basename(str(path + file)))
    tsnum = tsnum[10:-4]
    pstatic = pd.read_csv(file, sep='\s+', header=0, usecols=["pressure"], dtype=str, skiprows=0, decimal='.')
    pstatic = pd.DataFrame(data = pstatic,)
    pstatic.columns = [tsnum]
    frames = [acupress, pstatic]
    acupress = pd.concat(frames, axis=1)

os.chdir(path2)
acupress.to_csv('exp_acupress.csv', sep=',')