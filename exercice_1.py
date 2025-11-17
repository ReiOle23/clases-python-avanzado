# Ejercicio 1 - Dataclass Cola (o Queue) que sirva para almacenar tareas o procesos. 
# No hace falta que os compliqueis con la logica de las tareas en si, simplemente 
# pensad en como puede ser. Lo que si que quiero es que haya una buena cola, que se 
# maneje esto bien, y que tenga estos tres metodos. añadir_tarea, siguiente_tarea, tareas_pendientes
from collections import deque
from dataclasses import dataclass, field

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
