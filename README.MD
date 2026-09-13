# AgroTrace

Sistema web para la gestión de acopio y trazabilidad de materia prima agrícola, desarrollado con Django, Django ORM y SQLite como parte del laboratorio GLAB-S03 (Desarrollo de Aplicaciones Empresariales).

## Problemática

En el sector agroexportador peruano, específicamente en la cadena de suministro de productos como la palta y el mango, muchas empresas procesadoras adquieren materia prima de diversos fundos y pequeños productores rurales utilizando registros físicos o planillas desarticuladas. Esta falta de centralización dificulta garantizar el origen exacto de los productos exigido por los mercados internacionales, genera demoras al evaluar los porcentajes de descarte por calidad y complica la liquidación de pagos a los agricultores.

**AgroTrace** digitaliza la recepción de cosechas y el control de calidad desde el campo hasta el almacén, permitiendo:

- Registrar los fundos productores de origen y su condición para exportación.
- Registrar cada lote de materia prima recibido, vinculado obligatoriamente a su fundo de origen.
- Consultar, actualizar y eliminar esta información de manera centralizada y persistente.

## Usuarios involucrados

- **Auditor de calidad / Ingeniero de campo:** inspecciona los predios y verifica las certificaciones agrícolas.
- **Jefe de centro de acopio:** realiza el pesaje en balanza, el registro de lotes y la evaluación de merma.
- **Administrador de la agroexportadora:** supervisa el volumen consolidado, aprueba el estado de cada lote y gestiona las liquidaciones comerciales.

## Requisitos funcionales principales

- RF-01 / RF-02: Registrar y listar centros de acopio.
- RF-03 / RF-04: Registrar variedades de cultivo y consultar certificaciones agrícolas.
- RF-05 / RF-06: Registrar y listar fundos productores, filtrando por condición de exportación.
- RF-07 / RF-08: Actualizar y eliminar fundos productores.
- RF-09 / RF-10: Registrar y listar lotes recepcionados, vinculados a su fundo de origen.
- RF-11 / RF-12: Actualizar el estado de evaluación de un lote y eliminar registros duplicados o erróneos.

## Modelo de datos

El sistema define 5 entidades:

**Entidades independientes**
- `CentroAcopio`
- `VariedadCultivo`
- `CertificacionAgricola`

**Entidades relacionadas (ForeignKey)**
- `FundoProductor` (padre)
- `LoteRecepcionado` (hija, vinculada a `FundoProductor` mediante `fundo_id`)

Un fundo agrícola puede entregar múltiples lotes de materia prima a lo largo de una campaña (relación 1:N), garantizando la trazabilidad completa desde la planta hasta el predio de origen.

## Tecnologías utilizadas

- Python 3.10+
- Django 5
- Django ORM
- SQLite
- Bootstrap 5 (interfaz web)

## Funcionalidades implementadas

CRUD completo (Crear, Leer, Actualizar, Eliminar) mediante Django ORM para:

- **Fundos Productores** (`/agrotrace/fundos/`)
- **Lotes Recepcionados** (`/agrotrace/lotes/`)

Cada operación reemplaza el manejo de datos en memoria por persistencia real en SQLite, utilizando `Model.objects.all()`, `.create()`, `.get_object_or_404()` y `.delete()` según corresponda.

## Instalación y ejecución

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd lab03-agrotrace-project

# Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario (opcional, para acceder al admin)
python manage.py createsuperuser

# Levantar el servidor de desarrollo
python manage.py runserver
```

Luego abrir en el navegador:
- `http://127.0.0.1:8000/agrotrace/fundos/`
- `http://127.0.0.1:8000/agrotrace/lotes/`
- `http://127.0.0.1:8000/admin/` (panel de administración)

## Autor

- Carlos Fernando, Junco Santiago (C24 - D IV)
- Gael Matteo, La Jara Barboza (C24 - D IV)
