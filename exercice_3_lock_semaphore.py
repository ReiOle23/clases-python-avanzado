# Un servicio web expone sesiones de usuario (por ejemplo, compras de un ecommerce);
# por razones de infraestructura solo 10 sesiones activas pueden trabajar simultáneamente.
# Haz el ejercicio con locks y con semaforos, y al final, dime cual de las dos prefieres y por que.

from threading import Semaphore, Lock, Thread
from typing import TypeVar
import random, time

T = TypeVar("T")
lock = Lock()
active_sessions = 10

# Lock
def client_session_buy_with_lock(client: str, item: str) -> callable:
    global active_sessions
    with lock:
        if active_sessions > 0:
            time.sleep(0.1)
            active_sessions -= 1
            print(f"Session name:{client} to buy item {item}")
        else:
            active_sessions = 10
            print("---------------New Sessions---------------")
    # aqui hace release

sem = Semaphore(10)
# Semaphore
def client_session_buy_with_semaphore(client: str, item: str) -> callable:
    with sem:
        print(f"Session name:{client} to buy item {item}")
        time.sleep(0.1)
        print("---------------New Sessions---------------")
    # aqui hace release
    

if __name__ == "__main__":
    lock_items = []
    threads_lock = []
    sem_items = []
    threads_sem = []
    for n in range(50):
        random_item = random.choice(["Juguete", "Pelota", "Disfraz"])
        client_task_lock = Thread(target=client_session_buy_with_lock, args=(f"Client-{n}",random_item,))
        client_task_sem = Thread(target=client_session_buy_with_semaphore, args=(f"Client-{n}",random_item,))
        lock_items.append(client_task_lock)
        sem_items.append(client_task_sem)
        
    
    for li in lock_items:
        threads_lock.append(li)
        li.start()
        
    for t in threads_lock:
        t.join()
        
    print("*************************Semaphore Sessions:")
    time.sleep(6)
    
    for si in sem_items:
        threads_sem.append(si)
        si.start()
        
    for t in threads_sem:
        t.join()
        
# En este caso es mejor el semaphoro ya que no tienes que escrivir codigo para parar hilos si existen 10 o más.
