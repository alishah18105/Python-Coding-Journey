# Create a snake, water gun game
'''
Snake drinks water
Water damages gun
Gun kills snake
'''
import random
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
    else:
        print("Computer wins")
