# SOLID PRINCIPLES

# Single Responsability
# All components has to do only 1 thing


# Open/Closed
from typing import TypeVar
Number = TypeVar("Number",int,float)
class Calculator:
    staticmethod
    def sumar(n1:Number, n2:Number) -> Number:
        return n1+n2
    
    staticmethod
    def restar(n1:Number, n2:Number) -> Number:
        return n1-n2
    
    staticmethod
    def multiplicar(n1:Number, n2:Number) -> Number:
        return n1*n2
    
    staticmethod
    def producto(n1:Number, n2:Number) -> Number:
        return n1/n2
    

    
# Liskov substitution
class Pajaro:
    def volar(self):
        print(f"Esta volando")
        
class Aguila(Pajaro):
    pass

# pinguino no esta bien porque no puede volar, quiebra el principio
class Pinguino(Pajaro):
    pass

ag = Aguila()
ag.volar()
pin = Aguila()
pin.volar()

from abc import ABC, abstractmethod
class Pajaro:
    # obliga a implementar el metodo a hijos
    @abstractmethod
    def volar(self):
        print(f"Esta volando")
class Aguila(Pajaro):
    def volar(self):
        print(f"Vuela")
class Pinguino(Pajaro):
    def volar(self):
        print(f"No puede volar")

ag = Aguila()
ag.volar()
pin = Aguila()
pin.volar()

# Interface Segregation Principle
class Animal(ABC):
    @abstractmethod
    def run(self):
        ...
    
    @abstractmethod
    def swim(self):
        ...
        
    @abstractmethod
    def fly(self):
        ...
        
class Dog(ABC):
    def run(self):
        print("run")
    
    def swim(self):
        print("swin")
        
    def fly(self):
        print("cannot fly")
        
class Aguila(ABC):
    def run(self):
        print("cannot run")
    
    def swim(self):
        print("cannot swin")
        
    def fly(self):
        print("fly")
        
# Segregar Interfaces
class AnimalQueCorre(ABC):
    @abstractmethod
    def run(self):
        ...
class AnimalQueNada(ABC):
    @abstractmethod
    def swim(self):
        ...
class AnimalQueVuela(ABC):
    @abstractmethod
    def fly(self):
        ...
                
class Perro(AnimalQueCorre, AnimalQueNada):
    def run(self):
        print("coree")
    
    def swim(self):
        print("nada")
    
    
# Dependency Inversion Principle
