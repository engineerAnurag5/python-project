# easy level
# import random
# letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# number=['0','1', '2', '3', '4', '5','6','7','8','9']
# symbol=['!','#','$','%','&','*','+','-','_' ]
# print("Welcome to PyPassword Generator")
# nr_letter=int(input('How many letter would you like in your password?\n'))
# nr_number=int(input("How many numbers do you want in password?\n"))
# nr_symbol=int(input('How many symbols would you like ?\n'))
# password=""
# for char in range(1, nr_letter+1):
#     random_char=random.choice(letter)
#     password+=random_char
#     # print(password)
# for no in range(1,nr_number+1):
#   password +=random.choice(number)
#     # print(password)
# for sym in range (1,nr_symbol+1):
#     password+=random.choice(symbol)
# print(password)

#  hard level
import random
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number=['0','1', '2', '3', '4', '5','6','7','8','9']
symbol=['!','#','$','%','&','*','+','-','_' ]
print("Welcome to PyPassword Generator")
nr_letter=int(input('How many letter would you like in your password?\n'))
nr_number=int(input("How many numbers do you want in password?\n"))
nr_symbol=int(input('How many symbols would you like ?\n'))
password_list=[]
for char in range(1, nr_letter+1):
    random_char=random.choice(letter)
    password_list+=random_char
    # print(password)
for no in range(1,nr_number+1):
  password_list +=random.choice(number)
    # print(password)
for sym in range (1,nr_symbol+1):
    password_list+=random.choice(symbol)
print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
   password+=char
print(f"Your password is: {password}")
 