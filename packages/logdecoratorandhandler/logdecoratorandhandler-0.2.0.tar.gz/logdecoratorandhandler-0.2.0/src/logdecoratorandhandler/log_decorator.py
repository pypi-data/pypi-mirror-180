"""
LogDecorator for logging errors of try-except handling.
"""
from functools import wraps
from time import time

from .log_handler import Logger


class LogDecorator:
    """
    Class decorator for logs.
    """
    def __init__(self, message):
        self.logger = Logger()
        self.message = message

    def __call__(self, fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            try:
                self.logger.log(fn.__name__, self.message)
                return fn(*args, **kwargs)
            except Exception as ex:
                self.logger.log(fn.__name__, f'ERROR - {ex}')
                raise ex

        return decorated


class TimeDecorator:
    """
    Class decorator for logging performance.
    """

    def __call__(self, fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            start = time()
            result = fn(*args, **kwargs)
            end = time()
            time_difference = round(end - start, 4)
            print(f'{fn.__name__} - time used: {time_difference} seconds')
            return result

        return decorated

#
# def exception_handler(log: Logger):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):  # type: ignore
#             try:
#                 response = func(*args, **kwargs)
#             except es_exception.SerializationError:
#                 log.critical("serialization error!")
#                 raise
#             except es_exception.ConnectionError:
#                 log.critical("connection error!", extra={"update_func_name": func.__name__})
#                 raise
#             except es_exception.RequestError:
#                 log.critical("request error!")
#                 raise
#             except Exception as err:
#                 log.critical(f"uncaught error! :{err}")
#                 raise
#
#             return response
#         return wrapper
#     return decorator
