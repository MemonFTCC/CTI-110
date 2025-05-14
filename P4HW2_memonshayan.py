#Shayan Memon
#4/6/2025
#p4hw2
#employees pay





#totals
total_overtime = 0
total_reg_pay = 0
total_gross = 0
num_employees = 0

#get employee name
name = input("enter employees name or done to terminate: ")
while name.lower() != 'done':    
    
    
#get employee pay info
    pay_rate = float(input("enter employees pay rate: $"))
    hours = float(input("enter number of hours worked: "))
    
#calculate hours and pay
    if hours <= 40:
        reg_hours = hours
        ovt_hours = 0
    else:
        reg_hours = 40
        ovt_hours = hours - 40
        
    reg_pay = reg_hours * pay_rate
    ovt_pay = ovt_hours * (pay_rate * 1.5)
    gross_pay = reg_pay + ovt_pay
    
#totals 2
    total_overtime += ovt_pay
    total_reg_pay += reg_pay
    total_gross += gross_pay
    num_employees += 1
    
# display employee results
    print("\nemployee pay summary for:", name)
    print(f"hours worked: {hours:.1f}")
    print(f"pay rate: ${pay_rate:.2f}")
    print(f"overtime hours: {ovt_hours:.1f}")
    print(f"overtime pay: ${ovt_pay:.2f}")
    print(f"regular hours pay: ${reg_pay:.2f}")
    print(f"gross pay: ${gross_pay:.2f}")
    
#next employee name
    name = input("\nenter employees name or done to terminate: ")

#display final summary
print("\ntotal number of employees entered:", num_employees)
print(f"total amount paid for overtime: ${total_overtime:.2f}")
print(f"total amount paid for regular hours: ${total_reg_pay:.2f}")
print(f"total amount paid in gross: ${total_gross:.2f}")