def type_check(type_to_check):
    def decorator(function):
        def wrapper(arg):
            if isinstance(arg, type_to_check):
                return function(arg)
            return "Bad Type"
        return wrapper
    return decorator