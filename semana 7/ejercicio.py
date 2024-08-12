def sum_num(num_1):
    condi = True
    while condi:
        try:
            num_2 = int(input(f'Ingrese el segundo numero: {num_1} + '))
            sum_result = num_1 + num_2
            return sum_result
        except ValueError:
            print("ERROR: Lo ingresado no es un numero. Por favor ingrese un número válido.")


def res_num(num_1):
    condi = True
    while condi:
        try:
            num_2 = int(input(f'Ingrese el segundo numero: {num_1} - '))
            res_result = num_1 - num_2
            return res_result
        except ValueError:
            print("ERROR: Lo ingresado no es un numero. Por favor ingrese un número válido.")
    return res_result


def mul_num(num_1):
    condi = True
    while condi:
        try:
            num_2 = int(input(f'Ingrese el segundo numero: {num_1} * '))
            mul_result = num_1 * num_2
            return mul_result
        except ValueError:
            print("ERROR: Lo ingresado no es un numero. Por favor ingrese un número válido.")


def div_num(num_1):
    condi = True
    while condi:
        try:
            num_2 = int(input(f'Ingrese el segundo numero: {num_1} / '))
            div_result = num_1 / num_2
            return div_result
        except ValueError:
            print("ERROR: Lo ingresado no es un numero. Por favor ingrese un número válido.")


condicion = True
act_num = 0
while condicion:
    try:
        print(f'El numero inicial es {act_num}')
        if act_num == 0:
            act_num = int(input(f'Ingrese el primer numero: '))

        print("1- Suma")
        print("2- Resta")
        print("3- Multiplicacion")
        print("4- Division")
        print("5- Borrar el primer numero ingresado")
        eleccion = int(input("Elija que operacion le gustaria realizar: "))
        
        if eleccion == 1: 
            act_num = sum_num(act_num)
            print(f'El resultado de la suma es: {act_num}')
        elif eleccion == 2: 
            act_num = res_num(act_num)
            print(f'El resultado de la resta es: {act_num}')
        elif eleccion == 3: 
            act_num = mul_num(act_num)
            print(f'El resultado de la multiplicacion es: {act_num}')
        elif eleccion == 4: 
            act_num = div_num(act_num)
            print(f'El resultado de la division es: {act_num}')
        elif eleccion == 5:
            if act_num == 0:
                raise ValueError("El número a borrar ya es cero.")
            else:
                act_num = 0
        else:
            print("ERROR: Selecciono una opcion invalida.")
        
    except ValueError:
        print("ERROR: Lo ingresado no es un numero. Por favor ingrese un número válido.")
