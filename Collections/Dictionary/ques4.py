#Check if a key exists in a dictionary.
books_store = {
    "Python Basics": 25,
    "Data Science with Python": 30,
    "Machine Learning": 40,
    "Deep Learning": 50,
    "Artificial Intelligence": 60
    }
book = input("Enter the book name to check if it exists: ")



if book in books_store.keys():
    print(f"The book '{book}' is available in the store.")
else:
    print(f"The book '{book}' is not available in the store.")