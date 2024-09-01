print("Welcome to Python Pizza Deliveries! ")
print("MENU::\n Small pizza = $15\n Medium pizza = $20\nLarge pizza= $25")

size=input("What size pizza do you want? S,M or L:  ")
bill=0
if size=="S":
    bill=15
    add_pepperoni= input('Do you want extra pepperoni? Y or N: ')
    if (add_pepperoni=="Y") :
     bill+=2
elif size=="M":
    bill=20
    add_pepperoni= input('Do you want extra pepperoni? Y or N: ')
    if (add_pepperoni=="Y") :
     bill+=3
else:
    bill=25
    add_pepperoni= input('Do you want extra pepperoni? Y or N: ')
    if (add_pepperoni=="Y") :
     bill+=3
extra_cheese=input('Do you want extra cheese? Y or N:  ')
if extra_cheese=='Y':
   bill+=1

print(f"Your bill is ${bill}")