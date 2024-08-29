def letter_viewer(my_phrase):
    upper_cases = 0
    lower_cases = 0
    for i in my_phrase:
        if i.islower():
            lower_cases += 1
        elif i.isupper():
            upper_cases += 1
    return (upper_cases, lower_cases)

result = letter_viewer("I love Nacion Shushi")
print(f'There’s {result[0]} upper cases and {result[1]} lower cases')