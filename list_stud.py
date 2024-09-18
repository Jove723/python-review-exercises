estudiantes = {
    "Ana": 85,
    "Luis": 90,
    "Marta": 78
}

def agregar_estudiante(diccionario, nombre, calificacion):
    diccionario[nombre] = calificacion
    print(f"Estudiante {nombre} añadido con una calificación de {calificacion}.")

def eliminar_estudiante(diccionario, nombre):
    if nombre in diccionario:
        del diccionario[nombre]
        print(f"El usuario {nombre} ha sido elimidado")
    else:
        print(f"El usuario {nombre} no ha sido encontrado")

def mostrar_estudiantes(diccionario):
    if diccionario:
        print("Lista de estudiantes y calificaciones:")
        for nombre, calificacion in diccionario.items():
            print(f"{nombre}: {calificacion}")
    else:
        print("No hay estudiantes en la lista")



agregar_estudiante(estudiantes, "juan", 70)

eliminar_estudiante(estudiantes, "Ana")

mostrar_estudiantes(estudiantes)

