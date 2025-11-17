# Ejercicio 2 - Crear una dataclass que sea un edificio, y que tenga una convencion especial. 
# Se construye con dos numeros (el piso base y el piso mas alto) y deberia 
# tener una lista de pisos entre medias (obvio, todos ints)
# Todos los sotanos deberian ser S# (con el numero representando el sotano, por ejemplo el -2 seria el S", sotano 2)
# El bajo es B (nivel 0)
# el primero es E (de entreplanta)
# y el ultimo piso siempre va a ser la azotea (A)
 
from dataclasses import dataclass, field

@dataclass
class Edificio:
    ground_floor:int
    top_floor:int
    plantas: list = field(default_factory=list)
    
    
    def type_of_floor(self, num):
        if num < 0:
            return f"S{abs(num)}"
        elif num == 0:
            return "B"
        elif num == 1:
            return "E"
        elif num == self.top_floor:
            return "A"
        return num
    
    def set_floors(self):
        for i in range(self.ground_floor, self.top_floor+1):
            self.plantas.append(self.type_of_floor(i))
    
    def __post_init__(self):
        self.set_floors()
    

if __name__ == "__main__":
    inst = Edificio(-2, 10)
    print(inst.plantas)  # [S2, S1, B, E, 2, 3, 4, 5, 6, 7, 8, 9, A]
