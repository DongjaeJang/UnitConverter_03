class ValidationError(ValueError):
    pass

FORMAT_ERROR = "Invalid format. Use unit:value (ex: meter:2.5)"
NEGATIVE_ERROR = "Negative value not allowed"
KNOWN_UNITS = ("meter", "feet", "yard")


def validate(raw: str) -> tuple[str, float]:
    if not raw:
        raise ValidationError(FORMAT_ERROR)
    raise ValidationError("not implemented")