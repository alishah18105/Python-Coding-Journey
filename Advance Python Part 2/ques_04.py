#Write a program to filter a list of numbers which are divsible by 5

def divisible_by_5(num):
    if num%5==0:
        return True
    return False

lst = [10,23,45,67,89,90,34,22,15,78,55]
result = list(filter(divisible_by_5,lst))
print(result)
