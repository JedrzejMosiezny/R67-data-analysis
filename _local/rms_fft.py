#rms_fft.py
print("Loading Libraries...")
import os
import csv
import platform
import numpy as np
import pandas as pd
import dask.dataframe as dd
import math
print("Loaded Libraries...")

print("Starting code...")

print("Loading directories..")
#path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01'
#path_post = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post'
path_acu = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/acu'
#path_plots = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/plots'
path_rms = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/rms'
print("Loaded directories...")

'''
print("Loading directories..")
#path_data = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/int-01'
#path_post = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/int-01-post'
path_acu = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/int-01-post/acu'
#path_plots = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/int-01-post/plots'
path_rms = '/net/scratch/people/plgmosieznyj/SRS-v02/noise-data/int-01-post/rms'
print("Loaded directories...")
'''

print("Loading batch acoustic data...")
os.chdir(path_acu)
batch_data = dd.read_csv('*.dat', sep=',', decimal='.')
print("Batch data done...")

std_devs = pd.DataFrame(batch_data.groupby('nodenumber').std().compute())
os.chdir(path_rms)
std_devs.to_csv(str('int-01_RMS.dat'), sep=',')

fft = np.fft.fft(batch_data, n=None, axis=-1, norm=None) #chyba nie ruszy
fft.to_csv(str('int-01_FFT.dat'), sep=',')

'''
print("Prepare to plot RMS values...")
min_splrms=np.amin(std_devs['sound-pressure'])
min_dblrms=np.amin(std_devs['spl-db'])
max_splrms=np.amax(std_devs['sound-pressure'])
max_dblrms=np.amax(std_devs['spl-db'])
x = std_devs['x-coordinate']
y = std_devs['y-coordinate']
z = std_devs['z-coordinate']
spl = std_devs['sound-pressure']
dbl = std_devs['spl-db']
print("RMS values prep done...")


print("Plotting RMS values...")
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 10), dpi=300)
spl_plot = ax0.scatter(z, x, c=spl, s=0.1, cmap=plt.cm.bone, norm=colors.SymLogNorm(linthresh=0.3*max(abs(max_splrms), abs(min_splrms)), linscale=0.3*max(abs(max_splrms), abs(min_splrms)), vmin=min_splrms, vmax=max_splrms))
fig.colorbar(spl_plot, ax=ax0)
ax0.set_title("Sound pressure@int-tip. RMS values [Pa]")
dbl_plot = ax1.scatter(z, x, c=dbl, s=0.1, vmin=min_dblrms, vmax=max_dblrms, cmap=plt.cm.bone)
fig.colorbar(dbl_plot, ax=ax1)
ax1.set_title("dB level@int-01. RMS values [dB]")
os.chdir(path_plots)
plt.savefig(str('int-01_acu_RMS.png'))
print("Plotting RMS done...")
'''