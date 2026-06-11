# /golden-master — Golden Master · Approval Test (Agent)

**ARRR:** R — Respond (⑥)  
**모드:** Agent  
**브랜치:** `green`  
**전제:** 대상 Test ID pytest PASS

## 사용법

```
/golden-master
Phase: green | Layer: boundary | Track: UI
대상: U-OUT-01
1. tests/_approval.py — assert_matches_golden(actual, relative)
2. tests/golden/u_out_01_meter_2_5.approved.txt 연결
3. UPDATE_GOLDEN=1 pytest → 기준 생성
4. UPDATE_GOLDEN 없이 matched 확인
```

## 규칙

- golden 수동 편집으로 통과 우회 금지
- 출력 포맷(줄 순서·공백) 고정

## Windows

```powershell
$env:UPDATE_GOLDEN=1; python -m pytest tests/boundary/test_cli.py::test_u_out_01 -v
python -m pytest tests/boundary/test_cli.py::test_u_out_01 -v
```
