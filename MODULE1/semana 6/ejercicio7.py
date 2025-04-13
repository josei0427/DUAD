def prim_list(my_list):
    num_prim = []
    for i in my_list:
        if i > 1:
            es_primo = True
            for j in range(2, i):
                if i % j == 0:
                    es_primo = False
                    break
            if es_primo:
                num_prim.append(i)
    return num_prim


my_list = [1,4,6,7,13,9,67]
list_func = prim_list(my_list)
print(list_func)