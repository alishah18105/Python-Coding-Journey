#Given a tuple of (name, age) pairs, print only the names of people older than 18.

data = (("Ali", 20), ("Ibrahim", 17), ("Neha", 19), ("Ayesha", 18), ("Farheen", 21), ("Abdullah", 16))
for name, age in data:
    if age>18:
        print(name)
