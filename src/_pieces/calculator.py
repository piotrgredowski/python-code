class Calculator:
    """
    A simple calculator class.

    >>> calc = Calculator()
    >>> calc.add(2, 3)
    5
    >>> calc.subtract(5, 2)
    3
    >>> calc.multiply(4, 3)
    12
    >>> calc.divide(5, 0)  # Test division by zero exception
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero.
    >>> calc.divide(10, 2)
    5.0

    ### Testing parts we can't predict

    >>> import random
    >>> a, b = 1 + random.random(), 2
    >>> calc.add(a, b)
    3...

    ### Storytelling:

    1. Let's prepare some data to use with the calculator. Use for that decimals

    >>> import decimal
    >>> numbers = [decimal.Decimal("10.0"), decimal.Decimal("20.0")]

    2. Create a calculator instance

    >>> calc = Calculator()

    3. Modify numbers for some not very clear reason

    >>> numbers = [2 * n for n in numbers]

    3. Use the calculator to add the numbers together

    >>> float(calc.add(*numbers))
    60.0

    4. But remember that the calculator is not perfect

    >>> numbers = [1, 2, 3]
    >>> calc.add(*numbers)
    Traceback (most recent call last):
    ...
    TypeError: ...add() takes 3 positional arguments but 4 were given

    And that's how we can use `Calculator` and write some story with doctest at the same time
    """

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            err_msg = "Cannot divide by zero."
            raise ValueError(err_msg)
        return a / b
