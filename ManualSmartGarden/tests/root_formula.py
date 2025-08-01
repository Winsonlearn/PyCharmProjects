import math


def calculate_root(x):
    if x < 0:
        raise ValueError("Input harus lebih besar dari 0")
    return math.sqrt(x)

def calculate_divide(a, b):
    if b == 0:
        raise ValueError("Pembagi tidak boleh 0")
    return a / b

