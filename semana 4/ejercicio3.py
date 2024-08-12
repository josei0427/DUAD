s_num = 7
ver = True
while ver :
    u_num = int(input("Por favor ingrese un numero del 1 al 10: "))
    if u_num != s_num:
        print("El numero es incorrecto.")
    else:
        if u_num == s_num:
            print("EL NUMERO ES CORRECTO!!!")
            ver = False
