# UnitConverter_14 — 목표 아키텍처

> **spec 브랜치 산출물** — 구현은 `green` 브랜치에서 진행한다.

## 1. 패키지 구조

```
unit_converter/
├── domain/
│   ├── length_unit.py      # Protocol: name, to_meter_factor
│   ├── unit_registry.py    # 등록·조회 (OCP 핵심)
│   └── converter.py        # meter 기준 → 전 단위 변환 (SRP)
├── infrastructure/
│   └── config_loader.py    # JSON/YAML 로드 (EXT-01, P1)
├── app/
│   ├── input_parser.py     # "unit:value" 파싱·검증
│   └── output_formatter.py # table / json / csv (EXT-03, P1)
└── cli.py                  # CLI 진입점
```

## 2. 모듈 책임 (SRP — NFR-02)

| 모듈 | 책임 | 하지 않는 것 |
|------|------|--------------|
| `input_parser` | 문자열 → `(unit, value)` + 형식·음수 검증 | 변환 계산 |
| `unit_registry` | 단위 등록·조회·비율 보관 | 출력 포맷 |
| `converter` | meter 환산 → 전 단위 결과 dict | stdin/stdout |
| `output_formatter` | 결과 → 문자열/JSON/CSV | 비율 계산 |
| `config_loader` | 파일 → registry 초기화 | CLI 인자 파싱 |
| `cli` | 오케스트레이션 | 도메인 수식 직접 구현 |

## 3. OCP 확장 포인트 (NFR-01)

새 단위 추가 시 **기존 `converter.py` 수정 없이**:

1. `registry.register("inch", 0.0254)` — meter 대비 factor 등록, 또는
2. `units.json`에 `"inch": 39.3701` 한 줄 추가 (EXT-01)

```python
# converter.py — 단위별 분기 없음
def convert_all(value_in_meter: float, registry: UnitRegistry) -> dict[str, float]:
    return {
        name: value_in_meter * factor
        for name, factor in registry.all_factors().items()
    }
```

## 4. 데이터 흐름

```
stdin "meter:2.5"
    → input_parser.parse() → ("meter", 2.5)
    → registry.get_factor("meter") → 1.0
    → converter.to_meter(2.5, "meter", registry) → 2.5
    → converter.convert_all(2.5, registry) → {"meter": 2.5, "feet": 8.2021, ...}
    → output_formatter.format(results, fmt="table") → stdout
```

## 5. ECB (계층 의존 규칙)

| 계층 | import 허용 | import 금지 |
|------|-------------|-------------|
| `domain/` | domain 내부 | app, infrastructure, cli |
| `app/` | domain | cli (순환 방지) |
| `infrastructure/` | domain | app |
| `cli/` | domain, app, infrastructure | — |

## 6. 테스트 구조 (Dual-Track)

```
tests/
├── conftest.py           # 비율·입력 SSOT (로직 없음)
├── test_domain.py        # Track B — D-CNV-* (RED/GREEN)
├── test_boundary.py      # Track A — U-IN-*, U-OUT-* (RED/GREEN)
├── _approval.py          # Golden harness (green)
└── golden/               # Approval 기준 (green)
```

> **GREEN 단계:** 구현은 루트 `converter.py`, `validator.py`, `UnitConverter.py`(`process`/`main`)에 둔다.  
> `unit_converter/` 패키지는 **refactoring** 브랜치에서 이전한다.

## 7. 레거시 → 목표 매핑

| UnitConverter.py (시드) | 목표 모듈 |
|-------------------------|-----------|
| `split(':', 1)` + float | `input_parser.py` |
| `if unit == "meter"` 분기 | `unit_registry.py` + `converter.py` |
| `print(f"...")` | `output_formatter.py` + `cli.py` |
| `3.28084` 상수 | `conftest.py` SSOT → `registry` / `units.json` |
