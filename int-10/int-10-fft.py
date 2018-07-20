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
#import matplotlib.pyplot as plt
print("Loaded Libraries...")

print("Starting code...")

'''
#PUT Workstation
print("Loading directories..") 
#path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-10'
#path_post = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-10-post'
path_acu = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-10-post/acu'
#path_plots = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-10-post/plots'
#path_signal = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-10-post/signal'
path_fft = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-10-post/fft'
print("Loaded directories...")
'''
'''
#Local
print("Loading directories..")
#path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-10'
#path_post = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-10-post'
path_acu = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-10-post/acu'
#path_plots = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-10-post/plots'
path_rms = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-10-post/rms'
print("Loaded directories...")
'''
#PLGRID
print("Loading directories..")
#path_data = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-10'
#path_post = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-10-post'
path_acu = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-10-post/acu'
#path_plots = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-10-post/plots'
path_fft = '/net/scratch/people/plgmosieznyj/SRS_v02/results/fft'
print("Loaded directories...")

print("Loading batch data...")
os.chdir(path_acu)
batch_pressure = dd.read_csv('*1.dat', delimiter=",", decimal='.',usecols=["nodenumber", "sound-pressure"])
batch_pressure = batch_pressure.set_index("nodenumber")
print("Batch data done...")

print("Calculating FFT...") 
batch_fft = batch_pressure.groupby('nodenumber').apply(lambda x: fft(x), meta=('node-fourier-series', 'f8')).compute()
print("FFT Done..") 

print("Saving FFT to dataframe...")
#node_fft_max.set_index('nodenumber')
os.chdir(path_fft)
batch_fft.to_csv(str('int-10_fft.dat'), sep=",")
print("Dataframe saved...")
print("Script completed...")