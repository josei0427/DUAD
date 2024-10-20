def grocery_list(func):
    def wrapper (*args):
        print(args)
        result = func(*args)
        return result
    return wrapper


@grocery_list
def add_item(*args):
    print(f'Se necesita comprar: {args}')
    return

Add_item("Carne", "Leche", "Galletas", "Baterias")