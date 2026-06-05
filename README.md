# Gestor de Tareas

Aplicacion demtro de consola para gestionar tareas con opciones de crear, listar, completar y eliminar. Los datos persisten en `tareas.json`.

## Como ejecutar

```bash
python gestor.py
```

## Funciones

| Funcion | Que hace |
|---|---|
| `cargar_tareas()` | Lee `tareas.json` y retorna la lista. Si no existe, retorna lista vacia |
| `guardar_tareas()` | Escribe la lista de tareas en `tareas.json` |
| `crear_tarea(nombre)` | Crea una tarea con ID unico y estado pendiente |
| `listar_tareas()` | Muestra todas las tareas con su ID, estado y nombre |
| `completar_tarea()` | Marca una tarea como completada por ID |
| `eliminar_tarea()` | Elimina una tarea por ID |
| `mostrar_menu()` | Imprime el menu de opciones |
| `main()` | Carga las tareas y controla el flujo en un bucle |

## Diagrama de flujo

```
Inicio
  │
  V
cargar_tareas() ──> lee tareas.json (o lista vacia)
  │
  V
mostrar_menu()
  │
  V
Opcion?
  ├─ "1" ──> input nombre ──> crear_tarea() ──> guardar_tareas() ──> menu
  │
  ├─ "2" ──> listar_tareas() ─────────────────────────────────────> menu
  │
  ├─ "3" ──> listar_tareas()
  │               │
  │               V
  │          input ID ──> completar_tarea() ──> guardar_tareas() ──> menu
  │
  ├─ "4" ──> listar_tareas()
  │               │
  │               V
  │          input ID ──> eliminar_tarea() ──> guardar_tareas() ──> menu
  │
  ├─ "5" ──> Salir
  │
  └─ otra ──> "Opcion no valida" ──────────────────────────────────> menu
```

## Estructura de datos

Cada tarea se almacena como objeto en `tareas.json`:

```json
[
  {
    "id": 1,
    "nombre": "Estudiar Python",
    "completada": false
  }
]
```

## Tecnologias

- Python 3
- Modulo `json` (estandar)
- Modulo `os` (estandar)
