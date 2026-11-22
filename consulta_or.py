from sqlalchemy import or_

from configuracion import SessionLocal
from crear_base_entidades import HistoriaClinica


def consulta_or():
    session = SessionLocal()

    try:
        print("\n=== HISTORIAS CLÍNICAS: OR ===")

        historias = (
            session.query(HistoriaClinica)
            .filter(
                or_(
                    HistoriaClinica.diagnostico == "Gastritis",
                    HistoriaClinica.diagnostico == "Dermatitis"
                )
            )
            .all()
        )

        for historia in historias:
            print(
                f"Mascota: {historia.nombre_mascota} | "
                f"Diagnóstico: {historia.diagnostico} | "
                f"Tratamiento: {historia.tratamiento}"
            )

    finally:
        session.close()


if __name__ == "__main__":
    consulta_or()
