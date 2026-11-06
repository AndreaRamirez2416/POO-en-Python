with open("palabras_ingles.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())