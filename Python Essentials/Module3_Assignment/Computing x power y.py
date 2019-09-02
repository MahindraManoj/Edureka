'''
Python code to compute x raised to power n through a recursive function.
'''
def compute_xpower_n_recursive():
    # Function that computes 'x' raised to the power 'n' recursively
    try:
        # try section executes and takes input from user
        x = int(input("Please enter the base value: "))
    except ValueError:
        '''
        The except section will be executed if no value is given by the user i.e.
        when there's an error after try section has been executed
        '''
        print("You didn't enter any value for the base.")
    else:
        # if the value of x is given by user(when there's no error), below block of code will be executed
        if x > 0:
            try:
                n = int(input("Please enter the exponential value: "))
            except ValueError:
                print("You didn't enter any value for the exponent variable 'n'.")
            else:
                if n == 0:
                    return f'The result is: 1'
                elif n == 1:
                    return f'The result is: {x}'
                elif n > 1 or n < 0:
                    # below is the recursive formula
                    return f'The result is: {x*(x**(n-1))}'
        elif x == 0:
            try:
                n = int(input("Please enter the exponential value: "))
            except ValueError:
                print("You didn't enter any value for the exponent variable 'n'.")
            else:
                if n == 0:
                    return f'The result is 1.'
                elif n > 0:
                    return f'The result is 0.'
                else:
                    return f"The result is 'undefined'."
        else:
            print('Please make sure that x value should be greater than 0.')
#calling the function to be executed
compute_xpower_n_recursive()