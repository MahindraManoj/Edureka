def easy_addition():
    # this function asks user to answer the questions related to 'addition' with difficuly level set to easy
    print('Question-1')
    try:
        answer1 = int(input("What's the sum of 3 and 4? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 7:
            print("Congratulations! Your answer is correct.")
        else:
            print('Your answer is wrong!')
    print('Question-2')
    try:
        answer2 = int(input("What's the sum of 2 and 20? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 22:
            print("Congratulations! Your answer is correct.")
            print('Thank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, please run the program to attempt the quiz again. Thank you!')

def easy_multiplication():
    # this function asks user to answer the questions related to 'multiplication' with difficuly level set to easy
    print("Question-1")
    try:
        answer1 = int(input("What's 3 multiplied by 4? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 12:
            print("Congratulations! Your answer is correct.\n")
        else:
            print('Your answer is wrong!')
    print('Question-2')
    try:
        answer2 = int(input("What's 2 multiplied by 20? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 40:
            print("Congratulations! Your answer is correct.")
            print('Thank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, attempt the quiz again. Thank you!')

def easy_subtraction():
    # this function asks user to answer the questions related to 'subtraction' with difficuly level set to easy
    print("Question-1")
    try:
        answer1 = int(input("What's the value when 3 is subtracted from 5? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 2:
            print("Congratulations! Your answer is correct.")
        else:
            print('Your answer is wrong!')
    print('Question-2')
    try:
        answer2 = int(input("What's the value when 11 is subtracted from 17? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 6:
            print("Congratulations! Your answer is correct.")
            print('Thank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, attempt the quiz again. Thank you!')

def easy_division():
    # this function asks user to answer the questions related to 'division' with difficuly level set to easy
    print("Question-1")
    try:
        answer1 = int(input("What's 5 divided by 5? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 1:
            print("Congratulations! Your answer is correct.")
        else:
            print('Your answer is wrong!')

    print('Question-2')
    try:
        answer2 = int(input("What's 60 divided by 5? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 12:
            print('Congratulations! Your answer is correct.\nThank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, attempt the quiz again. Thank you!')