'''
Write a for loop that prints all elements of a list and their position in the list.
'''
# a is a list with elements in it
a = [4,7,3,2,5,9]

for num in a:
    print(f'Number {num} is at {a.index(num)} in the list a.')
