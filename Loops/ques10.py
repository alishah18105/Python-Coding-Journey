#Print all prime numbers between 1 and 100.
prime = True

for i in range(2, 101):
    for j in range(2, i+1):
        if i == j:
            prime = True
            break
        elif i %j == 0:
            prime = False
            break
    if prime:
        print(i, end=" ")
    prime = False  