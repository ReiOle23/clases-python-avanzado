# arquitectura de software 
# metrica de seguridad y del tiempo cuando tengas que utilizar un software de terceros o crear uno tuyo
# Necessitamos tiempo que tenemos, coste maximo, latencia minima, numero de datos, etc.
# Primero requerimientos de disseño, no tener en cuenta tecnologia que conocemos
# Al tener requerimientos hechos, luego decidimos tecnologia
# Profundidad tecnica, experto en algo
# En arquitectura es mejor saber de todo pero no hace falta ser experto
# primer ley de oro: todo depende 
# segunda ley: el porque es mas importante que el como
# tercera ley de conway: las arquitecturas son copias de la estructura que tiene la empresa


# medir eficiencia
# inicio = time()
# duracion = time() - inicio
# 1/duracion
from time import time
def fitnes_rendimiento(function):
    inicio = time()
    for _ in range(10_000_000):
        function(1,1)
    duracion = time() - inicio
    return 1/duracion

def fitnes_precision(function):
    pruebas = [
        (1,2,3),
        (-1,0,-1),
        (10,-4,6)
    ]
    aciertos = 0
    for n1,n2,resultado in pruebas:
        if function(n1,n2)==resultado:
            aciertos += 1
    return aciertos / len(pruebas)
