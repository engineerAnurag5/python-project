import random
print("LET'S CHECK YOUR PRIDICTION \nEnter any number between 1 and 20")
a=input("LET'S CHECK YOUR LUCK :  ")
randomno=random.randint(1,20)
print(f"what computer think is {randomno}")
if int(a)==randomno :
    print('CONCATULATION! \n You are very lucky')
else:
    b=randomno-int(a)
    print(f'Your are {b} less or more')
    print("let's try again")
# print(type(randomno))
