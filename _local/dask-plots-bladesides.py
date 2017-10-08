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
#path_data = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/pside'
#ath_post = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/pside-post'
path_acu = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/pside-post/acu'
path_spl_plots = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/pside-post/plots/spl'
path_dbl_plots = 'D:/01_Dokumenty/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/pside-post/plots/dbl'
print("Loaded directories...")

print("Loading batch acoustic data...")
os.chdir(path_acu)
batch_data = dd.read_csv('*.dat', sep=',', decimal='.')
print("Batch data done...")

print("Calculate min and max for plotting range...")
minima = pd.DataFrame(batch_data.groupby('nodenumber').min().compute())
maxima = pd.DataFrame(batch_data.groupby('nodenumber').max().compute())
min_spl=np.amin(minima['sound-pressure'])
min_dbl=np.amin(minima['db-level'])
max_spl=np.amax(maxima['sound-pressure'])
max_dbl=np.amax(maxima['db-level'])
print("Min and max for plotting range done...")

print("Starting plotting loop...")
os.chdir(path_acu)
filelist = os.listdir(path_acu)
for file in filelist:
    timestep = str(os.path.basename(str(file)))[10:-4]
    os.chdir(path_acu)
    acu = pd.read_csv(file, sep=',', decimal='.', header=0)
    x = acu['x-coordinate']
    y = acu['y-coordinate']
    z = acu['z-coordinate']
    spl = acu['sound-pressure']
    dbl = acu['db-level']
    #fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(6, 12), dpi=120)
    #pressure
    plt.figure(figsize=(5,7))
    plt.scatter(z, y, c=spl, s=2, cmap=plt.cm.bone, norm=colors.SymLogNorm(linthresh=0.3*max(abs(max_spl), abs(min_spl)), linscale=0.3*max(abs(max_spl), abs(min_spl)), vmin=min_spl, vmax=max_spl))
    plt.colorbar()
    #plt.set_title(str('Sound pressure@pside. Time: ' + str(timestep)))
    os.chdir(path_spl_plots)
    plt.savefig(str('pside_spl_t_' + str(timestep) + '.png'))
    plt.close()
    print(str('pside_spl_t_' + str(timestep) + '.png done...'))
    #density
    plt.figure(figsize=(5,7))
    plt.scatter(z, y, c=dbl, s=2, vmin=min_dbl, vmax=max_dbl, cmap=plt.cm.bone)
    plt.colorbar()
    #plt.set_title(str('dB level@pside. Time: ' + str(timestep)))
    os.chdir(path_dbl_plots)
    plt.savefig(str('pside_dbl_t_' + str(timestep) + '.png'))
    plt.close()
    print(str('pside_dbl_t_' + str(timestep) + '.png done...'))
print("Exiting plotting loop...")
'''
print("Starting plotting loop...")
os.chdir(path_acu)
filelist = os.listdir(path_acu)
for file in filelist:
    timestep = str(os.path.basename(str(file)))[10:-4]
    os.chdir(path_acu)
    acu = pd.read_csv(file, sep=',', decimal='.', header=0)
    x = acu['x-coordinate']
    y = acu['y-coordinate']
    z = acu['z-coordinate']
    spl = acu['sound-pressure']
    dbl = acu['db-level']
    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(6, 12), dpi=120)
    spl_plot = ax0.scatter(z, y, c=spl, s=2, cmap=plt.cm.bone, norm=colors.SymLogNorm(linthresh=0.3*max(abs(max_spl), abs(min_spl)), linscale=0.3*max(abs(max_spl), abs(min_spl)), vmin=min_spl, vmax=max_spl))
    fig.colorbar(spl_plot, ax=ax0)
    ax0.set_title(str('Sound pressure@pside. Time: ' + str(timestep)))
    dbl_plot = ax1.scatter(z, y, c=dbl, s=2, vmin=min_dbl, vmax=max_dbl, cmap=plt.cm.bone)
    fig.colorbar(dbl_plot, ax=ax1)
    ax1.set_title(str('dB level@pside. Time: ' + str(timestep)))
    os.chdir(path_plots)
    plt.savefig(str('pside_acu_t_' + str(timestep) + '.png'))
    plt.close()
    print(str('pside_acu_t_' + str(timestep) + '.png done...'))
print("Exiting plotting loop...")
'''
print("Script done, exiting.")