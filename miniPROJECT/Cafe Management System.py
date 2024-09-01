print("Welcome to our restaurant....\nHere's the MENU:\n"
      "Pizza:Rs40\n"
      "Pasta:Rs50\nBurger:Rs60\nSalad:Rs70\nCoffee:Rs80\n"
      "sandwiches:Rs55\nSoft drink:Rs60")
item={"pizza":40,"pasta":50,"burger":60,"salad":70,"coffee":80,"sandwiches":55,
      "soft drink":60}
ask=input("Enter your first item you want to order=  ").lower()
p=int(input('For how many person ? '))
# item={"pizza":40,"pasta":50,"burger":60,"salad":70,"coffee":80,}
prize_list=[]
prize_list.append(item[ask]*p)

# print(prize_list)
print(f"Order of {ask} has been added for {p}person..")
ask_again=input("Do you want to order  anything else? ")
is_continue=True
if ask_again=="yes":

      while not ask_again=="no":
             ask2=input("Enter the next item").lower()
             p = int(input('For how many person ? \n'))
             prize_list.append(item[ask2]*p)
             # print(prize_list)
             print(f"Order of {ask2} has been added for {p} person..")
             ask_again = input("Do you want to order  anything else? ")


else:
      is_continue = False


b=sum(prize_list)
t=int(input('What percentage tip would you like to give ? 10,15,18, or 20:   \n'))


if input("Do you want to split the bill?")=="yes":
   split=int(input("In how many person do you want to split the bill? "))
   p=(b+(b*t)/100)/split
   # bill=(sum(prize_list)+pay)/split
   print('Each person shold pay: ', round(p, 2))
else:
    print("Total bill to pay is:", (b+(b*t)/100))

print("THANK YOU FOR VISINTING...\n ")

