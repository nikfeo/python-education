"""
This module implements factorial function
"""


def factorial(number: int):
    """
    Calculates factorial of specified number
    :param number: integer
    :return: integer
    """
    if not isinstance(number, int):
        raise TypeError('The argument "number" must be integer')
    else:
        if number < 0:
            raise ValueError('The argument "number" must be positive integer')
        elif number == 1:
            return 1
        else:
            return number * factorial(number-1)
