#Check if one set is a subset of another. Print a message accordingly.

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3}

if set_2.issubset(set_1):
    print(f"{set_2} is a subset of{set_1}") 
else:
    print(f"{set_2} is not a subset of {set_1}")