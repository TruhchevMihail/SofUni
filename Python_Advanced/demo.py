# Вариант при който не викам функции, а просто проверявам условията в цикъл
class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


while True:
    password = input()

    if password == "Done":
        break


    if len(password) < 8:
        raise PasswordTooShortError("Password must be at least 8 characters long")

    if password.lower() in ["password", "12345678", "qwerty"]:
        raise PasswordTooCommonError("Password is too common")

    if not any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for char in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least one special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain spaces")

    print("Password is valid")

