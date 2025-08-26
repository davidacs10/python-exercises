def print_increasing_power(x):
    cnt = 1
    while cnt <= x:
        power_jump = cnt**2
        if power_jump > x:
            break
        print(power_jump, end=" ")

        cnt += 1
