# Jose Rodriguez
# 7/19/26
# Module 9.2 Assignment

import requests

# Test the connection to the astronaut API
astronaut_url = "http://api.open-notify.org/astros.json"
response = requests.get(astronaut_url)

print("Astronaut API Connection Test")
print("Status Code:", response.status_code)

# Unformatted astronaut response
print()
print("Unformatted Astronaut Response:")
print(response.json())

# Formatted astronaut response
astronaut_data = response.json()

print()
print("Current Astronauts")
print("------------------")
print("Number of people in space:", astronaut_data["number"])

for person in astronaut_data["people"]:
    print(person["name"], "-", person["craft"])

# Test the connection to the Pokemon API
pokemon_url = "https://pokeapi.co/api/v2/generation/?limit=2"
response = requests.get(pokemon_url)

print()
print("Pokemon API Connection Test")
print("Status Code:", response.status_code)

# Unformatted Pokemon response
print()
print("Unformatted Pokemon Response:")
print(response.json())

# Formatted Pokemon response
pokemon_data = response.json()

print()
print("Pokemon Generations")
print("-------------------")
print("Total generations:", pokemon_data["count"])

for generation in pokemon_data["results"]:
    print("Generation:", generation["name"])
    print("URL:", generation["url"])