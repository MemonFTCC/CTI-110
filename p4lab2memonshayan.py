# shayan memon 
# 3/19/2025
# p4lab2
# using a for loop inside a while loop to print math


# create the variable to control while loop

run_again = "yes"

# while loop that controls the whole program 
while run_again != "no":
    # get int form user
    user_num = int(input("Enter an integer:"))
    if user_num < 0: 
       print("Negative numbers are not allowed")
    else: # user_num is 0 or greater
        for i in range (1,13): 
          print(F"{user_num} * {i} = {user_num * i } ")
        run_again = input("Would you like to run again? 'yes'/'no'")

# While loop ends here
print("Program has ended......")

