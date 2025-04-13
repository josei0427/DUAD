num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))
mayor = num_1
if num_2 > num_1 and num_2 > num_3:
    mayor = num_2
    print(mayor)
elif num_3 > num_2 and num_3 > num_1:
    mayor = num_3
    print(mayor)
else:
    print(mayor)
