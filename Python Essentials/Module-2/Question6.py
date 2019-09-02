'''
Write a python program which should create a dictionary of key:values
Use: Dictionary comprehension
'''
# lists to represent keys and values
keys = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
# Forming dictionary using dict comprehension
Dict = {k:v for (k,v) in zip(keys, values)}
print(Dict)
