# /refactor-safe — REFACTOR ⑧ 안전 실행 (Agent)

**ARRR:** R — Refine  
**모드:** Agent  
**브랜치:** `refactoring`

## 사용법

```
/refactor-safe
Phase: refactor | Layer: domain | Track: Logic
스멜 1개 (P0): Duplicated Code — unit별 분기
대상: unit_converter/domain/converter.py
Budget: 파일 1 · 메서드 ≤2
원칙: 입출력·예외·Golden 계약 불변, assert 완화 금지
완료: pytest 전체 PASS + golden matched
```

## 금지

- 기능 추가 · 버그 수정
- 외부 계약(메시지·출력 형식) 변경
- Change Budget 초과
