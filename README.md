# Gestor de Tareas

Aplicacion de consola para gestionar tareas con estados personalizados, edicion de nombre y persistencia en `tareas.json`.

## Como ejecutar

```bash
python gestor.py
```

## Funciones

| Funcion | Que hace |
|---|---|
| `cargar_tareas()` | Lee `tareas.json` y retorna la lista. Si no existe, retorna lista vacia |
| `guardar_tareas()` | Escribe la lista de tareas en `tareas.json` |
| `crear_tarea(nombre)` | Crea una tarea con ID unico y estado `[--]` Pendiente |
| `listar_tareas()` | Muestra todas las tareas con su ID, simbolo de estado y nombre |
| `cambiar_estado()` | Cambia el estado de una tarea por ID con opciones del menu |
| `editar_tarea()` | Edita el nombre de una tarea por ID |
| `eliminar_tarea()` | Elimina una tarea por ID |
| `mostrar_menu()` | Imprime el menu de opciones |
| `main()` | Carga las tareas y controla el flujo en un bucle |

## Diagrama de flujo

```
Inicio
  |
  V
cargar_tareas() -> lee tareas.json (o lista vacia)
  |
  V
mostrar_menu()
  |
  V
Opcion?
  |- "1" -> input nombre -> crear_tarea() -> guardar_tareas() -> menu
  |
  |- "2" -> listar_tareas() ----------------------------------------> menu
  |
  |- "3" -> listar_tareas()
  |              |
  |              V
  |         input ID -> seleccionar estado -> cambiar_estado() -> guardar_tareas() -> menu
  |
  |- "4" -> listar_tareas()
  |              |
  |              V
  |         input ID -> input nuevo nombre -> editar_tarea() -> guardar_tareas() -> menu
  |
  |- "5" -> listar_tareas()
  |              |
  |              V
  |         input ID -> eliminar_tarea() -> guardar_tareas() -> menu
  |
  |- "6" -> Salir
  |
  `- otra -> "Opcion no valida" -----> menu
```

## Estados disponibles

| Simbolo | Significado |
|---|---|
| `[--]` | Pendiente |
| `[o]`  | Completada |
| `[x]`  | Rechazada |

## Estructura de datos

Cada tarea se almacena como objeto en `tareas.json`:

```json
[
  {
    "id": 1,
    "nombre": "Estudiar Python",
    "estado": "--"
  }
]
```

## Tecnologias

- Python 3
- Modulo `json` (estandar)
- Modulo `os` (estandar)


## Como ejecutar

```bash
python gestor.py
```

## Funciones

| Funcion | Que hace |
|---|---|
| `cargar_tareas()` | Lee `tareas.json` y retorna la lista. Si no existe, retorna lista vacia |
| `guardar_tareas()` | Escribe la lista de tareas en `tareas.json` |
| `crear_tarea(nombre)` | Crea una tarea con ID unico y estado `[--]` Pendiente |
| `listar_tareas()` | Muestra todas las tareas con su ID, simbolo de estado y nombre |
| `cambiar_estado()` | Cambia el estado de una tarea por ID con opciones del menu |
| `editar_tarea()` | Edita el nombre de una tarea por ID |
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
<<<<<<< HEAD
  │               ▼
  │          input ID ──► seleccionar estado ──► cambiar_estado() ──► guardar_tareas() ──► menu
=======
  │               V
  │          input ID ──> completar_tarea() ──> guardar_tareas() ──> menu
>>>>>>> 95c70ad2f0108c8ded4956d6a754f73b2df34d48
  │
  ├─ "4" ──> listar_tareas()
  │               │
<<<<<<< HEAD
  │               ▼
  │          input ID ──► input nuevo nombre ──► editar_tarea() ──► guardar_tareas() ──► menu
  │
  ├─ "5" ──► listar_tareas()
  │               │
  │               ▼
  │          input ID ──► eliminar_tarea() ──► guardar_tareas() ──► menu
  │
  ├─ "6" ──► Salir
=======
  │               V
  │          input ID ──> eliminar_tarea() ──> guardar_tareas() ──> menu
  │
  ├─ "5" ──> Salir
>>>>>>> 95c70ad2f0108c8ded4956d6a754f73b2df34d48
  │
  └─ otra ──> "Opcion no valida" ──────────────────────────────────> menu
```

## Estados disponibles

| Simbolo | Significado |
|---|---|
| `[--]` | Pendiente |
| `[o]` | Completada |
| `[x]` | Rechazada |

## Estructura de datos

Cada tarea se almacena como objeto en `tareas.json`:

```json
[
  {
    "id": 1,
    "nombre": "Estudiar Python",
    "estado": "--"
  }
]
```

## Tecnologias

- Python 3
- Modulo `json` (estandar)
- Modulo `os` (estandar)
