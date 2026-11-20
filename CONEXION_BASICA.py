#pip install psycopg2-binary
import psycopg2

# 1) datos de conexion (los mismos que al crear la base de datos en psql)
conexion = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="carolina",
    user="postgres",
    password="241623"
)

# 2) un cursor es lo que realmente envia SQL y trae resultados
cursor = conexion.cursor()

# ejemplo de creacion de tabla

# A) borramos la tabla vieja para que se cree desde cero con la estructura nueva
cursor.execute("DROP TABLE IF EXISTS usuarios2;")

# B) creamos la tablas tal y como la quieres (sin password)
cursor.execute("""
CREATE TABLE usuarios2 (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
""")

# C) ahora si puedes insertar datos sin la columna password
cursor.execute(
    "INSERT INTO usuarios2 (nombre, email) VALUES (%s, %s)",
    ("Juan Perez", "juan.perez@example.com")
)

# D) confirmar y cerrar 
conexion.commit()
print("Tabla creada y usuario insertados correctamente.")

cursor.close()
conexion.close()