"""
02 - tabla con SQLAlchemy + PostgreSQL
-------------------------------------------------
Requisitos:  pip install sqlalchemy psycopg2-binary
"""

from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# PASO 1: conexión (usuario:clave@servidor:puerto/base_de_datos)
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
)


# PASO 2: la clase que representa la tabla
class Base(DeclarativeBase):
    pass


class Usuario(Base):
    _tablename_ = "usuarios_prueba"  # nombre de la tabla en PostgreSQL

    id: Mapped[int] = mapped_column(primary_key=True)  # se numera solo: 1, 2, 3...
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(200))


# PASO 3: crear la tabla (borra y recrea solo esta tabla)
Base.metadata.drop_all(engine)
Base.metadata.create_all(
    engine
)  # Con el modelo y el engine listos, una sola línea crea la tabla en PostgreSQL (si no existe ya):
print("Tabla usuarios_prueba creada")

# PASO 4: insertar datos de prueba
with Session(engine) as session:
    session.add_all(
        [
            Usuario(nombre="Juan Pérez", email="juan@example.com", password="1234"),
            Usuario(nombre="Ana Torres", email="ana@example.com", password="5678"),
            Usuario(nombre="Luis Gómez", email="luis@example.com", password="9012"),
        ]
    )
    session.commit()
    print("3 usuarios insertados")

    nuevo_usuario = Usuario(
        nombre="María López", email="maria@example.com", password="3456"
    )
    session.add(nuevo_usuario)
    session.commit()
    print("1 usuario agregado")

    # PASO 5: consultar y recorrer
    for usuario in session.scalars(select(Usuario)):
        print(usuario.id, usuario.nombre, usuario.email)

    print("_" * 40)

    resultado = session.execute(select(Usuario)).scalars().all()
    for usuario in resultado:
        print(usuario.id, usuario.nombre, usuario.email)

    print("_" * 40)

    # Filtrar con una condición (WHERE)
    consulta = select(Usuario).where(Usuario.email == "luis@example.com")
    usuario = session.execute(consulta).scalar_one()
    print(usuario.nombre)

    # Estilo clásico (session.query), también válido
    usuarios = session.query(Usuario).all()
    for usuario in usuarios:
        print(usuario.nombre, usuario.email)

    # Actualizar un registro
    usuario = session.execute(
        select(Usuario).where(Usuario.email == "luis@example.com")
    ).scalar_one()

    usuario.nombre = "Luis Gómez Actualizado"
    session.commit()  # el UPDATE se genera solo, al detectar el cambio

    # Eliminar un registro
    usuario = session.execute(
        select(Usuario).where(Usuario.email == "ana@example.com")
    ).scalar_one()

session.delete(usuario)
session.commit()