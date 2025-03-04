import PySimpleGUI as sg

def expense_window(data_from_user, lst_cats):
    layout = [
        [sg.Text("Add an expense", font=("Helvetica", 16, ))],
        [sg.Text("Enter the title"), sg.InputText(key='-NAME-')],
        [sg.Text("Enter the category"), sg.InputText(key='-CATEGORY-')],
        [sg.Text("Enter the amount"), sg.InputText(key='-AMOUNT-')],
        [sg.Button("Accept", bind_return_key=True)]
    ]

    window = sg.Window('Financial Management System', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Accept':
            name = values['-NAME-']
            category = values['-CATEGORY-']
            w_type = 'Expense'
            amount = values['-AMOUNT-']
            if category not in lst_cats:
                sg.popup('ERROR: Category does not exist. Please register a category.')
                window.close()
            elif name and category and amount:
                data_from_user.append([name, category, w_type, amount])
                sg.popup('Data added successfully.')
                window.close()
                return data_from_user
        else:
            sg.popup('ERROR: There cannot be any empty spaces. Please check again.')


    window.close()