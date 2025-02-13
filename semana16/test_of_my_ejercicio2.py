from ejercicio2 import list_sum

def test_of_sum_with_alot_of_nums():
    my_list = [22, 50, 14, 8, 33, 49, 11, 7, 61]
    result = list_sum(my_list)
    assert result == 255

def test_of_sum_with_afew_nums():
    my_list = [12, 8, 2, 10]
    result = list_sum(my_list)
    assert result == 32

def test_with_an_empty_list():
    result = list_sum([])
    assert result == 0