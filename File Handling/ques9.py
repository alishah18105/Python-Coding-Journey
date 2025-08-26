#Write a program to check whether the contents of two files are identical or not.

with open("this.txt","r") as f:
    content1 = f.read()

with open("this_copy.txt","r") as f:
    content2 = f.read()

if content1 == content2:
    print("The contents are identical.")

else:
    print("The contents are not identical.")