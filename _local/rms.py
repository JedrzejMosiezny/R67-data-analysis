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

#PUT Workstation
print("Loading directories..") 
#path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01'
#path_post = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post'
path_acu = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/acu'
#path_plots = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/plots'
#path_signal = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/signal'
path_fft = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/fft'
path_rms = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/rms'
print("Loaded directories...")

'''
#Local
print("Loading directories..")
#path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01'
#path_post = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post'
path_acu = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/acu'
#path_plots = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/plots'
path_rms = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/rms'
print("Loaded directories...")
'''

'''
#PLGRID
print("Loading directories..")
#path_data = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01'
#path_post = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01-post'
path_acu = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01-post/acu'
#path_plots = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01-post/plots'
path_rms = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01-post/rms'
print("Loaded directories...")
'''

print("Loading batch data...")
os.chdir(path_acu)
batch_data = dd.read_csv('int-01*', delimiter=",", decimal='.',usecols=["nodenumber", "sound-pressure", "sound-intensity"])
batch_data = batch_data.set_index("nodenumber")
print("Batch data done...")

rms = pd.DataFrame(batch_data.groupby('nodenumber').apply(lambda x: np.sqrt(np.mean(x**2)), meta={'sound-pressure': 'f8', 'sound-intensity': 'f8'}).compute())
rms['rms_spldb'] = rms['sound-pressure'].apply(lambda x: 20*np.log10(x/0.00002))
rms['rms_sildb'] = rms['sound-intensity'].apply(lambda x: 20*np.log10(x/0.00002))

os.chdir(path_rms)
rms.to_csv(str('int-01_rms.dat'), sep=",")