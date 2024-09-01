def get_info(my_list):
    condition = True
    while condition:
        name = input("Ingrese el nombre del estudiante: ")
        group_section = input("Ingrese la seccion del estudiante: ")
        spanish_grade = get_note("español")
        english_grade = get_note("inglés")
        socials_grade = get_note("sociales")
        science_grade = get_note("ciencias")
                    
        info_dict = {
            "Nombre": name,
            "Seccion": group_section,
            "Nota de español": spanish_grade,
            "Nota de ingles": english_grade,
            "Nota de sociales": socials_grade,
            "Nota de ciencias": science_grade,
            "Nota Promedio": (spanish_grade + english_grade + socials_grade + science_grade) /4
        }
        my_list.append(info_dict)
        option = input("Quiere ingresar otro estudiante? ( 'si' o 'no'): ")
        option = option.lower()
        if option == "no":
            print(f"Se han guardado los datos del estudiante.")
            break
        elif option != "si":
            print("Opción no válida. Por favor, responda con 'si' o 'no'.")
    return my_list


def get_note(subject):
    condition = True
    while condition:
        try:
            grade = int(input(f"Ingrese la nota de {subject} del estudiante: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Nota inválida. La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


def show_info(save_students):
    if not save_students:
        print("No hay información de estudiantes para mostrar.")
    return save_students


def get_top3(my_list):
    result = []
    if not my_list:
        print("No hay información de estudiantes.")
        return
    top3 = sorted(my_list, key=lambda i: i['Nota Promedio'], reverse=True)[:3]
    for j in top3:
        student_info = {
            'Nombre': j['Nombre'],
            'Nota Promedio': j['Nota Promedio']
        }
        result.append(student_info)
    return result


def gpa_ofgpa(students_info):
    if not students_info:
        print("No hay información de estudiantes.")
        return
    all_gpa = []
    num_ofstudents = len(students_info)
    result = 0
    for i in students_info:
        all_gpa.append(i["Nota Promedio"])
    result = sum(all_gpa) / num_ofstudents
    return result