from decimal import Decimal

METER_TO_FEET = Decimal("3.28084")
METER_TO_YARD = Decimal("1.09361")

OUTPUT_UNITS = ("feet", "yard", "meter")


class UnitRegistry:
    """OCP: new units register without changing converter logic."""

    def __init__(self) -> None:
        self._to_meter_factor: dict[str, Decimal] = {
            "meter": Decimal("1"),
            "feet": METER_TO_FEET,
            "yard": METER_TO_YARD,
        }

    def known_units(self) -> frozenset[str]:
        return frozenset(self._to_meter_factor)

    def to_meter_factor(self, unit: str) -> Decimal:
        if unit not in self._to_meter_factor:
            raise ValueError(f"Unknown unit: {unit}")
        return self._to_meter_factor[unit]

    def output_units(self) -> tuple[str, ...]:
        return OUTPUT_UNITS


DEFAULT_REGISTRY = UnitRegistry()
