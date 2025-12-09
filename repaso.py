from typing import Protocol, TypeVar, Generic


# hilo tiene que ver con tiempo perdido(no es paralelo)
# proceso clona para funcionar en paralelo

# decorado que vuelva a intentar una funcion
from typing import TypeVar, Protocol, Generic
from abc import ABC
from functools import wraps

T = TypeVar("T")

def retry(tries:int)-> callable:
    def decorador(operation: callable):
        @wraps(operation)
        def wrapper(*args, **kwargs):
            w_tries = tries
            while w_tries>0:
                print("Intentando",w_tries)
                try:
                    return operation(*args, **kwargs)
                except:
                    print("Fallo")
                    w_tries-=1
                    if w_tries<=0:
                        raise
        return wrapper
    return decorador

@retry(3)
def sumar(n1:int, n2:T):
    return n1 + n2

sumar(2, "a")


# iteradores
# iter() __iter__
# next() __next__
# StopIteration


# 1. Protocolo
class SoportaSuma(Protocol):
    def sumar_con(self, other: "SoportaSuma") -> "SoportaSuma":
        ...


# 2. Alias de tipo
T = TypeVar("T", int, float)


# 3. Implementamos protocolo
class Caja(Generic[T]):
    def __init__(self, valor: T):
        self.valor = valor

    def sumar(self, otro: T) -> T:
        if isinstance(self.valor, SoportaSuma):
            return self.valor.sumar_con(otro)
        raise TypeError("El tipo no implementa SoportaSuma")


# 4. Se usa el protocolo
def sumar(a: SoportaSuma, b: SoportaSuma) -> SoportaSuma:
    return a.sumar_con(b)


# 5. Tipo que cumple el protocolo
class Numero:
    def __init__(self, n: int):
        self.n = n

    def sumar_con(self, other: "Numero") -> "Numero":
        return Numero(self.n + other.n)

    def __repr__(self):
        return f"Numero({self.n})"




x = Numero(10)
y = Numero(5)

print(sumar(x, y))

c1 = Caja(x)
print(c1.sumar(y))
