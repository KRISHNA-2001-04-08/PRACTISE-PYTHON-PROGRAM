password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()-_+=<>?/"

if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Password is VALID")
    else:
        print("Password is INVALID")
else:
    print("Password must be at least 8 characters long")
