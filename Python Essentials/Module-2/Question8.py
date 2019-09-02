'''
Using given list L = ['a', 'b', 'c', 'd'], write a python code to create a dictionary of key:values
'''

# L is a list with elements in it
L = ['a','b','c','d']
dict_L = dict(enumerate(L,1))  # enumerate() function iterates through the list
L_Dict = {value:key for key,value in dict_L.items()}
print(f'The dictionary output is: {L_Dict}')