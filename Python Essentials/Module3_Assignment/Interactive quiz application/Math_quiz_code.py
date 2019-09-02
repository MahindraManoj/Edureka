'''
This is python code for attempting a quiz related to Addtion, Multiplication, Subtraction and Divison.
The quiz has three difficulty levels: Easy, Intermediate and Hard.
Based on user's choice questions will be provided and the user needs to attempt the quiz.
'''
# importing below module to run the main program since the code has been written in modules
from quiz_modes import easy_mode
from quiz_modes import intermediate_mode
from quiz_modes import hard_mode
A = True
print(
    "Hello user! This is a quiz related to math.\nIt has three leves of difficulty. User selects only one from three.")
# While the condition is True, below code will execute
while A:
    try:
        # Try statement executes the below block of code to check if there's an error
        user_level = input(
            "Please choose the level of difficulty from the options: A. Easy\tB. Intermediate\tC. Hard\n")
        # Manually raises a Value error when there's an empty string
        if not user_level:
            raise ValueError('Empty string')
    except ValueError:
        # When there's no error in try section, below line will be printed
        print("Please enter only from A, B, C.")
    else:
        # When there's no error
        if user_level == "A":
            easy_mode()
        elif user_level == "B":
            intermediate_mode()
        elif user_level == "C":
            hard_mode()
        further_attempt = None
        while further_attempt not in ("Yes", "No"):
            further_attempt = input("Do you wish to re-attempt the quiz(Yes/No)? ")
            if further_attempt == "Yes":
                continue
            elif further_attempt == "No":
                print("Thank you!")
                A = False
                break
            else:
                print("Please enter 'Yes' to proceed or 'No' to quit the re-attempt.")
