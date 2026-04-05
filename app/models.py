from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from typing import List


class CategoriaDB(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(unique=True)

    articulos: Mapped[List["ArticuloDB"]] = relationship(
        back_populates="categoria", cascade="all, delete-orphan")


class ArticuloDB(Base):
    __tablename__ = "articulos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column()
    precio: Mapped[float] = mapped_column()

    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))

    categoria: Mapped["CategoriaDB"] = relationship(back_populates="articulos")
