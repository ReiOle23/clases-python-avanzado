# django orm utiliza fabricas
# patron iterador en django
from threading import Thread
from typing import TypeVar

resultados = []

T = TypeVar("T", int, float)

def sumar_dos(a: T, b: T)-> T:
    print("Sumar dos", a, b)
    global resultado
    resultado = a+b
    return a + b

def elevar_2(val: T)-> T:
    print("Elevar quadrado", val)
    return val**2
    
def fabrica_hilos(operation: callable, *args, **kwargs) -> Thread:
    return Thread(target=operation, args=args, kwargs=kwargs)

hilo = fabrica_hilos(sumar_dos, 10, 20)
hilo.start()
hilo.join()

hilo = fabrica_hilos(elevar_2, 10)
hilo.start()
hilo.join()

hilo = fabrica_hilos(elevar_2, val=10)
hilo.start()
hilo.join()

from multiprocessing import Process
# fabrica de processos
def fabrica_processos(operation: callable, *args, **kwargs) -> Process:
    return Process(target=operation, args=args, kwargs=kwargs)

# class fabrica
class ThreadFactory:
    
    def __init__(self, target: callable):
        self.target = target
        
    def create_thread(self, *args, **kwargs) -> Thread:
        return Thread(target=self.target, args=args, kwargs=kwargs)
    
class ThreadManager:
    
    def __init__(self, factory: ThreadFactory, threads: int, *args, **kwargs):
        self.lista = [factory.create_thread(args,kwargs) for t in range(threads)]
        
    def start_all(self):
        for l in self.lista:
            l.start()
        
    def join_all(self):
        for l in self.lista:
            l.join()
        
    def execute(self):
        self.start_all()
        self.join_all()
        return self.resultados

hilo_obj = ThreadFactory(sumar_dos)
hilo = hilo_obj.create_thread(10, 20)
hilo.start()
hilo.join()

example = Thread(target=sumar_dos, args=(2,3))
example.start()
example.join()
print(example)
print(resultado)
# hilo_obj = ThreadManager(sumar_dos)






# class
class Persona:
    registro = [] # var compartida por todas las Instancia Persona
    
    def __init__(self, name):
        self.name = name
        
    @classmethod
    def inspeccion(cls):
        print("Nombres")
        