class Distance:
    """Conversion between distance units."""

    def km_to_m(value: float = 1) -> float:
        return value * 1000

    def m_to_km(value: float = 1) -> float:
        return value / 1000

    def m_to_mi(value: float = 1) -> float:
        return value / 1609.344

    def mi_to_m(value: float = 1) -> float:
        return value * 1609.344

    def km_to_mi(value: float = 1) -> float:
        return Distance.m_to_mi(Distance.km_to_m(value))

    def mi_to_km(value: float = 1) -> float:
        return Distance.m_to_km(Distance.mi_to_m(value))