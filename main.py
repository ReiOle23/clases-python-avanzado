
import asyncio
from time import sleep
from datetime import datetime
from threading import Thread

inicio = datetime.now()
def funcion_1():
    sleep(2)
    print("Hecha tarea 1")
    
def funcion_2():
    sleep(1)
    print("Hecha tarea 2")
    
def funcion_3():
    sleep(3)
    print("Hecha tarea 3")
    
h1 = Thread(target=funcion_1)  # hilo 1
h2 = Thread(target=funcion_2)  # hilo 2
h3 = Thread(target=funcion_3)  # hilo 3

h1.start()
h2.start()
h3.start()

final = datetime.now()

print(f"He tardado {final - inicio}")
# hilo 0