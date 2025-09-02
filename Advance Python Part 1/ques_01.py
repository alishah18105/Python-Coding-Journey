#Write a program to open thrEe files 1.txt,2.txt and 3 txt. If any of these files are not present, 
# a message without exiting the prograM must be prinTed prormpting the same

try:
    with open("1.txt","r") as f1:
        print(f1.read())

except FileNotFoundError:
    print("File 1 is not present")

try:
    with open("1.txt","r") as f2:
        print(f2.read())

except FileNotFoundError:
    print("File 2 is not present")

try:
    with open("1.txt","r") as f3:
        print(f3.read())

except FileNotFoundError:
    print("File 3 is not present")