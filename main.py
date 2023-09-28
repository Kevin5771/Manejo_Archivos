
def presentacion():
    print("Bienvenido a Nuestro Sistema de Agenda de Tareas")
    print("************************************************")

def cargar_tareas(archivo):
    try:
        with open(archivo, "r") as archivos:
            tareas = [line.strip().split(',') for line in archivos.readlines()]
    except FileNotFoundError:
        tareas = []
    return tareas

def guardar_tareas(archivo, tareas):
    with open(archivo, "w") as guardar:
        for tarea in tareas:
            guardar.write(','.join(tarea) + '\n')

def agregar_tarea(tareas):
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento (dd-mm-aaaa) o presione Enter para omitir: ")
    tarea = [titulo, descripcion, "False", 
             fecha_vencimiento 
             if fecha_vencimiento 
             else 'Sin fecha']
    tareas.append(tarea)
    print("Tarea agregada con éxito.\n")

def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas Pendientes:\n")
        for index, tarea in enumerate(tareas, 1):
            print(f"Tarea {index}:")
            print(f"Título: {tarea[0]}")
            print(f"Descripción: {tarea[1]}")
            print(f"Completada: {'Sí' if tarea[2] == 'True' else 'No'}")
            print(f"Fecha de Vencimiento: {tarea[3]}\n")

def marcar_completada(tareas):
    listar_tareas(tareas)
    num_tarea = input("Ingrese el número de la tarea que desea marcar como completada: ")
    try:
        num_tarea = int(num_tarea)
        if 1 <= num_tarea <= len(tareas):
            tarea = tareas[num_tarea - 1]
            if tarea[2] == 'False':
                tarea[2] = 'True'
                print("Tarea marcada como completada.\n")
            else:
                print("La tarea ya está marcada como completada.\n")
        else:
            print("Número de tarea no válido.\n")
    except ValueError:
        print("Número de tarea no válido.\n")

# Bloque Principal

tareas_pendientes = cargar_tareas("tareas_pendientes.txt")

while True:
    presentacion()
    print("Gestión de Tareas Pendientes")
    print("1. Agregar Tarea")
    print("2. Listar Tareas")
    print("3. Marcar Tarea como Completada")
    print("4. Salir")
    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        agregar_tarea(tareas_pendientes)
    elif opcion == "2":
        print("*******************************")
        listar_tareas(tareas_pendientes)
        print("*******************************")
    elif opcion == "3":
        marcar_completada(tareas_pendientes)
    elif opcion == "4":
        guardar_tareas("tareas_pendientes.txt", tareas_pendientes)
        print("¡Adiós!")
        print("Gracias por usar nuestro Servicio de Agenda")
        break
    else:
        print("Opción no válida. Por favor, elija 1, 2, 3 o 4.\n")
