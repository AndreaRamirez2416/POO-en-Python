Notas=[5,4,1]
Notas.pop(-1)
Notas.append(3)
Estudiantes=["Juan", "Pedro", "Maria", "Luis", "Ana"]
Estudiantes.remove("Luis")
Suma=0
for Nota in Notas:
    Suma=Suma+Nota
    print(Nota)
print("Suma:", Suma)
for Estudiante in Estudiantes:
    print(Estudiante)
Promedio=Suma/len(Notas)
print("Promedio:", Promedio)
print("Cantidad de notas:", len(Notas))

