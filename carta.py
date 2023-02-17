#Cree una clase Carta que contenga dos propiedades valor y pinta,
# las cuales son asignadas solo al momento de la construcción del objeto
# (se pasan como parámetros en el constructor). Defina 4 constantes que
# representan los nombres de las 4 pintas que puede tener una carta.

class Carta:

    PICAS = "PICAS"
    CORAZONES = "CORAZONES"
    TREBOLES = "TREBOLES"
    ESPADAS = "ESPADAS"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta


Carta(4, Carta.ESPADAS)
