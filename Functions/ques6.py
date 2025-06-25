#Write a function find_max(lst) that takes a list and returns the largest element.
def find_max(lst):
    if not lst:
        return None  # Return None if the list is empty
    max_lst  = lst[0]
    for num in lst:
        if num > max_lst:
            max_lst = num
    return max_lst

print(f"The largest element in the list is: {find_max([3, 1, 4, 1, 5, 9, 2, 6])}")