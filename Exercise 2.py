# Exercise 2 - Faulty Calculator
# Design a calculator which will correctly solve all the problems except the following ones:
# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4
# Your program should take operator and the two numbers as input from the user and then return the result

print("Welcome To Calculator!")
print(
"""
Please Type int the math Operation you Would Like toComplete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
""")
operator = input("Choose Any Operator: ")
num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Second Number: "))
# Addition
if operator == '+' and num1 == 56 and num2 == 9:
    print("56 + 9 = 77")
elif operator == '+':
    print(num1, "+", num2, "=", num1 + num2)
# Subtraction
elif operator == '-' :
    print(num1, "-", num2, "=", num1 - num2)
# Multiplication
elif operator == '*' and num1 == 45 and num2 == 3:
    print("45 * 3 = 555")
elif operator == '*':
    print(num1, "*", num2, "=", num1 * num2)
# division
elif operator == '/' and num1 == 56 and num2 == 6:
    print("56 / 6 = 4")
elif operator == '/':
    print(num1, "/", num2, "=", num1 / num2)
# Power Calculate
elif operator == '**':
    print(num1, "**", num2, "=", num1 ** num2)
# Modulo
elif operator == '%':
    print(num1, "%", num2, "=", num1 % num2)