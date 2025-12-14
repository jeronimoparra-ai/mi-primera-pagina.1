# tarea2.py
# Implementación de una mini tortuga gráfica en modo texto




# -------------------------
# Variable global
# -------------------------
posicion_x = 0

# -------------------------
# Interfaz requerida
# -------------------------
def reiniciar():
    """Reinicia la posición horizontal a 0."""
    global posicion_x
    posicion_x = 0

def adelante(n):
    """Dibuja una línea horizontal de longitud n desde la posición actual y avanza."""
    global posicion_x
    if n <= 0:
        return
    print(" " * posicion_x + "-" * n + ">")
    posicion_x += n

def abajo(n):
    """Dibuja n líneas verticales en la columna actual y coloca 'v' al final."""
    global posicion_x
    if n <= 0:
        
        print(" " * posicion_x + "v")
        return
    for _ in range(n):
        print(" " * posicion_x + "|")
    print(" " * posicion_x + "v")

# -------------------------
# Utilidad para pedir enteros 
# -------------------------
def pedir_entero(prompt):
    """
    Pide un entero al usuario usando exactamente el texto de 'prompt'.
    Repite hasta recibir un entero válido.
    Si el usuario envía EOF (Ctrl+D) o interrumpe (Ctrl+C), el programa sale limpiamente.
    """
    while True:
        try:
            texto = input(prompt)
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada interrumpida. Saliendo del programa.")
            raise SystemExit(0)

        texto = texto.strip()
        if texto == "":
            print("Entrada vacía. Ingresa un número entero.")
            continue
        try:
            valor = int(texto)
            return valor
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

# -------------------------
# Retos
# -------------------------
def reto1():
    reiniciar()
    print("\nRETO 1")
    pasos = pedir_entero("adelante: ")
    adelante(pasos)

def reto2():
    reiniciar()
    print("\nRETO 2")
    pasos = pedir_entero("abajo: ")
    abajo(pasos)

def reto3():
    reiniciar()
    print("\nRETO 3: Forma de L")
    h = pedir_entero("adelante: ")
    adelante(h)
    v = pedir_entero("abajo: ")
    abajo(v)

def reto4():
    reiniciar()
    print("\nRETO 4 (ejemplo fijo)")
    adelante(5)
    abajo(3)

def reto5():
    """
    Reto 5 con la interfaz EXACTA modificada a 'adelante:' y 'abajo:':
    adelante:
    abajo:


    adelante:
    abajo:


    adelante:
    """
    reiniciar()
    print("\nRETO 5 (prototipo)")

    # Primer bloque
    x1 = pedir_entero("adelante: ")
    adelante(x1)

    y1 = pedir_entero("abajo: ")
    abajo(y1)

    # Separación visual 
    print("\n")

    # Segundo bloque
    x2 = pedir_entero("adelante: ")
    adelante(x2)

    y2 = pedir_entero("abajo: ")
    abajo(y2)

    # Separación visual
    print("\n")

    # Tercer bloque (solo adelante)
    x3 = pedir_entero("adelante: ")
    adelante(x3)

    # Opcional: mostrar posición final
    print(f"\nSecuencia completada. posicion_x = {posicion_x}")

# -------------------------
# Menú principal
# -------------------------
def menu():
    try:
        while True:
            print("\n----- MENÚ PRINCIPAL -----")
            print("1. Reto 1")
            print("2. Reto 2")
            print("3. Reto 3")
            print("4. Reto 4")
            print("5. Reto 5")
            print("6. Reiniciar posicion_x")
            print("7. Mostrar posicion_x")
            print("8. Salir")

            try:
                opcion = input("Selecciona una opción: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nEntrada interrumpida. Saliendo del programa.")
                break

            if opcion == "1":
                reto1()
            elif opcion == "2":
                reto2()
            elif opcion == "3":
                reto3()
            elif opcion == "4":
                reto4()
            elif opcion == "5":
                reto5()
            elif opcion == "6":
                reiniciar()
                print("Posición reiniciada.")
            elif opcion == "7":
                print(f"[posicion_x] = {posicion_x}")
            elif opcion == "8":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Ingresa un número del 1 al 8.")
    except SystemExit:
        # salir limpio si pedir_entero decidió terminar
        pass

# -------------------------
# Ejecución principal
# -------------------------
if __name__ == "__main__":
    menu()
