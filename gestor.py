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

def completar_tarea():
    listar_tareas()
    if not tareas:
        return
    try:
        id_tarea = int(input("\nID de tarea a completar: "))
        tarea = next((t for t in tareas if t["id"] == id_tarea), None)
        if tarea:
            tarea["completada"] = True
            print(f"Tarea '{tarea['nombre']}' marcada como completada.")
        else:
            print("No se encontro la tarea.")
    except ValueError:
        print("Entrada invalida.")

def eliminar_tarea():
    listar_tareas()
    if not tareas:
        return
    try:
        id_tarea = int(input("\nID de tarea a eliminar: "))
        tarea = next((t for t in tareas if t["id"] == id_tarea), None)
        if tarea:
            tareas.remove(tarea)
            print(f"Tarea '{tarea['nombre']}' eliminada.")
        else:
            print("No se encontro la tarea.")
    except ValueError:
        print("Entrada invalida.")

def mostrar_menu():
    print("\n===== Gestor de Tareas =====")
    print("1. Crear tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
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
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Bye!")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()
