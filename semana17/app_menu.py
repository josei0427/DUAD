import PySimpleGUI as sg
import csv
import add_income
import add_expense
import add_category

def show_main_window():
    headers = ['Title', 'Category', 'Income or Expense', 'Amount']
    data_from_user = import_data()
    lst_cats = lst_cats = import_categories()

    layout = [
        [sg.Text("Financial Management System", font=("Helvetica", 16), justification="center")],
        [sg.Button("Add an income")],
        [sg.Button("Add an expense")],
        [sg.Button("Add a category")],
        [sg.Table(values=data_from_user, headings=headers, key='-TABLE-', auto_size_columns=True, justification='right')]
    ]

    window = sg.Window('Financial Management System', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Add an income":
            agregar_ingreso.income_window(data_from_user, lst_cats)
            window['-TABLE-'].update(values=data_from_user)
            export_to_csv(data_from_user)
        elif event == "Add an expense":
            agregar_gasto.expense_window(data_from_user, lst_cats)
            window['-TABLE-'].update(values=data_from_user)
            export_to_csv(data_from_user)
        elif event == "Add a category":
            agregar_categoria.category_window(lst_cats)
            export_categories(lst_cats)

    window.close()

def export_to_csv(data_from_user):
    the_file = 'Financial.csv'
    with open(the_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Title', 'Category', 'Income or Expense', 'Amount'])
        writer.writerows(data_from_user)

def import_data():
    the_file = 'Financial.csv'
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
    categories_file = 'Categories.csv'
    with open(categories_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Category'])
        for i in lst_cats:
            writer.writerow([i])

def import_categories():
    categories_file = 'Categories.csv'
    lst_cats = []
    try:
        with open(categories_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for i in reader:
                lst_cats.append(i[0])
    except FileNotFoundError:
        pass
    return lst_cats



if __name__ == '__main__':
    show_main_window()