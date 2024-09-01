from random import randint
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
answer=randint(1,100)
# guess=int(input("Make a guess: "))
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def game():
    def check_answer(guess,answer,turns):
     if guess>answer :
        print("Too high")
        return turns-1
     elif guess<answer:
        print("Too low")
        return turns-1
     else:
        print(f"You  got it! The answer was {answer}")
    #  Make function to set difficulty
    def difficulty():
        level=input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level=="easy":
            # global >>>>too use this value in outside the def fxn
            global turns
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS
    turns=difficulty()
    guess=0
    # repeaat the guessing
    while guess !=answer:
      print(f"You have {turns} attempts remaining to guess the number.")
      guess=int(input("Make a guess: "))


      turns= check_answer(guess,answer,turns)
      if turns ==0:
         print("You've run out of guesses, You lose")
         return # Remember that with functions you have the return keyword
    #   You can return with an output or you can just write return for it to exit and end

game()
