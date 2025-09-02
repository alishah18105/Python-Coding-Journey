#Write a list comprehenion to print a list which contains the multiplication table of a user entered number

num = int(input("Enter a number: "))
multiplication = [i*num for i in range(1,11)]
print(multiplication)