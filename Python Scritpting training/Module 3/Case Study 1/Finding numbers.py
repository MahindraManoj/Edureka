'''
Finding numbers between 2000 and 3200 (inclusive of them)
which are divisible of 7 and not multiples of 5
'''

def finding_numbers():
    output = []
    for i in range(2000,3201):
        if i%7 == 0 and i%5 != 0:
            output.append(str(i))
            result = ",".join(output)

    print(result)

finding_numbers()