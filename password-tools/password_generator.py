#COMP1888 (2025-2026) Programming for Data Science
#CW1 Portfolio, Deadline 12/11/2025
#Student ID 001260070
# Portfolio Question 1b

import string
import random


def generate_secure_password(min_length, upper=True, lower=True, numbers=True, specials=True):

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    upper_char = string.ascii_uppercase
    lower_char = string.ascii_lowercase


    chrs = ""
    if upper:
        chrs += upper_char
    if lower:
        chrs += lower_char
    if numbers:
        chrs += digits
    if specials:
        chrs += special


    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_ch = random.choice(chrs)
        password += new_ch

        if new_ch in digits:
            has_number = True
        elif new_ch in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if specials:
            meets_criteria = meets_criteria and has_special

    return password



lngth = int(input("Your minimum password length: "))
uppercase = input("Use uppercase letters (YES/NO)? ").lower() == "yes"
lowercase = input("Use lowercase letters (YES/NO)? ").lower() == "yes"
num = input("Use numbers (YES/NO)? ").lower() == "yes"
spec = input("Have special characters (YES/NO)? ").lower() == "yes"


password = generate_secure_password(lngth, uppercase, lowercase, num, spec)
print("Your generated secure password is: ", password)