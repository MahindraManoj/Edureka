'''
Write a python program to reverse/inverse key:value
'''
Dict = {'a':1,'b':2,'c':3}
inversed_Dict = {value:key  for key,value in Dict.items()}
print(f'The inverted dictionary is: {inversed_Dict}')