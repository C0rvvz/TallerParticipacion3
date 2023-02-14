if __name__ == "__main__":

    from punto import Punto

    punto1 = Punto(3,4)
    punto1.mover_punto(4,7)
    punto2 = Punto(5,6)
    punto1.mostrar_coordenadas()
    punto2.calcular_distancia(punto1)

    from rectangulo import Rectangulo

    punto1 = Rectangulo(5,3)
    punto2 = Rectangulo(6, 40)

    punto1.calcular_perimetro(punto2)

