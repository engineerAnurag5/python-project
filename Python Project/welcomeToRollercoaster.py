name=input('Enter your name :  ')
print('WELCOME!',name,'in the world of rollercoaster')
hight=float(input('Enter you hight in cm:  '))
bill=0
if hight>=120:
    print('You can enjoy ride of rollercoaster',name)
    age=int(input("Enter your age here: "))
    
    if age>=18 and age<45:
        bill= 12
        print('ADULT TICKETS are  $12')
    elif age>12 and age<18:
        bill=7
        print('YOUTH TICKETS are $7')
    elif age>=45 and age<=55:
       bill=0
       print("For MIDLIFE crisis ride is FREE ")
    
    else:
        bill=5
        print(' CHILD TICKET are $5')
    want_photo=input('Do you want a photo taken ? Y or N :  ')
    if want_photo=="Y":
      bill=bill+3
    #   bill+=3
    print(f"your final bill is: ${bill}")

else:
  print('Sorry, you have to grow taller before you can ride ')
  
