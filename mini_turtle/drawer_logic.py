# drawer_logic.py
# Lógica interna del paquete mini_turtle 
posicion_x = 0

def reiniciar():
    """Restablece la posición horizontal global a 0."""
    global posicion_x
    posicion_x = 0

def adelante(n):
    """
    Dibuja una línea horizontal de longitud n desde la posición actual
    y mueve la posición global hacia la derecha.
    """
    global posicion_x
    if n <= 0:
        return
    print(" " * posicion_x + "-" * n + ">")
    posicion_x += n

def abajo(n):
    """
    Dibuja n líneas verticales bajo la columna actual y coloca 'v' al final.
    """
    global posicion_x
    if n <= 0:
        print(" " * posicion_x + "v")
        return
    for _ in range(n):
        print(" " * posicion_x + "|")
    print(" " * posicion_x + "v")
