if __name__ == "__main__":

    from punto import Punto
    """
    punto1 = Punto(3,4)
    punto1.mover_punto(4,7)
    punto2 = Punto(5,6)
    punto1.mostrar_coordenadas()
    punto2.calcular_distancia(punto1)
    """
    from rectangulo import Rectangulo
    punto1 = Punto(5,7)
    punto2 = Punto(9,9)
    rect_1 = Rectangulo(punto1, punto2)
    print(rect_1.calcular_perimetro())
    print(rect_1.calcular_area())
    rect_1.es_cuadrado()

