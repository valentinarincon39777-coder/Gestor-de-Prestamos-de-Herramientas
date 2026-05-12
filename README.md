# 🛠️ Sistema de Préstamo de Herramientas Comunitarias

## Descripción
Este proyecto consiste en un programa de consola desarrollado en Python para administrar el préstamo de herramientas entre vecinos de una comunidad.  

El sistema permite llevar un control organizado de las herramientas disponibles, los usuarios registrados y los préstamos realizados, evitando pérdidas o desorden en el inventario.

La información se almacena utilizando archivos `.json`, permitiendo guardar los datos incluso después de cerrar el programa.

---

## Funcionalidades

### CRUD de herramientas
El sistema permite:
- Crear herramientas.
- Registrar información como nombre, categoría, cantidad disponible, estado y valor estimado.
- Consultar y listar herramientas.
- Actualizar información.
- Eliminar o inactivar herramientas.

### CRUD de usuarios
El sistema permite:
- Registrar vecinos.
- Consultar usuarios registrados.
- Actualizar información.
- Eliminar usuarios.

### Gestión de préstamos
- Registrar préstamos de herramientas.
- Verificar disponibilidad antes de prestar.
- Reducir automáticamente la cantidad disponible.
- Registrar devoluciones.
- Restaurar el stock al devolver herramientas.

### Reportes y consultas
- Herramientas con poco stock.
- Préstamos activos y vencidos.
- Historial de préstamos por usuario.
- Herramientas más solicitadas.

### Logs del sistema
El programa registra eventos importantes y errores en un archivo de texto para llevar seguimiento de las operaciones realizadas.

---

## Tecnologías utilizadas
- Python 3
- Archivos `.json`

---

## Ejecución

1. Tener instalado Python 3.
2. Abrir el proyecto en Visual Studio Code.
3. Ejecutar el archivo principal:

```bash
python main.py
```

---

## Roles del sistema

### Administrador
- Registrar usuarios y herramientas.
- Gestionar inventario.

### Usuario
- Consultar herramientas disponibles.
- Ver disponibilidad de herramientas.

---

## Objetivo
Brindar una solución sencilla y organizada para controlar el préstamo de herramientas dentro de una comunidad utilizando programación en Python.

---

## Autoría
Proyecto desarrollado por Valentina Rincón.
