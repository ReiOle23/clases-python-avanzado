# py Generics
from typing import TypeVar

# alias de tipo
T = TypeVar("T") # generic

def the_same(something: T) -> T:
    return something

def first_element(lista: list[T]) -> T:
    return lista[0]

def last_element(tuple: tuple[T]) -> T:
    return tuple[-1]

def dato(dato: T) -> tuple[T, T]:
    return dato, dato

def validacion(dato: T, validacion: bool) -> tuple[T, bool]:
    return dato, True if validacion else dato

Numero = TypeVar("Numero", int, float) # generic only numbers
def sumar(n1: Numero, n2: Numero) -> Numero:
    return n1 + n2

my_iterable = TypeVar("my_iterable", list, str, tuple, dict)
def check_empty(data: my_iterable) -> bool:
    return False if len(data) > 0 else True
print(check_empty([]))

# Funcion que devuelva el tamaño de algo
# y que este bien anotada con genericos
my_iterable = TypeVar("my_iterable", list, str, tuple, set, dict)
def check_empty_2(data: my_iterable) -> int:
    return len(data)
