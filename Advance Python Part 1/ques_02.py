# Write a program to print third, fifth and seventh element from a list using enumerate function

list1 = [23,45,67,89,90,12,34,56,78]

for index, value in enumerate(list1):
    if index in (2,4,6):
        print(f"Element at index {index} is {value}")