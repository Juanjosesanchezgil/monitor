from pydantic import BaseModel
from typing import List


class ArticuloBase(BaseModel):
    nombre: str
    precio: float
    categoria_id: int


class Articulo(ArticuloBase):
    id: int

    class Config:
        from_attributes = True


class CategoriaBase(BaseModel):
    nombre: str


class Categoria(CategoriaBase):
    id: int
    articulos: List[Articulo] = []

    class Config:
        from_attributes = True
