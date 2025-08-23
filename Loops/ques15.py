#Write a python program to print following star pattern
#*
#**
#***

for i in range(3):
    for j in range(i+1):
        if j<=i:
            print("*", end="")
    print()