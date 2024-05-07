class Palabra:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


def construir_arbol():
    # Creamos el árbol de adivinanzas
    raiz = Palabra("¿Vive en el agua?")
    raiz.izquierda = Palabra("pez")
    raiz.derecha = Palabra("¿Tiene alas?")
    raiz.derecha.izquierda = Palabra("Ave")
    raiz.derecha.derecha = Palabra("¿Es un animal grande y tiene cuernos?")
    raiz.derecha.derecha.izquierda = Palabra("toro")
    raiz.derecha.derecha.derecha = Palabra("elefante")
    return raiz


def jugar_arbol(intento):
    if intento is None:
        return

    print(intento.dato)
    respuesta = input("(sí/no): ").lower()
    if respuesta == 'sí':
        jugar_arbol(intento.izquierda)
    elif respuesta == 'no':
        jugar_arbol(intento.derecha)
    else:
        print("Por favor responde con 'sí' o 'no'.")
        jugar_arbol(intento)

# Ejemplo de uso:
arbol = construir_arbol()
jugar_arbol(arbol)
jugar_nuevamente = input("¿Quieres volver a jugar? (sí/no): ").lower()
while jugar_nuevamente == 'sí':
    arbol = construir_arbol()
    jugar_arbol(arbol)
    jugar_nuevamente = input("¿Quieres volver a jugar? (sí/no): ").lower()
print("Termino el juego.")



