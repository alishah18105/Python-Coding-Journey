#Write a program to count how many times each element appears in a tuple.

num = (2, 7, 5, 3, 8, 14, 11, 19, 6, 12, 2, 7)
elements_count = {}
for x in num:
    if x in elements_count:
        elements_count[x] += 1
    else:
        elements_count[x] = 1
print("Count of each element in the tuple:")
for key, value in elements_count.items():
    print(f"{key}: {value}")