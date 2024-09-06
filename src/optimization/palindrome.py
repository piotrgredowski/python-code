"""
"We should forget about small efficiencies, say about 97% of the time: premature
optimization is the root of all evil. Yet we should not pass up our opportunities
in that critical 3%"

https://en.wikipedia.org/wiki/Program_optimization

Premature optimization can lead to several issues:

- Increased Complexity: Introducing optimizations too early can make the code more complex and harder to understand, maintain, and debug.
- Wasted Resources: Time and effort spent on optimizing parts of the code that do not significantly impact performance could be better used elsewhere.
- Reduced Flexibility: Early optimizations can create rigid structures that are difficult to modify or extend, limiting the ability to adapt to future requirements or improvements.
"""

"""
A palindrome is a word, number, phrase, or other sequence of symbols that reads the
same backwards as forwards, such as madam or racecar.

https://en.wikipedia.org/wiki/Palindrome
"""


def is_palindrome__simple(s):
    """
    When `is_palindrome__simple` is good enough?
        - when we want to check not *a lot* of strings
        - when the strings are not *too long*, I mean 1_000_000
        - when after profiling we see that the function is not a bottleneck and other parts of the code
        are taking *much* (100x) more time
    """
    return s == s[::-1]


def is_palindrome__optimized_v1(s):
    """
    When `is_palindrome__optimized` is required?
        - when we want to check *a lot* of strings
        - when the strings are *too long*, I mean 1_000_000_000
        - when after profiling we see that the function is a bottleneck and other parts of the code
    """
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


def is_palindrome__optimized_v2(string):
    """
    When `is_palindrome__optimized` is required?
        - when we want to check *a lot* of strings
        - when the strings are *too long*, I mean 1_000_000_000
        - when after profiling we see that the function is a bottleneck and other parts of the code
    """
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True


# def measure_them(string_formula: str, number: int = 1_000):

#     import timeit

#     s = eval(string_formula)
#     print(f"String formula: {string_formula}")

#     simple_time = timeit.timeit(lambda: is_palindrome__simple(s), number=number)
#     optimized_time_v1 = timeit.timeit(lambda: is_palindrome__optimized_v1(s), number=number)
#     optimized_time_v2 = timeit.timeit(lambda: is_palindrome__optimized_v2(s), number=number)

#     padding = 30

#     print(f"> Simple:".ljust(padding), f"{simple_time} s")
#     print(f"> Optimized v1:".ljust(padding), f"{optimized_time_v1} s")
#     print(f"> Optimized v2:".ljust(padding), f"{optimized_time_v2} s")

#     print(f"> Simple/Optimized:".ljust(padding), f"{simple_time / optimized_time_v2:.2f}")
#     print()


if __name__ == "__main__":
    for _ in range(1000):
        is_palindrome__simple(eval('"ab" * 10**6'))
    # measure_them('"ab" * 10**6', number=1_000)
    # measure_them('"racecar"', number=10_000)
    # measure_them('"saippuakivikauppias"', number=10_000)
