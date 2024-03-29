import requests
import json
import emoji


class Estudiante:
    def __init__(self, nombre, correo, carrera, matricula=None):
        self.nombre = nombre
        self.correo = correo
        self.carrera = carrera
        self.matricula = matricula

    def __str__(self):
        estudiante = "Nombre: " + str(self.nombre) + "\nMatricula: " + str(
            self.matricula) + "\nCorreo: " + str(self.correo) + "\nCarrera: " + str(self.carrera)
        return estudiante


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def print_menu():
    print()
    print("-------------------- REST Api " +
          emoji.emojize(":grinning_face_with_big_eyes:") + "  ----------------------")
    print("| Eliga la opción deseada en las siguientes opciones: |")
    print("| 1. Lista de Estudiantes                             |")
    print("| 2. Información de Estudiante                        |")
    print("| 3. Crear estudiante                                 |")
    print("| 0. Exit                                             |")
    print("-------------------------------------------------------")


def get_estudiantes():
    req = requests.get('http://localhost:4567/rest/estudiantes/')
    jprint(req.json())
    print()


def post_estudiante():
    nombre = input("\nInserte nombre del estudiante: ")
    correo = input("Inserte correo del estudiante: ")
    carrera = input("Inserte carrera del estudiante: ")
    estudiante = Estudiante(nombre, correo, carrera)
    try:
        requests.post('http://localhost:4567/rest/estudiantes/',
                      json=estudiante.__dict__)
        print("Se ha creado exitosamente. ")
        print()
    except:
        print("La creación de estudiante no funciono. ")


def get_estudiante():
    matricula = int(input("Inserte la matricula del estudiante: "))
    response = requests.get(
        "http://localhost:4567/rest/estudiantes/" + str(matricula))
    estudiante = Estudiante(
        response.json()["nombre"], response.json()["correo"], response.json()["carrera"], response.json()["matricula"])
    print("\n" + str(estudiante))
    return estudiante


opcion = -1
while True:
    print_menu()
    opcion = int(input("Opción tomada: "))

    if opcion == 0:
        break
    elif opcion == 1:
        get_estudiantes()
    elif opcion == 2:
        get_estudiante()
    elif opcion == 3:
        post_estudiante()
