my_list = [500, 21, 55, 63, 78, 13, 9, 22, 14]
print(my_list)

first_index = my_list[0]
last_index = my_list[-1]
my_list.pop(0)
my_list.pop(-1)
my_list.insert(0, last_index)
my_list.append(first_index)
print(my_list)