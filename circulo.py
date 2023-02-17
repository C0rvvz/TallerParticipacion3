#5. Cree una clase Circulo que tenga las propiedades
# centro y radio, las cuales se inicializan con parámetros
# en el constructor. Defina métodos en la clase para calcular el área,
# el perímetro e indicar si un punto pertenece al círculo o no.

from punto import Punto
import math
class Circulo:
    def __init__(self, centro: Punto, radio: float):
        self.centro: Punto = centro
        self.radio: float = radio

    def calcular_area(self) -> float:
        print(f"El area del circulo es {math.pi * self.radio ** 2}")
        return

    def calcular_perimetro(self) -> float:
        print(f"El perimetro del circulo es {2 * math.pi * self.radio}")
        return

    def pertenece_al_circulo(self,otro_punto):
        if otro_punto.centro.x <= self.centro.x + self.radio and otro_punto.centro.y <= self.centro.y + self.radio:
            print("Es parte del circulo")
        else:
            print("No es parte del circulo")