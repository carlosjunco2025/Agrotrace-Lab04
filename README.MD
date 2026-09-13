# AgroTrace

Sistema web para la gestión de acopio y trazabilidad de materia prima agrícola, desarrollado con Django, Django ORM y SQLite. Proyecto iniciado en el laboratorio GLAB-S03 (persistencia con Models, migraciones y ORM) y ampliado en el laboratorio GLAB-S04 (relaciones OneToOneField, ForeignKey y ManyToManyField con modelo intermedio).

## Problemática

En el sector agroexportador peruano, muchas empresas procesadoras adquieren materia prima de diversos fundos y pequeños productores rurales utilizando registros físicos o planillas desarticuladas. Esta falta de centralización dificulta garantizar el origen exacto de los productos exigido por los mercados internacionales, genera demoras al evaluar la calidad y los porcentajes de descarte, y complica la verificación de certificaciones agrícolas vigentes por lote.

**AgroTrace** digitaliza la recepción de cosechas, el control de calidad y la trazabilidad de certificaciones desde el campo hasta el almacén.

## Modelo de datos

El sistema cuenta con **7 entidades**:

**Entidades independientes**
- `CentroAcopio`
- `VariedadCultivo`
- `CertificacionAgricola`

**Entidades relacionadas**
- `FundoProductor` — origen de la materia prima.
- `LoteRecepcionado` — cada entrega física recibida, vinculada a su fundo de origen.
- `EvaluacionCalidadLote` — ficha complementaria de control de calidad de un lote.
- `CertificacionLote` — modelo intermedio que registra la auditoría de una certificación sobre un lote específico.

### Relaciones implementadas

| Tipo | Entidades | Campo | related_name | on_delete |
|---|---|---|---|---|
| 1:N (ForeignKey) | FundoProductor → LoteRecepcionado | `fundo` | `lotes` | CASCADE |
| 1:1 (OneToOneField) | LoteRecepcionado → EvaluacionCalidadLote | `lote` | `evaluacion_calidad` | CASCADE |
| N:M (ManyToManyField + through) | LoteRecepcionado ↔ CertificacionAgricola, vía CertificacionLote | `certificaciones` | `lotes` | CASCADE (en ambas FK del intermedio) |

**Justificación de negocio:**

- **1:N** — Un fundo agrícola entrega su cosecha en múltiples camiones a lo largo de la temporada, generando muchos lotes distintos que deben rastrearse hasta su origen para efectos de pago y auditoría.
- **1:1** — La evaluación de calidad (grados Brix, firmeza del fruto) la realiza el área de control de calidad en un momento posterior y opcional respecto al ingreso del lote, por lo que se modela como una ficha complementaria y no como campos adicionales del lote.
- **N:M** — Un mismo lote puede cumplir varias normas de calidad exigidas por distintos mercados de destino, y cada auditoría de una certificación sobre un lote específico tiene su propia fecha y código de inspección, información que solo tiene sentido en el cruce de ambas entidades — de ahí el modelo intermedio `CertificacionLote`.

## Tecnologías utilizadas

- Python 3.10+
- Django 5 / 6
- Django ORM
- SQLite
- Bootstrap 5 (interfaz web)

## Funcionalidades implementadas

CRUD completo (Crear, Leer, Actualizar, Eliminar) mediante Django ORM para:

- **Fundos Productores** (`/agrotrace/fundos/`)
- **Lotes Recepcionados** (`/agrotrace/lotes/`), con visualización de datos relacionados (fundo, evaluación de calidad y certificaciones) mediante `select_related()` y `prefetch_related()`.
- **Certificaciones de Lote** (`/agrotrace/certificaciones-lote/`) — CRUD del modelo intermedio de la relación N:M, permitiendo asignar, editar y eliminar la auditoría de una certificación sobre un lote junto con sus atributos propios (`fecha_auditoria`, `codigo_inspeccion`).

## Instalación y ejecución

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd Agrotrace-Lab04

# Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Crear superusuario (opcional, para acceder al admin)
python manage.py createsuperuser

# Levantar el servidor de desarrollo
python manage.py runserver
```

Luego abrir en el navegador:
- `http://127.0.0.1:8000/agrotrace/fundos/`
- `http://127.0.0.1:8000/agrotrace/lotes/`
- `http://127.0.0.1:8000/agrotrace/certificaciones-lote/`
- `http://127.0.0.1:8000/admin/` (panel de administración)

## Autor

- Carlos Fernando, Junco Santiago (C24 - D IV)
- Gael Matteo, La Jara Barboza (C24 - D IV)
