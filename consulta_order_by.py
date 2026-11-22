
from configuracion import SessionLocal
from crear_base_entidades import Clinica


def consulta_order_by():
    session = SessionLocal()

    try:
        print("\n=== CLÍNICAS ORDENADAS POR NOMBRE ===")

        clinicas = (
            session.query(Clinica)
            .order_by(Clinica.nombre.asc())
            .all()
        )

        for clinica in clinicas:
            print(
                f"ID: {clinica.id} | "
                f"Clínica: {clinica.nombre} | "
                f"Dirección: {clinica.direccion}"
            )

    finally:
        session.close()


if __name__ == "__main__":
    consulta_order_by()
