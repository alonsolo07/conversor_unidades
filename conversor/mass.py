class Mass:
    """Conversion between mass units."""

    def kg_to_lb(value: float = 1) -> float:
        return value * 2.20462

    def lb_to_kg(value: float = 1) -> float:
        return value / 2.20462

    def kg_to_g(value: float = 1) -> float:
        return value * 1000

    def g_to_kg(value: float = 1) -> float:
        return value / 1000

    def lb_to_g(value: float = 1) -> float:
        return Mass.kg_to_g(Mass.lb_to_kg(value))

    def g_to_lb(value: float = 1) -> float:
        return Mass.kg_to_lb(Mass.g_to_kg(value))