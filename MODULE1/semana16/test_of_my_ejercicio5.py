from ejercicio5 import my_phrase

def test_of_the_function():
    user_input = "python-variable-funcion-computadora-monitor"
    result = my_phrase(user_input)
    assert result == ['computadora', 'funcion', 'monitor', 'python', 'variable']

def test_with_words_already_sorted():
    user_input = "año-bisiesto-cielo-piedra"
    result = my_phrase(user_input)
    assert result == ['año', 'bisiesto', 'cielo', 'piedra']

def test_with_words_and_nums():
    user_input = "zapato-2-pantalon-1-gato"
    result = my_phrase(user_input)
    assert result == ['1', '2', 'gato', 'pantalon', 'zapato']