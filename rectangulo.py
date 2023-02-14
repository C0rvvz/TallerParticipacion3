#4. Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan
#los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro,
#calcular su área e indicar si el rectángulo es un cuadrado.

class Rectangulo:

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def calcular_perimetro(self, otro_punto):

        perimetro_base_x = self.x-otro_punto.x
        perimetro_altura_y = self.y-otro_punto.y

        print(perimetro_altura_y,perimetro_base_x)

    def calcular_area(self):
        pass

    def cuadrado(self):
        pass