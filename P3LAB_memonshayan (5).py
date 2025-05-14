# Shayan Memon
# 3/10/2025 
# P3Lab 

# Use if/else statemnts to determine coin combination 


# Get a float from user and convert to intger 

input_money= float(input("Enter the amount of money as a float: $"))

money= int(input_money * 100)

(money)

# Calculate number of whole dollars
num_dollars = money //100
(f"Num dollars: {num_dollars}")


# Remove the dollars from the amount of money
money= money - (num_dollars*100)

(f"The remaining money is:{money}")


# Calculate number of whole quarters 
num_quarters= money// 25
(f"num quaters: {num_quarters}")

#remove the quaters from the amount of money
money= money - (num_quarters* 25)

(f"the remaining money is{money}")

# Calulate number of whole dimes
num_dimes = money //10 

(f" the remianing money is {num_dimes}")


# calulate number of whole nickles 
num_nickeles= money //5
(f'num nickles:{num_nickeles}')


# remove the dollars from the amount of money
money= money -(num_nickeles*5)

(f"The reminaing money id {money}")

num_pennies = money






# DISPLAY coins/dollars needed only if they are used
# Ensure all grammer is correct

print()
print()
print()

print(f"{input_money:.2f}")

# if no change is due, display "no change"

if input_money <= 0.00:
   print("No change")


   if num_dollars ==0 and num_quarters == 0 and num_dimes == 0 and num_dimes== 0:
    ("no change")


# Display dollars  
if num_dollars > 0: 
    if num_dollars==1:
     (f"{num_dollars}Dollar")
    else:
     (f"{num_dollars}Dollars")




# Display Quarters
if num_quarters > 0:
    if num_quarters == 1: 
         (f"{num_quarters} Quarter")

else: 
     (f"{num_quarters} Quarters")



# Display Quarters 
if num_quarters > 0:
    if num_quarters == 1:
         (f"{num_quarters} Quarter")

else: 
    (f"{num_quarters} Quarters")


    # Display nickles 
    if num_nickeles > 0: 
     if num_nickeles == 1:
       (f"{num_nickeles} Nickles")
     else: 
      (f"{num_nickeles} Nickles")




    #Display pennies 

if num_pennies > 0:
  if num_pennies == 1:
    (f"{num_pennies} penny")
  else: 
    (f"{num_pennies} pennies")



    


               
