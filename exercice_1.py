# Ejercicio 1 - Dataclass Cola (o Queue) que sirva para almacenar tareas o procesos. 
# No hace falta que os compliqueis con la logica de las tareas en si, simplemente 
# pensad en como puede ser. Lo que si que quiero es que haya una buena cola, que se 
# maneje esto bien, y que tenga estos tres metodos. añadir_tarea, siguiente_tarea, tareas_pendientes
from collections import deque
from dataclasses import dataclass, field, asdict, make_dataclass
import json

@dataclass
class Cola:
    pendientes: deque = field(default_factory=deque)
    
    def añadir_tarea(self, value):
        self.pendientes.append(value)
    
    def siguiente_tarea(self):
        return self.pendientes.popleft() if self.pendientes else None
        
    def tareas_pendientes(self):
        return len(self.pendientes)
    

if __name__ == "__main__":
    cola = Cola()
    cola.añadir_tarea("procesar_imagen")
    cola.añadir_tarea("backup")
    cola.añadir_tarea("exportar_pdf")

    print(cola)  # Cola(pendientes=3)

    print(cola.siguiente_tarea())  # procesar_imagen
    print(cola.siguiente_tarea())  # backup

    print(cola)  # Cola(pendientes=1)
    # print(asdict(cola)) # test
    # data = asdict(cola)
    # with open("test.json", "w") as file:
    #     json.dump(file, data)
    
    
    # dynamic class
    # with open("data.json") as file:
    #     data =json.load(file)
        
    # mi_clase = make_dataclass("Empresa", tuple(data.items()))  # clase
    # mi_instancia = mi_clase(**data)  # instancia
    # mi_instancia.numero_sucursales = 10

    # with open("output.json", "w") as file:
    #     json.dump(asdict(mi_instancia), file)
    
    # class vs dataclass
    # if it is a lot of process, go for a class, if its more params and values, go for dataclass
