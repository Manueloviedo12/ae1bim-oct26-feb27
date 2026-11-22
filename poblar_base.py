
from datetime import date

from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError

from configuracion import SessionLocal
from crear_base_entidades import (
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica
)


def poblar_base():
    session = SessionLocal()

    try:
        # Evitar insertar datos duplicados al ejecutar otra vez
        cantidad = session.scalar(
            select(func.count()).select_from(Clinica)
        )

        if cantidad > 0:
            print("La base de datos ya contiene clínicas.")
            print("No se insertaron registros duplicados.")
            return

        # 1. CREAR CLÍNICAS
        clinica1 = Clinica(
            nombre="Patitas Loja",
            direccion="Av. Universitaria, Loja",
            veterinario_responsable="Carlos Torres"
        )

        clinica2 = Clinica(
            nombre="Vida Animal",
            direccion="Centro de Catacocha, Loja",
            veterinario_responsable="María González"
        )

        clinica3 = Clinica(
            nombre="Huellitas Sur",
            direccion="Av. Principal, Zamora",
            veterinario_responsable="Pedro Ramírez"
        )

        session.add_all([clinica1, clinica2, clinica3])
        session.flush()

        # 2. CREAR CONSULTORIOS
        consultorio1 = Consultorio(
            nombre="Consultorio General",
            especialidad="Medicina general",
            clinica_id=clinica1.id
        )

        consultorio2 = Consultorio(
            nombre="Consultorio Cirugía",
            especialidad="Cirugía",
            clinica_id=clinica1.id
        )

        consultorio3 = Consultorio(
            nombre="Consultorio Dermatología",
            especialidad="Dermatología",
            clinica_id=clinica2.id
        )

        consultorio4 = Consultorio(
            nombre="Consultorio General 2",
            especialidad="Medicina general",
            clinica_id=clinica3.id
        )

        session.add_all([
            consultorio1,
            consultorio2,
            consultorio3,
            consultorio4
        ])
        session.flush()

        # 3. CREAR VETERINARIOS
        veterinario1 = Veterinario(
            nombres="Carlos",
            apellidos="Torres",
            correo="carlos@patitas.com",
            licencia="VET001",
            consultorio_id=consultorio1.id
        )

        veterinario2 = Veterinario(
            nombres="Ana",
            apellidos="López",
            correo="ana@patitas.com",
            licencia="VET002",
            consultorio_id=consultorio2.id
        )

        veterinario3 = Veterinario(
            nombres="María",
            apellidos="González",
            correo="maria@vidaanimal.com",
            licencia="VET003",
            consultorio_id=consultorio3.id
        )

        veterinario4 = Veterinario(
            nombres="Luis",
            apellidos="Mendoza",
            correo="luis@vidaanimal.com",
            licencia="VET004",
            consultorio_id=consultorio3.id
        )

        veterinario5 = Veterinario(
            nombres="Pedro",
            apellidos="Ramírez",
            correo="pedro@huellitas.com",
            licencia="VET005",
            consultorio_id=consultorio4.id
        )

        session.add_all([
            veterinario1,
            veterinario2,
            veterinario3,
            veterinario4,
            veterinario5
        ])
        session.flush()

        # 4. CREAR HISTORIAS CLÍNICAS
        historias = [
            HistoriaClinica(
                fecha_atencion=date(2026, 11, 10),
                diagnostico="Gastritis",
                tratamiento="Dieta blanda y medicación",
                nombre_mascota="Max",
                veterinario_id=veterinario1.id
            ),
            HistoriaClinica(
                fecha_atencion=date(2026, 11, 11),
                diagnostico="Infección respiratoria",
                tratamiento="Antibióticos",
                nombre_mascota="Luna",
                veterinario_id=veterinario1.id
            ),
            HistoriaClinica(
                fecha_atencion=date(2026, 11, 12),
                diagnostico="Fractura",
                tratamiento="Cirugía y reposo",
                nombre_mascota="Rocky",
                veterinario_id=veterinario2.id
            ),
            HistoriaClinica(
                fecha_atencion=date(2026, 11, 13),
                diagnostico="Herida superficial",
                tratamiento="Limpieza y curaciones",
                nombre_mascota="Toby",
                veterinario_id=veterinario2.id
            ),
            HistoriaClinica(
                fecha_atencion=date(2026, 11, 14),
                diagnostico="Dermatitis",
                tratamiento="Champú medicado",
                nombre_mascota="Mia",
                veterinario_id=veterinario3.id
            ),
            HistoriaClinica(
                fecha_atencion=date(2026, 11, 15),
                diagnostico="Alergia cutánea",
                tratamiento="Antihistamínicos",
                nombre_mascota="Nala",
                veterinario_id=veterinario4.id
            )
        ]

        session.add_all(historias)

        # Guardar todos los registros
        session.commit()

        print("Base de datos poblada correctamente.")
        print("3 clínicas registradas")
        print("4 consultorios registrados")
        print("5 veterinarios registrados")
        print("6 historias clínicas registradas")

    except SQLAlchemyError as error:
        session.rollback()
        print(f"Error al poblar la base: {error}")
        raise

    finally:
        session.close()


if __name__ == "__main__":
    poblar_base()
