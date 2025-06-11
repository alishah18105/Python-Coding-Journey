# Check if a number is a palindrome (e.g., 121).
num = 121
original_num = num
reverse_num = ""

while num > 0:
    digit = num % 10
    reverse_num = reverse_num + str(digit)
    num = num // 10

if original_num == int(reverse_num):
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")