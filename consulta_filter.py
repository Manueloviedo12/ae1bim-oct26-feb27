
from configuracion import SessionLocal
from crear_base_entidades import Veterinario, Consultorio


def consulta_filter():
    session = SessionLocal()

    try:
        print("\n=== VETERINARIOS DE MEDICINA GENERAL ===")

        veterinarios = (
            session.query(Veterinario)
            .join(Consultorio)
            .filter(
                Consultorio.especialidad == "Medicina general"
            )
            .all()
        )

        for veterinario in veterinarios:
            print(
                f"ID: {veterinario.id} | "
                f"Nombre: {veterinario.nombres} "
                f"{veterinario.apellidos} | "
                f"Licencia: {veterinario.licencia}"
            )

    finally:
        session.close()


if __name__ == "__main__":
    consulta_filter()
