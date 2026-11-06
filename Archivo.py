import random

ARCHIVO_PALABRAS = "palabras_ingles.txt"


def cargar_palabras():
    """Lee el archivo de texto y devuelve una lista con las palabras."""
    try:
        with open(ARCHIVO_PALABRAS, "r", encoding="utf-8") as archivo:
            # Lee cada línea, quita saltos de línea/espacios y filtra líneas vacías
            return [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ARCHIVO_PALABRAS}'.")
        print("Asegúrate de crear el archivo en la misma carpeta que este script.")
        return []


def elegir_palabra():
    """Elige una palabra al azar de la lista cargada."""
    palabras = cargar_palabras()
    if palabras:
        return random.choice(palabras)
    return None


# Prueba rápida para ver si funciona
if __name__ == "__main__":
    print("Palabra elegida:", elegir_palabra())
