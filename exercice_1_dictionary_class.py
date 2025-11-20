# create a class working as a dictionary
import pytest
from pytest import fixture, mark


class DictionaryObject:
    keys = []
    values = []
     
    def add(self, key, value):
        try:
            if self.keys.index(key):
                return
        except:
            self.keys.append(key)
            self.values.append(value)
        
        
    def get(self,key):
        return self.values[self.keys.index(key)]
    
    def update(self, key, value):
        return self.values.insert(self.keys.index(key), value)
    
    def remove(self,key):
        if self.keys.index(key):
            self.values.remove(self.keys.index(key))
        self.keys.remove(key)
        
    def len(self):
        return len(self.keys)
        
  
@fixture
def dict_obj():
    return DictionaryObject()
  
def test_dictionary_add_key_value(dict_obj):
    dict_obj.add("animal","tortuga")
    assert "animal" in dict_obj.keys
  
def test_dictionary_get_value(dict_obj):
    dict_obj.add("animal","tortuga")
    assert dict_obj.get("animal") == "tortuga"

def test_dictionary_update_value(dict_obj):
    dict_obj.add("animal","tortuga")
    dict_obj.update("animal","perro")
    assert dict_obj.get("animal") == "perro"

def test_dictionary_remove_key(dict_obj):
    dict_obj.add("animal","tortuga")
    dict_obj.remove("animal")
    assert "animal" in dict_obj.keys
      
def test_dictionary_lenght(dict_obj):
    dict_obj.add("animal","tortuga")
    dict_obj.add("animal","tortuga marina")
    dict_obj.add("objecto","piedra")
    assert dict_obj.len() == 2
    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    
    
class Diccionario:
    def __init__(self):
        self._data = []

    def set(self, clave, valor):
        #  __setitem__
        for index, (key, value) in enumerate(self._data):
            if key == clave:
                self._data[index] = (clave, valor)
                return None
        self._data.append((clave, valor))

    def get(self, clave, defecto=None):
        # __getitem__
        for key, value in self._data:
            if key == clave:
                return value
        return defecto

    def delete(self, clave):
        # __delitem__
        for index, (key, value) in enumerate(self._data):
            if key == clave:
                del self._data[index]
                return True
        return False

    def contains(self, clave):
        # __contains__
        for key, value in self._data:
            if key == clave:
                return True
        return False

    def keys(self):
        return [key for key, value in self._data]

    def values(self):
        return [value for key, value in self._data]

    def items(self):
        return list(self._data)

    def length(self):
        # __len__
        return len(self._data)

    def clear(self):
        self._data = []
        
    def __str__(self):
        elementos = [f"{repr(key)}: {repr(value)}" for key, value in self._data]
        contenido = ", ".join(elementos)
        return f"{{{contenido}}}"

 
@pytest.fixture
def dic():
    return Diccionario()

print(Diccionario())

def test_basico_set_and_get(dic):
    dic.set("a", 1)
    dic.set("b", 2)
    assert dic.get("a") == 1
    assert dic.get("b") == 2


def test_set_sobreescribe(dic):
    dic.set("k", "first")
    dic.set("k", "second")
    assert dic.get("k") == "second"
    assert dic.length() == 1


def test_get_con_missing(dic):
    assert dic.get("noexiste") is None
    guardia = object()
    assert dic.get("noexiste", guardia) is guardia


def test_delete(dic):
    dic.set("x", 10)
    assert dic.delete("x") is True
    assert dic.get("x") is None
    assert dic.delete("x") is False


def test_avanzado_contains_length_clear(dic):
    assert dic.contains("z") is False
    dic.set("z", 99)
    assert dic.contains("z") is True
    assert dic.length() == 1
    dic.clear()
    assert dic.length() == 0
    assert dic.contains("z") is False


def test_llaves_en_orden(dic):
    pares = [("uno", 1), ("dos", 2), ("tres", 3)]
    for key, value in pares:
        dic.set(key, value)
    assert dic.keys() == ["uno", "dos", "tres"]
    assert dic.values() == [1, 2, 3]
    assert dic.items() == pares


def test_items_independientes(dic):
    dic.set("a", [1, 2])
    items = dic.items()
    assert isinstance(items, list)
    assert isinstance(items[0], tuple)
    assert items[0][0] == "a"
    assert items[0][1] == [1, 2]


def test_imprime_como_dict(dic):
    dic.set("a", 1)
    dic.set("b", "test")
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
    dic.set(key, value)
    assert dic.get(key) == value
    assert dic.contains(key) is True
    assert dic.length() == 1


def test_secuencia_operaciones(dic):
    dic.set("a", 1)
    dic.set("b", 2)
    dic.set("c", 3)
    assert dic.length() == 3
    dic.delete("b")
    assert dic.length() == 2
    assert dic.keys() == ["a", "c"]
    dic.set("a", 10)
    assert dic.get("a") == 10
 