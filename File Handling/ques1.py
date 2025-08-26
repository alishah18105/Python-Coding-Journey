# Write a program to read the text from a given file poems txt and find out whether it contains the word twinkle

with open('poem.txt', 'r') as f:
    content = f.read()
    if 'twinkle' in content:
        print("The word 'twinkle' is present in the file.\n\n")
    else:
        print("The word 'twinkle' is not present in the file.\n\n")
