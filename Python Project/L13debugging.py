# Describe problem
# def my_function():
#     for i in range(1,21):
#         if i==20:
#             print("You got it.")
# my_function()



# REproduce the bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dic_num=randint(1,6)
# print(dice_imgs[dic_num-1])



# Play Computer
# year=int(input("What's your year of birth? "))
# if year>1989 and year<=1994:
#     print("You are a millenial.")
# elif year>1994:
#     print("You are a Gen Z.")



# PRINT is your Friend 
# pgs=0
# words_per_pgs=0
# pgs=int(input("Number of pages: "))
# words_per_pgs=int(input("Number of words per pages: "))
# total_words=pgs*words_per_pgs
# print(total_words)



# USE of DEBUGGER
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])




