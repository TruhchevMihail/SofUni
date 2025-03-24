def password_lenght(password):
    if 6 <= len(password) <= 10:
        return True
    return False

def password_letters_and_digits(password):
    for char in password:
        if not char.isalnum():
            return False
    return True

def password_digits(password):
    digits_count = 0
    for char in password:
        if char.isdigit():
            digits_count += 1
    if digits_count >= 2:
        return True
    return False

def password_validator(password):
    errors = []
    if not password_lenght(password):
        errors.append("Password must be between 6 and 10 characters")
    if not password_letters_and_digits(password):
        errors.append("Password must consist only of letters and digits")
    if not password_digits(password):
        errors.append("Password must have at least 2 digits")
    if errors:
        return "\n".join(errors)
    return "Password is valid"

password_input = input()

print(password_validator(password_input))

