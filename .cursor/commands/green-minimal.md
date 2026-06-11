# /green-minimal — GREEN 최소 구현 (Agent)

**ARRR:** R — Respond  
**모드:** Agent  
**브랜치:** `green`

## 사용법

```
/green-minimal
Phase: green | Layer: domain | Track: Logic
RED 대상: D-CNV-01 (tests/test_domain.py)
1. RED 재확인 — pytest.fail 상태인지 실행
2. 루트 `converter.py` / `validator.py` + `UnitConverter.py` 에 최소 구현 (GREEN 단계 `unit_converter/` 패키지 금지)
3. 하드코딩·매직넘버 금지 → conftest SSOT 또는 registry
4. pytest.fail 제거 → 실제 assert
5. PASS 확인
금지: 이번 RED 묶음 외 ID 동시 해결, REFACTOR
```

## 원칙

- 1 RED 묶음 = 1 커밋
- 통과하는 **최소** 코드만
- ECB: domain은 app/cli import 금지

## 완료 보고

- PASS Test ID · 변경 파일 · 회귀 실패 시 즉시 수정
