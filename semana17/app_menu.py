import PySimpleGUI as sg
import csv
import os  # Importamos os para verificar la existencia del archivo
import agregar_ingreso
import agregar_gasto
import agregar_categoria

def show_main_window():
    headers = ['Titulo', 'Categoria', 'Ingreso o Gasto', 'Monto']
    data_from_user = import_data()
    lst_cats = lst_cats = import_categories()

    layout = [
        [sg.Text("Sistema de Manejo de Finanzas", font=("Helvetica", 16), justification="center")],
        [sg.Button("Agregar un ingreso")],
        [sg.Button("Agregar un gasto")],
        [sg.Button("Agregar una categoria")],
        [sg.Table(values=data_from_user, headings=headers, key='-TABLE-', auto_size_columns=True, justification='right')]
    ]

    window = sg.Window('Manejo de Finanzas', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Agregar un ingreso":
            agregar_ingreso.income_window(data_from_user, lst_cats)
            window['-TABLE-'].update(values=data_from_user)
            export_to_csv(data_from_user)
        elif event == "Agregar un gasto":
            agregar_gasto.expense_window(data_from_user, lst_cats)
            window['-TABLE-'].update(values=data_from_user)
            export_to_csv(data_from_user)
        elif event == "Agregar una categoria":
            agregar_categoria.category_window(lst_cats)
            export_categories(lst_cats)

    window.close()

def export_to_csv(data_from_user):
    the_file = 'Finanzas.csv'
    with open(the_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Titulo', 'Categoria', 'Ingreso o Gasto', 'Monto'])
        writer.writerows(data_from_user)

def import_data():
    the_file = 'Finanzas.csv'
    data_from_user = []
    try:
        with open(the_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)
            for i in reader:
                data_from_user.append(i)
    except FileNotFoundError:
        pass
    return data_from_user

def export_categories(lst_cats):
    categories_file = 'Categorias.csv'
    with open(categories_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Categoria'])
        for i in lst_cats:
            writer.writerow([i])

def import_categories():
    categories_file = 'Categorias.csv'
    lst_cats = []
    try:
        with open(categories_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                lst_cats.append(row[0])
    except FileNotFoundError:
        pass
    return lst_cats



if __name__ == '__main__':
    show_main_window()