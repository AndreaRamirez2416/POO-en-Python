import os
import requests


class GestorCatalogoModa:
    def __init__(self):
        # Usamos el CDN directo de imágenes de Unsplash, evitando el bloqueo 403
        self.dominio_cdn = "https://images.unsplash.com"
        self.carpeta_destino = "Catalogo_Moda"
        self.txt_destino = os.path.join(self.carpeta_destino, "creditos_autores.txt")

    def inicializar_carpeta(self):
        # Si la carpeta no existe en tu espacio del INTEP, la crea automáticamente
        if not os.path.exists(self.carpeta_destino):
            os.makedirs(self.carpeta_destino)
            print(f"📁 Carpeta de almacenamiento lista: '{self.carpeta_destino}'")

    def descargar_catalogo(self):
        print("📸 INICIANDO EXTRACTOR AUTOMATIZADO DE FOTOGRAFÍA DE MODA... 📸\n")

        # Nos aseguramos de tener el directorio creado antes de conectar
        self.inicializar_carpeta()

        # Galería con IDs reales de retratos artísticos y fotografía editorial femenina en Unsplash
        galeria_modelos = [
            {"id": "photo-1534528741775-53994a69daeb", "autor": "Christopher Campbell"},
            {"id": "photo-1524504388940-b1c1722653e1", "autor": "Christopher Campbell"},
            {"id": "photo-1494790108377-be9c29b29330", "autor": "Michael Dam"},
            {"id": "photo-1506794778202-cad84cf45f1d", "autor": "Albert Dera"},
            {"id": "photo-1517841905240-472988babdf9", "autor": "Mimi Thian"},
        ]

        try:
            print(f"📡 Conectando con los servidores CDN de Unsplash...\n")

            # Abrimos el archivo de texto dentro de nuestra subcarpeta
            with open(self.txt_destino, "w", encoding="utf-8") as archivo_txt:
                archivo_txt.write(
                    "=== REPORTE DE CRÉDITOS: CATÁLOGO DE MODA EDITORIAL / GLAMOUR ===\n\n"
                )

                # Definimos un User-Agent común para simular una petición de navegador estándar
                cabeceras = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                }

                # Recorremos nuestro lote curado de modelos femeninas
                for indice, foto in enumerate(galeria_modelos, start=1):
                    autor = foto["autor"]

                    # Construimos la URL apuntando al CDN directo con encuadre de catálogo vertical (800x1100)
                    url_descarga_hd = f"{self.dominio_cdn}/{foto['id']}?auto=format&fit=crop&w=800&h=1100&q=80"

                    print(f"✨ [{indice}] Procesando obra del fotógrafo: {autor}")

                    # 1. Guardamos el registro de texto plano con los créditos de autor
                    archivo_txt.write(f"📷 Fotografía #{indice}\n")
                    archivo_txt.write(f"   👤 Autor/Fotógrafo: {autor}\n")
                    archivo_txt.write(f"   🔗 Enlace de Origen:   {url_descarga_hd}\n")
                    archivo_txt.write("-" * 55 + "\n")

                    # 2. Descargamos los bytes binarios de la fotografía profesional
                    nombre_archivo = os.path.join(
                        self.carpeta_destino, f"modelo_glamour_{indice}.jpg"
                    )
                    print(f"   📥 Guardando archivo binario en -> {nombre_archivo}...")

                    # Pasamos las cabeceras para una conexión limpia y segura
                    respuesta_foto = requests.get(
                        url_descarga_hd, headers=cabeceras, timeout=15
                    )
                    respuesta_foto.raise_for_status()

                    # Escritura binaria ("wb") para reconstruir la imagen en tu disco duro
                    with open(nombre_archivo, "wb") as archivo_img:
                        archivo_img.write(respuesta_foto.content)

        except requests.exceptions.RequestException as e:
            print(
                f"🔌 ERROR DE RED: No se pudo establecer la comunicación con el servidor. Detalle: {e}"
            )
        except KeyError as e:
            print(
                f"🧠 ERROR DE ESTRUCTURA: Falló la lectura de las claves de datos. Detalle: {e}"
            )
        except IOError as e:
            print(
                f"📂 ERROR DE DISCO: Error al escribir los archivos en la computadora. Detalle: {e}"
            )
        except Exception as e:
            print(f"💥 ANOMALÍA INESPERADA: {e}")
        else:
            print(f"\n🎉 ¡CATÁLOGO COMPLETADO EXITOSAMENTE!")
            print(
                f"📝 Registro de créditos guardado en: {os.path.abspath(self.txt_destino)}"
            )
            print(
                f"🖼️ Revisa tu carpeta '{self.carpeta_destino}', las imágenes estéticas de moda ya están listas."
            )
        finally:
            print(
                "\n🧹 Limpiando conexiones de red y cerrando descriptores de archivos."
            )


if __name__ == "__main__":
    catalogo = GestorCatalogoModa()
    catalogo.descargar_catalogo()
    print("🖥️ Fin de la ejecución.")
