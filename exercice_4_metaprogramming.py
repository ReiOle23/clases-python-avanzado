# https://www.pythonmorsels.com/every-dunder-method/
from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    apellido_1: str
    apellido_2: str
    
    # metodo magico
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido_1} {self.apellido_2}"
    
    # metodo magico __algo__
    def __len__(self) -> int:
        return len(self.nombre+self.apellido_1+self.apellido_2)
    
    def __eq__(self, other) -> bool:
        return True if len(other)== len(self) else False
    
joa = Persona("Joaquin", "Hernandex", "Martinez")
joa2 = Persona("Joaquin", "Hernandex", "Martinez")

print(joa == joa2)


# ************************************
# class Iterable:
#     def __iter__(self):
#         pass
    
# iter()

# class Iterator:
#     def __next__(self):
#         pass
    
# next()

# Un generador va devolviendo trozos (es un iterador)
# range es un generador
def generator(max: int) -> list:
    contador = 0
    while max > contador:
        yield contador
        contador += 1

gen = generator(10)

next(gen)
next(gen)
next(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))

gen_numeros = (num +10 for num in range(10)) # generator
lista_numeros = {str(num):num for num in range(10)}
print(lista_numeros)

# corutina és un generador que és capaz de esperar
# generadores con promesas