print("Loading Libraries...")
import os, sys
import csv
import platform
import numpy as np
import pandas as pd
import dask.dataframe as dd
import scipy
import sklearn
import matplotlib.pyplot as plt
import flask
import math
import scipy.interpolate as scin
import matplotlib.colors as colors
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
from sklearn import neighbors, datasets
print("Loaded Libraries...")

print("Starting code...")

#PUT Workstation
print("Loading directories..") 
#path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside'
#path_post = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside-post'
path_acu = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside-post/acu'
path_coords = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside-post/coords'
path_plots = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside-post/plots'
#path_signal = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside-post/signal'
#path_fft = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside-post/fft'
print("Loaded directories...")

'''
#Local
print("Loading directories..")
#path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/pside'
#path_post = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/pside-post'
path_acu = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/pside-post/acu'
#path_plots = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/pside-post/plots'
path_rms = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/pside-post/rms'
print("Loaded directories...")
'''

'''
#PLGRID
print("Loading directories..")
#path_data = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/pside'
#path_post = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/pside-post'
path_acu = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/pside-post/acu'
#path_plots = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/pside-post/plots'
path_rms = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/pside-post/rms'
print("Loaded directories...")
'''

print("Loading batch acoustic data...")
os.chdir(path_acu)
batch_data = dd.read_csv('*', delimiter=",", decimal='.',usecols=["nodenumber", "sound-pressure"])
batch_data = batch_data.set_index("nodenumber")
print("Batch data done...")

print("Calculate min and max for plotting range...")
batch_min = pd.DataFrame(batch_data.min().compute())
batch_max = pd.DataFrame(batch_data.max().compute())
spl_min = batch_min.iloc[[0]][0]
#sil_min = batch_min.iloc[[1]][0]
spl_max = batch_max.iloc[[0]][0]
#sil_max = batch_max.iloc[[1]][0]
print("Min and max for plotting range done...")

print("Generating coordinates")
os.chdir(path_coords)
coords = pd.DataFrame(pd.read_csv('int-tip_coords.dat', delimiter=",", header=0, skiprows=0, decimal='.')).set_index('nodenumber')
x = coords['x-coordinate']
y = coords['y-coordinate']
z = coords['z-coordinate']
print("Coordinates done")

print("Starting plotting loop...")
os.chdir(path_acu)
filelist = os.listdir(path_acu)[-1000:]
for file in filelist:
    os.chdir(path_acu)
    timestep = str(os.path.basename(str(file)))[11:-4] #[12:-4] for tip

    data = pd.DataFrame(pd.read_csv('int-tip_acu_83371.dat', delimiter=",", header=0, skiprows=0, decimal='.')).set_index('nodenumber')
    spl = data['sound-pressure']
    spl_db = data['spl-db']
    #sil = data['sound-intensity']
    #sil_db = data['sil-db']

    pressure, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 10), dpi=90)
    spl_plot = ax0.scatter(z, y, c=spl, s=0.5, cmap=plt.cm.bone, norm=colors.SymLogNorm(linthresh=15000, linscale=15000, vmin=spl_min[0], vmax=spl_max[0]))
    pressure.colorbar(spl_plot, ax=ax0)
    ax0.set_title(str('Sound pressure at pside. Time: ' + str(timestep) + ' [Pa]'))
    spldb_plot = ax1.scatter(z, x, c=spl_db, s=0.5, vmin=0, vmax=200, cmap=plt.cm.bone)
    pressure.colorbar(spldb_plot, ax=ax1)
    ax1.set_title(str('SPLdB at pside. Time: ' + str(timestep) + ' [dB]'))
    os.chdir(path_plots)
    plt.savefig(str('pside_spl_t_' + str(timestep) + '.png'))
    plt.close()
'''
    intensity, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 10), dpi=90)
    spl_plot = ax0.scatter(z, x, c=spl, s=0.5, cmap=plt.cm.bone, norm=colors.SymLogNorm(linthresh=15000, linscale=15000, vmin=spl_min[0], vmax=spl_max[0]))
    intensity.colorbar(spl_plot, ax=ax0)
    ax0.set_title(str('Sound pressure at pside. Time: ' + str(timestep) + ' [Pa]'))
    spldb_plot = ax1.scatter(z, x, c=spl_db, s=0.5, vmin=0, vmax=200, cmap=plt.cm.bone)
    intensity.colorbar(spldb_plot, ax=ax1)
    ax1.set_title(str('SPLdB at pside. Time: ' + str(timestep) + ' [dB]'))
    os.chdir(path_plots)
    plt.savefig(str('pside_sil_t_' + str(timestep) + '.png'))
    plt.close()
'''
    print(str(str(timestep) + ' done...'))
print("Exiting plotting loop...")

print("Script done, exiting.")