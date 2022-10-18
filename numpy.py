import numpy as np
my_data = np.getfromtxt( 'poligono_de_medellin.csv' , delimiter=' ; ' )
my_data = np.getfromtxt( 'calles_de_medellin_con_acoso.csv' , delimiter=' ; ' )

with open("calles_de_medellin_con_acoso.csv") as archivo:
   cadenaDeCaracteres = archivo.read( )

print(cadenaDeCaracteres)


with open("calles_de_medellin_con_acoso.csv") as archivo:
   listaDeLineasDondeCadaLineaEsUnaCadena = archivo.readlines( )

print (listaDeLineasDondeCadaLineaEsUnaCadena)

 
 
