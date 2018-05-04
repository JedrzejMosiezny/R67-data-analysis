#fft.py
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

print("Starting code...")

#PLGRID
print("Loading directories..")
path_acu = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-05-post/acu'
path_plots = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-05-post/plots'
path_fft = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-05-post/fft'
path_rms = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-05-post/rms'
path_coords = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-05-post/coords'
print("Loaded directories...")

print("Defining functions") 
def FFT_db(x):
    T = 0.050150  # Duration in seconds
    #f0 = 100  # Fundamental frequency
    Fs = 25000  # Sampling frequency

    # Time domain signal
    t = np.arange(0, T*Fs)/Fs
    x = np.asarray(x, np.float)
    N = x.size

    # DFT
    X = np.fft.fft(x)
    X_db = 20*np.log10(2*np.abs(X)/N)
    #f = np.fft.fftfreq(N, 1/Fs)
    #f = np.arange(0, N)*Fs/N
    #return np.concatenate([X, X_db])
    return np.concatenate([X_db])

def FFT_freq(x):
    T = 0.050150  # Duration in seconds
    #T = 0.0001  # Duration in seconds
    #f0 = 100  # Fundamental frequency
    Fs = 25000  # Sampling frequency

    # Time domain signal
    t = np.arange(0, T*Fs)/Fs
    x = np.asarray(x, np.float)
    N = x.size

    # DFT
    #X = np.fft.fft(x)
    #X_db = 20*np.log10(2*np.abs(X)/N)
    f = np.fft.fftfreq(N, 1/Fs)
    #f = np.arange(0, N)*Fs/N
    #return np.concatenate([X, X_db])
    return np.concatenate([f])
print("Functions defined...") 

print("Loading batch data...")
os.chdir(path_acu)
batch_pressure = dd.read_csv('int-05*', delimiter=",", decimal='.',usecols=["nodenumber", "sound-pressure"])
batch_pressure = batch_pressure.set_index("nodenumber")
print("Batch data done...")

print("Calculating FFT...") 
#fft_values = pd.DataFrame(batch_pressure.groupby('nodenumber').apply(lambda x: FFT_values(x), meta=('sound-pressure', 'f8')).compute()).sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True)
fft_db = pd.DataFrame(batch_pressure.groupby('nodenumber').apply(lambda x: FFT_db(x), meta=('sound-pressure', 'f8')).compute()).sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True)
fft_freq = pd.DataFrame(batch_pressure.groupby('nodenumber').apply(lambda x: FFT_freq(x), meta=('sound-pressure', 'f8')).compute()).sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True)
print("FFT Done..") 

print("Creating FFT DataFrame...") 
j = 1
node_DB = fft_db.loc[j].values[0]
node_FREQ = fft_freq.loc[j].values[0]
node_DB_max = np.max(node_DB)
node_DB_deviation = np.divide((np.abs(np.mean(node_DB))) - np.abs(node_DB_max), np.std(node_DB))
node_FREQ_max = node_FREQ[np.flatnonzero(node_DB == np.max(node_DB))][0]
node_fft_max = {'nodenumber': [j], 'node_DB_max': [node_DB_max], 'node_DB_deviation': [node_DB_deviation], 'node_FREQ_max': [node_FREQ_max]}
node_fft_max = pd.DataFrame(data = node_fft_max)
#node_fft_max.columns = ['nodenumber', 'node_DB_max', 'node_DB_deviation', 'node_FREQ_max']
#node_fft_max_i.append(node_fft_max)
print("FFT DataFrame created")

print("Entering FFT Loop...")
nodelist = list(range(2, 38138+1))
for i in nodelist:
    node_DB = fft_db.loc[i].values[0]
    node_FREQ = fft_freq.loc[i].values[0]
    node_DB_max = np.max(node_DB)
    node_DB_deviation = np.divide((np.abs(np.mean(node_DB)) - np.abs(node_DB_max)), np.std(node_DB))
    node_FREQ_max = node_FREQ[np.flatnonzero(node_DB == np.max(node_DB))][0]
    node_fft_max_i = {'nodenumber': [i], 'node_DB_max': [node_DB_max], 'node_DB_deviation': [node_DB_deviation], 'node_FREQ_max': [node_FREQ_max]}
    node_fft_max_i = pd.DataFrame(data = node_fft_max_i)
    #node_fft_max_i.columns = ['nodenumber', 'node_DB_max', 'node_DB_deviation', 'node_FREQ_max']
    node_fft_max = node_fft_max.append(node_fft_max_i, ignore_index=True)
    print(str('Node ' + str(i) + ' done...'))
print("FFT Loop done...")

print("Saving FFT to dataframe...")
node_fft_max.set_index('nodenumber')
os.chdir(path_fft)
node_fft_max.to_csv(str('int-05_fft_max.dat'), sep=",")
print("Dataframe saved...")
print("Script completed...")