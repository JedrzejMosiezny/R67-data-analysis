# dask-noise.py
print("Loading Libraries...")
import os, sys
import csv
import platform
import numpy as np
import pandas as pd
import dask.dataframe as dd
import math
print("Starting code...")

print("Loading directories..")
path_data = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/sside'
path_post = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/sside-post'
path_acu = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/sside-post/acu'
path_plots = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/sside-post/plots' 
print("Loaded directories...")

print("Loading batch data...")
os.chdir(path_data)
batch_data = dd.read_csv('ss*.dat', delimiter=r"\s+", decimal='.')
print("Batch data done...")

print("Calculating batch averages...")
averages = pd.DataFrame(batch_data.groupby('nodenumber').mean().compute())
print("Batch averages done...")

print("Generating node coordinates...")
avg_static_p = pd.DataFrame({'pressure': averages['pressure']})
node_coords = pd.DataFrame({
    'x-coordinate': averages['x-coordinate'],
    'y-coordinate': averages['y-coordinate'],
    'z-coordinate': averages['z-coordinate']
})
print("Node coords done...")

del(batch_data)
print("Batch data deleted...")

print("Listing files...")
filelist = os.listdir(path_data)

print("Starting noise analysis loop...")
for file in filelist:
    os.chdir(path_data)
    timestep = str(os.path.basename(str(file)))[11:-4]
    time_static_p = pd.DataFrame(pd.read_csv(file, delimiter=r"\s+", header=0, usecols=["nodenumber", "pressure"], skiprows=0, decimal='.')).set_index('nodenumber')
    acoustic_p = time_static_p.subtract(avg_static_p, fill_value=None)
    db = acoustic_p.apply(lambda x: 20 * np.log10(np.abs(x)/0.00002), axis=1)
    acoustic_data = pd.concat([node_coords, acoustic_p, db], axis=1)
    acoustic_data.columns = ['x-coordinate', 'y-coordinate', 'z-coordinate', 'sound-pressure', 'db-level']
    os.chdir(path_acu)
    acoustic_data.to_csv(str('sside_acu_' + str(timestep) + '.dat'), sep=',')
    print(str('sside_acu_' + str(timestep) + '.dat done...'))
print("Exiting noise analysis loop...")

print("Script done, exiting.")