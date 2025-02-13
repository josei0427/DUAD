from ejercicio4 import letter_viewer
import pytest

def test_with_of_normal_sentence():
    user_input = "Football is the GREATEST sport of all time"
    result = letter_viewer(user_input)
    assert result == (9, 26)

def test_with_of_lower_letters():
    user_input = "life is such a gift"
    result = letter_viewer(user_input)
    assert result == (0, 15)

def test_with_no_phrase_word():
    user_input = ""
    with pytest.raises(ValueError):
        letter_viewer(user_input)