from unit_converter.domain.registry import DEFAULT_REGISTRY, UnitRegistry

FORMAT_ERROR = "Invalid format. Use unit:value (ex: meter:2.5)"
NEGATIVE_ERROR = "Negative value not allowed"


class ValidationError(ValueError):
    pass


def validate(raw: str, registry: UnitRegistry = DEFAULT_REGISTRY) -> tuple[str, float]:
    if not raw:
        raise ValidationError(FORMAT_ERROR)
    if ":" not in raw:
        raise ValidationError(FORMAT_ERROR)
    unit, value_str = raw.split(":", 1)
    if not unit or not value_str:
        raise ValidationError(FORMAT_ERROR)
    try:
        value = float(value_str)
    except ValueError as exc:
        raise ValidationError(f"Invalid number: {value_str}") from exc
    if value < 0:
        raise ValidationError(NEGATIVE_ERROR)
    if unit not in registry.known_units():
        raise ValidationError(f"Unknown unit: {unit}")
    return unit, value
