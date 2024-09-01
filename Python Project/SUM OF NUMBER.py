print("SUM OF EVEN NUMBER BETWEEN 1 AND 100")
sum=0
for number in range (2,101,2):
    sum+=number
print(sum)
print("another way ")
total=0
for number in range (1,101):
    if number%2==0:
        total+=number
print(total)
