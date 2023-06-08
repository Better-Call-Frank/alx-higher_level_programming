#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide

a = 10
b = 5

result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

print("The sum of", a, "and", b, "is:", result_add)
print("The difference between", a, "and", b, "is:", result_subtract)
print("The product of", a, "and", b, "is:", result_multiply)
print("The division of", a, "and", b, "is:", result_divide)
