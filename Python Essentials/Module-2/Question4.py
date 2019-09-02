'''
Write a python program to prompt the user for hours and rate per hour to compute gross pay
'''
# hours_worked is a variable that takes float input from user
hours_worked = float(input("Please enter the number of hours you worked: "))
# pay_rate is a variable that takes float input from user
pay_rate = float(input("Enter the rate per hour: "))
# calculation of pay (gross_pay)
pay = hours_worked * pay_rate
print("Your gross pay is: $%.2f" %pay)



