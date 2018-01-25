# point timestep transposition
print("Loading Libraries...")
import os
import csv
import platform
import numpy as np
import pandas as pd
import dask.dataframe as dd
import math
import matplotlib.pyplot as plt
print("Loaded Libraries...")

'''
#Local
print("Loading directories..")
#path_post = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post'
path_acu = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/acu'
#path_plots = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/plots'
path_signal = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/signal'
#path_rms = 'C:/Users/JMosiezny/Documents/01_PUT/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/rms'
print("Loaded directories...")
'''
#PUT Workstation
print("Loading directories..") 
#path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01'
#path_post = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post'
path_acu = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/acu'
#path_plots = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/plots'
path_signal = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/signal'
#path_rms = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/rms'
print("Loaded directories...")

'''
print("Loading directories..")
path_data = '/net/archive/groups/plggcfdp/R67_fluent/SRS_v02/noise-data/int-01'
#path_post = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01-post'
path_acu = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01-post/acu'
#path_plots = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01-post/plots'
path_signal = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01-post/signal'
#path_rms = '/net/scratch/people/plgmosieznyj/SRS_v02/noise-data/int-01-post/rms'
print("Loaded directories...")
'''

print("Creating outer loop node list")
#nodelist = list(range(1, 100+1))
nodelist = list(range(1, 38138+1))[len(os.listdir(path_signal)):]
print("Done")
print("Creating inner loop file list")
filelist = sorted(os.listdir(path_acu))
print("Done")

print("Entering outer loop")
for i in nodelist:
    print("Outer Loop number " + str(i))
    os.chdir(path_acu)
    node_ts = []
    for file in filelist:
        print("Inner Loop number " + str(file))
        node = pd.read_csv(file, delimiter=",", usecols = ["sound-pressure", "sound-intensity"], skiprows=(range(1, i)), nrows=1, decimal='.')
        node_ts.append(node)
    node_ts = pd.concat(node_ts, axis=0, ignore_index=True)
    os.chdir(path_signal)
    node_ts.to_csv(str('int-01_acu_node_' + str(i) +'.dat'), sep=",")