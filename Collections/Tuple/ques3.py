#Create a tuple of names and check which names start with the letter "A".

names = ("Neha", "Ali", "Ibrahim", "Mustafa", "Ayesha", "Farheen", "Abdullah")
for x in names:
    if x.startswith("A"):
        print(f"{x} starts with 'A'")