#Grade calculator based on marks:
#90+ → A One
#80–89 → A
#70–79 → B
#60–69 → C 
#50–59 → D
#Below 50 → Fail

total_marks = 500
obtain_marks = 0

for i in range(1,6):
    marks = float(input(f"Enter marks for subject {i}: "))
    obtain_marks+= marks

percentage = (obtain_marks / total_marks) * 100

if percentage>= 90:
    grade = "A One"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print(f"Total Marks: {total_marks}")
print(f"Obtained Marks: {obtain_marks}")    
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
