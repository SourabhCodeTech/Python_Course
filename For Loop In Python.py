# list = [["Harry", 1], ["Larry", 2], ["Carry", 230],["Array", 5000]]
# print(list)

# dic = dict(list)
# print(dic)

# for item, lollypop in dic.items():
#     print(item, "and lollypop is: ", lollypop)

# for item in dic:
#     print(item)

# Quick Quiz

list1 = [int, float, "Sourabh", "Rohan", 4, 93, 9, 28, 19, 659, 6]

for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)