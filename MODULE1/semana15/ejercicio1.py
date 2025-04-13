def my_bubblesort(my_list):
    for other_i in range(0, len(my_list)-1):
        for i in range(len(my_list)-1, other_i, -1):
            current_number = my_list[i]
            next_number = my_list[i-1]
            print(f'Elemento actual: {current_number}, Siguiente elemento: {next_number}')
            if current_number < next_number:
                print("El numero siguiente es mayor. Realizando cambios...")
                my_list[i] = next_number
                my_list[i-1] = current_number


my_list = [5,7,3,8,2,9,1]
my_bubblesort(my_list)
print(my_list)