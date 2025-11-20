# callback 
def calculadora(n1:int, n2:int, operation:callable): # 5 principle of dependencies
    return operation(n1,n2)

# closure : funciona que guarda algo dentro de su scope
# uso, memoria de n1, hasta que me interese obtener el resultado
def closure(n1:int) -> callable:
    # guarda n1
    def interior(n2: int) -> int:
        return n1*n2
    return interior

variable = closure(10)
resultado = variable(5)
print(resultado)

# decorator
# *args → captura múltiples argumentos posicionales (tupla)
# **kwargs → captura argumentos con nombre/clave (diccionario)
def closure(function:callable) -> callable:
    def interior(*args, **kwargs):
        print(f"la funciona se llama: {function.__name__}")
        return function(*args, **kwargs)
    return interior

@closure
def decir_hola(name):
    print(f"Holaa {name}")
    
decir_hola("olee")

from functools import wraps

def error_silencioso(silencio:bool) -> callable:
    def decorator(function:callable) -> callable:
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception:
                if silencio:
                    return None
                # raise Exception("ahahaha")
                raise
        return wrapper
    return decorator

@error_silencioso(True)
# @error_silencioso(False)
def sumar(n1,n2):
    return n1+n2
    
print(sumar(2,"a"))