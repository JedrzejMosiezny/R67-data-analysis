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

print("Loading directories..")
#path_data = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-tip'
#path_post = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-tip-post'
path_acu = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-tip-post/acu'
path_plots = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-tip-post/plots' #ścieżka do katalogu z interesującymi nas plikami
print("Loaded directories...")

print("Loading batch acoustic data...")
os.chdir(path_acu)
batch_data = dd.read_csv('*.dat', sep=',', decimal='.')
print("Batch data done...")

print("Calculate min and max for plotting range...")
minima = pd.DataFrame(batch_data.groupby('nodenumber').min().compute())
maxima = pd.DataFrame(batch_data.groupby('nodenumber').max().compute())
min_spl=np.amin(minima['sound-pressure'])
min_dbl=np.amin(minima['spl-db'])
max_spl=np.amax(maxima['sound-pressure'])
max_dbl=np.amax(maxima['spl-db'])
print("Min and max for plotting range done...")

print("Starting plotting loop...")
os.chdir(path_acu)
filelist = os.listdir(path_acu)
for file in filelist:
    timestep = str(os.path.basename(str(file)))[11:-4] #[12:-4] for tip
    os.chdir(path_acu)
    acu = pd.read_csv(file, sep=',', decimal='.', header=0)
    x = acu['x-coordinate']
    y = acu['y-coordinate']
    z = acu['z-coordinate']
    sound_pressure = acu['sound-pressure']
    spl_db = acu['spl-db']
    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 10), dpi=120)
    spl_plot = ax0.scatter(z, x, c=sound_pressure, s=2, cmap=plt.cm.bone, norm=colors.SymLogNorm(linthresh=0.3*max(abs(max_spl), abs(min_spl)), linscale=0.3*max(abs(max_spl), abs(min_spl)), vmin=min_spl, vmax=max_spl))
    fig.colorbar(spl_plot, ax=ax0, extend=max_spl)
    ax0.set_title(str('Sound pressure. int-tip. Time: ' + str(timestep)))
    dbl_plot = ax1.scatter(z, x, c=spl_db, s=2, vmin=min_dbl, vmax=max_dbl, cmap=plt.cm.bone)
    fig.colorbar(dbl_plot, ax=ax1, extend=max_dbl)
    ax1.set_title(str('dB level. int-tip. Time: ' + str(timestep)))
    os.chdir(path_plots)
    plt.savefig(str('int-tip_acu_t_' + str(timestep) + '.png'))
    plt.close()
    print(str('int-tip_acu_t_' + str(timestep) + '.png done...'))
print("Exiting plotting loop...")

print("Script done, exiting.")