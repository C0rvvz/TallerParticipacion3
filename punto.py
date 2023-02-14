#2. Cree una clase Punto que
# represente un punto en el plano cartesiano.

class Punto:

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

# 3. A la clase del punto anterior,
# defínale los siguientes métodos:
#    - Un método mostrar que imprima
#    por consola las coordenadas del
#    punto
#    - Un método mover que cambie las
#    coordenadas del punto
#    - Un método calcular_distancia
#    que calcule la distancia de la
#    instancia actual con otro punto.

    def mostrar_coordenadas(self):
        print(f"{self.x} X, {self.y} Y")

    def mover_punto(self, nueva_x: int, nuevo_y: int):
        self.x = nueva_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        distancia_x = self.x-otro_punto.x
        distancia_y = self.y-otro_punto.y
        print(distancia_y,distancia_x)




