# decorador que me diga el nombre de la funcion
from functools import wraps
from typing import TypeVar

def funct_name(function:callable) -> callable:
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Function name is {function.__name__}")
        return function(*args, **kwargs)
    return wrapper


@funct_name
def multiply_val(value1:int,value2:int):
    return value1*value2

multiply_val(2,4)

def class_decorator(cls:object) -> object:
    def wrapper(*args, **kwargs):
        print(f"Class name is {cls.__name__}")
        return cls(*args, **kwargs)
    return wrapper

@class_decorator
class Persona:
    
    def __init__(self, name):
        self.name = name
        
print(Persona("Ina").name)
print(Persona("Gla").name)


T = TypeVar("Object", object, callable)

def object_namer(_obj:T) -> T:
    @wraps(_obj)
    def wrapper(*args, **kwargs):
        print(f"Object name is {_obj.__name__}")
        return _obj(*args, **kwargs)
    return wrapper

@object_namer
class Coche:
        
    @object_namer
    def arrancar(self):
        print("Arrancamos coche")
        
coche1 = Coche()
coche1.arrancar()
print(coche1.arrancar.__name__)
