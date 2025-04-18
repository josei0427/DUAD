name = input("Ingrese su nombre: ")
lst_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))
if age <= 4:
    print("El usuario es un bebe")
elif age >= 5 and age <= 11:
    print("El usuario es un niño.")
elif age >= 12 and age <= 14:
    print("El usuario es un preadolecente.")
elif age >= 14 and age <= 17:
    print("El usuario es un adolecente.")
elif age >= 18 and age <= 29:
    print("El usuario es un adulto joven.")
elif age >= 30 and age <= 65:
    print("El usuario es un adulto.")
else:
    print("El usuario es un adulto mayor.")