
class Alumno:
    def __init__(self, matricula, calificaciones):
        self.matricula = matricula
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        # copia la lista para no modificar la original
        lista = self.calificaciones.copy()
        if len(lista) > 1:
            cal_baja = min(lista)
            lista.remove(cal_baja)

        promedio = 0
        for calificacion in lista:
            promedio += (calificacion * 0.01) * 1.25

        return promedio


# funcion extra: determina si aprobó
def aprobo(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"


# lista de alumnos
alumnos = []


def registrar_alumno():
    matricula = input("Ingresa matrícula del alumno: ")

    calificaciones = []
    for i in range(5):
        cal = float(input(f"Ingrese calificación {i+1}: "))
        calificaciones.append(cal)

    alumnos.append(Alumno(matricula, calificaciones))
    print("Alumno registrado!\n")


def consultar_alumnos():
    if not alumnos:
        print("No hay alumnos registrados.\n")
    else:
        for i, al in enumerate(alumnos):
            prom = al.calcular_promedio()
            print(f"{i+1}. Matrícula: {al.matricula} - Calificaciones: {al.calificaciones} - Promedio: {prom} - {aprobo(prom)}")
    print()


def modificar_alumno():
    consultar_alumnos()
    if alumnos:
        idx = int(input("Elige el número del alumno a modificar: ")) - 1
        if 0 <= idx < len(alumnos):
            nuevas_calificaciones = []
            for i in range(5):
                cal = float(input(f"Ingresa nueva calificación {i+1}: "))
                nuevas_calificaciones.append(cal)
            alumnos[idx].calificaciones = nuevas_calificaciones
            print("Calificaciones actualizadas!\n")


def eliminar_alumno():
    consultar_alumnos()
    if alumnos:
        idx = int(input("Elige el número del alumno a eliminar: ")) - 1
        if 0 <= idx < len(alumnos):
            alumnos.pop(idx)
            print("Alumno eliminado!\n")


# menu principal
while True:
    print("=== MENU ALUMNOS ===")
    print("1. Registrar alumno")
    print("2. Consultar alumnos")
    print("3. Modificar alumno")
    print("4. Eliminar alumno")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        registrar_alumno()
    elif opcion == "2":
        consultar_alumnos()
    elif opcion == "3":
        modificar_alumno()
    elif opcion == "4":
        eliminar_alumno()
    elif opcion == "5":
        print("Adios!")
        break
    else:
        print("Opción no válida\n")
