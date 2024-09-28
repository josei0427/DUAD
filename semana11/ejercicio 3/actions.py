class Students:
    def __init__(self, name, section, spanish_grade, english_grade, socials_grade, science_grade):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.socials_grade = socials_grade
        self.science_grade = science_grade
        self.gpa_grade = (spanish_grade + english_grade + socials_grade + science_grade) / 4
    

    def __str__(self):
        return (f"Nombre: {self.name}, Sección: {self.section}, Español: {self.spanish_grade}, Inglés: {self.english_grade}, Sociales: {self.socials_grade}, Ciencias: {self.science_grade}, Nota Promedio: {self.gpa_grade}")
    

    def to_dict(self):
        return {
            'Nombre': self.name,
            'Seccion': self.section,
            'Nota de español': self.spanish_grade,
            'Nota de ingles': self.english_grade,
            'Nota de sociales': self.socials_grade,
            'Nota de ciencias': self.science_grade,
            'Nota Promedio': self.gpa_grade
        }


def get_info(my_list):
    while True:
        name = input("Ingrese el nombre del estudiante: ")
        group_section = input("Ingrese la seccion del estudiante: ")
        spanish_grade = get_note("español")
        english_grade = get_note("inglés")
        socials_grade = get_note("sociales")
        science_grade = get_note("ciencias")
                    
        student = Students(name, group_section, spanish_grade, english_grade, socials_grade, science_grade)
        my_list.append(student)
        
        option = input("Quiere ingresar otro estudiante? ( 'si' o 'no'): ").lower()
        if option == "no":
            print("Se han guardado los datos del estudiante.")
            break
        elif option != "si":
            print("Opción no válida. Por favor, responda con 'si' o 'no'.")
    return my_list

def get_note(subject):
    while True:
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
    top3 = sorted(my_list, key=lambda student: student.gpa_grade, reverse=True)[:3]
    return top3

def gpa_ofgpa(students_info):
    if not students_info:
        print("No hay información de estudiantes.")
        return
    all_gpa = []
    num_ofstudents = len(students_info)
    for student in students_info:
        all_gpa.append(student.gpa_grade)
    result = sum(all_gpa) / num_ofstudents
    return result