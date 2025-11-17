# Ejercicio 1 - Dataclass Cola (o Queue) que sirva para almacenar tareas o procesos. 
# No hace falta que os compliqueis con la logica de las tareas en si, simplemente 
# pensad en como puede ser. Lo que si que quiero es que haya una buena cola, que se 
# maneje esto bien, y que tenga estos tres metodos. añadir_tarea, siguiente_tarea, tareas_pendientes
from collections import deque

    
class Cola:
    
    def __init__(self):
        self.content = deque()
    
    def añadir_tarea(self, value):
        self.content.append(value)
    
    def siguiente_tarea(self):
        task = self.content.popleft()
        print(f"tarea '{task}' completada:")
                
    def __repr__(self):
        return f"Cola(pendientes={len(self.content)})"
    

def main():
    cola = Cola()
    cola.añadir_tarea("procesar_imagen")
    cola.añadir_tarea("backup")
    cola.añadir_tarea("exportar_pdf")

    print(cola)  # Cola(pendientes=3)

    print(cola.siguiente_tarea())  # procesar_imagen
    print(cola.siguiente_tarea())  # backup

    print(cola)  # Cola(pendientes=1)

if __name__ == "__main__":
    main()