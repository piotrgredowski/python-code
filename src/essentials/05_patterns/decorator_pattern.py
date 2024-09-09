import functools
import typing


def make_bold(func: typing.Callable[..., str]) -> typing.Callable[..., str]:
    def wrapper(*args, **kwargs):
        return f"\033[1m{func(*args, **kwargs)}\033[0m"
    return wrapper


def make_cyan(func: typing.Callable[..., str]) -> typing.Callable[..., str]:
    # https://docs.python.org/3/library/functools.html#functools.wraps
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"\033[96m{func(*args, **kwargs)}\033[0m"
    return wrapper

if __name__ == "__main__":

    def greet_raw(name):
        return f"Hello, {name}!"

    @make_bold
    def greet_with_decorator(name):
        return f"Hello, {name}!"


    greet_bold = make_bold(greet_raw)
    greet_cyan = make_cyan(greet_raw)

    text = "Hello, World!"

    print(text)
    print(greet_raw(text))
    print(greet_bold(text))
    print(greet_with_decorator(text))
    print(greet_cyan(text))


    print(greet_bold.__name__)
    print(greet_cyan.__name__)

    pass
