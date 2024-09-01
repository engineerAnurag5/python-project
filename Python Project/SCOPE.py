################ SCOPE ######################
enemies=1
def increase_enemies():
    enemies=2
    print(f"Enemies inside function : {enemies}")
increase_enemies()
print(f"Enemies outside function : {enemies}")
######### Local Scope:
# When you define a variable inside a function (or any other block, like an if statement or a loop), that variable’s scope is local to that block.
# It exists only within that block and any nested blocks within it.
# Once you step out of the block, the variable vanishes like morning mist


def apple():
    number_of_apple=342
    print(f"The  number of apple is : {number_of_apple}")
apple()
# print (f"The  number of apple is : {number_of_apple}")>>>>>>>>>>>>THIS THROW ERROR NAMED AS NameError



############# Global scope:
# Variables defined outside any function or block have global scope.
# They’re accessible from anywhere in your code.


player_health = 10
def apple():
    number_of_apple=342
    print(f"The  number of apple is : {player_health}")
apple()
print(player_health)
# THere is no block scope
game_level=3
def create_enemy():
    enemies=["Skeleton","Zombie","Alien"]
    if game_level<5:
        new_enemies=enemies[0]
        print(new_enemies)############ Local scope
create_enemy()
########### MODIFYING GLOBAL SCOPE
enemies=1
def increase_enemies():
    # global enemies
    
    print(f"Enemies inside function : {enemies}")
    return enemies+1
enemies=increase_enemies()
print(f"Enemies outside function : {enemies}")
# lecture 4
#  Global constants
# >>>>>>>>>>>>>>>when we use value or const and we don't want to change it we use global scope
# eg; pi=3.14159
#     url="https://www.google.com"