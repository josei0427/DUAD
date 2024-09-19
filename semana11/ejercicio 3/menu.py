import actions
import data

def form_options():
    my_list = []
    while True:
        try:
            print("1- Ingresar un estudiante.")
            print("2- Ver la informacion de todos los estudiantes.")
            print("3- Ver el top 3 de estudiantes con la mejor nota promedio.")
            print("4- Ver la nota promedio entre las notas de todos los estudiantes.")
            print("5- Exportar todos los datos actuales.")
            print("6- Importar los datos de un archivo CSV previamente exportado")
            print("7- Salir del programa")
            option = int(input("Elija que operacion le gustaria realizar: "))

            if option == 1: 
                my_list = actions.get_info(my_list)
            elif option == 2: 
                students_info = actions.show_info(my_list)
                print(f'Informacion de todos los estudiantes: ')
                for student in students_info:
                    print(student)
            elif option == 3: 
                top_students = actions.get_top3(my_list)
                print(f'Top 3 estudiantes: ')
                for student in top_students:
                    print(student)
            elif option == 4: 
                average_note = actions.gpa_ofgpa(my_list)
                print(f'Nota promedio de todos los estudiantes: {average_note}')
            elif option == 5:
                headers = ['Nombre', 'Seccion', 'Nota de español', 'Nota de ingles', 'Nota de sociales', 'Nota de ciencias', 'Nota Promedio']
                data.export_info(my_list, 'students.csv', headers)
                print("Datos exportados correctamente.")
            elif option == 6:
                my_list = data.import_info('students.csv')
                print("Datos importados correctamente.")
            elif option == 7:
                return "Hasta luego!"
            else:
                print("ERROR: Seleccionó una opción inválida.")
            
        except ValueError:
            print("ERROR: Lo ingresado no es un número. Por favor ingrese un número válido.")
            continue