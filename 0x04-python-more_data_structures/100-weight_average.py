#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    prod = []
    denom = 0

    for a, b in my_list:
        prod.append(a * b)
        denom += b

    avg = sum(prod) / denom
    return avg
