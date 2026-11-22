
from datetime import date

from sqlalchemy import (
    Column, Integer, String, Date,
    ForeignKey, Text
)
from sqlalchemy.orm import relationship

from configuracion import Base, engine


class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(
        String(150), nullable=False
    )

    consultorios = relationship(
        "Consultorio",
        back_populates="clinica"
    )


class Consultorio(Base):
    __tablename__ = "consultorios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)

    clinica_id = Column(
        Integer,
        ForeignKey("clinicas.id"),
        nullable=False
    )

    clinica = relationship(
        "Clinica",
        back_populates="consultorios"
    )

    veterinarios = relationship(
        "Veterinario",
        back_populates="consultorio"
    )


class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(
        String(150), unique=True, nullable=False
    )
    licencia = Column(
        String(50), unique=True, nullable=False
    )

    consultorio_id = Column(
        Integer,
        ForeignKey("consultorios.id"),
        nullable=False
    )

    consultorio = relationship(
        "Consultorio",
        back_populates="veterinarios"
    )

    historias_clinicas = relationship(
        "HistoriaClinica",
        back_populates="veterinario"
    )


class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(
        Date, nullable=False, default=date.today
    )
    diagnostico = Column(Text, nullable=False)
    tratamiento = Column(Text, nullable=False)
    nombre_mascota = Column(
        String(100), nullable=False
    )

    veterinario_id = Column(
        Integer,
        ForeignKey("veterinarios.id"),
        nullable=False
    )

    veterinario = relationship(
        "Veterinario",
        back_populates="historias_clinicas"
    )


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Base de datos creada correctamente.")
    print("Tablas: clinicas, consultorios, "
          "veterinarios, historias_clinicas")
