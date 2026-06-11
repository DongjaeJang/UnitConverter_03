# SPEC — 설계 문서만

UnitConverter_14 **SPEC 단계**. **프로덕션·테스트 코드 작성 금지.**

---

## 필수 선언

**응답 첫 줄:**

```
Phase: spec
```

---

## 허용

- `docs/*.md` 작성·수정 (`PRD.md`, `ARCHITECTURE.md`)
- `Report/*.md` 작성·수정
- `.cursor/rules/`, `.cursor/skills/`, `.cursor/commands/` 정의
- `pyproject.toml`, `tests/conftest.py`, `.gitignore` (Harness)
- 레거시 `UnitConverter.py` **분석만** (수정 ❌)

## 금지

| 금지 | 대상 |
|------|------|
| 구현 | `unit_converter/`, `converter.py`, `validator.py` |
| 테스트 | `tests/test_*.py` |
| RED 우회 | SPEC에서 pytest·구현 선행 |

## SSOT 문서

| 문서 | 내용 |
|------|------|
| `docs/PRD.md` | FR/NFR · C2C · Dual-Track RED 설계표 |
| `docs/ARCHITECTURE.md` | REFACTOR 목표 패키지 · ECB |
| `Report/01.REPORT.md` | 레거시 Gap 분석 |

## 커밋

`[SPEC] …` — 문서·Cursor 설정·Harness만.
