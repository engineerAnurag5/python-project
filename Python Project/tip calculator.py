a=input('Enter your name here : ')
print('Welcome',a,'to the TIP CALCULATOR')
b=int(input('What was the total bill? :(in rupees)  \n '))
t=int(input('What percentage tip would you like to give ? 10,15,18, or 20:   \n'))
p=int(input('How many person to split the bill? \n'))
pay=(b+b*t/100)/p
print('Each person shold pay: ', round(pay,2)) 
