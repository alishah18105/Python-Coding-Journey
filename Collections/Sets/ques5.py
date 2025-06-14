#Create a set of cities visited during a tour. Let the user input a city name and check if it was visited or not.

cities_visited = {"New York", "Los Angeles", "Chicago", "Houston", "Phoenix"}
city = input("Enter a city name to check if it was visited: ")

if city in cities_visited:
    print(f"{city} was visited during the tour.")
else:
    print(f"{city} was not visited during the tour.")