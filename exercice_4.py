# Ejercicio - Voy a dar 3 JSON, y quiero que hagamos un sistema para leerlos en paralelo (con Hilos)
# Quiero tener el tamaño de esos JSON 
# y para hacerlo eficiente, vamos a usar Hilos

from threading import Thread
import json
from pathlib import Path

def get_json_size(file_url:Path,results: dict[str: [int,None]]):
    try:
        with file_url.open() as f:
            data = json.load(f)
        size = len(data)
        results[file_url.name] = size
        print(f"'{file_url.name}' -> {size} claves")
    except Exception as err:
        results[file_url.name] = None
        print(f"Error al leer '{file_url.name}': {err}")

if __name__ == "__main__":
    datasets = [Path("test.json"),Path("test2.json"),Path("test3.json")]
    results = {}
    threads = []
    
    for ds in datasets:
        t = Thread(target=get_json_size, args=(ds,results))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        