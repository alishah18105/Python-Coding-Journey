#The game() function in a program lets a user play a game and returns the score as an integer.
#  You need to read a file "Hiscore.txt", which is either blank or contains the previous high
# score. You need to write a program to update the high score whenever game() breaks the 
# current high score.
import random

def game( score = 0):
    computer = random.choice([-1,0,1])
    
    user = int(input("Enter 1 for snake, 0 for water and -1 for gun: "))
    choiceDic = {1:"snake", 0:"water", -1:"gun"}
    print(f"You chose {choiceDic[user]}")
    print(f"Computer chose {choiceDic[computer]}")

    if user == computer:
        print("It's a tie")
    else:
        if (user == 1 and computer == 0) or (user == 0 and computer == -1) or (user == -1 and computer == 1):
            print("You win")
            game(score+1)
        else:
            print("Computer wins")
            with open('Hiscore.txt', 'r') as f:
                hiscore = f.read()
            if hiscore=='':
                with open('Hiscore.txt', 'w') as f:
                    f.write(str(score))
            elif int(hiscore)<score:
                with open('Hiscore.txt', 'w') as f:
                    f.write(str(score))
            print(f"Your score is {score}")
            print("Game Over")
            return

game(0)            


