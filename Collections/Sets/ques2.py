#From a sentence, extract all unique words using a set.
sentence = "This is a sample sentence with some sample words and some repeated words"
unique_words = set()

for x in sentence.split():
    unique_words.add(x)
print("Unique words in the sentence:", unique_words)