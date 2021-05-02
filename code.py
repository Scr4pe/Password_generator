# Import Modules
import string
import random

# Variables
length_of_password = 0
kind_of_password = 0
Start_text = "\n\nWelcome to the Password generator\nWe would advice you to use 14 to 22 Characters"
Options_text = "\nChoose which kind of password you want to create:\n1. Letters, Punctuations, Numbers\n2. Hexadecimal\n3. Letters, Punctuation\n4. Numbers, Punctuation\n5. Letters, Numbers\n"
length_of_password_text = "\nChoose the length of your Password"
User_input_invalid = "The user selected an invalid value\n"
user_selected = ""
password_length_short ="\nYour Password is to short, below 14 characters"
password_length_long = "\nYour Password is to long, above 22 characters\nThis Application doesn't support so long characters\n"
password_length_change = "Do you want to change the length below?\n[Y/N] "
password_length_remain = "Password length remains as you selected\n"
password = ""
password_length_new = "\nSelect new Password length"
output_after_completion = "\nThank you for using our service\n"

# Functions

# This function is for Dealing with invalid input
def invalid_value():
    print(User_input_invalid)
    invalid_value.user_selected = input("Do you want to retry?\n[Y/N]")

# This function is for checking if the length of the password is valid
def password_length():
    password_length.length_of_password = int(input())
    # If your password is shorter then 14 letters/numbers/symbols 
    if (password_length.length_of_password < 14):
        # Ask the user if a longer password is a better idea
        print(password_length_short)
        user_selected = input(password_length_change)
        # True if you want to change the Password length
        if (user_selected == "Y" or user_selected == "y"):
            print(password_length_new)
            password_length()
        # True if you want to continue with length
        elif(user_selected == "N" or user_selected == "n"):
            print(password_length_remain)
        # True if input is invalid
        else:
            print(User_input_invalid)
            password_length()
    # If your password is longer then 22 letters/numbers/symbols
    if (password_length.length_of_password > 22):
        # Ask the user if a shorter password is a better idea
        print(password_length_long)
        user_selected = input(password_length_change)
        if (user_selected == "Y" or user_selected == "y"):
            print(password_length_new)
            password_length()
        elif (user_selected == "N" or user_selected == "n"):
            print(password_length_remain)
        else:
            print(User_input_invalid)
            password_length()

# This function creates the password
def password_kind_input():
    # Print instructions for the user
    print(Options_text)
    password_kind_input.Kind_of_password = input()

    # If selection is letters, punctuations, numbers
    if (password_kind_input.Kind_of_password == "1"):
        # Generate a password in which there are 
        # no repeating letters (lowercase or uppercase) and numbers and punctations
        # And cutted it to the selected length 
        password_kind_input.password = "".join(random.sample((string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits),password_length.length_of_password))

    # If selection is hexade
    elif (password_kind_input.Kind_of_password == "2"):
        # Generate a password in which there are
        # no repeating numbers and punctations
        # And cutted it to the selected length
        password_kind_input.password = "".join(random.sample(string.hexdigits,password_length.length_of_password))

    # If selection is letters, punctuations
    elif (password_kind_input.Kind_of_password == "3"):
        # Generate a password in which there are
        # no repeating numbers and punctations
        # And cutted it to the selected length
        password_kind_input.password = "".join(random.sample((string.ascii_uppercase + string.ascii_lowercase + string.punctuation),password_length.length_of_password))

    # If selection is letters, numbers
    elif (password_kind_input.Kind_of_password == "4"):
        # Generate a password in which there are
        # no repeating letters (lowercase or uppercase) and numbers
        # And cutted it to the selected length
        password_kind_input.password = "".join(random.sample((string.digits + string.ascii_lowercase + string.ascii_uppercase),password_length.length_of_password))

    # If selection is numbers, punctuations
    elif (password_kind_input.Kind_of_password == "5"):
        # Generate a password in which there are
        # no repeating numbers and punctations
        # And cutted it to the selected length
        password_kind_input.password = "".join(random.sample((string.digits + string.punctuation),password_length.length_of_password))

    # If the user selection is an invalid value
    else:
        # Start invalid function
        invalid_value()
        if (invalid_value.user_selected == "Y" or invalid_value.user_selected == "y"):
            password_kind_input()
        elif (invalid_value.user_selected == "N" or invalid_value.user_selected == "n"):
            print()
        # If User selected invalid value
        else:
            invalid_value()

# This functon starts the script
def init():
    print(Start_text)
    print(length_of_password_text)
    password_length()
    password_length.length_of_password
    password_kind_input()
    password_kind_input.password
    print("\n" + password_kind_input.password)
    print(output_after_completion)

# Init
init()

