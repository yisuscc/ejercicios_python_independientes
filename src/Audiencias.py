'''
Created on 15 oct. 2020

@author: jesus carrascosa carro
'''
import csv
import statistics
from matplotlib import pyplot as plt


# 1ee_audiencias
'''
el fichero contiene una columna correspondiente al nuumero de temporada 
y al porcentaje de la audiencia. 
'''

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

#2 funcion calcula ediciones
def calcula_ediciones(audiencias):
    '''
    Dada una lista de tuplas con las audiencias, calcula el conjunto de ediciones presentes
    '''
    '''
     1 de la lista de audiencias se coge las temporadas 
     2 las metemos en un tipo que no admita repeticiones en este caso un conjunto (mutable,no admite repetición, NO ORDENADO, llaves)
     3 los pasamos a una lista  y lo ordenamos con el objeto .sort()
     '''
    ediciones = {t for t, s  in audiencias} #de una lista con tuplas formadas por dos elementos e y i  nos quedamos solo con e y i mediante un bucle.
    #lo convertimos a  unalista
    ediciones = list(ediciones)
    ediciones.sort()
    return ediciones 

# versión del ejercicio, para comparar y averiguar  por que no funciona mi versíon si el cambio es mínimo
# al parecerr no se puede integrar el sort en el return
def calcula_ediciones_version_ejecicio(audiencias):
  
    # Calculamos el conjunto de ediciones presentes
    ediciones = {e for e, _ in audiencias}
    # Convertimos el conjunto en lista para poder ordenarlo
    ediciones = list(ediciones)
    # Ordenamos las ediciones
    ediciones.sort()
    return ediciones

def filtra_por_temporadas(audiencias,temporada):
   # no sirve porque no es una namedtuple
   # res = [s for temporada, s in audiencias if audiencias.temporada == temporada]
   res = [(t,s) for t,s in audiencias if t == temporada]
   return res 

def medias_por_ediciones(audiencias):
    '''
    1º Averiguamos cuantas ediciones tenemos.
    2º Hscemos un bucle que según la  edición nos lo clasifique el share en una lista.
    3º Calculamos los elementos de la lista y los metemos en una variable auxiliar.
    4ªSumamos todos lo valores de la lista y los metemos en ortra variable auxiliar.
    5ºHacemos la media y la metemos en una variable aux.
    6º Metemos un diccionario  siendo la clave la edición y el valor la media
    '''
    medias = dict
    temporada= calcula_ediciones(audiencias)
    for temporada in temporada:
        '''
         No entiendo muy bien porqué me da error
        temp_share = filtra_por_temporadas(audiencias, temporada)
        share = [s for e,s in temp_share]
        '''
        share = [s for e, s in audiencias if temporada == e]
        num_share = len(share)
        media = sum(share)/num_share
        media =float(media)
        medias[temporada]= media
    return medias
    



         
 