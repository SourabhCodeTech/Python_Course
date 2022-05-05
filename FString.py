import math

# F String
me = "Sourabh"
a1 = 5


# a = "I am %s %s"%(me, a1)
# a = "This is {1} {0}"
# b = a.format(me, a1)
a = f"This is {me} {a1} {math.cos(60)}."
print(a)