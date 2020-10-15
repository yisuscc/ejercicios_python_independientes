'''
Created on 15 oct. 2020

@author: jesus carrascosa carro
'''
from Audiencias import *
fichero = ('../data/GH.csv')
audiencias = lee_audiencias(fichero)
print(calcula_ediciones(audiencias))