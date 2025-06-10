class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if email.split("@")[1].endswith(".com"):
        print("Email is valid")
        pass
    elif email.split("@")[1].endswith(".bg"):
        print("Email is valid")
        pass
    elif email.split("@")[1].endswith(".org"):
        print("Email is valid")
        pass
    elif email.split("@")[1].endswith(".net"):
        print("Email is valid")
        pass
    else:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")



