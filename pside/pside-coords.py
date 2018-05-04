print("Loading Libraries...")
import os, sys
import csv
import platform
import numpy as np
import pandas as pd
import dask.dataframe as dd

'''
#PUT Workstation
print("Loading directories..") 
path_acu = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside-post/acu'
path_plots = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside-post/plots'
path_fft = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside-post/fft'
path_rms = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside-post/rms'
path_coords = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside-post/coords'
print("Loaded directories...")
'''

#PLGRID
print("Loading directories..")
path_acu = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/pside-post/acu'
path_plots = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/pside-post/plots'
path_fft = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/pside-post/fft'
path_rms = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/pside-post/rms'
path_coords = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/pside-post/coords'
print("Loaded directories...")

print("Generating coords...")
os.chdir(path_acu)
filelist = os.listdir(path_acu)
first = filelist[0]
base_file = pd.read_csv(first, delimiter=",", decimal='.').set_index('nodenumber')
coords = base_file.iloc[:, :3]
os.chdir(path_coords)
coords.to_csv(str('pside_coords.dat'), sep=',')

print("Starting coords loop...")
os.chdir(path_acu)
for file in filelist:
    base_file = pd.read_csv(file, delimiter=",", decimal='.').set_index('nodenumber')
    data = base_file.iloc[:, 3:]
    data.to_csv(str(file), sep=',')
print("Coords done")