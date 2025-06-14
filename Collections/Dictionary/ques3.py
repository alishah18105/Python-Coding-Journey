#Merge two dictionaries
students = {
    "Ali": 85,
    "Neha": 92, 
    "Ayesha": 78,
}
students2 ={
    "Mustafa": 68,
    "Farheen": 90,
    "Abdullah": 71
}

students.update(students2)
print(f"Merged Dictionary:  {students}")