import time
from threading import Thread
import multiprocessing

def trabajo(nombre):
    print(f"[{nombre}] Entrando al trabajo")
    # con processing no hace falta time.sleep(2)  
    print(f"[{nombre}] Saliendo del trabajo")
    
def elevated_values(value1: int,value2:int):
    print(f"Elevated value of {value1} and {value2} is {value1**value2}")

if __name__ == "__main__":
    # # Creamos dos hilos que ejecutan la misma función
    # # se utilizan para cosas largas como descargar datos o imagenes.
    # hilo1 = Thread(target=trabajo, args=("Hilo_1",))
    # hilo2 = Thread(target=trabajo, args=("Hilo_2",))

    # # Iniciamos los hilos
    # hilo1.start()
    # hilo2.start()

    # # Esperamos a que terminen
    # hilo1.join()
    # hilo2.join()

    # print("Todos los hilos han terminado")
    
    # # esto si es concurrente de verdad(esta aprovechando un processo por nucleo)
    # # interpretes distintos, como si tuviera 2 entornos virtuales (hay dos gils)
    # # se utilizan para tareas que dependen de cpu, muchos datos
    # processo1 = multiprocessing.Process(target=trabajo, args=("Processo_1",))
    # processo2 = multiprocessing.Process(target=trabajo, args=("Processo_2",))

    # # Iniciamos los processos
    # processo1.start()
    # processo2.start()

    # # Esperamos a que terminen
    # processo1.join()
    # processo2.join()

    # print("Todos los Processos han terminado")
    # processos no son para api calls o descargar datos, son para funciones que necessiten mucha carga de cpu
    values = [(100,200),(304,532),(404,531),(300,120),(150,40)]
    process_started = []
    start = time.time()
    for v in values:
        process = multiprocessing.Process(target=elevated_values, args=v)
        process_started.append(process)
        process.start()

    for ps in process_started:
        ps.join()

    end = time.time() 

    print("Todos los Processos han terminado con tiempo", end-start)

    # p = Pool(7)
    # with p as pool:
    #     # starmap desempaqueta lista de valores en un map
    #     results = pool.starmap(elevated_values, values)