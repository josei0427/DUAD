import csv
from actions import Students

def export_info(my_list, file_name, headers):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for i in my_list:
            writer.writerow(i.to_dict())

def import_info(file_name):
    students_list = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            #print(row)
            student = Students(
                name= row['Nombre'],
                section= row['Seccion'],
                spanish_grade=int(row['Nota de español']),
                english_grade=int(row['Nota de ingles']),
                socials_grade=int(row['Nota de sociales']),
                science_grade=int(row['Nota de ciencias'])
            )
            students_list.append(student)
    return students_list