import PySimpleGUI as sg

def category_window(lst_cats):
    headers = ['Existing categories']
    layout = [
        [sg.Text("Add a category", font=("Helvetica", 16, ))],
        [sg.Text("Enter the name for the category"), sg.InputText(key='-CATEGORY-')],
        [sg.Table(values= lst_cats, headings=headers, key='-TABLE-', auto_size_columns=True, justification='right')],
        [sg.Button("Accept", bind_return_key=True)]
    ]

    window = sg.Window('Financial Management System', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Accept':
            category = values['-CATEGORY-']
            if category in lst_cats:
                sg.popup('ERROR: The category entered already exists. Please register a new category.')
            elif category:
                lst_cats.append(category)
                sg.popup('Category added successfully.')
                window.close()
                return lst_cats
        else:
            sg.popup('ERROR: There cannot be any empty spaces. Please check again.')


    window.close()