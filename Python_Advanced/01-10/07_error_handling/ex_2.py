MIN_LEN_NAME = 4
VALID_DOMAINS = {".com", ".bg", ".net", ".org"}


#клас за грешка, когато името е по-кратко от 4 символа с функция за инициализация на класа със съобщение за грешка
#прочето за super() функцията: https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python и 
# https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods

class NameTooShortError(Exception):
    def __init__(self):
        super().__init__("Name must be more than 4 characters")

#клас за грешка, когато имейлът не съдържа символа @ с функция за инициализация на класа със съобщение за грешка
class MustContainAtSymbolError(Exception):
    def __init__(self):
        super().__init__("Email must contain @")

#клас за грешка, когато домейнът не е един от валидните с функция за инициализация на класа със съобщение за грешка
class InvalidDomainError(Exception):
    def __init__(self):
        super().__init__("Domain must be one of the following: .com, .bg, .org, .net")

#функция която вика горните функции за проверка на имейл адреса, която проверява дали името е по-кратко от 4 символа, дали съдържа символа @ и дали домейнът е валиден
def validator_email(email):
    if "@" not in email:
        raise MustContainAtSymbolError()
    
    name, domain = email.split("@") #трябва да има само един @, иначе ще се получи грешка при разделянето на имейла на име и домейн/Който го чете, моля за съвет как/
    if len(name) <= MIN_LEN_NAME:
        raise NameTooShortError()
    
    mail_domain = "." + domain.split(".")[-1] #добавяме точка пред домейна, за да го сравним с валидните домейни
    if mail_domain not in VALID_DOMAINS:
        raise InvalidDomainError()
    
    print("Email is Valid") #извеждаме съобщение, че имейлът е валиден, ако не е хвърлена грешка


while True:
    email = input()
    
    if email == "End":
        break

    try:
        validator_email(email) #викаме функцията за проверка на имейл адреса
    except Exception as e: #хващаме грешките и извеждаме съобщението за грешка
        print(e) 