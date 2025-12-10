# mi-primera-pagina.1 

# Desarrollo De Software 2025-2 Grupo: PREICA2502B020026

<img width="757" height="658" alt="image" src="https://github.com/user-attachments/assets/61cab564-d4ef-46dc-91bf-c29397b720e0" />

# Mi primer Turtle
El desafío consistía en simular el comportamiento de una tortuga gráfica utilizando únicamente las funciones básicas de Python: print() e input(). Mi objetivo era representar movimiento bidimensional en un espacio de texto, construyendo la solución de forma progresiva a través de cinco retos.

# Tarea 2 — Simulación de la tortuga
## Reto 1: Simula el comportamiento de la tortuga usando solo print() e input()
Comencé con lo más simple: desplazar la tortuga horizontalmente. Utilicé la multiplicación de strings en Python para repetir el carácter - según los pasos solicitados.

```
def reto1():
    print("RETO 1: Tortuga avanzando horizontal")
    pasos = int(input("¿Cuántos pasos quieres que avance? "))
    print("-" * pasos + ">")   # Dibujo horizontal

# Ejemplo: crea una tortuga simulada... que da 50 pasos.
# --------------------------------------------->
```
La expresión "-" * pasos genera una línea de longitud variable, mientras que ">" representa la dirección del movimiento.


``
## Reto 2: Tortuga bajando
Para el desplazamiento vertical, implementé un bucle for que imprime el carácter | en múltiples líneas, simulando el descenso de la tortuga.
```python
def reto2():
    print("RETO 2: Tortuga bajando vertical")
    pasos = int(input("¿Cuántos pasos quieres bajar? "))

    for i in range(pasos):
        print("|")
    print("v")   # Flecha final hacia abajo

# Ejemplo de uso:
# ¿Cuántos pasos quieres bajar? 5
# |
# |
# |
# |
# |
# v



```
 ## Reto 3: Girar y dibujar usando solo print() e input()
 El verdadero desafío surgió al combinar ambos movimientos para crear una forma de "L". Aquí introduje espacios en blanco para mantener la continuidad visual de la posición horizontal.
 ```python
def reto3():
    print("RETO 3: Forma de L")
    pasos_horizontal = int(input("¿Cuántos pasos horizontales? "))
    pasos_vertical = int(input("¿Cuántos pasos verticales? "))

    print("-" * pasos_horizontal + ">")

    for i in range(pasos_vertical):
        print(" " * pasos_horizontal + "|")

    print(" " * pasos_horizontal + "v")

# Ejemplo:
# ¿Cuántos pasos horizontales? 10
# ¿Cuántos pasos verticales? 4
#
# ---------->        (10 guiones luego '>')
#           |
#           |
#           |
#           v


```
## Reto 4: Encapsula los comportamientos anteriores usando funciones
Reconocí que estaba repitiendo lógica, por lo que decidí modularizar el código. Creé funciones específicas para cada comportamiento y utilicé una variable global posicion_x para mantener el estado de la tortuga.
```python
posicion_x = 0

def adelante(n):
    global posicion_x
    print(" " * posicion_x + "-" * n + ">")
    posicion_x += n

def abajo(n):
    global posicion_x
    for i in range(n):
        print(" " * posicion_x + "|")

def mostrar_flecha():
    global posicion_x
    print(" " * posicion_x + "v")

def reto4():
    global posicion_x
    posicion_x = 0
    print("RETO 4: Usando funciones (Ejemplo L)")
    adelante(5)
    abajo(3)
    mostrar_flecha()

# Resultado aproximado:
# -----> 
#      |
#      |
#      |
#      v


```
## Reto 5: La tortuga baja las escalas
Finalmente, implementé la función escalon() que combina movimientos básicos para crear patrones más complejos. Esto demuestra el principio de composición funcional.
```python
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
```
# Resultado aproximado (escalera repetida varias veces):
```python
# --->      (primer escalon)
#    |
#    |
#     --->   (siguiente escalon desplazado)
#        |
#        |
# ...
```
## Conclusiones
Este ejercicio me permitió aplicar tres principios fundamentales de la programación:
Abstracción progresiva: construir soluciones complejas a partir de componentes simples
Modularización: encapsular comportamientos repetitivos en funciones reutilizables
Gestión de estado: utilizar variables globales para mantener el contexto del programa
La simulación de la tortuga, aunque básica, ilustra cómo conceptos espaciales pueden traducirse efectivamente a representaciones textuales mediante el uso estratégico de strings y estructuras de control.


``
## Mi progreso👇
https://github.com/jeronimoparra-ai/mi-primera-pagina.1/blob/main/blog/tarea2_unidad1.md









