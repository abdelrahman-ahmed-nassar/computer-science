

def power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result


print(power(8, 3))


# or
print(8**3)


# def powering (B_num, P_num):
