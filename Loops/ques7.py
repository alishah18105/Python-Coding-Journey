#Reverse a number (e.g., 12345 → 54321).

num = 12345
reverse = ""
print(f"Reverse Of Number {num} is: ", end = "")
while num!=0 :
    last = num % 10
    last = str(last)
    reverse += last
    num = num // 10
print(reverse)