#A file contains the word " Donkey" multiple times. You need to write a program that 
# replaces this word with ###### by updating the Same file.
words = ["donkey", "village"]

with open("donkey_story.txt", "r",  encoding="cp1252") as f: 
    content = f.read()
    for word in words:
        content = content.replace(word, "#" * len(word))
with open("donkey_story.txt", "w") as f:
    f.write(content) 