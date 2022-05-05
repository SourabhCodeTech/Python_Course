# Health Management System
# 3 Client - Harry, Rohan and Hammad
# Total 6 Files
# Write a Function that when exected takes as input  client name

def getdate():
    import datetime
    return datetime.datetime.now()
# print(getdate())

lo_re = input("Log karna chataho Ya Receive karna chataho: ")
if lo_re == "Log":
    name = input("Kis ko log karna chataho: ")
    if name == name:
        food_exer = input("Food Log karna chataho Ya Exercise Log karana chataho: ")
        if food_exer == "Food":
            Food = input("Food Name: ")
            create_file = open(f"{name}_Food_Name.txt", "a")
            namefile = open(f"{name}_Food_Name.txt", "a")
            namefile.write(str([str(getdate())])+": "+Food+"\n")
            create_file.write(Food)
            print("SuccesFully Right")
        elif food_exer == "Exercise":
            Exercise = input("Exercise Name: ")
            create_file = open(f"{name}_Exercise_Name.txt", "a")
            namefile = open(f"{name}_Exercise_Name.txt", "a")
            namefile.write(str([str(getdate())])+": "+Exercise+"\n")
            create_file.write(Exercise)
            print("SuccesFully Right")
elif lo_re == "Retrieve":
    name = input("Kis ko Retrieve karna chataho: ")
    if (name == name):
        food_exer = input("Food Retrieve karna chataho Ya Exercise Retrieve karana chataho: ")
        if food_exer == "Food":
            read_file = open(f"{name}_Food_Name.txt")
            print(read_file.read())
        elif food_exer == "Exercise":
            op = open(f"{name}_Exercise_Name.txt")
            print(op.read())
