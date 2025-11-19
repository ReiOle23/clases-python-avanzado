from threading import Thread
from time import sleep

cuenta_bancaria = 1000

def retirar_efectivo(cantidad: int):
    global cuenta_bancaria
    sleep(0.1)
    cuenta_bancaria -= cantidad
    print(f"Cuenta bancaria con {cuenta_bancaria} €")
    return cantidad

tarea_1 = Thread(target=retirar_efectivo, args=(500,))
tarea_2 = Thread(target=retirar_efectivo, args=(500,))

tarea_1.start()
tarea_2.start()

tarea_1.join()
tarea_2.join()

print(f"Me queda {cuenta_bancaria} € en mi banco")

from multiprocessing import Process

cuenta_bancaria = 1000

tarea_1 = Process(target=retirar_efectivo, args=(500,))
tarea_2 = Process(target=retirar_efectivo, args=(500,))

tarea_1.start()
tarea_2.start()
tarea_2.terminate()
tarea_2.kill()

tarea_1.join()
tarea_2.join()

print(f"Me queda {cuenta_bancaria} € en mi banco")