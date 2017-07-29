import pandas as pd
import os
path = '/data/'
os.chdir(path)
df = pd.read_csv('asdp_data-0001.dat', sep='\s+', header=0, usecols=["pressure"], dtype=str, skiprows=None, decimal='.')

print(df)