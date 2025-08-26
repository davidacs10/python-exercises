def check_status(a, b, flag):
    return ((a >= 0) ^ (b >= 0) and not flag) or ((a < 0) and (b < 0) and flag)


print(check_status(-7, -3, True))
