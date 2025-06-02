#Вариант при който не викам функции, а просто проверявам условията в цикъл(не съм убден дали е по-добре само с if-else или с try-except)
class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

def common_passwords(password, special_characters):
    only_letters = password.isalpha()
    only_digits = password.isdigit()
    only_special = all(char in special_characters for char in password)
    return only_letters or only_digits or only_special


SPECIAL_CHARACTERS = {"@", "*", "&", "%"}


while True:
    password = input()

    if password == "Done":
        break

    try:
        if len(password) < 8:
            raise PasswordTooShortError("Password must contain at least 8 characters")
        
        if common_passwords(password, SPECIAL_CHARACTERS):
            raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
        
        if not any(char in SPECIAL_CHARACTERS for char in password):
            raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
        
        if " " in password:
            raise PasswordContainsSpacesError("Password must not contain empty spaces")
        
        print("Password is valid")

    except (PasswordTooShortError, PasswordTooCommonError, PasswordNoSpecialCharactersError, PasswordContainsSpacesError) as e:
        print(e)