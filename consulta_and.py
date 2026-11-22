
from sqlalchemy import and_

from configuracion import SessionLocal
from crear_base_entidades import Clinica, Consultorio


def consulta_and():
    session = SessionLocal()

    try:
        print("\n=== CONSULTORIOS: AND ===")

        consultorios = (
            session.query(Consultorio)
            .join(Clinica)
            .filter(
                and_(
                    Clinica.nombre == "Patitas Loja",
                    Consultorio.especialidad == "Medicina general"
                )
            )
            .all()
        )

        for consultorio in consultorios:
            print(
                f"Consultorio: {consultorio.nombre} | "
                f"Especialidad: {consultorio.especialidad} | "
                f"Clínica: {consultorio.clinica.nombre}"
            )

    finally:
        session.close()


if __name__ == "__main__":
    consulta_and()
