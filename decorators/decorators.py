from functools import wraps


def logged_arguments(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(filename, 'a') as file:
                argument_value = [f"{func.name}:{arg}= {value} " for arg, value in kwargs.items()]
                argument_str = '\n'.join(argument_value)
                file.write(argument_str + '\n')
                return func(*args, **kwargs)

        return wrapper

    return decorator


def logged_exception(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                with open(filename, 'a') as file:
                    log_message = f"Method:{func.name}, Exception: {type(e).name}"
                    file.write(log_message + '/n')
                    raise

        return wrapper

    return decorator