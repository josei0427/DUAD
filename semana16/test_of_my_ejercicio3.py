from ejercicio3 import the_phrase
import pytest

def test_with_small_sentence():
    user_input = "hello world"
    result = the_phrase(user_input)
    assert result == "dlrow olleh"

def test_with_big_sentence():
    user_input = "Today is a great to learn how to code"
    result = the_phrase(user_input)
    assert result == "edoc ot woh nrael ot taerg a si yadoT"

def test_with_no_phrase():
    user_input = ""
    with pytest.raises(ValueError):
        the_phrase(user_input)