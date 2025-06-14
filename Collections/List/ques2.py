#Find the maximum and minimum in a list.

num = [2, 6, 3, 4, 10, 16, 19, 28, 39, 60]
min = num[0]
max = num[0]

for i in num:
    if i< min:
        min = i
    if i > max:
        max = i

print("The minimum value in the list is:", min)
print("The maximum value in the list is:", max)
