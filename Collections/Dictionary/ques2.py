#Store student names and marks, then find the highest
record = {
    "Ali": 85,
    "Neha": 92,
    "Ayesha": 78,
    "Mustafa": 68,
    "Farheen": 90,
    "Abdullah": 71
}

highest_marks = 0
highest_marks_holder = ""
for x,y in record.items():
    print(f"Name: {x}  Marks: {y}")
    if y>highest_marks:
        highest_marks = y
        highest_marks_holder = x

print(f"\n\nThe student with the highest marks is {highest_marks_holder} with {highest_marks} marks.")

