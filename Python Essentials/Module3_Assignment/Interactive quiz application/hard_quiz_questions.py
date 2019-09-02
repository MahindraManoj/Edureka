def hard_addition():
    # this function asks user to answer the questions related to 'addition' with difficuly level set to hard
    print('Question-1')
    try:
        answer1 = int(input("What's 3474569 + 454579? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 3929148:
            print("Congratulations! Your answer is correct.")
        else:
            print('Your answer is wrong!')

    print('Question-2\nNote: This question has decimal output.')
    try:
        answer2 = float(input("What's 4312458.27 + 4559.45? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 4317017.72:
            print("Congratulations! Your answer is correct.")
            print('Thank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, please run the program to attempt the quiz again. Thank you!')

def hard_multiplication():
    # this function asks user to answer the questions related to 'multiplication' with difficuly level set to hard
    print("Question-1")
    try:
        answer1 = int(input("What's 121 * 123? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 14883:
            print("Congratulations! Your answer is correct.\n")
        else:
            print('Your answer is wrong!')

    print('Question-2\nNote: This question expects decimal output.')
    try:
        answer2 = float(input("What's 29*243*479.45? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 3795805.65:
            print("Congratulations! Your answer is correct.")
            print('Thank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, attempt the quiz again. Thank you!')

def hard_subtraction():
    # this function asks user to answer the questions related to 'subtraction' with difficuly level set to hard
    print("Question-1\nThis question expects decimal output")
    try:
        answer1 = float(input("What's 51356.71- 1173.56? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 50183.15:
            print("Congratulations! Your answer is correct.")
        else:
            print('Your answer is wrong!')

    print('Question-2')
    try:
        answer2 = int(input("What's 7891567 - 12347 - 456796? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 7422424:
            print("Congratulations! Your answer is correct.")
            print('Thank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, attempt the quiz again. Thank you!')

def hard_division():
    # this function asks user to answer the questions related to 'division' with difficuly level set to hard
    print("Question-1")
    try:
        answer1 = int(input("What's 10534/23? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer1 == 458:
            print("Congratulations! Your answer is correct.")
        else:
            print('Your answer is wrong!')

    print('Question-2')
    try:
        answer2 = int(input("What's (591426/87)/8? "))
    except ValueError:
        print("A value should be entered. Run the program again to attempt the quiz.")
    else:
        if answer2 == 3399:
            print("Congratulations! Your answer is correct.")
            print('Thank you for participating in quiz.')
        else:
            print('Your answer is wrong! If you want, attempt the quiz again. Thank you!')