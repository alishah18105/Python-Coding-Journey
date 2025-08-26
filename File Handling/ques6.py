#Write a program to check if the word "python" is present in the file log.txt or not. If present, print the line number.
with open("log.txt","r") as f:
    content = f.readlines()
line_no = 1
for line in content:
    if "python" in line:
        print(f"Yes, python is present at Line no: {line_no}")
        break
    line_no += 1
else:
        print("No,python is not present")