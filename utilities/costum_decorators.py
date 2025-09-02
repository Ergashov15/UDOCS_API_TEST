import pytest
import  functools

def safe_exception_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            test_name = func.__name__
            pytest.fail(f"Unhandled exception: {test_name}")

    return wrapper

