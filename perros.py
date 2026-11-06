import os
import requests
import json

# URL REAL Y EXACTA de la API para obtener un perrito aleatorio
URL_API = "https://dog.ceo/api/breed/affenpinscher/images/random"
ARCHIVO_DESTINO = "perrito_aleatorio.jpg"

print("🐶 INICIANDO EL CAPTURADOR DE PERRITOS INTERNET... 🐶\n")

try:
    print(f"📡 Conectando con la API canina en: {URL_API}...")
    # 1. Pedimos los datos del perro a la API
    respuesta_api = requests.get(URL_API, timeout=5)
    respuesta_api.raise_for_status()

    # 2. Transformamos la respuesta en un diccionario de Python
    datos = respuesta_api.json()

    # Extraemos la ruta de la imagen que viene dentro de la clave 'message'
    url_imagen = datos["message"]
    print(f"🔗 ¡Perrito localizado! Enlace de la foto: {url_imagen}")

    print("📥 Descargando el archivo de la imagen...")
    # 3. Hacemos la petición para bajar los bytes de la foto real (.jpg)
    respuesta_imagen = requests.get(url_imagen, timeout=7)
    respuesta_imagen.raise_for_status()

    # 4. Guardamos la imagen de forma binaria ("wb")
    with open(ARCHIVO_DESTINO, "wb") as archivo_local:
        archivo_local.write(respuesta_imagen.content)

except requests.exceptions.HTTPError as err_http:
    print(
        f"❌ ERROR HTTP: El servidor reportó un fallo. Código: {err_http.response.status_code}"
    )

except requests.exceptions.ConnectionError:
    print("🔌 ERROR DE CONEXIÓN: No se pudo conectar con la API. Revisa tu internet.")

except requests.exceptions.Timeout:
    print("⏱️ ERROR DE TIEMPO: El servidor tardó demasiado en responder.")

except json.JSONDecodeError as err_json:
    # Esto evitará confusiones si la URL llegara a devolver HTML en vez de un JSON
    print(
        f"🧩 ERROR DE FORMATO: La respuesta no es un JSON válido. Detalle: {err_json}"
    )

except KeyError:
    print("🧠 ERROR DE ESTRUCTURA: Los datos JSON no contienen la clave 'message'.")

except IOError as err_archivo:
    # Ahora este bloque solo atrapará fallos reales de escritura en tu disco duro
    print(
        f"📂 ERROR DE ARCHIVO: No se pudo guardar la imagen en el disco. Detalle: {err_archivo}"
    )

except Exception as e:
    print(f"💥 ANOMALÍA INESPERADA: {e}")

else:
    print(f"\n🎉 ¡ÉXITO TOTAL! Tu imagen se ha guardado como '{ARCHIVO_DESTINO}'")
    print(f"📂 Ruta real del archivo: {os.path.abspath(ARCHIVO_DESTINO)}")

finally:
    print("\n🧹 Limpiando antenas de red y cerrando canales.")

print("🖥️ Fin de la ejecución.")
