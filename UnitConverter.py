from converter import convert_all
from validator import ValidationError, validate

OUTPUT_UNITS = ("feet", "yard", "meter")


def process(input_str: str) -> list[str]:
    unit, value = validate(input_str)
    results = convert_all(unit, value)
    lines: list[str] = []
    for name in ("feet", "yard"):
        if name in results:
            lines.append(f"{value} {unit} = {results[name]:.1f} {name}")
    return lines


def main() -> None:
    try:
        input_str = input("Insert value for converting (ex: meter:2.5): ")
        for line in process(input_str):
            print(line)
    except ValidationError as exc:
        print(exc)


if __name__ == "__main__":
    main()
