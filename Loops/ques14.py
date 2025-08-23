#Write a python program to print following star pattern
#* * *
#*   *
#* * *

for i in range(1,4):
    for j in range(1,4):
        if i == 2 and j == 2:
            print("  ", end=" ")
        else:
            print("* ", end=" ")
    print()