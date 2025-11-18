# Ejercicio - Crear un codigo en Python que me permita evaluar funciones matematicas, por ejemplo
# f(x) = x + 5 es una funcion por la que x = 10 se evalua como: 
# f(10) = 10 + 5 = 15
# por tanto tengo que ver print(f(x)) es 15 si x = 10
# sin embargo, la funcion puede ser de cualquier forma!
# como hago el codigo de forma que defina una x = ? (numero) y f(x) me de una funcion correcta?
from pytest import fixture, mark


class MathFunction():
    
    def __init__(self, function):
        self.function = function
    
    def validate(self, x):
        return self.function(x)

@fixture
def random_funct():
    def f(x):
        return x + 5
    return f

def test_f_function(random_funct):
    m = MathFunction(random_funct)
    assert m.validate(5) == random_funct(5)
    

x = 10
y = 5
z = 9
f = lambda x: lambda y: lambda z: x + y + z
res = f(x)(y)(z)
print(res)
    