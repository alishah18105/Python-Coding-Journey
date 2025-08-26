#Write a program to copy the contents of a file this.txt to another file this_copy.txt

with open("this.txt","r") as f:
    content = f.read()
with open("this_copy.txt","w") as f:
    f.write(content)