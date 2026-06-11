# UnitConverter_03

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

## ARRR ↔ Cursor 8계층

| ARRR | 개발 활동 | Command | 모드 |
|------|-----------|---------|------|
| **A — Ask** | RED 설계·스켈레톤 | `/red-test-plan` → `/red-skeleton` | Ask → Agent |
| **R — Respond** | GREEN·Golden | `/green-minimal` → `/golden-master` | Agent |
| **R — Refine** | REFACTOR | `/refactor-smell` → `/refactor-safe` | Ask → Agent |
| **R — Repeat** | 문서화 | Report · Prompting | Agent |

## 슬래시 Command 목록

| Command | ARRR | 모드 |
|---------|------|------|
| `/red-test-plan` | RED ③ 설계표 | Ask |
| `/red-skeleton` | RED ④ 스켈레톤 | Agent |
| `/green-minimal` | GREEN | Agent |
| `/golden-master` | Golden Master | Agent |
| `/refactor-smell` | REFACTOR ⑦ 스멜 | Ask |
| `/refactor-safe` | REFACTOR ⑧ 실행 | Agent |

## 브랜치 전략 (ARRR)

```
main → staging → spec → red → green → refactoring → new_features
```

| 브랜치 | ARRR | 수정 범위 |
|--------|------|-----------|
| `spec` | 준비 | docs, .cursor/, Harness |
| `red` | Ask=RED | `tests/`만 |
| `green` | Respond | `unit_converter/` + 해당 tests |
| `refactoring` | Refine | 구조 개선 (계약 불변) |
| `new_features` | Repeat | EXT-01~03 (각 RED 사이클) |

**현재 브랜치:** `spec` ✅

---

## 프로젝트 구조

```
UnitConverter_03/
├── .cursor/
│   ├── rules/unit-converter.mdc    # ARRR·브랜치·C2C 헌법
│   ├── commands/                   # 슬래시 Command 6종
│   └── skills/unit-converter-tdd/  # TDD 절차 Skill
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
unit_converter/          # green — domain/app/infrastructure/cli
tests/domain/            # red — Track B
tests/boundary/          # red — Track A
tests/golden/            # green — Golden Master
```

---

## C2C 추적표 (요약)

| PRD | Test ID | Track |
|-----|---------|-------|
| FR-01~02 | D-CNV-01~03 | B |
| FR-04~05 | U-IN-01~03 | A |
| FR-02 출력 | U-OUT-01 | A |
| NFR-01 | D-REG-01 | B |
| EXT-01~03 | D-CFG-01, D-REG-01, U-OUT-02 | P1 |

전체: [docs/PRD.md §7](docs/PRD.md)

---

## ARRR 실습 순서 (복붙)

```
/red-test-plan          # Ask — 설계표만
/red-skeleton           # Agent — pytest.fail 스켈레톤 (red 브랜치)
/green-minimal          # Agent — 최소 구현 (green 브랜치)
/golden-master          # Agent — Golden (PASS 후)
/refactor-smell         # Ask — 스멜 표
/refactor-safe          # Agent — 스멜 1개
```

### RED 설계 프롬프트 예시

**Track B — Domain**

```
/red-test-plan
Phase: red | Layer: domain | Track: Logic
이번 RED 묶음: D-CNV-01 (FR-02)
(표 4블록 작성, tests/·unit_converter/ 만들지 마)
```

**Track A — Boundary**

```
/red-test-plan
Phase: red | Layer: boundary | Track: UI
이번 RED 묶음: U-IN-01, U-IN-02 (FR-05)
(표 4블록 작성, tests/·unit_converter/ 만들지 마)
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

`/red-skeleton`으로 `D-CNV-01`부터 Track B 테스트 스켈레톤을 작성합니다.
