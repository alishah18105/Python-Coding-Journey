# Write a program to display a/b where a and b are two integers. If b = 0 display infiniteby handling ZeroDivisionError.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a/b
    print("Result is:", result)

except ZeroDivisionError:
    print("Infinity")
