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

'''
print("Loading directories..")
path_data = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-09'
#path_post = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-09-post'
path_acu = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-09-post/acu'
#path_plots = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-09-post/plots'
print("Loaded directories...")
'''

print("Loading directories..")
path_data = '/net/archive/groups/plggcfdp/R67_fluent/SRS_v02/noise-data/int-09'
#path_post = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-09-post'
path_acu = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-09-post/acu'
#path_plots = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-09-post/plots'
print("Loaded directories...")

print("Loading batch data...")
os.chdir(path_data)
batch_data = dd.read_csv('*.dat', delimiter=r"\s+", decimal='.')
print("Batch data done...")

print("Calculating batch averages...")
averages = pd.DataFrame(batch_data.groupby('nodenumber').mean().compute())
print("Batch averages done...")

print("Generating average pressure dataframe")
avg_static_p = pd.DataFrame({'pressure': averages['pressure']})

print("Generating average velocity dataframe")
avg_rel_v = pd.DataFrame({'rel-velocity-magnitude': averages['rel-velocity-magnitude']})

print("Generating node coordinates...")
node_coords = pd.DataFrame({
    'x-coordinate': averages['x-coordinate'],
    'y-coordinate': averages['y-coordinate'],
    'z-coordinate': averages['z-coordinate']
})

del(batch_data)
print("Batch data deleted...")

print("Listing files...")
filelist = sorted(os.listdir(path_data))[len(os.listdir(path_acu)):]

print("Starting noise analysis loop...")
for file in filelist:
    os.chdir(path_data)
    timestep = str(os.path.basename(str(file)))[7:-4]
    time_static_p = pd.DataFrame(pd.read_csv(file, delimiter=r"\s+", header=0, usecols=["nodenumber", "pressure"], skiprows=0, decimal='.')).set_index('nodenumber')
    acoustic_p = time_static_p.subtract(avg_static_p, fill_value=None)
    spl_db = acoustic_p.apply(lambda x: 20 * np.log10(np.abs(x)/0.00002), axis=1)
    time_rel_vel = pd.DataFrame(pd.read_csv(file, delimiter=r"\s+", header=0, usecols=["nodenumber", "rel-velocity-magnitude"], skiprows=0, decimal='.')).set_index('nodenumber')
    particle_v = time_rel_vel.subtract(avg_rel_v, fill_value=None).abs()
    sound_intensity = pd.DataFrame(acoustic_p.values*particle_v.values, index=acoustic_p.index)
    sil_db = sound_intensity.apply(lambda x: 10 * np.log10(np.abs(x)/1e-12), axis=1)
    acoustic_data = pd.concat([node_coords, acoustic_p, spl_db, particle_v, sound_intensity, sil_db], axis=1)
    acoustic_data.columns = ['x-coordinate', 'y-coordinate', 'z-coordinate', 'sound-pressure', 'spl-db', 'particle-velocity', 'sound-intensity', 'sil-db']
    os.chdir(path_acu)
    acoustic_data.to_csv(str('int-09_acu_' + str(timestep) + '.dat'), sep=',')
    print(str('int-09_acu_' + str(timestep) + '.dat done...'))
print("Exiting noise analysis loop...")

print("Script done, exiting.")