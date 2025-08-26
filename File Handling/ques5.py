#Write a program to check if the word "python" is present in the file log.txt or not.
with open("log.txt","r") as f:
    content = f.read()
    if content .__contains__("python"):
        print("yes")
    else:
        print("no")