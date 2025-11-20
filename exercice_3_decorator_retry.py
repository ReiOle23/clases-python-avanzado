# decorator retry, le pasamos un numero y queremos reintentar un numero de veces esa funcion
import random
from functools import wraps
from typing import TypeVar

# using generics
T = TypeVar("T")

def retry(retries:int) -> callable:
    def decorator(function: callable) -> callable:
        @wraps(function)
        def wrapper(*args, **kwargs) -> T:
            current_r = retries
            for n in range(current_r):
                try:
                    return function(*args, **kwargs)
                except Exception as err:
                    if n == retries-1:
                        raise
                    print(err)
                    current_r-=1
        return wrapper
    return decorator

@retry(4)
def function_fails():
    random_value = random.randint(0,10)
    if random_value > 1:
        raise Exception(f"Random value {random_value} > than 1")
    print(f"Random value {random_value} correct!!")

function_fails()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # vv

from functools import wraps

def login(role: str, max_retries: int = 3) -> callable:
    def decorador(funcion: callable) -> callable:
        @wraps(funcion)
        def wrapper(*args, **kwargs) -> any:
            print(f"El rol del usuario es: {role}")
            print(f"He entrado en mi función: {funcion.__name__}")

            intentos = 0
            while intentos < max_retries:
                intentos += 1
                print(f"Intento #{intentos} de login...")

                if kwargs.get("valido", False):
                    return funcion(*args, **kwargs)
                else:
                    print("Credenciales inválidas.")

            print(f"Acceso denegado tras {max_retries} intentos.")
            return None
        return wrapper
    return decorador


# Ejemplo de uso

@login("admin", max_retries=3)
def conexion_bd(usuario: str, *, valido: bool):
    if valido:
        print(f"El usuario {usuario} ha accedido a base de datos")

# Caso válido
# conexion_bd("Miguel", valido=True)

# print("-" * 40)

# # Caso inválido
# conexion_bd("Maria", valido=False)
