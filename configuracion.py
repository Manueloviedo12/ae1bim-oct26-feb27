
from pathlib import Path

from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base, sessionmaker

# Ruta de la base de datos
BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'veterinaria.db'}"

# Motor de conexión
engine = create_engine(
    DATABASE_URL,
    echo=False
)

# Activar claves foráneas en SQLite
@event.listens_for(engine, "connect")
def activar_claves_foraneas(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# Configuración de sesiones
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# Base para los modelos ORM
Base = declarative_base()
