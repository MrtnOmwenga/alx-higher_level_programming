#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    weight_sum = 0
    for i in my_list:
        result = result + (i[0] * i[1])
        weight_sum = weight_sum + i[1]
    result = result / weight_sum
    return (result)
