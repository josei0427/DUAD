def my_bubblesort(my_list):
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")
    for other_i in range(0, len(my_list)-1):
        for i in range(len(my_list)-1, other_i, -1):
            current_number = my_list[i]
            next_number = my_list[i-1]
            if current_number < next_number:
                my_list[i] = next_number
                my_list[i-1] = current_number
    return my_list
