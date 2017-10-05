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
path_data = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-tip'
path_post = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-tip-post'
path_acu = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-tip-post/acu'
path_plots = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-tip-post/plots'
print("Loaded directories...")

print("Loading batch acoustic data...")
os.chdir(path_acu)
batch_data = dd.read_csv('*.dat', sep=',', decimal='.')
print("Batch data done...")

print("Calculate min, max, std for plotting range...")
minima = pd.DataFrame(batch_data.groupby('nodenumber').min().compute())
maxima = pd.DataFrame(batch_data.groupby('nodenumber').max().compute())
min_spl=np.amin(minima['sound-pressure'])
min_dbl=np.amin(minima['db-level'])
max_spl=np.amax(maxima['sound-pressure'])
max_dbl=np.amax(maxima['db-level'])
std_devs = pd.DataFrame(batch_data.groupby('nodenumber').max().compute()) # to nie RMS, poprawić
min_splrms=np.amin(std_devs['sound-pressure'])
min_dblrms=np.amin(std_devs['db-level'])
max_splrms=np.amax(std_devs['sound-pressure'])
max_dblrms=np.amax(std_devs['db-level'])
print("Min, max, std for plotting range done...")

print("Prepare to plot RMS values...")
x = std_devs['x-coordinate']
y = std_devs['y-coordinate']
z = std_devs['z-coordinate']
spl = std_devs['sound-pressure']
dbl = std_devs['db-level']
print("RMS values prep done...")

print("Plotting RMS values...")
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 10), dpi=300)
spl_plot = ax0.scatter(z, x, c=spl, s=0.1, cmap=plt.cm.bone, norm=colors.SymLogNorm(linthresh=4000, linscale=4000, vmin=1000, vmax=12000))
fig.colorbar(spl_plot, ax=ax0)
ax0.set_title("Sound pressure@int-tip. RMS values [Pa]")
dbl_plot = ax1.scatter(z, x, c=dbl, s=0.1, vmin=min_dblrms, vmax=max_dblrms, cmap=plt.cm.bone)
fig.colorbar(dbl_plot, ax=ax1)
ax1.set_title("dB level@int-tip. RMS values [dB]")
os.chdir(path_plots)
plt.savefig(str('int-tip_acu_RMS.png'))
print("Plotting RMS done...")

print("Starting plotting loop...")
os.chdir(path_acu)
filelist = os.listdir(path_acu)
for file in filelist:
    timestep = str(os.path.basename(str(file)))[12:-4]
    os.chdir(path_acu)
    acu = pd.read_csv(file, sep=',', decimal='.', header=0)
    x = acu['x-coordinate']
    y = acu['y-coordinate']
    z = acu['z-coordinate']
    spl = acu['sound-pressure']
    dbl = acu['db-level']
    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 10), dpi=300)
    spl_plot = ax0.scatter(z, x, c=spl, s=2, cmap=plt.cm.bone, norm=colors.SymLogNorm(linthresh=5000, linscale=5000, vmin=-15000, vmax=12000))
    fig.colorbar(spl_plot, ax=ax0)
    ax0.set_title(str('Sound pressure. int-tip. Time: ' + str(timestep)))
    dbl_plot = ax1.scatter(z, x, c=dbl, s=2, vmin=min_dbl, vmax=max_dbl, cmap=plt.cm.bone)
    fig.colorbar(dbl_plot, ax=ax1)
    ax1.set_title(str('dB level. int-tip. Time: ' + str(timestep)))
    os.chdir(path_plots)
    plt.savefig(str('int-tip_acu_t_' + str(timestep) + '.png'))
    plt.close()
    print(str('int-tip_acu_t_' + str(timestep) + '.png done...'))
print("Exiting plotting loop...")

print("Script done, exiting.")