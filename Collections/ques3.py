#Remove duplicates from a list.
num = [2, 6, 3, 4, 10, 16, 19, 28, 39, 60, 2, 6]
unique = []

for i in num:
    if i not in unique:
        unique.append(i)
print("The list after removing duplicates is:", unique)