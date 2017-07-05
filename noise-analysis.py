import os, sys
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

path_gen = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/' #ścieżka do katalogu z interesującymi nas plikami
path_data = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/data/' #ścieżka do katalogu z interesującymi nas plikami
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
    
dev_p = pd.DataFrame(data = dev_p)
dev_p = dev_p.T
dev_p.to_csv('exp_dev_p.csv', sep=',')

for index, row in dev_p.iterrows():
    row = dev_p.iloc[index]
    plt.figure(index, figsize=(7,6))
    plt.plot(row)
    plt.title('Acoustic pressure at point '+index+'')
    plt.xlabel('Time 1e-06')
    plt.ylabel('[Pa]')
    plt.ylim((-2500,2500))
    plt.savefig('Ap_point'+index+'.png')
    #plt.show()
    #print(row)




'''
plt.figure(1, figsize=(7,6))        #Numer rysunku (okna), rozmiar wykresu w calach
plt.plot(heat)
plt.title('Heat of reaction')
plt.xlabel('Iteration')
plt.ylabel('[W]')

plt.text(120, 7000, Average heat of reaction from last 15 iteration is equal +avg_heat+' kW')

'''
