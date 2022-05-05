# Create a Dictionary and take Input from the user and return the meaning of the word from the dictionary

dic = {"Apple":"सेब", "Mango":"आ म", "Lichi":"लीची", "Orange":"संतर", "Pineapple":"नासपत्ती", "Turnip":"शलजम", "Grapes":"अंगूर", "Kite":"पतंग"} 
input = input("Enter KeyWord: ")
name = input.capitalize()
print(dic[name])