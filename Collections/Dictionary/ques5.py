#Sort a dictionary by values.
students = {
    "Ali": 85,
    "Neha": 92,
    "Ayesha": 78,
    "Mustafa": 68,
    "Farheen": 90,
    "Abdullah": 71
}

sorted_students = dict(sorted(students.items(), key=lambda item: item[0])) #To Sort By Value: item[1] & tTo Sort in Descending Order reverse = True
print("Sorted Dictionary by Values (Descending):\n\n")
for name, marks in sorted_students.items():
    print(f"Name: {name},\t\t\t Marks: {marks}")

