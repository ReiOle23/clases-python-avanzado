# Ejercicio 2 - Reservas de hotel 
# Tenemos una llamada a una API que reserva habitaciones de hotel, 
# y unas habitaciones disponibles. Tenemos que hacer un sistema que nos 
# permita, de forma asincrona, realizar estas llamadas.
import time
from threading import Thread, Lock, Semaphore, Event, Condition, Barrier

# Lock permite abrir o cerrar hilos

# avoid race condition
lock = Lock()
# same
# sem = Semaphore(1)

# same as lock but to avoid number of threads (only 2 threads)
sem = Semaphore(2)

# sem = Semaphore(4)
# espera a que lleguen 4 hilos para hacer codigo
# barrier = Barrier(4)
# barrier.wait()

import time
from threading import Thread, Lock

habitaciones_disponibles = 10

def reservar_habitacion(cliente):
    global habitaciones_disponibles
    # lock.acquire()
    # if habitaciones_disponibles > 0:
    #     print(f"[{cliente}] - {habitaciones_disponibles} habitaciones disponibles")
    #     time.sleep(0.1)
    #     habitaciones_disponibles -= 1
    #     print(f"[{cliente}] ✓ Reserva confirmada. Quedan {habitaciones_disponibles}")
    # else:
    #     print(f"[{cliente}] ✗ No hay habitaciones disponibles")
    # lock.release()
    
    # hace lo mismo
    # with lock:
    # with sem:
    with lock:
        if habitaciones_disponibles > 0:
            print(f"[{cliente}] - {habitaciones_disponibles} habitaciones disponibles")
            time.sleep(0.1)
            habitaciones_disponibles -= 1
            print(f"[{cliente}] ✓ Reserva confirmada. Quedan {habitaciones_disponibles}")
        else:
            print(f"[{cliente}] ✗ No hay habitaciones disponibles")
    
if __name__ == "__main__":
    clients = ["Jose","Maria","Hernan","Clara","Alo","Julain", "Everin", "Eren", "Brook", "Fga", "Mulan","Inna"]
    threads = []
    for c in clients:
        client_task = Thread(target=reservar_habitacion, args=(c,))
        threads.append(client_task)
        client_task.start()
        
    for t in threads:
        t.join()
        
    print(f"Final counter: {habitaciones_disponibles}")
            