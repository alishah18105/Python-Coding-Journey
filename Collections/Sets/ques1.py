#Create two sets of student roll numbers (Set A for math class, Set B for science class) and find:
#Students who are in both classes.
#Students who are only in the math class.

set_a = {101, 102, 103, 104, 105}  # Math class roll numbers
set_b = {104, 105, 106, 107, 108}  # Science class roll numbers

both_classes = set_a.intersection(set_b)
only_mathClass = set_a.difference(set_b)

print("Students in both classes:", both_classes)
print("Students only in the math class:", only_mathClass)