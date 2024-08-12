my_list =[]
cont = 1
while (cont <= 10):
    num = int(input("Ingrese un numero: "))
    my_list.append(num)
    cont += 1
valor_alto = 0
for i in my_list:
    if i > valor_alto:
        valor_alto = i
print(f'{my_list}. El mas alto fue: {valor_alto}')