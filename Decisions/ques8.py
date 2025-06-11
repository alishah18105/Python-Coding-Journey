#Classify a triangle as Equilateral, Isosceles, or Scalene.
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 and side2 == side3 and side3== side1:
    print("The triangle is Equilateral.")
elif side1 != side2 and side2 != side3 and side3 != side1:
    print("The triangle is Scalene.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is Isosceles.")