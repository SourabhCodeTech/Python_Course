# l = 10 # Gobal
# def function1(n):
#     # l = 5 # Local
#     m = 8 # Local
#     global l
#     l = l + 50
#     print(l, m)
#     print(n, "I have printed")

# function1("This is me")
# print(l)


x = 89
def harry():
    x = 10
    def rohan():
        global x
        x = 88
    # print("Before Calling Rohan()", x)
    rohan()
    print("After Calling Rohan()", x)

harry()
print(x)

