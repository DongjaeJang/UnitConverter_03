"""pytest 픽스처 — 로직 없음, 변환 비율·입력 SSOT만.

SSOT: docs/PRD.md §9
"""

import pytest

# --- 변환 비율 (meter = 1.0 기준) ---
METER_TO_FEET: float = 3.28084
METER_TO_YARD: float = 1.09361

DEFAULT_UNITS: dict[str, float] = {
    "meter": 1.0,
    "feet": METER_TO_FEET,
    "yard": METER_TO_YARD,
}

# --- 부동소수 비교 ---
FLOAT_EPS: float = 1e-4

# --- 기본 시나리오 (FR-01, FR-02) ---
SAMPLE_INPUT: str = "meter:2.5"
SAMPLE_VALUE: float = 2.5
SAMPLE_UNIT: str = "meter"

# D-CNV-02 Then (5자리)
EXPECTED_FEET_2_5M: float = 8.20210
EXPECTED_YARD_2_5M: float = 2.73403

# D-CNV-01 Then
ONE_FEET_IN_METERS: float = 1.0 / METER_TO_FEET  # ≈ 0.3048


@pytest.fixture
def conversion_ratios() -> dict[str, float]:
    """기본 3단위 비율 — registry 초기화용."""
    return dict(DEFAULT_UNITS)


@pytest.fixture
def sample_input() -> str:
    """FR-01 기본 입력."""
    return SAMPLE_INPUT
