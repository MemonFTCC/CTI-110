#Shayan Memon
#3/2/2025
#P2HW1
# Budget project revised


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


print(f"Intial Budget: $ {int(budget):.2f}")


print(f"Fuel: $ {int(gas):.2f}")


print(f"Accommodation:$ {int(accommodation):.2f}")


print(f"Food: $ {int(food):.2f}")


print("--------------------------")


print(f"Remaining Balance: $ {int(remaining):.2f}")










