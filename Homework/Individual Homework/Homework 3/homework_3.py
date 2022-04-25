# Exercise 1
from tkinter import E


def integer_sum(*args, **kwargs):
    sum = 0
    for value in args:
        if type(value) == int:
            sum += value
    return sum


print(integer_sum(1, 5, -3, 'abc', [12, 56, 'cad']))
print(integer_sum())
print(integer_sum(2, 4, 'abc', param_1=2))

# Exercise 2


def recursive_sum(n: int):
    if n == 0:
        return 0, 0, 0

    sum, even_sum, odd_sum = recursive_sum(n-1)
    if n % 2 == 0:
        return n + sum, n + even_sum, odd_sum

    return n + sum, even_sum, n + odd_sum


print(recursive_sum(5))

# Exercise 3


def input_integer():
    value = input("Please enter a value: ")
    try:
        return int(value)
    except Exception:
        return 0


print(input_integer())
