my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
other_list = []
for i in my_list:
    if i % 2 == 0:
        other_list.append(i)
print(other_list)