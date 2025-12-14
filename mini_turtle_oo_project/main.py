# main.py
# Demostración de independencia entre objetos Turtle

from mini_turtle_oo import Turtle

def main():
    print("Demostración POO: dos tortugas independientes\n")

    t1 = Turtle()
    t2 = Turtle()

    print("Movimiento de t1:")
    t1.adelante(5)
    t1.abajo(2)

    print("\nMovimiento de t2 (empieza desde 0, independiente):")
    t2.adelante(3)
    t2.abajo(1)

    print("\nSegunda acción de t1 (comprueba que su estado se mantuvo):")
    t1.adelante(2)  # debe dibujar desde la posición previa de t1

    print("\nReiniciar t1 y dibujar otra cosa:")
    t1.reiniciar()
    t1.adelante(4)
    t1.abajo(1)

if __name__ == "__main__":
    main()
# mini_turtle_oo/__init__.py
# Interfaz pública: exporta la clase Turtle