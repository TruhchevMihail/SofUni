#Отново както при втора задача с функцията super() извикваме конструктора на базовия клас Exception, за да предадем съобщението за грешка. Според мен е по-добре да се използва super() функцията, защото така можем да добавим и други параметри към конструктора на базовия клас, ако е необходимо в бъдеще.
class MoneyNotEnoughError(Exception):
    def __init__(self):
        super().__init__("Insufficient funds for the requested transaction")


class PINCodeError(Exception):
    def __init__(self):
        super().__init__("Invalid PIN code")


class UnderageTransactionError(Exception):
    def __init__(self):
        super().__init__("You must be 18 years or older to perform online transactions")


class MoneyIsNegativeError(Exception):
    def __init__(self):
        super().__init__("The amount of money cannot be a negative number")


pin, balance, age = [int(x) for x in input().split(", ")]

while True:

    input_data = input().split("#")

    if input_data[0] == "End":
        break
    
    try:
        if input_data[0] == "Send Money":

            money = int(input_data[1])
            pin_code = int(input_data[2])

            if money > balance:
                raise MoneyNotEnoughError()
        
            if pin_code != pin:
                raise PINCodeError()
            
            if age < 18:
                raise UnderageTransactionError()

            else:
                balance -= money
                print(f"Successfully sent {money:.2f} money to a friend")
                print(f"There is {balance:.2f} money left in the bank account")

        elif input_data[0] == "Receive Money":
           
            money = int(input_data[1])

            if money < 0:
                raise MoneyIsNegativeError()
            
            invested_money = money / 2

            print(f"{invested_money:.2f} money went straight into the bank account")
           

    except (MoneyNotEnoughError, PINCodeError, UnderageTransactionError, MoneyIsNegativeError) as e:
        print(e)

