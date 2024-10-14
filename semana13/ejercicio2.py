def only_numbers(func):
    def wrapper(*args):
        for i in args:
            if not isinstance(i, (int, float)):
                raise ValueError("This should be only for numbers")
        return func(*args) 
    return wrapper

@only_numbers
def print_numbers(*args):
    print(args)


print_numbers(1,5,8,4,3,10)