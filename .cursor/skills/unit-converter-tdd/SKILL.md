---
name: unit-converter-tdd
description: UnitConverter_14 Dual-Track TDD (Track A Boundary, Track B Domain). Use for RED/GREEN/REFACTOR, pytest, OCP/SRP, U-*/D-* tests, unit_converter package, or when the user mentions SPEC phase rules.
---

# unit-converter-tdd

UnitConverter_14 **Dual-Track TDD** 절차 SSOT. `.cursor/rules/` · `docs/` 와 충돌 시 **RED 금지 규칙** 우선.

## 언제 사용

- TDD, RED/GREEN/REFACTOR, Track A/B, `U-*`/`D-*`, OCP/SRP, `unit_converter/` 언급
- `tests/` 또는 `UnitConverter.py` 수정 요청
- `/tdd-red` · `/tdd-green` Command 실행

## 시작 선언 (필수)

```
Phase: red|green|refactor | Track: A|B | Test ID: D-CNV-01 (또는 U-IN-01)
```

## Track A vs Track B

| | Track A — Boundary | Track B — Domain |
|--|-------------------|------------------|
| TC | `U-*` | `D-*` |
| 파일 | `tests/test_boundary.py` | `tests/test_domain.py` |
| Mock | 최소 | **금지** (순수 변환) |
| RED 순서 | **2번째** | **1번째** |

Test ID: [reference.md](reference.md)

## RED 단계 금지 규칙

- **RED 단계에서 구현 코드 작성 금지**
- **`pytest.fail("RED: ...")` 허용**
- **`skip` / `xfail` 금지**
- **1 RED 묶음 = 1 커밋**

### RED 절차

1. Test ID 확인 (`reference.md`)
2. `Phase: red | Track: … | Test ID: …` 선언
3. `tests/` only — AAA 주석 + `pytest.fail("RED: {ID} — …")`
4. `pytest` 실행 → **FAIL** 확인
5. 커밋: `[RED] D-CNV-01 …` (1 묶음 = 1 커밋)

### RED 금지

- `unit_converter/` · `converter.py` · `validator.py` 생성
- `UnitConverter.py` 리팩터 (GREEN 전)
- `skip` / `xfail` / 통과 더미 assert
- Track B Domain `@patch`

## GREEN / REFACTOR

| Phase | 코드 | 테스트 |
|-------|------|--------|
| GREEN | 최소 구현 (`converter.py`, `validator.py`, `UnitConverter.py`) | `pytest.fail` → assert |
| REFACTOR | `docs/ARCHITECTURE.md` 패키지 구조 | Phase 1 TC 회귀 Green |

REFACTOR 시 `Converter` 본체는 Phase 2에서도 **수정하지 않음** (OCP).

## Command

| Command | Phase |
|---------|-------|
| `/spec-only` | spec |
| `/tdd-red` | red |
| `/tdd-green` | green |

## 추가 자료

- [reference.md](reference.md) — Phase 1 10 TC · FR 요약
- `docs/PRD.md` — C2C · RED 설계표
- `docs/ARCHITECTURE.md` — REFACTOR 목표 패키지
- `.cursor/commands/tdd-red.md` — RED Command
