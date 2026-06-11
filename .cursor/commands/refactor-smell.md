# /refactor-smell — REFACTOR ⑦ 스멜 탐지 (Ask)

**ARRR:** R — Refine  
**모드:** Ask (코드 수정 금지)  
**브랜치:** `refactoring`

## 사용법

```
/refactor-smell
Phase: refactor | Scope: unit_converter/ tests/
전제: python -m pytest tests/ -v → 전부 PASS
스멜 표 작성 (P0/P1/P2), Change Budget 내 후보 1~3개 제안
```

## 스멜 체크리스트

| 스멜 | UnitConverter 예시 |
|------|-------------------|
| Duplicated Code | 단위별 if/elif (레거시) |
| Long Method | main() 혼재 |
| Magic Number | 3.28084 리터럴 |
| Feature Envy | cli가 변환 수식 직접 계산 |
| ECB 위반 | domain → app import |

## Change Budget

파일≤3 · 클래스≤1 · 메서드≤3
