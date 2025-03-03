import PySimpleGUI as sg

def income_window(data_from_user, lst_cats):
    layout = [
        [sg.Text("Agregar un ingreso", font=("Helvetica", 16, ))],
        [sg.Text("Ingrese el nombre"), sg.InputText(key='-NAME-')],
        [sg.Text("Ingrese la categoria"), sg.InputText(key='-CATEGORY-')],
        [sg.Text("Ingrese el monto"), sg.InputText(key='-AMOUNT-')],
        [sg.Button("Agregar", bind_return_key=True)]
    ]

    window = sg.Window('Manejo de Finanzas', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Agregar':
            name = values['-NAME-']
            category = values['-CATEGORY-']
            w_type = 'Ingreso'
            amount = values['-AMOUNT-']
            if category not in lst_cats:
                sg.popup('ERROR: La categoría no existe. Registre la categoria por favor.')
                window.close()
            elif name and category and amount:
                data_from_user.append([name, category, w_type, amount])
                sg.popup('Datos agregados correctamente.')
                window.close()
                return data_from_user
        else:
            sg.popup('ERROR: No pueden haber espacios vacíos. Por favor revisa nuevamente.')


    window.close()