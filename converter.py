from decimal import Decimal

METER_TO_FEET = Decimal("3.28084")
METER_TO_YARD = Decimal("1.09361")

def to_meter(unit: str, value: float) -> float:
    if unit == "meter":
        return value
    if unit == "feet":
        return float(Decimal(str(value)) / METER_TO_FEET)
    raise ValueError(f"Unknown unit: {unit}")
