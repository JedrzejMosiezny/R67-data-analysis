import os, sys
import pandas as pd
import numpy as np
import csv

path = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/data/' #ścieżka do katalogu z interesującymi nas plikami
path2 = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/' #ścieżka do katalogu, gdzie będzie utworzony plik z wynikiem


filelist = os.listdir(path)            #Tworzy listę z plików w danym katalogu
tscount = len(filelist);
#print(filelist)                        #Wyświetla listę plików
os.chdir(path)                          #przejdź do katalogu
pstatic = pd.read_csv('asdp_data-0001.dat', sep='\s+', header=0, usecols=["pressure"], dtype=str, skiprows=None, decimal='.') #wczytaj pierwszą kolumnę

acupress = pd.DataFrame(data = pstatic) #zamień kolumnę na dataframe

for file in filelist:
    pstatic = pd.read_csv(file, sep='\s+', header=0, usecols=["pressure"], dtype=str, skiprows=None, decimal='.')
    pstatic = pd.DataFrame(data = pstatic)
    frames = [acupress, pstatic]
    acupress = pd.concat(frames, axis=1)

#acupress.drop(acupress.columns(1, axis=1)
os.chdir(path2)
acupress.to_csv('acupress.csv', sep=', ', header = ["timestep", 1, tscount, 1])