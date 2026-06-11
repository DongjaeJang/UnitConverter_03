"""Track B — Domain / Logic (Phase 1: D-CNV-01 ~ D-CNV-03)."""

import pytest


def test_d_cnv_01_to_meter_feet():
    # Given: 1 feet
    # When: to_meter("feet", 1)
    # Then: 0.3048 m (±ε)
    pytest.fail("RED: D-CNV-01 — 1 feet → 0.3048 m, 구현 없음")


def test_d_cnv_02_convert_all_feet():
    # Given: 2.5 meter
    # When: convert_all("meter", 2.5)
    # Then: 8.20210 ft (소수 5자리)
    pytest.fail("RED: D-CNV-02 — 2.5 m → 8.20210 ft, 구현 없음")


def test_d_cnv_03_feet_yard_consistency():
    # Given: 1 feet
    # When: convert_all("feet", 1) — yard 값이 meter 경유 결과와 일치
    # Then: meter 경유 yard와 일치
    pytest.fail("RED: D-CNV-03 — feet→yard meter 경유 일치, 구현 없음")
