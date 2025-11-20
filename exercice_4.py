from typing import TypeVar, Collection

colect = TypeVar("N", dict, list, tuple) 
T = TypeVar("T") 

def fetch_primer_elemento(coleccion: Collection[T]) -> T:
    if isinstance(coleccion, dict):
        return coleccion["primero"]
    elif isinstance(coleccion, (list, tuple)):
        return coleccion[0]
    else:
        raise Exception()
    
lista = [1,2,3] #TypeError, KeyError
print(lista[0])

# Better
def fetch_primer_elemento_2(coleccion: Collection[T]) -> T:
    try:
        return coleccion[0]
    except KeyError:
        return coleccion["primero"]
            
    
lista = [1,2,3] #TypeError, KeyError
print(fetch_primer_elemento_2(lista))
