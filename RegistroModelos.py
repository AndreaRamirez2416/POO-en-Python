import os
import requests


class GestorModelos:
    def __init__(self):
        # Unimos las piezas de la URL para que apunte directamente al servidor de datos JSON
        dominio = "https://randomuser.me"
        ruta_api = "/api/"
        parametros = "?gender=female&results=5"

        self.url_api = dominio + ruta_api + parametros
        self.txt_destino = "perfil_modelos_mujeres.txt"

    def descargar_perfiles(self):
        print("👩‍💻 INICIANDO SISTEMA DE DESCARGA EXCLUSIVO DE MODELOS... 👩‍💻\n")

        try:
            print(f"📡 Conectando con la API en: {self.url_api}...")
            respuesta_api = requests.get(self.url_api, timeout=7)
            respuesta_api.raise_for_status()  # Si no es código 200, salta al except

            # Convertimos la respuesta a un diccionario de Python
            datos = respuesta_api.json()
            lista_modelos = datos["results"]

            print(
                f"🔓 ¡Lote obtenido! Procesando y descargando {len(lista_modelos)} perfiles...\n"
            )

            # Creamos el reporte de texto plano
            with open(self.txt_destino, "w", encoding="utf-8") as archivo_txt:
                archivo_txt.write("=== REGISTRO DE MODELOS MUJERES ===\n\n")

                # Recorremos la lista de mujeres devuelta por el servidor
                for indice, modelo in enumerate(lista_modelos, start=1):
                    nombre_completo = (
                        f"{modelo['name']['first']} {modelo['name']['last']}"
                    )
                    correo = modelo["email"]
                    pais = modelo["location"]["country"]
                    url_foto = modelo["picture"]["large"]  # URL de la foto de la modelo

                    print(f"✨ [{indice}] Registrando a: {nombre_completo}")

                    # 1. Escribimos la información de texto en nuestro reporte
                    archivo_txt.write(f"📌 Modelo #{indice}: {nombre_completo}\n")
                    archivo_txt.write(f"   🌍 País:   {pais}\n")
                    archivo_txt.write(f"   📧 Correo: {correo}\n")
                    archivo_txt.write(f"   🔗 Foto:   {url_foto}\n")
                    archivo_txt.write("-" * 45 + "\n")

                    # 2. Descargamos y guardamos la imagen binaria ("wb")
                    nombre_imagen = f"modelo_mujer_{indice}.jpg"
                    print(f"   📥 Guardando foto como -> {nombre_imagen}...")

                    respuesta_foto = requests.get(url_foto, timeout=5)
                    respuesta_foto.raise_for_status()

                    with open(nombre_imagen, "wb") as archivo_img:
                        archivo_img.write(respuesta_foto.content)

        except requests.exceptions.RequestException as err_red:
            print(
                f"🔌 ERROR DE RED: No se pudo conectar con el servidor. Detalle: {err_red}"
            )

        except KeyError as err_key:
            print(
                f"🧠 ERROR DE ESTRUCTURA: Las llaves del JSON no coinciden. Detalle: {err_key}"
            )

        except IOError as err_disco:
            print(
                f"📂 ERROR DE ARCHIVO: Error al escribir en el disco. Detalle: {err_disco}"
            )

        except Exception as e:
            print(f"💥 ANOMALÍA INESPERADA: {e}")

        else:
            print(f"\n🎉 ¡PROCESO COMPLETADO EXITOSAMENTE!")
            print(f"📝 Reporte consolidado en: {os.path.abspath(self.txt_destino)}")
            print(
                f"🖼️ Se guardaron {len(lista_modelos)} fotos de mujeres reales en tu carpeta."
            )

        finally:
            print("\n🧹 Cerrando flujos de archivos y terminando conexiones.")


# --- BLOQUE DE EJECUCIÓN ---
if __name__ == "__main__":
    gestor = GestorModelos()
    gestor.descargar_perfiles()
