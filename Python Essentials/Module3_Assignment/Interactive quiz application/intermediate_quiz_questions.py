def intermediate_addition():
    # this function asks user to answer the questions related to 'addition' with difficuly level set to intermediate
    print('Question-1')
    try:
        answer1 = int(input("What's 34 + 44489? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 44523:
            print("Congratulations! Your answer is correct.")
        else:
            print('Your answer is wrong!')
    print('Question-2')
    try:
        answer2 = int(input("What's 35 + 455? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 490:
            print("Congratulations! Your answer is correct.")
            print('Thank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, please run the program to attempt the quiz again. Thank you!')

def intermediate_multiplication():
    # this function asks user to answer the questions related to 'multiplication' with difficuly level set to intermediate
    print("Question-1")
    try:
        answer1 = int(input("What's 12 * 12? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 144:
            print("Congratulations! Your answer is correct.\n")
        else:
            print('Your answer is wrong!')
    print('Question-2')
    try:
        answer2 = int(input("What's 20 multiplied by 25? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 500:
            print("Congratulations! Your answer is correct.")
            print('Thank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, attempt the quiz again. Thank you!')

def intermediate_subtraction():
    # this function asks user to answer the questions related to 'subtraction' with difficuly level set to intermediate
    print("Question-1")
    try:
        answer1 = int(input("What's 513 - 117? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 396:
            print("Congratulations! Your answer is correct.")
        else:
            print('Your answer is wrong!')
    print('Question-2')
    try:
        answer2 = int(input("What's 7891 - 1234? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 6657:
            print("Congratulations! Your answer is correct.")
            print('Thank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, attempt the quiz again. Thank you!')

def intermediate_division():
    # this function asks user to answer the questions related to 'division' with difficuly level set to intermediate
    print("Question-1")
    try:
        answer1 = int(input("What's 117/3? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 37:
            print("Congratulations! Your answer is correct.")
        else:
            print('Your answer is wrong!')
    print('Question-2')
    try:
        answer2 = int(input("What's 623/8? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 79:
            print("Congratulations! Your answer is correct.")
            print('Thank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, attempt the quiz again. Thank you!')