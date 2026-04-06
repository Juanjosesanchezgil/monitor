# Inventario API con FastAPI

Sistema de gestión de artículos y categorías con persistencia en SQLite.

## Requisitos
- Python 3.10+
- FastAPI
- SQLAlchemy 2.0

## Instalación
1. Clonar repositorio
2. `pip install -r requirements.txt`
3. `uvicorn app.main:app --reload`

## Endpoints Principales
- `POST /categorias`: Crear familia de productos.
- `POST /articulos`: Crear producto asociado a categoría.
- `GET /docs`: Documentación interactiva (Swagger).