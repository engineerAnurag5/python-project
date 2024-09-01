logo =  """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


def add(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operation={
    '+':add ,
    '-':subtraction ,
    '*':multiply ,
    '/':divide ,

}
def calculator():
    a=float(input("What's the first number?: "))
    for  symbol in operation:
        print(symbol)
    should_continue=True
    while should_continue:
        sign=input("Pick The Operation From Above ") 
        b=float(input("What's the next number?: "))
        calculation_function=operation[sign]
        answer=calculation_function(a,b)
        print(f"{a} {sign} {b}={answer}")
        if input(f"Type 'y' to continue  calculation with {answer}: or 'n' to start a new calculation: ")=='y':
            a=answer
        else  :
            should_continue=False
            calculator()
         
calculator()