import re
from typing import Any

import pytest


def is_valid_email(email: str) -> bool:
    """Check if the given string is a valid email address.

    Args:
        email: The email address to validate.

    Returns:
        True if the email is valid, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> is_valid_email("test@example.com")
        True
        >>> is_valid_email("invalid-email")
        False
    """
    if not isinstance(email, str):
        raise TypeError("Input must be a string")

    # Regular expression for validating an email
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


# Unit tests
@pytest.mark.parametrize(
    "email,expected",
    [
        ("test@example.com", True),
        ("invalid-email", False),
        ("another.test@domain.co", True),
        ("bad@domain", False),
        ("@missingusername.com", False),
        ("missingatsign.com", False),
        ("missingdomain@.com", False),
        ("missingdot@domaincom", False),
        ("valid.email+alias@gmail.com", True),
        ("email@sub.domain.com", True),
    ],
)
def test_is_valid_email(email: str, expected: bool) -> None:
    assert is_valid_email(email) == expected


if __name__ == "__main__":
    pytest.main()
