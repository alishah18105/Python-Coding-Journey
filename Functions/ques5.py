#Write a function factorial(n) that returns the factorial of a number using a loop.

def fact(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(1,num+1):
            fact *= i
        return fact

print(f"Factorial of 5 is: {fact(5)}")