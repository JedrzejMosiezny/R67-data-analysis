import os, sys
import pandas as pd
import numpy as np
import csv

path = str(input('Podaj ścieżkę do katalogu z plikami: ')) #Tutaj można skopiować ścieżkę
result_file = input('Podaj nazwę pliku wyjściowego: ')



#path = 'C:/Users/HP/Dysk Google/ICS/reburning/badania/Wyniki/TXT/Wyniki/Reburning_29_05/dobre/' #ścieżka do katalogu z interesującymi nas plikami
lista = os.listdir(path)            #Tworzy listę z plików w danym katalogu
#print(lista)                        #Wyświetla listę plików

plik = []
wartosc_co = []
wartosc_no = []
wartosc_o2 = []
for file in lista:
         data_co = pd.read_csv(file, sep='\t', usecols=['Untitled 14'], skiprows=22, decimal=',')
         last_co = data_co.tail(15)
         avg_co = last_co.mean()
         avg_co = avg_co.values

         data_no = pd.read_csv(file, sep='\t', usecols=['Untitled 17'], skiprows=22, decimal=',')
         last_no = data_no.tail(15)
         avg_no = last_no.mean()
         avg_no = avg_no.values

         data_o2 = pd.read_csv(file, sep='\t', usecols=['Untitled 16'], skiprows=22, decimal=',')
         last_o2 = data_o2.tail(15)
         avg_o2 = last_o2.mean()
         avg_o2 = avg_o2.values

         plik.append(file)
         wartosc_co.append(avg_co)
         wartosc_no.append(avg_no)
         wartosc_o2.append(avg_o2)

#print(plik, wartosc_co, wartosc_no, wartosc_o2)               #Opcjonalnie można wyświetlić listy
wyniki = list(zip(plik, wartosc_co, wartosc_no, wartosc_o2))   #Łączy listy w jeden plik
#print(wyniki)
df = pd.DataFrame(data = wyniki, columns=['Nazwa pliku', 'Emisja CO', 'Emisja NO', 'O2'])                   #Tworzy DataFrame (nie do końca to rozumiem, muszę zgłębić)
df.to_csv(result_file+'.csv', index=False, header=['Nazwa pliku', 'Emisja CO', 'Emisja NO', 'O2'])          #Zapisuje do pliku CSV

input('\n\nAby zakończyć program, naciśnij klawisz Enter.')