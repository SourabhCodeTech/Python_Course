# # n! = n*n-1*n-2*n-3........1
# # n! = n * (n-1)!
# def factorial_iteratives(n):
#     """
#     :param n: Integer
#     :return: n*n-1*n-2*n-3........1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac


# def factorial_recursive(n):
#     """
#     :param n: Integer
#     :return: n*n-1*n-2*n-3........1
#     """
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1) 
    
#     # 5 * factorial_recursive(4)
#     # 5 * 4 * factorial_recursive(3)
#     # 5 * 4 * 3 * factorial_recursive(2)
#     # 5 * 4 * 3 * 2 * factorial_recursive(1)
#     # 5 * 4 * 3 * 2 * 1

# number = int(input("Enter the Number: "))
# print("Factorial Using Iterative:", factorial_iteratives(number))
# print("Factorial Using Iterative:", factorial_recursive(number))
    

# Quiz
# 0 1 1 2 3 5 8 13 .....
def febonachi(n):
    febo = 0
    for i in range(n):
        febo = febo + (i + )
        return febo
    
number1 = int(input("Enter the number: "))
print(febonachi(number1))