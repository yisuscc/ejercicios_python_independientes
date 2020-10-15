'''
Created on 15 oct. 2020

@author: jesus
'''
import csv
import statistics
from matplotlib import pyplot as plt


# 1ee_audiencias
'''
el fichero contiene una columna correspondiente al nuumero de temporada 
y al porcentaje de la audiencia. 
'''
fichero = ('../data/GH.csv')
def lee_audiencias(fichero):
    '''
    Nos piden que hagamos una lista(corchetes y mutable) con los porcentajes del share, tenemos que separar los datos, que están divididos con comas
    '''
    audiencias = [] 
    with open (fichero,'r',encoding='utf-8') as f: 
        # hay que ir línea por línea. las lineas son f
        for e in f:
            #separarmos los elementos entre comas
            temporada, share = e.split(',')
            
            temporada = int(temporada)
            share = float(share)
            
            #yo habia entendido una lista con solo el share , y no una lista de tuplas.
             
            temp_y_share = (temporada, share) 
            audiencias.append(temp_y_share)
    return audiencias
         
 