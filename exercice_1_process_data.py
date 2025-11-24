# Tenemos una funcion que procesa imagenes y tarda un tiempo en ello. 
# Estamos simulando una llamada a una lambda de AWS. 
# Queremos descargar miles de imagenes de forma eficiente, y hacer estas transformaciones, 
# pero para ver que funciona de momento queremos hacerlo con 5, 8, 10, 12, 20, ... 
# un numero entre 0 y 50 imagenes, que todas tendran que pasar por esta funcion.
# Como podriamos hacerlo de forma eficiente? Aqui teneis la funcion
 
import time
from pathlib import Path
import random
from threading import Thread

def procesar_imagen(nombre_imagen):
    print(f"Iniciando procesamiento de {nombre_imagen}")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"{nombre_imagen} procesada y guardada")

if __name__ == "__main__":
    lambda_images = [
                Path("multiple_images/img.png"),
                Path("multiple_images/img copy.png"),
                Path("multiple_images/img copy 2.png"),
                Path("multiple_images/img copy 3.png"),
                Path("multiple_images/img copy 4.png"),
                Path("multiple_images/img copy 5.png"),
                Path("multiple_images/img copy 6.png"),
                Path("multiple_images/img copy 7.png"),
                Path("multiple_images/img copy 8.png"),
                Path("multiple_images/img copy 9.png"),
                Path("multiple_images/img copy 10.png"),
                ]
    threads = []
    for img in lambda_images:
        with open(img) as f:
            task = Thread(target=procesar_imagen, args=(f.name,))
            threads.append(task)
            task.start()

    for t in threads:
        t.join()
        