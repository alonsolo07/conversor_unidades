class Velocity:
    """Conversion between speed units."""

    def kmh_to_mps(value: float = 1) -> float:
        return value / 3.6

    def mps_to_kmh(value: float = 1) -> float:
        return value * 3.6

    def mph_to_mps(value: float = 1) -> float:
        return value * 0.44704

    def mps_to_mph(value: float = 1) -> float:
        return value / 0.44704

    def kmh_to_mph(value: float = 1) -> float:
        return Velocity.mps_to_mph(Velocity.kmh_to_mps(value))

    def mph_to_kmh(value: float = 1) -> float:
        return Velocity.mps_to_kmh(Velocity.mph_to_mps(value))