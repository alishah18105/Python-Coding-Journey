#Write a function is_prime(n) that returns True if n is a prime number.

def is_prime(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    
print(f"The Number 5 is a prime number: {is_prime(5)}")
print(f"The Number 12 is a prime number: {is_prime(12)}")


        