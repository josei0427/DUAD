notas_totales = int(input("Ingrese el numero de notas que desea ingresar: "))
notas = []
notas_mayores = []
notas_menores = []
sum_tot = 0
sum_mayores = 0
sum_menores = 0
cant_mayores = 0
cant_menores = 0
contador = 1
while (contador <= notas_totales):
    nota = int(input("Ingrese la nota: "))
    notas.append(nota)
    contador += 1
for nota in notas:
    if nota >= 70:
        notas_mayores.append(nota)
        cant_mayores += 1
    else:
        notas_menores.append(nota)
        cant_menores +=1
for i in notas:
    sum_tot += i
prom_total = sum_tot / notas_totales

for j in notas_mayores:
    sum_mayores += j
prom_mayores = sum_mayores / notas_totales

for k in notas:
    sum_menores += k
prom_menores = sum_menores / notas_totales
print("")
print("Las notas mayores a 70 son: " + str(cant_mayores))
print("Las notas menores a 70 son: " + str(cant_menores))
print("El promedio de todas las notas es: " + str(prom_total))
print("El promedio de las notas mayores es: " + str(prom_mayores))
print("El promedio de las notas menores es: " + str(prom_menores))