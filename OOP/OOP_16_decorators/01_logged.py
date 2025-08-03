def logged(function):
    def wrapper(*args):
        func_name = function.__name__
        result = function(*args)
        return f"you called {func_name}{args}\nit returned {result}"
    return wrapper