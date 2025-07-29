class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(*args):
        if not args:
            raise ValueError("At least one number is required.")
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result /= num
        return result

    @staticmethod
    def subtract(*args):
        if not args:
            raise ValueError("At least one number is required.")
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
