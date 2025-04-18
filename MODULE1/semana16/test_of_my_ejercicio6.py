from ejercicio6 import prim_list

def test_with_only_prime_nums():
    user_input = [2, 3, 5, 7, 11, 13]
    result = prim_list(user_input)
    assert result == [2, 3, 5, 7, 11, 13]

def test_with_all_kind_of_nums():
    user_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = prim_list(user_input)
    assert result == [2, 3, 5, 7]

def test_with_no_prime_nums():
    user_input = [0, 1, 4, 6, 8, 9, 10]
    result = prim_list(user_input)
    assert result == []