def my_phrase(text):
    text_list = text.split("-")
    text_list.sort()
    new_list = text_list
    return new_list


text = "python-variable-funcion-computadora-monitor"
correct_text = my_phrase(text)
print("-".join(correct_text))