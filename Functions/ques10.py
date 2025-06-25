#Write a function calculator(a, b, op) that takes two numbers and an operator ('+', '-', '*', '/') and returns the result.

def calculator(num1,num2,operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Invalid Operator"
    
print(f"Addition of 5 and 3: {calculator(5, 3, '+')}")
print(f"Subtraction of 5 and 3: {calculator(5, 3, '-')}")
print(f"Multiplication of 5 and 3: {calculator(5, 3 , '*')}")
print(f"Division of 5 and 3: {calculator(5, 3, '/'):.2f}")
print(f"Modulus of 5 and 3: {calculator(5, 3, '%')}")
print(f"Invalid operation: {calculator(5, 3, '^')}")