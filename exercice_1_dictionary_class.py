# ejercicio de dictionarios pero con metodos magicos
import pytest
from typing import TypeVar

T = TypeVar("T")

class NoKey(Exception):
    def __init__(self, message):            
        super().__init__(message)
        
class Diccionario:
    
    def __init__(self):
        self._data = []
        
    def __eq__(self, y: "Diccionario") -> bool:
        return set(self.__pos__()) == set(+y) and set(self.__neg__()) == set(-y)
        
    def __repr__(self):
        elementos = [f"{repr(key)}: {repr(value)}" for key, value in self._data]
        contenido = ", ".join(elementos)
        return f"{{{contenido}}}"
    
    def __missing__(self, key):
        raise NoKey(f"Diccionario key error: {key}")
    
    def __iter__(self):
        return iter(self._data)
    
    def __setitem__(self, key: T, value: T):
        for index, (k, v) in enumerate(self._data):
            if k == key:
                self._data[index] = (key, value)
                return None
        self._data.append((key, value))

    def __getitem__(self, key: T):
        if isinstance(key, tuple) and len(key) != 1:
            return key[-1]
             
        for k, v in self._data:
            if k == key:
                return v
            
        return self.__missing__(key)
    
    def __contains__(self, key):
        for k, v in self._data:
            if k == key:
                return True
        return False

    def __delitem__(self, key):
        for index, (k, v) in enumerate(self._data):
            if k == key:
                del self._data[index]
                return True
        return False

    # def keys(self):	
    def __pos__(self):
        return [key for key, value in self._data]

    # def values(self):
    def __neg__(self):
        return [value for key, value in self._data]

    # def items(self):
    def __invert__(self):
        return list(self._data)

    def __len__(self):
        return len(self._data)

    # def clear(self):
    def __abs__(self):
        self._data = []
        
    def __add__(self, obj: "Diccionario"):
        for index, (k, v) in enumerate(obj):
            added = False
            for index, (c_k, c_v) in enumerate(self._data):
                if k == c_k:
                    self._data[index] = (k, v)
                    added = True
            if not added:
                self._data.append((k, v))
        
 
@pytest.fixture
def dic():
    return Diccionario()

@pytest.fixture
def dic2():
    obj = Diccionario()
    obj["b"] = "tigre"
    obj["c"] = 3
    return obj


print(Diccionario())

def test_basico_set_and_get(dic):
    dic["a"] = 1
    dic["b"] = 2
    assert dic["a"] == 1
    assert dic["b"] == 2


def test_set_sobreescribe(dic):
    dic["k"] = "first"
    dic["k"] = "second"
    assert dic["k"] == "second"
    assert len(dic) == 1


def test_get_con_missing(dic):
    with pytest.raises(NoKey):
        assert dic["noexiste"]
    guardia = object()
    assert dic["noexiste", guardia] is guardia


def test_delete(dic):
    dic["x"] = 10
    assert dic.__delitem__("x") is True
    with pytest.raises(NoKey):
        assert dic["x"]
    assert dic.__delitem__("x") is False


def test_avanzado_contains_length_clear(dic):
    assert ("z" in dic) is False
    dic["z"] = 99
    assert ("z" in dic) is True
    assert len(dic) == 1
    abs(dic)
    assert len(dic) == 0
    assert ("z" in dic) is False


def test_llaves_en_orden(dic):
    pares = [("uno", 1), ("dos", 2), ("tres", 3)]
    for key, value in pares:
        dic[key] = value
    assert +dic == ["uno", "dos", "tres"]
    assert -dic == [1, 2, 3]
    assert ~dic == pares


def test_items_independientes(dic):
    dic["a"]= [1,2]
    items = ~dic
    assert isinstance(items, list)
    assert isinstance(items[0], tuple)
    assert items[0][0] == "a"
    assert items[0][1] == [1, 2]


def test_imprime_como_dict(dic):
    dic["a"]= 1
    dic["b"]= "test"
    expected = "{" + f"{repr('a')}: {repr(1)}, {repr('b')}: {repr('test')}" + "}"
    assert str(dic) == expected


@pytest.mark.parametrize(
    "key, value",
    [
        ("str", "texto"),
        (123, 456),
        (("tupla",), ("valor",)),
    ],
)
def test_duck_typing(dic, key, value):
    dic[key] = value
    assert dic[key] == value
    assert (key in dic) is True
    assert len(dic) == 1


def test_secuencia_operaciones(dic):
    dic["a"] = 1
    dic["b"] = 2
    dic["c"] = 3
    assert len(dic) == 3
    del dic["b"]
    assert len(dic) == 2
    assert +dic == ["a", "c"]
    dic["a"] = 10
    assert dic["a"] == 10
 
def test_compare_dicts(dic):
    dic["a"] = 1
    dic["b"] = 2
    dic["c"] = 3
    
    equal_dict = Diccionario()
    equal_dict["a"] = 1
    equal_dict["b"] = 2
    equal_dict["c"] = 3
    assert dic == equal_dict
    dic["c"] = 5
    assert dic != equal_dict
    
def test_missing_key(dic):
    with pytest.raises(NoKey):
        dic["ole"]
 
def test_add_dict_left(dic, dic2):
    dic["a"] = "word"
    dic["b"] = "animal"
    
    dic + dic2
    
    dic_expected = Diccionario()
    dic_expected["a"] = "word"
    dic_expected["b"] = "tigre"
    dic_expected["c"] = 3
    assert dic == dic_expected
    
def test_add_dict_right(dic, dic2):
    dic["a"] = "word"
    dic["b"] = "animal"
    
    dic2 + dic
    
    dic_expected = Diccionario()
    dic_expected["a"] = "word"
    dic_expected["b"] = "animal"
    dic_expected["c"] = 3
    assert dic2 == dic_expected
