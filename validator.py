class ValidationError(ValueError):
    pass

FORMAT_ERROR = "Invalid format. Use unit:value (ex: meter:2.5)"
NEGATIVE_ERROR = "Negative value not allowed"
KNOWN_UNITS = ("meter", "feet", "yard")


def validate(raw: str) -> tuple[str, float]:
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
    if unit not in KNOWN_UNITS:
        raise ValidationError(f"Unknown unit: {unit}")
    return unit, value