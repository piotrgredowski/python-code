# 1. Non-descriptive function names
def func():
    pass


# 2. Overly abbreviated function names
def calc():
    pass


# 3. Misleading function names
def get_data():
    pass  # But it actually updates the database


# 4. CamelCase function names (not recommended in Python)
def getData():  # noqa: N802
    pass


def set_a_number():
    pass


# 1. Non-descriptive class names
class MyClass:
    pass


# 2. Overly abbreviated class names
class C:
    pass


# 3. Misleading class names
class Manager:
    pass  # But it actually represents a single employee


# 4. CamelCase class names (not recommended in Python)
class MyFirstClass:
    pass


# 1. Single-letter variable names
x = 10

diameter = 10

# 2. Overly abbreviated variable names
temp = 25

# 3. Misleading variable names
num = "John"  # When it should represent an integer

data = {}

# 4. Using reserved keywords as variable names
for_ = 5  # 'for' is a reserved keyword in Python

type_ = 123

__a = 1

## Other bad examples
flag = False  # It's not clear what 'flag' is indicating.
use_database = True  # It's indicating action, not a state.
red = True
x = 172800  # It's not clear what 'x' represents.

## Good examples
should_use_database = True
is_red = True
two_days = 60 * 60 * 24 * 2  # 2 days in seconds
timeout = two_days


class PositiveCalculator:
    def _validate_number(self, number):
        if number < 0:
            raise ValueError("Number must be positive")  # noqa: EM101, TRY003

    def add(self, a, b):
        self._validate_number(a)
        self._validate_number(b)
        return a + b

    def subtract(self, a, b):
        return a - b


# 1.2.3
# 2.0.0
