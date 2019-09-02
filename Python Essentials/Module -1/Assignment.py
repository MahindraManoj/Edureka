import re

'''
Python code to print the number of 'a' and 'o', 'L' and 'N'
in the sentence "Discover, Learning, with, Edureka"
'''

input_string = "Discover, Learning, with, Edureka"
# count() is a built-in string method
a = input_string.count("a")
o = input_string.count("o")
L = input_string.count("L")
N = input_string.count("N")
print(f'Number of "a" in the given string is: {a}')
print(f'Number of "o" in the given string is: {o}')
print(f'Number of "L" in the given string is: {L}')
print(f'Number of "N" in the given string is: {N}')

'''
Python code to remove the following from www.edureka.in
a. remove all W's before and after .edureka
b. remove all lowercase letters before and after .edureka
c. Remove all printable characters
'''

mystring = "www.edureka.in"
# using built-in string strip() method to get the trimmed version
a = mystring.strip("w")
print(a)
#converting the string in to list by splitting usin '.'
list_mystring = list(mystring.split('.'))
# checks if the list[0] and list[2] are in lower case and removes it
b = re.sub('[a-z]','',list_mystring[0]) + '.' + list_mystring[1] + '.' + re.sub('[a-z]','',list_mystring[2])
print(b)
print(re.sub('[a-z]','',mystring))

'''
Python code to identify the type of numbers
a. 0X7AE
b. 3+4j
c. -01234
d. 3.14e-2
'''

a = 0X7AE
b = 3+4j
c = -1234
d = float(3.14e-2)
print(f'The type of a is: {type(a)}')
print(f'The type of b is: {type(b)}')
print(f'The type of c is: {type(c)}')
print(f'The type of d is: {type(d)}')

'''
Write a program for string formatting operator % which should include
the following conversions:
a.Character
b.Signed decimal integer
c.Octal integer
d.Hexadecimal integer (UPPERcase letters)
e.Floating point real number
f.Exponential notation (with lowercase 'e')
'''

