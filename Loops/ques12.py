#Write a python program to greet all the person names stored in a list l1 and which starts with letter 'S'.
l1 = ["Ali", "Sara", "Hamza", "Saym", "Neha"]
for name in l1:
    if name.startswith('S'):
        print("Hello " + name)