# A list contains the multiplication table of 7. Write a program to convert it to a vertical string of Same numbers
#7
#14
num = 7
table = [ str(num*i) for i in range(1,11)]
print("\n".join(table))

