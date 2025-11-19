# Decorators
from typing import TypeVar
from time import time, sleep

Numero = TypeVar("Numero", int, float)

def avisar(function: callable) -> callable:
    def wrapper(n1: Numero,n2: Numero) -> Numero:
        start = time()
        print(f"He entrado en mi decorador: {function.__name__}")
        end = time()
        res = function(n1,n2)
        print(f"Ha tardado: {end-start}")
        return res
    return wrapper

@avisar
def sumar(n1, n2):
    return n1+n2

@avisar
def restar(n1, n2):
    return n1-n2

# print(sumar(10,20))
# print(restar(10,20))

# Ejercicio decorador cache

T = TypeVar("t")

def cache(function: callable) -> callable:
    data: dict = {}
    
    def wrapper(*args: T, **kwargs: T) -> T:
        print(f"He entrado en mi decorador: {function.__name__}")
        key = (args)
        if key in data:
            print(f"Resultado en cache: {data[key]}")
            return data[key]
        
        res = function(*args)
        data[key] = res
        return res
    return wrapper

@cache
def sumar_2(n1, n2):
    return n1+n2

@cache
def decir_hola(nombre):
    return nombre


print(sumar_2(10,20))
print(sumar_2(10,20))
print(sumar_2(12,30))

print(decir_hola("Hola"))
print(decir_hola("Hola"))



def login(role: str) -> callable:
    def decorador(funcion: callable) -> callable:
        def wrapper(*args, **kwargs) -> any:
            print(f"El rol del usuario es: {role}")
            print(f"He entrado en mi funcion: {funcion.__name__}")
            return funcion(*args, **kwargs)
        return wrapper
    return decorador

@login("admin")
def conexion_bd(usuario: str, *, valido: bool):
    if valido:
        print(f"El usuario {usuario} ha accedido a base de datos")
        
conexion_bd("joaquin", valido=True)