a = '**********for loop'
print(a.capitalize())

nm='anurag'
for i in nm:
    print(i)
    # if( i=='a') :
        # print("it's special")
# for k in range(9):
   # print(k)
total=0
for n in range (1,12):
     print(n)
    #  print(n+2)  
     total+=n
    #  when we print total it give us sum of no from 1 to 11
print(total)

for k in range(1,21,4):
     print(k)
    #  3rd no of range is the diff btw the no.

    
b='**********WHILE LOOP*****'

print(b)
 
i=0
while (i<3):
    print(i)
    i=i+1
print("NEXT EXAMPLE")

count=5
while(count>= -3):
    print(count)
    count=count-2
else :
    print("THANK U")   
print("NEXT EXAMPLE")

i=int(input('enter the  no.  '))
while(i<=38):
    i=int(input('enter the no.  '))
    print(i)
else :
    print ("thanks")
print('done with loop')


b='**** BREAK'
print(b)
# loop ko chhod kar nikal ja
for i in range(12): 
  if(i==10):
    print('iske aage print nhi hoga ')
    break
  print(i)

c='****CONTINUE'
print(c)
for i in range(12):
    if (i==10):
        print('--')
        continue
    print(i)