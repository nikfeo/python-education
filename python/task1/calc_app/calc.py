"""This is a simple calculator module

with four operations: addition, subtraction, multiplication, division
"""


class Calculator:
    """Creating simple calculator class and"""

    @staticmethod
    def addition(num_1, num_2):
        """Returns a sum of two numbers"""
        return num_1 + num_2

    @staticmethod
    def subtraction(num_1, num_2):
        """Returns a difference of two numbers"""
        return num_1 - num_2

    @staticmethod
    def multiplication(num_1, num_2):
        """Returns a multiplication of two numbers"""
        return num_1 * num_2

    @staticmethod
    def division(num_1, num_2):
        """Returns a division of two numbers"""
        return num_1 / num_2


calculation = Calculator()

print(calculation.addition(5, 5))
print(calculation.subtraction(10, 5))
print(calculation.multiplication(5, 5))
print(calculation.division(5, 5))
