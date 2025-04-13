from ejercicio1 import my_bubblesort
import random
import pytest

def test_of_my_bubblesort():
    my_list = [3, 6, 1]
    result = my_bubblesort(my_list)
    assert result == [1, 3, 6]

def test_of_my_bubblesort_long_list():
    my_long_list = random.sample(range(1, 501), 120)
    result = my_bubblesort(my_long_list)
    assert result == sorted(my_long_list)

def test_of_my_bubblesort_empty_list():
    result = my_bubblesort([])
    assert result == []

def test_of_my_bubblesort_with_no_list():
    user_input = '123'
    with pytest.raises(TypeError):
        my_bubblesort(user_input)