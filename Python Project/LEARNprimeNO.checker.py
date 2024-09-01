print("Welcome to Prime number checker")
n=int(input("Enter your number: "))
def prime_checker(number):
    if n==1:
        print("It's not a prime number")
    else:
        for i in range(2,number-1):
            if number%i==0:
                is_prime=False #ae is_prime kyu define kiye h
        if is_prime:
            print("It's  a prime number")
        else:
            print("It's not a  prime number")

prime_checker(number=n)