#Write a function reverse_string(s) that returns the reverse of the string s.

def reverse_string(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word    

print(f"Reversed string of 'Hello World' is: {reverse_string('Hello World')}")