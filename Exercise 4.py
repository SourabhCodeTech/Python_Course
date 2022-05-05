# Pattern Printing
# Input = Integer n
# Boolean = True or False
# True n = 4
    # *
    # **
    # ***
    # ****
# False n = 4
    # ****
    # ***
    # **
    # *

n = int(input("Enter Ek Number:"))
bool_val = input("Enter True Or False:")
if bool_val == "1":
    for i in range(0,n+1):
        print("*"*i)
if bool_val == "0":
    for i in range(n, 0, -1):
        print("*"*i)
