import os
path = './data' 
lista = os.listdir(path)

for filename in lista:
    os.rename(filename, filename + ".dat")
