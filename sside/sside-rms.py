#rms.py
print("Loading Libraries...")
import os
import csv
import platform
import numpy as np
from scipy.fftpack import fft
import pandas as pd
import dask.dataframe as dd
import math
import matplotlib.pyplot as plt
print("Loaded Libraries...")

#PLGRID
print("Loading directories..")
path_acu = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/sside-post/acu'
path_rms = '/net/scratch/people/plgmosieznyj/SRS_v02/results/rms'
print("Loaded directories...")

print("Loading batch data...")
os.chdir(path_acu)
batch_data = dd.read_csv('*1.dat', delimiter=",", decimal='.',usecols=["nodenumber", "sound-pressure"])
batch_data = batch_data.set_index("nodenumber")
print("Batch data done...")

print("Calculating rms...")
#rms = pd.DataFrame(batch_data.groupby('nodenumber').apply(lambda x: np.sqrt(np.mean(np.square(x))), meta={'sound-pressure': 'f8', 'sound-intensity': 'f8'}).compute())
rms = pd.DataFrame(batch_data.groupby('nodenumber').std().compute())
rms['rms_spldb'] = rms['sound-pressure'].apply(lambda x: 20*np.log10(x/0.00002))
#rms['rms_sildb'] = rms['sound-intensity'].apply(lambda x: 10*np.log10(x/1e-12))

os.chdir(path_rms)
rms.to_csv(str('sside-rms.dat'), sep=",")