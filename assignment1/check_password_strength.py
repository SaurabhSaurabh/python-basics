# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential.
#  Create a Python script to check the strength of the password. 

# ●       Implement a Python function called check_password_strength that takes a password string as input.

# ●       The function should check the password against the following criteria:

# ○       Minimum length: The password should be at least 8 characters long.

# ○       Contains both uppercase and lowercase letters.

# ○       Contains at least one digit (0-9).

# ○       Contains at least one special character (e.g., !, @, #, $, %).

# ●       The function should return a boolean value indicating whether the password meets the criteria.

# ●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

# ●       Provide appropriate feedback to the user based on the strength of the password.  


def minimum_length(password):
    return len(password) >= 8

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False
    
def has_uppercase_and_lowercase(password):
    has_upper = False
    has_lower = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
    return has_upper and has_lower

def has_special_character(password):
    special_characters = "!@#$%"
    for char in password:
        if char in special_characters:
            return True
    return False

def password_feedback(password):
    print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, at least one digit, and at least one special character (!, @, #, $, %).")
    print("Is Minimum Length :", minimum_length(password))
    print("Is Digit:", has_digit(password))
    print("Is Uppercase and Lowercase:", has_uppercase_and_lowercase(password))
    print("Is Special Character:", has_special_character(password))

def check_password_strength(password):
    if (minimum_length(password) and 
            has_digit(password) and 
            has_uppercase_and_lowercase(password) and 
            has_special_character(password)):
        print("Strong Password")
    else:
        print("Weak Password")
        password_feedback(password)
        

user_password = input("Enter your password: ")
check_password_strength(user_password)


