
from sqlalchemy import func

from configuracion import SessionLocal
from crear_base_entidades import (
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica
)


def consultar_clinicas():
    session = SessionLocal()

    try:
        # Consultar todas las clínicas
        clinicas = session.query(Clinica).all()

        print("\n=== CLÍNICAS VETERINARIAS ===\n")

        for clinica in clinicas:
            # Contar historias clínicas asociadas
            total_historias = (
                session.query(func.count(HistoriaClinica.id))
                .join(
                    Veterinario,
                    HistoriaClinica.veterinario_id
                    == Veterinario.id
                )
                .join(
                    Consultorio,
                    Veterinario.consultorio_id
                    == Consultorio.id
                )
                .filter(
                    Consultorio.clinica_id == clinica.id
                )
                .scalar()
            )

            print(f"ID: {clinica.id}")
            print(f"Clínica: {clinica.nombre}")
            print(f"Dirección: {clinica.direccion}")
            print(
                f"Veterinario responsable: "
                f"{clinica.veterinario_responsable}"
            )
            print(
                f"Número de historias clínicas: "
                f"{total_historias}"
            )
            print("-" * 45)

    finally:
        session.close()


if __name__ == "__main__":
    consultar_clinicas()

