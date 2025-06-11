#Determine if a triangle is valid with 3 sides.

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")