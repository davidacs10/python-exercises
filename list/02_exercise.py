def find_union(a, b):
    new_arr = set(a + b)
    sorted_list = sorted(new_arr)

    return sorted_list


lst_1 = [2, 1, 3, 4, 100]
lst_2 = [2, 1, 3, 5]

print(find_union(lst_1, lst_2))
