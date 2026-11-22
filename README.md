# ae1bim-oct25-feb26


## Descripción del proyecto

Este proyecto desarrolla un sistema de gestión de información para una red de clínicas veterinarias utilizando **Python, SQLite y SQLAlchemy (ORM)**.

El objetivo es aplicar los conceptos de mapeo objeto-relacional (ORM) para crear entidades, establecer relaciones, insertar registros y realizar consultas sobre una base de datos relacional.

El proyecto corresponde a la actividad experimental AE1 de la Unidad 3: Acceso a bases de datos relacionales mediante ORM.

## Tecnologías utilizadas

- **Python:** lenguaje de programación principal.
- **SQLite:** sistema de gestión de base de datos relacional.
- **SQLAlchemy:** biblioteca ORM para gestionar entidades y consultas.
- **Git y GitHub:** control de versiones del proyecto.

## Requisitos e instalación del proyecto

Esta sección explica cómo instalar, configurar y ejecutar el Sistema de Gestión de Clínicas Veterinarias desde cero.

El proyecto utiliza **Python, SQLite y SQLAlchemy ORM**. Fue desarrollado en un entorno Linux mediante WSL (Windows Subsystem for Linux).

### 1. Tecnologías utilizadas

| Tecnología | Descripción | Instalación |
|---|---|---|
| Python 3 | Lenguaje de programación principal | Obligatoria |
| SQLite 3 | Base de datos relacional | Incluida en Python |
| SQLAlchemy 2.x | ORM para gestionar entidades y consultas | Obligatoria |
| pip | Administrador de paquetes de Python | Obligatoria |
| venv | Entorno virtual de Python | Recomendado |
| Git | Clonación y control de versiones | Recomendado |
| Visual Studio Code | Editor de código | Opcional |
| DB Browser for SQLite | Visualización gráfica de la base de datos | Opcional |

No se requiere instalar MySQL, PostgreSQL, XAMPP ni servidores web.

### 2. Instalar las herramientas en Linux

Los siguientes comandos están dirigidos a Ubuntu o Debian.

Actualizar los repositorios:

```bash
sudo apt update
```

Instalar Python, pip y el módulo para crear entornos virtuales:

```bash
sudo apt install python3 python3-pip python3-venv -y
```

Instalar Git y la herramienta de consola de SQLite:

```bash
sudo apt install git sqlite3 -y
```

Verificar las instalaciones:

```bash
python3 --version
python3 -m pip --version
git --version
sqlite3 --version
```

**Nota:** si algún paquete no está disponible, se debe revisar la versión de Linux y los repositorios configurados antes de continuar.

### 3. Descargar el proyecto desde GitHub

Clonar el repositorio:

```bash
git clone https://github.com/taw-desarrollo-plataformas-web/ae1bim-oct26-feb27.git
```

Ingresar al directorio:

```bash
cd ae1bim-oct26-feb27
```

Si el proyecto se descargó como ZIP, simplemente descomprimirlo y abrir su carpeta desde la terminal.

### 4. Crear y activar el entorno virtual

Dentro de la carpeta principal del proyecto, ejecutar:

```bash
python3 -m venv .venv
```

Activar el entorno virtual:

```bash
source .venv/bin/activate
```

Cuando el entorno esté activo, aparecerá `(.venv)` al inicio de la terminal.

Para desactivarlo:

```bash
deactivate
```

### 5. Instalar las dependencias

Con el entorno virtual activado, instalar las dependencias declaradas en el proyecto:

```bash
python -m pip install -r requirements.txt
```

El archivo `requirements.txt` debe incluir SQLAlchemy y sus dependencias necesarias.

Si se desea instalar SQLAlchemy manualmente:

```bash
python -m pip install SQLAlchemy
```

Comprobar su instalación:

```bash
python -c "import sqlalchemy; print(sqlalchemy.__version__)"
```

Verificar que no existan conflictos entre dependencias:

```bash
python -m pip check
```

Para generar o actualizar `requirements.txt` desde el entorno virtual:

```bash
python -m pip freeze > requirements.txt
```

### 6. Crear la base de datos SQLite

El sistema utiliza una base de datos local denominada:

`veterinaria.db`

Para crear las tablas mediante SQLAlchemy ORM:

```bash
python crear_base_entidades.py
```

Se generan cuatro entidades:

- **Clínicas:** información de las clínicas veterinarias.
- **Consultorios:** especialidades y asociación con una clínica.
- **Veterinarios:** profesionales asociados a un consultorio.
- **Historias clínicas:** diagnósticos y tratamientos asociados a un veterinario.

Las entidades están relacionadas mediante claves foráneas.

### 7. Insertar información de prueba

Ejecutar:

```bash
python poblar_base.py
```

El programa inserta los siguientes registros iniciales:

| Entidad | Cantidad |
|---|---:|
| Clínicas | 3 |
| Consultorios | 4 |
| Veterinarios | 5 |
| Historias clínicas | 6 |

El script comprueba si ya existen clínicas para evitar duplicar los datos iniciales al ejecutarlo nuevamente.

### 8. Ejecutar las consultas ORM

El sistema implementa las cinco consultas solicitadas en la actividad.

**Consulta ALL:** obtiene todas las clínicas y muestra el número de historias clínicas asociadas.

```bash
python consulta_all.py
```

**Consulta FILTER:** filtra veterinarios por especialidad.

```bash
python consulta_filter.py
```

**Consulta ORDER BY:** ordena las clínicas alfabéticamente.

```bash
python consulta_order_by.py
```

**Consulta OR:** busca historias clínicas que cumplan una de dos condiciones.

```bash
python consulta_or.py
```

**Consulta AND:** busca consultorios que cumplan simultáneamente dos condiciones.

```bash
python consulta_and.py
```

### 9. Ejecutar el menú interactivo

Se desarrolló un menú de consola para ejecutar las consultas desde una sola interfaz.

Iniciar el programa:

```bash
python main.py
```

El menú presenta las siguientes opciones:

```text
=======================================================
       SISTEMA DE CLÍNICAS VETERINARIAS
=======================================================

1. Consultar todas las clínicas (ALL)
2. Filtrar veterinarios (FILTER)
3. Ordenar clínicas (ORDER BY)
4. Consultar diagnósticos (OR)
5. Consultar consultorios (AND)
6. Salir

=======================================================
Seleccione una opción (1-6):
```

El usuario puede seleccionar una consulta, visualizar sus resultados y regresar al menú principal sin reiniciar el programa.

### 10. Verificar la base de datos

Para comprobar que las tablas existen, ejecutar:

```bash
sqlite3 veterinaria.db ".tables"
```

Para consultar los registros de clínicas:

```bash
sqlite3 veterinaria.db "SELECT * FROM clinicas;"
```

También se puede utilizar DB Browser for SQLite para inspeccionar gráficamente las tablas y sus registros.

### 11. Orden correcto de ejecución

En una instalación nueva, ejecutar los siguientes comandos desde la carpeta del proyecto:

```bash
# Crear el entorno virtual
python3 -m venv .venv

# Activar el entorno
source .venv/bin/activate

# Instalar las dependencias
python -m pip install -r requirements.txt

# Crear las tablas
python crear_base_entidades.py

# Insertar los registros iniciales
python poblar_base.py

# Iniciar el sistema interactivo
python main.py
```

Una vez creada y poblada la base de datos, para volver a utilizar el sistema normalmente solo se necesita activar el entorno virtual y ejecutar:

```bash
source .venv/bin/activate
python main.py
```

### 12. Solución de problemas frecuentes

**Error: `No module named sqlalchemy`**

Verificar que el entorno virtual esté activado e instalar SQLAlchemy:

```bash
python -m pip install SQLAlchemy
```

**Error: `No such file or directory: requirements.txt`**

Verificar que se está ejecutando el comando desde la carpeta principal del proyecto y que existe el archivo `requirements.txt`.

**Error: `python: command not found`**

Utilizar `python3` si el entorno virtual no está activado.

**Error: `No module named venv`**

Instalar el paquete de entorno virtual correspondiente a la versión de Python y distribución Linux utilizada.

**Error: `no such table`**

Comprobar que se haya ejecutado:

```bash
python crear_base_entidades.py
```

**Error: `database is locked`**

Cerrar otras conexiones o aplicaciones que estén utilizando el archivo SQLite e intentar nuevamente.

### 13. Recomendaciones para GitHub

No se deben subir al repositorio las carpetas del entorno virtual, archivos temporales ni cachés de Python.

Se recomienda agregar un archivo `.gitignore` con el siguiente contenido:

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.env
```

Para una entrega académica que solicite la base de datos poblada, se puede incluir `veterinaria.db` con los registros de ejemplo, siempre que no contenga información personal real.

### 14. Conclusión

El sistema permite administrar y consultar información de clínicas veterinarias mediante SQLAlchemy ORM y SQLite.

Se implementaron las entidades, sus relaciones, la inserción de registros, las cinco consultas ORM y un menú interactivo que facilita la ejecución del programa.

La aplicación funciona localmente, no requiere conexión a un servidor de base de datos y puede ejecutarse en otros equipos instalando las dependencias indicadas.
