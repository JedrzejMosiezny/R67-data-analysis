#fft.py
print("Loading Libraries...")
import os
import numpy as np
# from scipy.fftpack import fft
import pandas as pd
print("Loaded Libraries...")

print("Starting code...")

#PLGRID
print("Loading directories..")
path_acu = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/sside-post/acu'
path_fft = '/net/scratch/people/plgmosieznyj/SRS_v02/fft'
print("Loaded directories...")
'''
print("Loading directories..")
path_acu = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/sside-post/acu'
path_fft = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/15_results/fft'
print("Loaded directories...")
'''
print("Getting filelist...")
os.chdir(path_acu)
filelist = sorted(os.listdir(path_acu))[0::10]

print("Starting batch loop...")
batch_data = pd.DataFrame()
for file in filelist:
    batch_data[file] = pd.read_csv(file).set_index('nodenumber')['sound-pressure']
    print(str(file) + " done...")

print("Calculating FFT...")
fft_data = batch_data.apply(lambda x: np.fft.fft(x), axis=1)

print("Saving FFT to dataframe...")
#fft_data.set_index('nodenumber')
os.chdir(path_fft)
fft_data.to_csv('sside-fft.csv', sep=',')
print("Dataframe saved...")
print("Script completed...")