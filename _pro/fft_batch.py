#batch_fft.py

import os
import csv
import platform
import numpy as np
from scipy.fftpack import fft
import pandas as pd
import dask.dataframe as dd
import math

def folder_fft(folder)
    folder = str(folder)

    '''
    #PUT Workstation
    print("Loading directories..") 
    #path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01'
    #path_post = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post'
    path_acu = 'D:/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/acu'
    #path_plots = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/plots'
    path_fft = 'D:/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/fft'
    #path_rms = 'D:/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/rms'
    print("Loaded directories...")
    '''

    '''
    #Local
    print("Loading directories..")
    #path_data = 'int-01'
    #path_post = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post'
    path_acu = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/acu'
    #path_plots = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/plots'
    path_fft = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/fft'
    print("Loaded directories...")
    '''
    
    #PLGRID
    print("Loading directories..")
    #path_data = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01'
    #path_post = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01-post'
    #path_plots = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01-post/plots'
    path_acu = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/' + folder + '/acu'
    path_fft = '/net/scratch/people/plgmosieznyj/SRS_v02/results/fft'
    print("Loaded directories...")
    
    print("Loading batch data...")
    os.chdir(path_acu)
    batch_pressure = dd.read_csv('*', delimiter=",", decimal='.',usecols=["nodenumber", "sound-pressure"])
    batch_pressure = batch_pressure.set_index("nodenumber")
    print("Batch data done...")

    print("Calculating FFT...") 
    fft_batch = batch_pressure.groupby('nodenumber').apply(lambda x: fft(x), meta=('node-fft-series', 'f8')).compute()
    print("FFT Done..") 

    print("Saving FFT to dataframe...")
    os.chdir(path_fft)
    fft_batch.to_csv(str(folder + '_fft_batch.dat'), sep=",")
    print("Dataframe saved...")
    
print("Starting script")
folder_fft('int-01-post')
folder_fft('int-02-post')
folder_fft('int-03-post')
folder_fft('int-04-post')
folder_fft('int-05-post')
folder_fft('int-06-post')
folder_fft('int-07-post')
folder_fft('int-08-post')
folder_fft('int-09-post')
folder_fft('int-10-post')
folder_fft('int-11-post')
folder_fft('int-12-post')
folder_fft('int-tip-post')
folder_fft('pside-post')
folder_fft('sside-post')
folder_fft('tip-post')
folder_fft('lead-post')
folder_fft('trail-post')
print("Script completed...")