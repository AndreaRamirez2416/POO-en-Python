#pip install psycopg2-binary
import psycopg2

#1 Datos de conexion(los mismos que al crear la base de datos con psql)
conexion = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="carolina",
    user="postgres",
    password="241623",
)
#2 un cursor es lo que realemente envia sql y trae resultados
cursor = conexion.cursor()

# ejemplo de creacion de tabla

#A)Borramos la tabla vieja para q se cree desde cero con la estructura nueva
cursor.execute("DROP TABLE IF EXISTS usuarios2;")

#B)Creamos la tabla tal y como l quieres (sin password)
cursor.execute("""
CREATE TABLE usuarios2(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
""")
#C)Ahora si puedes insertar datos en la columna password
cursor.execute(
    "INSERT INTO usuarios2 (nombre, email) VALUES (%s, %s);",
    ("Erika","erika@gmail.com")
)
cursor.execute(
    "INSERT INTO usuarios2 (nombre, email) VALUES (%s, %s);",
    ('Camila Fernanda Herrera', 'camila.herrera@ejemplo.com')
)
cursor.execute(
    "INSERT INTO usuarios2 (nombre, email) VALUES (%s, %s);",
    ('Sebastián Morales', 'sebastian.morales@ejemplo.com')
)
cursor.execute(
    "INSERT INTO usuarios2 (nombre, email) VALUES (%s, %s);",
    ('Mariana Rojas', 'mariana.rojas@ejemplo.com')
)
cursor.execute(
    "INSERT INTO usuarios2 (nombre, email) VALUES (%s, %s);",
    ('Andrés Felipe Vargas', 'andres.vargas@ejemplo.com')
)
#D) confrimar y cerrar
conexion.commit()
print("Tabla creada y datos insertados correctamente.")


#E) Consultar y mostrar los datos (select)
cursor.execute("SELECT id, nombre, email FROM usuarios2;")

#F) Recuperar y mostrar los resultados
resultados = cursor.fetchall()
for fila in resultados:
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Email: {fila[2]}")

cursor.close()
conexion.close()