#Perfect Guess Game
import random
number = random.randint(1,100)
no_of_guess = 0

print("\nWelcome to the Perfect Guess Game")
print("=================================\n")
user_input = int(input("Enter a number between 1 to 100: "))

while True:
    no_of_guess+= 1
    if user_input < number:
        print("You entered a smaller number. Please try again")
        user_input = int(input("Enter a number between 1 to 100: "))
    elif user_input > number:
        print("You entered a larger number. Please try again")
        user_input = int(input("Enter a number between 1 to 100: "))
    else:
        print(f"Congratulations! You guessed the number {number} in {no_of_guess} attempts")
        break