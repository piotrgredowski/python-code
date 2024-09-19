import functools
import inspect
import pathlib
import time
import typing


def measure_time(func: typing.Callable[..., typing.Any]) -> typing.Callable[..., typing.Any]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} s")
        return result

    return wrapper


def measure_time_2(log_to_file: bool = False, log_file: str = "_execution_times.log"):  # noqa: FBT001, FBT002
    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time

            file_path = pathlib.Path(inspect.getfile(func)).resolve()
            line_number = inspect.getsourcelines(func)[1]

            message = f"Function '{func.__name__}' from file '{file_path}:{line_number}' took {execution_time:.4f} seconds to execute."  # noqa: E501

            if log_to_file:
                with open(log_file, "a") as f:
                    f.write(message + "\n")
            else:
                print(message)

            return result

        return wrapper

    return decorator


if __name__ == "__main__":

    @measure_time
    def slow_function():
        import time

        time.sleep(1)
        return "Done!"

    @measure_time_2(log_to_file=True, log_file="_slow_functions.txt")
    def another_slow_function(x: int, y: int) -> int:
        time.sleep(1.1)
        return x + y

    @measure_time_2()
    def my_function():
        time.sleep(1.2)
        return "My function"

    @measure_time_2(log_to_file=True)
    def my_function_2():
        time.sleep(0.6)
        return "My function 2"

    print(slow_function())
    print()
    print(another_slow_function(1, 2))
    print()
    print(my_function())
    print()
    print(my_function_2())
