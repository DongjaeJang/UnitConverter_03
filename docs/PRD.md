# UnitConverter_03 — PRD (Product Requirements Document)

| 항목 | 내용 |
|------|------|
| 프로젝트 | UnitConverter_03 |
| 버전 | 0.1 (초안) |
| 생성일 | 2026-06-11 |
| 근거 | [Report/01.REPORT.md](../Report/01.REPORT.md), [Report/02.REPORT.md](../Report/02.REPORT.md) |
| 세션 | **spec** — 분석·설계 · C2C · Harness · Cursor 체계 |

---

## 1. 개요

### 1.1 배경

길이 단위 변환 CLI는 단순해 보이지만, 레거시 시드(`UnitConverter.py`)는 단위 추가 시 `main()` 분기가 늘고, 파싱·변환·출력이 한 함수에 섞여 **OCP/SRP를 위반**한다. 비율이 하드코딩되어 **설정 외부화**와 **동적 단위 등록**을 막는다.

### 1.2 진짜 문제

> `unit:value` 형식 입력을 받아 전 단위로 변환할 때, **단위가 늘어날 때마다 기존 변환 로직을 수정**해야 하고, **입력 검증·출력 형식이 코드 곳곳에 흩어져** 테스트로 추적하기 어렵다.

### 1.3 이번 릴리스 목표 (P0)

PRD와 테스트로 **C2C 추적 가능**한 길이 변환 CLI를 재구현한다.

| 포함 (P0) | 설명 |
|-----------|------|
| FR-01~05 | 파싱, 전 단위 출력, 미지 단위·음수·형식 오류 |
| NFR-01 | OCP — 새 단위 추가 시 기존 변환기 비수정 |
| NFR-02 | SRP — Parser / Registry / Converter / Formatter 분리 |
| Domain TC | Track B — `D-CNV-*` |
| Boundary TC | Track A — `U-IN-*`, `U-OUT-01` (기본) |

| 배제 (P1 — new_features) | 설명 |
|--------------------------|------|
| EXT-01~03 | 설정 파일, 동적 등록, 출력 포맷 3종 |

### 1.4 주제 (1문장)

> **길이 단위 변환 CLI를 PRD·테스트와 추적 가능하게 재구현하고, OCP/SRP를 만족하는 모듈 구조로 단위 추가·검증·출력을 분리한다.**

---

## 2. R-G-I-O

| | 내용 |
|---|---|
| **R — Role** | 길이 단위를 변환해야 하는 CLI 사용자·개발자 |
| **G — Goal** | `unit:value` 입력 → **모든 등록 단위**로 정확히 변환 출력, 잘못된 입력은 명확히 거부 |
| **I — Input** | `"meter:2.5"`, `"feet:8.2"`, `"yard:1.0"` 등 `단위:숫자` 문자열 |
| **O — Output** | `{value} {source} = {result} {target}` 형식 줄 단위 출력 (기본 table) |

### 성공 기준 (테스트 씨앗)

| 조건 | 통과 | 실패 |
|------|------|------|
| `meter:2.5` | feet≈8.2021, yard≈2.7340 | 오차 초과 또는 단위 누락 |
| `cubit:1` (미등록) | 명확한 오류 | 변환 시도 또는 무응답 |
| `meter:-1` | 음수 거부 | 음수 변환 출력 |
| `meter` (콜론 없음) | 형식 오류 | 파싱 성공 |
| inch 추가 (NFR-01) | `converter.py` 등 핵심 변환기 **비수정** | if/elif 분기 추가 |

---

## 3. 비즈니스 규칙

### 3.1 변환 비율 (meter = 1.0 기준)

| 단위 | meter 대비 비율 | 비고 |
|------|-----------------|------|
| meter | 1.0 | 기준 단위 |
| feet | 3.28084 | `1 m = 3.28084 ft` |
| yard | 1.09361 | `1 m = 1.09361 yd` |

feet ↔ yard 변환은 **meter 경유**: `value_in_meter = value / ratio[source]`, `result = value_in_meter * ratio[target]`.

### 3.2 입력 형식

- 패턴: `{unit}:{value}` — 콜론 1개, `split(':', 1)` 사용
- `value`: 양의 실수 (`float`)
- `unit`: registry에 등록된 단위명 (소문자)

### 3.3 오류 조건

| 조건 | 기대 동작 |
|------|-----------|
| 콜론 없음 | 형식 오류 메시지 |
| 숫자 파싱 실패 | 숫자 오류 메시지 |
| 음수 | 거부 |
| 미등록 단위 | 미지 단위 오류 |
| 빈 입력 | 형식 오류 |

---

## 4. 기능 요구사항 (FR)

| ID | 요구 | Given | Then | 우선순위 |
|----|------|-------|------|----------|
| FR-01 | `meter:2.5` 파싱 | 유효 문자열 | `value=2.5`, `unit=meter` | P0 |
| FR-02 | 전 단위 출력 | meter 2.5 | feet≈8.2021, yard≈2.7340 | P0 |
| FR-03 | 미지 단위 | `cubit:1` (미등록) | 명확한 오류 | P0 |
| FR-04 | 음수 | `meter:-1` | 거부 / 예외 | P0 |
| FR-05 | 잘못된 형식 | `meter` / `abc` | 형식 오류 | P0 |

---

## 5. 비기능 요구사항 (NFR)

| ID | 요구 | 검증 방법 | 우선순위 |
|----|------|-----------|----------|
| NFR-01 | OCP | inch 추가 시 `converter.py` 핵심 로직 비수정 | P0 |
| NFR-02 | SRP | Parser / Registry / Converter / Formatter 4모듈 분리 | P0 |

---

## 6. 추가 요구사항 (EXT — P1)

| ID | 요구 | Given | Then | 우선순위 |
|----|------|-------|------|----------|
| EXT-01 | 설정 파일 | `units.json` | 비율 로드 | P1 |
| EXT-02 | 동적 등록 | `1 cubit = 0.4572 meter` | 즉시 변환 가능 | P1 |
| EXT-03 | 출력 포맷 | `--format json\|csv\|table` | 포맷별 검증 | P1 |

---

## 7. C2C 추적표 (PRD → Test ID)

| PRD ID | Test ID | Layer | Track | 상태 |
|--------|---------|-------|-------|------|
| FR-01 | D-CNV-02 (파싱+변환) | domain | B | spec |
| FR-02 | D-CNV-02, D-CNV-03 | domain | B | spec |
| FR-03 | U-IN-04 *(후속)* / D-REG-01 | boundary/domain | A/B | spec |
| FR-04 | U-IN-03 | boundary | A | spec |
| FR-05 | U-IN-01, U-IN-02 | boundary | A | spec |
| NFR-01 | D-REG-01 | domain | B | spec |
| NFR-02 | *(구조 리뷰)* | — | — | green+refactor |
| EXT-01 | D-CFG-01 | domain | B | new_features |
| EXT-02 | D-REG-01 | domain | B | new_features |
| EXT-03 | U-OUT-02 *(후속)* | boundary | A | new_features |

---

## 8. Dual-Track RED 설계표 (③ — 코드 없음)

### Track B — Domain / Logic

| Test ID | 대상 함수 | Given | Then (Expected) | Invariant |
|---------|-----------|-------|-----------------|-----------|
| D-CNV-01 | `to_meter` | 1 feet | 0.3048 m (±ε) | meter 기준 |
| D-CNV-02 | `convert_all` | 2.5 meter | feet=8.20210 (5자리) | registry 3단위 |
| D-CNV-03 | `convert_all` | feet→yard | meter 경유 일치 | 교차 검증 |
| D-CNV-04 | `convert_all` | 2.5 meter | yard=2.73403 (5자리) | ROUND_HALF_UP |
| D-REG-01 | `register` | cubit 0.4572 m | 변환 가능 | OCP |
| D-CFG-01 | `load_config` | 깨진 JSON | ConfigError | P1 |

### Track A — Boundary / CLI

| Test ID | Given | Then (Expected) | Expected RED |
|---------|-------|-----------------|--------------|
| U-IN-01 | `""` (빈 입력) | 형식 오류 메시지 | pytest.fail |
| U-IN-02 | `meter` (콜론 없음) | 형식 오류 | pytest.fail |
| U-IN-03 | `meter:-1` | 음수 거부 | pytest.fail |
| U-IN-04 | `mile:1` | unknown unit 오류 | pytest.fail |
| U-IN-05 | `:2.5` / `meter:` | 빈 토큰 형식 오류 | pytest.fail |
| U-OUT-01 | `meter:2.5` | stdout 2줄 (feet·yard, 소수 1자리) | pytest.fail |

---

## 9. SSOT 상수 (tests/conftest.py)

| 상수 | 값 | 용도 |
|------|-----|------|
| `METER_TO_FEET` | 3.28084 | 비율 SSOT |
| `METER_TO_YARD` | 1.09361 | 비율 SSOT |
| `FLOAT_EPS` | 1e-4 | 부동소수 비교 |
| `SAMPLE_INPUT` | `"meter:2.5"` | 기본 시나리오 |
| `EXPECTED_FEET_2_5M` | 8.20210 | D-CNV-02 Then |
| `EXPECTED_YARD_2_5M` | 2.73403 | D-CNV-02 Then (5자리) |

---

## 10. 참고 문서

| 문서 | 설명 |
|------|------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | 목표 패키지 구조 |
| [../Report/01.REPORT.md](../Report/01.REPORT.md) | 레거시 갭 분석 |
| [../Report/02.REPORT.md](../Report/02.REPORT.md) | spec 설계 보고서 |
