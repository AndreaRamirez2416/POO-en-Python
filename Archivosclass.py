# https://forms.gle/4TJHLr7emV9ipruE9

import random


class LectorPalabras:
    def __init__(self, archivo="palabras_ingles.txt"):
        self.archivo = archivo

    def cargar_palabras(self):
        """Lee el archivo de texto y devuelve una lista con las palabras."""
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return [linea.strip() for linea in f if linea.strip()]
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.archivo}.")
            print("Asegúrate de crear el archivo en la misma carpeta que este script.")
            return []

    def elegir_palabra(self):
        """Elige una palabra al azar de la lista cargada."""
        palabras = self.cargar_palabras()
        if palabras:
            return random.choice(palabras)
        return None


# Prueba rápida para ver si funciona
if __name__ == "__main__":
    gestor = LectorPalabras("palabras_ingles.txt")
print(
    "Palabra elegida:",
    gestor.elegir_palabra(),
)
