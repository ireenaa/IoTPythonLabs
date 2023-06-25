import inspect
import logging
from functools import wraps


class ThereAreNoPeopleOnBoard(Exception):
    pass


def logged(exception, mode):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ThereAreNoPeopleOnBoard as err:
                frame = inspect.currentframe().f_back
                filename = frame.f_code.co_filename
                line_number = frame.f_lineno
                class_name = frame.f_locals.get('self', None).__class__.__name__
                message = f"Exception {exception.__name__} was raised in {class_name}.{func.__name__}\n " \
                          f"At line {line_number}\n In file {filename}\n With message: {err}"
                logging.basicConfig(filename='exception.log', level=logging.ERROR, format='%(asctime)s\n%(message)s')
                logging.error(message)
                if mode == "file":
                    logging.basicConfig(filename='exception_ship', level=logging.ERROR)
                    logging.error(message)
                elif mode == "console":
                    logging.basicConfig(level=logging.ERROR)
                    logging.error(message)

        return wrapper

    return decorator
