# 📦 Sistema de Inventario API (FastAPI + SQLAlchemy)

API profesional para la gestión de inventarios, desarrollada con una arquitectura limpia y persistencia de datos relacional.

## 🚀 Tecnologías Utilizadas
- **FastAPI**: Framework web de alto rendimiento.
- **SQLAlchemy 2.0**: ORM moderno con soporte para `Mapped` y `mapped_column`.
- **SQLite**: Base de datos ligera y eficiente.
- **Pydantic v2**: Validación de datos y esquemas.
- **Python-dotenv**: Gestión de variables de entorno.

## 🏗️ Arquitectura del Proyecto
El proyecto sigue una estructura modular para facilitar el mantenimiento:
- `app/models.py`: Definición de tablas y relaciones (Uno a Muchos).
- `app/schemas.py`: Modelos de datos para validación de entrada/salida.
- `app/database.py`: Configuración de la conexión y sesión de DB.
- `app/main.py`: Lógica de endpoints y manejo de excepciones.

## 🛠️ Instalación y Uso
1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`.
3. Instalar dependencias: `pip install -r requirements.txt`.
4. Configurar `.env` con `DATABASE_URL=sqlite:///./sql_app.db`.
5. Ejecutar: `uvicorn app.main:app --reload`.

Accede a la documentación interactiva en: `http://127.0.0.1:8000/docs`