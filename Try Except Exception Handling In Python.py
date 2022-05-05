num1 = input("Enter Number 1: ")
num2 = input("Enter Number 2: ")

try:
    print("The Sum of These two number is: ", 
    int(num1)+int(num2))
except Exception as e:
    print(e)

print("The is a Very Important Line")