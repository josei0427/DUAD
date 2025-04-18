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
    