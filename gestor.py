tareas = []

def crear_tarea(nombre):
    tarea = {"id": len(tareas) + 1, "nombre": nombre, "completada": False}
    tareas.append(tarea)
    print(f"Tarea '{nombre}' creada.")

def listar_tareas():
    if not tareas:
        print("No hay tareas.")
        return
    print(f"\n{'ID':<4} {'Estado':<12} {'Tarea'}")
    print("-" * 40)
    for t in tareas:
        estado = "[x]" if t["completada"] else "[ ]"
        print(f"{t['id']:<4} {estado:<12} {t['nombre']}")

def mostrar_menu():
    print("\n===== Gestor de Tareas =====")
    print("1. Crear tarea")
    print("2. Ver tareas")
    print("3. Salir")
    print("============================")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            nombre = input("Nombre de la tarea: ").strip()
            if nombre:
                crear_tarea(nombre)
            else:
                print("El nombre no puede estar vacio.")
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            print("Bye!")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()
