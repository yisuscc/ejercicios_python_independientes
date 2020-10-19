'''
Created on 15 oct. 2020

@author: jesus carrascosa carro
'''
from Audiencias import *
fichero = ('../data/GH.csv')
audiencias = lee_audiencias(fichero)
temporada = 1

#tests
print(lee_audiencias(fichero))
print(calcula_ediciones(audiencias))
print(calcula_ediciones_version_ejecicio(audiencias))
print(filtra_por_temporadas(audiencias,temporada))