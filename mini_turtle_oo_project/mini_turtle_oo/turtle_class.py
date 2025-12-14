# turtle_class.py
# Implementación OO: clase Turtle que encapsula posicion_x

class Turtle:
    def __init__(self):
        """Inicializa una tortuga con posicion_x = 0"""
        self.posicion_x = 0

    def reiniciar(self):
        """Reinicia la posición horizontal de la tortuga a 0."""
        self.posicion_x = 0

    def adelante(self, n):
        """
        Mueve la tortuga hacia la derecha n pasos (dibuja y actualiza self.posicion_x).
        """
        if n <= 0:
            return
        print(" " * self.posicion_x + "-" * n + ">")
        self.posicion_x += n

    def abajo(self, n):
        """
        Mueve la tortuga hacia abajo n pasos desde la columna actual (dibujo vertical).
        """
        if n <= 0:
            print(" " * self.posicion_x + "v")
            return
        for _ in range(n):
            print(" " * self.posicion_x + "|")
        print(" " * self.posicion_x + "v")
