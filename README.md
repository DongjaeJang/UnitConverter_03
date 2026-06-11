# UnitConverter_14

길이 단위 변환 CLI를 **PRD·테스트와 추적 가능(C2C)** 하게 재구현하는 프로젝트입니다.

![unit-converter](./unit-converter.jpg)

> **한 줄 요약:** `meter:2.5` 입력 → meter·feet·yard 전 단위 변환 출력, OCP/SRP를 만족하는 모듈 구조.

---

## 빠른 시작

```bash
# 가상환경
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# 개발 의존성
pip install -e ".[dev]"

# 레거시 시드 실행 (참고용)
python UnitConverter.py

# 테스트 (spec: 테스트 파일 없음 → 0 collected)
python -m pytest tests/ -v
```

---

## 요구사항 요약

| 구분 | 내용 |
|------|------|
| 입력 | `meter:2.5` 형식 |
| 기본 단위 | meter, feet, yard |
| 비율 | 1m = 3.28084ft = 1.09361yd (feet↔yard는 meter 경유) |
| 품질 | OCP, SRP, 입력 검증 (음수·형식·미지 단위) |
| 추가 (P1) | units.json, 동적 등록, `--format json\|csv\|table` |

상세: [docs/PRD.md](docs/PRD.md)

---

## ARRR ↔ Cursor Command (UnitConverter_09 방식)

| ARRR | 개발 활동 | Command | 모드 |
|------|-----------|---------|------|
| **준비** | SPEC 설계 | `/spec-only` | Agent |
| **A — Ask** | RED 실패 테스트 | `/tdd-red` | Agent |
| **R — Respond** | GREEN 최소 구현 | `/tdd-green` | Agent |
| **R — Refine** | REFACTOR | Skill + `.cursor/rules/unit-converter-refactor.mdc` | Agent |
| **R — Repeat** | 문서화 | Report · Prompting | Agent |

## 슬래시 Command 목록

| Command | Phase | 모드 |
|---------|-------|------|
| `/spec-only` | spec — 문서·Harness만 | Agent |
| `/tdd-red` | red — `pytest.fail` 스켈레톤 | Agent |
| `/tdd-green` | green — 최소 구현 | Agent |

## 브랜치 전략 (ARRR)

```
main → staging → spec → red → green → refactoring → new_features
```

| 브랜치 | ARRR | 수정 범위 |
|--------|------|-----------|
| `spec` | 준비 | docs, .cursor/, Harness |
| `red` | Ask=RED | `tests/`만 |
| `green` | Respond | `converter.py`/`validator.py`/`UnitConverter.py` + tests |
| `refactoring` | Refine | 구조 개선 (계약 불변) |
| `new_features` | Repeat | EXT-01~03 (각 RED 사이클) |

**현재 브랜치:** `spec` ✅

---

## 프로젝트 구조

```
UnitConverter_14/
├── .cursor/
│   ├── rules/                      # project · red · refactor
│   ├── commands/                   # spec-only · tdd-red · tdd-green
│   └── skills/unit-converter-tdd/  # SKILL.md + reference.md
├── docs/
│   ├── PRD.md                      # FR/NFR/C2C/RED 설계표
│   └── ARCHITECTURE.md             # 목표 패키지 구조
├── tests/
│   └── conftest.py                 # 비율·입력 SSOT (로직 없음)
├── Report/
│   ├── 01.REPORT.md                # 레거시 갭 분석
│   └── 02.REPORT.md                # spec 설계 완료
├── UnitConverter.py                # 레거시 시드 (참고)
├── pyproject.toml
└── README.md
```

`red` 이후 추가 예정:

```
converter.py             # green — Domain 임시 모듈
validator.py             # green — 입력 검증
tests/test_domain.py     # red — Track B
tests/test_boundary.py   # red — Track A
unit_converter/          # refactoring — 패키지 이전
```

---

## C2C 추적표 (요약)

| PRD | Test ID | Track |
|-----|---------|-------|
| FR-01~02 | D-CNV-01~04 | B |
| FR-04~05 | U-IN-01~05 | A |
| FR-02 출력 | U-OUT-01 | A |
| NFR-01 | D-REG-01 | B |
| EXT-01~03 | D-CFG-01, D-REG-01, U-OUT-02 | P1 |

전체: [docs/PRD.md §7](docs/PRD.md)

---

## ARRR 실습 순서 (복붙)

```
/spec-only              # spec — 문서·Cursor 설정만
/tdd-red                # red — pytest.fail 스켈레톤 (red 브랜치)
/tdd-green              # green — 최소 구현 (green 브랜치)
```

### RED 프롬프트 예시

**Track B — Domain**

```
/tdd-red
Phase: red | Track: B | Test ID: D-CNV-01
tests/test_domain.py에 pytest.fail 스켈레톤 작성
```

**Track A — Boundary**

```
/tdd-red
Phase: red | Track: A | Test ID: U-IN-01
tests/test_boundary.py에 pytest.fail 스켈레톤 작성
```

---

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | 제품 요구사항 · C2C · RED 설계표 |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | 목표 아키텍처 · ECB |
| [Report/01.REPORT.md](Report/01.REPORT.md) | 레거시 스멜 · PRD 갭 |
| [Report/02.REPORT.md](Report/02.REPORT.md) | spec 산출물 체크리스트 |

---

## 다음 단계

```bash
git checkout -b red
```

`/tdd-red`로 `D-CNV-01`부터 Track B 테스트 스켈레톤을 작성합니다.
