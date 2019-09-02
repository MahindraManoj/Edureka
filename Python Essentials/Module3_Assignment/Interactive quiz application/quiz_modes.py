'''
This is python code with three fucntions.
As per user input, it displays related information to user.
'''
# importing below modules(python codes) to let this program work. They have been written separately.
from easy_quiz_questions import easy_addition
from easy_quiz_questions import easy_multiplication
from easy_quiz_questions import easy_subtraction
from easy_quiz_questions import easy_division
from intermediate_quiz_questions import intermediate_addition
from intermediate_quiz_questions import intermediate_multiplication
from intermediate_quiz_questions import intermediate_subtraction
from intermediate_quiz_questions import intermediate_division
from hard_quiz_questions import hard_addition
from hard_quiz_questions import hard_multiplication
from hard_quiz_questions import hard_subtraction
from hard_quiz_questions import hard_division

def easy_mode():
    # this functions provides the easy level of questions to user since the user selected easy mode
    print("Difficulty level has been set to EASY.\nQuestions are categorized as follows:\nA. Addition\nB. Multuplication\nC. Subtraction\nD. Division.")
    try:
        # The try statement runs the below line
        question_type = input("Please choose from A, B, C, D: ")
    except ValueError:
        # If user answers other than A, B, C, D in easy level(error), below line will print
        print("Please choose only from A, B, C, D.")
    else:
        # If there's no error, then the else block of code will be executed
        if question_type == "A":
            easy_addition()
        elif question_type == "B":
            easy_multiplication()
        elif question_type == "C":
            easy_subtraction()
        elif question_type == "D":
            easy_division()

def intermediate_mode():
    # this functions provides the easy level of questions to user since the user selected intermediate mode
    print("Difficuly level has been set to INTERMEDIATE.\nQuestions are categorized as follows:\nA. Addition\nB. Multuplication\nC. Subtraction\nD. Division.")
    try:
        # The try statement runs the below line
        question_type = input("Please choose from A, B, C, D: ")
    except ValueError:
        # If user answers other than A, B, C, D in intermediate level(error), below line will print
        print("Please choose only from A, B, C, D.")
    else:
        # If there's no error, then the else block of code will be executed
        if question_type == "A":
            intermediate_addition()
        elif question_type == "B":
            intermediate_multiplication()
        elif question_type == "C":
            intermediate_subtraction()
        elif question_type == "D":
            intermediate_division()

def hard_mode():
    # this functions provides the easy level of questions to user since the user selected hard mode
    print("Difficuly level has been set to HARD.\nQuestions are categorized as follows:\nA. Addition\nB. Multuplication\nC. Subtraction\nD. Division.")
    try:
        # The try statement runs the line
        question_type = input("Please choose from A, B, C, D: ")
    except ValueError:
        # If user answers other than A, B, C, D in hard level(error), below line will print
        print("Please choose only from A, B, C, D.")
    else:
        # If there's no error, then the else block of code will be executed
        if question_type == "A":
            hard_addition()
        elif question_type == "B":
            hard_multiplication()
        elif question_type == "C":
            hard_subtraction()
        elif question_type == "D":
            hard_division()