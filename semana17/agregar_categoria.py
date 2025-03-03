import PySimpleGUI as sg

def category_window(lst_cats):
    headers = ['Categorias existentes']
    layout = [
        [sg.Text("Agregar una categoria", font=("Helvetica", 16, ))],
        [sg.Text("Ingrese el nombre de la categoria"), sg.InputText(key='-CATEGORY-')],
        [sg.Table(values= lst_cats, headings=headers, key='-TABLE-', auto_size_columns=True, justification='right')],
        [sg.Button("Agregar", bind_return_key=True)]
    ]

    window = sg.Window('Manejo de Finanzas', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Agregar':
            category = values['-CATEGORY-']
            if category in lst_cats:
                sg.popup('ERROR: La categoría ingresada ya existe. Registre una categoria nueva.')
            elif category:
                lst_cats.append(category)
                sg.popup('Categoria agregada correctamente.')
                window.close()
                return lst_cats
        else:
            sg.popup('ERROR: No pueden haber espacios vacíos. Por favor revisa nuevamente.')


    window.close()