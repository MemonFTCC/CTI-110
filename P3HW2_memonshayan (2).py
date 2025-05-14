#Shayan Memon
#3/16/2025
#P3HW2
#employees pay


# get employee Information
name =input("enter employees Name: ")
hours = float(input("enter number of hours Worked: "))
payrate = float(input("enter employees pay Rate: "))

# Calculate hours
if hours <= 40:
    regularhours = hours
    overtimehours = 0
else:
    regularhours = 40
    overtimehours = hours - 40

# Calculate pay
regularpay = regularhours * payrate
overtime_pay = overtimehours * (payrate * 1.5)
grosspay = regularpay + overtimehours

# Display results
print(f'employees Name: {name}')
print(f'hours worked: {hours:.1f}')
print(f'pay rate: {payrate:.2f}')
print(f'Overtime hours: {overtimehours:.1f}')
print(f'overtime pay: {overtime_pay:.2f}')
print(f'regularhours Pay: ${regularpay:.2f}')
print(f'gross pay: ${grosspay:.2f}')
