import os
import requests

# API de Star Wars
URL_API = "https://swapi.py4e.com/api/films/"
ARCHIVO_DESTINO = "peliculas_star_wars.txt"

print("🎬 INICIANDO EL EXTRACTOR DE DATOS CINEMATOGRÁFICOS... 🎬\n")

try:
    print(f"📡 Conectando con la base de datos en: {URL_API}...")

    respuesta = requests.get(URL_API, timeout=5)

    # Lanza una excepción si el servidor responde con un error (4xx o 5xx)
    respuesta.raise_for_status()

    # Convertimos la respuesta JSON en un diccionario de Python
    datos = respuesta.json()

    print("🔓 ¡Datos descargados con éxito! Procesando cartelera...")

    with open(ARCHIVO_DESTINO, "w", encoding="utf-8") as archivo_local:
        archivo_local.write("=== REPORTE DE PELÍCULAS DE STAR WARS ===\n\n")

        # Ahora sí, recorremos la clave 'results' que contiene la lista de películas reales
        for pelicula in datos["results"]:
            titulo = pelicula["title"]
            episodio = pelicula["episode_id"]
            director = pelicula["director"]
            estreno = pelicula["release_date"]

            linea_pelicula = f"🎬 Episodio {episodio}: {titulo} | Director: {director} | Lanzamiento: {estreno}\n"

            print(f"✍️ Guardando: {linea_pelicula.strip()}")
            archivo_local.write(linea_pelicula)

except requests.exceptions.HTTPError as err_http:
    print(
        f"❌ ERROR HTTP: La API reportó un problema de acceso. Código: {err_http.response.status_code}"
    )

except requests.exceptions.ConnectionError:
    print(
        "🔌 ERROR DE CONEXIÓN: No se pudo contactar al servidor. Revisa tu conexión a internet."
    )

except requests.exceptions.Timeout:
    print("⏱️ ERROR DE TIEMPO: El servidor de películas tardó demasiado en responder.")

except KeyError:
    print(
        "🧠 ERROR DE ESTRUCTURA: Los datos JSON recibidos no tienen el formato esperado."
    )

except IOError as err_archivo:
    print(
        f"📂 ERROR DE ARCHIVO: No se pudo escribir en '{ARCHIVO_DESTINO}'. Detalle: {err_archivo}"
    )

except Exception as e:
    print(f"💥 ANOMALÍA INESPERADA: {e}")

else:
    print(
        f"\n🎉 ¡PROCESO COMPLETADO! Se ha creado el archivo '{ARCHIVO_DESTINO}' con éxito."
    )
    print(f"📂 Ubicación actual del archivo: {os.path.abspath(ARCHIVO_DESTINO)}")

finally:
    print("\n🧹 Cerrando conexiones y liberando recursos del sistema.")

print("🖥️ Fin de la ejecución.")
