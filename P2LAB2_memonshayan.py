# Shayan Memon
# 2/23/2025
#P2LAB2
#work with dictionaries




# Create a dictionary named cars that represents cars and their mph
cars = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}

# Create a list of the keys in the dictionary
keys = cars.keys()

# View the contents of the keys list
print(keys)

# Get one of the keys from the user
user_input = input("Enter a vehicle to see its mpg: ")

# With user_input holding the key, we want back the value
print(f"The {user_input} gets {cars[user_input]} mpg.")

# Get number of miles to drive from the user
miles = float(input(f"How many miles will you drive the {user_input}? "))

# Calculate amount of gas needed to drive the chosen car the given number of miles
num_gallons = miles/cars[user_input]

print(f"{num_gallons:.2f} gallon(s) are needed to drive the {user_input} {miles} miles.")
