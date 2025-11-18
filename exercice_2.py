# 1 - Fixtures
# 2 - Marks
# 3 - Parametrize

# pytest -v exercice_2.py 
# pytest -m ui exercice_2.py 
import pytest
from pytest import fixture, mark
from hypothesis import given, strategies as st

class Calculadora:
    def __init__(self):
        self.valor = 0

    def sumar(self, n):
        if n < 0:
            raise ValueError("Value negative")
        self.valor += n
        return self.valor
    
    def multiply(self, n1, n2):
        self.valor = n1 * n2
        return self.valor

    def reset(self):
        self.valor = 0
        
@fixture
def calculadora():
    return Calculadora()
       
@mark.skip
def test_calculator_sum(calculadora):
    assert 2 == calculadora.sumar(2)
    assert 5 == calculadora.sumar(3)

@mark.xfail(reason="hay bug que no esta resuelto")
def test_calculator_reset(calculadora):
    calculadora.sumar(5)
    calculadora.reset()
    assert 0 == calculadora.valor
    
@mark.ui
def test_custom():
    assert 0 == 0
    
def test_calculator_sum_negatives(calculadora):
    with pytest.raises(ValueError):
        calculadora.sumar(-2)
        

def test_sum_many(calculadora):
    assert calculadora.multiply(2,3) == 6

# @pytest.mark.parametrize("input,output", [((2,3),6),((4,4),10),((5,3),15),((2,3),6),((2,3),6)])
# def test_sum_many(calculadora, input, output):
#     assert calculadora.multiply(*input) == output
    
    
class Usuario:
    def __init__(self, nombre, edad):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self.nombre = nombre
        self.edad = edad

    def es_adulto(self):
        return self.edad >= 18

    def actualizar_nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = nuevo_nombre
        return self.nombre
 
@fixture
def user():
    return Usuario("Joa", 30)

@mark.skip()
def test_is_adult(user):
    assert user.es_adulto()
    
@mark.parametrize("input,output", [(Usuario("Joa", 30),True),(Usuario("Joa2", 12),False),(Usuario("Joa3", 18),True)])
def test_multiple_is_adult(input, output):
    assert input.es_adulto() == output

def test_update_name(user):
    with pytest.raises(ValueError):
        user.actualizar_nombre("")

@given(name=st.text(min_size=1), age=st.integers(min_value=0, max_value=120))
def test_invariant_age_no_negative(name, age):
    """INVARIANTE: La edad siempre es >= 0"""
    user = Usuario(name, age)
    assert user.edad >= 0

@given(nombre=st.text(min_size=1), edad=st.integers(min_value=0, max_value=120))
def test_usuario_valido(nombre, edad):
    u = Usuario(nombre, edad)
    assert u.nombre == nombre
    assert u.edad == edad
    # Propiedad: Que sea mayor de edad (aqui es donde usamos realmente hypothesis)
    assert u.es_adulto() == (edad >= 18)
    
