# /red-test-plan — RED ③ 설계표 (Ask)

**ARRR:** A — Ask  
**모드:** Ask (코드·파일 생성 금지)  
**브랜치:** `red` (설계는 spec에서 선행 가능)

## 사용법

```
/red-test-plan
Phase: red | Layer: domain | Track: Logic
이번 RED 묶음: D-CNV-01 (FR-02)
(표 4블록 작성, tests/·unit_converter/ 만들지 마)
```

## 출력 형식 (4블록)

### 1. Test ID · PRD 추적

| Test ID | PRD | Layer | Track |
|---------|-----|-------|-------|

### 2. Given / When / Then

| Given | When | Then |
|-------|------|------|

### 3. Invariant · SSOT

- 비율: `tests/conftest.py` 상수 인용
- 부동소수: `FLOAT_EPS`

### 4. Expected RED Failure

- `pytest.fail("RED: D-CNV-01 — 구현 없음")` 예상

## 참고 SSOT

- `docs/PRD.md` §8 Dual-Track RED 설계표
- C2C: `docs/PRD.md` §7
