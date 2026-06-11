---
name: unit-converter-tdd
description: UnitConverter_03 TDD·ARRR 절차. RED 설계·스켈레톤, GREEN 최소 구현, Golden Master, REFACTOR 시 참조.
---

# UnitConverter TDD Skill

## SSOT

- 요구사항: `docs/PRD.md`
- 아키텍처: `docs/ARCHITECTURE.md`
- 비율 상수: `tests/conftest.py`

## ARRR 1사이클

```
/red-test-plan   → Ask, 설계표 (docs/PRD §8 참고)
/red-skeleton    → Agent, tests/ 스켈레톤, pytest FAIL
/green-minimal   → Agent, unit_converter/ 최소 구현, PASS
/golden-master   → Agent, 출력 계약 고정 (boundary)
/refactor-smell  → Ask, 스멜 표
/refactor-safe   → Agent, 스멜 1개, Budget 준수
```

## Dual-Track

| Track | Layer | 경로 | Mock |
|-------|-------|------|------|
| B — Logic | domain | `tests/domain/` | 금지 |
| A — Boundary | app/cli | `tests/boundary/` | 허용 |

## P0 Test ID (필수 완료)

**Domain:** D-CNV-01, D-CNV-02, D-CNV-03  
**Boundary:** U-IN-01, U-IN-02, U-IN-03, U-OUT-01

## RED 스켈레톤 템플릿

```python
def test_d_cnv_01_one_feet_to_meter(conversion_ratios):
    # Given: 1 feet
    # When: to_meter(1.0, "feet", registry)
    # Then: ≈ 0.3048 m (FLOAT_EPS)
    pytest.fail("RED: D-CNV-01 — 구현 없음, 의도적 실패")
```

## 변환 공식

```
meter_value = input_value / ratio[source_unit]
result[unit] = meter_value * ratio[unit]
```

ratio는 meter=1.0 기준 (feet=3.28084, yard=1.09361).
