from typing import Protocol
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def arrancar(self):
        ...

class Motoneta(Vehicle):
    pass

inst = Motoneta()
# falla falta implementar el metodo obligatorio
inst.arrancar()

class Vehicle(Protocol):
    @abstractmethod
    def arrancar(self):
        ...

class Motoneta:
    pass

def arrancar_motoneta(veh: Vehicle):
    veh.arrancar()
    
# falla porque no tiene ese metodo
arrancar_motoneta(Motoneta())

class Motoneta:
    def arrancar(self):
        print("brum brum")

def arrancar_motoneta(veh: Vehicle):
    veh.arrancar()
    
# ahora si
arrancar_motoneta(Motoneta())


# definir interfaz: usamos ABC o Protocol
# usar ABC en caso de duda
# ABC estructura clara de ABC
# Protocol cuando un ABC no se pueda hacer porque no hay herencia
