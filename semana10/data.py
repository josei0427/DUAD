import csv

def export_info(save_students, filee, headers):
    with open(filee, 'a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = headers, delimiter='\t')
        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(save_students)


def import_info(filee):
    new_list = []
    with open(filee, 'r') as file:
        for line in file.readlines():
            print(line)
            new_list.append(line.strip())