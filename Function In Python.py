# a = 9
# b = 8
# c = sum((a, b))
# print(c)

# def function1(a, b):
#     print("Hello You are in Function 1", a + b)

# print(function1())
# function1(5, 7)

def function2(j, k):
    """This is a Function Which will Calculate Average of Two Numbers.\nThis function doesn't work for three numbers"""
    avg = (j + k)/2
    # print(avg)
    return avg 

# v = function2(5, 7)
# print(v)
print(function2.__doc__)