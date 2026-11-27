from abc import ABC, abstractmethod
import sqlite3
import psycopg2

# 1. CONTRATO (Interfaz): nunca se modifica al agregar nuevas BD
class BaseConexionDB(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def cerrar(self):
        pass

# 2. IMPLEMENTACION A: PostgreSQL (la que ya teniamos)
class PostgresConexionDB(BaseConexionDB):
    def __init__(self, host, port, dbname, user, password):
        self._config = {
            "host": host,
            "port": port,
            "dbname": dbname,
            "user": user,
            "password": password
        }
        self.conexion = None

    def conectar(self):
        if self.conexion is None and self.conexion.closed:
            self.conexion = psycopg2.connect(**self._config)
        return self.conexion
    
    def cerrar(self):
        if self.conexion and not self.conexion.closed:
            self.conexion.close()

# 3. NUEVA IMPLEMENTACION B: Agregada sin tocar el codigo anterior
class SQLiteConexionDB(BaseConexionDB):
    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo
        self.conexion = None

    def conectar(self):
        if self.conexion is None:
            self.conexion = sqlite3.connect(self.ruta_archivo)
        return self.conexion

    def cerrar(self):
        if self.conexion:
            self.conexion.close()

# 4. REPOSITORIO: Intacto, acepta cualquier clase que herede de BaseConexionDB --- INYECTA---
class UsuarioRepositorio:
    def __init__(self, db: BaseConexionDB):
        self.db = db

    def obtener_todos(self) -> list:
        conexion = self.db.conectar()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, email FROM usuarios;")
            return cursor.fetchall()

# --- Uso intercambiando conexiones sin modificar el repositorio ni la interfaz ---
if __name__ == "__main__":
    # Opcion A: Tu base PostgreSQL original
    db_postgres = PostgresConexionDB(
        "localhost", 5432, "carolina", "postgres", "posgrest"
    )
    repo_postgres = UsuarioRepositorio(db_postgres)

    #Opcion B: Una segunda base PostgresSQL distinta (solo creas otra instancia)
    db_respaldo = PostgresConexionDB(
        "192.168.1.50", 5432, "carolina_backup", "postgres", "1234"
    )
    repo_backup = UsuarioRepositorio(db_respaldo)

    # Opcion C: Otro motor distinto (SQLite para pruebas locales)
    db_local = SQLiteConexionDB("pruebas.db")
    repo_test = UsuarioRepositorio(db_local)