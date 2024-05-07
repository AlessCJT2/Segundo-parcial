class Nodo:
    def __init__(self, pregunta=None, respuesta=None):
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.si = None
        self.no = None

def jugar_adivinanzas(nodo, contador):
    if contador >= 5:
        print("Has alcanzado el límite de preguntas. Mi respuesta es:", nodo.respuesta)
    else:
        respuesta = input(nodo.pregunta + " (sí/no): ")
        if respuesta.lower() == "sí":
            if nodo.si is None:
                print("No puedo avanzar más. Mi respuesta es:", nodo.respuesta)
            else:
                jugar_adivinanzas(nodo.si, contador + 1)
        elif respuesta.lower() == "no":
            if nodo.no is None:
                objeto = input("No he adivinado. ¿Qué objeto, animal o personaje era? ")
                print("He aprendido algo nuevo.")
                nodo.no = Nodo(respuesta=objeto)
            else:
                jugar_adivinanzas(nodo.no, contador + 1)

# Construir el árbol de adivinanzas
raiz = Nodo(pregunta="¿Es un animal?", respuesta="perro")
raiz.si = Nodo(pregunta="¿Es un mamífero?", respuesta="gato")
raiz.no = Nodo(pregunta="¿Es un objeto?", respuesta="silla")
raiz.si.si = Nodo(pregunta="¿Es un animal doméstico?", respuesta="perro")
raiz.si.no = Nodo(pregunta="¿Vuela?", respuesta="pájaro")
raiz.no.si = Nodo(pregunta="¿Se usa en la cocina?", respuesta="cuchillo")
raiz.no.no = Nodo(pregunta="¿Es de color rojo?", respuesta="manzana")

# Iniciar el juego
print("Piensa en algo y responde las preguntas.")
jugar_adivinanzas(raiz, 0)
