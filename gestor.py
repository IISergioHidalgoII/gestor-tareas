import json
import os

#==================== Constantes ====================

ARCHIVO = "tareas.json"

#==================== Funciones ====================

def cargar_tareas():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_tareas():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=2)

ESTADOS = {
    "1": ("--", "Pendiente"),
    "2": ("o",  "Completada"),
    "3": ("x",  "Rechazada"),
}

tareas = cargar_tareas()

def crear_tarea(nombre):
    id_nuevo = max((t["id"] for t in tareas), default=0) + 1
    tarea = {"id": id_nuevo, "nombre": nombre, "estado": "--"}
    tareas.append(tarea)
    guardar_tareas()
    print(f"Tarea '{nombre}' creada.")

def listar_tareas():
    if not tareas:
        print("No hay tareas.")
        return
    print(f"\n{'ID':<4} {'Estado':<14} {'Tarea'}")
    print("-" * 45)
    for t in tareas:
        estado_simbolo = t.get("estado", "--")
        etiqueta = next((v[1] for v in ESTADOS.values() if v[0] == estado_simbolo), "Pendiente")
        print(f"{t['id']:<4} [{estado_simbolo}] {etiqueta:<10} {t['nombre']}")

def cambiar_estado():
    listar_tareas()
    if not tareas:
        return
    try:
        id_tarea = int(input("\nID de tarea a actualizar: "))
        tarea = next((t for t in tareas if t["id"] == id_tarea), None)
        if not tarea:
            print("No se encontro la tarea.")
            return
        print("\nNuevo estado:")
        for k, (simbolo, nombre) in ESTADOS.items():
            print(f"  {k}. [{simbolo}] {nombre}")
        opcion = input("Selecciona: ").strip()
        if opcion in ESTADOS:
            tarea["estado"] = ESTADOS[opcion][0]
            guardar_tareas()
            print(f"Estado actualizado a [{ESTADOS[opcion][0]}] {ESTADOS[opcion][1]}.")
        else:
            print("Opcion no valida.")
    except ValueError:
        print("Entrada invalida.")

def editar_tarea():
    listar_tareas()
    if not tareas:
        return
    try:
        id_tarea = int(input("\nID de tarea a editar: "))
        tarea = next((t for t in tareas if t["id"] == id_tarea), None)
        if not tarea:
            print("No se encontro la tarea.")
            return
        nuevo_nombre = input(f"Nombre [{tarea['nombre']}]: ").strip()
        if nuevo_nombre:
            tarea["nombre"] = nuevo_nombre
        guardar_tareas()
        print("Tarea actualizada.")
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
            guardar_tareas()
            print(f"Tarea '{tarea['nombre']}' eliminada.")
        else:
            print("No se encontro la tarea.")
    except ValueError:
        print("Entrada invalida.")

#==================== Menu principal ====================

def mostrar_menu():
    print("\n===== Gestor de Tareas =====")
    print("1. Crear tarea")
    print("2. Ver tareas")
    print("3. Cambiar estado")
    print("4. Editar nombre")
    print("5. Eliminar tarea")
    print("6. Salir")
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
            cambiar_estado()
        elif opcion == "4":
            editar_tarea()
        elif opcion == "5":
            eliminar_tarea()
        elif opcion == "6":
            print("Bye!")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()
