# Correct the python code
# In python 3, raw_input() has been transformed to input()
# total (total amount or bill) is a variable which takes an integer input from the user
total = int(input('What is the total amount for your online shopping?'))
# country is a variable if user wants to ship the product(s) either to US or Canada, and takes input from  user
country = input('Shipping within the US or Canada?')
'''
   checks if the user's input is same as US or Canada, if Yes, then checks the total amount of the user
   and prints the respective shipping cost
'''
if country == "US":
    if total <= 50:
        print("Shipping Costs $6.00")
    elif total <= 100:
        print("Shipping Costs $9.00")
    elif total == 150:
        print("Shipping Costs $12.00")
    else:
        print("FREE")
elif country == "Canada":
    if total <= 50:
        print("Shipping Costs $8.00")
    elif total <= 100:
        print("Shipping Costs $12.00")
    elif total <= 150:
        print("Shipping Costs $15.00")
    else:
        print("FREE")
