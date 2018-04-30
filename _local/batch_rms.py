#batch_rms.py

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

def folder_rms(folder)
    #PUT Workstation
    print("Loading directories..") 
    #path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01'
    #path_post = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post'
    path_acu = 'D:/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/acu'
    #path_plots = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/plots'
    #path_fft = 'D:/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/fft'
    path_fft = 'D:/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/rms'
    print("Loaded directories...")

    '''
    #Local
    print("Loading directories..")
    #path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01'
    #path_post = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post'
    path_acu = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/acu'
    #path_plots = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/plots'
    path_fft = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/fft'
    print("Loaded directories...")
    '''

    print("Loading batch data...")
    os.chdir(path_acu)
    batch_data = dd.read_csv('int-01*', delimiter=",", decimal='.',usecols=["nodenumber", "sound-pressure", "sound-intensity"])
    batch_data = batch_data.set_index("nodenumber")
    print("Batch data done...")

    print("Calculating RMS...")
    rms = pd.DataFrame(batch_data.groupby('nodenumber').apply(lambda x: np.sqrt(np.mean(x**2)), meta={'sound-pressure': 'f8', 'sound-intensity': 'f8'}).compute())
    rms['rms_spldb'] = rms['sound-pressure'].apply(lambda x: 20*np.log10(x/0.00002))
    rms['rms_sildb'] = rms['sound-intensity'].apply(lambda x: 20*np.log10(x/0.00002))
    print("RMS done...")


    os.chdir(path_rms)
    rms.to_csv(str('int-01_rms.dat'), sep=",")
    print("RMS saved...")

print("Starting script")

folder_rms('int-01-post')
folder_rms('int-02-post')
folder_rms('int-03-post')
folder_rms('int-04-post')
folder_rms('int-05-post')
folder_rms('int-06-post')
folder_rms('int-07-post')
folder_rms('int-08-post')
folder_rms('int-09-post')
folder_rms('int-10-post')
folder_rms('int-11-post')
folder_rms('int-12-post')
folder_rms('int-tip-post')
folder_rms('pside-post')
folder_rms('sside-post')
folder_rms('tip-post')
folder_rms('lead-post')
folder_rms('trail-post')

print("Script completed...")