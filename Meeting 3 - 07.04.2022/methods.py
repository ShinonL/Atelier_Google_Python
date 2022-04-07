# sum of two numbers
def sum(a, b = 1):
    if type(a) == str:
        return int(a) + b
    return a + b

def return_tuple(a, b) -> (int, int):
    """
    :param a: first number
    :param b: second number
    :return: sum, difference
    """
    return a + b, a - b

print(return_tuple(3, 4))