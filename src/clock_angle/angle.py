def split_hours_and_minutes(string: str):
    """
    Split a string in the format "HH:MM" into a list of integers (HH, MM)

    >>> split_hours_and_minutes("12:34")
    [12, 34]
    >>> split_hours_and_minutes("00:00")
    [0, 0]
    """

    return [int(s) for s in string.split(":")]


def hours_hand(hour: int, minutes: int):
    """
    Calculate the angle of the hour hand

    >>> hours_hand(12, 0)
    0.0
    >>> hours_hand(3, 0)
    90.0
    >>> hours_hand(6, 0)
    180.0
    >>> hours_hand(9, 0)
    270.0
    >>> hours_hand(12, 15)
    7.5
    """
    base = (hour % 12) * (360 // 12)
    correction = float((minutes / 60) * (360 // 12))
    return base + correction


def minutes_hand(minutes: int) -> float:
    """
    Calculate the angle of the minute hand

    >>> minutes_hand(0)
    0.0
    >>> minutes_hand(15)
    90.0
    >>> minutes_hand(30)
    180.0
    >>> minutes_hand(45)
    270.0
    """
    return float(minutes * (360 // 60))


def between(time: str):
    """
    Calculate the angle between the hour and minute hands of a clock

    >>> between("12:00")
    0.0
    >>> between("3:00")
    90.0
    >>> between("6:00")
    180.0
    >>> between("9:00")
    270.0
    >>> between("12:15")
    82.5
    >>> between("12:30")
    165.0
    >>> between("00:01")
    5.5
    """
    hour, minutes = split_hours_and_minutes(time)

    if hour not in range(0, 24) or minutes not in range(0, 60):
        message = f"Invalid time: {time}"
        raise ValueError(message)

    return abs(hours_hand(hour, minutes) - minutes_hand(minutes))
