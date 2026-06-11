# /red-skeleton — RED ④ 스켈레톤 (Agent)

**ARRR:** A — Ask (실행)  
**모드:** Agent  
**브랜치:** `red`  
**수정 범위:** `tests/`만

## 사용법

```
/red-skeleton
Phase: red | Layer: domain | Track: Logic
RED 대상: D-CNV-01 (tests/domain/test_converter.py)
1. Given/When/Then 주석 + pytest.fail("RED: D-CNV-01 — ...")
2. conftest.py 픽스처 사용 (conversion_ratios, sample_input)
3. unit_converter/ 수정 금지
4. pytest 실행 → FAIL 확인 보고
```

## Track B (Domain)

- 경로: `tests/domain/test_converter.py`
- import 대상: `unit_converter.domain.*` (ModuleNotFoundError 허용)

## Track A (Boundary)

- 경로: `tests/boundary/test_cli.py`
- Domain Mock 허용

## 완료 보고

- Test ID · FAIL 한 줄 · 변경 파일 (`tests/`만)
