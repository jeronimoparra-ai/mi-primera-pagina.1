# Reto 1: Simula el comportamiento de la tortuga usando solo print() e input()
def reto1():
    print("RETO 1: Tortuga avanzando horizontal")
    pasos = int(input("Cuantos pasos quieres que avance? "))
    print("-" * pasos + ">")

#Reto 2: Tortuga bajando
def reto2():   print("RETO 2: Tortuga bajando vertical")   
pasos = (input("Cuantos pasos quieres bajar? ")) 

     
print ("|")
    
print("v")

 # Reto 3: Girar y dibujar usando solo print() e input()

def reto3():
    print("RETO 3: Forma de L")
    pasos_horizontal = int(input("Cuantos pasos horizontales? "))
    pasos_vertical = int(input("Cuantos pasos verticales? "))
    
    print("-" * pasos_horizontal + ">")
    
    for i in range(pasos_vertical):
        print(" " * pasos_horizontal + "|")
    
    print(" " * pasos_horizontal + "v")

# Reto 4: Encapsula los comportamientos anteriores usando funciones
posicion_x = 0

def adelante(n):
    global posicion_x
    print(" " * posicion_x + "-" * n + ">")
    posicion_x = posicion_x + n

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
    print("RETO 4: Usando funciones (ejemplo L)")
    adelante(5)
    abajo(3)
    mostrar_flecha()

    # Reto 5: La tortuga baja las escalas

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
