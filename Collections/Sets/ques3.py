#Given a list of numbers, use a set to find and print only the duplicate values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
duplicates = set()
for i in numbers:
    if numbers.count(i) > 1:
        duplicates.add(i)   
print("Duplicate values:", duplicates)