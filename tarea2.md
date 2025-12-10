# mi-primera-pagina.1 

# Desarrollo De Software 2025-2 Grupo: PREICA2502B020026

<img width="757" height="658" alt="image" src="https://github.com/user-attachments/assets/61cab564-d4ef-46dc-91bf-c29397b720e0" />

# Mi primer Turtle


## Reto 1: Simula el comportamiento de la tortuga usando solo print() e input()
# Tarea 2 — Simulación de la tortuga

## Reto 1: Simula la tortuga avanzando horizontal
```python
def reto1():
    print("RETO 1: Tortuga avanzando horizontal")
    pasos = int(input("Cuantos pasos quieres que avance? "))
    print("-" * pasos + ">")
# Ejemplo: crea una tortuga simulada... que da 50 pasos.
# --------------------------------------------->


## Reto 2: Tortuga bajando

def reto2():
    print("RETO 2: Tortuga bajando vertical")
    pasos = int(input("Cuantos pasos quieres bajar? "))
    for i in range(pasos):
        print("|")
    print("v")
# Ejemplo de uso:
# ¿Cuántos pasos quieres bajar? 5
# |
# |
# |
# |
# |
# v




 ## Reto 3: Girar y dibujar usando solo print() e input()
def reto3():
    print("RETO 3: Forma de L")
    pasos_horizontal = int(input("Cuantos pasos horizontales? "))
    pasos_vertical = int(input("Cuantos pasos verticales? "))
    print("-" * pasos_horizontal + ">")
    for i in range(pasos_vertical):
        print(" " * pasos_horizontal + "|")
    print(" " * pasos_horizontal + "v")
# Ejemplo:
# ¿Cuántos pasos horizontales? 10
# ¿Cuántos pasos verticales? 4
#
# ---------->        (10 guiones luego >
#           |
#           |
#           |
#           v


## Reto 4: Encapsula los comportamientos anteriores usando funciones
posicion_x = 0

def adelante(n):
    global posicion_x
    # dibuja la línea horizontal desde la posición actual
    print(" " * posicion_x + "-" * n + ">")
    posicion_x = posicion_x + n

def abajo(n):
    global posicion_x
    # dibuja n líneas verticales debajo de la posición actual
    for i in range(n):
        print(" " * posicion_x + "|")

def mostrar_flecha():
    global posicion_x
    print(" " * posicion_x + "v")

def reto4():
    global posicion_x
    posicion_x = 0
    print("RETO 4: Usando funciones (ejemplo L)")
    adelante(5)
    abajo(3)
    mostrar_flecha()
# Resultado aproximado:
# ----->
#      |
#      |
#      |
#      v


## Reto 5: La tortuga baja las escalas
def escalon(horizontal, vertical):
    adelante(horizontal)
    abajo(vertical)

def reto5():
    global posicion_x
    posicion_x = 0
    print("RETO 5: Escaleras")
    escalon(3, 2)
    escalon(3, 2)
    escalon(3, 2)
    escalon(3, 2)
    mostrar_flecha()
# Resultado aproximado (escalera repetida varias veces):
# --->      (primer escalon)
#    |
#    |
#     ---> (siguiente escalon desplazado)
#        |
#        |
# ...
# al final: mostrar_flecha() para colocar la flecha 'v' bajo la posición final



