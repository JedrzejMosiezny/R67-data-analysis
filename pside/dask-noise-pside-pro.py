# dask-noise.py
print("Loading Libraries...")
import os, sys
import csv
import platform
import numpy as np
import pandas as pd
import dask.dataframe as dd
import math
print("Loaded Libraries...")
print("Starting code...")

print("Loading directories..")
path_data = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/pside'
path_post = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/pside-post'
path_acu = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/pside-post/acu'
#path_plots = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/int-01-post/plots'
print("Loaded directories...")

print("Loading batch data...")
os.chdir(path_data)
batch_data = dd.read_csv('*.dat', delimiter=r"\s+", decimal='.')
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
filelist = sorted(os.listdir(path_data))[len(os.listdir(path_acu)):]

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
    acoustic_data.to_csv(str('pside_acu_' + str(timestep) + '.dat'), sep=',')
    print(str('pside_acu_' + str(timestep) + '.dat done...'))
print("Exiting noise analysis loop...")

print("Script done, exiting.")