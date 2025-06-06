class Temperature:
    """Conversion between temperature units."""

    def c_to_f(value: float = 0) -> float:
        return (value * 9/5) + 32

    def f_to_c(value: float = 32) -> float:
        return (value - 32) * 5/9

    def c_to_k(value: float = 0) -> float:
        return value + 273.15

    def k_to_c(value: float = 273.15) -> float:
        return value - 273.15

    def f_to_k(value: float = 32) -> float:
        return Temperature.c_to_k(Temperature.f_to_c(value))

    def k_to_f(value: float = 273.15) -> float:
        return Temperature.c_to_f(Temperature.k_to_c(value))