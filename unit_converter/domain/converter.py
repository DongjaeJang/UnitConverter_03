from decimal import ROUND_HALF_UP, Decimal

from unit_converter.domain.registry import (
    DEFAULT_REGISTRY,
    METER_TO_FEET,
    METER_TO_YARD,
    UnitRegistry,
)

_QUANT = Decimal("0.00001")


def _quantize5(amount: Decimal) -> float:
    return float(amount.quantize(_QUANT, rounding=ROUND_HALF_UP))


def _value_in_meters(unit: str, value: float, registry: UnitRegistry) -> Decimal:
    factor = registry.to_meter_factor(unit)
    return Decimal(str(value)) / factor


def to_meter(unit: str, value: float, registry: UnitRegistry = DEFAULT_REGISTRY) -> float:
    if unit == "meter":
        return value
    if unit == "feet":
        return float(_value_in_meters(unit, value, registry))
    raise ValueError(f"Unknown unit: {unit}")


def convert_all(
    unit: str,
    value: float,
    registry: UnitRegistry = DEFAULT_REGISTRY,
) -> dict[str, float]:
    meter = _value_in_meters(unit, value, registry)
    results: dict[str, float] = {}
    for name in registry.output_units():
        if name == unit:
            continue
        if name == "meter":
            converted = meter
        elif name == "feet":
            converted = meter * METER_TO_FEET
        else:
            converted = meter * METER_TO_YARD
        results[name] = _quantize5(converted)
    return results
