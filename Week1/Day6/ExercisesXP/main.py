# 1
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

print({key: number for (key, number) in zip(keys, values)})

# 2
# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
#     Under 3 years old: Free
#     3 to 12 years old: $10
#     Over 12 years old: $15

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

total = 0
for name, age in family.items():
    if age < 3:
        print(f"{name}: free")
    elif age <= 12:
        print(f"{name}: $10")
        total += 10
    else:
        print(f"{name}: $15")
        total += 15
print(f"Total cost: ${total}")

# 3
# Create and manipulate a dictionary that contains information about the Zara brand.
#   Brand Information:
#
#      name: Zara
#      creation_date: 1975
#      creator_name: Amancio Ortega Gaona
#      type_of_clothes: men, women, children, home
#      international_competitors: Gap, H&M, Benetton
#      number_stores: 7000
#      major_color:
#          France: blue,
#          Spain: red,
#          US: pink, green
#
#
# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
#     Change the value of number_stores to 2.
#     Print a sentence describing Zara’s clients using the type_of_clothes key.
#     Add a new key country_creation with the value Spain.
#     Check if international_competitors exists and, if so, add “Desigual” to the list.
#     Delete the creation_date key.
#     Print the last item in international_competitors.
#     Print the major colors in the US.
#     Print the number of keys in the dictionary.
#     Print all keys of the dictionary.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": {"men", "women", "children", "home"},
    "international_competitors": {"Gap", "H&M", "Benetton"},
    "number_stores": 7000,
    "major_color": {"France": {"blue"}, "Spain": {"red"}, "US": {"pink", "green"}},
}

brand["number_stores"] = 2
print(f"Zara's clients buy {', '.join(brand['type_of_clothes'])} clothes")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].add("Desigual")
brand.pop("creation_date")

print(list(brand["international_competitors"])[-1])

print(brand["major_color"]["US"])
print(len(brand))
print(list(brand.keys()))

# 4
# Instructions
#
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
#
#
# Character List:
#
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#
#
# Expected Results:
#
# 1. Create a dictionary that maps characters to their indices:
#
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#
#
# 2. Create a dictionary that maps indices to characters:
#
# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#
#
# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
#
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
user_to_index = {name: num for (num, name) in enumerate(users)}
index_to_user = {num: name for (num, name) in enumerate(users)}
sorted_user_to_index = {name: num for (num, name) in enumerate(sorted(users))}
