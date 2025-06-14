#Count character frequency in a string using a dictionary.
word = "hello world"
frequency = {}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i] =1
print("Character frequency in the string is:", frequency)