import random
import os

rock='''  
    _________
____'   _____ )
      (_________)
       (_______)
       (_______)
----.___(_____) 
'''
paper='''  
    ______________
____'       ______)
            ________)
            _______)
            ______)
----.__________)

'''
scissors=''' 
     ______________
_____'     ________)_____
           ______________)___
           __________________)
            _______)
-----.______)
'''
# print(rock)
# print(paper)
# print(scissors)

print("Type 0 for rock\nType 1 for paper\nType 2 for scissors")
# *****
scores=[]
# ****
def rps():
        should_continue=True
        while should_continue:
            # *****
            global scores
            # *****
            game_image=[rock,paper,scissors]
            user_input=int(input("Press your number :  "))
            print(game_image[user_input])
            
            computer_think=random.randint(0,2)
            print(f'what computer choose:{computer_think}')
            print(game_image[computer_think])
            
            if user_input==0 and computer_think==2:
                print("CONGRATULATION!🎉 You Win")
                scores.append(1)
            elif user_input>computer_think and user_input<3:
                print("'CONGRATULATION!🎉 You Win'")
                scores.append(1)
            elif user_input==computer_think:
                print("It's DRAW 🙂")
                scores.append(0)
            else:
                print('You loose 😔')
                scores.append(-1)
            ask=input("Do you want to play again(say 'Yes' or 'No'): ").lower()
            # print(scores)
            if ask=="no":
                # ***
                print(f"The final score list is: {scores}")
                print(f"Hey There, your final score is: {sum(scores)}")
                should_continue=False
                print("Thank You")
                 
            else:
                 os.system("cls" if os.name=="nt" else "clear")    
                
                
rps()
