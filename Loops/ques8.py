#Count digits in a number.
num = 54321
count = 0
print(f"Number of digits in {num} are: ", end = "")
while num !=0:
    num = num // 10
    count+=1
print(count)