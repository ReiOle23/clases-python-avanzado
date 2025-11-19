# verifica que los metodos esten
# i que devuelvan el mismo typo
from typing import Protocol
class Animal(Protocol):
    def comer(self) -> str:
        ...
        
class Gacela:
    def comer(self)-> str:
        return "la gacela se come hierva"
        ...

def que_coma(animal: Animal):
    print(animal.comer())

# Ejerciciio - Hacer un Protocol para un Handler de eventos
from typing import Protocol
# el Protocol se utiliza para checkear estructura, si no 
# Mal porque el SomeData no implementa los dos handler
class EventHandler(Protocol):
    def handle_get_data(self) -> dict:
        ...

    def handle_len_data(self) -> int:
        ...

class SomeData:
    data: dict = {}
    def handle_get_data(self)-> dict:
        return self.data
        ...

def get_data(event: EventHandler):
    print(event.handle_get_data())

sd= SomeData()
get_data(sd)

# Bien
class EventHandler(Protocol):
    def handle(self, event: dict) -> dict:
        ...
class SizeCounterEventHandler:
    def handle(self, event: dict) -> dict:
        event["size"] = len(event) + 1
        return event
class AddSumParamEventHandler:
    def handle(self, event: dict) -> dict:
        event["sum"] = 2+2
        return event
    
def use_event(hanlder: EventHandler, event: dict):
    return hanlder.handle(event)
    
sd= SizeCounterEventHandler()
print(use_event(sd,{}))
asum= AddSumParamEventHandler()
print(use_event(asum,{}))
