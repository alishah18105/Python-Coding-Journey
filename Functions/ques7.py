#Write a function count_vowels(s) that returns the number of vowels in a string
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

print(f"Number of vowels in 'Hello World' is: {count_vowels('Hello World')}")