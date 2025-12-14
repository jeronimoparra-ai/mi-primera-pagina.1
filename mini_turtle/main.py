# main.py
# Script de demostración para el Ejercicio 1 

from mini_turtle import adelante, abajo, reiniciar

def main():
    print("Demostración: paquete funcional mini_turtle\n")

    # Dibujar una escalera simple (3 escalones)
    reiniciar()
    print("Escalera 1 (3 escalones):")
    adelante(5)
    abajo(2)

    print()  # separación

    adelante(5)
    abajo(2)

    print()  # separación

    adelante(5)
    abajo(2)

    # Usar reiniciar para dibujar algo diferente
    print("\nReiniciando y dibujando otra figura...")
    reiniciar()
    adelante(7)
    abajo(1)
    adelante(3)

if __name__ == "__main__":
    main()
