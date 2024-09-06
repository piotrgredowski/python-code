def _add(a, b):
    return a + b

def _check_if_positive(a):
    ...

def add_two_numbers(a, b):
    _check_if_positive(a)
    return _add(a, b)


class Calculator:
    class _Adder:
        def add(self, a, b):
            return a + b
    class Subtracter:
        def subtract(self, a, b):
            return a - b

    class Config:
        ...

Calculator._Adder()
Calculator.Config()


quarter = 0.25

plot_size_multiplier = [0.5, 0.25, 0.25]

plot_size_multiplier[0]

plot_size_multiplier[1]

standard_plot_width = 1000

plot_2_size = standard_plot_width * plot_size_multiplier[1]
plot_2_size = 1000 * 0.25
plot_2_size = 250

#

time_for_timeout = 60 * 60 * 24 # 24 hours

timeout(86400)
