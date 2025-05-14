
# Shayan Memon
# 3/16/2025 
# P3HW1

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
module_1 = float(input('Enter grade for Module 1: '))
module_2 = float(input('Enter grade for Module 2: '))
module_3 = float(input('Enter grade for Module 3: '))
module_4 = float(input('Enter grade for Module 4: '))
module_5 = float(input('Enter grade for Module 5: '))
module_6 = float(input('Enter grade for Module 6: '))

# Create an empty list
grades= []

# add grades entered to a list

grades.append(module_1)
grades.append(module_2)           
grades.append(module_3) 
grades.append(module_4) 
grades.append(module_5) 
grades.append(module_6) 





# TO DO: determine lowest, highest , sum and average for grades
lowest = min(grades)
highest = max(grades)
total = sum(grades)
avg = total / len(grades)

# Print results 
print("----------Results------------")
print(f'lowest grade: {lowest}')
print(f'Highest Grade: {highest}')
print(f'sum of grades: {total}')
print(f'Average: {avg:.2f}')





# determine letter grade for average
if avg >= 90:
    print('your grade is: A')
else:
    if avg >= 80:
        print('Your Grade is: B')
    else:
        if avg >= 70:
            print('Your Grade is: C')
        else:
            if avg >= 60:
                print('Your grade is: D')
            else:
                if avg >= 50:
                    print('Your grade is: F')
                else:
                    print('Grade below 50: F')



