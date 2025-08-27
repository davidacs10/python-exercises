def pos(n):
    for i in range(n - 1, 0 - 1, -1):
        print(i, end=" ")


def neg(n):
    for i in range(n, 1):
        print(i, end=" ")


pos(4)
neg(-3)
