print("Loading Libraries...")
import os, sys
import csv
import platform
import numpy as np
import pandas as pd
import dask.dataframe as dd

def coords(folder):
    #PUT Workstation
    print("Loading directories..") 
    #path_data = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01'
    #path_post = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post'
    path_acu = 'D:/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/acu'
    #path_plots = 'D:/01_DOKTORAT/13_PLGRID/noise-data/int-01-post/plots'
    #path_fft = 'D:/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/fft'
    #path_rms = 'D:/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/rms'
    path_coords = 'D:/01_DOKTORAT/13_PLGRID/noise-data/' + folder + '/coords'
    print("Loaded directories...")

    print("Generating coords...")
    os.chdir(path_acu)
    filelist = os.listdir(path_acu)
    first = filelist[0]
    base_file = pd.read_csv(first, delimiter=",", decimal='.').set_index('nodenumber')
    coords = base_file.iloc[:, :3]
    os.chdir(path_coords)
    coords.to_csv(str('int-01_coords.dat'), sep=',')

    print("Starting coords loop...")
    os.chdir(path_acu)
    for file in filelist:
        base_file = pd.read_csv(file, delimiter=",", decimal='.').set_index('nodenumber')
        data = base_file.iloc[:, 3:]
        data.to_csv(str(file), sep=',')
    print("Coords done")

#coords('int-01-post')
#coords('int-02-post')
#coords('int-03-post')
#coords('int-04-post')
#coords('int-05-post')
#coords('int-06-post')
#coords('int-07-post')
#coords('int-08-post')
#coords('int-09-post')
#coords('int-10-post')
#coords('int-11-post')
#coords('int-12-post')
#coords('int-tip-post')

coords('pside-post')
coords('sside-post')
coords('tip-post')
coords('lead-post')
coords('trail-post')