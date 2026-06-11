from decimal import Decimal, ROUND_HALF_UP

METER_TO_FEET = Decimal("3.28084")
METER_TO_YARD = Decimal("1.09361")

OUTPUT_UNITS = ("feet", "yard", "meter")


def to_meter(unit: str, value: float) -> float:
    if unit == "meter":
        return value
    if unit == "feet":
        return float(Decimal(str(value)) / METER_TO_FEET)
    raise ValueError(f"Unknown unit: {unit}")


def _value_in_meters(unit: str, value: float) -> Decimal:
    if unit == "meter":
        return Decimal(str(value))
    if unit == "feet":
        return Decimal(str(value)) / METER_TO_FEET
    if unit == "yard":
        return Decimal(str(value)) / METER_TO_YARD
    raise ValueError(f"Unknown unit: {unit}")


def _quantize5(amount: Decimal) -> float:
    return float(amount.quantize(Decimal("0.00001"), rounding=ROUND_HALF_UP))


def convert_all(unit: str, value: float) -> dict[str, float]:
    meter = _value_in_meters(unit, value)
    results: dict[str, float] = {}
    for name in OUTPUT_UNITS:
        if name == unit:
            continue
        if name == "feet":
            converted = meter * METER_TO_FEET
        elif name == "yard":
            converted = meter * METER_TO_YARD
        else:
            converted = meter
        results[name] = _quantize5(converted)
    return results