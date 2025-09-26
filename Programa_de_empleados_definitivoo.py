
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_impuesto(self):
        if self.salario > 3000:
            return self.salario * 0.04
        else:
            return 0

    def salario_neto(self):
        return self.salario - self.calcular_impuesto()


# funcion extra
def pesos_a_dolares(pesos):
    return pesos / 18.5


# lista de empleados
empleados = []


def registrar_empleado():
    nombre = input("Nombre del empleado: ")
    salario = float(input("Salario semanal: "))
    empleados.append(Empleado(nombre, salario))
    print("Empleado registrado!\n")


def consultar_empleados():
    if not empleados:
        print("No hay empleados registrados.\n")
    else:
        for i, emp in enumerate(empleados):
            print(f"{i+1}. {emp.nombre} - Bruto: {emp.salario} - Neto: {emp.salario_neto()}")
    print()


def modificar_empleado():
    consultar_empleados()
    if empleados:
        idx = int(input("Elige el número del empleado a modificar: ")) - 1
        if 0 <= idx < len(empleados):
            nuevo_salario = float(input("Nuevo salario: "))
            empleados[idx].salario = nuevo_salario
            print("Salario modificado!\n")


def eliminar_empleado():
    consultar_empleados()
    if empleados:
        idx = int(input("Elige el número del empleado a eliminar: ")) - 1
        if 0 <= idx < len(empleados):
            empleados.pop(idx)
            print("Empleado eliminado!\n")


# menu principal
while True:
    print("=== MENU EMPLEADOS ===")
    print("1. Registrar empleado")
    print("2. Consultar empleados")
    print("3. Modificar empleado")
    print("4. Eliminar empleado")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        registrar_empleado()
    elif opcion == "2":
        consultar_empleados()
    elif opcion == "3":
        modificar_empleado()
    elif opcion == "4":
        eliminar_empleado()
    elif opcion == "5":
        print("Adios!")
        break
    else:
        print("Opcion no valida\n")
