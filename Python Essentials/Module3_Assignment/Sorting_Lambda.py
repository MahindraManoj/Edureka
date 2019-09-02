'''
Sort the list using lambda function mylist = [["john", 1, "a"], ["larry", 0, "b"]]. Sort the list by second item 1 and 0
'''
mylist = [["John",1,"a"],["larry",0,"b"]]
# Lambda function takes the values of 1 and o which are first element in the given list
print(sorted(mylist, key = lambda i: i[1]))


'''
Sort the list using operator.itemgetter function mylist = [["john", 1, "a"], ["larry", 0, "b"]]. 
Sort the list by second item 1 and 0
'''
from operator import itemgetter

mylist = [["John",1,"a"],["larry",0,"b"]]
# Lambda function takes the values of 1 and o which are first element in the given list and assigns to itemgetter
print(sorted(mylist, key = itemgetter(1)))
