import os
import requests

URL_MODELO = "https://pollinations.ai/p/"
ARCHIVO_ARTE = "arte_ia.jpg"

print("🤖 INICIANDO CONEXIÓN CON EL MODELO DE IA VIA API... 🤖\n")

prompt_usuario = input("✏️ Describe la imagen que quieres generar: ")

if not prompt_usuario.strip():
    print(
        "⚠️ No escribiste nada. Usaremos un prompt por defecto: 'a cute robot learning python'."
    )
    prompt_usuario = "a cute robot learning python"

# Reemplazamos los espacios por %20 para que sea una URL válida
prompt_url = requests.utils.quote(prompt_usuario)
url_completa = f"{URL_MODELO}{prompt_url}?width=1024&height=1024&seed=42"

try:
    print("\n🧠 El modelo está procesando tus instrucciones en la nube...")
    print(f"📡 Enviando petición a: {url_completa}")

    # 1. Hacemos la petición al modelo.
    # Le damos un timeout (20s) porque los modelos de IA tardan un poco en generar el archivo
    respuesta_modelo = requests.get(url_completa, timeout=20)
    respuesta_modelo.raise_for_status()

    print("📥 ¡Imagen generada con éxito! Descargando los bytes del archivo...")

    # 2. Guardamos los bytes binarios de la imagen generada por el modelo
    with open(ARCHIVO_ARTE, "wb") as archivo_local:
        archivo_local.write(respuesta_modelo.content)

except requests.exceptions.HTTPError as err_http:
    print(
        f"❌ ERROR DEL MODELO (HTTP): El servidor de IA reportó un problema. Código: {err_http.response.status_code}"
    )

except requests.exceptions.ConnectionError:
    print(
        "🔌 ERROR DE CONEXIÓN: No se pudo contactar al servidor del modelo. Revisa tu internet."
    )

except requests.exceptions.Timeout:
    print("⏱️ ERROR DE TIEMPO: El modelo de IA tardó demasiado en responder (Timeout).")

except IOError as err_archivo:
    print(
        f"📂 ERROR DE ARCHIVO: No se pudo escribir la imagen en tu carpeta. Detalle: {err_archivo}"
    )

except Exception as e:
    print(f"💥 ANOMALÍA INESPERADA: {e}")

else:
    print(f"\n🎉 ¡PROCESO COMPLETADO CON ÉXITO!")
    print(f"🖼️ Tu obra de arte generada por IA se guardó como: '{ARCHIVO_ARTE}'")
    print(f"📂 Ubicación en tu sistema: {os.path.abspath(ARCHIVO_ARTE)}")

finally:
    print("\n🧹 Liberando memoria y cerrando canales con el servidor de IA.")

print("🖥️ Fin de la ejecución.")
