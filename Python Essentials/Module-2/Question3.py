'''
Python code to take the input from  user in terms of Fahrenheit and print the temperature in terms of Celsius
'''

#Fahrenheit is a variable that takes integer input from user
Fahrenheit = int(input("Please enter a Fahrenheit value: "))
# Formula to convert Fahrenheit to celsius
Celsius = float((Fahrenheit - 32) * (5/9))
print("Celsius conversion of Fahrenheit is %.1f" %Celsius)
