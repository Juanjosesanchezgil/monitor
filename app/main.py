from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from typing import List

# Crear tablas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


# Dependencia de DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- ENDPOINTS CATEGORIAS ---
@app.post("/categorias", response_model=schemas.Categoria)
def crear_categoria(cat: schemas.CategoriaBase, db: Session = Depends(get_db)):
    # 1. Verificar si ya existe una categoría con ese nombre
    db_categoria = db.query(models.CategoriaDB).filter(
        models.CategoriaDB.nombre == cat.nombre).first()
    if db_categoria:
        raise HTTPException(status_code=400, detail="La categoría ya existe")

    nueva = models.CategoriaDB(nombre=cat.nombre)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@app.put("/categorias/{categoria_id}", response_model=schemas.Categoria)
def actualizar_categoria(categoria_id: int, cat_update: schemas.CategoriaBase,
                         db: Session = Depends(get_db)):
    db_cat = db.query(models.CategoriaDB).filter(
        models.CategoriaDB.id == categoria_id).first()
    if not db_cat:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")

    db_cat.nombre = cat_update.nombre
    db.commit()
    db.refresh(db_cat)
    return db_cat


@app.delete("/catgorias/{categoria_id}")
def borrar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_cat = db.query(models.CategoriaDB).filter(
        models.CategoriaDB.id == categoria_id).first()
    if not db_cat:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")

    db.delete(db_cat)
    db.commit()
    return {"ok": True, "mensaje": "Categoria eliminada"}


# --- ENDPOINTS ARTICULOS ---
@app.post("/articulos", response_model=schemas.Articulo)
def crear_articulo(art: schemas.ArticuloBase, db: Session = Depends(get_db)):
    # Verificamos si la categoría existe antes de crear
    cat_existe = db.query(models.CategoriaDB).filter(
        models.CategoriaDB.id == art.categoria_id).first()
    if not cat_existe:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")

    nuevo = models.ArticuloDB(**art.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/articulos", response_model=List[schemas.Articulo])
def listar_articulos(
        skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.ArticuloDB).offset(skip).limit(limit).all()
