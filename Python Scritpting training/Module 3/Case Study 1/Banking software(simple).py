'''
Python program for bank system with features like cash withdrawal, cash credit and PIN change.
According to user inout, the code should display the required output
'''

def cash_withdraw():
    debit_pin = int(input("Please enter your debit card PIN (4-digit) to continue: "))
    # assuming user knows the default PIN that bank gives to account holders.
    if debit_pin == 1234:
        debit_amount = input("Please enter the amount that you want to WITHDRAW: ")
        print(f'{debit_amount} has been debited from your account. Thank you for banking with us.')
    else:
        print(f'The PIN you entered is incorrect. Please check and try again!')


def cash_deposit():
    debit_pin = int(input("Please enter your debit card PIN (4-digit) to continue: "))
    if debit_pin == 1234:
        credit_amount = input("Please enter the amount you want to DEPOSIT: ")
        print(f'{credit_amount} has been credited to your account. Thank you for banking with us.')
    else:
        print(f'The PIN you entered is incorrect. Please check and try again!')


def password_change():
    print('Follow the instructions to change your debit PIN.')
    debit_pin = int(input('Please enter your old PIN to contiune: '))
    new_pin = int(input("Please enter new PIN: "))
    if new_pin != debit_pin:
        print(f'Your PIN has been changed. Your new PIN is {new_pin}. Thank you for banking with us.')
    else:
        print('Your new PIN should not be same as old PIN.')


def user_selection_option():
    print('Welcome to XYZ bank. Select from the options below.')
    print("1. Cash Withdrawal\n2. Deposit cash\n3. PIN change")
    select = None
    while select not in (1, 2, 3):
        select = int(input("Enter your choice: "))
        if select == 1:
            cash_withdraw()
        elif select == 2:
            cash_deposit()

        elif select == 3:
            password_change()
        else:
            print('Sorry! Please enter your choice from the available ones.')


user_selection_option()