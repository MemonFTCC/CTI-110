#Shayan Memon
#2/28/2025
#P1HW2
# Budget project


print("This program calculates and displays travel expenses")


# Get an budget from the user
budget = float(input("Enter budget: "))

# Get user to enter travel destination
destination = input(" Enter your travel destination: ")

# Get amount from user for gas
gas = float(input("How much do you think you will spend on gas?  "))


# Get ammount from user for accomodation
accommodation = float(input("Approximately, how much will you need for accommodation/hotel?  "))

# Ask user for an ammount for food
food = float(input("Last, how much do you need for food?  "))


# Adding Money
total = gas + accommodation + food

# Subtracting Money
remaining = budget - total


print("--------------- Travel Expenses-----------")

print(f"Location: {destination}")


print(f"Intial Budget: {int(budget)}")


print(f"Fuel: {int(gas)}")


print(f"Accommodation: {int(accommodation)}")


print(f"Food: {int(food)}")

print(f"Remaining Balance: {int(remaining)}")










