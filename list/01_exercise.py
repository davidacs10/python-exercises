def get_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in arr[1:]:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i

    return (min_val, max_val)


arr = [3, 4, 5, 1, 0.5, 400, 1000, 99, 132, 42, 50, 2001]
print(get_min_max(arr))
