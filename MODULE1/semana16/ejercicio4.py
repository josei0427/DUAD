def letter_viewer(my_phrase):
    if my_phrase == "":
        raise ValueError("It's empy, no phrase or word introduced.")
    else:
        upper_cases = 0
        lower_cases = 0
        for i in my_phrase:
            if i.islower():
                lower_cases += 1
            elif i.isupper():
                upper_cases += 1
    return (upper_cases, lower_cases)