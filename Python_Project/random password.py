# Random Password Generator

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '123456890'
symbol = ')(*&^%$#!{}[]|'

inputnum = int(input("Enter the password lenght number: "))
length = inputnum

arr = lower + upper + number + symbol
result = "".join(random.sample(arr, length))
print(result)
a= input()
