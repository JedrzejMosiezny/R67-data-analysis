import os, sys
import csv
import platform
import numpy as np
import pandas as pd
import dask.dataframe as dd
import scipy
import sklearn
import matplotlib as plt
import flask
import math

path_data = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/data'
path_post = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/post' 
path_acu = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/post/acu'
path_plots = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/11_CFX/05_PhD runs/R67_fluent/peak_R67_hgt_512k/trn_des_v01/post/plots' #ścieżka do katalogu z interesującymi nas plikami

batch_data = dd.read_csv('data/asdp_data-*.dat', sep='\s+', decimal='.')
averages = pd.DataFrame(batch_data.groupby('nodenumber').mean().compute())
avg_static_p = pd.DataFrame({'pressure': averages['pressure']})

del(batch_data)

filelist = os.listdir(path_data)

for file in filelist:
    os.chdir(path_data)
    timestep = str(os.path.basename(str(file)))[10:-4]
    time_static_p = pd.DataFrame(pd.read_csv(file, sep='\s+', header=0, usecols=["nodenumber", "pressure"], skiprows=0, decimal='.')).set_index('nodenumber')
    acoustic_p = time_static_p.subtract(avg_static_p, fill_value=None)
    os.chdir(path_acu)
    acoustic_p.to_csv(str('asdp_acu_p_' + str(timestep) + '.dat'), sep=',')
    




rms = batch_data.groupby('nodenumber').square().compute()
