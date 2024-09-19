vol, height, width = 200, 10, 20
Number = int | float


def calculate_depth(vol: Number, height: Number, width: Number) -> Number:
    return vol / (height * width)


print(
    f"Having volume {vol} and height {height} and width {width} we get depth {calculate_depth(vol, height, width)}",  # noqa: E501
)
