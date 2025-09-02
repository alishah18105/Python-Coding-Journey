# Store the multiplicaton tables generated in Problem 3 in a file named Tables- txt

with open("Tables.txt","a") as f:
    num = int(input("Enter a number: "))
    multiplication = [i*num for i in range(1,11)]
    print(multiplication)
    f.write(f"Multiplication table of {num} is:\n {str(multiplication)}\n\n")